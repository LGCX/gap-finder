#!/usr/bin/env python3
"""Federal Register ingest + deterministic triage for the gap-finder scout.

Stages (run in order):
    ingest   pull final rules from the FR API into SQLite
    filter   three-tier classification on title patterns
    triage   fetch rule text for `review` rows, extract RFA numbers, apply the A2 floor
    queue    write the surviving candidates to QUEUE.md for Claude to score

Nothing is ever deleted. Kills are recorded with the reason that killed them so the
filter can be audited for false negatives — a silent filter discarding the one good
idea is the failure mode that matters.
"""

import argparse, json, re, sqlite3, sys, time, urllib.parse, urllib.request
from pathlib import Path

DB = Path(__file__).parent / "data" / "rules.db"
API = "https://www.federalregister.gov/api/v1/documents.json"
UA = {"User-Agent": "gap-finder-scout/1.0 (research; contact via github.com/LGCX/gap-finder)"}

# Rule classes that structurally cannot produce a buyer with a budget line.
# Each entry is (label, pattern) so kills are auditable by class, not just "noise".
KILL = [
    ("airworthiness",   r"airworthiness directive"),
    ("airspace",        r"class [a-e] airspace|area navigation route|federal airway|"
                        r"prohibited area|restricted area|\bVOR\b|jet route"),
    ("waterway",        r"drawbridge|safety zone|security zone|anchorage ground|regulated navigation"),
    ("species",         r"endangered and threatened|critical habitat|marine mammal|"
                        r"migratory bird|fishery management|essential fish habitat"),
    ("state-plan",      r"air plan approval|operating permit program approval|"
                        r"state implementation plan|promulgation of state plan|regulatory program\b"),
    ("nuclear-cask",    r"spent fuel storage cask"),
    ("housekeeping",    r"technical amendment|correcting amendment|delegation of authority|"
                        r"privacy act of 1974|freedom of information act"),
]

# Removes an obligation rather than creating one. NOT a hard kill: a rescission can
# create a scramble (a safe harbour vanishing, a permitted thing becoming unpermitted).
DEPRIORITIZE = [
    ("deregulatory", r"rescind|rescission|revocation|removal of obsolete|reducing bureaucracy|"
                     r"obsolete or unnecessary|withdrawal of|delay of effective date"),
]

# Titles hide burden-reducing rules: 5 of 21 candidates on 2026-08-03 announced cost
# SAVINGS in their own economic analysis while carrying a neutral title. A rule that
# saves the regulated party money is a negative forcing function — B1 scores 1.
SAVINGS = re.compile(
    r"cost savings|savings of (?:approximately |about )?\$|will save|"
    r"decrease annually by|decrease in burden|reduction in burden", re.I)

# --- RFA extraction. Fail-open: no match means "stay in review", never "kill". ---
#
# Extraction is NOT reliable enough to classify on. Measured over 86 rules: only ~5%
# yielded a confident per-entity figure, and the single most common dollar match is
# UMRA boilerplate ("$100 million in 1995 dollars") that appears in nearly every rule
# and means nothing. So the job here is COMPRESSION, not decision — pull the two or
# three sentences that actually carry burden numbers and hand those to the scorer,
# instead of making it read a 20,000-line rule.
#
# The auto-kill survives only for unambiguous per-entity phrasings. It is safe because
# the asymmetry favours us: a kill needs a number BELOW the floor, while boilerplate
# and aggregate figures are large. Misreads fail to kill rather than killing wrongly.

BOILERPLATE = re.compile(
    r"\$100 million in 1995 dollars|\$100,000,000 or more|unfunded mandates reform|"
    r"section 202|executive order 12866|"
    # UMRA text appears as both "updated" and "adjusted" — matching only one leaked
    # pure boilerplate into the evidence of 3 of 21 rules on 2026-08-03.
    r"(?:updated|adjusted) annually for inflation|"
    # "regulatory review cost" is the cost of READING the rule, not complying with it.
    # It is small by definition and killed a live candidate on 2026-08-03 before this
    # exclusion existed — the kill audit log is what surfaced it.
    r"regulatory review cost|cost of reviewing|reviewing the rule", re.I)

