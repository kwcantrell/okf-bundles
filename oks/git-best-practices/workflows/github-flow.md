---
type: Git Workflow
title: GitHub Flow
description: A lightweight, branch-based workflow — branch, commit, open a pull request, review, merge, and delete — built around a single deployable default branch.
resource: https://docs.github.com/en/get-started/using-github/github-flow
tags:
  - git
  - github
  - workflow
timestamp: 2026-07-07T00:00:00Z
---

# GitHub Flow

GitHub flow is a lightweight, branch-based workflow that is useful for
developers and non-developers alike collaborating on a project. It keeps
ceremony to a minimum: there is one long-lived branch (the default branch), and
all work happens on short-lived branches that come back through pull requests.

## The steps

1. **Create a branch.** Give it a short, descriptive name so collaborators can
   see what is in progress at a glance. Branching off the default branch means
   your work is isolated until it is ready.
2. **Make changes.** Commit and push to your branch, giving each commit a
   descriptive message so others understand what it contains.
3. **Open a pull request.** Once your changes are pushed, open a
   [pull request](/oks/git-best-practices/collaboration/pull-requests.md) to ask
   collaborators for feedback. You can open one early to start a conversation,
   not only when the work is finished.
4. **Review and iterate.** Reviewers can comment on the whole pull request or on
   specific lines and files. Pushing new commits to the branch automatically
   updates the pull request, so review and revision happen in one place.
5. **Merge.** After the pull request is approved, merge it into the default
   branch.
6. **Delete the branch.** Deleting the merged branch signals that the work is
   complete while the historical record is preserved in the default branch.

## Trade-offs and when to use it

GitHub flow's strength is simplicity: a single always-deployable default branch
and short-lived feature branches. It fits teams that release continuously or
frequently and want minimal branching overhead. Because it assumes the default
branch is always deployable, it pairs naturally with
[branch protection](/oks/git-best-practices/branching/branch-protection.md) and
automated checks to keep that branch healthy.

Its main limitation is that it has no built-in place to stage and stabilize a
specific release over time — if your project needs to maintain multiple released
versions in parallel and patch them independently, the release-and-hotfix
structure of [Git Flow](/oks/git-best-practices/workflows/git-flow.md) may fit
better. For fast-moving teams practicing continuous integration,
[trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md)
pushes the same simplicity even further.

# Related

- [Git Flow](/oks/git-best-practices/workflows/git-flow.md)
- [trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md)
- [forking workflow](/oks/git-best-practices/workflows/forking-workflow.md)
- [pull requests](/oks/git-best-practices/collaboration/pull-requests.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)

# Sources

- https://docs.github.com/en/get-started/using-github/github-flow
