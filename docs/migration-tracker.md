# Learnish migration tracker

> **Purpose:** Track progress migrating this repo from the forked **Own** (Uzbekistan e-commerce GTM) content to **Learnish** marketing operations.
>
> **Status:** Phases 0–3 done — Foundation, GTM spine, and now Brand & voice (`brand-voice/`, `brand-review/`) all rewritten for Learnish. Next: Phase 4 (Measurement). See [`pricing/monetization-model.md`](../pricing/monetization-model.md) and [`playbook/README.md`](playbook/README.md).
>
> **Last updated:** 2026-06-07 · **Owner:** [assign DRI]

---

## How to use this doc

1. **Fill Phase 0 first.** Nothing else should ship until the Learnish product brief is agreed.
2. **Check boxes as work completes.** One checkbox = one deliverable merged or explicitly decided (e.g. archived).
3. **Log decisions** in the [Decision log](#decision-log) when assumptions change — don't silently overwrite strategy docs.
4. **Update the status line** at the top when a phase completes or the overall migration stage changes.

**Status values:** `Not started` · `In progress` · `Done` · `Blocked` · `N/A` (keep as-is from fork)

---

## Overall progress


| Phase | Name                     | Status      | Target | Notes                                    |
| ----- | ------------------------ | ----------- | ------ | ---------------------------------------- |
| 0     | Product inputs           | Done        | —      | Brief, competitors, monetization captured |
| 1     | Foundation               | Done        | —      | product-marketing-context, README, brief, thesis, OQ register |
| 2     | Strategy & GTM spine     | Done        | —      | Playbook, operating principles, 6-month plan rewritten for Learnish |
| 3     | Brand & voice            | Done        | —      | Voice guide, language matrix, review rubric/log + READMEs rewritten for Learnish (dual parent/kid audience) |
| 4     | Measurement              | Not started | —      | Funnel, KPIs                             |
| 5     | Competitive intelligence | Not started | —      | Mostly replace                           |
| 6     | Campaigns & content      | Not started | —      | Full rewrite                             |
| 7     | SEO                      | Not started | —      |                                          |
| 8     | Skills cleanup           | Not started | —      | Low priority                             |


**Rough completion:** 3 / 8 phases done (Phase 1, Phase 2, Phase 3)

---

## Phase 0 — Product inputs (prerequisite)

Complete this table before rewriting any downstream docs. Use `/product-marketing` in Cursor to draft `.agents/product-marketing-context.md` from these answers.


| Question                  | Own (current fork)                            | Learnish (agreed 2026-06-06)                                                                                                                                   | Done |
| ------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| One-liner                 | E-commerce OS for Uzbekistan merchants        | A safe, trusted learning & development platform that makes everyday learning exciting for kids 5–17                                                            | [x]  |
| Product category          | B2B SaaS + high-touch onboarding              | B2C kids/family EdTech — multi-modal: learning app + STEAM toys store + tutor/teacher-led workshops + freemium courses (languages, STEAM, personal finance)    | [x]  |
| Primary buyer / ICP       | Merchant owner, ops lead                      | **Parents** of kids aged 5–17 who want their kids to achieve their best (kids 5–17 are the end users)                                                          | [x]  |
| North-star metric         | 1,000 merchants (signed/live/transacting TBD) | Family account signups                                                                                                                                         | [x]  |
| Geographic focus          | Uzbekistan first                              | Uzbekistan / Central Asia                                                                                                                                      | [x]  |
| Business model            | Sales-led design partners                     | Blended: freemium → premium courses, STEAM toy sales, paid workshops (single monetization focus not yet decided)                                               | [x]  |
| Primary conversion action | Book launch plan call                         | Download app / create a family account                                                                                                                         | [x]  |
| Top competitors           | Shopify, WooCommerce, local marketplaces      | **Attention** (compete for kids' time): YouTube/YouTube Kids, TikTok, Instagram, Netflix, Roblox, Facebook. **Category** (compete for the spend): Khan Academy Kids, Duolingo/Duolingo ABC, ABCmouse, KiwiCo/MEL Science (kits), Outschool (workshops), local tutoring centers & kids clubs, marketplaces selling STEAM toys (e.g. Uzum) | [x]  |
| GTM motion                | Founder-led design partners → scaled channels | Community / word-of-mouth led                                                                                                                                  | [x]  |
| Languages / markets       | UZ / RU / EN TBD                              | Uzbek + Russian + English                                                                                                                                      | [x]  |


**Phase 0 exit criteria**

- [x] Founders agree on one-liner and north-star metric
- [x] ICP and primary CTA documented
- [x] Competitive set named — split into **attention** (TikTok/YouTube/Roblox/Netflix) vs **category** (Khan Academy Kids, KiwiCo, Outschool, local clubs)
- [x] Decision on milestone model — **redesign** for a B2C family model (e.g. first 100 → 1,000 → 10,000 families); replaces 10 → 100 → 1,000 merchants

> **Note — partial fork reuse:** The STEAM toys store is real e-commerce, so parts of the Own competitive/payments/delivery research (local payments, fiscalization, marketplaces like Uzum) may be repurposed rather than fully discarded. Flag reusable pieces during Phase 5.

---

## Phase 1 — Foundation

*Blocks all skills and workstream folders — every slash command reads product context first.*


| Task                               | File(s)                                    | Status | Done |
| ---------------------------------- | ------------------------------------------ | ------ | ---- |
| Rewrite product marketing context  | `.agents/product-marketing-context.md`     | Done   | [x]  |
| Optional: rename to canonical path | `.agents/product-marketing.md`             | N/A    | [ ]  |
| Update repo README                 | `README.md`                                | Done   | [x]  |
| Update short brief                 | `brief.md`                                 | Done   | [x]  |
| Reset founder thesis worksheet     | `founder-team-thesis-alignment.md`         | Done   | [x]  |
| Refresh open questions             | `docs/playbook/open-questions-register.md` | Done   | [x]  |
| Update contributing references     | `CONTRIBUTING.md`                          | Done   | [x]  |


**Phase 1 exit criteria**

- [x] `/product-marketing` summarizes Learnish, not Own
- [x] README describes Learnish purpose and links to this tracker
- [x] No "Own" in foundation files except historical notes

> **Note:** `founder-team-thesis-alignment.md` is *reset to blanks* for Learnish (founder name kept) — the team still needs to fill it in. Worksheet scaffold and reference appendices are intentionally product-agnostic and were left intact.

---

## Phase 2 — Strategy & GTM spine


| Task                     | File(s)                                 | Status | Done |
| ------------------------ | --------------------------------------- | ------ | ---- |
| Playbook index           | `docs/playbook/README.md`               | Done   | [x]  |
| Phase 0 — Foundation     | `docs/playbook/phase-0-foundation.md`   | Done   | [x]  |
| Phase 1 — First cohort   | `docs/playbook/phase-1-first-10.md`     | Done   | [x]  |
| Phase 2 — Early adopters | `docs/playbook/phase-2-first-100.md`    | Done   | [x]  |
| Phase 3 — Scale          | `docs/playbook/phase-3-first-1000.md`   | Done   | [x]  |
| Operating cadence        | `docs/playbook/operating-cadence.md`    | Done   | [x]  |
| Governance RACI          | `docs/playbook/governance-raci.md`      | Done   | [x]  |
| Operating principles     | `docs/strategy/operating-principles.md` | Done   | [x]  |
| 6-month plan index       | `docs/plan-6m/README.md`                | Done   | [x]  |
| Month 01                 | `docs/plan-6m/month-01.md`              | Done   | [x]  |
| Month 02                 | `docs/plan-6m/month-02.md`              | Done   | [x]  |
| Month 03                 | `docs/plan-6m/month-03.md`              | Done   | [x]  |
| Month 04                 | `docs/plan-6m/month-04.md`              | Done   | [x]  |
| Month 05                 | `docs/plan-6m/month-05.md`              | Done   | [x]  |
| Month 06                 | `docs/plan-6m/month-06.md`              | Done   | [x]  |


**Decisions needed**

- [x] Milestone labels — **paying Club families** gate each phase (10 → 100 → 1,000 families; 10,000 = post-playbook); **family signups** remain the north-star
- [x] Phase structure — kept 4 phases, reframed around the community/workshop flywheel; filenames retained as slots
- [x] Timeline horizon — **6 months**, extendable to 12 (next-cycle brief in Month 06)

**Phase 2 exit criteria**

- [x] Each phase doc has Learnish ICP, motion, channels, exit criteria
- [x] 6-month plan aligns with playbook phases
- [x] Operating principles reflect Learnish thesis, not Own (LEGO / Duolingo / Disney + local community moat)

> **Open / deferred from Phase 2:** `playbook/open-questions-register.md` still carries Own-era OQs (signed/live/transacting). It's listed under Phase 1 ("Refresh open questions") — refresh it there. Phase 2 docs reference the Learnish Phase 0 brief + monetization model as the source of truth, not the still-Own `.agents/product-marketing-context.md` (Phase 1).

---

## Phase 3 — Brand & voice


| Task                                   | File(s)                          | Status      | Done |
| -------------------------------------- | -------------------------------- | ----------- | ---- |
| Voice guide                            | `brand-voice/voice-guide.md`     | Done        | [x]  |
| Language matrix                        | `brand-voice/language-matrix.md` | Done        | [x]  |
| Folder README                          | `brand-voice/README.md`          | Done        | [x]  |
| Review rubric (product-specific items) | `brand-review/review-rubric.md`  | Done        | [x]  |
| Review log                             | `brand-review/review-log.md`     | Done        | [x]  |
| Folder README                          | `brand-review/README.md`         | Done        | [x]  |


**Phase 3 exit criteria**

- [x] Voice guide has Learnish tone, words to use/avoid, and personality
- [x] Language matrix matches Learnish markets

---

## Phase 4 — Measurement


| Task                   | File(s)                                           | Status      | Done |
| ---------------------- | ------------------------------------------------- | ----------- | ---- |
| Funnel definition      | `performance-analytics/funnel-definition.md`      | Not started | [ ]  |
| KPI tree               | `performance-analytics/kpi-tree.md`               | Not started | [ ]  |
| Experiments log        | `performance-analytics/experiments-log.md`        | Not started | [ ]  |
| Weekly report template | `performance-analytics/weekly-report-template.md` | Not started | [ ]  |
| Folder README          | `performance-analytics/README.md`                 | Not started | [ ]  |


**Phase 4 exit criteria**

- [ ] Funnel stages match Learnish buyer journey (not merchant signed → live → transacting)
- [ ] North-star and supporting metrics defined in KPI tree

---

## Phase 5 — Competitive intelligence

*Mostly replace — current research is e-commerce / Uzbekistan specific.*


| Task                      | File(s)                              | Status      | Done |
| ------------------------- | ------------------------------------ | ----------- | ---- |
| Competitor summary        | `competitor-profiles/_summary.md`    | Not started | [ ]  |
| Market map                | `competitive-analysis/market-map.md` | Not started | [ ]  |
| Analysis README           | `competitive-analysis/README.md`     | Not started | [ ]  |
| Battlecard template       | `competitive-brief/template.md`      | Not started | [ ]  |
| Brief README              | `competitive-brief/README.md`        | Not started | [ ]  |
| New competitor profile #1 | `competitor-profiles/`               | Not started | [ ]  |
| New competitor profile #2 | `competitor-profiles/`               | Not started | [ ]  |
| New competitor profile #3 | `competitor-profiles/`               | Not started | [ ]  |


**Archive (Own fork — move to `_archive/own-fork/` when ready)**


| File                                               | Done |
| -------------------------------------------------- | ---- |
| `competitor-profiles/shopify.md`                   | [ ]  |
| `competitor-profiles/woocommerce.md`               | [ ]  |
| `competitor-profiles/uzbekistan-landscape.md`      | [ ]  |
| `competitor-profiles/raw/` (desk research scrapes) | [ ]  |


**Phase 5 exit criteria**

- [ ] At least 3 Learnish-relevant competitor profiles exist
- [ ] Market map and summary reflect Learnish category
- [ ] Own-specific profiles archived or removed

---

## Phase 6 — Campaigns & content


| Task                            | File(s)                                                | Status      | Done |
| ------------------------------- | ------------------------------------------------------ | ----------- | ---- |
| Campaign README                 | `campaigns/README.md`                                  | Not started | [ ]  |
| Phase 1 brief                   | `campaigns/phase-1-brief.md`                           | Not started | [ ]  |
| Phase 2 brief                   | `campaigns/phase-2-brief.md`                           | Not started | [ ]  |
| Phase 3 brief                   | `campaigns/phase-3-brief.md`                           | Not started | [ ]  |
| Campaign calendar               | `campaigns/calendar.md`                                | Not started | [ ]  |
| Paid ads README                 | `content-creation/paid-ads/README.md`                  | Not started | [ ]  |
| Paid ads draft                  | `content-creation/paid-ads/2026-06-brand-awareness.md` | Not started | [ ]  |
| Social README                   | `content-creation/social/README.md`                    | Not started | [ ]  |
| Social calendar                 | `content-creation/social/calendar.md`                  | Not started | [ ]  |
| Instagram draft                 | `content-creation/social/instagram/2026-06.md`         | Not started | [ ]  |
| LinkedIn draft                  | `content-creation/social/linkedin/2026-06.md`          | Not started | [ ]  |
| Content README                  | `content-creation/README.md`                           | Not started | [ ]  |
| Landing page (rename + rewrite) | `landing-pages/merchant-signup.md` → TBD               | Not started | [ ]  |
| Sales deck (replace)            | `sales-enablement/decks/marketplace-escape-deck.md`    | Not started | [ ]  |


**Phase 6 exit criteria**

- [ ] At least one landing page draft with Learnish CTA
- [ ] One campaign brief aligned to current playbook phase
- [ ] Own-specific sales deck archived or replaced

---

## Phase 7 — SEO


| Task             | File(s)                         | Status      | Done |
| ---------------- | ------------------------------- | ----------- | ---- |
| Keyword universe | `seo-audit/keyword-universe.md` | Not started | [ ]  |
| Technical audit  | `seo-audit/technical-audit.md`  | Not started | [ ]  |
| Folder README    | `seo-audit/README.md`           | Not started | [ ]  |


**Phase 7 exit criteria**

- [ ] Keyword universe targets Learnish category and ICP
- [ ] Technical audit references Learnish site URL (when available)

---

## Phase 8 — Skills cleanup (low priority)

Generic skills in `.agents/skills/` stay. Spot-check Own-specific examples only.


| Task                                  | File(s)                                                        | Status      | Done |
| ------------------------------------- | -------------------------------------------------------------- | ----------- | ---- |
| Headless CMS reference                | `.agents/skills/content-strategy/references/headless-cms.md`   | Not started | [ ]  |
| Customer research sources             | `.agents/skills/customer-research/references/source-guides.md` | Not started | [ ]  |
| Marketing plan example                | `.agents/skills/marketing-plan/references/example-quietude.md` | Not started | [ ]  |
| Skill evals with merchant/UZ examples | `.agents/skills/**/evals/*.json`                               | Not started | [ ]  |
| Regenerate Cursor commands            | `python3 .agents/generate-skill-commands.py`                   | Not started | [ ]  |


**Phase 8 exit criteria**

- [ ] No misleading Own examples in skill references used day-to-day
- [ ] Slash commands regenerated after skill edits

---

## Final verification

Run before calling the migration complete:


| Check                                                                                   | Done |
| --------------------------------------------------------------------------------------- | ---- |
| `grep -ri "Own|merchant|Shopify|Uzum|Humo"` clean in product docs (exclude `_archive/`) | [ ]  |
| `.agents/product-marketing-context.md` describes Learnish only                          | [x]  |
| `README.md` describes Learnish only                                                     | [x]  |
| Playbook north-star matches Learnish metric                                             | [x]  |
| Funnel stages match Learnish journey                                                    | [ ]  |
| ≥3 competitor profiles for Learnish                                                     | [ ]  |
| ≥1 landing page draft exists                                                            | [ ]  |
| Open questions register has Learnish-specific items                                     | [x]  |


---

## Decision log

Record major migration decisions here. Link to PRs or docs when possible.


| Date       | Decision                                | Rationale                                                                                                                 | Owner |
| ---------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----- |
| 2026-06-06 | Created migration tracker               | Fork still contains Own content; Learnish brief not yet captured                                                          | —     |
| 2026-06-06 | Captured Learnish Phase 0 product brief | Kids 5–17 L&D platform for parents; UZ/Central Asia; community-led; app signup = primary CTA; north-star = family signups | —     |
| 2026-06-06 | Redesign milestone model                | Own's 10→100→1,000 merchants doesn't fit a B2C family product; move to families/signups-based phases                      | —     |
| 2026-06-06 | Keep some Own e-commerce research       | STEAM toys store is real commerce; local payments/delivery/marketplace research is partially reusable                     | —     |
| 2026-06-06 | Split competitors: attention vs category | Attention (TikTok/YouTube/Roblox/Netflix) frames the problem + emotional tension; category (Khan Academy Kids, KiwiCo, Outschool) frames alternatives | —     |
| 2026-06-06 | Pricing by COGS: digital per-family, physical per-child | Digital marginal cost ~$0 (give generously, fuels signups); kits cost $15–20 each so must be per-child to protect margin | —     |
| 2026-06-06 | Annual-prepay subscription is the focus  | Funds kit costs upfront, cuts churn at quarterly shipment moment; see `pricing/monetization-model.md`                     | —     |
| 2026-06-06 | Workshops = revenue line AND acquisition engine | 40/30/30 split → ~$19K/mo to platform at target; in-person sessions also build trust + feed signups (community motion)    | —     |
| 2026-06-06 | Included workshops are not free to bundle | 60% (teacher+venue) flows out per seat (~$9–12/child); 4/yr = ~$36–48 COGS → bundle margin ≈ 26–47%                       | —     |
| 2026-06-07 | Brand the offer as "Learnish Club"      | Membership + community framing suits word-of-mouth motion; boosts identity/retention; non-members still pay à la carte    | —     |
| 2026-06-07 | Family tiers: Solo / Family(3) / Big Family(5) / 5+ contact | Physical scales per child (floored ~$12–13/mo/child); volume discount comes from free digital layer, not kits | —     |
| 2026-06-07 | Workshop ops via student ambassadors    | Teachers sourced locally; ops comped with benefits not payroll → 40% stays ~pure margin + doubles as community/acquisition | —     |
| 2026-06-07 | Sell Digital tier standalone            | All-digital, ~100% margin, low-price entry to the Club; matches $5 entertainment anchor                                   | —     |
| 2026-06-07 | Store credits: Full Club = 2× rate      | Loops subscription spend back into the STEAM toys store; base credit rate still TBD                                       | —     |
| 2026-06-07 | ≥4 workshops included (guaranteed seats) | Confirms ~$36–48/child/yr COGS in the bundle; not empty-seat comped                                                      | —     |
| 2026-06-07 | Phase 2 GTM spine rewritten for Learnish | Playbook, operating principles, and 6-month plan moved from Own (merchants) to Learnish (families); built on Phase 0 brief + monetization model | —     |
| 2026-06-07 | Playbook built around the workshop flywheel | Community-led motion: workshop → free signup → Digital Club → Full Club → referrals; workshops are acquisition + trust engine, not just a revenue line | —     |
| 2026-06-07 | Milestone = paying Club families (10 → 100 → 1,000) | Kept filenames as slots; family signups stay the north-star; paying families gate each phase; 10,000 = next milestone beyond the playbook | —     |
| 2026-06-07 | Operating principles: LEGO / Duolingo / Disney | Replaces Apple/Google/Shopify "Own play"; moat = local in-person trust/community that global attention & EdTech apps can't replicate here | —     |
| 2026-06-07 | Phase 1 Foundation rewritten for Learnish | `.agents/product-marketing-context.md`, `README.md`, `brief.md`, `CONTRIBUTING.md` now describe Learnish; OQ register refreshed; thesis worksheet reset to blanks | —     |
| 2026-06-07 | Phase 3 Brand & voice rewritten for Learnish | `brand-voice/` + `brand-review/` moved from Own (merchants) to Learnish; voice built on the dual parent(buy)/kid(use) audience with trust-wins rule, LEGO/Duolingo/Disney analogs, UZ/RU language matrix, and safety/claim hard gates in the review rubric | —     |


---

## Notes & blockers



- **Open (validate in Phase 4):** Willingness-to-pay for the family price points (~$18 / $40 / $60 per mo) and ~$5–8/mo digital tier.
- **Open:** Base store-credit rate (then 2× for Full Club) — watch margin impact.
- **Open:** Confirm which line leads messaging — currently leaning **Learnish Club** membership.
- **Fork source:** Repo content is Own (Uzbekistan e-commerce GTM). Repo name/remote already say `learnish-marketing`.
- **Phase 1 + 2 + 3 done (2026-06-07):** Foundation (`.agents/product-marketing-context.md`, `README.md`, `brief.md`, `CONTRIBUTING.md`, OQ register, thesis reset), the GTM spine (`docs/playbook/`, `docs/strategy/operating-principles.md`, `docs/plan-6m/`), and Brand & voice (`brand-voice/`, `brand-review/`) are all Learnish.
- **Founder action (not blocking):** Fill in the reset `founder-team-thesis-alignment.md` for Learnish.
- **Next action:** Phase 4 — Measurement (`performance-analytics/`): funnel definition, KPI tree, experiments log, weekly report template. Validate willingness-to-pay and define funnel stages for the Learnish family journey.

---

## Related docs

- [Monetization model](../pricing/monetization-model.md) — pricing architecture, unit economics, workshop P&L
- [Product marketing context](../.agents/product-marketing-context.md) — source of truth for all skills (needs rewrite)
- [Playbook index](playbook/README.md) — Learnish GTM phases (workshop flywheel)
- [Operating principles](strategy/operating-principles.md) — the Learnish strategic thesis (LEGO / Duolingo / Disney)
- [Open questions register](playbook/open-questions-register.md) — unresolved assumptions
- [Contributing](../CONTRIBUTING.md) — doc conventions

