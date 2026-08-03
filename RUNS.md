# Run Log

Append one block per run. Newest at top. Keeps consecutive runs from
re-treading the same ground within a day.

Format:

```
## YYYY-MM-DD HH:MM
Swept: <sources, from SOURCES.md>
Generated: N | Passed gates: M | Scored ≥4.0: K
New ideas: [[slug]], [[slug]]
Killed: [[slug]] (G1 — Vanta ships this)
Note: <anything the next run should know — a thread to pull, a dead end, a date to watch>
```

---

## 2026-08-03 07:40 UTC — built `scout.py`, ran the full pipeline
Swept: Federal Register API, publication_date ≥ 2026-01-01, effective_date ≥ 2026-08-10
Corpus: **183 rules** → kill 82 · deprioritize 16 · **review 85** · 21/85 carry burden evidence
Generated: 0 new scored ideas this pass — the pipeline was the deliverable
Output: [QUEUE.md](QUEUE.md), regenerate with `python3 scout.py queue`

Note: **Throughput problem addressed.** Prior runs hand-examined ~15 rules out of 160; the
pipeline now classifies the whole corpus and surfaces only what survives.

Pipeline: `ingest` (FR API → SQLite) → `filter` (title tiers) → `triage` (fetch text, extract
burden sentences, apply A2 floor) → `queue` (markdown for scoring). `python3 scout.py selftest`
covers the filter logic.

(1) **Structural kill rate 45%** (82/183), and it is honest volume, not judgment:
airspace 33 · airworthiness 24 · species 10 · state-plan 8 · waterway 3 · nuclear-cask 2 ·
housekeeping 1. Plus 16 deprioritized as deregulatory — kept, not killed, because a rescission
can create a scramble (a safe harbour vanishing, a permitted thing becoming unpermitted).

(2) **Per-entity cost extraction is NOT reliably deterministic — this was the day's real
lesson.** First attempt hit 4/86 (4.7%). The single most common dollar figure in any rule is
UMRA boilerplate, "$100 million in 1995 dollars, updated annually for inflation", which is
present nearly everywhere and means nothing. Rewrote the stage from *classification* to
*compression*: extract the 2-3 sentences carrying burden figures and hand those to the scorer.
Evidence coverage went 4/86 → 21/85. The scorer now reads ~200 words instead of a
19,537-line rule. **Automate the compression, not the judgement.**

(3) **The kill audit log caught a false positive, which is the whole reason it exists.**
The A2 auto-kill killed *Medicare IRF PPS* on "$341 per entity" — but that was the
**regulatory review cost**, the cost of *reading* the rule, not of complying with it.
Two bugs behind it: no exclusion for that phrase, and the exclusion check only looked at the
matched span while the disqualifying words sit ~60 chars earlier. Both fixed, rule reinstated,
and both cases are now asserted in `selftest`. **Never let a filter delete — log the reason and
sample the kills.** A silent filter discarding the one good idea is the failure mode that matters.

(4) **A verified number replaced a derived one.** Evidence extraction surfaced the EAS rule's
own cost model — `25,800 entities x 10 hours x $65 ...` — replacing my hand-derived
"~21,000 UNVERIFIED" in [[eas-cybersecurity-risk-plan-certification]]. Only one A2 kill now
stands, and it was independently confirmed by hand earlier.

(5) NEXT: score the 21 evidence-carrying rows in QUEUE.md against RUBRIC.md before touching
anything else. Flagged on sight, unscored: **EPCRA Hazardous Chemical Inventory Reporting**
(eff. 2026-08-21, conforming Tier II to OSHA HazCom 2024) — buyer is any facility storing
hazardous chemicals above threshold, which is a large unglamorous population.

(6) STILL OPEN: this only covers the regulatory leg. The revealed-pain sources — reviews, job
postings, forum threads — have no ingester and remain hand-swept, and run 06:41 argued they
deserve the rotation weight. That is the next thing to build.

## 2026-08-03 07:05 UTC — first LOCAL run (partial, run inline to validate tooling)
Swept: Federal Register (API scan) only — **not a full spec run**, 1 source instead of 3–4
Generated: 2 worked + ~10 surveyed and set aside | Passed gates: 0 | Scored ≥4.0: 0
New ideas: none — **null run**
Killed: [[eas-cybersecurity-risk-plan-certification]] (G3 +A2/B4 — FCC caps total burden at ≤$1,000/entity/yr) · [[dhs-fixed-admission-period-i539]] (G7 +G3 — I-539 advice is unauthorized practice of law)

Note: **TOOLING CONFIRMED.** `curl` and the Federal Register JSON API both work locally.
API returned the complete set — 475 final rules since 2026-06-15, 160 with future effective
dates — versus the cloud run's search-roulette. This is the upgrade that justified going local.

