---
type: OKF Concept Index
title: Context
description: Managing what Claude Code knows in a session — precise instructions, a clean context window, persistent memory, and rich inline references.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - context
timestamp: 2026-07-07T00:00:00Z
---

# Context

Claude Code's biggest lever is what's in its context window: how precisely
you instruct it, how much irrelevant history has piled up, what persists
across sessions, and what you point it at directly. These concepts cover
managing that context effectively.

## Concepts

- [be specific in instructions](/oks/claude-best-practices/context/be-specific-in-instructions.md) — precise, concrete prompts need fewer corrections, and correcting early keeps a session from drifting.
- [managing the context window](/oks/claude-best-practices/context/managing-the-context-window.md) — why a focused context matters, resetting with `/clear`, and how compaction works.
- [claude.md as memory](/oks/claude-best-practices/context/claude-md-as-memory.md) — CLAUDE.md as auto-loaded, persistent instructions, viewed and tuned via `/memory`.
- [referencing files, urls, and images](/oks/claude-best-practices/context/referencing-files-urls-images.md) — pointing Claude at files, screenshots, diagrams, and URLs directly.
