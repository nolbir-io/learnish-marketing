# Funnel Definition

The Learnish family journey, end to end. One shared spine for the [KPI tree](kpi-tree.md), the [weekly report](weekly-report-template.md), and the [experiments log](experiments-log.md).

> **Status:** Phase 4 (Measurement) of the [migration](../docs/migration-tracker.md). Built on the [monetization model](../pricing/monetization-model.md) Club ladder (Free → Digital → Full) and the workshop flywheel in the [playbook](../docs/playbook/README.md).
>
> **Last updated:** 2026-06-07 · **Owner:** [assign Analytics Owner]

---

## What's live vs. planned (read this first)

The funnel is built for the full Learnish product, but not all of it is shipped. Stages are tagged so we measure reality, not aspiration.

- **Live now:** STEAM toys store + weekend workshops (curriculum in development with a curriculum partner). These carry acquisition, revenue, and trust today.
- **Planned:** the app + freemium courses. Content rolls out in sequence — **entertainment → math → languages → other subjects**. The digital Club tiers and the in-app activation/habit metrics go live with the app.

Until the app launches, "signup" is a **captured family** (phone/email + kids' ages from a workshop or store purchase). At app launch it becomes a **family account**, and the digital stages switch on.

---

## Stages

| # | Stage | The moment it happens | Status |
|---|-------|----------------------|--------|
| 1 | **Reach** | A parent encounters Learnish — workshop invite, referral, social, store, app-store impression | Live |
| 2 | **À la carte buyer** | Parent buys a workshop seat or a STEAM toy (non-member) | Live |
| 3 | **Family signup** ⭐ | Family captured (pre-app: phone/email + kids' ages) → family account created (at app launch) | Live (proxy) → Planned (account) |
| 4 | **Activated family** | A kid completes first meaningful action (first app session / first course lesson / day-1 streak); pre-app proxy = a *second* workshop or store purchase | Planned (proxy live) |
| 5 | **Digital Club** | Family upgrades to paid Digital Club (~$5–8/mo, all-digital) | Planned (needs app) |
| 6 | **Full Club** | Family converts to Full Club — kits + ≥4 workshops/yr, annual prepay preferred | Physical live · full bundle Planned |
| 7 | **Retention / Habit** | Active family — recurring use + renewal + repeat workshops | Physical live · app habit Planned |
| 8 | **Referral / Advocacy** | Family refers another family or becomes an ambassador → feeds the next workshop | Live |

**À la carte is a loop, not a dead end.** Workshop tickets and store purchases by non-members are both a revenue line *and* a re-entry point that pushes people toward Club membership. They feed stage 3 (and re-feed stage 8), rather than forming a separate funnel.

---

## Stage exit criteria

- **Reach → À la carte buyer:** completes a workshop booking or a store checkout.
- **À la carte buyer → Family signup:** leaves contact + kids' ages (pre-app) / creates a family account (post-app). *Note: a parent can sign up without buying first — signup does not require stage 2.*
- **Family signup → Activated:** first in-app learning action (post-app) / second paid touch with Learnish (pre-app proxy).
- **Activated → Digital Club:** starts a paid Digital Club subscription.
- **Digital Club → Full Club:** upgrades to a Full Club plan (Solo / Family / Big Family).
- **Full Club → Retention:** stays active (see definition below) and renews at the annual / quarterly mark.
- **Any paid stage → Referral:** refers a family who signs up, or converts to ambassador.

---

## Definitions that need to be exact

- **Active family (lead with weekly):**
  - **WAF (Weekly Active Family):** ≥1 kid in the family completed a learning session in the last 7 days. **Primary retention metric.**
  - **MAF (Monthly Active Family):** ≥1 kid active in the last 30 days. Secondary / smoothing metric.
  - *Pre-app proxy:* a family that attended a workshop or purchased in the last 30 days.
- **Paying family:** any family on a paid tier (Digital or Full). Gates the playbook milestones (10 → 100 → 1,000).
- **Signup (north-star):** one **family account** = one signup. Pre-app, count captured families (dedupe by phone number).
- **À la carte buyer:** distinct from signup — track overlap (what % of buyers become signups, and vice versa).

---

## Core conversion metrics

| Conversion | Why it matters | Status |
|------------|----------------|--------|
| Reach → À la carte | Top-of-funnel efficiency of workshops/store | Live |
| À la carte → Signup | Are we capturing the families we touch? | Live |
| Signup → Activated | Onboarding / time-to-value health | Planned |
| Activated → Digital Club | First-dollar conversion | Planned |
| Digital → Full Club | Core monetization (the anchor offer) | Partial |
| Full Club → renewal | Retention quality; % choosing annual prepay | Partial |
| Any → Referral | Health of the word-of-mouth engine | Live |

---

## Target conversions (working hypotheses — validate, do not trust)

These are placeholders to react to, not commitments. Replace as real data lands.

| Step | Initial target | Confidence |
|------|---------------|------------|
| À la carte → Signup | 60% | low |
| Signup → Activated | 40% | low |
| Activated → Digital Club | 15% | low |
| Digital → Full Club | 25% | low |
| Annual prepay share of Full Club | 60% | low |
| Referral rate (per active paying family / yr) | 0.3 | low |

---

## Attribution (OQ-011)

First 6 months, keep it cheap and honest:

- **Primary:** self-reported "How did you hear about Learnish?" at signup (workshop / referral / social / store / search / other).
- **Workshop-sourced** is the flywheel's headline number — tag every signup that traces to a workshop attendee.
- **Referral** tracked via referral codes / ambassador attribution once that program exists.
- Defer multi-touch modeling until volume justifies it.

---

## SLAs & cadence

- New signup → first onboarding touch (welcome message / next-workshop invite) within **2 days**.
- Workshop attendee → signup follow-up within **48 hours** of the session.
- Funnel reviewed **weekly** in Growth Ops (see [operating cadence](../docs/playbook/operating-cadence.md)).

---

## Related

- [KPI tree](kpi-tree.md) · [Weekly report](weekly-report-template.md) · [Experiments log](experiments-log.md)
- [Willingness-to-pay research plan](willingness-to-pay-research.md)
- [Monetization model](../pricing/monetization-model.md) · [Open questions](../docs/playbook/open-questions-register.md)
