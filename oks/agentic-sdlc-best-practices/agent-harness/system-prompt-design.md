---
type: Agentic SDLC Practice
title: System Prompt Design
description: The system prompt is the harness's instruction layer, and its hardest problem is altitude — pitching guidance high enough to give strong heuristics without hardcoding brittle rules that go stale.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# System Prompt Design

The system prompt is the part of the [harness](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
that tells the model who it is and how to behave. OpenAI's guidance is blunt about why
it matters: "clear instructions reduce ambiguity and improve agent decision-making,
resulting in smoother workflow execution and fewer errors"
([A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 11). But writing a good one is not about writing *more* — it is about pitching the
instructions at the right level.

## Altitude: heuristics over hardcoded rules

The central design problem is what Anthropic calls altitude. Set the prompt too low —
a long list of if-this-then-that rules — and it becomes brittle: every case you didn't
enumerate is a case the model handles badly. Set it too high — vague platitudes — and
it fails to steer. The target is between them: "the right altitude strikes a balance:
specific enough to guide behavior effectively, yet flexible enough to provide the model
with strong heuristics"
([Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
The practical test is whether an instruction gives the model a *principle* it can apply
to unseen situations, or just a lookup entry for one situation.

## Structure the work into stages

Altitude does not mean vagueness about process. A useful pattern is to give the model an
explicit high-level shape for the task without dictating each keystroke. LangChain's
revised coding-agent prompt does exactly this, structuring agent work into four stages —
"1. Planning & Discovery ... 2. Build ... 3. Verify ... 4. Fix"
([Improving Deep Agents with Harness Engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)).
That is a heuristic scaffold: it tells the agent the arc of good work without hardcoding
what to do at each step.

## Examples do work that rules cannot

Instructions derived from real procedures beat invented ones. OpenAI recommends deriving
routines from "existing operating procedures, support scripts, or policy documents"
([building agents guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 11), and being explicit where explicitness pays: "being explicit about the action
(and even the wording of a user-facing message) leaves less room for errors in
interpretation"
([building agents guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 11). A concrete example of a hard edge case is often clearer than three sentences
trying to describe it.

## Common failure modes: over-specification and stale instructions

Two failure modes recur. The first is over-specification — the low-altitude trap, where
a prompt so crammed with rules that it fights the model's own judgment and breaks on
anything unanticipated. The second is staleness: a system prompt is code, and like any
code it rots. Instructions written for an older model, an older codebase, or a
since-removed tool linger and actively mislead. Because good context engineering means
finding "the smallest possible set of high-signal tokens that maximize the likelihood of
some desired outcome"
([Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)),
every stale or over-specified line is worse than absent — it spends context *and*
misdirects. Treat the system prompt as a maintained artifact: prune it as aggressively
as you add to it.

Generating and iterating on system prompts programmatically — using a model to draft and
refine them against evals — is a further application covered later in this bundle.

# Related

- [harness engineering](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
- [tool design for agents](/oks/agentic-sdlc-best-practices/agent-harness/tool-design-for-agents.md)

# Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
