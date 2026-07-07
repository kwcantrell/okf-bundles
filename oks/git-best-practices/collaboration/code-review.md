---
type: Collaboration Practice
title: Code Review
description: How pull request reviews work on GitHub — commenting, suggesting line changes, and submitting a Comment, Approve, or Request changes verdict.
resource: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
tags:
  - git
  - github
  - collaboration
  - code-review
timestamp: 2026-07-07T00:00:00Z
---

# Code Review

Pull request reviews are one of the primary ways people collaborate on GitHub.
A review lets a teammate comment on changes, suggest improvements, and approve or
request changes before code is merged. Done well, review spreads knowledge and
catches problems early; done as a rubber stamp, it adds delay without value — so
it's worth understanding the mechanics and using them deliberately.

## Who can review

After a [pull request](/oks/git-best-practices/collaboration/pull-requests.md) is
opened, **anyone with read access** to the repository can review and comment on
the changes it proposes. Reviewers can also suggest specific changes to lines of
code, which the pull request author can then apply directly from the pull
request — turning a suggestion into a committed change with one click.

## The three review verdicts

A review is submitted as one of three types:

- **Comment** — general feedback without explicit approval or a change request.
- **Approve** — feedback plus approval to merge.
- **Request changes** — feedback that must be addressed before the pull request
  can be merged.

## Making review enforceable

Two features turn review from a courtesy into a gate:

- **Required approvals.** Repository administrators can require approvals before
  pull requests are merged, which helps ensure code quality and prevent
  accidental merges. This is configured through
  [branch protection](/oks/git-best-practices/branching/branch-protection.md).
- **Automatic reviewer requests.** When
  [code owners](/oks/git-best-practices/collaboration/codeowners.md) are defined
  for the code being changed, they are automatically requested as reviewers on any
  pull request that modifies that code, so the right people see the right changes
  without manual routing.

## Practical guidance

Keep changes small so reviews stay fast and thorough — this is one reason
[trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md)
favors immediate, incremental review. Review the *why* as well as the *what*,
prefer concrete suggestions over vague objections, and reserve "Request changes"
for issues that genuinely must block the merge.

# Related

- [pull requests](/oks/git-best-practices/collaboration/pull-requests.md)
- [CODEOWNERS](/oks/git-best-practices/collaboration/codeowners.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)

# Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
