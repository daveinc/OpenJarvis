"""Test: look up a HOD skill by name, inject its content into an agent call."""
from pathlib import Path
from openjarvis.core.config import load_config
from openjarvis.core.events import EventBus
from openjarvis.skills.loader import discover_skills
from openjarvis import Jarvis

cfg = load_config()
skills_path = Path(cfg.skills.skills_dir)

print(f"Loading skills from: {skills_path}")
all_skills = discover_skills(skills_path)
skill_index = {s.name: s for s in all_skills}

# Look up using-superpowers
target = "using-superpowers"
skill = skill_index.get(target)
if not skill:
    print(f"ERROR: skill '{target}' not found. Available: {list(skill_index.keys())}")
    raise SystemExit(1)

print(f"Found skill: [{skill.name}] — {skill.description[:60]}")
print(f"Content length: {len(skill.markdown_content)} chars")
print()

# Inject skill content into query (SDK doesn't expose system prompt yet — HOD patch pending)
skill_excerpt = skill.markdown_content[:600]
query = (
    f"[SKILL: {skill.name}]\n{skill_excerpt}\n\n"
    f"[QUESTION] Based on this skill, what should I check before starting any task?"
)

print("Sending query with skill content injected...")
print("=" * 50)

with Jarvis(engine_key="ollama", model="llama3.2:3b") as j:
    response = j.ask(query)
    print(response)

print("=" * 50)
print("Skill invocation test complete.")