(1) **Read the Regulatory Flexibility Analysis before anything else.** The EAS kill came
straight out of it: the FCC's own "not exceed $1,000 annually" line ended the idea in one
sentence, no competitor research needed. The RFA gives the agency's own estimate of what
compliance costs — which is a hard ceiling on what anyone can charge. Cheapest kill available.

(2) **New pattern for G8, worth encoding:** when a burdened population is obviously unserved,
find the *legal* reason before assuming oversight. I-539 has no vendor for the filer because
advising on it is unauthorized practice of law — the same wall that stops universities helping
stops a solo founder. "Obligated party has no vendor" is necessary, not sufficient.

(3) **SIGNAL/NOISE, quantified:** of 100 rules pulled, 47 were pure noise (airworthiness
directives, airspace amendments, endangered species, air-plan approvals) and **6 of the
remaining 53 were explicitly deregulatory** — "Reducing Bureaucracy and Burden", "Rescinding",
"Removal of Obsolete", "Revocation". This rulemaking window is stripping obligations more than
creating them. If that holds across the next few scans, the Federal Register is structurally
low-yield right now and the revealed-pain tier deserves the rotation weight instead.

(4) **Federal Register HTML is bot-blocked** (302 → unblock.federalregister.gov). WebFetch on a
document URL fails. Use the API `raw_text_url`; `curl` retrieves full text fine.

(5) Competitor pricing check ran as designed: Terra Dotta / Sunapsis publish no pricing —
demo-gated, enterprise sales-led. Per the job spec that is itself the finding (favourable C2),
though it did not save either candidate.

(6) NEXT RUN: this run swept only one source. Rotate to the untouched ones — enforcement
actions, procurement (SAM.gov), vertical app-store reviews, state licensing boards — and start
the next Federal Register scan from publication_date ≥ 2026-08-03.

## 2026-08-03 06:41 UTC
Swept: Federal Register (final rules 0–18mo) · Standards bodies & accreditation schemes · Job postings (attempted, blocked) · Vendor EOL / sunset announcements
Generated: 8 | Passed gates: 0 | Scored ≥4.0: 0
New ideas: none — **null run**
Killed: [[dmepos-annual-survey-readiness]] (G2 — The Compliance Team ships the readiness portal itself) · [[hfc-leak-repair-recordkeeping]] (G1 — Trakref/Fexa, Accruent Verisae/Fortive, ServiceChannel, SafetyCulture) · [[qmsr-iso-13485-transition]] (G1 — Greenlight Guru, Qualio $63M+) · [[sqf-edition-10-readiness]] (G1 — SafetyChain $73M; +B2, not mandatory before 2027-01-02) · [[mcs-installer-scheme-evidence]] (G2 — Payaca already ships MCS workflow) · [[cfpb-1071-small-business-lending-register]] (B2 — compliance deferred to 2028, threshold cut 100→1,000) · [[tsca-pfas-8a7-reporting]] (B4/E2 — one-time lookback filing) · [[cms-6225-provider-based-attestation]] (G2 — CMS is building the submission system itself)

Note: **First run — index was empty, so no dedupe was possible; everything here is new ground.**
(1) TOOLING: WebFetch and direct curl are 403-blocked by egress policy in this environment — only WebSearch works. federalregister.gov, cms.gov, and most primary sources cannot be read directly, so several claims rest on secondary law-firm/trade coverage rather than the primary text. **Test WebFetch at the start of the next run**; if still blocked, drop the job-postings and Upwork/Fiverr sources from rotation entirely (they need crawling) and lean on sources that surface through search.
(2) PATTERN, worth generalising: five of eight kills were the *same shape* — a real, already-in-force rule whose compliance-software category is already owned, either by a funded vendor or by the body that runs the certification. **A new in-force rule is not a gap; it is an advertisement that a market exists.** Bias the next sweeps toward rules where the buyer has no software vendor at all, or where the obligated party is not the one the existing vendors sell to.
(3) SEGMENT WATCH: health/CMS and environment/EPA are now mined for this cycle — 5 of 8 candidates. Next run should deliberately rotate to DOL / DOT / FCC dockets or state licensing boards.
(4) DATES TO WATCH: 2026-10-13 TSCA PFAS filing (confirms/denies the "one-time event" read) · 2027-01-02 SQF Ed.10 mandatory audits · 2027-Q1 re-check CFPB 1071 per [[cfpb-1071-small-business-lending-register]] · DMEPOS enrollment moratorium (Feb 2026, 6 months) expiry — watch whether the supplier pool actually shrinks.
(5) UNVERIFIED and needs a primary source before reuse: the "79,000+ DMEPOS suppliers approved nationwide" count. It came through secondary coverage, not a CMS enrollment table.
