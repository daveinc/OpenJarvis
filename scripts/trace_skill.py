"""Trace exactly how a specific skill is loaded."""
from pathlib import Path
import yaml
from openjarvis.skills.loader import load_skill_directory, load_skill_markdown

skill_path = Path(r"C:\Users\davei\.claude\skills\superceo-crisis")
md_path = skill_path / "SKILL.md"

# Check raw YAML parse
raw = md_path.read_text(encoding="utf-8-sig")
print("File starts with '---':", raw.startswith("---"))
print("First 100 chars:", repr(raw[:100]))

if raw.startswith("---"):
    rest = raw[3:]
    if rest.startswith("\n"):
        rest = rest[1:]
    end_idx = rest.find("\n---")
    print(f"end_idx: {end_idx}")
    if end_idx != -1:
        yaml_block = rest[:end_idx]
        print("YAML block:", repr(yaml_block[:200]))
        try:
            fm = yaml.safe_load(yaml_block)
            print("Parsed frontmatter:", fm)
        except yaml.YAMLError as e:
            print("YAML ERROR:", e)

print()
manifest = load_skill_markdown(md_path)
print(f"Loaded: name={manifest.name}, tags={manifest.tags}")
