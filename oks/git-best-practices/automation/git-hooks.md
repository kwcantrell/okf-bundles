---
type: Automation Practice
title: Git Hooks
description: Scripts Git runs at defined points in its operations — client-side hooks for local events and server-side hooks that can accept or reject a push.
resource: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
tags:
  - git
  - automation
  - hooks
timestamp: 2026-07-07T00:00:00Z
---

# Git Hooks

Git hooks are scripts Git executes automatically at defined points in its
operations, letting you enforce policy and trigger side effects without manual
steps.

## How hooks are enabled

Hooks live in the `hooks` subdirectory of the Git directory — by default
`.git/hooks`, or wherever `core.hooksPath` points. A hook is enabled by placing
an appropriately named, **executable** file there. Git ships sample scripts with
a `.sample` extension; you activate one by renaming it to remove that extension.
Hooks can be written in **any scripting language** that can be executed as a
program — shell, Ruby, Python, Perl, and so on — not just shell.

## Client-side hooks

Client-side hooks are triggered by local operations like committing, merging, and
pushing. Common ones include `pre-commit`, `commit-msg`, `post-commit`, and
`pre-push`. The `pre-push` hook runs during `git push`, after the remote refs
have been updated but before any objects are transferred, and can **halt the
push**.

A crucial limitation: **client-side hooks are not copied when a repository is
cloned.** Because hooks can live wherever `core.hooksPath` points, teams work
around this by committing a hooks directory to the repository and having each
contributor point Git at it — see
[pre-commit](/oks/git-best-practices/automation/pre-commit.md) for how that
looks in practice.

## Server-side hooks

Server-side hooks run on the remote when a push is received:

- **`pre-receive`** runs once and can **reject the entire push**.
- **`update`** runs once per branch and can reject just that reference.
- **`post-receive`** runs after the push completes and is often used to trigger
  notifications or [CI](/oks/git-best-practices/automation/ci-integration.md).

Because they live on the server, these hooks enforce policy that individual
developers cannot bypass — complementing branch-level rules like
[branch protection](/oks/git-best-practices/branching/branch-protection.md).

# Related

- [pre-commit](/oks/git-best-practices/automation/pre-commit.md)
- [ci integration](/oks/git-best-practices/automation/ci-integration.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)
- [secret management](/oks/git-best-practices/security/secret-management.md)

# Sources

- https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
- https://git-scm.com/docs/githooks
