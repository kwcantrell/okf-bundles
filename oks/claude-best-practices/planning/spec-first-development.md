---
type: Claude Code Technique
title: Spec-First Development
description: Have Claude produce and refine a written plan or spec before implementing, so you catch a wrong approach on paper instead of in a wrong diff.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - planning
timestamp: 2026-07-07T00:00:00Z
---

# Spec-First Development

Letting Claude jump straight to coding can produce code that solves the wrong
problem. The fix is to separate research and planning from implementation:
explore first, then plan, then code. You review the plan while it is still cheap
to change — on paper — rather than discovering the wrong approach in a finished
diff.

## Produce a plan, then review it

Ask Claude to create a detailed implementation plan before it writes any code:
which files need to change, what the flow is, and what the steps are. Review that
plan and refine it through conversation before approving. For larger features,
have Claude interview you first: start with a minimal prompt and ask Claude to
interview you in detail about technical implementation, UI/UX, edge cases, and
tradeoffs, then write a complete spec to a file such as `SPEC.md`. Once the spec
is complete, you can start a fresh session to execute it, so the implementation
session has clean context focused entirely on the work and a written spec to
reference.

## What makes a spec worth writing

The most useful specs are self-contained: they name the files and interfaces
involved, state what is out of scope, and end with an end-to-end verification
step that proves the feature works. Time spent making the spec precise pays off
more than time spent watching the implementation. This is the "explore, plan,
code, commit" discipline — research and agree on the approach before writing the
code, so each later phase builds on a reviewed foundation instead of a guess.

# Related

- [plan mode](/oks/claude-best-practices/planning/plan-mode.md)
- [extended thinking](/oks/claude-best-practices/planning/extended-thinking.md)

# Sources

- https://code.claude.com/docs/en/best-practices
