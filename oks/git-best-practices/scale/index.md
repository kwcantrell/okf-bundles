---
type: OKF Concept Index
title: Scale
description: Strategies for large repositories and multi-project setups — monorepo vs. polyrepo, Git LFS for large files, and sparse checkout.
resource: https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
tags:
  - git
  - scale
timestamp: 2026-07-07T00:00:00Z
---

# Scale

As repositories and organizations grow, Git's defaults start to strain: a single
repo may hold many projects, files may be too large to version normally, and a
working tree may be too big to check out in full. These concepts cover the
structural choice between one repo and many, and the mechanisms — Git LFS and
sparse checkout — that keep a large repository workable.

## Concepts

- [monorepo vs. polyrepo](/oks/git-best-practices/scale/monorepo-vs-polyrepo.md) — one shared repository or many, and how submodules compose repos.
- [large files and Git LFS](/oks/git-best-practices/scale/large-files-lfs.md) — versioning large binaries via pointer files.
- [sparse checkout](/oks/git-best-practices/scale/sparse-checkout.md) — checking out only a subset of a large working tree.
