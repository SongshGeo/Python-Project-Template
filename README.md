# Python Project Template

[English](README.md) | [中文](README.zh.md)

A modern Python project template with batteries included: tooling, docs, tests, CI, and packaging.

## Quick Start

### 1) Install uv

```bash
# Install uv (fast, modern)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2) Create a new project

```bash
# Clone this template
git clone https://github.com/SongshGeo/project_template.git my-project
cd my-project

# Initialize the project (configure name/description)
make setup

# Manual configuration (optional, if make setup is skipped)
make configure-project          # auto-detects package manager
# or run directly (requires deps installed)
python scripts/configure_project.py
```

**What the config script does**
- Update `[project]` in `pyproject.toml`
- Update GitHub workflow config
- Create/update `README.md`
- Clear `CHANGELOG.md`

**The script will ask for**
- **Project name**: used in package/config
- **Project description**: short project summary

### Optional: install dependencies only

```bash
uv sync --all-extras
```

### 3) Develop

```bash
# Run tests
make test

# View test report
make report

# Run pre-commit checks
pre-commit run --all-files
```

## Use with Claude Code

This template ships with a Claude Code workflow so you can configure and drive a
project through **skills** instead of memorizing commands.

1. Apply/clone the template and open the folder in Claude Code.
2. Run the **`setup-project`** skill — it collects the project name/description,
   installs dependencies, sets up pre-commit, installs the recommended external
   skills (`npx skills@latest add SongshGeo/skills`), and initializes the shared
   memory bank.
3. For an **existing** project built from an older version of this template, run
   the **`upgrade-project`** skill instead (idempotent migration).

Coding standards and the skill index live in [`CLAUDE.md`](CLAUDE.md); the
persistent plan → architect → progress context lives in
[`memory-bank/`](memory-bank/). See
[`.claude/recommended-skills.md`](.claude/recommended-skills.md) for the external
skills. Cursor users share the same `memory-bank/` via `.cursor/rules/`.

## Project Structure

```shell
.
├── src/                    # Source code
│   ├── api/                # API layer
│   ├── core/               # Core logic
│   └── __init__.py
├── tests/                  # Tests
│   ├── conftest.py         # pytest config
│   └── helper.py           # test helpers
├── config/                 # Configuration
│   └── config.yaml         # Main config
├── data/                   # Data assets
├── docs/                   # Documentation
├── examples/               # Examples
├── scripts/                # Utility scripts
│   └── configure_project.py
├── pyproject.toml          # Project config (uv, PEP 621)
├── tox.ini                 # Multi-Python testing
├── makefile                # Make shortcuts
└── README.md               # This file
```

## Features

1. Makefile automation
2. Hydra-friendly config management
3. pytest unit tests
4. allure reports
5. nbstripout for notebooks (keep outputs)
6. pre-commit for linting
7. mkdocs for docs
8. uv package manager
9. interrogate doc coverage
10. Jupyter for analysis
11. snakeviz profiling
12. isort imports
13. flake8 linting
14. ruff linting
15. black formatting
16. mypy type checking
17. coverage reports
18. tox for Python 3.10-3.13 matrix
19. release-please versioning
20. mkdocs-material theme

## Common Commands

### Dev workflow

```bash
# Install all deps
make setup

# Run tests
make test

# Matrix tests (Python 3.10-3.13)
make tox

# Test report
make report

# Configure project metadata
make configure-project

# Serve docs
make docs
```

**Note:** The Makefile uses uv. If uv isn't installed, it prints an install hint.

### Using uv (recommended)

```bash
# Install deps
uv sync --all-extras

# Run tests
uv run pytest

# Run any Python command
uv run python your_script.py

# Add a dependency
uv add package-name

# Add a dev dependency
uv add --optional dev package-name
```

### Code quality

```bash
# Install pre-commit hooks
pre-commit install

# Run all checks
pre-commit run --all-files

# Run specific checks
pre-commit run flake8 --all-files
pre-commit run black --all-files
pre-commit run interrogate --all-files  # doc coverage
```

### Multi-Python testing

```bash
# All versions (via Makefile)
make tox

# Specific version
make tox-e pyversion=py311

# List envs
make tox-list

# Direct tox
tox                  # all versions
tox -e py311         # Python 3.11
tox list             # show envs
tox -p               # parallel
```

## Documentation

!!! info "Online docs"
    Visit [Online Docs](https://songshgeo.github.io/project_template/) for the full site.

### View docs locally

```bash
# Dev server with live reload
make docs

# Or run directly
uv run mkdocs serve
```

Open `http://127.0.0.1:8000`.

### Build docs

```bash
make docs-build
# or
uv run mkdocs build
```

### Deploy docs to GitHub Pages

Docs are deployed by GitHub Actions:

1. Push to `main`
2. Actions build automatically
3. Pages deploy

**URL:** `https://songshgeo.github.io/project_template/`

### Doc sections

- 📖 [Quick Start](docs/en/doc/quick-start.md) - step-by-step tutorial
- 🔧 [Tooling](docs/en/doc/tools.md) - usage and best practices
- ⚙️ [Configuration](docs/en/doc/configuration.md) - config walkthrough
- 📝 [Development](docs/en/doc/development.md) - coding standards
- 🚀 [Deployment](docs/en/doc/deployment.md) - release process

## FAQ

### Q: How to start a new project?
A: Run `make setup` to configure and install deps.

### Q: How to add dependencies?

```bash
uv add package-name          # runtime deps
uv add --dev package-name    # dev deps
```

### Q: How to run tests?

```bash
make test        # via Make
uv run pytest    # direct
```

## Contributing

Contributions welcome! Steps:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit (`git commit -m 'feat: add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- All linters pass
- Tests are added/updated
- Docs are updated
- Follow coding guidelines

## License

MIT License. See [LICENSE](LICENSE).

## Author

- **SongshGeo** - [GitHub](https://github.com/SongshGeo) - [Website](https://cv.songshgeo.com/)
