---
slug: dmepos-annual-survey-readiness
date_found: 2026-08-03
last_reviewed: 2026-08-03
status: DEAD
score: null
failed_gate: G2
buyer: DMEPOS supplier locations billing Medicare (owner / compliance officer)
segment: dme
forcing_function: statute
in_force_date: 2026-01-01
source_found: Standards bodies & accreditation schemes
---

# DMEPOS Continuous Survey-Readiness

**One line:** Year-round evidence-and-documentation platform for durable medical
equipment suppliers, because CMS-1828-F replaced the 3-year accreditation cycle with
**unannounced annual resurveys**.

## Why it looked good
CMS Final Rule CMS-1828-F (published Nov 2025, provisions effective Jan 1 2026)
requires every accredited DMEPOS supplier to be resurveyed and reaccredited **at
least once every 12 months**, and all surveys are now unannounced. For a supplier
transitioning off a 3-year cycle that expired 2026-06-01, the annual cycle started
that day — so this is **already in force**, not pending.
- https://achc.org/wp-content/uploads/2026/03/DMEPOS-CMS-Final-Rule-Flyer-2026.pdf
- https://www.homecaremag.com/cmsmedicare-competitive-bidding-health-care/february-2026/understanding-cmss-new-accreditation
- https://opedge.com/cms-clarifies-three-year-one-year-accreditation-cycles/

Buyer pool is large: **more than 79,000 DMEPOS suppliers approved nationwide**
(figure surfaced via CMS/OIG-related coverage; treat as `UNVERIFIED` until read off
a primary CMS enrollment table). Penalty for failure is existential — loss of
accreditation means loss of Medicare billing privileges.

## Killing gate — G2 (feature of someone's roadmap)
The dominant platform in this buyer's stack is **their accreditor**, and the
accreditors already ship the documentation portal as part of the accreditation they
sell. The Compliance Team runs a real-time remote (RtR) virtual survey process and
has explicitly **upgraded its client portal for easier submission of documentation**
— that is this product, bundled, by the org that also grants the certificate.
- https://thecomplianceteam.org/real-time-remote-survey-process/
- https://achcu.com/dmepos-education/ (ACHC's education/prep arm)

Nine CMS-approved DMEPOS accreditors exist (ACHC, TCT, BOC, ABC, CHAP, TJC, HQAA,
NABP, DNV), each with an incentive to own readiness tooling for their own standard.

**Secondary pressure — G1.** A third party already sells exactly this to DMEPOS:
QPI Healthcare Services' *Lavear HARP Light* platform covers PTAN tracking,
credentialing, staff files and accreditation prep against ACHC/CHAP/BOC/TJC
(https://qpihcs.org/cms-annual-dmepos-accreditation-2026/). Above it sit
well-capitalised horizontal healthcare-compliance players doing accreditation
management and survey readiness — MedTrainer
(https://medtrainer.com/products/compliance-overview/accreditation/) and PowerDMS
(https://www.powerdms.com/accreditation-management-software), the latter owned by
NEOGOV. And the DME practice-management vendors already claim the ground:
NikoHealth markets documentation standards and **audit readiness** inside its
billing/PM suite (https://nikohealth.com/dmepos-accreditation-everything-you-need-to-know-in-2026/).

## Segment headwind
CMS imposed a **nationwide 6-month moratorium on new DMEPOS supplier enrollment** in
Feb 2026 as a fraud crackdown — the buyer population is being deliberately shrunk,
which scores A4 down independently of the gate failure.
- https://www.federalregister.gov/documents/2026/02/27/2026-03971/medicare-medicaid-and-childrens-health-insurance-programs-announcement-of-nationwide-temporary

## Thread a future run may pull
The interesting residue is **not** readiness-document storage. It is that a supplier
may need to satisfy a *different* accreditor's standard set on an unannounced
schedule, and the nine standard sets are not harmonised. A cross-accreditor
standards-mapping record could clear G2 where a document vault cannot. Only worth
re-opening if evidence appears of suppliers switching accreditors under the annual
cycle. Do not re-open the generic "survey readiness portal" framing.

## Links
Related ideas: [[cms-6225-provider-based-attestation]] — same regulator, same
pattern of CMS building the submission system itself.

## History
- 2026-08-03 — found via accreditation-scheme sweep, killed on G2
