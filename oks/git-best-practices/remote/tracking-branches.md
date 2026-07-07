---
type: Remote Practice
title: Tracking Branches
description: Remote-tracking branches mirror the remote's state, and upstream tracking branches link a local branch to a remote one so pull and push know where to go.
resource: https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches
tags:
  - git
  - remote
  - branches
timestamp: 2026-07-07T00:00:00Z
---

# Tracking Branches

Two related concepts share the word "tracking," and keeping them distinct clears
up a lot of confusion about remotes.

## Remote-tracking branches

A **remote-tracking branch** is a local reference named `<remote>/<branch>` —
for example `origin/master` — that Git **moves automatically** during network
communication to reflect the state of that branch on the remote. You do not edit
these directly; they are Git's cached snapshot of where the remote was as of your
last [fetch](/oks/git-best-practices/remote/fetch-pull-push.md).

## Upstream (tracking) branches

A **tracking branch** (also called an upstream branch) is a *local* branch with a
direct relationship to a remote branch. That relationship is what lets a plain
`git pull` on the branch know automatically which server to fetch from and which
branch to merge.

Ways to establish it:

- **Checkout by name:** `git checkout serverfix` (or the explicit
  `git checkout --track origin/serverfix`) automatically creates a local branch
  tracking the matching remote branch, when the name matches exactly one remote
  branch.
- **Set on an existing branch:** `git branch -u origin/serverfix` (i.e.
  `--set-upstream-to`) sets or changes the upstream for the current local branch.

## Inspecting status

`git branch -vv` lists your local branches with their tracked remote branch and
ahead/behind counts, e.g. `[origin/serverfix: ahead 3, behind 1]`. Note a
gotcha: **those numbers reflect only your last fetch**, so run `git fetch --all`
first if you need them to be accurate.

# Related

- [fetch, pull, push](/oks/git-best-practices/remote/fetch-pull-push.md)
- [tags and releases](/oks/git-best-practices/remote/tags-and-releases.md)
- [naming conventions](/oks/git-best-practices/branching/naming-conventions.md)
- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches
