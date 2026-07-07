---
type: OKF Concept Index
title: Commit Practices
description: How to shape and describe commits — keeping them atomic, structuring messages, adopting Conventional Commits, and signing your work.
resource: https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
tags:
  - git
  - commits
timestamp: 2026-07-07T00:00:00Z
---

# Commit Practices

A commit is the unit of change in Git, and good commits are the raw material of
a readable history. These concepts cover both the *shape* of a commit (what
belongs in it) and its *description* (how to write and, optionally, sign it).

## Concepts

- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md) — make each commit one logically separate changeset.
- [Conventional Commits](/oks/git-best-practices/commits/conventional-commits.md) — a structured `type(scope): description` message format.
- [commit-message style](/oks/git-best-practices/commits/commit-message-style.md) — subject line, blank line, and wrapped body conventions.
- [signing commits](/oks/git-best-practices/commits/signing-commits.md) — cryptographically verifying authorship with GPG, SSH, or S/MIME.
