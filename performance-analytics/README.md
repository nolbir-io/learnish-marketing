# performance-analytics

How Learnish knows whether marketing is working — the funnel, the KPI tree, the weekly read, and the experiments behind them.

> **Status:** Phase 4 (Measurement) of the [migration](../docs/migration-tracker.md), rewritten for Learnish.
>
> **Last updated:** 2026-06-07 · **Owner:** [assign Analytics Owner]

## Purpose

Define the metrics, instrument them, and report on them. Receives campaign goals from `campaigns/`, content output from `content-creation/`, and feeds learnings back to all three and to the [open questions register](../docs/playbook/open-questions-register.md).

## North-star

**Family account signups** (D-001). Paying Club families gate the [playbook](../docs/playbook/README.md) milestones (10 → 100 → 1,000). See the [KPI tree](kpi-tree.md) for the full driver map.

## Live vs. planned

Learnish's app/courses aren't shipped yet (content rolls out entertainment → math → languages → other). Today's measurable surfaces are the **STEAM toys store** and **weekend workshops**. The funnel and KPI docs tag every metric `live` or `planned` so we instrument the app stages now and switch them on at launch.

## Files

- [`funnel-definition.md`](funnel-definition.md) — the family journey, stage definitions, exit criteria, attribution
- [`kpi-tree.md`](kpi-tree.md) — north-star → drivers → leading indicators
- [`willingness-to-pay-research.md`](willingness-to-pay-research.md) — Van Westendorp + Gabor-Granger plan and survey (closes OQ-001)
- [`weekly-report-template.md`](weekly-report-template.md) — the standing weekly read
- [`experiments-log.md`](experiments-log.md) — what we tested, what we decided
- `dashboards/` — tool specs (to add once a tool is chosen)

## Open questions owned here

- **OQ-001** — willingness to pay (see WTP research plan)
- **OQ-010** — funnel stage & "active family" definitions (drafted in funnel-definition.md; lead with Weekly Active Family)
- **OQ-011** — attribution model (self-reported + workshop/referral tagging for first 6 months)

## Cadence & ownership

- **Weekly:** Analytics Owner publishes the weekly report in Growth Ops.
- **Monthly:** review lagging/health metrics; update phase assumptions.
- **Targets:** Marketing Lead + Founder/CEO. See [operating cadence](../docs/playbook/operating-cadence.md) and [governance RACI](../docs/playbook/governance-raci.md).
