---
type: Agentic SDLC Practice
title: Workflows Vs Agents
description: Not every problem needs an autonomous agent. When the shape of the work is known, a predefined workflow beats agency — deterministic orchestration for the predictable, autonomy only where the path can't be known in advance.
resource: https://www.anthropic.com/engineering/building-effective-agents
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# Workflows Vs Agents

A harness can run a fixed script or hand the model the wheel, and choosing between them is
one of the most consequential [harness](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
decisions. Anthropic draws the line precisely: "workflows are systems where LLMs and tools
are orchestrated through predefined code paths," whereas agents "are systems where LLMs
dynamically direct their own processes"
([Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)).
The difference is who decides the sequence — your code, or the model.

## When a workflow wins

If the shape of the work is known in advance, a predefined path is more reliable, cheaper,
and easier to debug than an autonomous loop. OpenAI is explicit that agency is for the cases
deterministic code can't handle: agents "are uniquely suited to workflows where traditional
deterministic and rule-based approaches fall short"
([A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 5) — which is also a statement that where those approaches *do* hold, you should use them.
OpenAI even suggests validating the need before building: "before committing to building an
agent, validate that your use case can meet these criteria clearly. Otherwise, a
deterministic solution may suffice"
([building agents guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 6).

## When agency earns its cost

Autonomy pays off when the subtasks can't be enumerated up front. Anthropic's
orchestrator-workers pattern fits exactly there: "a central LLM dynamically breaks down
tasks, delegates them to worker LLMs, and synthesizes their results"
([Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)) —
useful precisely because the decomposition isn't known in advance. This is the machinery
behind the [conductor and orchestrator roles](/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md):
open-ended, judgment-heavy work is where the model directing its own process beats a
hardcoded path.

## Start simple, add agency only when needed

Both sources converge on the same discipline: don't reach for autonomy by default. Anthropic
recommends "finding the simplest solution possible, and only increasing complexity when
needed"
([Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)).
OpenAI advises starting with one agent and growing: "while it's tempting to immediately build
a fully autonomous agent with complex architecture, customers typically achieve greater
success with an incremental approach"
([building agents guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 13). Every degree of agency you add is capability the harness must then constrain and
verify — so add it deliberately, where the work genuinely can't be scripted, and use a
deterministic workflow everywhere else.

# Related

- [harness engineering](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
- [conductor and orchestrator roles](/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md)

# Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
