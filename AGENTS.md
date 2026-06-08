# AGENTS.md

Guidance for AI agents working in this repository.

## What this repo is

This is a **documentation-only** GTM (go-to-market) repository for **Own**, an e-commerce infrastructure company in Uzbekistan. There is no application server, frontend, database, or Docker stack. Content is Markdown plus Cursor marketing skills and slash commands.

See `README.md` for the full map of folders and the phased playbook (10 → 100 → 1,000 merchants).

## Cursor Cloud specific instructions

### No runtime services

Nothing needs to be started for local development. There is no `npm install`, `docker compose up`, or dev server. Agents edit Markdown and optionally regenerate Cursor slash commands.

### System requirements

- **Git** — version control
- **Python 3.12+** — only for `.agents/generate-skill-commands.py` (stdlib only; no pip packages)

### Regenerating slash commands

After `.agents/skills/` changes, regenerate `.cursor/commands/`:

```bash
python3 .agents/generate-skill-commands.py
```

This is idempotent. Expect `Wrote 44 command(s) to .cursor/commands` when all skills are present.

### Lint / test / build

There is no formal linter, test suite, or build step. Validation options:

1. Run the generator above and confirm skill/command parity (44 skills ↔ 44 commands).
2. Quick sanity check:

```bash
python3 -c "from pathlib import Path; s=set(p.name for p in Path('.agents/skills').iterdir() if (p/'SKILL.md').exists()); c=set(p.stem for p in Path('.cursor/commands').glob('*.md')); assert s==c; print('OK:', len(s), 'skills/commands')"
```

### Core workflow (hello world)

1. Read `.agents/product-marketing-context.md` for shared product/ICP context.
2. Pick a slash command from `.cursor/commands/` (e.g. `/seo-audit`, `/cro`, `/launch`).
3. Read the matching `.agents/skills/<name>/SKILL.md` and follow it against docs in the relevant workstream folder (`seo-audit/`, `campaigns/`, etc.).

### Conventions

Follow `CONTRIBUTING.md`: one doc per purpose, kebab-case filenames, DRI ownership in metadata, log assumption changes in `docs/playbook/open-questions-register.md`.

### External dependencies

None for repo development. Skills are vendored from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (see `skills-lock.json`). Some skills reference optional external MCP tools for live research; those are not required to work in this repo.
