# Source Rotation Ledger

The job runs every few hours. Hitting the same feeds each time returns nothing.
**Each run: pick the 3–4 least-recently-swept sources with `yield` ≠ dead.**
Update `last swept` and `yield` after every sweep.

`yield`: `hot` (produced a BUILD/PARK in last 30d) · `warm` (produced candidates) · `cold` (nothing in 3+ sweeps) · `dead` (retire it)

## Forcing functions — highest yield, sweep most often

| Source | Last swept | Yield | Notes / cursor |
|---|---|---|---|
| Federal Register — final rules, effective 0–18mo | never | — | filter by agency; log last rule ID seen |
| EPA rulemaking + enforcement alerts | never | — | |
| OSHA standards + state-plan adoptions | never | — | |
| FDA / DOL / DOT / FCC rule dockets | never | — | rotate one agency per sweep |
| State professional licensing boards | never | — | rotate states; log which |
| State insurance / labor / environmental depts | never | — | |
| EUR-Lex + national transpositions | never | — | |
| Insurer & underwriter requirement changes | never | — | quiet but forces adoption hard |
| Prime-contractor / franchise mandates on suppliers | never | — | |
| Standards bodies & accreditation schemes | never | — | new audit requirement = new market |

## Revealed pain

| Source | Last swept | Yield | Notes / cursor |
|---|---|---|---|
| G2 / Capterra / Software Advice — 1–3★ on vertical incumbents | never | — | rotate vertical; mine review text |
| Trade subreddits | never | — | rotate: r/HVAC r/msp r/Construction r/Accounting r/dentistry r/logistics r/farming r/smallbusiness |
| Profession forums & Facebook groups | never | — | |
| Niche Slack / Discord communities | never | — | |
| Trade association newsletters | never | — | |
| **Conference session titles** | never | — | agendas are a map of unsolved pain |
| Job postings — human hired to run a spreadsheet | never | — | search: "maintain the tracking spreadsheet" |
| Upwork / Fiverr repeated identical build requests | never | — | |

## Vacuums

| Source | Last swept | Yield | Notes / cursor |
|---|---|---|---|
| Vendor EOL / sunset announcements | never | — | |
| Products gutted after acquisition | never | — | |
| Platform changelogs & deprecations | never | — | Shopify, QuickBooks, Xero, Epic, Microsoft |
| Vertical ERPs with locked installed base, no public API | never | — | |
| Categories abandoned as "too small for VC" | never | — | |

## Sizing (not swept — used on demand)

Licence registries · state business registries · census & industry statistics · association membership counts.
Use these for buyer counts. A number without one of these is `UNVERIFIED`.

## Retired sources

Move `dead` sources here with the date and why.
