---
type: OKF Concept Index
title: Git Workflows
description: The branching models teams use to collaborate — GitHub flow, Git Flow, trunk-based development, and the forking workflow — and when each fits.
resource: https://docs.github.com/en/get-started/using-github/github-flow
tags:
  - git
  - workflows
  - collaboration
timestamp: 2026-07-07T00:00:00Z
---

# Git Workflows

A workflow is the agreed set of conventions a team follows for branching,
integrating, and releasing. There is no single correct workflow — the right
choice depends on team size, release cadence, and how much process the project
needs. These concepts describe four widely used models and their trade-offs.

## Concepts

- [GitHub flow](/oks/git-best-practices/workflows/github-flow.md) — a lightweight branch-and-pull-request model built around a single deployable default branch.
- [Git Flow](/oks/git-best-practices/workflows/git-flow.md) — a stricter release-oriented model with long-running `main` and `develop` branches plus release and hotfix branches.
- [trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md) — small, frequent merges to a single trunk, optimized for CI/CD.
- [forking workflow](/oks/git-best-practices/workflows/forking-workflow.md) — every contributor works from their own server-side fork, common in open source.
