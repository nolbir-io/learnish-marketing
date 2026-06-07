# Learnish — Go-to-Market & Marketing Operating System

> Make everyday learning **exciting** for kids 5–17 — safe, trusted, and built on real community.

This repository is the **marketing and go-to-market (GTM) brain** for **Learnish**, a safe, trusted kids' learning & development platform (ages 5–17) for parents in Uzbekistan / Central Asia. It is a **documentation repository** — there is no application code here. Everything is Markdown: strategy, playbooks, campaigns, brand voice, competitive research, content drafts, and the measurement system used to take Learnish from its first founding families to **1,000 families** and beyond.

If this is your first time here, read this page top to bottom, then open [`docs/playbook/README.md`](docs/playbook/README.md).

---

## What is Learnish?

**One-liner:** Learnish is a safe, trusted learning & development platform that makes everyday learning exciting for kids aged 5–17.

- **Category:** B2C kids/family EdTech — multi-modal (app + courses + STEAM kits + in-person workshops + commerce), framed as the **Learnish Club**.
- **The thesis:** The real competitor for a child's afternoon is passive screen time (YouTube, TikTok, Roblox). The company that wins gives kids something **exciting and safe** to do instead — and earns the parent's trust through **local, in-person community**, not just another app.
- **The wedge:** **Weekend workshops** in Tashkent — they make "safe and trusted" tangible, fill the top of the funnel with free family signups, and seed word of mouth.
- **The moat:** Local depth and in-person trust — real teachers, real venues, parents who meet — which a global attention app or a global EdTech app structurally cannot replicate here.
- **The north-star:** **Family account signups.** Primary CTA: *download the app / create a family account.*
- **The goal:** **1,000 paying families** via a phased, community-led GTM (first 10 → 100 → 1,000 families).

For the full product context (audience, personas, objections, positioning), see [`.agents/product-marketing-context.md`](.agents/product-marketing-context.md). For pricing and unit economics, see [`pricing/monetization-model.md`](pricing/monetization-model.md).

---

## How this repository is organized

The repo has two layers:

1. **`docs/` — the strategy and operating system.** The playbook (phases), the 6-month execution plan, and strategy notes. This is where decisions are made and tracked.
2. **Root workstream folders — the workshops.** Each functional area (brand, campaigns, competitive research, content, analytics, SEO, sales) has its own folder with a `README.md` explaining its purpose. The playbook **pulls from** these folders and **pushes decisions back** into them.

```
.
├── README.md                       ← you are here
├── brief.md                        ← short pointer into the playbook
├── CONTRIBUTING.md                 ← how to update docs (ownership, review, naming)
├── founder-team-thesis-alignment.md← founding-team alignment worksheet
│
├── docs/                           ← STRATEGY & OPERATING SYSTEM
│   ├── migration-tracker.md        ← Own → Learnish migration progress
│   ├── playbook/                   ← phased GTM playbook (start here)
│   │   ├── README.md               ← playbook index + phases 0–3
│   │   ├── phase-0-foundation.md
│   │   ├── phase-1-first-10.md     ← first 10 founding families
│   │   ├── phase-2-first-100.md    ← first 100 families
│   │   ├── phase-3-first-1000.md   ← first 1,000 families
│   │   ├── operating-cadence.md    ← weekly/monthly/quarterly rituals
│   │   ├── governance-raci.md      ← decision rights
│   │   └── open-questions-register.md ← unresolved assumptions + decisions
│   ├── plan-6m/                    ← month-by-month execution roadmap (M1–M6)
│   └── strategy/                   ← strategy notes (e.g. operating-principles.md)
│
├── pricing/                        ← monetization model (Club tiers, unit economics)
├── brand-voice/                    ← how Learnish sounds (voice guide, language matrix)
├── brand-review/                   ← how content gets checked (rubric, review log)
├── campaigns/                      ← campaign & workshop briefs per phase + calendar
├── competitive-analysis/           ← attention-vs-category market map, signals tracker
├── competitive-brief/              ← positioning brief template
├── competitor-profiles/            ← competitor profiles + raw research
├── content-creation/               ← drafts: paid ads, social (Instagram, etc.)
├── landing-pages/                  ← landing page copy (e.g. family signup)
├── performance-analytics/          ← KPI tree, funnel definition, experiments log, reporting
├── sales-enablement/               ← decks and collateral
└── seo-audit/                      ← keyword universe + technical audit
```

> Almost every folder contains its own `README.md` describing its purpose and what belongs in it. When in doubt, open the folder's README first.

---

## The playbook: the road to 1,000 families

The core of this repo is a **phased, community-led GTM playbook** built around the **workshop flywheel**: *weekend workshop → free family signup (north-star) → Digital Club → Full Club → referrals*. Each phase answers the same five questions: **Goal · ICP focus · Motion · Channels & content · Exit criteria.**

