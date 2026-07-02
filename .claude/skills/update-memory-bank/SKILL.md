---
name: update-memory-bank
description: Update the shared memory bank (architecture.md / model-design.md / progress.md) after design or progress changes, so the persistent context stays accurate for both Cursor and Claude Code. Use when the codebase structure, data model, or project status has changed, or at the end of a work session.
---

# update-memory-bank

Keep `memory-bank/` accurate. It is the persistent context both Cursor and Claude
Code read before working, so stale entries actively mislead.

## What to update

- **`architecture.md`** — when modules, boundaries, or key flows change. Keep it
  a concise map (prefer short descriptions + links to source-of-truth over long
  prose). Preserve the `Purpose / Audience / Usage` header comment.
- **`model-design.md`** — when core entities, relationships, or invariants
  change. Favor small diagrams/examples over exhaustive detail.
- **`progress.md`** — append brief, actionable notes on what changed and the next
  steps; **prune** entries that are now resolved. This is a rolling worklog, not
  an archive.
- **`tech-stack.md`** — only when major dependencies or runtime/build tooling
  change.

## How to work

1. Diff intent vs. reality: read the relevant memory-bank file and the code it
   describes; note where they disagree.
2. Make the smallest edit that restores accuracy. Do not invent structure that
   isn't in the code.
3. Keep each file's existing header-comment convention intact.
4. If a `memory-bank/plans/<task>.md` plan is now complete, summarize the outcome
   into `progress.md` and remove or archive the plan.
