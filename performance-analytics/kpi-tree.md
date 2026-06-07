# KPI Tree

North-star and driver metrics for Learnish, shaped by the [funnel](funnel-definition.md) and the Club ladder.

> **Status:** Phase 4 (Measurement) of the [migration](../docs/migration-tracker.md). North-star and milestone model are decided (D-001, D-002); driver targets are working hypotheses.
>
> **Last updated:** 2026-06-07 · **Owner:** [assign Analytics Owner]

---

## North-star

**Family account signups.** (D-001) — the count of families who create an account / are captured.

Why signups and not revenue: digital marginal cost is ~$0, so a generous free layer is the engine for word-of-mouth and Club conversion. Revenue is governed separately by **paying Club families**, which gate the [playbook](../docs/playbook/README.md) milestones (10 → 100 → 1,000).

> **Two numbers, one system:** *signups* scale fast in the background (north-star); *paying families* are the committed, referenceable core (milestone gate). The KPI tree tracks both.

---

## The tree

```
NORTH-STAR: Family account signups
│
├── ACQUISITION  (how families arrive)
│   ├── Workshop attendees / mo           [live]
│   ├── Workshop → signup conversion %    [live]
│   ├── Referral-sourced signups          [live]
│   ├── Store buyers → signup %           [live]
│   └── Social / organic signups          [live]
│
├── ACTIVATION  (do they get value)
│   ├── Signup → activated %              [planned: app]
│   ├── Time-to-first-value               [planned: app]
│   └── Pre-app proxy: 2nd paid touch %   [live]
│
├── MONETIZATION  (Club ladder)
│   ├── Free → Digital Club %             [planned]
│   ├── Digital → Full Club %             [partial]
│   ├── Paying families (count)  ← milestone gate
│   ├── ARPA (avg revenue per account)    [partial]
│   ├── Annual prepay share %             [partial]
│   └── À la carte revenue (workshops + store) [live]
│
├── RETENTION  (do they stay)
│   ├── Weekly Active Families (WAF) ⭐    [planned: app · proxy live]
│   ├── Monthly Active Families (MAF)     [planned · proxy live]
│   ├── Renewal rate (annual / quarterly) [partial]
│   ├── Churn rate                        [partial]
│   └── Repeat workshop attendance %      [live]
│
└── REFERRAL  (do they bring others)
    ├── Referral rate / active family     [live]
    ├── Ambassador-sourced signups        [live]
    └── Workshops seeded by referrals     [live]
```

---

## Leading indicators (weekly — react in days, not months)

- New family signups (and % workshop-sourced)
- Workshops booked + seats filled for next 2 weekends
- Workshop → signup conversion (last 7 days)
- New paying families (Digital + Full)
- À la carte revenue (store + workshop tickets)
- Referral codes redeemed

## Lagging / health (monthly)

- WAF / MAF and active-family rate
- Renewal & churn
- ARPA and annual-prepay share
- Blended CAC by channel (workshop, referral, social, store)
- Gross margin per Full Club child (track against the ~26–47% model)

---

## Targets (working hypotheses — replace with real baselines)

| Metric | Initial target | Confidence |
|--------|---------------|------------|
| Workshop → signup | 50% | low |
| Free → Digital Club | 15% | low |
| Digital → Full Club | 25% | low |
| Annual prepay share | 60% | low |
| Weekly active-family rate | 40% | low |
| Annual renewal | 70% | low |
| Referral rate / active paying family / yr | 0.3 | low |

---

## Pre-launch focus (what we can actually measure today)

Until the app ships, the live KPI subset is the priority:

1. Workshop attendees and **workshop → signup conversion**
2. À la carte revenue (workshops + STEAM store) and repeat-purchase rate
3. Referral / word-of-mouth signups
4. Captured-family list growth (the pre-app north-star proxy)

The planned (app) metrics are scaffolded now so instrumentation is ready at launch.

---

## Ownership

- **KPI definitions & instrumentation:** Analytics Owner
- **Target setting:** Marketing Lead + Founder/CEO
- **Weekly reporting:** Analytics Owner (Growth Ops)

## Related

- [Funnel definition](funnel-definition.md) · [Weekly report](weekly-report-template.md) · [Willingness-to-pay research](willingness-to-pay-research.md)
- [Monetization model](../pricing/monetization-model.md) · [Open questions](../docs/playbook/open-questions-register.md)
