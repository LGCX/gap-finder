---
slug: fdta-emma-municipal-disclosure-standards
date_found: 2026-08-03
last_reviewed: 2026-08-03
status: DEAD
score: null
failed_gate: B2 (refuted, batch 1)
buyer: Municipal securities issuers — cities, counties, school districts, special districts
segment: muni-finance
forcing_function: statute
in_force_date: unknown — Phase 2 not proposed, statutory outer bound 2028-10-01
watch_date: 2027-06-30
source_found: scout.py — Federal Register API, Treasury/OCC 2026 FDTA joint standards
---

# FDTA Machine-Readable Disclosure for Small Municipal Issuers

**One line:** The Financial Data Transparency Act forces municipal issuers to file EMMA
disclosures in structured machine-readable form; the SEC must set the standard by December 2026,
with compliance expected in early 2027.

## Job to be done
Municipal issuers file offering documents and continuing disclosures to the MSRB's EMMA system.
Today that is PDFs. Under FDTA it becomes structured, machine-readable data — a format change for
every issuer, most of whom are small governments with a part-time finance officer.

## Forcing function
Statutory (FDTA, signed Dec 2022). Joint agency data standards rule finalized June 2026, effective
**2026-10-01**. The SEC must establish EMMA submission standards **by December 2026**, compliance
expected early 2027.
Sources: [GFOA](https://www.gfoa.org/fdta) · [Data Foundation fact sheet](https://datafoundation.org/news/financial-data-transparency-hub/863/863-FACT-SHEET-Financial-Data-Transparency-Act-FDTA-Final-Rule) · [GAO-26-108420](https://files.gao.gov/reports/GAO-26-108420/index.html).

## Why the buyer is interesting
GFOA states plainly that the law **"does not provide any financial assistance with transition costs
to hire consultants, reconfigure financial systems, or implement new software"**, and warns a broad
implementation "could overburden municipal issuers and borrowers who may already face limited
resources and staff bandwidth."

An unfunded mandate landing on thousands of small governments with no budget line and no vendor is
close to the ideal shape. Buyer count is **`UNVERIFIED`** — needs a primary MSRB/EMMA issuer count
before this is scored.

## Why PARK rather than BUILD

**The standard does not exist yet.** The SEC has not published the EMMA taxonomy. There is nothing
to build against, and the FDTA explicitly permits agencies to **scale requirements down for smaller
entities** — which could remove the buyer entirely before the deadline. Rubric B2 is doing its job:
already-in-force beats pending, and this is pending.

Building now means guessing the schema. Waiting means arriving with everyone else — but the
schema publication is the starting gun, and it is dated.

## Watch trigger — 2026-12-31
Re-open when the SEC publishes the EMMA data standard. At that point check, in order:
1. Did small-issuer scaling relief gut the obligated population?
2. What is the actual issuer count subject to it? (primary MSRB source)
3. Did the existing muni-disclosure vendors (BondLink, DisclosureNet, MuniOS, Munilytics) ship it
   first — and at what price? All `UNVERIFIED`, none checked yet.

## Links
[[epcra-tier-ii-hazcom-2024-conformity]] — same run.

## History
- 2026-08-03 — surfaced by `scout.py`; PARKed pending SEC EMMA standard, watch 2026-12-31


## Pressure test — batch 1, 2026-08-03: **REFUTED**

**No buyer, no spec, no deadline.** The December 2026 date in my premise was stale — it
assumed FDTA Phase 1 landed Dec 2024. It landed **18 months late**, sliding the municipal
rule to a statutory outer bound of **2028-10-01** with no compliance date at all.

**1. There is nothing to build against.** Phase 1 joint rule is final ([91 FR 38246](https://www.federalregister.gov/documents/2026/06/25/2026-12787), effective 2026-10-01)
but says verbatim: *"The effective date for the final joint rule will not change any
reporting requirements without further action by the Agencies."* **No Phase 2 municipal rule
has been proposed**, and it is absent from the SEC's July 2026 regulatory agenda. The agencies
**expressly declined to establish accounting or reporting taxonomies** (final rule §II.E).
Realistic compliance: **≥2029**.

GFOA's own warning: *"Be aware vendors are promoting products based on taxonomies that have
not yet been endorsed by federal regulations."* Anyone building this today is guessing.

**2. The city does not hold the pen.** MSRB formally supports third-party filing: issuers
"designate a single party as their agent… and agents can act on behalf of multiple issuers,"
with a dedicated dissemination-agent workflow. The buyer is a **dissemination agent, municipal
advisor, or bond counsel** — not a municipality. That is a different product: multi-tenant
agent tooling, sold to a few hundred firms, not software for 50,000 governments.

**3. The tagging layer is already commoditised and free.** The XBRL US GRIP/ACFR taxonomy is
[royalty-free](https://xbrl.us/acfr/), **GASB has taken over taxonomy development** under its
Voluntary Digital Financial Reporting initiative, and **EMMA filing itself is free**. Workiva,
DataTracks, IRIS and CoreFiling already sit on the XBRL US Standard Government Reporting
working group. Munilytics is defunct — its domain is parked and listed for $595.

**4. ~70% probability small-issuer relief guts it anyway.** The agencies *broadened* tailoring
authority in the final rule after comment; the statute requires scaling for small entities; and
a live **Tower Amendment** claim argues any SEC/MSRB standard must be **voluntary** for issuers,
still unresolved. Plus 10th Amendment and unfunded-mandate objections.

**Counts, for the record:** MSRB 2025 Fact Book reports 102,860 financial and 45,922 event
submissions in 2025 — **documents, not issuers**. GFOA cites 80,000+ affected entities and
50,000+ issuers. Distinct annual filers: `UNVERIFIED`; MSRB does not publish it.

**Re-open trigger (revised):** publication of an **SEC Phase 2 NPRM for municipal data
standards** in the Federal Register, or its appearance on the SEC reg-flex agenda. Check
**2027-06-30**, then semiannually. Secondary trigger: GASB's VDFR taxonomy moving from
voluntary to mandatory.

### Price ceiling — the A2 kill, from XBRL US's own letter to the SEC

XBRL US told the SEC (2025-10-11) that for this job **open-source tools are free, commercial
tools run $1,000–$1,500/year, and an LEI costs ~$39/year**.
[Source](https://www.xbrl.org/news/xbrl-us-responds-to-sec-on-digital-standards-for-municipal-bond-reporting/)

$1,000–1,500/yr is **$83–125/month** — below the $200–500/month floor rubric A2 requires, and
that is the *commercial* number, competing against free. **A2 fails independently of everything
else.** Gravity's own marketing benchmarks the alternative at consultant fees of "$50,000 to
$200,000+ per year", which tells you the value is captured by advisory, not software.

### No machine-readable submission endpoint exists either

MSRB's EMMA revamp shipping in 2026 is **reorganisation, not ingestion** — natural-language
search, issuer-centric pages, expanded alerts. MSRB's Chief Product Officer framed it explicitly
as "reorganizing this information," not new data sources, and the coverage makes no mention of
machine-readable submissions or APIs.
[Bond Buyer](https://www.bondbuyer.com/news/emma-website-revamp-coming-in-2026). MSRB has no rule
to build submission plumbing against, because the SEC muni rule is not proposed.

### Negative finding worth keeping

**No venture-funded FDTA-specific startup could be found** — every entrant is an existing XBRL
filing agent extending into government (IRIS Instant, Novaworks, EcoActive/Ez-XBRL), an existing
govtech finance platform bolting on FDTA messaging (Gravity/ClearGov, DebtBook, DFIN, Workiva,
Tyler), or free/open-source. Nobody owns this — and the market is right not to. Realistic issuer
compliance is **~2029–2030**; nearly every vendor page still advertises a stale "2027 deadline".

### Competitor sweep — the commoditisation is already shipped

**The decisive fact:** University of Michigan CLOSUP, working with DAC Bond, has shipped a
**free, open-source, MIT-licensed** converter turning ACFRs from Excel/Word into inline XBRL —
with a free hosted web version and 661 commits.
[github.com/closup/process-xbrl](https://github.com/closup/process-xbrl). A business whose
value is "we tag your ACFR" is competing with a university giving it away, on top of a
royalty-free taxonomy, against free EMMA filing. XBRL US CEO Campbell Pryde anchors small
local-government cost at **$500** — that is the number issuers will remember.

**Precedent, already live:** Florida has mandated XBRL for local government filings since FYs
ending on/after 2022-09-01 (HB 1073), with the **state paying for the tooling**. Michigan ran a
pilot. Where this has actually happened, the government funded it.

**No large incumbent has announced an FDTA product** — BondLink, MuniOS/ImageMaster, ICE,
Bloomberg, S&P, Tyler, OpenGov, Euna, DebtBook are all silent. That reads as a rational market
judging the rule non-binding until ~2028, not as an opening.
Shipping muni-XBRL today: **IRIS Carbon** (ACFR iXBRL with ML auto-tagging) and **Dinocrates**
(built Florida's taxonomy under state contract). **ClearGov + Gravity** (now merged) is the
closest positioning play — an FDTA-readiness narrative, but no shipping XBRL export.

**Premise corrections from the sweep:** Munilytics is defunct (domain parked at $595, operating
entity is a consulting firm). DisclosureNet is not a muni vendor — acquired by Certent, then
insightsoftware; it searches EDGAR/SEDAR/ASX. MuniOS is owned by ImageMaster, unrelated to the
Ipreo lineage. XBRL was **not** mandated by the joint rule at all; it is principles-based, with
format punted to agency rulemakings.

*Caveat: both verifying agents exhausted their web-search budgets. bloomberg.com, workiva.com,
gfoa.org, gasb.org and tylertech.com all 403 automated fetch. Tyler, OpenGov, Toppan Merrill and
DFIN warrant a second pass. Cells above sourced only via search index are flagged UNVERIFIED in
the agent transcripts.*

## History
- 2026-08-03 — surfaced by `scout.py`; PARKed pending SEC EMMA standard
- 2026-08-03 — **refuted in pressure-test batch 1**; DEAD on B2. Watch moved to 2027-06-30
