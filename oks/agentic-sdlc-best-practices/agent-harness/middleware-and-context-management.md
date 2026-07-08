---
type: Agentic SDLC Practice
title: Middleware And Context Management
description: Middleware is the layer that sits between the agent loop and the model, where context management stops being a one-time prompt-writing task and becomes a runtime discipline of summarizing, editing, and guarding every step.
resource: https://docs.langchain.com/oss/python/langchain/middleware
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# Middleware And Context Management

The agent loop is simple to state: "the core agent loop involves calling a model,
letting it choose tools to execute, and then finishing when it calls no more tools"
([LangChain middleware docs](https://docs.langchain.com/oss/python/langchain/middleware)).
Middleware is the part of the [harness](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
that lets you intervene at each turn of that loop rather than only at its edges. LangChain
describes it as the way to "more tightly control what happens inside the agent"
([LangChain middleware docs](https://docs.langchain.com/oss/python/langchain/middleware)) —
logging, transforming prompts and outputs, adding retries and fallbacks, and enforcing
safety guardrails, all attached before and after each model and tool call.

## Context management is a runtime problem

The reframing that makes middleware important is this: LangChain argues "context
engineering is a runtime problem, not a one-time prompt problem"
([how middleware lets you customize your agent harness](https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness)).
You cannot curate the context window once at the start and be done, because the window
fills continuously as the agent works. Middleware is "the mechanism under the hood that
makes context engineering practical for developers"
([LangChain context-engineering docs](https://docs.langchain.com/oss/python/langchain/context-engineering)) —
the place where each strategy gets implemented as a hook on the loop.

## The lifecycle hooks (as of mid-2026)

LangChain's middleware API, as of mid-2026, exposes distinct lifecycle hooks —
`before_agent`, `before_model`, `wrap_model_call`, `wrap_tool_call`, `after_model`, and
`after_agent` — that sit between the loop and the underlying model and tool calls.
`wrap_model_call` is the natural home for cross-cutting concerns: it "wraps the model
call end-to-end. Caching, retries, and dynamic model requests like changing available
tools all live here"
([how middleware lets you customize your agent harness](https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness)).
Named middleware makes the pattern concrete. `SummarizationMiddleware` implements
`before_model` — "if message history exceeds a certain token threshold, its contents are
summarized before being passed to the model"
([how middleware lets you customize your agent harness](https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness)) —
which is [compaction](/oks/agentic-sdlc-best-practices/context-engineering/compaction-and-long-horizon-context.md)
implemented as a hook. Extensions of it "implement a `wrap_tool_call` hook to extend
verbose tool call inputs and outputs to the filesystem"
([same post](https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness)),
offloading bulk out of the window instead of summarizing it.

## Summarization, context editing, guardrails, caching

These hooks give you the standard context-management moves as composable pieces.
*Summarization and compaction* keep long-horizon runs under the token limit.
*Context editing* — offloading verbose tool output to the filesystem and keeping a
lightweight reference — trims noise without losing recoverability. *Guardrail hooks* run
deterministic checks around model and tool calls, the kind of safety layer middleware is
built to host. And *caching* pays off on the static parts of the prompt: LangChain's Deep
Agents "automatically applies prompt caching to static sections of the system prompt...
This avoids reprocessing the same tokens across calls, reducing both latency and cost"
([Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview)) — for
Anthropic and Amazon Bedrock models as of mid-2026. Deep Agents itself is described as an
"agent harness"
([Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview)),
which is exactly the point: the middleware stack *is* a large part of the harness you tune.

# Related

- [harness engineering](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
- [compaction and long-horizon context](/oks/agentic-sdlc-best-practices/context-engineering/compaction-and-long-horizon-context.md)

# Sources

- https://docs.langchain.com/oss/python/langchain/middleware
- https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness
- https://docs.langchain.com/oss/python/langchain/context-engineering
- https://docs.langchain.com/oss/python/deepagents/overview
