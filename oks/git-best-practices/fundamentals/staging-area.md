---
type: Git Concept
title: The Staging Area
description: The index lets you build commits incrementally by choosing exactly which changes go into the next snapshot.
resource: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
tags:
  - git
  - fundamentals
  - staging
  - index
timestamp: 2026-07-07T00:00:00Z
---

# The Staging Area

The staging area — also called the **index** — is the section of Git that
records what will go into your next commit. It sits between your working tree
and your commit history, and it is the tool that lets you shape a commit
deliberately instead of dumping everything you've touched into one blob.

## Tracked vs. untracked

Files in your working directory are either **tracked** or **untracked**.
Tracked files are ones Git already knows about: they were in the last snapshot,
or they have been newly staged. Untracked files are everything else — files not
in your last snapshot and not yet staged. Git will not include an untracked file
in a commit until you tell it to.

## `git add` and the snapshot-at-add-time rule

`git add` is a multipurpose command. You use it to begin tracking new files, to
stage modified files, and to mark merge-conflicted files as resolved.

A subtle but important detail: Git stages a file **exactly as it is at the
moment you run `git add`**. If you edit the file again afterward, that later edit
is *not* staged — you must run `git add` again to stage the newest version
before committing. Otherwise you'll commit the older, already-staged content and
leave your latest change behind.

## Reading the state with `git status` and `git diff`

`git status` reports files in three groupings that map directly onto the states:

- **Changes to be committed** — staged.
- **Changes not staged for commit** — modified but unstaged.
- **Untracked files** — not yet tracked.

`git diff` shows you the *content* behind those groupings, and which two things
it compares depends on its arguments:

- `git diff` with no arguments compares the **working directory to the staging
  area** — i.e. what you've changed but not yet staged.
- `git diff --staged` (equivalently `--cached`) compares the **staging area to
  the last commit** — i.e. exactly what will be in your next commit.

Getting these two straight is the single biggest source of "wait, why didn't
that change get committed?" confusion.

## Why the staging area is a feature, not overhead

The staging area lets you build commits **incrementally**: you can selectively
choose which modified files — or, with `git add --patch`, which individual
changes within a file — to include in the next commit, leaving the rest
unstaged. That is what makes it possible to keep commits
[atomic](/oks/git-best-practices/commits/atomic-commits.md) even when your
working tree contains several unrelated changes at once.

# Related

- [the repository model](/oks/git-best-practices/fundamentals/repository-model.md)
- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md)
- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
