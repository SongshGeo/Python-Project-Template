<!--
Purpose:
- Summarize the chosen tech stack (libraries/tools) and the rationale for key selections.

Audience:
- Contributors onboarding or evaluating dependency/stack changes.

Usage:
- Update when adding/removing major dependencies or changing runtime/build tooling.
-->
# Tech-stack documentation

## Develop Env Stack

- Python 3.10–3.13 (PEP 563 via `future-annotations`, typing support via `typing-extensions`).
- `uv` for dependency management; **hatchling** build backend (PEP 621). Runtime deps only `typing-extensions`, `future-annotations`.
- Tooling via pre-commit: Black (code + Jupyter), Isort (`--profile=black`), Ruff lint/format, Flake8 (custom ignores/line length), nbstripout (keep outputs), check-ast/EOL/trailing-space.
- Quality gates: Mypy (`--ignore-missing-imports`), Interrogate (docstring coverage fail-under 80), docstrings follow Google style.
- Testing harness: Pytest; task orchestration: Tox; notebooks: ipykernel/ipywidgets.
- Versioning/releases: Google Release Please automation.
