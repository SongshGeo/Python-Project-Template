# Python Project Template

[English](index.md) | [中文](https://songshgeo.github.io/project_template/zh/)

A modern Python project template with a full toolchain and best practices baked in.

!!! info "Highlights"
    - 🚀 Package management with `uv`
    - 🧪 Testing with `pytest`, multi-version with `tox`
    - 📊 Beautiful reports via `allure`
    - 🔧 Code quality enforced by `pre-commit`
    - 📝 Documentation with `mkdocs`
    - 🎯 Doc coverage via `interrogate`
    - 🔍 Code checks with `ruff`, `flake8`, `mypy`

## Quick Start

### 1. Install uv (recommended)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create a new project

```bash
# Clone the template
git clone https://github.com/SongshGeo/project_template.git my-project
cd my-project

# Initialize
make setup
```

### 3. Start developing

```bash
# Run tests
make test

# View test report
make report

# Run code checks
pre-commit run --all-files
```

!!! tip "Need help?"
    See the [Quick Start Guide](doc/quick-start.md) for details.

## Project Structure

```tree
.
├── src/                    # Source code
├── tests/                  # Tests
├── config/                 # Config files
├── docs/                   # Documentation
├── scripts/                # Utility scripts
├── pyproject.toml          # Project config
├── makefile                # Shortcuts
└── README.md               # Project overview
```

## Core Capabilities

### Package manager
- **uv**: extremely fast; this template is uv-only

### Code quality
- Black: formatting
- Ruff: blazing-fast lint/format
- Flake8: style checks
- MyPy: type checks
- Interrogate: doc coverage

### Testing
- Pytest: unit testing
- Tox: Python 3.10-3.13 matrix
- Allure: test reports
- Coverage: coverage reports

### Docs
- MkDocs with Material theme

## Docs Navigation

!!! tip "Jump to a section"
    - 📖 [Quick Start](doc/quick-start.md) - step-by-step tutorial
    - 🔧 [Tooling](doc/tools.md) - tools and best practices
    - ⚙️ [Configuration](doc/configuration.md) - config walkthrough
    - 📝 [Development](doc/development.md) - coding standards
    - 🚀 [Deployment](doc/deployment.md) - release process

## Feature Matrix

| Feature        | Tool              | Notes                          |
|----------------|-------------------|--------------------------------|
| Package mgmt   | uv                | Modern dependency management   |
| Formatting     | Black, Ruff       | Consistent style               |
| Linting        | Ruff, Flake8, MyPy| Multi-layer quality            |
| Testing        | Pytest, Tox       | Comprehensive coverage         |
| Reports        | Allure            | Visual test reports            |
| Docs           | MkDocs            | Professional doc site          |
| Doc coverage   | Interrogate       | Ensure docstrings              |
| Git hooks      | Pre-commit        | Checks before commit           |
| Versioning     | Release Please    | Automated releases             |
| Typing         | MyPy              | Static typing                  |
| Profiling      | Snakeviz          | Performance visualization      |

## Common Commands

```bash
# Install deps
make setup

# Run tests
make test

# View report
make report

# Configure project
make configure-project
```

## License

MIT License.

## Contributing

Contributions welcome. Typical steps:

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

## Links

- 📖 [Full docs](doc/quick-start.md)
- 🔧 [GitHub repo](https://github.com/SongshGeo/project_template)
- 👤 [Author site](https://cv.songshgeo.com/)
