---
type: Scale Practice
title: Large Files and Git LFS
description: Version large files by storing a small pointer in Git while the real content lives elsewhere — how Git LFS works, its per-file limits, and its restrictions.
resource: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
tags:
  - git
  - github
  - scale
  - lfs
timestamp: 2026-07-07T00:00:00Z
---

# Large Files and Git LFS

Git is built for text and struggles with large binaries: every version of a big
file bloats every clone, since Git stores
[snapshots](/oks/git-best-practices/fundamentals/repository-model.md) of the whole
tree. **Git Large File Storage (Git LFS)** solves this.

## How it works

Git LFS is an open-source Git extension that lets large files be versioned like
other files by storing a small **pointer file** in the Git repository instead of
the file's actual contents. The pointer records the Git LFS version in use, a
unique object identifier (oid) for the file, and the file's size. When the
repository is cloned, GitHub uses the pointer as a map to **fetch the actual large
file** from LFS storage.

## Setup

Git LFS must be **downloaded and installed separately from Git**. To track a file
type, run `git lfs track` followed by the file extension (e.g.
`git lfs track "*.psd"`); this records the pattern in `.gitattributes`. GitHub's
repository best-practices guidance recommends using Git LFS for large files for
performance, since GitHub limits the sizes of files allowed in ordinary
repositories.

## Limits and restrictions

- **Per-file size** varies by plan: **2 GB** on Free and Pro, **4 GB** on Team,
  and **5 GB** on Enterprise Cloud. Any file above the absolute **5 GB** ceiling
  is rejected by Git LFS with an error.
- Git LFS **cannot be used with GitHub Pages sites or with template
  repositories**.

## Trade-offs

LFS keeps clones fast and repositories small, but it adds a dependency: every
contributor and CI job needs Git LFS installed, and the objects live in separate
storage that has its own quotas and access rules. For files that are large *and*
regenerable, it is often better to keep them out of the repo entirely via
[.gitignore hygiene](/oks/git-best-practices/security/gitignore-hygiene.md) and
publish them as [release assets](/oks/git-best-practices/remote/tags-and-releases.md)
instead.

# Related

- [gitignore hygiene](/oks/git-best-practices/security/gitignore-hygiene.md)
- [tags and releases](/oks/git-best-practices/remote/tags-and-releases.md)
- [monorepo vs. polyrepo](/oks/git-best-practices/scale/monorepo-vs-polyrepo.md)
- [the repository model](/oks/git-best-practices/fundamentals/repository-model.md)

# Sources

- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
