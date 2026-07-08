---
type: Agentic SDLC Practice
title: Model Selection And Routing
description: Not every task deserves the frontier model. Matching model tier to task complexity — routing simple work down and hard work up — is a harness-level cost and quality lever, not a one-time choice.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# Model Selection And Routing

The model may be only ~10% of the [harness](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md),
but *which* model runs each task is a lever you set inside the harness — and using one
frontier model for everything is expensive and often unnecessary. The paper describes the
default anti-pattern: in an unstructured workflow "a developer typically relies on a
single, massive frontier model for every interaction — paying premium token prices just to
ask the AI to fix a typo or generate a basic unit test"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 42).

## Match the model tier to the task

The alternative is intelligent routing: send hard tasks up to capable models and simple
tasks down to cheaper ones. The paper's version routes by SDLC phase — a well-designed
system "uses large, advanced models for highly complex tasks (Requirements, Architecture,
and initial Implementation) but automatically routes deterministic, lower-complexity tasks
(Test Generation, Code Review, and CI/CD monitoring) to smaller, faster, and significantly
cheaper models"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 42). OpenAI
frames the same principle at the task level: "not every task requires the smartest model —
a simple retrieval or intent classification task may be handled by a smaller, faster model,
while harder tasks like deciding whether to approve a refund may benefit from a more
capable model"
([A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 8).

## Baseline high, then downshift where you can

The routing map is not something to guess at — you derive it from evals. OpenAI's
recommended sequence is to establish a ceiling first, then trim: "build your agent
prototype with the most capable model for every task to establish a performance baseline.
From there, try swapping in smaller models to see if they still achieve acceptable results"
([building agents guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 8). The stated order of operations is: "set up evals to establish a performance
baseline... focus on meeting your accuracy target with the best models available...
optimize for cost and latency by replacing larger models with smaller ones where possible"
([building agents guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 8). Downshift only where the eval confirms quality holds — the smaller model is a saving
only if it still passes.

## Routing is a cost/quality lever, not a downgrade

Done well, routing does not trade quality for cost — it spends capability where it earns
its price and saves it where it doesn't. Because specific model names and tiers move quickly
(any given "frontier" and "cheap" model as of mid-2026 will be superseded), treat routing as
a policy over *tiers* rather than a hardcoded model list, and re-run the evals when the
model lineup changes. For the Claude-specific version of this decision, see
[choosing a model](/oks/claude-best-practices/subagents/choosing-a-model.md).

# Related

- [harness engineering](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
- [choosing a model](/oks/claude-best-practices/subagents/choosing-a-model.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
