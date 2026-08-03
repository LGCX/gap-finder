# Gap-Finding Rubric — Solo Founder, Fast to Market

Two layers. **Gates** are pass/fail — one failure discards the idea, no score computed.
**Scores** are 1–5. Weighted total decides ranking.

---

## LAYER 1 — HARD GATES (any fail = discard)

| # | Gate | Fail condition |
|---|------|----------------|
| G1 | **No big incumbent** | Any player with >$50M ARR, or >$20M raised, serving *this exact buyer doing this exact job*. Horizontal giants count only if this job is in their product today. |
| G2 | **Not a feature of someone's roadmap** | If a dominant platform in the buyer's stack (ServiceTitan, Vanta, Shopify, HubSpot, Epic, QuickBooks…) could ship this as a checkbox without changing their business model → fail. |
| G3 | **Not LLM-zero-shot-able** | If a general chatbot does ≥80% of the job in one prompt today, fail. The product must own state, integrations, or a record of truth — not just a prompt. |
| G4 | **Buyer has an existing budget line** | The money already leaves their account for *something* (a person, a spreadsheet-wrangler, a consultant, a fine, a legacy tool). "Would be nice to have" = fail. |
| G5 | **Reachable without SEO** | A named, enumerable channel exists: association, licence registry, distributor, directory, conference, subreddit, Slack/Discord, partner. If the only plan is "rank on Google" → fail. |
| G6 | **v1 buildable solo in ≤8 weeks** | Needs a team, hardware, or a data partnership to be useful at all → fail. |
| G7 | **No custody trap** | Money movement, PHI at scale, licensed activity, or a certification you can't obtain in <90 days → fail *unless* that certification is itself the moat and you accept the ramp. |
| G8 | **Answers "why is this still open?"** | Must have a concrete reason: too small for VC · needs domain access you can get · needs painful legacy integration · boring/ugly · created by a rule change <18 months old · buyer is non-technical and unreachable by normal marketing. "Nobody thought of it" = fail. |

---

## LAYER 2 — SCORED (1–5)

### A. Market (weight 20%)
| # | Criterion | 5 = |
|---|---|---|
| A1 | Reachable buyer count | 5k–50k orgs. Under 2k = no ceiling. Over 200k = a big player is already there or will be. |
| A2 | Price tolerance | Bears $200–500/mo. (Solo servicing ceiling ≈ 300–800 accounts, so ARPU sets your max MRR.) |
| A3 | Budget origin | Replacing a **fine/audit exposure** > replacing a **person's hours** > replacing a **spreadsheet** > replacing **nothing**. |
| A4 | Segment direction | Buyer industry growing or being newly regulated. Shrinking industry = trap. |
| A5 | Willingness to buy from a stranger | Do they buy software self-serve, or only via a rep they met at a conference? |

### B. Gap quality (weight 25%)
| # | Criterion | 5 = |
|---|---|---|
| B1 | Forcing-function strength | Statute with deadline + penalty > customer/insurer/prime-contractor mandate > hard cost pain > convenience. |
| B2 | Forcing-function durability | **Already in force**, unlikely to be repealed or deferred. (Score down anything pending; regulators defer constantly.) |
| B3 | Evidence of unmet demand | 1–3★ reviews of the incumbent naming this exact gap · "we built an internal spreadsheet for this" posts · repeated Upwork/Fiverr requests · job ads hiring a human to do it manually. |
| B4 | Pain frequency | Daily/weekly in the workflow, not annual. |
| B5 | Gap freshness | Created or widened in the last 6–24 months (rule change, vendor EOL, platform deprecation, acquisition gutting a product). **Score 1–2 if the rule is already in force AND the obligated party is one existing compliance vendors already sell to** — see the note below. |

