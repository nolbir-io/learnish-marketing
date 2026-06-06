#!/usr/bin/env python3
"""Generate Cursor slash-commands (.cursor/commands/*.md) from the marketing skills.

Each skill in .agents/skills/<name>/SKILL.md becomes an invokable Cursor command
(`/<name>`). The generated command tells the agent to read the shared
product-marketing context first, then read and follow the skill, and points at
related skills via the cross-reference map taken from the marketingskills
taxonomy.

Run from the repo root:  python3 .agents/generate-skill-commands.py
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / ".agents" / "skills"
COMMANDS_DIR = REPO_ROOT / ".cursor" / "commands"
CONTEXT_FILE = ".agents/product-marketing-context.md"

# Functional groups from the marketingskills taxonomy.
GROUPS: dict[str, list[str]] = {
    "Foundation": ["product-marketing"],
    "SEO & Content": [
        "seo-audit", "ai-seo", "site-architecture", "programmatic-seo",
        "schema", "content-strategy", "aso",
    ],
    "CRO": ["cro", "signup", "onboarding", "popups", "paywalls"],
    "Content & Copy": [
        "copywriting", "copy-editing", "cold-email", "emails", "social",
        "video", "image", "sms",
    ],
    "Paid & Measurement": ["ads", "ad-creative", "ab-testing", "analytics"],
    "Growth & Retention": [
        "referrals", "free-tools", "churn-prevention", "community-marketing",
        "lead-magnets", "co-marketing",
    ],
    "Sales & GTM": [
        "revops", "sales-enablement", "launch", "pricing", "competitors",
        "competitor-profiling", "directory-submissions", "prospecting",
        "gtm-partnership-architecture",
    ],
    "Strategy": [
        "marketing-ideas", "marketing-psychology", "customer-research",
        "marketing-plan",
    ],
}

# Explicit cross-references from the taxonomy diagram.
#   copywriting <-> cro <-> ab-testing
#   revops <-> sales-enablement <-> cold-email
#   seo-audit <-> schema <-> ai-seo
#   customer-research -> copywriting, cro, competitors
CROSS_REFS: dict[str, list[str]] = {
    "copywriting": ["cro", "ab-testing", "copy-editing", "emails"],
    "cro": ["copywriting", "ab-testing", "signup", "popups"],
    "ab-testing": ["cro", "copywriting", "analytics"],
    "revops": ["sales-enablement", "cold-email", "prospecting"],
    "sales-enablement": ["revops", "cold-email", "competitors"],
    "cold-email": ["revops", "sales-enablement", "prospecting", "emails"],
    "seo-audit": ["schema", "ai-seo", "programmatic-seo", "site-architecture"],
    "schema": ["seo-audit", "ai-seo"],
    "ai-seo": ["seo-audit", "schema", "content-strategy"],
    "customer-research": ["copywriting", "cro", "competitors", "product-marketing"],
}


def slug_to_title(slug: str) -> str:
    return slug.replace("-", " ").title()


def read_frontmatter(skill_path: Path) -> dict[str, str]:
    """Return name, description, and H1 title from a SKILL.md file."""
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    fm: dict[str, str] = {}
    body = text
    if match:
        block = match.group(1)
        body = text[match.end():]
        name_m = re.search(r"^name:\s*(.+)$", block, re.MULTILINE)
        if name_m:
            fm["name"] = name_m.group(1).strip().strip("\"'")
        desc_m = re.search(r"^description:\s*(.+)$", block, re.MULTILINE)
        if desc_m:
            fm["description"] = desc_m.group(1).strip().strip("\"'")
    # First H1 heading in the body becomes the human title.
    title_m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if title_m:
        fm["title"] = title_m.group(1).strip()
    return fm


def concise_description(full: str) -> str:
    """Trim the long trigger-laden description down to a one-line picker label."""
    if not full:
        return ""
    # Take the first sentence; strip a leading "When the user wants to".
    first = re.split(r"(?<=[.!?])\s", full.strip())[0]
    first = re.sub(r"^When the user wants to\s+", "", first, flags=re.IGNORECASE)
    first = first[:1].upper() + first[1:]
    # Keep it short.
    if len(first) > 160:
        first = first[:157].rstrip() + "..."
    return first


def group_for(skill: str) -> str:
    for group, members in GROUPS.items():
        if skill in members:
            return group
    return "Other"


def related_for(skill: str, group: str) -> list[str]:
    related = list(CROSS_REFS.get(skill, []))
    # Add same-group siblings (excluding self and Foundation), preserving order.
    if group not in ("Foundation",):
        for sibling in GROUPS.get(group, []):
            if sibling != skill and sibling not in related:
                related.append(sibling)
    return related


def build_command(skill: str, fm: dict[str, str]) -> str:
    title = fm.get("title") or slug_to_title(skill)
    desc = concise_description(fm.get("description", ""))
    group = group_for(skill)
    related = related_for(skill, group)
    is_foundation = skill == "product-marketing"

    related_line = (
        ", ".join(f"`/{r}`" for r in related) if related else "_none_"
    )

    # Cursor project slash commands are plain Markdown: the filename is the
    # command name and the whole file is the prompt body. No YAML frontmatter
    # (that format is for skills/rules, and Cursor mis-handles it in commands).
    lines: list[str] = []
    lines.append(f"# /{skill} — {title}")
    lines.append("")
    if desc:
        lines.append(f"> {desc}")
        lines.append("")
    lines.append(f"Invoke the **{skill}** marketing skill and follow it for this task.")
    lines.append("")
    lines.append("**Do this now:**")
    lines.append("")
    if is_foundation:
        lines.append(
            f"1. Read and follow `.agents/skills/{skill}/SKILL.md`. This is the "
            "foundation skill that every other skill reads first — its job is to "
            f"create or update `{CONTEXT_FILE}`."
        )
    else:
        lines.append(
            f"1. Read `{CONTEXT_FILE}` first for shared product, ICP, and "
            "positioning context (every skill relies on it). If it is missing or "
            "thin, consider running `/product-marketing` first."
        )
        lines.append(
            f"2. Read and follow `.agents/skills/{skill}/SKILL.md` for this request."
        )
    lines.append("")
    lines.append(f"**Group:** {group}")
    lines.append("")
    lines.append(f"**Cross-references** (use if the task spills into their domain): {related_line}")
    lines.append("")
    lines.append(
        f"Treat any text I type after `/{skill}` as the specific scope/request for "
        "this workflow. If I didn't add anything, ask me what to focus on before "
        "proceeding."
    )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
    skills = sorted(p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists())

    # Sanity: warn about skills that aren't placed in any group.
    ungrouped = [s for s in skills if group_for(s) == "Other"]
    if ungrouped:
        print(f"WARNING: ungrouped skills (placed in 'Other'): {ungrouped}")

    written = 0
    for skill in skills:
        fm = read_frontmatter(SKILLS_DIR / skill / "SKILL.md")
        content = build_command(skill, fm)
        (COMMANDS_DIR / f"{skill}.md").write_text(content, encoding="utf-8")
        written += 1

    print(f"Wrote {written} command(s) to {COMMANDS_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
