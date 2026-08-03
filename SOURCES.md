# Source Rotation Ledger

The job runs every few hours. Hitting the same feeds each time returns nothing.
**Each run: pick the 3–4 least-recently-swept sources with `yield` ≠ dead.**
Update `last swept` and `yield` after every sweep.

`yield`: `hot` (produced a BUILD/PARK in last 30d) · `warm` (produced candidates) · `cold` (nothing in 3+ sweeps) · `dead` (retire it)

## Forcing functions — highest yield, sweep most often

| Source | Last swept | Yield | Notes / cursor |
|---|---|---|---|
| Federal Register — final rules, effective 0–18mo | 2026-08-03 | warm | **federalregister.gov is blocked by egress policy (403) — API and HTML both. Swept indirectly via WebSearch + law-firm alerts.** Covered: EPA AIM Act (h) ER&R (eff. 2026-01-01), FDA QMSR (eff. 2026-02-02), CFPB 1071 revision (eff. 2026-06-30, compliance 2028), TSCA 8(a)(7) PFAS (due 2026-10-13), CMS-1828-F DMEPOS, CMS §6225 (proposed). Next: rotate to DOL / DOT / FCC dockets — health + environment now well mined |
| EPA rulemaking + enforcement alerts | never | — | |
| OSHA standards + state-plan adoptions | never | — | |
| FDA / DOL / DOT / FCC rule dockets | never | — | rotate one agency per sweep |
| State professional licensing boards | never | — | rotate states; log which |
| State insurance / labor / environmental depts | never | — | |
| EUR-Lex + national transpositions | never | — | |
| Insurer & underwriter requirement changes | never | — | quiet but forces adoption hard |
| Prime-contractor / franchise mandates on suppliers | never | — | |
| Standards bodies & accreditation schemes | 2026-08-03 | warm | Produced 3 candidates, all killed. Covered: CMS DMEPOS annual reaccreditation, SQF Edition 10, UK MCS redeveloped installer scheme, ISO 17025/17020 (nothing new in force). Also seen, not yet worked: **CHSA ethical audit requirement, compulsory end-2026** (UK cleaning & hygiene suppliers — likely too small a buyer pool, check before spending a sweep). Pattern learned: where a scheme owner runs the certification, it usually also ships the evidence portal → G2 |

## Revealed pain

| Source | Last swept | Yield | Notes / cursor |
|---|---|---|---|
| G2 / Capterra / Software Advice — 1–3★ on vertical incumbents | never | — | rotate vertical; mine review text |
| Trade subreddits | never | — | rotate: r/HVAC r/msp r/Construction r/Accounting r/dentistry r/logistics r/farming r/smallbusiness |
| Profession forums & Facebook groups | never | — | |
| Niche Slack / Discord communities | never | — | |
| Trade association newsletters | never | — | |
| **Conference session titles** | never | — | agendas are a map of unsolved pain |
| Job postings — human hired to run a spreadsheet | 2026-08-03 | cold | **Attempted, produced nothing — a tooling problem, not a dead source.** WebFetch/curl are 403-blocked by this environment's egress policy, so job boards (Indeed, LinkedIn, ZipRecruiter, Glassdoor) cannot be crawled, and WebSearch will not surface posting *body* text for phrase queries like "maintain the tracking spreadsheet". Do not re-attempt from a sandboxed run unless WebFetch works — test it first. Re-mark `—` if fetch is restored |
| Upwork / Fiverr repeated identical build requests | never | — | |

## Vacuums

| Source | Last swept | Yield | Notes / cursor |
|---|---|---|---|
| Vendor EOL / sunset announcements | 2026-08-03 | cold | Search collapsed onto Microsoft's 2026 retirements (~70 products, incl. Dynamics GP new-subscription stop 2026-04-01) — horizontal, no vertical wedge, no candidate generated. Vertical practice-management sunsets (dental/vet/pharmacy/legal) did **not** surface via general search; they live in trade press and vendor customer emails. Next attempt: query named trade publications per vertical, not generic "end of life" |
| Products gutted after acquisition | never | — | |
| Platform changelogs & deprecations | never | — | Shopify, QuickBooks, Xero, Epic, Microsoft |
| Vertical ERPs with locked installed base, no public API | never | — | |
| Categories abandoned as "too small for VC" | never | — | |

## Sizing (not swept — used on demand)

Licence registries · state business registries · census & industry statistics · association membership counts.
Use these for buyer counts. A number without one of these is `UNVERIFIED`.

## Retired sources

Move `dead` sources here with the date and why.
