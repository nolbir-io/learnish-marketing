# Social posts

Channel-specific post drafts for Learnish. Source-of-truth for what we publish on **Instagram** (parents + kid delight), **Telegram** (primary parent comms + community), and **LinkedIn** (investors / partners / hiring).

## Channel roles (decided)

- **Instagram** — local awareness + real session proof. Parent-facing trust + kid delight. 3×/week.
- **Telegram** — primary parent comms + per-district community groups. Workshop invites, recaps, referral asks. Ongoing around each workshop.
- **LinkedIn** — repurposed for **investors, partners (venues/schools/brands), and hiring/ambassadors** — *not* parents. 1×/week.

## Folder layout

```
social/
  README.md                # this file — conventions
  calendar.md              # master cross-channel timeline
  instagram/
    YYYY-MM.md             # all Instagram posts in a given campaign batch
  linkedin/
    YYYY-MM.md             # all LinkedIn posts in a given campaign batch
  telegram/                # district-group templates, invites, recaps (add as needed)
  _archive/                # closed months / superseded drafts
```

## Naming convention

- One file per channel per campaign-batch month: `social/instagram/2026-06.md`.
- File month = the month the batch *starts*. Posts that spill into early next month stay in the start-month file. A new file starts when the next month has its own batch.
- Each post gets a stable ID: `IG-YYYY-MM-NN` / `LI-YYYY-MM-NN` / `TG-YYYY-MM-NN`.

## Post header format

Every post starts with this header so it's greppable and shows up cleanly in the calendar:

```
### IG-2026-06-01 · Carousel · Draft · Safe-and-trusted
Publish: 2026-06-08
Campaign: Phase 1 — First 10 trusted families
```

**Fields:**

- **ID** — stable across edits.
- **Format** — Carousel · Single · Reel · Quote · Long-form
- **Status** — Draft · In review · Approved · Scheduled · Published · Archived
- **Theme** — short tag (e.g. Safe-and-trusted, Workshop-invite, Local-and-human, Founding-family, Make-screen-time-count)
- **Publish** — ISO date
- **Campaign** — which phase brief this supports

## Status workflow

`Draft` → `In review` (brand-review check) → `Approved` → `Scheduled` → `Published` → `Archived`.

## Voice and proof rules

All posts clear [`brand-voice/voice-guide.md`](../../brand-voice/voice-guide.md). Lead **safe & trusted (reviewed, age-appropriate content)** and the tangible **workshops + STEAM toys**; the Learnish Club is the wrapper. Two audiences at once: parents (trust) + kids 5–17 (delight) — **trust wins** when they conflict. **Nish (the bee) is kid-facing only.** No fabricated stats or testimonials; real session photos/quotes with consent; pricing as **intro, being validated**; placeholders marked `[PROOF — to collect]`.

## Languages

English source. Translate **Uzbek (primary, parent first-touch)** + **Russian (secondary)** per [`brand-voice/language-matrix.md`](../../brand-voice/language-matrix.md) before publish. Native review required for any safety/wellbeing wording.

## When to start a new file

- A new calendar month has its own batch → new `YYYY-MM.md`.
- A batch grows past ~20 posts in one file → split by theme.

## Index updates

When you add or change a post, update [`social/calendar.md`](calendar.md) so the cross-channel timeline stays current.
