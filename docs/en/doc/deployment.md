# Deployment Guide

[English](deployment.md) | [中文](https://songshgeo.github.io/project_template/zh/doc/deployment/)

How to build, test, and ship the project.

## Local Build

### Install dependencies

```bash
# uv
uv sync --all-extras

# poetry
poetry install
```

### Run tests

```bash
make test           # via Make
uv run pytest       # direct
make report         # allure report
```

### Code quality

```bash
pre-commit run --all-files
black src/ tests/
ruff format src/ tests/
ruff check src/
flake8 src/
mypy src/
interrogate src/
```

## Build Packages

### With uv

```bash
uv build            # wheel + sdist
ls dist/
```

### With poetry

```bash
poetry build
ls dist/
```

### Verify build

```bash
tar -tzf dist/*.tar.gz
pip install dist/*.whl
python -c "import your_package"
```

## Versioning

### Automated (recommended)

Using [release-please](https://github.com/googleapis/release-please):
1. Commit to `main`
2. Release PR auto-created
3. Merge → GitHub release

Config: `release-please-config.json`

### Manual

```bash
# Update pyproject.toml version
# version = "1.2.0"

git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to 1.2.0"
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin main --tags
```

## Publish to PyPI

### Set token
1. Create token in PyPI
2. Add to GitHub Secrets: `PYPI_TOKEN`

### Automatic publish
Triggered by `.github/workflows/release-please.yml` when a release is created.

### Manual publish

#### uv
```bash
uv build
uv publish --token YOUR_PYPI_TOKEN
uv publish --publish-url https://test.pypi.org/legacy/   # TestPyPI
```

#### poetry
```bash
poetry config pypi-token.pypi YOUR_PYPI_TOKEN
poetry publish
poetry publish --repository testpypi
```

#### twine
```bash
pip install twine
twine upload dist/*
twine upload --repository testpypi dist/*
```

## Compatibility Testing

### tox
```bash
tox                     # py3.10-3.13
tox -e py311            # single env
tox -p                  # parallel
tox --notest            # skip env install
```

### CI example

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.10', '3.11', '3.12', '3.13']
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync --all-extras
      - name: Run tests
        run: uv run pytest
      - name: Run checks
        run: pre-commit run --all-files
```

## Container Deployment

### Example Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
COPY src/ ./src/
CMD ["uv", "run", "python", "-m", "src.main"]
```

Build and run:

```bash
docker build -t myapp:latest .
docker run -p 8000:8000 myapp:latest
```

## CI/CD

### Test workflow (example)

```yaml
name: Test
on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12', '3.13']
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync --all-extras
      - name: Run tests
        run: uv run pytest
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
```

### Docs deployment (example)

```bash
uv run mkdocs serve      # preview
uv run mkdocs build      # build
uv run mike deploy 3.10 -p
```

GitHub Pages workflow sample:

```yaml
name: Deploy Docs
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync --extras docs
      - name: Build docs
        run: uv run mkdocs build
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

## Environment Checklist
- Use production-ready WSGI server (e.g., Gunicorn)
- Enable HTTPS
- Configure logging
- Set environment variables
- Monitoring and alerts
- Backups
- Firewalls

### Environment variables

```bash
# .env.production
DATABASE_URL=postgresql://user:pass@host:5432/dbname
SECRET_KEY=your-secret-key
DEBUG=False
LOG_LEVEL=INFO
```

## Monitoring & Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)
```

Health check example:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}, 200
```

## Troubleshooting

### Build failed?
- Check Python version
- Verify dependency compatibility
- Run `uv sync --all-extras`
- Inspect logs

### Coverage too low?

```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

### PyPI publish failed?
- Validate API token
- Ensure package name is unique
- Run `uv build` to verify artifacts

### Roll back a version?

```bash
git tag -a v1.0.0-rollback -m "Rollback to 1.0.0"
# Restore previous release from history as needed
```

## Next Steps
- See [Quick Start](quick-start.md)
- Read [Tooling](tools.md)
- Review [Development](development.md)
