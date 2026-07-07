---
type: Git Workflow
title: Git Flow
description: A strict, release-oriented branching model with long-running main and develop branches plus dedicated feature, release, and hotfix branches.
resource: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
tags:
  - git
  - workflow
  - release-management
timestamp: 2026-07-07T00:00:00Z
---

# Git Flow

The Gitflow Workflow defines a strict branching model designed around the
project release. It was first published in a 2010 blog post by Vincent Driessen
at nvie, and it remains a useful model for teams that ship discrete, versioned
releases rather than deploying continuously.

## The branch structure

Instead of a single main branch, Gitflow uses **two long-running branches**:

- **`main`** stores the official release history.
- **`develop`** serves as an integration branch for features.

Around those, three kinds of supporting branches come and go:

- **Feature branches** are branched off `develop` and merged back into `develop`
  once the feature is complete. This is where day-to-day work happens.
- **Release branches** support preparation of a new production release
  (version-bumping, last-minute fixes, release notes). A release branch is
  merged into **both** `main` and `develop` so the stabilization work is not
  lost.
- **Hotfix branches** provide a dedicated channel for patching production. A
  hotfix branch is likewise merged into **both** `main` and `develop`, so an
  urgent production fix also flows back into ongoing development.

The `git-flow` extension library automates the branch bookkeeping; running
`git flow init` on an existing repository creates the `develop` branch.

## Trade-offs and when to use it

Gitflow's explicit release and hotfix branches make it well suited to software
with scheduled releases and multiple versions in the wild that must be patched
independently. The structure gives everyone a shared, unambiguous place for each
kind of work.

That structure is also its cost. The extra long-running branches and the
merge-into-both discipline add overhead, and the model has fallen in popularity
in favor of trunk-based workflows for teams practicing continuous delivery — see
[trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md).
If your team deploys frequently from a single always-releasable branch,
[GitHub flow](/oks/git-best-practices/workflows/github-flow.md) is usually a
lighter fit. Because Gitflow relies on many parallel branches, a clear
[branch naming convention](/oks/git-best-practices/branching/naming-conventions.md)
and a deliberate stance on
[merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md) matter
more here than in simpler models.

# Related

- [GitHub flow](/oks/git-best-practices/workflows/github-flow.md)
- [trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md)
- [forking workflow](/oks/git-best-practices/workflows/forking-workflow.md)
- [branch naming conventions](/oks/git-best-practices/branching/naming-conventions.md)
- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)

# Sources

- https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
