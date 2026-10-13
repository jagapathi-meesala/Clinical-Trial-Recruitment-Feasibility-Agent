# Clinical Trial Recruitment Feasibility Agent

An explainable local tool for screening aggregate, de-identified clinical-trial recruitment inputs and preparing feasibility summaries for research-team review.

## Features
- Validates study targets, eligible-cohort estimates, site activation assumptions, and monthly recruitment rates.
- Calculates a transparent projected recruitment timeline and estimated recruitment coverage.
- Flags impossible or missing values and surfaces assumptions.
- Produces a JSON summary with operational risks and review prompts.
- Uses aggregate counts only; do not submit patient identifiers or sensitive personal health data.

## Run
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pytest -q
python3 verification/readiness_audit.py
python3 -m core.cli examples/site_feasibility.json
```
If the OpenGAP CLI is installed, run `opengap validate` from this directory.

## Limitations
This is an operational screening heuristic, not clinical advice, a statistical power calculation, a validated enrollment forecast, or a substitute for protocol review, ethics approval, privacy review, or site-investigator judgment.
