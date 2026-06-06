# Learnish migration tracker

> **Purpose:** Track progress migrating this repo from the forked **Own** (Uzbekistan e-commerce GTM) content to **Learnish** marketing operations.
>
> **Status:** Not started — product brief and Phase 0 inputs still needed.
>
> **Last updated:** 2026-06-06 · **Owner:** [assign DRI]

---

## How to use this doc

1. **Fill Phase 0 first.** Nothing else should ship until the Learnish product brief is agreed.
2. **Check boxes as work completes.** One checkbox = one deliverable merged or explicitly decided (e.g. archived).
3. **Log decisions** in the [Decision log](#decision-log) when assumptions change — don't silently overwrite strategy docs.
4. **Update the status line** at the top when a phase completes or the overall migration stage changes.

**Status values:** `Not started` · `In progress` · `Done` · `Blocked` · `N/A` (keep as-is from fork)

---

## Overall progress

| Phase | Name | Status | Target | Notes |
|-------|------|--------|--------|-------|
| 0 | Product inputs | Not started | — | Blocks all rewrites |
| 1 | Foundation | Not started | — | product-marketing-context, README, brief |
| 2 | Strategy & GTM spine | Not started | — | Playbook, 6-month plan |
| 3 | Brand & voice | Not started | — | |
| 4 | Measurement | Not started | — | Funnel, KPIs |
| 5 | Competitive intelligence | Not started | — | Mostly replace |
| 6 | Campaigns & content | Not started | — | Full rewrite |
| 7 | SEO | Not started | — | |
| 8 | Skills cleanup | Not started | — | Low priority |

**Rough completion:** 0 / 8 phases done

---

## Phase 0 — Product inputs (prerequisite)

Complete this table before rewriting any downstream docs. Use `/product-marketing` in Cursor to draft `.agents/product-marketing-context.md` from these answers.

| Question | Own (current fork) | Learnish (fill in) | Done |
|----------|-------------------|-------------------|------|
| One-liner | E-commerce OS for Uzbekistan merchants | | [ ] |
| Product category | B2B SaaS + high-touch onboarding | | [ ] |
| Primary buyer / ICP | Merchant owner, ops lead | | [ ] |
| North-star metric | 1,000 merchants (signed/live/transacting TBD) | | [ ] |
| Geographic focus | Uzbekistan first | | [ ] |
| Business model | Sales-led design partners | | [ ] |
| Primary conversion action | Book launch plan call | | [ ] |
| Top 3–5 competitors | Shopify, WooCommerce, local marketplaces | | [ ] |
| GTM motion | Founder-led design partners → scaled channels | | [ ] |
| Languages / markets | UZ / RU / EN TBD | | [ ] |

**Phase 0 exit criteria**

- [ ] Founders agree on one-liner and north-star metric
- [ ] ICP and primary CTA documented
- [ ] Competitive set named (even if profiles not written yet)
- [ ] Decision on milestone model (keep 10 → 100 → 1,000 or define new phases)

---

## Phase 1 — Foundation

*Blocks all skills and workstream folders — every slash command reads product context first.*

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Rewrite product marketing context | `.agents/product-marketing-context.md` | Not started | [ ] |
| Optional: rename to canonical path | `.agents/product-marketing.md` | N/A | [ ] |
| Update repo README | `README.md` | Not started | [ ] |
| Update short brief | `brief.md` | Not started | [ ] |
| Reset founder thesis worksheet | `founder-team-thesis-alignment.md` | Not started | [ ] |
| Refresh open questions | `docs/playbook/open-questions-register.md` | Not started | [ ] |
| Update contributing references | `CONTRIBUTING.md` | Not started | [ ] |

**Phase 1 exit criteria**

- [ ] `/product-marketing` summarizes Learnish, not Own
- [ ] README describes Learnish purpose and links to this tracker
- [ ] No "Own" in foundation files except historical notes

---

## Phase 2 — Strategy & GTM spine

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Playbook index | `docs/playbook/README.md` | Not started | [ ] |
| Phase 0 — Foundation | `docs/playbook/phase-0-foundation.md` | Not started | [ ] |
| Phase 1 — First cohort | `docs/playbook/phase-1-first-10.md` | Not started | [ ] |
| Phase 2 — Early adopters | `docs/playbook/phase-2-first-100.md` | Not started | [ ] |
| Phase 3 — Scale | `docs/playbook/phase-3-first-1000.md` | Not started | [ ] |
| Operating cadence | `docs/playbook/operating-cadence.md` | Not started | [ ] |
| Governance RACI | `docs/playbook/governance-raci.md` | Not started | [ ] |
| Operating principles | `docs/strategy/operating-principles.md` | Not started | [ ] |
| 6-month plan index | `docs/plan-6m/README.md` | Not started | [ ] |
| Month 01 | `docs/plan-6m/month-01.md` | Not started | [ ] |
| Month 02 | `docs/plan-6m/month-02.md` | Not started | [ ] |
| Month 03 | `docs/plan-6m/month-03.md` | Not started | [ ] |
| Month 04 | `docs/plan-6m/month-04.md` | Not started | [ ] |
| Month 05 | `docs/plan-6m/month-05.md` | Not started | [ ] |
| Month 06 | `docs/plan-6m/month-06.md` | Not started | [ ] |

**Decisions needed**

- [ ] Milestone labels (merchants → learners / enrollments / other)
- [ ] Phase structure still valid or redesigned
- [ ] Timeline horizon (6 / 12 / 24 months)

**Phase 2 exit criteria**

- [ ] Each phase doc has Learnish ICP, motion, channels, exit criteria
- [ ] 6-month plan aligns with playbook phases
- [ ] Operating principles reflect Learnish thesis, not Own

---

## Phase 3 — Brand & voice

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Voice guide | `brand-voice/voice-guide.md` | Not started | [ ] |
| Language matrix | `brand-voice/language-matrix.md` | Not started | [ ] |
| Folder README | `brand-voice/README.md` | Not started | [ ] |
| Review rubric (product-specific items) | `brand-review/review-rubric.md` | Not started | [ ] |
| Review log | `brand-review/review-log.md` | Not started | [ ] |
| Folder README | `brand-review/README.md` | Not started | [ ] |

**Phase 3 exit criteria**

- [ ] Voice guide has Learnish tone, words to use/avoid, and personality
- [ ] Language matrix matches Learnish markets

---

## Phase 4 — Measurement

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Funnel definition | `performance-analytics/funnel-definition.md` | Not started | [ ] |
| KPI tree | `performance-analytics/kpi-tree.md` | Not started | [ ] |
| Experiments log | `performance-analytics/experiments-log.md` | Not started | [ ] |
| Weekly report template | `performance-analytics/weekly-report-template.md` | Not started | [ ] |
| Folder README | `performance-analytics/README.md` | Not started | [ ] |

**Phase 4 exit criteria**

- [ ] Funnel stages match Learnish buyer journey (not merchant signed → live → transacting)
- [ ] North-star and supporting metrics defined in KPI tree

---

## Phase 5 — Competitive intelligence

*Mostly replace — current research is e-commerce / Uzbekistan specific.*

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Competitor summary | `competitor-profiles/_summary.md` | Not started | [ ] |
| Market map | `competitive-analysis/market-map.md` | Not started | [ ] |
| Analysis README | `competitive-analysis/README.md` | Not started | [ ] |
| Battlecard template | `competitive-brief/template.md` | Not started | [ ] |
| Brief README | `competitive-brief/README.md` | Not started | [ ] |
| New competitor profile #1 | `competitor-profiles/` | Not started | [ ] |
| New competitor profile #2 | `competitor-profiles/` | Not started | [ ] |
| New competitor profile #3 | `competitor-profiles/` | Not started | [ ] |

**Archive (Own fork — move to `_archive/own-fork/` when ready)**

| File | Done |
|------|------|
| `competitor-profiles/shopify.md` | [ ] |
| `competitor-profiles/woocommerce.md` | [ ] |
| `competitor-profiles/uzbekistan-landscape.md` | [ ] |
| `competitor-profiles/raw/` (desk research scrapes) | [ ] |

**Phase 5 exit criteria**

- [ ] At least 3 Learnish-relevant competitor profiles exist
- [ ] Market map and summary reflect Learnish category
- [ ] Own-specific profiles archived or removed

---

## Phase 6 — Campaigns & content

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Campaign README | `campaigns/README.md` | Not started | [ ] |
| Phase 1 brief | `campaigns/phase-1-brief.md` | Not started | [ ] |
| Phase 2 brief | `campaigns/phase-2-brief.md` | Not started | [ ] |
| Phase 3 brief | `campaigns/phase-3-brief.md` | Not started | [ ] |
| Campaign calendar | `campaigns/calendar.md` | Not started | [ ] |
| Paid ads README | `content-creation/paid-ads/README.md` | Not started | [ ] |
| Paid ads draft | `content-creation/paid-ads/2026-06-brand-awareness.md` | Not started | [ ] |
| Social README | `content-creation/social/README.md` | Not started | [ ] |
| Social calendar | `content-creation/social/calendar.md` | Not started | [ ] |
| Instagram draft | `content-creation/social/instagram/2026-06.md` | Not started | [ ] |
| LinkedIn draft | `content-creation/social/linkedin/2026-06.md` | Not started | [ ] |
| Content README | `content-creation/README.md` | Not started | [ ] |
| Landing page (rename + rewrite) | `landing-pages/merchant-signup.md` → TBD | Not started | [ ] |
| Sales deck (replace) | `sales-enablement/decks/marketplace-escape-deck.md` | Not started | [ ] |

**Phase 6 exit criteria**

- [ ] At least one landing page draft with Learnish CTA
- [ ] One campaign brief aligned to current playbook phase
- [ ] Own-specific sales deck archived or replaced

---

## Phase 7 — SEO

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Keyword universe | `seo-audit/keyword-universe.md` | Not started | [ ] |
| Technical audit | `seo-audit/technical-audit.md` | Not started | [ ] |
| Folder README | `seo-audit/README.md` | Not started | [ ] |

**Phase 7 exit criteria**

- [ ] Keyword universe targets Learnish category and ICP
- [ ] Technical audit references Learnish site URL (when available)

---

## Phase 8 — Skills cleanup (low priority)

Generic skills in `.agents/skills/` stay. Spot-check Own-specific examples only.

| Task | File(s) | Status | Done |
|------|---------|--------|------|
| Headless CMS reference | `.agents/skills/content-strategy/references/headless-cms.md` | Not started | [ ] |
| Customer research sources | `.agents/skills/customer-research/references/source-guides.md` | Not started | [ ] |
| Marketing plan example | `.agents/skills/marketing-plan/references/example-quietude.md` | Not started | [ ] |
| Skill evals with merchant/UZ examples | `.agents/skills/**/evals/*.json` | Not started | [ ] |
| Regenerate Cursor commands | `python3 .agents/generate-skill-commands.py` | Not started | [ ] |

**Phase 8 exit criteria**

- [ ] No misleading Own examples in skill references used day-to-day
- [ ] Slash commands regenerated after skill edits

---

## Final verification

Run before calling the migration complete:

| Check | Done |
|-------|------|
| `grep -ri "Own\|merchant\|Shopify\|Uzum\|Humo"` clean in product docs (exclude `_archive/`) | [ ] |
| `.agents/product-marketing-context.md` describes Learnish only | [ ] |
| `README.md` describes Learnish only | [ ] |
| Playbook north-star matches Learnish metric | [ ] |
| Funnel stages match Learnish journey | [ ] |
| ≥3 competitor profiles for Learnish | [ ] |
| ≥1 landing page draft exists | [ ] |
| Open questions register has Learnish-specific items | [ ] |

---

## Decision log

Record major migration decisions here. Link to PRs or docs when possible.

| Date | Decision | Rationale | Owner |
|------|----------|-----------|-------|
| 2026-06-06 | Created migration tracker | Fork still contains Own content; Learnish brief not yet captured | — |
| | | | |

---

## Notes & blockers

<!-- Add blockers, open questions, and links to working docs -->

- **Blocker:** Learnish product brief not yet written — Phase 0 incomplete.
- **Fork source:** Repo content is Own (Uzbekistan e-commerce GTM). Repo name/remote already say `learnish-marketing`.
- **Suggested first action:** Fill Phase 0 table, then run `/product-marketing` to draft context.

---

## Related docs

- [Product marketing context](../.agents/product-marketing-context.md) — source of truth for all skills (needs rewrite)
- [Playbook index](playbook/README.md) — current GTM phases (Own)
- [Open questions register](playbook/open-questions-register.md) — unresolved assumptions
- [Contributing](../CONTRIBUTING.md) — doc conventions
