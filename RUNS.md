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
