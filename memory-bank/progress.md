<!--
Purpose:
- Track current implementation progress, open questions, and next steps during active development.

Audience:
- Any contributor (or coding agent) coordinating ongoing work.

Usage:
- Keep entries brief and actionable; remove outdated notes once resolved.
-->
# progress

## Done

- Migrated the template to a Claude Code workflow: added `CLAUDE.md`, `.claude/`
  (skills + settings + recommended-skills), and moved the memory bank from
  `.cursor/cache/` to top-level `memory-bank/` (shared with Cursor).
- Dropped poetry: `pyproject.toml` uses hatchling + uv only; makefile and docs
  are uv-only.
- `configure_project.py` gained a non-interactive `--name/--description` mode.
- Added `scripts/__init__.py` to fix a mypy duplicate-module error.

## Open / next

- Quality gate has two pre-existing reds: nbstripout normalizes
  `playground.ipynb`; interrogate counts empty `__init__.py` / `conftest.py` /
  `helper.py` and drops below the 80% gate.
- `src/core` and `src/api` are still empty scaffolds.
