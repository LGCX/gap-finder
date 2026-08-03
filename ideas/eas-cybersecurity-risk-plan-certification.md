---
slug: eas-cybersecurity-risk-plan-certification
date_found: 2026-08-03
last_reviewed: 2026-08-03
status: DEAD
score: null
failed_gate: G3 (+A2, B4)
buyer: EAS Participants — broadcast stations, cable systems, wireline video, Participating CMS Providers
segment: broadcast-emergency-alerting
forcing_function: statute
in_force_date: 2026-09-29
source_found: Federal Register API — FCC 2026-15601
---

# EAS Cybersecurity Risk Management Plan Certification

**One line:** Annual cybersecurity-plan drafting and FCC certification for EAS Participants,
forced by the FCC's Alerting Security Report and Order effective 2026-09-29.

## Job to be done
EAS Participants must create, update, and **annually certify** to the FCC that they hold a
sufficient cybersecurity risk management plan, plus change default passwords, install security
patches, and implement firewalls or network segmentation.
Source: [FCC 2026-15601](https://www.federalregister.gov/documents/2026/07/31/2026-15601/modernization-of-the-nations-alerting-systems-protecting-the-nations-communications-systems-from), rule text lines 688–689, 938–939, 1148–1149.

## Forcing function
Real, dated, already final. Effective **2026-09-29**. Annual certification to the Commission.
Strong on B1/B2 — this is not the problem.

## Buyer
EAS Participants. The rule does not print a headline count; the NPRM's **$21 million** total
burden against a **≤$1,000 per-entity** annual figure implies roughly **21,000 entities**
(derived, not stated — treat as `UNVERIFIED` until a primary count is found).

## Why it dies

**G3 — LLM-zero-shot-able.** The deliverable is a written cybersecurity risk management plan
for a small broadcaster. A general chatbot drafts a defensible one in a single prompt. The
product would own no state, no integration, and no record of truth.

**A2 — price ceiling, from the agency's own numbers.** The FCC estimates the *entire* annual
compliance cost, across all three adopted requirements, at **"not exceed[ing] $1,000 annually,
based on 10 hours of labor per entity per year"** — and says explicitly that changing default
passwords and installing patches "can be accomplished in the normal course of business and at
little or no additional cost." A tool captures a fraction of $1,000/yr. Rubric A2 needs
$200–500/**month**. The burden is roughly 6× too small to support a solo-viable price.

**B4 — pain frequency.** Annual checkbox, not daily workflow. Churn floor is terrible: the
buyer needs it once a year and remembers that.

## What this case teaches
A forcing function can be real, dated, federal, and enforceable and still be worthless, because
**the size of the burden caps the price**. The Regulatory Flexibility Analysis states that cap
in the agency's own words. Read it before scoring anything else — it kills faster than
competitor research, and it is only visible in the primary rule text.

## Links
[[dhs-fixed-admission-period-i539]] — same sweep, same source.

## History
- 2026-08-03 — found via Federal Register API scan, killed on G3/A2/B4 from primary rule text
