---
type: History Practice
title: Cherry-pick
description: Apply the changes from an individual commit onto the current branch as a new commit — the tool for backports and selective porting of fixes.
resource: https://git-scm.com/docs/git-cherry-pick
tags:
  - git
  - history
  - cherry-pick
timestamp: 2026-07-07T00:00:00Z
---

# Cherry-pick

`git cherry-pick <commit>` applies the changes introduced by an existing commit
and records them as a **new commit** on top of the current branch's tip. It is
the tool for pulling one specific change out of context — most commonly
backporting a bug fix to a maintenance branch without merging everything else.

## Useful options

- **`-n` / `--no-commit`** applies the change to the working tree and index
  without creating a commit. This lets you cherry-pick several commits and commit
  them together as one.
- **`-x`** appends a line `(cherry picked from commit ...)` to the new commit
  message, recording its origin. It is meant for cherry-picks **between public
  branches** (e.g. backporting to a maintenance branch) and should be avoided
  when cherry-picking from a private branch, where the referenced hash means
  nothing to others.
- **`-m` / `--mainline <parent-number>`** is required to cherry-pick a merge
  commit: because a merge has multiple parents, you must name which parent
  (numbered from 1) is the mainline for the replay.

## When it conflicts

If a cherry-pick cannot apply cleanly, the branch and HEAD stay at the last
successful commit, `CHERRY_PICK_HEAD` is set to point at the problematic commit,
and the conflicting files get conflict markers you must resolve before
continuing — the same markers described in
[resolving conflicts](/oks/git-best-practices/branching/resolving-conflicts.md).

## Trade-offs

Cherry-picking duplicates a change onto a new commit with a different hash, so
overusing it between long-lived branches creates divergent, hard-to-track
history. When you want *all* of a branch's commits on a new base, prefer
[rebasing](/oks/git-best-practices/history/rebasing.md) or a merge; reserve
cherry-pick for the genuinely selective case.

# Related

- [rebasing](/oks/git-best-practices/history/rebasing.md)
- [revert vs. reset](/oks/git-best-practices/history/revert-vs-reset.md)
- [resolving conflicts](/oks/git-best-practices/branching/resolving-conflicts.md)

# Sources

- https://git-scm.com/docs/git-cherry-pick
