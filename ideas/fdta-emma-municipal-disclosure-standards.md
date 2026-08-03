---
slug: fdta-emma-municipal-disclosure-standards
date_found: 2026-08-03
last_reviewed: 2026-08-03
status: PARK
score: null
failed_gate: null
buyer: Municipal securities issuers — cities, counties, school districts, special districts
segment: muni-finance
forcing_function: statute
in_force_date: 2027-01-01
watch_date: 2026-12-31
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
