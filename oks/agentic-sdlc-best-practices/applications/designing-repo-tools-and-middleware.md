---
type: Agentic SDLC Practice
title: Designing Repo Tools And Middleware
description: When an instruction alone isn't reliably followed, the fix is often a tool or a piece of middleware — a repeatable procedure for mining SDLC pain points, deciding instruction vs. tool vs. middleware, designing to tool-design principles, and proving the change moved an eval.
resource: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
tags:
  - agentic-sdlc
  - applications
timestamp: 2026-07-07T00:00:00Z
---

# Designing Repo Tools And Middleware

Not every problem is solved by writing a better instruction. Some behaviours the
model won't reliably do on prose alone — verify before exiting, avoid editing the
same file in a loop, load the working directory up front — are better enforced by
a *tool* the agent calls or *middleware* that wraps the agent loop. The motivating
evidence is concrete: LangChain moved its coding agent 13.7 points on
Terminal-Bench 2.0 (52.8% to 66.5%) with the model held fixed at gpt-5.2-codex,
changing only the harness (langchain.com). This procedure decides when to reach
for a tool or middleware instead of an instruction, and how to prove the change
worked. The design principles it applies live in
[tool design for agents](/oks/agentic-sdlc-best-practices/agent-harness/tool-design-for-agents.md)
and
[middleware and context management](/oks/agentic-sdlc-best-practices/agent-harness/middleware-and-context-management.md).

## Procedure: designing repo tools and middleware

1. **Mine the SDLC pain points.** Look at where the agent actually fails in this
   repo: skipped verification, doom-loops re-editing one file, wasted turns
   rediscovering the working directory, verbose tool output crowding out context.
   Most agent failures trace to a configuration gap — "a missing tool, a vague
   rule, an absent guardrail, or a context window stuffed with noise" (kaggle.com)
   — so name the specific failure before choosing a fix.

2. **Decide: instruction vs. tool vs. middleware.**
   - *Instruction* when the model already can do the thing and just needs telling
     — cheapest, try it first.
   - *Tool* when the agent needs a capability or a consolidated operation it
     otherwise can't perform reliably; a well-designed tool can collapse several
     API calls into one round-trip (anthropic.com), and for legacy systems without
     APIs a tool can even drive a UI (cdn.openai.com).
   - *Middleware* when the behaviour must be enforced around the loop regardless of
     what the model decides — LangChain's `PreCompletionChecklistMiddleware`
     intercepts the agent before it can exit to force self-verification, a
     `LocalContextMiddleware` maps the working directory on start, and a
     `LoopDetectionMiddleware` tracks per-file edit counts to catch doom-loops
     (langchain.com). A tool the model may forget to call; middleware runs whether
     it remembers or not.

3. **Design to the principles.** For tools: names and descriptions are loaded into
   context and act as prompts, so engineer them to steer tool choice; namespace
   related tools under a common prefix; keep responses token-efficient with
   pagination, filtering, or truncation; and write errors that tell the agent
   specifically how to fix its next call (anthropic.com). For middleware: attach at
   the right lifecycle hook — `before_model` to summarize history over a threshold,
   `wrap_tool_call` to offload verbose I/O to the filesystem — treating context
   management as a runtime concern, not a one-time prompt (langchain.com).

4. **Measure with evals.** A harness change is only real if it moves the suite.
   Establish a baseline, change one tool or one middleware, and re-run against the
   eval set — the 13.7-point gain was measured this way, model fixed. Route the
   measurement through
   [evals for agentic changes](/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md);
   keep what moves the number, revert what doesn't.

## Skeleton: the instruction-vs-tool-vs-middleware decision

```text
Observed failure: __________________________________

  Can the model already do it, given a clearer instruction?
    -> YES: write the instruction. (cheapest; stop here if it holds on evals)
    -> NO / it forgets:
         Does it need a new capability or a consolidated operation?
            -> YES: build a TOOL (namespaced, compact output, teaching errors).
         Must the behaviour hold regardless of what the model chooses?
            -> YES: build MIDDLEWARE (pick the lifecycle hook that fits).

Baseline eval: ____   After change: ____   Keep only if it moved the suite.
```

# Related

- [tool design for agents](/oks/agentic-sdlc-best-practices/agent-harness/tool-design-for-agents.md)
- [middleware and context management](/oks/agentic-sdlc-best-practices/agent-harness/middleware-and-context-management.md)
- [generating system prompts](/oks/agentic-sdlc-best-practices/applications/generating-system-prompts.md)

# Sources

- https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- https://www.anthropic.com/engineering/writing-tools-for-agents
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
