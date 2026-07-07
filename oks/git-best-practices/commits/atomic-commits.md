---
type: Commit Practice
title: Atomic Commits
description: Make each commit a single logically separate changeset so history is easy to review, revert, and reason about.
resource: https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
tags:
  - git
  - commits
  - best-practices
timestamp: 2026-07-07T00:00:00Z
---

# Atomic Commits

Git's guidance is to make each commit a **logically separate changeset** rather
than combining unrelated work into one massive commit. An atomic commit does one
thing — fixes one bug, adds one small feature, renames one thing — and does it
completely. This is a discipline about the *shape* of a commit, complementary to
how you [word its message](/oks/git-best-practices/commits/commit-message-style.md).

## Why atomic commits pay off

- **Reviewability.** Small, focused commits are far easier for a reviewer to
  understand than a sprawling change touching many concerns at once.
- **Revertability.** Making commits logically separate also makes it easier to
  pull out or revert one of the changesets later if it turns out to be a mistake,
  without disturbing unrelated work.
- **Low cost.** The project snapshot at the tip of a branch is identical whether
  the work is one commit or five, as long as all the changes are added at some
  point. Splitting work into logical commits only helps reviewers — it doesn't
  change the final tree — so there is no downside to doing it well.

## Tools for keeping commits atomic

Real work is messy; you often end up with several unrelated changes in your
working tree at once. Git gives you tools to still commit them separately:

- **`git add --patch`** partially stages a file, letting you choose individual
  hunks, so unrelated changes that happen to live in the same file end up in
  separate commits. This is the [staging area](/oks/git-best-practices/fundamentals/staging-area.md)
  doing exactly what it was designed for.
- **`git rebase -i`** (interactive rebase) lets you squash work down to a single
  commit or rearrange work across commits before you submit it, so you can clean
  up an untidy sequence into an atomic one.
- **`git diff --check`** before committing identifies possible whitespace errors
  and lists them, so you can clean them up rather than baking them into the
  commit.

Atomic commits are also what make [trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md)
and small, frequent integration practical.

# Related

- [Conventional Commits](/oks/git-best-practices/commits/conventional-commits.md)
- [commit-message style](/oks/git-best-practices/commits/commit-message-style.md)
- [staging area](/oks/git-best-practices/fundamentals/staging-area.md)
- [interactive rebase](/oks/git-best-practices/history/interactive-rebase.md)

# Sources

- https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
