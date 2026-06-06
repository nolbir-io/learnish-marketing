# Learnish — Monetization model (working draft)

> **Status:** Illustrative / pre-validation. Price points are working hypotheses to be tested with willingness-to-pay research in Phase 4 (see [migration tracker](../docs/migration-tracker.md)).
>
> **Last updated:** 2026-06-06 · **Owner:** [assign DRI]

Learnish is a multi-modal kids' L&D platform (ages 5–17) sold to parents in Uzbekistan / Central Asia. Revenue comes from a blend of: a **subscription membership** (digital + physical kit + workshops), a **STEAM toys store**, and a **weekend workshop marketplace**. The free app + freemium courses drive the north-star metric (**family account signups**).

---

## 1. À la carte anchor (what a parent pays separately today)

Per child, per year — used as the value anchor for the bundle.

| Item | Unit price | Per year | Annual value |
|------|-----------|----------|--------------|
| Kits (treated as toys) | ~$25 ea | 4 | ~$100 |
| Workshops | $15–20 ea | 4 | ~$50–60 |
| Courses (ad-free) | $25 ea | ~3 | ~$75 |
| Entertainment app | $5/mo | 12 | ~$60 |
| **Total bought separately** | | | **~$280–300 / child / yr** |

**Implication:** the full bundle must deliver ~$280+ of perceived value and charge visibly less.

---

## 2. Core packaging principle — price by COGS, not by product

Offerings have very different marginal costs, so they are priced on different units:

| Component | Marginal cost per extra child | Pricing unit |
|-----------|-------------------------------|--------------|
| App + courses (digital) | ~$0 | **Per family** (give generously → fuels signups + word of mouth) |
| Kit ($15–20 incl. shipping) | Real, scales per child | **Per child** |
| Workshops | 60% payout (teacher + venue) per seat | **Per child** |

Resolves per-child vs family: **digital is per-family, physical is per-child.** Family discounts apply to the free/cheap digital layer, never to the kit (each kid needs their own kit; discounting it crushes margin).

---

## 3. Tier architecture — the "Learnish Club" (illustrative)

Position the whole thing as a **membership / club**, not a product list — it suits the community-led motion, builds identity and belonging, and improves retention. Members are part of the club; non-members can still pay à la carte for workshops, courses, and toys.

| Tier | Contents | Price (hypothesis) | Role |
|------|----------|--------------------|------|
| **Free** | Ad-free app + freemium courses, whole family | $0 | Drives north-star (family signups), word of mouth |
| **Digital Club** (per family) | All courses ad-free, full app, 1× store credits | ~$5–8/mo per family | Sold standalone; matches $5 entertainment anchor; ~100% margin |
| **Full Club membership** (per child) ⭐ | Digital + 4 kits/yr + ≥4 workshops/yr + **2× store credits** | see family pricing below | Hero offer, anchored vs ~$280 à la carte |

### Family pricing (Full Club — physical scales per child)

Each child needs their own kit + workshop seats, so price is floored by per-child COGS (~$96–122/child/yr). The volume discount comes from the free-to-serve digital layer + shipping efficiency, not the kits.

| Plan | Kids | Price (hypothesis) | Effective / child |
|------|------|--------------------|-------------------|
| Solo | 1 | ~$18/mo (~$190/yr prepaid) | ~$18 |
| Family | 3 | ~$40/mo (~$430/yr prepaid) | ~$13 |
| Big Family | 5 | ~$60/mo (~$650/yr prepaid) | ~$12 |
| 5+ | 6+ | **Contact us** | custom |

**Annual prepay is the focus** — it funds kit costs upfront, cuts churn (no quarterly "should we cancel?" moment at kit shipment), and the saved CAC/shipping can fund the annual discount.

**Store credits:** members earn store credits toward the STEAM toys store; **Full Club members get 2× the credit rate** of Digital members. Base credit rate TBD (e.g. % of subscription back as credit).

