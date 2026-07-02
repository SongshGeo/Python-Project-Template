# Recommended external skills

This template pairs with SongshGeo's skill pack:
<https://github.com/SongshGeo/skills>

Install (interactive picker — enable them for Claude Code):

```bash
npx skills@latest add SongshGeo/skills
```

The `setup-project` skill runs this for you. Skills are **installed, not
vendored** — this file is only a curated recommendation, so upstream updates flow
through `npx skills` naturally. Select the following set.

## Recommended set and how it maps to the workflow

The core discipline of this template is *plan → architect → progress*, backed by
the shared `memory-bank/`. Each recommended skill plugs into that loop:

### Plan / interview — think before you code
- **`grill-me`**, **`grilling`** — interrogate a request until the intent is
  sharp *before* writing code (the "planning is everything" gate). Feeds Claude
  Code's built-in `/plan` and the plans in `memory-bank/plans/`.
- **`to-prd`** — turn a discussion into a PRD.
- **`to-issues`** — break a plan into independently grabbable issues.

### Design / architecture — keep the memory bank sharp
- **`domain-modeling`** — build/refine the domain model → `memory-bank/model-design.md`.
- **`codebase-design`** — module design principles/vocabulary → `memory-bank/architecture.md`.
- **`improve-codebase-architecture`** — periodic architecture scan with a report.

### Dev loop — day-to-day implementation
- **`tdd`** — red-green-refactor. Pairs with the `quality-check` skill.
- **`diagnosing-bugs`** — structured debugging loop for hard issues.
- **`prototype`** — throwaway prototypes to validate a design quickly.

### Review / handoff
- **`code-review`** — two-axis (standards + spec) review via parallel sub-agents.
  Pairs with the `commit` skill (review before you commit).
- **`handoff`** — compact a session into a handoff doc; fold the summary into
  `memory-bank/progress.md`.

## Note

Skill names above must match what the pack actually ships. If `npx skills` shows
different names (renamed/removed upstream), trust the picker and update this list.
