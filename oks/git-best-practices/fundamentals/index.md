---
type: OKF Concept Index
title: Git Fundamentals
description: How Git models your project — snapshots and the three states, the staging area, and the refs and objects underneath.
resource: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
tags:
  - git
  - fundamentals
  - internals
timestamp: 2026-07-07T00:00:00Z
---

# Git Fundamentals

Understanding Git's data model makes every other practice easier: once you know
that Git stores snapshots referred to by checksum and that a commit is just a
pointer into a graph of objects, commands like rebase, revert, and reset stop
feeling like magic.

## Concepts

- [repository model](/oks/git-best-practices/fundamentals/repository-model.md) — Git stores snapshots, not diffs; the three file states and three project sections.
- [staging area](/oks/git-best-practices/fundamentals/staging-area.md) — the index, `git add`, and building commits incrementally.
- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md) — blobs, trees, and commits; refs, HEAD, and tags.
