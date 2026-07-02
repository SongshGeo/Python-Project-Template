<!--
Purpose:
- Record the project's high-level architecture (modules, boundaries, and key flows) as a quick reference.

Audience:
- Contributors and reviewers who need context before making changes.

Usage:
- Update this file when architectural decisions or major module interactions change.
-->

# Architecture

High-level layout (each path is the source-of-truth):

- `src/` — application code: `src/core/` (core logic) and `src/api/` (API layer).
  Both are placeholders to be filled per project.
- `tests/` — pytest suite (`test_*.py`), plus `conftest.py` and `helper.py`.
- `config/` — Hydra config: `config.yaml` composes a platform data-source group
  `ds` (`config/ds/{linux,mac,win}.yaml`, currently comment-only placeholders).
- `scripts/` — maintenance tooling; `configure_project.py` initializes project
  metadata (name/description → pyproject `[project]`, release-please, README,
  CHANGELOG). Runs interactively or via `--name/--description`.
- `docs/` — MkDocs Material, mirrored `docs/en` + `docs/zh`, built by
  `.github/workflows/docs.yml`.
- Packaging: PEP 621 `[project]` in `pyproject.toml`, **hatchling** build
  backend, managed with **uv**. Releases via release-please + PyPI publish.

AI collaboration layer:

- `CLAUDE.md` — authoritative coding standards + skill index.
- `.claude/skills/` — setup-project, upgrade-project, update-memory-bank,
  quality-check, commit. `.claude/recommended-skills.md` lists external skills.
- `memory-bank/` — shared persistent context (this directory), read by both
  Claude Code and Cursor (`.cursor/rules/cursorrules.mdc` points here).
