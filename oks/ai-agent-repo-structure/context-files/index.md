---
type: OKF Concept Index
title: Context Files
description: The instruction files an agent reads at startup — AGENTS.md and CLAUDE.md — how they load, and how they resolve across scopes.
resource: https://docs.claude.com/en/docs/claude-code/memory
tags:
  - ai-agents
  - context-files
  - agents-md
  - claude-md
timestamp: 2026-07-07T00:00:00Z
---

# Context Files

Context files are the plain-Markdown instructions an agent reads to learn how a
project works. These concepts cover the two dominant formats, how agents load
context incrementally rather than all at once, and how instructions at different
scopes combine.

## Concepts

- [AGENTS.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md) — the two context-file conventions and how to make both tools read the same instructions.
- [progressive disclosure](/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md) — loading lightweight identifiers up front and pulling detail into context only when needed.
- [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md) — the four scopes context files live at and how they concatenate rather than override.
