---
type: Commit Practice
title: Commit Message Style
description: The Git project's conventions for commit messages — a ~50-character imperative subject, a blank line, and a wrapped body explaining the why.
resource: https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
tags:
  - git
  - commits
  - style
timestamp: 2026-07-07T00:00:00Z
---

# Commit Message Style

A commit message is documentation that travels with the code forever. The Git
project's own conventions, followed across much of the open-source world,
produce messages that read well in `git log`, in emails, and in tools like
`git rebase`.

## The subject line

- Start with a **single summary line of no more than about 50 characters** that
  concisely describes the changeset.
- Write it in the **imperative mood** — "Fix bug", not "Fixed bug" or "Fixes
  bug". This matches the style Git itself uses for messages it generates, such as
  those from `git merge` and `git revert`. A useful test: the subject should
  complete the sentence "If applied, this commit will ___".

## The blank line

The subject line **must be followed by a blank line** before any detailed
explanation. This separation is not cosmetic: tools such as rebase get confused
if the summary and body run together, and many tools treat the first line as the
short description and the rest as the body based on that blank line.

## The body

- **Wrap the body at about 72 characters** so it displays well in terminals and
  tools that don't wrap for you.
- Explain the **motivation for the change** and contrast its implementation with
  the previous behavior — the *why*, not just the *what*. The diff already shows
  what changed; the body should capture what the diff cannot: why it was
  necessary and what alternatives were considered.
- Further paragraphs come after blank lines, and **bullet points** are
  acceptable — use a hyphen or asterisk followed by a single space, with blank
  lines between bullets.

## Relationship to other conventions

This style is the foundation that
[Conventional Commits](/oks/git-best-practices/commits/conventional-commits.md)
builds structure on top of, and it complements
[atomic commits](/oks/git-best-practices/commits/atomic-commits.md): a
single-purpose commit is far easier to summarize in 50 characters than a grab
bag of unrelated changes. The conventions are guidance, not a linter — adopt them
because they make history genuinely more useful, not as bureaucracy.

# Related

- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)
- [Conventional Commits](/oks/git-best-practices/commits/conventional-commits.md)

# Sources

- https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
