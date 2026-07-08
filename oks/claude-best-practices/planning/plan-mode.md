---
type: Claude Code Technique
title: Plan Mode
description: A read-only permission mode where Claude researches and proposes a plan without editing your source, so you can review changes before they touch disk.
resource: https://code.claude.com/docs/en/permission-modes
tags:
  - claude-code
  - planning
  - plan-mode
timestamp: 2026-07-07T00:00:00Z
---

# Plan Mode

Plan mode tells Claude to research and propose changes without making them.
Claude reads files, runs shell commands to explore, and writes a plan, but does
not edit your source. It is one of Claude Code's permission modes, and its whole
purpose is to separate exploration from execution so you can review the intended
changes before they touch disk.

## How to enter and approve

Enter plan mode by pressing `Shift+Tab` to cycle permission modes (the cycle runs
`default` → `acceptEdits` → `plan`), by prefixing a single prompt with `/plan`,
or by starting the CLI with `claude --permission-mode plan`. Permission prompts
still apply as they do in the default (Manual) mode.

When the plan is ready, Claude presents it and asks how to proceed. From that
prompt you can approve and start in auto mode, approve and accept edits, approve
and review each edit manually, or keep planning with feedback. Press `Ctrl+G` to
open the proposed plan in your default text editor and edit it directly before
Claude proceeds. Approving a plan exits plan mode and switches the session to the
permission mode the chosen option describes, so Claude starts editing.

## When to use it

Use plan mode when you want to review changes before they happen: exploring an
unfamiliar codebase, making risky changes, or modifying multiple files. The
recommended workflow is to explore and plan in plan mode, then switch out to let
Claude implement against its plan. Plan mode is useful but adds overhead — for
tasks where the scope is clear and the fix is small, like fixing a typo or
renaming a variable, ask Claude to do it directly. If you could describe the diff
in one sentence, skip the plan.

## Pairs with extended thinking

Because plan mode is where Claude reasons about an approach before committing to
it, it is the natural place to spend more reasoning. Raising the effort level or
adding `ultrathink` to a planning prompt gives Claude deeper reasoning for the
architectural decision, while the read-only mode guarantees no code changes until
you approve.

# Related

- [extended thinking](/oks/claude-best-practices/planning/extended-thinking.md)
- [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)

# Sources

- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/common-workflows
- https://code.claude.com/docs/en/best-practices
