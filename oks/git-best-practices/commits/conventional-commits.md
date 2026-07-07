---
type: Commit Practice
title: Conventional Commits
description: A lightweight convention that structures commit messages as type(scope):description, making history machine-readable for changelogs and versioning.
resource: https://www.conventionalcommits.org/en/v1.0.0/
tags:
  - git
  - commits
  - conventional-commits
  - automation
timestamp: 2026-07-07T00:00:00Z
---

# Conventional Commits

Conventional Commits is a specification for adding a lightweight, structured
format to commit messages. By encoding the *kind* of change into the subject
line, it makes history readable by tooling — changelog generators and automated
version bumping — as well as by humans. It layers a required structure on top of
ordinary [commit-message style](/oks/git-best-practices/commits/commit-message-style.md).

## The format

A Conventional Commit message is:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The rules that make it parseable:

- Commits **MUST** be prefixed with a **type** — a noun such as `feat` or `fix` —
  followed by an optional scope, an optional `!`, and a **required terminal colon
  and space**.
- The type **`feat`** MUST be used when a commit adds a new feature; the type
  **`fix`** MUST be used when a commit represents a bug fix. Other types (e.g.
  `docs`, `refactor`, `test`, `chore`) are permitted by convention.
- A **scope**, when present, MUST be a noun describing a section of the codebase,
  surrounded by parentheses — for example `fix(parser):`.
- The **description** MUST immediately follow the colon and space. If a body is
  present, it MUST begin one blank line after the description — the same
  blank-line rule that ordinary commit messages follow.

## Signaling breaking changes

Breaking changes MUST be indicated in one of two ways:

- a `!` immediately before the colon in the type/scope prefix
  (e.g. `feat!:` or `feat(api)!:`), or
- a footer whose token is the uppercase text `BREAKING CHANGE`, followed by a
  colon, a space, and a description.

## Case sensitivity

Implementors MUST NOT treat types and scopes as case-sensitive — with one
exception: `BREAKING CHANGE` MUST be uppercase, and `BREAKING-CHANGE` MUST be
treated as synonymous with `BREAKING CHANGE` as a footer token.

## Trade-offs

The payoff is automation: because the type and breaking-change signal are
machine-readable, tools can derive semantic-version bumps and generate
changelogs without human curation. The cost is a small amount of discipline on
every commit, which teams usually enforce with a commit-message linter. It works
best combined with [atomic commits](/oks/git-best-practices/commits/atomic-commits.md),
since a single-purpose commit maps cleanly to a single type.

# Related

- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)
- [commit-message style](/oks/git-best-practices/commits/commit-message-style.md)

# Sources

- https://www.conventionalcommits.org/en/v1.0.0/
