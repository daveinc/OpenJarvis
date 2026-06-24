from openjarvis.skills.loader import discover_skills

skills = discover_skills(r"C:\Users\davei\.claude\skills")
unnamed = [s for s in skills if s.name == "SKILL"]
named = [s for s in skills if s.name != "SKILL"]

print(f"Named correctly: {len(named)}")
print(f"Missing name field: {len(unnamed)}")
print()
print("=== MISSING NAME ===")
for s in unnamed:
    desc = s.description[:80] if s.description else "(none)"
    print(f"  desc: {desc}")
