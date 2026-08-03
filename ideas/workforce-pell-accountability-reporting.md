---
slug: workforce-pell-accountability-reporting
date_found: 2026-08-03
last_reviewed: 2026-08-03
status: DEAD
score: null
failed_gate: G4 (+G3, G2, A1)
buyer: Title IV institutions offering Workforce Pell short-term programs
segment: higher-ed-compliance
forcing_function: statute
in_force_date: 2026-07-20
source_found: scout.py — Federal Register API, ED 2026-10013
---

# Workforce Pell Accountability Reporting

**One line:** Outcomes tracking for institutions offering the new short-term Workforce Pell
programs — completion rates, placement rates, and graduate earnings against thresholds.

## Verdict: DEAD — refuted under pressure test, batch 1

Three of the premises I built this candidate on were wrong. Each correction cuts against it.

## 1. The institution barely does anything
Under §690.94 the institution annually submits a completer list to the **Governor**, plus
published tuition and fees. Under §690.95 **ED compiles the cohort list itself** from data
institutions already report for Title IV; the institution gets a 60-day window to *correct
ED's list*.
Source: [91 FR 29254](https://www.govinfo.gov/content/pkg/FR-2026-05-19/html/2026-10013.htm).

## 2. ED's own PRA table is the kill shot
> "100 schools x 22 hours = 2,200 total burden hours… $99.96 x 2,200 = **$219,912**."

That is the **entire national institutional burden** — every school, every vendor, every year.
No business fits inside $220K/yr. **G4 fails**: there is no budget line because there is
almost no burden.

## 3. Nobody at the institution computes the metric
ED obtains median earnings from "the Federal agency with earnings data" ([value-added earnings
test](https://www.ed.gov/media/document/2025-ahead-workforce-pell-value-added-earnings-test-112702.pdf)).
Completion and placement rates are certified by **Governors from state administrative wage
records**. The institution computes nothing → **G3 fails**, the product owns no state and no
record of truth.

## 4. A free incumbent already holds the job
National Student Clearinghouse gives FVT/GE compliance reporting away **free**
([source](https://www.studentclearinghouse.org/nscblog/qa-the-clearinghouses-new-fvt-ge-solution-compliance-reporting-platform/)).
Ellucian (which acquired Anthology's SIS in Dec 2025) and Jenzabar already ship Gainful
Employment reporting. The rule explicitly "amends and simplifies its existing FVT and GE
framework to harmonize" — this is a patch to tooling incumbents already ship → **G2 fails**.

## 5. Buyer count
**~100 institutions** with eligible workforce programs after year one, per ED's PRA table.
Accredited Title IV only — not unaccredited providers. **A1 fails** by two orders of magnitude.

## Corrections to the record
- The `$1.9 million` figure that first flagged this is **ED's own cost**, not institutions' —
  and ~70% of it funds the earnings data-sharing agreement. It was evidence the computation is
  *centralised*, i.e. evidence against the candidate. I read it backwards.
- Effective date is **2026-07-20**, not 2027-07-01. The later date belongs to the separate
  STATS rule (2026-13286).
- Durability is genuinely fine — statutory, P.L. 119-21 §83002, consensus rulemaking, no
  litigation found. Durable and irrelevant: the obligation is too thin to sell against.

## What this case teaches — now encoded in `scout.py`
**Read the PRA burden table before anything else.** Agencies are legally required to state
respondent count and hours per response. That single table settles A1 and A2 together, in the
agency's own numbers, before any competitor research. It is a harder kill than the RFA cost
ceiling and it is mechanically extractable. `COUNT_PATTERNS` now puts PRA phrasings first and
auto-kills below an `A1_FLOOR` of 400 obligated entities.

## Links
[[eas-cybersecurity-risk-plan-certification]] — same lesson from the RFA side: burden size
caps price. [[epcra-tier-ii-hazcom-2024-conformity]] · [[fdta-emma-municipal-disclosure-standards]]

## History
- 2026-08-03 — surfaced by `scout.py`; refuted in pressure-test batch 1 on G4/G3/G2/A1
