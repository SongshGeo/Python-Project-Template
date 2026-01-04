# Configuration Guide

[English](configuration.md) | [中文](https://songshgeo.github.io/project_template/zh/doc/configuration/)

This template includes multiple config files for project metadata, tooling, and CI.

## Key Config Files

### pyproject.toml
Central project config: metadata, dependencies, and tool settings.

#### [project] (uv)

```toml
[project]
name = "project-name"
version = "1.0.0"
description = "Project description"
requires-python = ">=3.10,<3.14"
dependencies = [
    "package1>=1.0.0",
    "package2>=2.0.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.0.0", "black>=23.0.0"]
docs = ["mkdocs>=1.4.0"]
```

#### [tool.poetry] (poetry compatibility)

```toml
[tool.poetry]
name = "project-name"
version = "1.0.0"
description = "Project description"

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
package1 = ">=1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = ">=7.0.0"
```

#### Tool configs

```toml
# Black
[tool.black]
line-length = 88
target-version = ['py310', 'py311', 'py312', 'py313']

# Ruff
[tool.ruff]
line-length = 88
target-version = "py310"
select = ["E", "F", "I", "N", "W", "B", "C4", "UP"]

# MyPy
[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true

# Interrogate
[tool.interrogate]
fail-under = 80
ignore-init-module = true

# Flake8
[tool.flake8]
max-line-length = 88
max-complexity = 10
```

### tox.ini
Multi-version test matrix.

```ini
[tox]
envlist = py310, py311, py312, py313
isolated_build = true

[testenv]
whitelist_externals = uv
commands_pre = uv sync --dev
commands = uv run pytest
commands =
    uv run pytest --cov=src --cov-report=html
    uv run pytest --cov=src --cov-report=term

[testenv:docs]
commands = uv run mkdocs build
```

### .pre-commit-config.yaml
Git hooks for automated checks.

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: '24.1.0'
    hooks:
      - id: black
      - id: black-jupyter

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
      - id: ruff-format

  - repo: https://github.com/kynan/nbstripout
    rev: 0.8.1
    hooks:
      - id: nbstripout
        args: ['--keep-output']

  - repo: https://github.com/econchick/interrogate
    rev: 1.7.0
    hooks:
      - id: interrogate
        args: [--verbose, --fail-under=80]
```

### makefile
Command shortcuts.

```makefile
# Install deps and init
setup:
    @uv sync --all-extras
    @make configure-project

# Run tests
test:
    uv run pytest

# Reports
report:
    uv run allure serve tmp/allure_results

# Configure project
configure-project:
    @uv run python scripts/configure_project.py
```

Custom commands example:

```makefile
format:
	@black src/ tests/
	@isort src/ tests/

typecheck:
	@mypy src/

clean:
	@rm -rf build/ dist/ *.egg-info
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete

docs:
	@uv run mkdocs build
```

### .github/workflows/
GitHub Actions configuration.

#### release-please.yml
Automated release flow:
1. Create release PR
2. Publish to PyPI
3. Create GitHub release

PyPI secret: `PYPI_TOKEN`.

## Project-specific Config

### config/config.yaml
Application config (e.g., Hydra).

```yaml
database:
  host: localhost
  port: 5432
  name: myapp

api:
  host: 0.0.0.0
  port: 8000
  debug: false

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### config/ds/
Dataset-specific configs:
- `mac.yaml`
- `win.yaml`

## Environment Variables

Use a `.env` file (do not commit):

```bash
# .env
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=your-api-key
DEBUG=True
```

Load in code:

```python
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
```

## IDE Setup

### VS Code (optional)

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

### PyCharm
1. Set interpreter to project venv
2. Enable Black formatting
3. Configure pytest
4. Enable flake8 and mypy

## Config Priority
1. CLI args
2. Environment variables
3. `.env`
4. Config files (`config.yaml`)
5. Defaults

## Customization Examples

### Change code style

```toml
[tool.black]
line-length = 100

[tool.ruff]
line-length = 100
```

### Change Python version

```toml
[project]
requires-python = ">=3.11,<3.14"

[tool.poetry.dependencies]
python = ">=3.11,<3.14"
```

### Update coverage threshold

```toml
[tool.interrogate]
fail-under = 90
```

### Add a new tool config

```toml
[tool.your-tool]
setting1 = "value1"
setting2 = "value2"
```

## Best Practices
- Version-control all configs
- Keep secrets in env vars
- Document config changes
- Keep team configs consistent
- Lint configs where possible

## Common Questions

### Change dependency versions?

Edit `pyproject.toml`, then:

```bash
uv lock
poetry lock
```

### Ignore files/dirs?

```toml
[tool.black]
exclude = '''
/(
    \.git
    | \.venv
    | build
    | dist
)/
'''
```

### Use another Python version?

```bash
pyenv install 3.12.0
pyenv local 3.12.0
```

## Next Steps
- See [Quick Start](quick-start.md)
- Read [Tooling](tools.md)
- Review [Development Guide](development.md)
