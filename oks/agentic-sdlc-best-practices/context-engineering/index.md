---
type: OKF Concept Index
title: Context Engineering
description: Curating everything the model sees — not just the prompt. The shift from prompt engineering to context engineering, treating the window as a finite budget, managing long-horizon tasks with compaction and isolation, and persisting knowledge across sessions.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - agentic-sdlc
  - context-engineering
timestamp: 2026-07-07T00:00:00Z
---

# Context Engineering

Once you're running an agent rather than typing single turns, the prompt is a
small fraction of what the model conditions on. The real lever is *everything the
model sees* — instructions, knowledge, tools, and running history — and curating
that is a distinct discipline from prompt-writing. These concepts move from the
reframing itself, to the moment-to-moment act of curation, to keeping long tasks
inside their budget, to what should persist across sessions.

## Concepts

- [context engineering over prompt engineering](/oks/agentic-sdlc-best-practices/context-engineering/context-engineering-over-prompt-engineering.md) — why output quality tracks context quality more than prompt cleverness, and the shift from tricking the model to briefing a teammate.
- [curating the context window](/oks/agentic-sdlc-best-practices/context-engineering/curating-the-context-window.md) — the window as a finite budget with a signal-to-noise problem: include the smallest high-signal set, retrieve the rest just-in-time.
- [compaction and long-horizon context](/oks/agentic-sdlc-best-practices/context-engineering/compaction-and-long-horizon-context.md) — carrying state across tasks that outgrow a single window, via summarization, handoffs, and sub-agent isolation.
- [memory and knowledge capture](/oks/agentic-sdlc-best-practices/context-engineering/memory-and-knowledge-capture.md) — the discipline of deciding what to persist across sessions and feed back into repo context.
