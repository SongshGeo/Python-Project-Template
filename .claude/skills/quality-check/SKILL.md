---
name: quality-check
description: Run the project's full quality gate — pytest, pre-commit (black/ruff/isort/flake8/mypy), interrogate docstring coverage, and optionally the tox matrix — then summarize failures with fixes. Use before committing, before opening a PR, or when the user asks to check code quality.
---

# quality-check

Run the repository's quality gate and report results clearly. uv is required.

## Steps

1. **Tests**
   ```bash
   make test          # == uv run pytest
   ```
2. **Pre-commit hooks** (black, ruff, isort, flake8, mypy, interrogate,
   nbstripout, file fixers):
   ```bash
   uv run pre-commit run --all-files
   ```
3. **Docstring coverage** (if you want it standalone):
   ```bash
   uv run interrogate -v
   ```
4. **Optional — multi-version matrix** (only if asked; it is slow):
   ```bash
   make tox           # Python 3.10–3.13
   ```

## Reporting

- Summarize each stage as pass/fail.
- For failures, quote the relevant output and propose the concrete fix; offer to
  apply it.
- Do not mark the work "done" while any stage is red.
