---
type: Git Workflow
title: Forking Workflow
description: Every contributor works from their own server-side fork and proposes changes upstream via pull requests — the common model for open-source projects.
resource: https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
tags:
  - git
  - workflow
  - open-source
  - forking
timestamp: 2026-07-07T00:00:00Z
---

# Forking Workflow

The Forking Workflow gives every developer their own server-side repository
instead of relying on one single central repository. It is fundamentally
different from workflows built around a shared repo, and it is the model most
commonly used in public open-source projects, where you cannot hand write access
to every potential contributor.

## How it works

Each contributor ends up with **two** Git repositories: a private local one and
a public server-side one — their **fork**. The key access rule is that no other
developer is allowed to push to another user's public fork, but anyone can pull
from it. Your fork is yours; the official repository is the maintainer's.

The contribution cycle looks like this:

1. A contributor pushes finished commits to their own public fork.
2. They file a [pull request](/oks/git-best-practices/collaboration/pull-requests.md)
   against the main repository to let the maintainer know an update is ready to
   be integrated.
3. The project maintainer pulls the contributor's changes into their local
   repository, verifies they don't break the project, merges them into the local
   `main` branch, and then pushes `main` to the official repository.

This gives maintainers a controlled integration point: contributions are
proposed, not pushed, and nothing enters the official history without the
maintainer's action.

## Trade-offs and when to use it

The forking workflow shines when contributors are numerous and untrusted — the
classic open-source situation — because it needs no central write access.
GitHub's own guidance, however, favors having *regular* collaborators work from
a single shared repository and reserves forking for contributors unaffiliated
with the project. For an internal team, the extra fork-and-sync overhead usually
isn't worth it, and a shared-repo model like
[GitHub flow](/oks/git-best-practices/workflows/github-flow.md) is simpler. The
underlying integration step is the same regardless: a
[pull request](/oks/git-best-practices/collaboration/pull-requests.md) reviewed
before merge.

# Related

- [GitHub flow](/oks/git-best-practices/workflows/github-flow.md)
- [Git Flow](/oks/git-best-practices/workflows/git-flow.md)
- [pull requests](/oks/git-best-practices/collaboration/pull-requests.md)

# Sources

- https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
- https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