| # | Phase | Goal |
|---|-------|------|
| 0 | [Foundation](docs/playbook/phase-0-foundation.md) | Sharpen positioning, the parent ICP, and the Club offer enough to sell. |
| 1 | [First 10 families — Founding cohort](docs/playbook/phase-1-first-10.md) | Run lighthouse workshops and convert parents into a founding cohort. |
| 2 | [First 100 families — Early adopters](docs/playbook/phase-2-first-100.md) | Prove the flywheel repeats without the founder in every session. |
| 3 | [First 1,000 families — Scale](docs/playbook/phase-3-first-1000.md) | Industrialize the workshop network across districts and regions. |

Running alongside the phases is a **[6-month execution roadmap](docs/plan-6m/README.md)** (Month 01 → Month 06), which translates strategy into monthly priorities.

The strategic spine is [`docs/strategy/operating-principles.md`](docs/strategy/operating-principles.md) — "the Learnish play": **LEGO's crafted, safe play × Duolingo's free-core habit and word-of-mouth brand × Disney's family trust and rituals**, all built on a local, in-person community moat.

---

## How to use this repo (by role)

- **New to the project?** Read this README → [`docs/playbook/README.md`](docs/playbook/README.md) → the current phase doc.
- **Founder / strategy:** [`founder-team-thesis-alignment.md`](founder-team-thesis-alignment.md) and [`docs/strategy/operating-principles.md`](docs/strategy/operating-principles.md).
- **Running execution week to week:** [`docs/plan-6m/`](docs/plan-6m/) + [`docs/playbook/operating-cadence.md`](docs/playbook/operating-cadence.md).
- **Writing copy or content:** start in [`brand-voice/`](brand-voice/), draft in [`content-creation/`](content-creation/), then check against [`brand-review/`](brand-review/).
- **Researching the market:** [`competitive-analysis/`](competitive-analysis/), [`competitor-profiles/`](competitor-profiles/), [`competitive-brief/`](competitive-brief/).
- **Pricing & monetization:** [`pricing/monetization-model.md`](pricing/monetization-model.md).
- **Measuring results:** [`performance-analytics/`](performance-analytics/) (KPI tree, funnel definition, experiments log).

---

## Working conventions

A few conventions keep this repo coherent (full version in [`CONTRIBUTING.md`](CONTRIBUTING.md)):

- **One document, one purpose.** Keep docs focused; use kebab-case filenames.
- **Every active doc names a single owner (DRI)** and, where relevant, a success metric and review cadence.
- **Decisions are tracked, not silently overwritten.** When an assumption changes, log it in [`docs/playbook/open-questions-register.md`](docs/playbook/open-questions-register.md) and keep changelog rows where present.
- **Strategy and execution stay in sync.** Every strategy change should show up in the execution docs (and vice versa).
- **`[unknown]` / `[to-validate]` markers are intentional.** They flag open questions that still need a decision — don't delete them, resolve them.

---

## Invoking skills as slash commands

Every marketing skill in [`.agents/skills/`](.agents/skills/) has a matching **Cursor slash command** in [`.cursor/commands/`](.cursor/commands/). Type `/` in Cursor chat and pick one (e.g. `/seo-audit`, `/cro`, `/launch`) to run that workflow on demand. Each command:

- reads [`.agents/product-marketing-context.md`](.agents/product-marketing-context.md) first (the shared context every skill relies on),
- then reads and follows the matching `SKILL.md`,
- lists its **group** and **cross-referenced** sibling skills so related workflows are one hop away.

Anything you type after the command (e.g. `/cro audit our pricing page`) is treated as the scope for that run. Start with [`/product-marketing`](.cursor/commands/product-marketing.md) if the shared context file is missing or thin.

The commands mirror the skill taxonomy and are **generated**, not hand-maintained. After skills change, regenerate them:

```bash
python3 .agents/generate-skill-commands.py
```

| Group | Commands |
|-------|----------|
| Foundation | `/product-marketing` |
| SEO & Content | `/seo-audit` `/ai-seo` `/site-architecture` `/programmatic-seo` `/schema` `/content-strategy` `/aso` |
| CRO | `/cro` `/signup` `/onboarding` `/popups` `/paywalls` |
| Content & Copy | `/copywriting` `/copy-editing` `/cold-email` `/emails` `/social` `/video` `/image` `/sms` |
| Paid & Measurement | `/ads` `/ad-creative` `/ab-testing` `/analytics` |
| Growth & Retention | `/referrals` `/free-tools` `/churn-prevention` `/community-marketing` `/lead-magnets` `/co-marketing` |
| Sales & GTM | `/revops` `/sales-enablement` `/launch` `/pricing` `/competitors` `/competitor-profiling` `/directory-submissions` `/prospecting` `/gtm-partnership-architecture` |
| Strategy | `/marketing-ideas` `/marketing-psychology` `/customer-research` `/marketing-plan` |

---

## Status

Working scaffold, migrating from a forked Own (Uzbekistan e-commerce) GTM into Learnish. The phase structure (10 → 100 → 1,000 families) is a working default to be revised once real ICP, timeline, and budget numbers are validated. Open assumptions (willingness to pay, founder bandwidth, budget, language posture) are tracked in the [playbook index](docs/playbook/README.md) and the [open-questions register](docs/playbook/open-questions-register.md).

**Tracking the Own → Learnish migration?** See [`docs/migration-tracker.md`](docs/migration-tracker.md).
