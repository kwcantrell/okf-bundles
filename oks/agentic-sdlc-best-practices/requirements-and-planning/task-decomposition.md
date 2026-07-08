---
type: Agentic SDLC Practice
title: Task Decomposition
description: Breaking work into agent-sized, independently verifiable units is the orchestrator's core skill — the decomposition determines whether an agent can finish a piece cleanly and whether you can check that it did.
resource: https://www.anthropic.com/engineering/building-effective-agents
tags:
  - agentic-sdlc
  - requirements-and-planning
timestamp: 2026-07-07T00:00:00Z
---

# Task Decomposition

A spec tells the agent what to build; decomposition decides how to cut the work
into pieces an agent can actually finish. This is not a formality — it is the
skill the May 2026 SDLC paper names as central to working at the orchestrator
level. When you stop watching code appear line by line and instead "define goals,
assign them to agents, and review results," success depends on how well you split
the goal. The paper lists decomposition alongside specification, evaluation, and
system design as one of the skills orchestrator mode "demands" in place of "deep
expertise in syntax and language idioms."

## Agent-sized, independently verifiable units

A good unit has two properties. It is *agent-sized* — small enough to fit an
agent's working context and finish in one focused pass, rather than sprawling
until the context window fills with half-finished threads. And it is
*independently verifiable* — it has a check you can run to confirm it is done
without inspecting everything around it. The second property is the one that is
easy to skip and expensive to omit: if a unit's correctness can only be judged by
reading the whole system, you have not really decomposed the work, you have only
chopped it up. The agentic pattern for this is dynamic rather than fixed. In
Anthropic's orchestrator-workers pattern, "a central LLM dynamically breaks down
tasks, delegates them to worker LLMs, and synthesizes their results" — a shape
suited to work whose subtasks can't all be predicted in advance.

## Decompose only as far as the work needs

Decomposition is a tool for managing complexity, not a goal in itself, and it can
be overdone. Anthropic's standing advice is to "find the simplest solution
possible, and only increas[e] complexity when needed" — the same restraint
applies to how finely you slice a task. Splitting work into more units than the
problem warrants adds coordination overhead and hand-off seams without buying
verifiability. The right granularity is the coarsest one where each piece is
still small enough to build and has its own check.

Who owns decomposition follows from this. Cutting the work and routing the pieces
is the [orchestrator's job](/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md);
the conductor, working in real time with an agent, decomposes implicitly and at a
finer grain as they go. Once the units are cut, each one becomes a small,
verifiable increment that the implementation phase builds and checks in turn.

# Related

- [specs as the primary artifact](/oks/agentic-sdlc-best-practices/requirements-and-planning/specs-as-the-primary-artifact.md)
- [conductor and orchestrator roles](/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md)
- [small verifiable increments](/oks/agentic-sdlc-best-practices/implementation/small-verifiable-increments.md)

# Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