COST_PATTERNS = [  # confident per-entity only — these may kill
    r"not exceed \$([\d,]+)(?:\.\d+)?\s*(?:annually|per year|per entity)",
    r"\$([\d,]+)(?:\.\d+)?\s*(?:annually |per year )?per (?:entity|respondent|small entity|firm|business|facility)",
    r"cost[s]? per entity[^.]{0,60}?\$([\d,]+)",
    r"per[- ]entity cost[^.]{0,60}?\$([\d,]+)",
]

# Sentences worth surfacing to the scorer. Broad on purpose — this only compresses.
EVIDENCE = re.compile(
    r"[^.]{0,130}?\$[\d,]+(?:\.\d+)?\s*(?:million|billion)?[^.]{0,110}?"
    r"(?:per (?:entity|respondent|firm|small|applicant|filing|petition|appeal|facility|year)|"
    r"annually|annualized|each year|burden hours?)[^.]{0,60}\.", re.I)
COUNT_PATTERNS = [
    r"(?:approximately|about|an estimated|estimated)\s+([\d,]{3,})\s+(?:small\s+)?"
    r"(?:entities|respondents|firms|businesses|participants|establishments|facilities|providers)",
]

A2_FLOOR = 2400  # rubric A2 wants $200+/mo; a burden ceiling below this cannot support it


def db():
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute("""CREATE TABLE IF NOT EXISTS rules (
        document_number TEXT PRIMARY KEY, title TEXT, agencies TEXT,
        effective_on TEXT, publication_date TEXT, html_url TEXT, raw_text_url TEXT,
        tier TEXT, kill_reason TEXT, cost_ceiling INTEGER, entity_count INTEGER,
        evidence TEXT, triaged_at TEXT)""")
    if "evidence" not in {r[1] for r in c.execute("PRAGMA table_info(rules)")}:
        c.execute("ALTER TABLE rules ADD COLUMN evidence TEXT")
    return c


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if i == tries - 1:
                print(f"    fetch failed: {url[:80]} — {e}", file=sys.stderr)
                return None
            time.sleep(2 * (i + 1))


def ingest(since, eff_from):
    c, new, seen = db(), 0, 0
    q = {"conditions[type][]": "RULE", "conditions[publication_date][gte]": since,
         "conditions[effective_date][gte]": eff_from, "per_page": "100", "order": "newest"}
    url = API + "?" + urllib.parse.urlencode(q) + "".join(
        "&fields[]=" + f for f in ("document_number", "title", "agencies", "effective_on",
                                   "publication_date", "html_url", "raw_text_url"))
    while url:
        body = get(url)
        if not body:
            break
        d = json.loads(body)
        for r in d.get("results", []):
            seen += 1
            ags = "/".join(a.get("name") or a.get("raw_name", "") for a in (r.get("agencies") or []))
            cur = c.execute("INSERT OR IGNORE INTO rules (document_number,title,agencies,"
                            "effective_on,publication_date,html_url,raw_text_url) VALUES (?,?,?,?,?,?,?)",
                            (r["document_number"], r.get("title"), ags, r.get("effective_on"),
                             r.get("publication_date"), r.get("html_url"), r.get("raw_text_url")))
            new += cur.rowcount
        c.commit()
        url = d.get("next_page_url")
        if url:
            time.sleep(0.4)
    print(f"ingest: {seen} rules seen, {new} new")


