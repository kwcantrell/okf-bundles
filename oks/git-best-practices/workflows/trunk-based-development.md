---
type: Git Workflow
title: Trunk-Based Development
description: Developers merge small, frequent updates straight to a single trunk, enabling continuous integration and delivery.
resource: https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
tags:
  - git
  - workflow
  - continuous-integration
  - devops
timestamp: 2026-07-07T00:00:00Z
---

# Trunk-Based Development

Trunk-based development is a version-control management practice where developers
merge small, frequent updates to a core **trunk** (the `main` branch). Rather
than letting work accumulate on long-lived branches, contributors integrate
often — ideally at least daily — so the trunk always reflects the latest
integrated state of the project.

## How it works

It is a more open model than fork- or release-heavy alternatives: all developers
have access to the main code, which enables teams to iterate quickly and to
implement CI/CD. Two practices make this safe at speed:

- **Immediate code review.** Review is performed right away rather than being
  placed into an asynchronous system for later. Short-lived branches and small
  changes keep each review quick.
- **Automated tests as preemptive review.** A strong automated test suite
  provides a layer of preemptive code review, catching regressions the moment
  changes land so the trunk stays releasable.

Because changes are small and land continuously, they are typically guarded by
[branch protection](/oks/git-best-practices/branching/branch-protection.md) with
required status checks, and they lean heavily on keeping each change
[atomic](/oks/git-best-practices/commits/atomic-commits.md).

## Trade-offs and when to use it

Trunk-based development is currently the standard for high-performing
engineering teams: it sets and maintains a software release cadence via a
simplified branching strategy, and Gitflow has fallen in popularity in favor of
it for modern continuous software delivery and DevOps.

The trade-off is that it demands discipline and infrastructure. Without robust
automated testing and fast review, merging frequently to a shared trunk is
risky. Teams also often need feature flags to merge incomplete work safely.
Where a project cannot yet support that automation, a more gated model such as
[GitHub flow](/oks/git-best-practices/workflows/github-flow.md) or
[Git Flow](/oks/git-best-practices/workflows/git-flow.md) may be a more
comfortable starting point.

# Related

- [GitHub flow](/oks/git-best-practices/workflows/github-flow.md)
- [Git Flow](/oks/git-best-practices/workflows/git-flow.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)
- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)
- [ci integration](/oks/git-best-practices/automation/ci-integration.md)

# Sources

- https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
