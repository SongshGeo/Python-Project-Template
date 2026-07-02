---
name: commit
description: Stage changes and author a Conventional Commit that drives release-please versioning. Use when the user asks to commit work. Handles branch-name sanity, commit type/scope/subject, and reminds not to hand-edit CHANGELOG or version.
---

# commit

Create a well-formed commit that this repo's `release-please` automation can
consume.

## Before committing

- Confirm the working tree contains what the user intends to commit
  (`git status`, `git diff`). Stage deliberately (`git add …`), not blindly.
- Check the branch name follows the convention (`feature/`, `fix/`, `hotfix/`,
  `refactor/`, `docs/`, `test/`). If on `main`/`master`, offer to branch first.
- Consider running the `quality-check` skill first.

## Message format

**Conventional Commits:** `<type>(<scope>): <subject>`

- `type` ∈ feat, fix, docs, style, refactor, test, chore.
- `feat` → minor bump, `fix` → patch bump; `feat!`/`fix!` or a `BREAKING CHANGE:`
  footer → major bump. release-please derives the version and `CHANGELOG.md` from
  these — **never hand-edit the version or CHANGELOG**.
- Keep the subject imperative and ≤ ~72 chars; add a body for the "why" if needed.

## Commit

```bash
git commit -m "<type>(<scope>): <subject>"
```

Only push when the user asks.
