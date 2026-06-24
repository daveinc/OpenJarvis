"""Verify HOD config loads correctly and skills are auto-discovered."""
from openjarvis.core.config import load_config
from openjarvis.skills.loader import discover_skills

cfg = load_config()
print(f"Engine: {cfg.engine.default}")
print(f"Ollama host: {cfg.engine.ollama.host}")
print(f"Skills dir: {cfg.skills.skills_dir}")
print(f"Auto-discover: {cfg.skills.auto_discover}")
print(f"Telemetry: {cfg.telemetry.enabled}")
print()

skills = discover_skills(cfg.skills.skills_dir)
print(f"Skills discovered: {len(skills)}")
for s in sorted(skills, key=lambda x: x.name):
    print(f"  {s.name}")
