---
type: Collaboration Practice
title: CODEOWNERS
description: A CODEOWNERS file assigns responsibility for parts of a repository so the right people or teams are automatically requested to review changes.
resource: https://docs.github.com/articles/about-code-owners
tags:
  - git
  - github
  - collaboration
  - code-review
timestamp: 2026-07-07T00:00:00Z
---

# CODEOWNERS

A `CODEOWNERS` file defines the individuals or teams responsible for code in a
repository. Its payoff is automation of review routing: code owners are
automatically requested for review when a
[pull request](/oks/git-best-practices/collaboration/pull-requests.md) modifies
code they own, so changes reach the people who know that code best without anyone
manually assigning reviewers.

## Where the file goes

Create the file in one of three locations: the `.github/`, root, or `docs/`
directory of the repository. If files exist in more than one location, GitHub
searches in that order and uses the **first** one it finds.

## Syntax and matching rules

CODEOWNERS syntax follows most of the same pattern rules as `.gitignore` files,
with some important exceptions:

- Escaping `#` with a backslash does **not** work.
- `!` negation is **not** supported.
- Character ranges with `[ ]` do **not** function.
- Patterns are **case-sensitive**.

**Order is significant:** the *last* matching pattern in the file takes the most
precedence over earlier matching patterns. Arrange from general at the top to
specific at the bottom so the most specific owner wins.

## Permissions and limits

- The people or teams listed as code owners **must have write permissions** for
  the repository. For a team to be a code owner, the team itself must have write
  permissions — even if all of its individual members already do.
- A CODEOWNERS file **must be under 3 MB**. A file over this limit will not be
  loaded, meaning code-owner information won't be shown and owners won't be
  requested to review changes.

## Making ownership enforceable

Defining owners requests them automatically, but does not by itself block a
merge. People with admin or owner permissions can additionally **require that
pull requests be approved by code owners** before they can be merged — combine
CODEOWNERS with
[branch protection](/oks/git-best-practices/branching/branch-protection.md) to
turn ownership into a genuine review gate. Note that
[draft pull requests](/oks/git-best-practices/collaboration/draft-prs.md) do not
auto-request code owners until they are marked ready for review.

# Related

- [pull requests](/oks/git-best-practices/collaboration/pull-requests.md)
- [code review](/oks/git-best-practices/collaboration/code-review.md)
- [draft pull requests](/oks/git-best-practices/collaboration/draft-prs.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)

# Sources

- https://docs.github.com/articles/about-code-owners
