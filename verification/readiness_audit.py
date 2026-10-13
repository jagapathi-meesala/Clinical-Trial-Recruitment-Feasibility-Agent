from pathlib import Path
required = [
"agent.yaml","SOUL.md","README.md","RULES.md","DUTIES.md","AGENTS.md","EXPLAINABILITY.md",
"requirements.txt",".env.example",".gitignore","pytest.ini","core/__init__.py","core/engine.py","core/cli.py",
"tools/validate-feasibility-input.yaml","tools/estimate-recruitment-feasibility.yaml","tools/prepare-feasibility-summary.yaml",
"skills/criteria-screening/SKILL.md","skills/site-feasibility/SKILL.md","skills/recruitment-planning/SKILL.md",
"tests/test_engine.py","examples/site_feasibility.json"
]
missing = [p for p in required if not Path(p).is_file()]
if missing:
    print("FAIL: missing required files: " + ", ".join(missing))
    raise SystemExit(1)
print(f"PASS: all {len(required)}/{len(required)} required files present")
