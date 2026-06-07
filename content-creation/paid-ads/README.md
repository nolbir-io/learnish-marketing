# Paid ads

Small, **local** workshop-promotion batches for Learnish. Learnish is community/word-of-mouth-led — paid is a **minimal top-up to fill weekend workshop seats and grow the local following**, not a primary acquisition engine. Source-of-truth for what we run on Meta (Instagram/Facebook) and Telegram, with Google/YouTube reserved for Phase 3 scale.

> **Strategic note — community-led, not ad-led.** The trust engine is the in-person workshop, not the ad. Paid here does one job: get more local parents to a free first workshop (and into the Telegram community). Keep budgets small and tightly geo-targeted to Tashkent districts near a confirmed venue. Judge creative only after ~1,000+ impressions per asset and let the 1–2 strongest angles carry the spend. Never run a hard "buy the Club" push in cold paid — the Club is introduced *after* a workshop earns trust.

## Folder layout

```
paid-ads/
  README.md                          # this file — conventions
  YYYY-MM-<objective>.md             # one file per campaign batch (objective + month)
  _archive/                          # closed / superseded batches
```

## Naming convention

- One file per objective per batch: `paid-ads/2026-06-brand-awareness.md`.
- File month = the month the batch *starts*.
- Each ad inside a file gets a stable ID: `<PLATFORM>-<OBJECTIVE>-NN`, e.g. `META-AWR-01`, `TG-AWR-02`.

## What each batch file holds

1. **Campaign header** — objective, KPI, phase tie-in, languages, market/geo.
2. **Audience configuration** — per platform: geo (district-level), demographics (parents 28–45), interests, custom/lookalike, exclusions, recommended objective + bid strategy.
3. **Ad creative** — organized by angle, then by platform, with character counts validated against each platform's limits.
4. **Production + tracking notes** — UTM scheme, localization status, brand-review status.

## Character-count rule

Every headline / description / primary-text line carries its character count in parentheses, e.g. `(28)`. Anything over a platform limit is flagged and trimmed inline. English is the source language; **Cyrillic (Russian) and Uzbek counts differ and must be re-validated after localization** in each platform's preview tool before launch.

## Voice and proof rules

All creative clears [`brand-voice/voice-guide.md`](../../brand-voice/voice-guide.md). Lead **safe & trusted (reviewed, age-appropriate content)** and the tangible **workshops + STEAM toys**. No fabricated stats or testimonials. Pricing shows as **intro, being validated**; session specifics (date, venue, what's built) are real or marked `[PROOF — to collect]`. **Nish (the bee) is kid-facing only** — keep Nish out of the parent trust line.

## Languages

English source. Translate **Uzbek (primary, parent first-touch)** + **Russian (secondary)** per [`brand-voice/language-matrix.md`](../../brand-voice/language-matrix.md) before publish. Native reviewer checks any safety/wellbeing wording.

## Status workflow

`Draft` → `In review` (brand-review check) → `Approved` → `Live` → `Archived`.
