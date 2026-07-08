---
type: OKF Concept Index
title: Safety
description: Controlling what Claude Code can do without asking, and containing the blast radius when you let it do more.
resource: https://code.claude.com/docs/en/permission-modes
tags:
  - claude-code
  - safety
timestamp: 2026-07-07T00:00:00Z
---

# Safety

Claude Code trades oversight for throughput along a spectrum: how often it
asks before acting, which specific tools and commands are pre-approved, and
how contained a session is if something goes wrong. These concepts cover
choosing a permission mode, tuning allow/deny rules, and isolating or
reviewing higher-autonomy runs.

## Concepts

- [permission modes](/oks/claude-best-practices/safety/permission-modes.md) — the `default`, `acceptEdits`, `plan`, and `bypassPermissions` modes, what each allows, and when to use which.
- [allowlists and settings](/oks/claude-best-practices/safety/allowlists-and-settings.md) — tuning allow/deny rules via `/permissions` and `settings.json`, and project vs. user settings.
- [sandboxing and review](/oks/claude-best-practices/safety/sandboxing-and-review.md) — isolating risky or auto-accepted runs and reviewing agent actions before trusting them.
