---
type: Branching Practice
title: Branch Protection
description: GitHub branch protection rules enforce reviews, status checks, signed commits, linear history, and force-push restrictions on important branches.
resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
tags:
  - git
  - github
  - branching
  - security
timestamp: 2026-07-07T00:00:00Z
---

# Branch Protection

Branch protection rules let you put guardrails on the branches that matter most —
typically your default branch and any release branches — so that changes can only
reach them through a controlled, reviewed path. On GitHub these rules are what
turn "the default branch should always be deployable" from a hope into an
enforced policy.

## What you can enforce

- **Required reviews.** Enforce that every pull request receives a specific
  number of approving reviews before anyone can merge into the protected branch.
  This pairs directly with [code review](/oks/git-best-practices/collaboration/code-review.md)
  and [CODEOWNERS](/oks/git-best-practices/collaboration/codeowners.md).
- **Required status checks.** Named checks (CI builds, tests, linters) must show
  a successful, skipped, or neutral status before collaborators can change the
  protected branch. This is the backbone of a
  [trunk-based](/oks/git-best-practices/workflows/trunk-based-development.md)
  or GitHub-flow model where the branch stays releasable.
- **Required signed commits.** When commit signing is required, contributors and
  bots can only push commits that have been signed and verified. See
  [signing commits](/oks/git-best-practices/commits/signing-commits.md).
- **Linear history.** Enforcing linear history requires that pull requests merged
  into the protected branch use a squash merge or a rebase merge, blocking
  ordinary merge commits — relevant to your
  [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)
  decision.
- **Force-push restrictions.** By default GitHub blocks force pushes to protected
  branches, though administrators can selectively enable them for specific users
  or teams.
- **Push restrictions.** Administrators can restrict who is allowed to push to
  matching branches by naming specific people, teams, or apps.

## Targeting branches

A branch protection rule can target a specific branch, all branches, or any
branch matching a name pattern specified with `fnmatch` syntax — for example
`*release*` to cover every release branch at once. This is where a consistent
[branch naming convention](/oks/git-best-practices/branching/naming-conventions.md)
pays off: good prefixes make protection patterns simple and reliable.

## Trade-offs

Protection buys safety at the cost of some friction — required reviews and
green checks slow down a merge, which is the point. Tune the strictness to the
branch and the team: a solo prototype needs little, while a shared production
branch benefits from the full set. The goal is guardrails proportionate to the
blast radius of a mistake on that branch.

# Related

- [branch naming conventions](/oks/git-best-practices/branching/naming-conventions.md)
- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)
- [code review](/oks/git-best-practices/collaboration/code-review.md)
- [signing commits](/oks/git-best-practices/commits/signing-commits.md)
- [trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md)

# Sources

- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
