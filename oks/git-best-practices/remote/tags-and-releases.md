---
type: Remote Practice
title: Tags and Releases
description: Lightweight vs. annotated tags, why tags aren't pushed by default, and how GitHub Releases build on tags to publish notes and binary assets.
resource: https://git-scm.com/book/en/v2/Git-Basics-Tagging
tags:
  - git
  - github
  - remote
  - tags
  - releases
timestamp: 2026-07-07T00:00:00Z
---

# Tags and Releases

Tags mark specific points in history as important — most often a release. Git
offers two kinds, and the choice matters.

## Two kinds of tag

- **Lightweight tags** are just a pointer (a commit checksum) to a commit,
  created with `git tag v1.4-lw`. They carry no extra metadata.
- **Annotated tags** are full objects storing the tagger's name, email, date, and
  a message, and they can be GPG-signed. Create one with
  `git tag -a v1.4 -m "my version 1.4"`.

For anything you publish, prefer **annotated** (and ideally
[signed](/oks/git-best-practices/security/signed-tags.md)) tags — the recorded
author, date, and message make a release auditable.

## Tags are not pushed by default

`git push` does **not** transfer tags to a remote automatically. You must push a
specific tag with `git push origin v1.5`, or all of them at once with
`git push origin --tags`. Note that `--follow-tags` pushes only annotated tags,
which is usually what you want for a release.

## Checking out a tag

Checking out a tag (e.g. `git checkout v2.0.0`) puts the repository in a
**detached HEAD** state. To make changes from that point safely, create a branch:
`git checkout -b version2 v2.0.0`.

## GitHub Releases

**GitHub Releases** are built on top of Git tags to mark points in history, though
a release's creation date can differ from its underlying tag's date, since the
two are created independently. A release can add release notes plus **binary file
assets**, and GitHub automatically generates downloadable ZIP and tarball
archives of the repository at the tagged point (admins control whether
[Git LFS](/oks/git-best-practices/scale/large-files-lfs.md) objects are included).
A single release supports up to **1,000 assets**, each capped at **2 GiB**.

# Related

- [signed tags](/oks/git-best-practices/security/signed-tags.md)
- [fetch, pull, push](/oks/git-best-practices/remote/fetch-pull-push.md)
- [large files and Git LFS](/oks/git-best-practices/scale/large-files-lfs.md)
- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Basics-Tagging
- https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
