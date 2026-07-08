---
type: OKF Concept Index
title: Design And Architecture
description: The most human-centric phase of the lifecycle, because its trade-offs turn on business context and strategy the model can't fully grasp. This area covers using the agent as a design partner while the human owns the decision, writing design docs the agent will consume downstream, and shaping architecture so a codebase stays legible to an agent working through a limited context window.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - design-and-architecture
timestamp: 2026-07-07T00:00:00Z
---

# Design And Architecture

Architecture is the phase that moves least toward the agent, because its choices
are trade-offs that depend on business context, organizational constraints, and
long-term strategy the model can't fully see. So the human keeps the decision —
but the work around it changes shape. The agent becomes a partner for exploring
options and stress-testing them, the design document becomes context the agent
builds from rather than ceremony, and the structure of the codebase itself
becomes something to design *for* an agent that reads it through a limited
context window. These concepts move from making the decision, to writing it
down for the agent, to shaping the code so the agent can work in it.

## Concepts

- [architecture decisions with ai](/oks/agentic-sdlc-best-practices/design-and-architecture/architecture-decisions-with-ai.md) — the agent explores alternatives and stress-tests trade-offs; the human owns the decision and its rationale.
- [design docs as agent context](/oks/agentic-sdlc-best-practices/design-and-architecture/design-docs-as-agent-context.md) — writing constraints, interfaces, and non-goals explicitly, so the document is durable context the agent consumes rather than ceremony.
- [designing for agent legibility](/oks/agentic-sdlc-best-practices/design-and-architecture/designing-for-agent-legibility.md) — modularity, clear boundaries, small focused files, and consistent conventions that make a codebase an agent can work in reliably.
