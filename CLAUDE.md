# CLAUDE.md — reasons-qagent

Agentic QA testing tool. Give it a URL, it figures out what to test, runs the tests in a real browser, and tells you what broke. Built as a learning project and interview artifact.

## Architecture
- **run.py** — CLI entry point. `--url` required, `--plan` for planner-driven test cases, `--mode qa|ux`.
- **tests/agent_test.py** — the agent loop (NOT a test file despite the path). Screenshot → Claude → action → repeat. 541 lines.
- **suite_runner.py** — planner → prioritized test cases → agent per case → suite_report.html.
- **generate_report.py** — ReportLab PDF generation for UX mode reports. 374 lines of layout code.
- **tests/planner.py** — scrapes page, asks Claude to generate test cases.
- **build_index.py** — aggregates `runs/` into `runs/index.json` and `runs/suite_index.json` for the dashboard.

## Key design decisions
- `max_tokens=1024` in agent loop — don't raise without measuring.
- Image stripping from conversation history after each step (84% token reduction).
- JPEG quality 40 for per-step screenshots.
- `runs/` directory is gitignored — contains site content.

## Common invocations
```bash
# Smoke test (fastest)
python tests/agent_test.py --url https://linear.app --mode qa --steps 4

# Full suite
python suite_runner.py --url https://linear.app --mode qa --steps 8
```

## Relationship to reasonable-ux
Same agent architecture origin, diverged significantly. reasonable-ux has nav:Label dispatch, persona inference, commercial product treatment. Don't backport features between repos without explicit discussion.

## Rules
- Minimum viable diff. Make the stated fix and nothing else.
- This is interview-ready code — commit messages should be honest and specific.
