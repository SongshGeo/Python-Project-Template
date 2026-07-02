# CLAUDE.md

Guidance for Claude Code (and any AI agent) working in this repository. This is
the **authoritative source** for coding standards and the skill/workflow index.
The Cursor rules in `.cursor/rules/cursorrules.mdc` are kept in sync with this
file; if the two ever diverge, this file wins.

This is a modern, bilingual (English + 中文) Python project template. It is
managed exclusively with **uv** (no poetry).

## Read the memory bank first

Before any non-trivial work, read the shared memory bank in `memory-bank/`:

- `architecture.md` — high-level structure, module boundaries, key flows.
- `model-design.md` — domain/data model: core entities, relationships, invariants.
- `tech-stack.md` — chosen tools and the rationale behind them.
- `progress.md` — current progress, open questions, next steps.

These files are shared by both Cursor and Claude Code. **Keep them up to date**:
when architecture, data shapes, or tooling change, update the relevant file;
append short, actionable notes to `progress.md` and prune stale ones. Per-task
implementation plans live in `memory-bank/plans/`.

## Coding standards

- **Typing:** every function and class gets full type annotations, including
  explicit return types (`None` where appropriate).
- **Docstrings:** Google-style docstrings on all public functions/classes
  (PEP 257). Update docstrings when behavior changes.
- **Comments:** preserve existing comments; match the surrounding style.
- **Error handling:** avoid bare/broad `try…except` that silently swallows
  exceptions — let failures surface or handle them explicitly with logging.
- **Style:** Black (88 cols), isort (`--profile black`), Ruff (lint + format).
  Docstring coverage is gated by interrogate (`--fail-under=80`).
- **Dependencies:** manage with `uv` only (`uv add`, `uv sync`). Runtime deps go
  in `[project.dependencies]`; dev/docs in `[project.optional-dependencies]`.

## Testing

- Use **pytest only** (never `unittest`). Tests live under `tests/`.
- Fully annotate tests and give them docstrings. Add `__init__.py` when creating
  new packages under `tests/` or `src/<package>`.
- When you need pytest fixtures, import them under `TYPE_CHECKING`:
  `CaptureFixture`, `FixtureRequest`, `LogCaptureFixture`, `MonkeyPatch`
  (`_pytest.*`), `MockerFixture` (`pytest_mock.plugin`).
- Coverage target: ≥80% overall, aim for 100% on core logic.

## Git & commits

- Branch naming: `feature/`, `fix/`, `hotfix/`, `refactor/`, `docs/`, `test/`.
- **Conventional Commits**: `<type>(<scope>): <subject>` (feat, fix, docs,
  style, refactor, test, chore). Commit messages drive `release-please`
  versioning — don't hand-edit `CHANGELOG.md` or the version.

## Skills in this repo

Project skills live in `.claude/skills/`:

- **`setup-project`** — one-stop onboarding for a **fresh** project: collect
  name + description, run the config script non-interactively, install deps, set
  up pre-commit, install the external skill pack, initialize the memory bank.
- **`upgrade-project`** — **idempotent** migration for an **existing/old** repo:
  detect current state, migrate `.cursor/cache/` → `memory-bank/`, add missing
  `.claude/` scaffolding, without touching already-configured metadata.
- **`update-memory-bank`** — guided update of `architecture.md` /
  `model-design.md` / `progress.md`.
- **`quality-check`** — run tests, pre-commit, interrogate, and (optionally) tox.
- **`commit`** — stage and author a Conventional Commit.

## External skills

This template recommends installing SongshGeo's skill pack
(<https://github.com/SongshGeo/skills>) via `npx skills@latest add
SongshGeo/skills`. See `.claude/recommended-skills.md` for the recommended set
and how each skill maps to the plan → architect → progress workflow. The
`setup-project` skill installs them for you.

## Common commands

The Makefile is uv-only (it errors with an install hint if `uv` is missing):

```bash
make setup              # install deps + configure project (name/description)
make test               # uv run pytest
make report             # uv run allure serve tmp/allure_results
make configure-project  # re-run the config wizard
make docs               # uv run mkdocs serve
make docs-build         # uv run mkdocs build
make tox                # tox across Python 3.10–3.13
make tox-e pyversion=py311
```

Direct uv usage: `uv sync --all-extras`, `uv run pytest`, `uv add <pkg>`,
`uv add --optional dev <pkg>`, `uv build`.
