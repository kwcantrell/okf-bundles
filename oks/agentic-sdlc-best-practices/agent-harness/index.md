---
type: OKF Concept Index
title: Agent Harness
description: The harness — system prompt, tools, middleware, context policies, and the model-routing and workflow decisions around them — is where most of an agent's real-world performance is won. This area treats that scaffolding as the primary engineering surface.
resource: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# Agent Harness

If the model is roughly 10% of an agentic system, the other 90% — the prompts, tools,
middleware, context policies, guardrails, and observability wrapped around the model — is the
harness, and it is where most performance is won or lost. This is the bundle's centerpiece
area: it treats that scaffolding as an engineering surface in its own right, drills into each
of its components, and ends with the decisions of which model runs each task and whether a
task needs an autonomous agent at all. The unifying evidence is that harness changes alone —
model held fixed — move hard benchmarks by double digits.

## Concepts

- [harness engineering](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md) — the harness as the ~90% of the system you actually build, and the evidence that tuning it (not the model) drives the gains.
- [system prompt design](/oks/agentic-sdlc-best-practices/agent-harness/system-prompt-design.md) — the instruction layer, and its hardest problem: altitude — strong heuristics over brittle hardcoded rules, and pruning staleness.
- [tool design for agents](/oks/agentic-sdlc-best-practices/agent-harness/tool-design-for-agents.md) — names and descriptions as prompts, token-efficient outputs, errors that teach, and consolidation over proliferation.
- [middleware and context management](/oks/agentic-sdlc-best-practices/agent-harness/middleware-and-context-management.md) — the layer between the loop and the model, where context management becomes a runtime discipline of summarization, editing, guardrails, and caching.
- [model selection and routing](/oks/agentic-sdlc-best-practices/agent-harness/model-selection-and-routing.md) — matching model tier to task complexity as a cost/quality lever: route simple work down, hard work up.
- [the factory model](/oks/agentic-sdlc-best-practices/agent-harness/the-factory-model.md) — building the system that builds the software, and treating the agent-plus-harness as a product with its own SDLC.
- [workflows vs agents](/oks/agentic-sdlc-best-practices/agent-harness/workflows-vs-agents.md) — when a predefined workflow beats an autonomous agent: deterministic orchestration for known shapes, agency only for open-ended work.
