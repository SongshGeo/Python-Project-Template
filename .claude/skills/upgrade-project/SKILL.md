---
name: upgrade-project
description: Idempotently migrate an existing project built from an older version of this template to the new Claude Code workflow — move .cursor/cache into the shared memory-bank, add missing .claude scaffolding (CLAUDE.md, skills, settings, recommended-skills), and optionally install the external skill pack. Use to modernize an old repo without touching already-configured metadata. Safe to run repeatedly.
---

# upgrade-project

Bring an **existing** repository (one already created from an older version of
this template) up to the current Claude Code workflow. This skill is
**idempotent**: every step checks current state first and skips what already
exists, so it is safe to run more than once.

## 1. Detect current state

Report what you find before changing anything:
- Does `.cursor/cache/` exist (old memory-bank location)?
- Does `memory-bank/` already exist?
- Do `CLAUDE.md` and `.claude/skills/` exist?
- Is `pyproject.toml` still using the placeholder name `songshgeo`?
- Is the build still on poetry (`[tool.poetry]` present / `poetry-core` backend)?

## 2. Migrate the memory bank

- If `.cursor/cache/*.md` exist and `memory-bank/` does not: `git mv` the four
  docs (`architecture`, `model-design`, `tech-stack`, `progress`) into
  `memory-bank/`, and `git mv .cursor/plans/.keep memory-bank/plans/.keep`.
- If **both** locations have content: merge without overwriting — bring any
  unique content from `.cursor/cache/` into `memory-bank/`, then remove the stale
  copies. Never clobber existing memory-bank content.
- Update `.cursor/rules/cursorrules.mdc` so it points at `memory-bank/` and notes
  `CLAUDE.md` as the authoritative rules source.

## 3. Add missing scaffolding

For each of these, create it only if absent (otherwise show a diff/summary and
let the user decide):
- `CLAUDE.md`
- `.claude/skills/{setup-project,upgrade-project,update-memory-bank,quality-check,commit}/SKILL.md`
- `.claude/settings.json`
- `.claude/recommended-skills.md`

## 4. Optional: modernize tooling

If the repo is still on poetry, offer (do not force) to migrate to uv-only:
drop `[tool.poetry]`, switch `[build-system]` to hatchling, and make the Makefile
uv-only. Confirm before editing build config on an established project.

## 5. Optional: install external skills

```bash
npx skills@latest add SongshGeo/skills
```

Point the user at `.claude/recommended-skills.md` for the recommended set.

## 6. Do NOT touch configured metadata

If `pyproject.toml` is already configured (name is not `songshgeo`), leave
name/description/README/CHANGELOG alone. Only if it is still the placeholder,
suggest running the `setup-project` skill instead.

## 7. Report

Print a concise migration report: **done**, **skipped (already present)**, and
**needs manual review**. End by reminding the user to read `CLAUDE.md` and the
memory bank.
