---
name: setup-project
description: Bootstrap a freshly cloned copy of this Python template into a working project — set the project name/description, install dependencies, wire pre-commit, install the recommended external skills, and initialize the memory bank. Use right after applying or cloning the template, or whenever pyproject.toml still shows the placeholder name "songshgeo".
---

# setup-project

Guided, one-stop initialization for a **new** project created from this template.
Run the steps in order, confirming with the user where noted. If a step's tool is
missing, stop and tell the user how to install it rather than guessing.

## 1. Gather metadata

Ask the user (conversationally) for:
- **Project name** — used as the package/distribution name.
- **Project description** — one short sentence.

Do not proceed until both are non-empty.

## 2. Configure project files (non-interactive)

Run the config script with the collected values:

```bash
uv run python scripts/configure_project.py --name "<name>" --description "<description>"
```

This updates `[project]` in `pyproject.toml`, fills the `${project_name}`
placeholder in `.github/workflows/release-please.yml`, rewrites `README.md`, and
clears `CHANGELOG.md`.

## 3. Install dependencies

```bash
uv sync --all-extras
```

(or `make setup` for the guided make path). uv is required — if it is missing,
point the user at `curl -LsSf https://astral.sh/uv/install.sh | sh`.

## 4. Set up pre-commit

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

Report any hook failures; offer to fix them.

## 5. Offer to reset git history

Ask whether the user wants a clean history for their new project. Only if they
say yes:

```bash
rm -rf .git && git init && git add -A && git commit -m "chore: initial commit from template"
```

Never reset history without explicit confirmation.

## 6. Install the recommended external skills

```bash
npx skills@latest add SongshGeo/skills
```

The CLI is interactive: tell the user to select the recommended set documented in
`.claude/recommended-skills.md` (grill-me, grilling, to-prd, to-issues, tdd,
diagnosing-bugs, prototype, domain-modeling, codebase-design,
improve-codebase-architecture, code-review, handoff) and to enable them for
Claude Code. This is optional — the user can skip it.

## 7. Initialize the memory bank

Using the project's stated vision, draft initial content for:
- `memory-bank/architecture.md` — intended module layout and boundaries.
- `memory-bank/model-design.md` — the core entities/data shapes, if known.

Set `memory-bank/progress.md` to a short "project initialized" note with the
immediate next steps. Keep `tech-stack.md` (already populated) accurate.

## 8. Verify

```bash
make test
```

Summarize what was configured and point the user at `CLAUDE.md` and the
memory-bank workflow for ongoing collaboration.
