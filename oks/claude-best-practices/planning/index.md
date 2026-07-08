---
type: OKF Concept Index
title: Planning
description: Getting Claude Code to think and plan before it writes code — deeper reasoning, a read-only planning mode, and reviewing a spec before implementation.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - planning
timestamp: 2026-07-07T00:00:00Z
---

# Planning

The most reliable way to get good code out of Claude Code is to separate thinking
from doing: give it room to reason, let it propose an approach without touching
your files, and review that approach before implementation begins. These concepts
cover the planning tools that make that separation practical.

## Concepts

- [extended thinking](/oks/claude-best-practices/planning/extended-thinking.md) — the reasoning Claude emits before answering, controlled mainly by effort level, with an `ultrathink` keyword for one-off deeper reasoning.
- [plan mode](/oks/claude-best-practices/planning/plan-mode.md) — a read-only permission mode that researches and proposes a plan without editing your source, so you review changes before they touch disk.
- [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md) — have Claude produce and refine a written plan or spec first, then implement against it.
