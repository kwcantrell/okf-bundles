---
type: Branching Practice
title: Merge vs. Rebase
description: Two ways to integrate one branch into another — a non-destructive merge commit or a linear rewrite via rebase — and the trade-offs between them.
resource: https://www.atlassian.com/git/tutorials/merging-vs-rebasing
tags:
  - git
  - branching
  - merge
  - rebase
timestamp: 2026-07-07T00:00:00Z
---

# Merge vs. Rebase

Both `git merge` and `git rebase` solve the same problem — integrating changes
from one branch into another — but they do it in very different ways. Neither is
universally "correct"; they trade history fidelity against history tidiness, and
teams reasonably choose differently.

## Merging

Merging creates a new **merge commit** that ties together the histories of both
branches without changing the existing branches. It is a non-destructive
operation: your original commits are left exactly as they were, and the merge
commit records the moment the two lines of work came together.

- **Pro:** it preserves context. History honestly shows that work happened in
  parallel and when upstream changes were incorporated. Nothing is rewritten, so
  it is safe on shared branches.
- **Con:** on a busy repository, frequent merges from `main` into feature
  branches litter history with extraneous merge commits, which some teams find
  noisy.

## Rebasing

Rebasing moves the entire feature branch so it begins at the tip of the base
branch, creating **brand-new commits** for each original commit. The result is a
perfectly linear project history that reads as though the work happened in
series, eliminating the merge commits that `git merge` would have introduced.

- **Pro:** a clean, linear history that is easy to read and `git log` through.
  **Interactive** rebasing additionally lets you alter commits as they are moved —
  reordering, squashing, and rewording — which is commonly used to clean up
  messy history *before* merging into `main`.
- **Con:** it loses the context a merge commit provides — you can no longer see
  when upstream changes were folded into the feature branch. More importantly,
  because rebasing replaces commits with new ones, it is unsafe on shared
  history: the **golden rule of rebasing** is to never rebase commits that exist
  outside your repository and that other people may have based work on. Rebasing
  public commits forces collaborators to re-merge and produces confusing
  duplicate-looking history.

## Choosing

A common, pragmatic compromise: **rebase locally to tidy up your own unpushed
work, then merge to integrate.** Rebase your feature branch onto the latest base
to keep it current and clean; use a merge (or a squash/rebase merge enforced by
[branch protection](/oks/git-best-practices/branching/branch-protection.md)) to
bring it into the shared branch. Whichever you pick, integrating branches
eventually surfaces
[conflicts](/oks/git-best-practices/branching/resolving-conflicts.md), which both
strategies resolve the same way.

# Related

- [resolving conflicts](/oks/git-best-practices/branching/resolving-conflicts.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)
- [Git Flow](/oks/git-best-practices/workflows/git-flow.md)

# Sources

- https://www.atlassian.com/git/tutorials/merging-vs-rebasing
- https://git-scm.com/book/en/v2/Git-Branching-Rebasing
