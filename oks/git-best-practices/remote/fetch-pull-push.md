---
type: Remote Practice
title: Fetch, Pull, and Push
description: The three commands that move commits between repositories — fetch downloads, pull fetches then merges, and push uploads — plus how they interact safely.
resource: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
tags:
  - git
  - remote
  - fetch
  - pull
  - push
timestamp: 2026-07-07T00:00:00Z
---

# Fetch, Pull, and Push

Three commands move commits between your repository and a remote. Understanding
exactly what each one touches is what keeps synchronizing safe.

## Fetch: download without changing your work

`git fetch <remote>` downloads all new data from a remote and updates your
**remote-tracking branches** (e.g. `origin/master`) **without touching your
working files or merging anything** into your current branch. It is always safe
to run: it only updates your view of the remote's state, which you can then
inspect before integrating.

## Pull: fetch, then integrate

`git pull` is effectively `git fetch` followed by `git merge`, and it only works
automatically when the current branch is set up to
[track](/oks/git-best-practices/remote/tracking-branches.md) a remote branch.

Since **Git 2.27**, `git pull` expects the `pull.rebase` configuration variable
to be set explicitly — `false` to merge (the historical default) or `true` to
rebase — to avoid a warning. Choosing `true` gives the linear history discussed
in [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md); the
important thing is to set it deliberately.

## Push: upload your commits

`git push <remote> <branch>` uploads your local commits to a remote. It is
**rejected if someone else has pushed to that branch in the meantime** — Git
refuses to let you overwrite their work, requiring you to fetch and incorporate
their changes first. This rejection is a feature: it prevents silent loss of
others' commits. Resist the urge to `--force` past it on shared branches; fetch
and reconcile instead.

## Note on cloning

Cloning a repository automatically sets up your local default branch to
[track](/oks/git-best-practices/remote/tracking-branches.md) the remote's default
branch, which is why `git pull` and `git push` "just work" immediately after a
fresh clone.

# Related

- [tracking branches](/oks/git-best-practices/remote/tracking-branches.md)
- [tags and releases](/oks/git-best-practices/remote/tags-and-releases.md)
- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)
- [the repository model](/oks/git-best-practices/fundamentals/repository-model.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
