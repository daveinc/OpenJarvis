from pathlib import Path
from openjarvis.core.config import load_config
from openjarvis.skills.loader import discover_skills

cfg = load_config()
skills = discover_skills(cfg.skills.skills_dir)
for s in sorted(skills, key=lambda x: x.name):
    if "_removed" not in s.name:
        tags = s.tags if s.tags else []
        print(f"{s.name}: tags={tags}")
