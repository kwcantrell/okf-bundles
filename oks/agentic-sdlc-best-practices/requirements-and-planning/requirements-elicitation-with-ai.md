---
type: Agentic SDLC Practice
title: Requirements Elicitation With AI
description: Agents are useful before any code is written — drafting user stories, surfacing edge cases and unstated assumptions, and turning a rough brief into a sharper spec — but the human still owns acceptance of what "correct" means.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - requirements-and-planning
timestamp: 2026-07-07T00:00:00Z
---

# Requirements Elicitation With AI

The most valuable place to point an agent is often *before* implementation, at the
requirements themselves. The May 2026 SDLC paper describes modern AI tools as able
to "participate directly in requirements refinement: generating user stories from
product briefs, identifying edge cases that humans miss, producing API schemas from
natural-language descriptions, and generating interactive prototypes from
specification documents." Used this way, the agent is not building the thing yet —
it is helping you figure out what the thing should be, and doing it faster than a
round of meetings would.

## Interrogating the brief, not just filling it in

The leverage comes from using the agent to *pressure-test* a requirement rather
than to rubber-stamp it. Ask it to enumerate the edge cases, name the unstated
assumptions, draft the acceptance criteria, and produce a throwaway prototype that
makes a vague idea concrete. The paper notes that agentic environments let you go
"from a description to a working prototype in minutes, collapsing the
requirements-to-prototype feedback loop to near zero" — which turns "would this
even work?" from a planning debate into a two-minute experiment. Surfacing the
edge cases a human would miss is exactly the kind of ambiguity that, left in the
spec, later gets implemented literally and wrong.

This is also where genuinely agentic reasoning earns its place. OpenAI's guidance
is to "validate that your use case can meet [agentic] criteria clearly. Otherwise,
a deterministic solution may suffice" — a check worth running during elicitation,
because the requirements phase is the cheapest moment to discover that the problem
does not need an agent at all.

## The human owns acceptance

An agent can draft requirements, but it cannot decide what "correct" means for a
business. That judgment stays with the human. The elicitation loop is a
conversation in which the model proposes user stories, edge cases, and criteria,
and the person accepts, rejects, or reshapes them against context the model does
not have — priorities, constraints, and what actually matters to users. The output
of the loop is a sharper spec that the human has signed off on, which is what makes
it safe to treat that spec as the artifact the agent then builds from.

# Related

- [specs as the primary artifact](/oks/agentic-sdlc-best-practices/requirements-and-planning/specs-as-the-primary-artifact.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