---

## 4. Hero bundle unit economics (per child, annual ~$200)

```
Revenue (annual prepay):              ~$200
- Kit COGS (4 × $15–20):              ~$60–80
- Workshop payouts (4 × $9–12*):      ~$36–48
- Payment + fulfillment:              ~$10–20
= Gross margin:                       ~$52–94   (≈ 26–47%)
```

*Workshop payout = 60% of the $15–20 ticket (teacher 30% + venue 30%) — the 4 included workshops are guaranteed seats, NOT free to the platform.*

**Confirmed:** ≥4 workshops included in the Full Club bundle (guaranteed, not empty-seat). Store-credit liability (2×) and a small fulfillment cost also sit against this margin.

**Levers if margin too thin:** raise full-bundle price, tune the store-credit rate, or improve kit COGS at volume.

---

## 5. Workshop marketplace (standalone line)

**Revenue share:** Platform (us) **40%** · Teacher **30%** · Venue/"school" **30%**.
Held weekends (Sat/Sun), 20–30 kids per session.

**Supply model:** teachers sourced locally (nearby the venue); on-the-ground ops run by **student ambassadors** comped with benefits (membership / store credits / experience), not payroll. This keeps the platform's 40% almost pure margin and doubles as a community-building / acquisition channel.

| | Tashkent | Regions | Total |
|---|---|---|---|
| Sessions/mo (target) | 80 | 40 | 120 |
| Avg kids/session | ~25 | ~20 | |
| Avg price/child | ~$17.50 | ~$15 | |
| GMV/session | ~$437 | ~$300 | |
| Our 40%/session | ~$175 | ~$120 | |
| **Our revenue/mo** | **~$14,000** | **~$4,800** | **~$18,800** |

≈ **$47K/mo GMV → ~$19K/mo to platform → ~$226K/yr** at target volume. Near-zero fixed cost (teacher + venue carry delivery). Regions run lower volume/price by design — they seed local community nodes.

---

## 6. The flywheel — workshops are also the acquisition + trust engine

In-person weekend sessions make the "safe and trusted" promise tangible and power the community-led motion:

```
Weekend workshop (parents meet, kids make friends, local trust + proof)
        ↓
Free app signup   ← north-star
        ↓
Digital membership (cheap, all-digital, ~100% margin)
        ↓
Full membership (kits + workshops, the anchor)
```

Workshops therefore serve a dual role: profitable à la carte marketplace **and** top-of-funnel for signups + subscriptions.

---

## 7. Other revenue lines

- **STEAM toys store:** à la carte $20–50 per purchase. Club members earn store credits (Full Club = 2× rate), looping subscription spend back into the store.
- **Single courses:** $25 à la carte for non-members; bundled free in membership.
- **Workshops (à la carte):** non-members can join any session by paying $15–20/child — feeds the funnel toward Club membership.

---

## 8. Open questions (to validate)

- [x] **Workshop delivery cost** — teachers sourced locally; ops run by student ambassadors comped with benefits, so no payroll beyond the 60% payout. *(Confirm material costs for kit-style workshops if any.)*
- [x] **Workshops included in bundle** — ≥4/year, guaranteed seats (not empty-seat).
- [x] **Family plan structure** — Solo (1) / Family (3) / Big Family (5) / 5+ contact us; physical per-child, digital flat per family.
- [x] **Toys store member benefit** — store credits; Full Club = 2× rate.
- [x] **Brand framing** — promote as "Learnish Club" (membership + community).
- [ ] **Base store-credit rate** — what % of subscription converts to credit (then 2× for Full Club)? Watch margin.
- [ ] **Willingness to pay** — validate the family price points (~$18 / $40 / $60 per mo) and ~$5–8/mo digital with parents (Van Westendorp, Phase 4).
- [ ] **Single monetization hero** — which line leads messaging (Club membership vs workshops vs toys); currently blended, leaning Club.
