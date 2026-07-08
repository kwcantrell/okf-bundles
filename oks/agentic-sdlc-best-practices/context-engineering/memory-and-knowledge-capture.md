---
type: Agentic SDLC Practice
title: Memory And Knowledge Capture
description: The discipline of deciding what to persist across sessions — decisions, conventions, and lessons — and feeding it back into repo context so the next session starts informed rather than blank.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - agentic-sdlc
  - context-engineering
timestamp: 2026-07-07T00:00:00Z
---

# Memory And Knowledge Capture

Curation and compaction manage context *within* a task. Memory is about what
survives *between* tasks. Every session an agent runs, it learns something —
which convention the team follows, why a design went one way, what mistake to
never repeat — and by default all of it evaporates when the window closes. The
discipline here is deciding what of that is worth persisting, and writing it back
into the repo's context so the next session starts informed instead of blank.
This concept is about that judgment, not the file-specific mechanics of any one
tool.

## What is worth persisting

Not everything an agent encounters deserves to become durable memory — that would
just recreate the signal-to-noise problem in a slower medium. Persist the things
a new teammate would need and could not re-derive cheaply: architectural
decisions and the reasoning behind them, project conventions and hard rules, and
lessons from failures. The SDLC paper's onboarding test applies directly — encode
"what would a new team member need to know to contribute effectively." The paper's
"where to start" advice models the growth pattern: begin small, then "add a rule
every time the agent does something it should not do again." Memory accretes from
real mistakes, not from a big upfront brain-dump.

## Feeding it back into context

Captured knowledge only pays off if it re-enters the window on future runs. The
paper's own taxonomy lists "Memory" as one of the six kinds of context a
developer must supply, and treats rule files as the static context that is "always
loaded." So the loop is: capture the durable lesson, write it where the agent will
read it, and let it condition the next session. Two established homes for this
knowledge sit in adjacent bundles —
[claude.md as memory](/oks/claude-best-practices/context/claude-md-as-memory.md)
for the always-loaded rules and conventions, and
[docs for agents](/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md) for
the deeper reference material an agent pulls in on demand. The point common to
both, and the reason this belongs in context engineering, is that memory is just
[context curation](/oks/agentic-sdlc-best-practices/context-engineering/curating-the-context-window.md)
extended across time: you are still choosing the smallest set of high-signal
tokens — only now the choice is about what to keep, not just what to load.

# Related

- [claude.md as memory](/oks/claude-best-practices/context/claude-md-as-memory.md)
- [docs for agents](/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md)
- [curating the context window](/oks/agentic-sdlc-best-practices/context-engineering/curating-the-context-window.md)

# Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
