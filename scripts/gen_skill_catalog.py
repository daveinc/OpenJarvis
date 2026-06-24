"""
gen_skill_catalog.py — Auto-generate skills-catalog.md from installed HOD SKILL.md files.

Run this whenever skills are added, renamed, or updated.
Output: C:/Users/davei/.claude/skills/skills-catalog.md

Usage:
    python scripts/gen_skill_catalog.py
"""
from pathlib import Path
from datetime import date
from openjarvis.core.config import load_config
from openjarvis.skills.loader import discover_skills

cfg = load_config()
skills_dir = Path(cfg.skills.skills_dir)
output_path = skills_dir / "skills-catalog.md"

skills = discover_skills(skills_dir)

# Filter out _removed skills
active = [s for s in skills if "_removed" not in s.name]
active.sort(key=lambda s: s.name)


def best_description(s) -> str:
    """Return the best available description for a skill."""
    # If description is set and not just the skill name, use it
    if s.description and s.description.strip() not in ("", s.name):
        return s.description.strip()
    # Fall back to first non-empty non-heading line of markdown content
    if s.markdown_content:
        for line in s.markdown_content.splitlines():
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("---"):
                return line[:120]
    return s.name

# Group by tags if present, else "General"
tagged: dict[str, list] = {}
for s in active:
    categories = s.tags if s.tags else ["general"]
    for cat in categories:
        tagged.setdefault(cat, []).append(s)

# Canonical category order for routing
ORDER = ["ceo", "meta", "dev", "debug", "analysis", "project", "general"]
all_cats = sorted(tagged.keys(), key=lambda c: ORDER.index(c) if c in ORDER else 99)

lines = [
    f"# HOD Skills Catalog",
    f"*Auto-generated {date.today()} from `{skills_dir}`. Do not edit — run gen_skill_catalog.py to update.*",
    f"*{len(active)} active skills.*",
    "",
    "## Quick Router",
    "| Skill | Description | Tags |",
    "|---|---|---|",
]

for s in active:
    tags = ", ".join(s.tags) if s.tags else "—"
    desc = best_description(s)[:70]
    lines.append(f"| `{s.name}` | {desc} | {tags} |")

lines += ["", "---", ""]

for cat in all_cats:
    cat_skills = tagged[cat]
    lines.append(f"## {cat.title()}")
    for s in cat_skills:
        lines.append(f"**`{s.name}`**")
        desc = best_description(s)
        if desc and desc != s.name:
            lines.append(desc)
        if s.tags:
            lines.append(f"*Tags: {', '.join(s.tags)}*")
        lines.append("")
    lines.append("---")
    lines.append("")

output_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Written: {output_path}")
print(f"Active skills: {len(active)}")
