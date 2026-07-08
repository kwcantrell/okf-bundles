---
type: Agentic SDLC Practice
title: Context Engineering Over Prompt Engineering
description: The quality of agent output depends less on clever prompt wording and more on curating everything the model sees — instructions, knowledge, files, tools, and history — which reframes the skill from prompting to context engineering.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - agentic-sdlc
  - context-engineering
timestamp: 2026-07-07T00:00:00Z
---

# Context Engineering Over Prompt Engineering

Prompt engineering treats the prompt as the lever: find the right phrasing and
the model produces good output. That framing misses where most of the leverage
actually lives. Once you're running an agent — a model in a loop, reading files,
calling tools, accumulating history — the prompt is only a fraction of what the
model conditions on. What matters is *everything the model sees*: the standing
instructions, the retrieved knowledge, the examples, the tool definitions, and
the running conversation. Deciding what goes into that window, and what stays
out, is the discipline the May 2026 SDLC paper calls context engineering — and
it argues "the quality of AI-generated code depends less on the cleverness of
your prompts and more on the quality of the context provided."

## From tricking the model to briefing a teammate

The mental shift is away from adversarial prompt-hacking and toward onboarding.
The paper reframes the core question as: not "how do I trick the AI into writing
good code?" but "what would a new team member need to know to contribute
effectively, and how do I encode that knowledge in a form the AI can use?" That
reframing is the same [syntax-to-intent](/oks/agentic-sdlc-best-practices/foundations/from-syntax-to-intent.md)
move applied to what you feed the agent: your job is to supply the intent,
constraints, and context that let the model translate a goal into working code —
not to hand-craft the phrasing of a single turn.

## The context, not the prompt, is the object of design

The paper enumerates six primary kinds of context a developer must consider —
"Instructions ... Knowledge ... Memory ... Examples ... Tools ... Guardrails" —
which makes plain how little of the picture the literal prompt covers. Anthropic
sharpens the goal: good context engineering means "finding the smallest possible
set of high-signal tokens that maximize the likelihood of some desired outcome."
The target is not a maximal dump of everything that might be relevant, but a
curated minimum. LangChain frames the same practice as a *runtime* concern —
"context engineering is a runtime problem, not a one-time prompt problem" — because
what the window should hold changes at every step of the agent's loop, not once
at the start.

The rest of this area is about doing that curation well: choosing what enters the
window, keeping long tasks inside their budget, and persisting the knowledge that
should survive across sessions.

# Related

- [from syntax to intent](/oks/agentic-sdlc-best-practices/foundations/from-syntax-to-intent.md)
- [curating the context window](/oks/agentic-sdlc-best-practices/context-engineering/curating-the-context-window.md)

# Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness
