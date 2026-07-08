---
type: Agentic SDLC Practice
title: Curating The Context Window
description: The context window is a finite budget with a signal-to-noise problem — include the smallest set of high-signal tokens, and pull the rest in just-in-time rather than preloading everything.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - agentic-sdlc
  - context-engineering
timestamp: 2026-07-07T00:00:00Z
---

# Curating The Context Window

If context engineering is the discipline, curation is the daily act: for every
step, deciding what the model should and should not see. The window is finite,
and it is not free — the SDLC paper notes that in the token economy "passing an
entire 100,000-token repository into every prompt is financially unviable at
scale." But cost is only half the reason to be selective. The other half is
signal: more context is not better context.

## Context is a budget, and signal beats volume

Treat the window as a budget you are spending, not a bin you are filling.
LangChain's analogy is that "the LLM is like the CPU and its context window is
like the RAM, serving as the model's working memory" — a scarce resource that
has to hold exactly the right working set. Anthropic's rule for what to put in it
is to find "the smallest possible set of high-signal tokens that maximize the
likelihood of some desired outcome." Every low-signal token you include — a stale
file, a verbose tool dump, an irrelevant tangent — competes for the model's
attention with the tokens that matter. Inclusion is a decision; so is exclusion.

## Just-in-time retrieval over preloading

The way to keep the working set small without losing reach is to load on demand.
Anthropic describes a "just in time" approach where agents "maintain lightweight
identifiers ... and use these references to dynamically load data into context at
runtime using tools" — keeping a file path or an ID in context, and only pulling
the actual bytes in when a tool needs them. Progressive disclosure is the same
idea applied to instructions and reference material: surface lightweight metadata
first, load the full detail only when a task matches. That mechanism is covered
in [progressive disclosure](/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md),
so it isn't restated here — the point for curation is that just-in-time loading
lets an agent stay reachable across a large codebase while its live window stays
lean.

## When the window still fills

Even well-curated sessions eventually approach the limit on long tasks, and the
harness-level knobs for staying focused — resetting between tasks, compaction,
delegating research to a subagent — live in
[managing the context window](/oks/claude-best-practices/context/managing-the-context-window.md).
The strategy for *long-horizon* work, where a single session outgrows the window
entirely, is the subject of the next concept.

# Related

- [progressive disclosure](/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md)
- [managing the context window](/oks/claude-best-practices/context/managing-the-context-window.md)
- [compaction and long-horizon context](/oks/agentic-sdlc-best-practices/context-engineering/compaction-and-long-horizon-context.md)

# Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://www.langchain.com/blog/context-engineering-for-agents
