# Tech Stack

## Develop Env Stack

- Python 3.10–3.13 (PEP 563 via `future-annotations`, typing support via `typing-extensions`).
- Poetry build (PEP 621) with runtime deps only `typing-extensions`, `future-annotations`.
- Tooling via pre-commit: Black (code + Jupyter), Isort (`--profile=black`), Ruff lint/format, Flake8 (custom ignores/line length), nbstripout (keep outputs), check-ast/EOL/trailing-space.
- Quality gates: Mypy (`--ignore-missing-imports`), Interrogate (docstring coverage fail-under 80), docstrings follow Google style.
- Testing harness: Pytest; task orchestration: Tox; notebooks: ipykernel/ipywidgets.
- Versioning/releases: Google Release Please automation.