def classify():
    c = db()
    counts = {}
    for dn, title in c.execute("SELECT document_number,title FROM rules WHERE tier IS NULL"):
        t, tier, reason = title or "", "review", None
        for label, pat in KILL:
            if re.search(pat, t, re.I):
                tier, reason = "kill", label
                break
        if tier == "review":
            for label, pat in DEPRIORITIZE:
                if re.search(pat, t, re.I):
                    tier, reason = "deprioritize", label
                    break
        c.execute("UPDATE rules SET tier=?,kill_reason=? WHERE document_number=?", (tier, reason, dn))
        counts[reason or "review"] = counts.get(reason or "review", 0) + 1
    c.commit()
    total = sum(counts.values())
    print(f"filter: classified {total}")
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"    {k:16} {v:5}  {v/total*100:4.1f}%" if total else "")


def num(s):
    return int(s.replace(",", ""))


def triage(limit):
    c = db()
    rows = c.execute("SELECT document_number,raw_text_url,title FROM rules "
                     "WHERE tier='review' AND triaged_at IS NULL AND raw_text_url IS NOT NULL "
                     "LIMIT ?", (limit,)).fetchall()
    print(f"triage: {len(rows)} rules to read")
    killed = found = 0
    for i, (dn, url, title) in enumerate(rows, 1):
        txt = get(url)
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        if not txt:
            c.execute("UPDATE rules SET triaged_at=? WHERE document_number=?", (now, dn))
            continue
        flat = " ".join(txt.split())
        cost = count = None
        for p in COST_PATTERNS:
            m = re.search(p, flat, re.I)
            # Check a window around the match, not just the span — the disqualifying
            # phrase ("regulatory review cost is $341 per entity") sits before the money.
            if m and not BOILERPLATE.search(flat[max(0, m.start() - 140):m.end() + 60]):
                cost = num(m.group(1)); break
        for p in COUNT_PATTERNS:
            m = re.search(p, flat, re.I)
            if m:
                count = num(m.group(1)); break
        ev = [" ".join(s.split()) for s in EVIDENCE.findall(flat)]
        ev = [s for s in ev if not BOILERPLATE.search(s)][:3]
        if ev:
            found += 1
        tier, reason = "review", None
        if cost is not None and cost < A2_FLOOR:
            tier, reason = "kill", f"A2: RFA burden ceiling ${cost:,}/yr < ${A2_FLOOR:,} floor"
            killed += 1
        elif ev and all(SAVINGS.search(s) for s in ev):
            # Every burden sentence it states is a saving — the rule reduces obligations.
            tier, reason = "deprioritize", "savings: economic analysis reports only cost savings"
        c.execute("UPDATE rules SET tier=?,kill_reason=COALESCE(?,kill_reason),"
                  "cost_ceiling=?,entity_count=?,evidence=?,triaged_at=? WHERE document_number=?",
                  (tier, reason, cost, count, " ⏐ ".join(ev), now, dn))
        if i % 10 == 0:
            c.commit(); print(f"    {i}/{len(rows)}")
        time.sleep(0.3)
    c.commit()
    print(f"triage: burden evidence extracted for {found}/{len(rows)}, "
          f"killed {killed} on the A2 floor")


