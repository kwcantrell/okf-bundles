---
type: OKF Concept Index
title: Rewriting and Navigating History
description: Tools for reshaping and searching Git history — rebasing, interactive rebase, cherry-pick, revert vs. reset, and bisect.
resource: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
tags:
  - git
  - history
timestamp: 2026-07-07T00:00:00Z
---

# Rewriting and Navigating History

Git history is not immutable — you can reshape it before sharing and search it
efficiently after the fact. These concepts cover the tools that move, rewrite,
undo, and locate commits. A recurring theme is the line between *local* history
(yours to rewrite freely) and *shared* history (rewrite only with a revert, or
you disrupt collaborators).

## Concepts

- [rebasing](/oks/git-best-practices/history/rebasing.md) — replay commits onto a new base for a linear history.
- [interactive rebase](/oks/git-best-practices/history/interactive-rebase.md) — reorder, squash, edit, and drop commits with `git rebase -i`.
- [cherry-pick](/oks/git-best-practices/history/cherry-pick.md) — apply an individual commit's changes onto the current branch.
- [revert vs. reset](/oks/git-best-practices/history/revert-vs-reset.md) — undo work safely by adding a commit, or by moving the branch pointer.
- [bisect](/oks/git-best-practices/history/bisect.md) — binary-search history to find the commit that introduced a bug.
