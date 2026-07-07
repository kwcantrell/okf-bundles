---
type: OKF Concept Index
title: Branching Practices
description: How to name branches, protect important ones, choose between merging and rebasing, and resolve the conflicts that arise.
resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
tags:
  - git
  - branching
  - github
timestamp: 2026-07-07T00:00:00Z
---

# Branching Practices

Branches are cheap in Git — a branch is just a movable pointer to a commit — so
teams create them freely. The practices here keep that freedom from turning into
chaos: consistent names, guardrails on the branches that matter, a clear-eyed
choice between merge and rebase, and a calm procedure for conflicts.

## Concepts

- [naming conventions](/oks/git-best-practices/branching/naming-conventions.md) — what characters are allowed and how to name branches for clarity.
- [branch protection](/oks/git-best-practices/branching/branch-protection.md) — required reviews, status checks, signing, and force-push rules on protected branches.
- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md) — two ways to integrate branches, and their trade-offs.
- [resolving conflicts](/oks/git-best-practices/branching/resolving-conflicts.md) — reading conflict markers and finishing a conflicted merge.
