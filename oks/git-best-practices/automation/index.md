---
type: OKF Concept Index
title: Automation
description: Automating checks and workflows around Git — client- and server-side hooks, CI integration with GitHub Actions, and the pre-commit framework.
resource: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
tags:
  - git
  - automation
timestamp: 2026-07-07T00:00:00Z
---

# Automation

Much of Git's value at scale comes from automating quality gates so humans do not
have to remember them. These concepts cover the hook mechanism Git provides,
continuous integration triggered from your repository, and the pre-commit
framework that makes local hooks portable across a team.

## Concepts

- [git hooks](/oks/git-best-practices/automation/git-hooks.md) — scripts Git runs at defined points, client-side and server-side.
- [ci integration](/oks/git-best-practices/automation/ci-integration.md) — running builds and tests automatically with GitHub Actions workflows.
- [pre-commit](/oks/git-best-practices/automation/pre-commit.md) — the pre-commit hook and the framework for sharing local checks.
