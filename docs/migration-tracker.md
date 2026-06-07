# Learnish migration tracker

> **Purpose:** Track progress migrating this repo from the forked **Own** (Uzbekistan e-commerce GTM) content to **Learnish** marketing operations.
>
> **Status:** Phases 0–6 done. **Phase 6 fully complete** — all `campaigns/` (README + phase-1/2/3 briefs + calendar) and all of `content-creation/` (READMEs, editorial calendar, paid-ads batch, social READMEs + Instagram/LinkedIn drafts + social calendar) rewritten for Learnish on the workshop flywheel. Next: Phase 7 (SEO), then Phase 8 (skills cleanup, low priority). See [`pricing/monetization-model.md`](../pricing/monetization-model.md) and [`playbook/README.md`](playbook/README.md).
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
| 4     | Measurement              | Done        | —      | Funnel (live vs planned), KPI tree, WTP research, weekly report, experiments log |
| 5     | Competitive intelligence | Done        | —      | 4 Learnish profiles (attention vs category), market map, battlecard; Own profiles archived |
| 6     | Campaigns & content      | Done        | —      | All campaigns/ + content-creation/ rewritten for Learnish (workshop flywheel) |
| 7     | SEO                      | Not started | —      |                                          |
| 8     | Skills cleanup           | Not started | —      | Low priority                             |


**Rough completion:** 6 / 8 phases done (Phase 1–6). Remaining: Phase 7 (SEO), Phase 8 (skills cleanup, low priority).

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


| Task                   | File(s)                                            | Status | Done |
| ---------------------- | -------------------------------------------------- | ------ | ---- |
| Funnel definition      | `performance-analytics/funnel-definition.md`       | Done   | [x]  |
| KPI tree               | `performance-analytics/kpi-tree.md`                | Done   | [x]  |
| Willingness-to-pay plan| `performance-analytics/willingness-to-pay-research.md` | Done | [x]  |
| Experiments log        | `performance-analytics/experiments-log.md`         | Done   | [x]  |
| Weekly report template | `performance-analytics/weekly-report-template.md`  | Done   | [x]  |
| Folder README          | `performance-analytics/README.md`                  | Done   | [x]  |


**Phase 4 exit criteria**

- [x] Funnel stages match Learnish buyer journey (not merchant signed → live → transacting)
- [x] North-star and supporting metrics defined in KPI tree

> **Note — live vs planned:** App/courses aren't shipped (content rolls out entertainment → math → languages → other), so funnel/KPI stages are tagged `live` (STEAM store + workshops) vs `planned` (app digital tiers). WTP survey (Van Westendorp + Gabor-Granger) drafted to validate price points (OQ-001). "Active family" = Weekly Active Family primary, Monthly secondary (OQ-010).

---

## Phase 5 — Competitive intelligence

*Mostly replace — current research is e-commerce / Uzbekistan specific.*


| Task                      | File(s)                                                  | Status | Done |
| ------------------------- | -------------------------------------------------------- | ------ | ---- |
| Competitor summary        | `competitor-profiles/_summary.md`                        | Done   | [x]  |
| Market map                | `competitive-analysis/market-map.md`                     | Done   | [x]  |
| Analysis README           | `competitive-analysis/README.md`                         | Done   | [x]  |
| Signals tracker           | `competitive-analysis/signals-tracker.md`                | Done   | [x]  |
| Battlecard template       | `competitive-brief/template.md`                          | Done   | [x]  |
| Brief README              | `competitive-brief/README.md`                            | Done   | [x]  |
| Profile #1 (attention)    | `competitor-profiles/youtube-kids.md`                    | Done   | [x]  |
| Profile #2 (digital app)  | `competitor-profiles/khan-academy-kids.md`               | Done   | [x]  |
| Profile #3 (STEAM kits)   | `competitor-profiles/steam-subscription-boxes.md`        | Done   | [x]  |
| Profile #4 (in-person)    | `competitor-profiles/local-tutoring-and-clubs.md`        | Done   | [x]  |


**Archive (Own fork — moved to `_archive/own-fork/competitor-profiles/`)**


| File                                               | Done |
| -------------------------------------------------- | ---- |
| `shopify.md`                                       | [x]  |
| `woocommerce.md`                                   | [x]  |
| `uzbekistan-landscape.md` (kept for partial reuse) | [x]  |
| `raw/` (desk research scrapes)                     | [x]  |


**Phase 5 exit criteria**

- [x] At least 3 Learnish-relevant competitor profiles exist (4 written)
- [x] Market map and summary reflect Learnish category
- [x] Own-specific profiles archived or removed

> **Note:** Profiles are desk-level from general knowledge — pricing/figures marked "approximate, verify." Highest-value follow-up: **name real local players** (Tashkent tutoring chains, kids clubs, local STEAM-toy sellers) for full profiles. Reusable local-commerce facts (Uzum, payments, logistics, regulation) pulled forward into the market map from the archived `uzbekistan-landscape.md`.

