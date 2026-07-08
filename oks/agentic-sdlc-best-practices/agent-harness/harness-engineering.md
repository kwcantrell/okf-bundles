---
type: Agentic SDLC Practice
title: Harness Engineering
description: The harness — system prompt, tools, middleware, and context policies wrapped around a model — is where most of an agent's real-world performance is won or lost, and it is an engineering surface in its own right.
resource: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# Harness Engineering

When people talk about "the agent," they usually mean the model. But the model is one
input into a much larger system. The paper puts it as an equation — Agent = Model +
Harness — where "everything else, the prompts, the tools, the context policies, the
hooks, the sandboxes, the sub-agents, the observability, is the harness: the
scaffolding wrapped around the model that lets it actually finish something"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 26). The striking claim that follows is one of proportion: a figure in the paper
depicts the model as roughly 10% of the system and the harness as roughly 90%
("Model ~10% Harness ~90%",
[paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 27).
Harness engineering is the practice of treating that 90% as the primary engineering
surface.

## What's in the harness

Concretely, the paper enumerates the harness as "Instructions and Rule Files ...
Tools ... Sandboxes and execution environments ... Orchestration logic ... Guardrails
or Hooks ... Observability"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 28).
Each of these is something you build, version, and tune — not something the model
brings with it. LangChain frames the discipline the same way: "Harness Engineering is
about systems, you're building tooling around the model to optimize goals"
([Improving Deep Agents with Harness Engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)).
The goals it names are task performance, token efficiency, and latency — the levers
you can move without touching the model at all.

## The model is roughly 10% of the system

The reason this matters is that it reassigns blame for failures. The paper's honest
diagnosis is that "most agent failures, examined honestly, are configuration
failures" — a missing tool, a vague rule, an absent guardrail, or "a context window
stuffed with noise"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 31).
If the model is only 10% of the system, then reaching for a bigger model is usually
the wrong first move; the leverage is in the surrounding 90% you actually control.

## The evidence: harness changes alone move benchmarks

This is not just a framing — it is measurable. LangChain reports improving
"deepagents-cli (our coding agent) 13.7 points from 52.8 to 66.5 on Terminal Bench
2.0"
([Improving Deep Agents with Harness Engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)),
and the point that makes it evidence about the harness is what they held constant:
"we only tweaked the harness and kept the model fixed, gpt-5.2-codex" (as reported in
that post). A +13.7-point move with an unchanged model — this is the kind of gain
harness work produces. The paper describes an even larger swing: "on Terminal Bench
2.0, one team moved a coding agent from outside the Top 30 to the Top 5 by changing
only the harness, with no model change at all"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 31).
(These are specific benchmark results as of late 2026; the exact numbers move as
models and harnesses evolve, but the lesson — that the harness is where the gains
are — is durable.)

## The harness is where the rest of this area lives

Because the harness is the system you actually build, the other concepts here are
its components: the [system prompt](/oks/agentic-sdlc-best-practices/agent-harness/system-prompt-design.md)
is its instructions, the [tools](/oks/agentic-sdlc-best-practices/agent-harness/tool-design-for-agents.md)
are its hands, the [middleware](/oks/agentic-sdlc-best-practices/agent-harness/middleware-and-context-management.md)
is the layer that manages context around the loop, and
[model selection and routing](/oks/agentic-sdlc-best-practices/agent-harness/model-selection-and-routing.md)
decides which model each task deserves. Treating the whole assembly as a product with
its own SDLC is the [factory model](/oks/agentic-sdlc-best-practices/agent-harness/the-factory-model.md).

# Related

- [anatomy of a coding agent](/oks/agentic-sdlc-best-practices/foundations/anatomy-of-a-coding-agent.md)
- [system prompt design](/oks/agentic-sdlc-best-practices/agent-harness/system-prompt-design.md)
- [tool design for agents](/oks/agentic-sdlc-best-practices/agent-harness/tool-design-for-agents.md)
- [middleware and context management](/oks/agentic-sdlc-best-practices/agent-harness/middleware-and-context-management.md)
- [evals for agentic changes](/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md)

# Sources

- https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