def queue(out):
    c = db()
    rows = c.execute("SELECT effective_on,agencies,title,cost_ceiling,entity_count,html_url,evidence "
                     "FROM rules WHERE tier='review' AND triaged_at IS NOT NULL "
                     "ORDER BY evidence='' , effective_on").fetchall()
    tiers = dict(c.execute("SELECT tier,COUNT(*) FROM rules GROUP BY tier").fetchall())
    withev = sum(1 for r in rows if r[6])
    lines = ["# Review Queue", "",
             "Auto-generated by `scout.py queue`. These survived deterministic filtering.",
             "Claude scores these against `RUBRIC.md` — everything upstream is arithmetic.",
             "Rules carrying extracted burden evidence sort first; read those before the rest.", "",
             f"Corpus: {sum(tiers.values())} rules — "
             + " · ".join(f"{k} {v}" for k, v in sorted(tiers.items()))
             + f" · {withev}/{len(rows)} of the queue carry burden evidence", "",
             "| Effective | Agency | Rule | $/entity/yr | Entities |", "|---|---|---|---|---|"]
    for eff, ag, title, cost, cnt, url, _ in rows:
        lines.append(f"| {eff or '—'} | {(ag or '')[:28]} | [{(title or '')[:70]}]({url}) | "
                     f"{f'${cost:,}' if cost else '—'} | {f'{cnt:,}' if cnt else '—'} |")
    lines += ["", "## Extracted burden evidence", "",
              "Sentences carrying cost or burden figures, boilerplate stripped.",
              "This is the compression that matters: read these instead of the rule.", ""]
    for eff, ag, title, cost, cnt, url, ev in rows:
        if not ev:
            continue
        lines.append(f"**[{(title or '')[:80]}]({url})** — eff. {eff or '—'}")
        for s in ev.split(" ⏐ "):
            lines.append(f"> {s}")
        lines.append("")
    Path(out).write_text("\n".join(lines) + "\n")
    print(f"queue: {len(rows)} candidates → {out}")


def selftest():
    def tier_of(title):
        for label, pat in KILL:
            if re.search(pat, title, re.I): return "kill", label
        for label, pat in DEPRIORITIZE:
            if re.search(pat, title, re.I): return "deprioritize", label
        return "review", None

    def cost_of(text):
        flat = " ".join(text.split())
        for p in COST_PATTERNS:
            m = re.search(p, flat, re.I)
            if m and not BOILERPLATE.search(flat[max(0, m.start() - 140):m.end() + 60]):
                return num(m.group(1))
        return None

    assert tier_of("Airworthiness Directives; Boeing Airplanes")[0] == "kill"
    assert tier_of("Amendment of Class D Airspace Over Groton, CT")[0] == "kill"
    assert tier_of("Rescission of Outdated Veterans Choice Program Regulations")[0] == "deprioritize"
    assert tier_of("Modernization of the Nation's Alerting Systems")[0] == "review"

    # Regression: regulatory-review cost is the cost of READING the rule. It killed a
    # live candidate on 2026-08-03 because the exclusion only checked the matched span.
    assert cost_of("According to the 2022 Economic Census, all Specialty Hospitals, "
                   "the regulatory review cost is $341 per entity.") is None
    # UMRA boilerplate must never register as a burden figure.
    assert cost_of("any rule whose mandates require spending in any 1 year of "
                   "$100 million in 1995 dollars, updated annually for inflation.") is None
    # A real per-entity ceiling must still be caught.
    assert cost_of("costs per entity will not exceed $1,000 annually, based on 10 hours "
                   "of labor per entity per year.") == 1000
    # UMRA also appears as "adjusted", not just "updated" — leaked into 3 of 21 rules.
    assert cost_of("of $100,000,000 or more (adjusted annually for inflation) in any one "
                   "year per entity.") is None
    # A rule whose own analysis reports only savings is a negative forcing function.
    assert SAVINGS.search("resulting in a savings of approximately $17.4 million per year")
    assert SAVINGS.search("annualized cost savings of $12.47 million")
    assert not SAVINGS.search("219 such appeals would cost approximately $135,025 annually")
    print("selftest: ok")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("selftest")
    i = s.add_parser("ingest"); i.add_argument("--since", default="2026-01-01"); i.add_argument("--effective-from", default="2026-08-10")
    s.add_parser("filter")
    t = s.add_parser("triage"); t.add_argument("--limit", type=int, default=60)
    q = s.add_parser("queue"); q.add_argument("--out", default=str(Path(__file__).parent / "QUEUE.md"))
    a = p.parse_args()
    if a.cmd == "selftest": selftest()
    elif a.cmd == "ingest": ingest(a.since, a.effective_from)
    elif a.cmd == "filter": classify()
    elif a.cmd == "triage": triage(a.limit)
    elif a.cmd == "queue": queue(a.out)