---

## Phase 6 — Campaigns & content


| Task                            | File(s)                                                | Status      | Done |
| ------------------------------- | ------------------------------------------------------ | ----------- | ---- |
| Campaign README                 | `campaigns/README.md`                                  | Done        | [x]  |
| Phase 1 brief                   | `campaigns/phase-1-brief.md`                           | Done        | [x]  |
| Phase 2 brief                   | `campaigns/phase-2-brief.md`                           | Done        | [x]  |
| Phase 3 brief                   | `campaigns/phase-3-brief.md`                           | Done        | [x]  |
| Campaign calendar               | `campaigns/calendar.md`                                | Done        | [x]  |
| Paid ads README                 | `content-creation/paid-ads/README.md`                  | Done        | [x]  |
| Paid ads draft                  | `content-creation/paid-ads/2026-06-brand-awareness.md` | Done        | [x]  |
| Social README                   | `content-creation/social/README.md`                    | Done        | [x]  |
| Social calendar                 | `content-creation/social/calendar.md`                  | Done        | [x]  |
| Instagram draft                 | `content-creation/social/instagram/2026-06.md`         | Done        | [x]  |
| LinkedIn draft                  | `content-creation/social/linkedin/2026-06.md`          | Done        | [x]  |
| Content README                  | `content-creation/README.md`                           | Done        | [x]  |
| Landing page (rename + rewrite) | `landing-pages/merchant-signup.md` → `workshop-signup.md` | Done        | [x]  |
| Sales deck (replace)            | `sales-enablement/decks/marketplace-escape-deck.md` → `venue-partner-deck.md` (Own deck archived) | Done | [x]  |


**Phase 6 exit criteria**

- [x] At least one landing page draft with Learnish CTA (`landing-pages/workshop-signup.md` — book-a-workshop)
- [x] One campaign brief aligned to current playbook phase (`campaigns/phase-1-brief.md` — First 10 trusted families)
- [x] Own-specific sales deck archived or replaced (archived to `_archive/own-fork/`; replaced by `venue-partner-deck.md`)