> **An in-force rule is not a gap. It is an advertisement that a market exists.**
>
> Evidence, run 2026-08-03: five of eight candidates died the same way — a real,
> already-in-force rule whose software category was already owned, either by a funded
> vendor (Greenlight Guru, Qualio, SafetyChain, Trakref, Accruent/Fortive) or by the
> body that runs the certification and ships its own portal.
>
> A dated mandate is necessary but nowhere near sufficient. Before scoring B, ask:
> **who is the obligated party, and do compliance vendors already sell to them?**
> If yes, the category is served and you are late. The exploitable cases are narrower:
> - the obligated party has *no* software vendor of any kind today, or
> - the obligation lands on a party existing vendors do *not* sell to (e.g. the rule
>   targets facility owners but the unserved pain sits with their subcontractors), or
> - the rule is enforced against a segment too small or too unglamorous for the
>   incumbents to bother pursuing.
>
> This cuts against the naive reading of B2. Already-in-force still beats pending on
> *durability* — but in-force plus a served buyer is a dead end, not a signal.

### C. Competition (weight 20%)
| # | Criterion | 5 = |
|---|---|---|
| C1 | Direct competitor count | **1–4 mediocre ones.** Zero = probably no market. 15+ = commoditized. |
| C2 | Incumbent shape | Enterprise-priced, sales-led, demo-gated, 2010s UI. You attack bottom-up. Score 1 if incumbents are cheap and self-serve. |
| C3 | Adjacency distance | How far is this from an existing big product's natural next release? Want: far, or strategically unattractive to them. |
| C4 | Time-to-clone by a competent solo dev | Want >3 months, and the delay must come from **non-code** barriers (data access, certification, partnership, domain knowledge). |
| C5 | Competitor health | Are the existing few stagnant, unmaintained, or recently acquired-and-neglected? |

### D. Moat (weight 20%)
| # | Criterion | 5 = |
|---|---|---|
| D1 | Moat type | Ranked: proprietary data / legacy-system integration > regulatory certification > system-of-record workflow lock-in > two-sided network > brand > **features (= no moat, score 1)**. |
| D2 | Switching cost after adoption | Data accumulates; it becomes the audit record; leaving means losing history. |
| D3 | Does the moat compound with usage? | More customers → better data/integrations → harder to displace. |
| D4 | Defensibility against AI | Would a better model make this product *more* valuable (more inputs to act on) or *unnecessary*? |

### E. Economics (weight 10%)
| # | Criterion | 5 = |
|---|---|---|
| E1 | Gross margin | ≥80%. Inference-heavy products: compute unit economics explicitly at the target price. |
| E2 | Expected churn | In the daily workflow / compliance record → low. Episodic or one-time job → high. |
| E3 | CAC payback | <6 months through the identified channel, with a plausible CAC number attached. |
| E4 | Expansion vector | Seats, volume, locations, or modules — revenue grows without new logos. |
| E5 | Concentration risk | No plausible customer exceeds 20% of revenue. |

### F. Execution fit (weight 5%)
| # | Criterion | 5 = |
|---|---|---|
| F1 | Domain access | You (or someone who'll take your call) already lives in this industry. **Biggest single multiplier — score honestly.** |
| F2 | Support load | Buyer self-serves. Score 1 if they phone you about every click. |
| F3 | Maintenance burden | Integrations are stable/documented. Brittle scraping or undocumented APIs = permanent on-call. |
| F4 | Platform dependency | If built on a store/API, can the host kill you or take the market? |

### G. Exit shape (tiebreaker, not weighted)
- Would this fetch **4x+ profit**? (B2B + boring + recurring + <5h/wk owner time.)
- Cleanly separable from you personally: own entity, own Stripe, own bank, documented ops, no personal-brand dependency.
- Reference: micro-SaaS clears ~3.9x profit median, ~2.6x revenue ask, ~81 days on market, and asks get cut 20–80%. B2C/trend products clear 1.5–2x regardless of profit.

---

## Scoring

```
score = 0.20*A + 0.25*B + 0.20*C + 0.20*D + 0.10*E + 0.05*F   (each section = mean of its criteria)
```

- **≥4.0** — build candidate. Do 20 customer calls before code.
- **3.2–3.9** — parking lot. Re-check when a forcing function strengthens.
- **<3.2** — discard, log the reason.

**Automatic downgrade to discard**, whatever the score: B1 ≤2 (no forcing function) or D1 = 1 (feature-only moat).
