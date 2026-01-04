# Tooling Guide

[English](tools.md) | [中文](https://songshgeo.github.io/project_template/zh/doc/tools/)

This template bundles a rich toolchain for quality, productivity, and release automation.

## Package Management

### uv (recommended)
- Very fast installs (10–100x faster than pip)
- Manages envs, deps, and packages in one tool
- Rust-based by astral-sh; PyPI compatible

Common commands:

```bash
uv sync --all-extras          # install deps
uv add package-name           # add runtime dep
uv add --dev package-name     # add dev dep
uv remove package-name        # remove dep
uv run python script.py       # run commands
uv run pytest
uv tree                       # dependency tree
uv pip compile pyproject.toml # export requirements
```

### poetry (alternative)
- Mature ecosystem and plugins
- Strong version management

```bash
poetry install
poetry add package-name
poetry add --group dev package-name
poetry remove package-name
poetry update
poetry run python script.py
poetry run pytest
```

## Code Quality

### Black (format)
- Auto-format Python; config in `.pre-commit-config.yaml`

```bash
black src/ tests/
black --check src/
black --include \.ipynb$ notebooks/
```

### Ruff (lint + format)
- Rust-fast linter/formatter; replaces flake8/isort/pyupgrade

```bash
ruff check src/
ruff check --fix src/
ruff format src/
pre-commit run ruff --all-files
pre-commit run ruff-format --all-files
```

Config: `[tool.ruff]` in `pyproject.toml`.

### Flake8

```bash
flake8 src/ tests/
flake8 src/core/exp.py
```

### isort (imports)

```bash
isort src/ tests/
isort --check src/
```

### MyPy (types)

```bash
mypy src/
mypy --ignore-missing-imports src/
```

Example annotation:

```python
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

### Interrogate (doc coverage)

```bash
interrogate src/
interrogate --fail-under=80 src/
interrogate --verbose src/
```

Example docstring in practice shown in code block in zh version.

## Testing

### Pytest

```bash
pytest                        # all tests
pytest tests/test_core.py     # file
pytest tests/test_core.py::test_example  # single test
pytest -v                     # verbose
pytest --cov=src --cov-report=html
pytest --lf                   # last failed
pytest -n auto                # parallel
```

Sample test:

```python
import pytest
from src.core.example import Example


def test_example():
    """Test example functionality."""
    example = Example(42)
    assert example.get_value() == 42
```

### Tox (multi-Python)

```bash
tox               # all envs
tox -e py311      # specific env
tox -p            # parallel
tox list          # list envs
```

### Allure (reports)

```bash
pytest --alluredir=tmp/allure_results
make report
# or
allure serve tmp/allure_results
```

## Documentation

### MkDocs

```bash
uv run mkdocs serve           # dev server
uv run mkdocs build           # static build
uv run mike deploy 3.10       # deploy with mike
```

### Jupyter

```bash
uv run jupyter lab
uv run jupyter notebook
nbstripout --keep-output
```

## Pre-commit (Git hooks)

```bash
pre-commit install
pre-commit run --all-files
pre-commit run black --all-files
# skip (not recommended)
git commit --no-verify
```

## Performance

### Snakeviz

```python
import cProfile
from snakeviz.cli import main

profiler = cProfile.Profile()
profiler.enable()
# run your code
profiler.disable()
profiler.dump_stats("tmp/profile.stats")
main(["tmp/profile.stats"])
```

## Release Management

### Release Please
- Automated versioning and releases
- Config: `release-please-config.json`
- Flow: push to `main` → release PR → merge → release + tag → Actions publish

## Configuration Best Practices
- Install pre-commit hooks locally
- Ensure CI runs: pre-commit, pytest, interrogate, tox
- Keep tool versions aligned across the team

## Troubleshooting
- Prefer Ruff over Flake8 for speed; uv over pip
- For tool conflicts, align configs or consolidate on Ruff
- Common errors:
  - `command not found: uv`: ensure installed
  - `ModuleNotFoundError`: activate venv and install deps
