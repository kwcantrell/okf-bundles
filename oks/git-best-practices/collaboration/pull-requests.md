---
type: Collaboration Practice
title: Pull Requests
description: GitHub's foundational collaboration feature for proposing, discussing, and reviewing changes before they merge, organized across conversation, commits, checks, and files views.
resource: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
tags:
  - git
  - github
  - collaboration
  - pull-requests
timestamp: 2026-07-07T00:00:00Z
---

# Pull Requests

A pull request (PR) is a proposal to merge code changes into a project. It is
described as GitHub's foundational collaboration feature: the place where changes
are discussed and reviewed before they are merged. Nearly every team workflow —
[GitHub flow](/oks/git-best-practices/workflows/github-flow.md), the
[forking workflow](/oks/git-best-practices/workflows/forking-workflow.md), and
others — routes work through pull requests.

## How a pull request is organized

A pull request presents the proposed change across several tabs:

- **Conversation** — a description of the changes, a timeline of events, and the
  comments and reviews from collaborators. This is the narrative home of the PR.
- **Commits** — all commits made to the pull request branch, in chronological
  order. Well-shaped [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)
  make this tab a readable story rather than noise.
- **Checks** — the status of automated tests, builds, and other CI workflows
  triggered by pushes to the branch.
- **Files changed** — the diff between the proposed changes and the existing
  code, and where line-by-line [review](/oks/git-best-practices/collaboration/code-review.md)
  comments are left.

## Behavior worth knowing

- **Drafts.** When creating a pull request, a contributor can choose to make it a
  [draft](/oks/git-best-practices/collaboration/draft-prs.md), which cannot be
  merged and does not automatically request review from code owners.
- **Live updating.** Pushing new commits to the branch automatically updates the
  pull request, so review happens against the latest state.
- **Generated refs.** GitHub creates temporary read-only Git references for a
  pull request, including one pointing to its latest commit and — when there are
  no conflicts — an optional simulated merge branch. These are what let CI test
  the *merged* result before you actually merge.

## Good practice

Write a clear description that explains the *why* (the diff already shows the
*what*), keep the change small enough to review well, and let checks and
[code review](/oks/git-best-practices/collaboration/code-review.md) do their job
before merging. Gating the target branch with
[branch protection](/oks/git-best-practices/branching/branch-protection.md)
ensures those steps actually happen.

# Related

- [code review](/oks/git-best-practices/collaboration/code-review.md)
- [draft pull requests](/oks/git-best-practices/collaboration/draft-prs.md)
- [CODEOWNERS](/oks/git-best-practices/collaboration/codeowners.md)
- [GitHub flow](/oks/git-best-practices/workflows/github-flow.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)

# Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
