---
type: Claude Code Workflow
title: Explore, Plan, Implement, Commit
description: The recommended four-phase loop for non-trivial changes — read and understand first, plan before touching code, implement against the plan, then commit.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - workflows
  - plan-mode
timestamp: 2026-07-07T00:00:00Z
---

# Explore, Plan, Implement, Commit

Letting Claude jump straight to coding can produce a solution to the wrong
problem. The documented fix is to separate research and planning from
execution, using [plan mode](/oks/claude-best-practices/planning/plan-mode.md)
to keep Claude from editing files while it explores and reasons about an
approach. The recommended workflow has four phases.

## The four phases

**Explore.** Enter plan mode and ask Claude to read the relevant files and
answer questions without making changes — for example, "read /src/auth and
understand how we handle sessions and login. also look at how we manage
environment variables for secrets." Nothing is edited in this phase.

**Plan.** Ask Claude to turn that understanding into a concrete implementation
plan: "I want to add Google OAuth. What files need to change? What's the
session flow? Create a plan." The plan can be opened in your default text
editor (`Ctrl+G`) and edited directly before Claude proceeds — see
[spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)
for turning this into a written, reviewable spec for larger features.

**Implement.** Switch out of plan mode and let Claude write the code,
verifying its own work against the plan as it goes — for example asking it to
write tests for a new handler and run the suite, fixing failures itself. See
[test-driven development](/oks/claude-best-practices/workflows/test-driven-development.md)
for structuring this phase around tests written before the implementation.

**Commit.** Ask Claude to commit with a descriptive message and open a pull
request once the implementation is verified.

## When to skip planning

Plan mode adds overhead, so it isn't the right choice for every change. It pays
off when the approach is uncertain, the change touches multiple files, or the
codebase is unfamiliar. If the resulting diff could be described in one
sentence — fixing a typo, adding a log line, renaming a variable — skip the
plan and ask Claude to do it directly.

# Related

- [test driven development](/oks/claude-best-practices/workflows/test-driven-development.md)
- [plan mode](/oks/claude-best-practices/planning/plan-mode.md)
- [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)

# Sources

- https://code.claude.com/docs/en/best-practices
