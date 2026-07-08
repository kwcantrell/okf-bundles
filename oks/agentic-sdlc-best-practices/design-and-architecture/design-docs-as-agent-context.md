---
type: Agentic SDLC Practice
title: Design Docs As Agent Context
description: When agents scaffold and extend a system from a design document, that document stops being ceremony and becomes durable context — so it earns its keep by stating constraints, interfaces, and non-goals explicitly enough that the agent builds the right thing without you re-explaining it each session.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - design-and-architecture
timestamp: 2026-07-07T00:00:00Z
---

# Design Docs As Agent Context

Design documents used to have a reputation as ceremony — written to satisfy a
process, skimmed once, then left to rot while the real design lived in the
code and in people's heads. In an agentic workflow that changes, because the
document becomes something an agent reads and acts on. "Given a clear
architecture document, AI agents can scaffold entire applications, generate
consistent patterns across modules, and ensure that new code conforms to
established conventions" (Osmani, Saboo, and Kartakis, *The New SDLC With Vibe
Coding*, May 2026). The doc is no longer a record of a decision already
executed; it's the input the agent builds from. That reframes the whole point
of writing one — you're not documenting for a reviewer, you're supplying
context to a builder.

## Write it to be consumed, not to be filed

A design doc written for an agent looks different from one written to close a
ticket. The things a human teammate would fill in from experience have to be on
the page, because the agent implements what's written rather than what you
meant:

- **Constraints** — the boundaries the implementation must respect (this store
  is the source of truth; this call path must stay synchronous; this table is
  append-only). Left unstated, they get violated the first time the agent finds
  a simpler path.
- **Interfaces** — the shapes at the seams between modules: the schema, the
  contract, the expected inputs and outputs. These are what let the agent
  generate consistent patterns across modules instead of inventing a new one
  each time.
- **Non-goals** — what this design deliberately does *not* do. An agent will
  helpfully build past the boundary you had in mind unless the boundary is
  written down; naming the non-goals is how you stop scope from quietly
  expanding.

## Docs as durable context, not ceremony

The payoff is that the document keeps working after it's written. Because the
agent reads it fresh each session, a good design doc means you don't
re-explain the same constraints and interfaces every time work resumes — the
knowledge lives in the repo rather than in the last conversation, which is the
same reason to
[capture memory and knowledge](/oks/agentic-sdlc-best-practices/context-engineering/memory-and-knowledge-capture.md)
durably rather than leave it in a session that will be cleared. This is docs as
context engineering: the design doc is one of the highest-leverage pieces of
[documentation written for agents](/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md)
to consume, and it earns its place by being read on every build rather than
filed and forgotten.

# Related

- [memory and knowledge capture](/oks/agentic-sdlc-best-practices/context-engineering/memory-and-knowledge-capture.md)
- [docs for agents](/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
