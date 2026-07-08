---
type: Agentic SDLC Practice
title: Architecture Decisions With AI
description: Architecture stays the most human-centric phase because its trade-offs turn on business context and long-term strategy the model can't fully see — so the agent works as a design partner that explores alternatives and stress-tests trade-offs, while the human owns the decision and its rationale.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - design-and-architecture
timestamp: 2026-07-07T00:00:00Z
---

# Architecture Decisions With AI

Of all the phases in the software lifecycle, architecture is the one that moves
least toward the agent. The reason is the nature of the work: architectural
choices are trade-offs — consistency versus availability, complexity versus
flexibility, build versus buy — and those trade-offs "depend on business
context, organisational constraints, and long-term strategic considerations that
AI cannot fully grasp" (Osmani, Saboo, and Kartakis, *The New SDLC With Vibe
Coding*, May 2026). A model can enumerate the options and their known
consequences, but it can't weigh them against a roadmap it can't see, a team's
appetite for operational risk, or a commercial constraint that never made it
into any document. That judgment is what the human keeps.

## The agent as a design partner

What the agent is good at here is breadth and speed, not the final call. Point
it at a decision and it will surface alternatives you hadn't listed, name the
trade-offs each one carries, and argue the case for and against — a tireless
partner for exploring the space before you commit. Used well it widens the set
of options under consideration and pressure-tests the one you're leaning toward,
which is exactly the kind of thinking that's cheap to get wrong on paper and
expensive to get wrong in a running system. The move is to treat its output as
input to your reasoning, not as the decision itself.

## The human owns the decision and its rationale

Once the decision is made, the developer's job shifts from writing the
structure to recording it. In an agentic workflow the boilerplate that
implements an architecture is nearly free — "given a clear architecture
document, AI agents can scaffold entire applications, generate consistent
patterns across modules, and ensure that new code conforms to established
conventions." So "the developer's role shifts from writing boilerplate to
making and documenting the structural decisions that boilerplate implements."
The decision and the *why* behind it are the durable artifact; the code that
expresses it is downstream. Capturing that rationale is what lets a later
agent — or a later human — extend the system without relitigating choices it
can't see the reasons for. That written record is itself the agent's context
for everything built on top of the decision, which is why it deserves the same
care as the decision.

# Related

- [specs as the primary artifact](/oks/agentic-sdlc-best-practices/requirements-and-planning/specs-as-the-primary-artifact.md)
- [design docs as agent context](/oks/agentic-sdlc-best-practices/design-and-architecture/design-docs-as-agent-context.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
