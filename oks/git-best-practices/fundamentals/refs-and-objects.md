---
type: Git Concept
title: Refs and Objects
description: Git is a content-addressable filesystem of blobs, trees, and commits, with refs and HEAD as friendly named pointers into that object graph.
resource: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
tags:
  - git
  - fundamentals
  - internals
  - refs
timestamp: 2026-07-07T00:00:00Z
---

# Refs and Objects

Underneath the porcelain commands, Git is a **content-addressable filesystem**:
you can hand it content and get back a unique SHA-1 key, then use that key to
retrieve the content later. Objects live under `.git/objects/`, filed using the
first two characters of the hash as a subdirectory name and the remaining 38 as
the filename.

## The three core object types

- **Blob** — stores file *content* only. A blob does not know its own filename.
- **Tree** — stores directory structure: it points at blobs and subtrees, each
  entry carrying a mode and a name. Trees are where filenames live.
- **Commit** — points to exactly one tree (the project snapshot), plus zero or
  more parent commit SHA-1s, along with author and committer information and the
  commit message.

Because a commit points to one tree and to zero or more parents, commits form a
**linked history graph**: the parent pointers are the edges. A first commit has
no parent; an ordinary commit has one; a merge commit has two or more. This
graph is the thing that rebase, revert, and bisect all operate on.

## References

A **reference** (ref) is simply a named pointer to a SHA-1 value, stored as a
file under `.git/refs`. Branches live under `.git/refs/heads` and tags under
`.git/refs/tags`. Refs exist so you can use a friendly name like `main` instead
of memorizing a raw 40-character hash — a branch is nothing more than a movable
pointer to a commit.

## HEAD

**HEAD** is a *symbolic* reference: normally it points at the current branch, so
its file contents look like `ref: refs/heads/main`. When you check out a commit
directly (rather than a branch), you enter a **detached HEAD** state, where HEAD
contains a commit SHA-1 directly instead of pointing at a branch. That is why
commits made in a detached HEAD state are easy to lose — no branch is following
along to keep them reachable.

## Lightweight vs. annotated tags

Tags come in two forms:

- **Lightweight tags** are refs that never move; they simply point at a commit.
- **Annotated tags** are full objects containing a tagger, date, and message,
  and they can point at any Git object, not only commits.

Annotated tags are the right choice for releases because they record *who*
tagged *what* and *when*, and they can be cryptographically signed.

Knowing that a branch is just a ref is what makes safe
[branch naming](/oks/git-best-practices/branching/naming-conventions.md) and
history operations intuitive rather than mysterious.

# Related

- [the repository model](/oks/git-best-practices/fundamentals/repository-model.md)
- [staging area](/oks/git-best-practices/fundamentals/staging-area.md)
- [branch naming conventions](/oks/git-best-practices/branching/naming-conventions.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
- https://git-scm.com/book/en/v2/Git-Internals-Git-References