> **Note — Phase 6 fully complete (2026-06-07):** All deferred items are now rewritten for Learnish. `campaigns/` README + phase-2/3 briefs + calendar follow the Phase 1 brief model (workshop flywheel; gates on paying Club families 10→100→1,000; north-star = free family signups). `content-creation/` README + editorial calendar reorganize content around the workshop schedule (one workshop → reel + posts + Telegram recap + email). `paid-ads/` reframed as a small **community-led local workshop-promotion** batch (Meta + Telegram; Google/YouTube reserved for Phase 3; angle S "safe & trusted" leads; soft CTA = book a free workshop). `social/` README + calendar + Instagram (parent trust + kid delight) + LinkedIn (investors/partners/hiring) drafts written. Applied throughout: workshop landing page is the lead LP; English source + Uzbek-lead/RU translation; Club pricing shown as "intro pricing, being validated"; Nish kid-facing only; real session proof with consent or `[PROOF — to collect]`.

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
| Funnel stages match Learnish journey                                                    | [x]  |
| ≥3 competitor profiles for Learnish                                                     | [x]  |
| ≥1 landing page draft exists                                                            | [x]  |
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
| 2026-06-07 | Phase 4 Measurement rewritten for Learnish | `performance-analytics/` moved from Own merchant funnel to the Learnish family journey; funnel/KPIs tagged live (store+workshops) vs planned (app); WTP research (Van Westendorp + Gabor-Granger) added | —     |
| 2026-06-07 | Funnel tagged live vs planned | App not shipped (content sequence: entertainment → math → languages → other); measure today's real surfaces (STEAM store + workshops), scaffold app metrics for launch | —     |
| 2026-06-07 | Active family = Weekly primary, Monthly secondary | Lead retention reads on WAF (≥1 kid had a session in 7d); MAF smooths; pre-app proxy = workshop/store activity in 30d (closes OQ-010 definition) | —     |
| 2026-06-07 | Phase 5 Competitive intelligence rewritten for Learnish | Replaced Own (Shopify/WooCommerce) with 4 Learnish profiles on the attention-vs-category frame; archived Own profiles; reused local-commerce facts for the toy store | —     |
| 2026-06-07 | Competitor frame = attention vs category | Two competitions: attention (YouTube/TikTok/Roblox) frames the problem+guilt; category (Khan/Duolingo apps, KiwiCo/MEL kits, local centers, Uzum toys) frames the spend. Moat = local in-person trust no global player can match | —     |
| 2026-06-07 | Local centers: compete AND partner | Local tutoring centers/kids clubs own the trust Learnish wants; convert them into workshop venues (the model's 30% share) rather than pure rivals | —     |
| 2026-06-07 | Phase 6 started — exit criteria first | Built the 3 exit-criteria deliverables before the full content rewrite: workshop landing page, Phase 1 brief, deck replacement. Remaining `campaigns/` + `content-creation/` deferred to a later pass | —     |
| 2026-06-07 | Lead landing page = workshop signup | App/courses not shipped; workshops are the live surface and top of the flywheel. Replaced `merchant-signup.md` (book-a-launch-call) with `workshop-signup.md` (book-a-weekend-workshop-seat); secondary CTA = free family account | —     |
| 2026-06-07 | Sales deck → venue/partner deck | Learnish is B2C/word-of-mouth-led, so a B2B sales deck doesn't fit; the only "sales" motion that matters is recruiting local centers as workshop venues (40/30/30 split). Own deck archived to `_archive/own-fork/`; new `venue-partner-deck.md` created | —     |
| 2026-06-07 | "First 10 trusted families" framing | Renamed Phase 1 cohort from "founding families" to "first 10 trusted families" (per founder); chosen for trust + referral reach, not revenue | —     |
| 2026-06-07 | Public pricing = "intro, being validated" | Show Club tiers honestly with a validation caveat (WTP is Phase 4); never present unvalidated prices as final. Store/site = `learnish.uz`. Workshop specifics kept as `[PROOF — to collect]` placeholders | —     |
| 2026-06-07 | Phase 6 finished — campaigns + content rewritten | All `campaigns/` + `content-creation/` moved from Own (merchants) to Learnish (families). Phase 2/3 briefs mirror the playbook (gates on paying Club families 10→100→1,000; north-star = free signups); content reorganized around the workshop flywheel | —     |
| 2026-06-07 | Paid = community-led local workshop top-up | Reframed the paid-ads batch from an Own "merchant movement" awareness push to a small, district-level Tashkent batch (Meta + Telegram) whose only job is filling free workshops + growing the Telegram community; Google/YouTube reserved for Phase 3; never a cold "buy the Club" push | —     |
| 2026-06-07 | Social channel roles fixed | Instagram = parent awareness + kid delight; Telegram = primary parent comms + per-district community (event-driven around workshops); LinkedIn = investors/partners/hiring, not parents. Lead angle everywhere = "safe & trusted (reviewed, age-appropriate)" + free first workshop; Nish kid-facing only | —     |


---

## Notes & blockers



- **Open (validate in Phase 4):** Willingness-to-pay for the family price points (~$18 / $40 / $60 per mo) and ~$5–8/mo digital tier.
- **Open:** Base store-credit rate (then 2× for Full Club) — watch margin impact.
- **Open:** Confirm which line leads messaging — currently leaning **Learnish Club** membership.
- **Fork source:** Repo content is Own (Uzbekistan e-commerce GTM). Repo name/remote already say `learnish-marketing`.
- **Phase 1–6 done (2026-06-07):** Foundation, the GTM spine, Brand & voice, Measurement, Competitive intelligence, and Campaigns & content are all Learnish.
- **Founder action (not blocking):** Fill in the reset `founder-team-thesis-alignment.md` for Learnish.
- **Product reality (affects measurement):** App/courses not shipped — only STEAM store + workshops are live today; course content rolls out entertainment → math → languages → other. Funnel/KPI docs tag stages live vs planned.
- **Phase 5 research debt:** Profiles are desk-level — the priority follow-up is naming **real local competitors** (Tashkent tutoring chains, kids clubs, local STEAM-toy sellers) and verifying pricing/figures.
- **Phase 6 complete (2026-06-07):** workshop landing page + Phase 1 brief + venue/partner deck, **plus** all remaining `campaigns/` (README, phase-2/3 briefs, calendar) and all of `content-creation/` (READMEs, editorial calendar, paid-ads batch, social READMEs + Instagram/LinkedIn drafts + social calendar) rewritten for Learnish on the workshop flywheel.
- **Next action:** Phase 7 (SEO) — `seo-audit/keyword-universe.md` (still Own: merchant onboarding/payment ops clusters), `technical-audit.md`, `README.md`. Then Phase 8 (skills cleanup, low priority) and the final-verification grep.
- **Telegram drafts:** social channel split is decided (IG + Telegram + LinkedIn) and Telegram is referenced as primary parent comms; concrete per-district Telegram templates (`content-creation/social/telegram/`) are to be added as workshops are scheduled (event-driven, not a fixed batch).

---

## Related docs

- [Monetization model](../pricing/monetization-model.md) — pricing architecture, unit economics, workshop P&L
- [Product marketing context](../.agents/product-marketing-context.md) — source of truth for all skills (needs rewrite)
- [Playbook index](playbook/README.md) — Learnish GTM phases (workshop flywheel)
- [Operating principles](strategy/operating-principles.md) — the Learnish strategic thesis (LEGO / Duolingo / Disney)
- [Open questions register](playbook/open-questions-register.md) — unresolved assumptions
- [Contributing](../CONTRIBUTING.md) — doc conventions

