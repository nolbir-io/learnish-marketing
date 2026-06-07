# Willingness-to-Pay Research Plan

How Learnish validates Club price points with parents before locking pricing. Closes **OQ-001**.

> **Status:** Phase 4 (Measurement) of the [migration](../docs/migration-tracker.md). Price points under test come from the [monetization model](../pricing/monetization-model.md) and are **hypotheses, not decisions**.
>
> **Last updated:** 2026-06-07 · **Owner:** [assign Analytics Owner + Marketing Lead]

---

## 1. What we're testing

| Tier | Price hypothesis | Question |
|------|-----------------|----------|
| Digital Club (per family) | ~$5–8/mo | Is the all-digital entry priced right vs. the ~$5 entertainment-app anchor? |
| Full Club — Solo (1 kid) | ~$18/mo (~$190/yr prepaid) | Does the anchor bundle read as a deal vs. ~$280 à la carte? |
| Full Club — Family (3 kids) | ~$40/mo (~$430/yr prepaid) | Is the per-child discount compelling without crushing margin? |
| Full Club — Big Family (5) | ~$60/mo (~$650/yr prepaid) | — |
| À la carte workshop | $15–20/child | Is the standalone ticket price acceptable (it also feeds Club)? |

Currency note: run in **UZS** with USD shown for internal analysis. Localize all numbers to round, familiar local price points (avoid literal $→UZS conversions that read oddly).

---

## 2. Methods (run in this order)

### A. Van Westendorp Price Sensitivity Meter (primary)
Four questions per product, plotted to find the acceptable price range and optimal price point (OPP). Best for *range-finding* a new category where buyers have weak reference prices.

### B. Gabor-Granger (secondary, for the chosen tier)
Ask purchase likelihood at specific price steps to estimate a demand curve and revenue-maximizing price. Run only on the **Full Club Solo** tier once Van Westendorp narrows the range.

### C. Real-money signal (most trustworthy)
The survey is stated preference. Triangulate against revealed preference:
- À la carte **workshop ticket** take-up at different prices (we already sell these — A/B the price).
- A **founding-family pre-sale / deposit** for the annual Full Club at app launch (real money = real WTP).

> Stated-preference surveys overstate WTP. Treat Van Westendorp/Gabor-Granger as *directional*; let workshop pricing and pre-sale conversion be the tiebreaker.

---

## 3. Who we ask & how many

- **Audience:** parents of kids 5–17 in Tashkent (primary), regions (secondary). Must be the **buyer** persona.
- **Recruit from:** workshop attendees, the captured-family list, parent Telegram/Instagram communities, and ambassador networks.
- **Sample size:** ≥100 completed responses per tier for a usable Van Westendorp curve; ≥40 to read a directional signal early.
- **Languages:** UZ (default), RU, EN — per the [language matrix](../brand-voice/language-matrix.md). Latin Uzbek default.
- **Screening:** must have ≥1 child aged 5–17 and be involved in purchase decisions.

---

## 4. Survey instrument

### Screener
1. Do you have a child aged 5–17? *(No → exclude)*
2. How many children aged 5–17 are in your household? *(1 / 2 / 3 / 4 / 5+)*
3. Who decides on paid learning activities/products for your child? *(Me / Me + partner / Someone else → exclude if "someone else")*

### Context primer (show before pricing questions)
> Imagine **Learnish Club** — a membership for your child's learning. It includes an app with courses (entertainment, math, languages and more), STEAM activity kits delivered to your home, and weekend in-person workshops where kids build and learn together. Everything is age-appropriate and reviewed for safety.

*(Show a one-screen visual of the three components. Keep the description identical across all respondents.)*

### Van Westendorp — ask per tier (Digital Club, then Full Club Solo)
For **[tier name + what's included]**, at what monthly price would you say it is:
1. **Too cheap** — so low you'd doubt the quality? *(open numeric, UZS/mo)*
2. **A bargain** — great value for the money? *(open numeric)*
3. **Getting expensive** — still worth considering, but you'd think twice? *(open numeric)*
4. **Too expensive** — you would not consider it? *(open numeric)*

*Also ask each tier as an **annual prepaid** figure to test prepay appetite.*

### Gabor-Granger — Full Club Solo only (run after Van Westendorp)
> Would you subscribe to Full Club Solo at **[X] UZS/month** (annual prepay)? *(Yes / Maybe / No)*
Repeat across 5 price steps spanning the Van Westendorp acceptable range (e.g. low / −, hypothesis, +, high). Randomize starting point to reduce anchoring.

### Value & framing checks
1. Bought separately, these would cost ~[à la carte total]. Knowing that, does the Club price feel: *Very cheap / Fair / Expensive / Very expensive.*
2. Which would make you most likely to subscribe? *(Lower monthly price / Annual discount / More workshops included / More kits / Store credits)*
3. Which **one** part is the main reason you'd pay? *(App & courses / STEAM kits / Workshops / Community / Safety & trust)* — informs the OQ-013 "single hero" question.
4. For multiple kids: would per-child pricing feel fair if each kid gets their own kit + workshop seat? *(Yes / No / Depends — open text)*

### Closing
- Self-reported "How did you hear about Learnish?" (attribution seed)
- Optional: join the founding-family pre-sale list *(captures real-intent leads)*

---

## 5. Analysis

- **Van Westendorp plot:** find Point of Marginal Cheapness (PMC), Point of Marginal Expensiveness (PME), Optimal Price Point (OPP), Indifference Price Point (IPP). Acceptable range = PMC→PME.
- **Margin gate:** any candidate price must clear per-child COGS (~$96–122/child/yr → floor ~$12–13/mo/child). A price the market loves but that breaks margin is not a valid answer.
- **Segment cuts:** by city (Tashkent vs regions), by # of kids, by language.
- **Triangulate:** compare survey OPP against workshop price-test take-up and pre-sale conversion.

---

## 6. Outputs & decision

- Recommended price per tier (with range), logged to the [open questions register](../docs/playbook/open-questions-register.md) as the OQ-001 decision.
- Update the [monetization model](../pricing/monetization-model.md) price table from "hypothesis" to "validated."
- Log each price test in the [experiments log](experiments-log.md).

## Related

- [Monetization model](../pricing/monetization-model.md) · [KPI tree](kpi-tree.md) · [Funnel](funnel-definition.md)
- [Language matrix](../brand-voice/language-matrix.md) · [Open questions](../docs/playbook/open-questions-register.md)
