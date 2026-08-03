---
slug: epcra-tier-ii-hazcom-2024-conformity
date_found: 2026-08-03
last_reviewed: 2026-08-03
status: DEAD
score: null
failed_gate: G1 (contested — see below)
buyer: Facilities storing hazardous chemicals above EPCRA thresholds
segment: ehs-chemical-reporting
forcing_function: statute
in_force_date: 2026-08-21
source_found: scout.py — Federal Register API, EPA 2026-12426
---

# EPCRA Tier II Reporting After HazCom 2024 Conformity

**One line:** EPA conforms EPCRA hazardous chemical inventory reporting to the 2024 OSHA Hazard
Communication standard, effective 2026-08-21, changing how ~463,000 facilities classify chemicals
on their annual Tier II filing.

## Job to be done
Every facility storing a hazardous chemical above threshold files a Tier II inventory with its
SERC, LEPC and fire department **by March 1 each year**. This rule changes the underlying hazard
classifications, so the mapping from safety data sheet to Tier II form changes for everyone.

## Forcing function
Annual, statutory, penalty-backed, and already in force (2026-08-21). The rule's own analysis puts
total burden at **$511,621,168 per year** — alongside $12.47M in annualized savings from the
harmonization itself.
Source: [EPA 2026-12426](https://www.federalregister.gov/documents/2026/06/22/2026-12426/epcra-hazardous-chemical-inventory-reporting-requirements-conformity-with-the-2024-osha-hazard).

## Buyer
**~463,000 facilities** must report annually by March 1 ([EPA](https://www.epa.gov/epcra/hazardous-chemical-inventory-reporting), via secondary coverage — `UNVERIFIED` against a primary EPA table).

## Why it dies — and why this one is worth arguing about

**G1.** [Encamp](https://encamp.com) serves exactly this buyer doing exactly this job: state-by-state
submission logic, automated fee payment to SERC/LEPC/fire departments, **27,000+ Tier II reports
filed across all 50 states**. Venture-funded well past the $20M gate threshold. Also present:
ERA Environmental, VelocityEHS, Cority, plus consultancies (J.J. Keller, Triumvirate, U.S. Compliance).
By the gate as written, this fails on sight.

**But the gate may be wrong here, and this is the clearest evidence yet:**
- Encamp's 27,000 filings against ~463,000 reporting facilities is roughly **6% penetration**. The
  remaining 94% are filing by hand, through state portals, or via consultants.
- Encamp's pricing is demo-gated and "personalized" — no public number. Per rubric C2 that is the
  favourable shape: enterprise-priced, sales-led, attackable bottom-up.
- A1 is also out of band in the opposite direction from usual: 463,000 buyers is far above the
  5k–50k window, and the rubric reads that as "a big player is already there." Here a big player
  is there and has 6% of it.

**Recorded as DEAD per the gate as written, not because the market is closed.** This is exactly the
case the pre-committed calibration decision was for: if a week of runs yields nothing, loosen G1 to
a revenue/penetration threshold rather than "any player over $20M raised." A funded incumbent with
6% share in a 463,000-buyer market is not the same fact as a served market, and the current gate
cannot tell the difference.

## Kill risks if pursued anyway
1. Encamp moves down-market with self-serve before you get distribution.
2. State portals are free; the buyer's alternative is annoying, not expensive.
3. Annual filing cadence = weak B4, high churn risk (once a year, then forgotten).

## Links
[[fdta-emma-municipal-disclosure-standards]] — same run.

## History
- 2026-08-03 — surfaced by `scout.py` evidence extraction; killed on G1 with the gate flagged as contested
