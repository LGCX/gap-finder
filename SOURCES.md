# Source Rotation Ledger

The job runs twice daily. Hitting the same feeds each time returns nothing.
**Each run: pick the 3–4 least-recently-swept sources with `yield` ≠ dead.**
Update `last swept` and `yield` after every sweep.

**Tooling assumption: this job runs locally with working `WebFetch` and `curl`.**
Many of these sources need page bodies — review text, job listings, pricing pages,
primary rule text. A sandboxed run without egress can only reach a third of this list,
and marks sources `cold` that are merely unreachable. If fetch is blocked, say so and
stop rather than downgrading sources that were never actually swept.

`yield`: `hot` (produced a BUILD/PARK in last 30d) · `warm` (produced candidates) · `cold` (nothing in 3+ sweeps) · `dead` (retire it)

## Forcing functions — highest yield, sweep most often

| Source | Last swept | Yield | Notes / cursor |
|---|---|---|---|
| Federal Register — final rules, effective 0–18mo | 2026-08-03 | warm | **Scan the API, do not search.** `curl -s "https://www.federalregister.gov/api/v1/documents.json?conditions[type][]=RULE&conditions[publication_date][gte]=YYYY-MM-DD&per_page=100"` → complete set, not whatever got law-firm coverage. Then fetch each rule's HTML for its **Regulatory Flexibility Analysis** — that section gives a citable count of affected small entities and the agency's own per-entity cost estimate (feeds A1/A2/A3). **The HTML pages 302 to `unblock.federalregister.gov` (anti-bot) — WebFetch fails. Use the API and `raw_text_url` instead; both work.** Covered so far: EPA AIM Act (h) ER&R (eff. 2026-01-01), FDA QMSR (eff. 2026-02-02), CFPB 1071 revision (compliance 2028), TSCA 8(a)(7) PFAS (due 2026-10-13), CMS-1828-F DMEPOS, CMS §6225 (proposed), FCC 2026-15601 EAS cyber (2026-09-29), DHS 2026-14439 fixed admission (2026-09-15). Cursor: scanned publication_date ≥ 2026-05-01 with effective_date ≥ 2026-08-10 — **next scan should start from publication_date ≥ 2026-08-03**. Surveyed but not worked: FAA interference-tolerant radio altimeters (2026-09-29), FCC NG911 reliability (2026-08-10), agency COI/conflict-of-commitment rules for federal grant recipients (2026-08-17), PHMSA pipeline standards updates (2027-01-01) |
| **Agency enforcement actions & consent decrees** | never | — | Fines actually levied, not rules merely written. A published penalty against a company shaped like the buyer is what makes B1 real; a rule nobody enforces scores low. Sweep EPA/OSHA/FDA/FTC/state-AG press releases |
| **Government procurement — SAM.gov awards, EU TED tenders** | never | — | What agencies pay humans and consultants to do manually, with dollar amounts. A direct map of unautomated workflows |
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
| Job postings — human hired to run a spreadsheet | never | — | Previously marked cold under a sandbox with no fetch — that was a tooling failure, not a dead source, and the mark is reset. Needs page bodies: crawl Indeed / LinkedIn / ZipRecruiter listing text for phrases like "maintain the tracking spreadsheet" |
| Upwork / Fiverr repeated identical build requests | never | — | |
| **Vertical app-store reviews** | never | — | Shopify, QuickBooks, Xero, Epic App Orchard, Procore. Reviews scoped to one ecosystem expose gaps inside a specific stack — where integration moats (D1) live |

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
