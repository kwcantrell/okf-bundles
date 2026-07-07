---
type: History Practice
title: Revert vs. Reset
description: Two ways to undo work — revert adds a new commit that reverses a change (safe on shared history), while reset moves the branch pointer and can discard commits.
resource: https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
tags:
  - git
  - history
  - undo
timestamp: 2026-07-07T00:00:00Z
---

# Revert vs. Reset

Both commands undo work, but they differ fundamentally in whether they *preserve*
history. `git revert` creates a **new commit** that records the reversal of an
existing commit's changes, leaving history intact. `git reset` **moves the branch
pointer** and can discard commits and uncommitted changes rather than adding
anything.

## How reset works: the three trees

`git reset` manipulates up to three trees in order:

- It **always moves HEAD** (the branch pointer) to the target commit.
- **`--mixed`** (the default) also updates the **index** to match the new HEAD,
  so changes between old and new HEAD become unstaged.
- **`--soft`** stops after moving HEAD, leaving the index and working directory
  untouched — the diff stays **staged**, ready to recommit.
- **`--hard`** additionally overwrites the **working directory** to match. This
  is the only variant that is **not working-directory-safe**: uncommitted work is
  destroyed.

Given a path, `reset` skips moving HEAD and updates only the index for that path:
`git reset file.txt` is shorthand for `git reset --mixed HEAD file.txt`, which
simply **unstages** the file.

## When to use which

- **Revert** is the right tool for undoing commits that have **already been
  published or shared**, because it preserves history via a new commit instead of
  rewriting existing commits. Reverting a merge commit requires
  `-m` / `--mainline <parent-number>` to say which parent is the mainline.
- **Reset** is for local, unshared history — unstaging, uncommitting, or
  discarding work you never pushed.

The distinction is the same shared-vs-local line drawn by
[rebasing](/oks/git-best-practices/history/rebasing.md): rewrite freely in
private, but reach for revert once others may depend on the commit.

# Related

- [rebasing](/oks/git-best-practices/history/rebasing.md)
- [cherry-pick](/oks/git-best-practices/history/cherry-pick.md)
- [resolving conflicts](/oks/git-best-practices/branching/resolving-conflicts.md)
- [the staging area](/oks/git-best-practices/fundamentals/staging-area.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
- https://git-scm.com/docs/git-revert
