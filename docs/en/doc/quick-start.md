# Quick Start Guide

[English](quick-start.md) | [中文](https://songshgeo.github.io/project_template/zh/doc/quick-start/)

A step-by-step guide to get productive with this Python project template.

## Prerequisites

- **Python 3.10-3.13** (3.11 recommended)
- **Git**
- **uv** (recommended) or **poetry**

## Step 1: Install a package manager

### Option A: uv (recommended)

uv is a blazing-fast Python package manager written in Rust.

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify
uv --version
```

### Option B: poetry

```bash
pip install poetry
poetry --version
```

## Step 2: Create a new project

```bash
# Clone the template
git clone https://github.com/SongshGeo/project_template.git my-project
cd my-project

# Optional: reset git history
rm -rf .git
git init
```

## Step 3: Configure the project

```bash
make configure-project
# or run directly
python scripts/configure_project.py
```

The script asks for:
- **Project name** (e.g., `my-awesome-project`)
- **Project description** (e.g., `An awesome Python project`)

What it does:
1. Update `pyproject.toml` `[project]` and `[tool.poetry]`
2. Update `.github/workflows/release-please.yml`
3. Create `README.md`
4. Clear `CHANGELOG.md`

Example output:

```
Project name: my-awesome-project
Project description: An awesome Python project
✓ Updated pyproject.toml
✓ Updated .github/workflows/release-please.yml

✨ Project configuration completed!
```

## Step 4: Install dependencies

### With uv

```bash
# All extras (dev + docs)
uv sync --all-extras

# Dev only
uv sync --dev
```

### With poetry

```bash
poetry install
```

## Step 5: Set up Git hooks

```bash
pre-commit install
pre-commit run --all-files
```

## Step 6: Verify setup

```bash
# Using Makefile
make test

# Or directly
uv run pytest
poetry run pytest
```

Test report:

```bash
make report
```

## Step 7: Start developing

### Project layout

```
src/
├── core/          # Core logic
└── api/           # API layer
tests/
├── conftest.py             # pytest config
├── test_configure_project.py  # config script tests
└── test_*.py               # other tests
```

### Current tests

- `tests/test_configure_project.py` verifies the config script.

Run tests:

```bash
make test
# or
uv run pytest
```

### Add new features

1. Add code under `src/`
2. Add matching tests under `tests/`
3. Run tests

Example test:

```python
# tests/test_my_module.py
def test_my_function():
    """Test my function."""
    from src.my_module import my_function
    assert my_function() == expected_value
```

### Add dependencies

Using uv:

```bash
uv add numpy pandas          # runtime deps
uv add --dev pytest-cov      # dev deps
uv add --dev mkdocs          # docs deps
```

Using poetry:

```bash
poetry add numpy pandas
poetry add --group dev pytest-cov
```

### Run code

```bash
uv run python src/your_script.py
poetry run python src/your_script.py

# Or activate virtual env
uv shell
poetry shell
```

## Step 8: Code quality

### Multi-version testing

```bash
make tox                      # Python 3.10-3.13
make tox-e pyversion=py311    # specific version
make tox-list                 # list envs
```

### Automated checks

```bash
pre-commit run --all-files
pre-commit run black --all-files
pre-commit run flake8 --all-files
pre-commit run interrogate --all-files
```

### Manual tools

```bash
black .
ruff format .
flake8 src/
mypy src/
interrogate src/
```

## Next steps

- Read [Tooling](tools.md)
- See [Configuration](configuration.md)
- Review [Development Guide](development.md)
- Check [Deployment](deployment.md)

## FAQ

### uv or poetry?
uv is faster (Rust). poetry is mature. The template supports both.

### Where is the virtualenv?
- uv: `.venv` by default
- poetry: manages its own venv

Check paths:

```bash
uv info
poetry env info
```

### Add more Python versions?

Edit `tox.ini` `envlist`:

```ini
envlist = py310, py311, py312, py313
```

### Generate docs?

```bash
uv run mkdocs serve
uv run mkdocs build
```

Docs output to `site/`.

### Publish to PyPI?

See [Deployment](deployment.md) for the PyPI section.
