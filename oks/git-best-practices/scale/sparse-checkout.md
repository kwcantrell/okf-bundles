---
type: Scale Practice
title: Sparse Checkout
description: Populate a working tree with only a defined subset of tracked files — cone mode, the sparse index, and how it keeps huge monorepos workable.
resource: https://git-scm.com/docs/git-sparse-checkout
tags:
  - git
  - scale
  - sparse-checkout
timestamp: 2026-07-07T00:00:00Z
---

# Sparse Checkout

In a large [monorepo](/oks/git-best-practices/scale/monorepo-vs-polyrepo.md), you
rarely need every file on disk at once. `git sparse-checkout` changes a working
tree from containing **all** tracked files to containing only a defined **subset**
of them, and can switch which subset is present or restore the full working copy.

## Cone mode vs. non-cone mode

- **Cone mode** (the default, enabled via `core.sparseCheckoutCone`) accepts only
  **directories** as input and includes all files under each specified directory
  at any depth, plus files immediately under any leading/top-level directories. It
  uses a faster hash-based matching algorithm.
- **Non-cone mode** accepts arbitrary gitignore-style patterns but is
  **deprecated**, due to O(N*M) matching cost and pattern-semantics pitfalls.

Prefer cone mode for both performance and predictability.

## Commands

- **`git sparse-checkout set <dir1> <dir2> ...`** switches the repository into
  sparse-checkout mode restricted to the given directories, and automatically
  enables the `core.sparseCheckout`, `core.sparseCheckoutCone`, and `index.sparse`
  settings.
- **`git sparse-checkout list`** prints the directories or patterns currently
  defining the checkout (showing only recursive directories in cone mode).
- **`git sparse-checkout init`** is **deprecated** (kept for compatibility); it
  behaves like `set` with no paths. Historically both were needed, but `set` now
  performs all necessary configuration itself.

## The sparse index

A **sparse index** (enabled via `set --sparse-index` and driven by `index.sparse`)
shrinks the Git index itself to align with the sparse-checkout definition, giving
**significant performance advantages** for commands like `git status` and
`git add` in large repositories — because Git no longer has to walk entries for
paths that are not checked out.

## Trade-off

Sparse checkout makes a huge repository feel small locally, but developers see
only part of the tree, which can make cross-cutting changes and full-tree searches
harder. It complements rather than replaces the structural decision in
[monorepo vs. polyrepo](/oks/git-best-practices/scale/monorepo-vs-polyrepo.md).

# Related

- [monorepo vs. polyrepo](/oks/git-best-practices/scale/monorepo-vs-polyrepo.md)
- [large files and Git LFS](/oks/git-best-practices/scale/large-files-lfs.md)
- [the staging area](/oks/git-best-practices/fundamentals/staging-area.md)

# Sources

- https://git-scm.com/docs/git-sparse-checkout
