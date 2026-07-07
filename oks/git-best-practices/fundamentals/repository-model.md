---
type: Git Concept
title: The Git Repository Model
description: Git stores your project as a stream of snapshots referred to by checksum, and tracks files through three states across three sections.
resource: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
tags:
  - git
  - fundamentals
  - snapshots
timestamp: 2026-07-07T00:00:00Z
---

# The Git Repository Model

Most version-control systems think in terms of files and the changes made to
each file over time. Git does not. Git stores its data as a series of
**snapshots** of your entire project at commit time, not as a set of file-based
changes or deltas. When you commit, Git takes a picture of what all your tracked
files look like at that moment and stores a reference to that snapshot.

To stay efficient, if a file has not changed between commits, Git does not store
it again — it stores only a link to the previous identical file. This is why
it's more accurate to picture Git as a *stream of snapshots* than as a series of
diffs. (Diffs still exist as a *view* Git computes on demand, e.g. `git diff`,
but they are not the storage model.)

## The three states

Every file Git manages is in one of three main states:

- **Modified** — you have changed the file but not yet committed it.
- **Staged** — you have marked a modified file, in its current version, to go
  into your next commit snapshot.
- **Committed** — the data is safely stored in your local database.

## The three sections

These states correspond to three sections of a Git project:

- **Working tree** — a single checkout of one version of the project on disk for
  you to edit.
- **Staging area (the index)** — a file, usually inside the Git directory, that
  records what will go into your next commit. See
  [staging area](/oks/git-best-practices/fundamentals/staging-area.md).
- **Git directory (`.git`)** — where Git stores the metadata and object database
  for your project. This is what is copied when you clone a repository from
  another computer.

## Why this matters in practice

Two consequences follow directly from the model and are worth internalizing:

- **Git is local-first.** Most operations only need local files and resources —
  browsing history, diffing, committing, and switching branches all work with no
  network. This makes Git fast and usable offline; you sync with others
  deliberately, not on every action.
- **Git is tamper-evident.** Everything is checksummed before it is stored and
  is then referred to by that checksum — a 40-character SHA-1 hash computed from
  the contents. You cannot change the contents of any file or commit without Git
  knowing, because the checksum would no longer match. Integrity is built into
  the storage layer, not bolted on.

Because the tip of a branch is just a snapshot, the final tree is identical
whether you got there in one commit or five — a fact that underpins
[atomic commits](/oks/git-best-practices/commits/atomic-commits.md).

# Related

- [staging area](/oks/git-best-practices/fundamentals/staging-area.md)
- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md)
- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)

# Sources

- https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
