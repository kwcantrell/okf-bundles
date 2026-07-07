---
type: History Practice
title: Rebasing
description: Replay a branch's commits onto a new base to produce a clean, linear history — and the golden rule that keeps it safe on shared branches.
resource: https://git-scm.com/book/en/v2/Git-Branching-Rebasing
tags:
  - git
  - history
  - rebase
timestamp: 2026-07-07T00:00:00Z
---

# Rebasing

Rebasing rewrites where a branch begins. Mechanically, `git rebase` finds the
common ancestor of your branch and the target branch, computes the diff
introduced by each commit on your branch, resets your branch to the target's
tip, and reapplies each of those diffs in turn as **new commits**. The result is
a cleaner, linear history that reads as though the work happened in series, even
when it actually happened in parallel on separate branches.

## Basic use

The everyday form is to bring a feature branch up to date with `main`:

```
git checkout feature
git rebase main
```

For more surgical moves, `git rebase --onto` replays only a subset of commits.
`git rebase --onto master server client` replays only the commits unique to
`client` (those it gained since diverging from `server`) onto `master`, without
requiring you to check out the target branch first.

## The golden rule

**Do not rebase commits that exist outside your repository and that other people
may have based work on.** Rebasing public/shared commits abandons the existing
commits and creates new, similar-but-different ones, which forces collaborators
to re-merge their work and produces confusing duplicate-looking history.

The safe practice follows directly: rebase *local* changes to clean up work
before pushing, but never rebase anything that has already been pushed and
shared.

## Trade-offs

Rebasing buys a linear, readable history at the cost of the context a merge
commit preserves — you lose the record of when upstream changes were folded in.
See [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md) for
the full comparison. To reshape commits (not just move them) while rebasing, use
[interactive rebase](/oks/git-best-practices/history/interactive-rebase.md).

# Related

- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)
- [interactive rebase](/oks/git-best-practices/history/interactive-rebase.md)
- [revert vs. reset](/oks/git-best-practices/history/revert-vs-reset.md)
- [resolving conflicts](/oks/git-best-practices/branching/resolving-conflicts.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Branching-Rebasing
