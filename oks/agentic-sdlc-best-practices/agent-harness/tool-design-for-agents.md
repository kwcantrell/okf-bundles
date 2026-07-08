---
type: Agentic SDLC Practice
title: Tool Design For Agents
description: Tools are the harness's hands, and a tool's name, description, output shape, and error messages are all prompt surface — designing them is prompt engineering by another name.
resource: https://www.anthropic.com/engineering/writing-tools-for-agents
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# Tool Design For Agents

Tools are how an agent acts on the world — and in the [harness](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md),
they are as much a prompt-engineering surface as the system prompt is. Everything about
a tool that the model sees — its name, its description, the shape of what it returns, the
text of its errors — flows into the context window and steers behavior. Anthropic makes
the point directly: because tool descriptions "are loaded into your agents' context, they
can collectively steer agents toward effective tool-calling behaviors"
([Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)).

## Names and descriptions are prompts

When several tools have overlapping purposes, the agent picks wrong. Anthropic's remedy
is namespacing: "namespacing (grouping related tools under common prefixes) can help
delineate boundaries between lots of tools"
([Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)).
A description should read like instruction, not documentation — it is telling the model
when and why to reach for this tool over its neighbors. OpenAI adds the operational
counterpart: tool definitions should be "well-documented, thoroughly tested, and
reusable" so they "improve discoverability, simplify version management, and prevent
redundant definitions"
([A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 9).

## Token-efficient outputs

A tool that dumps its full result into context taxes every subsequent turn. Anthropic
recommends compact output by default: "implement some combination of pagination, range
selection, filtering, and/or truncation with sensible default parameter values"
([Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)).
The default matters — the agent should get the useful subset without having to ask, and
should be able to request more only when it needs it.

## Error messages that teach

An error is a chance to correct the agent's next move, so write it like a prompt.
Anthropic's guidance: "you can prompt-engineer your error responses to clearly
communicate specific and actionable improvements"
([Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)).
"Invalid argument" tells the model nothing; "expected an ISO-8601 date like
2026-07-07, got 'yesterday'" tells it exactly how to fix the call.

## Consolidate rather than proliferate

The instinct to expose every underlying API as its own tool backfires — it multiplies
round-trips and overlapping choices. Better-designed tools "consolidate functionality,
handling potentially multiple discrete operations (or API calls) under the hood"
([Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)).
OpenAI's data on where this bites is worth keeping in mind: the problem is overlap, not
raw count — "some implementations successfully manage more than 15 well-defined, distinct
tools while others struggle with fewer than 10 overlapping tools"
([building agents guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 16). Prefer a few high-level, distinct tools over many narrow overlapping ones.

Designing repository-specific tools and middleware for your own codebase is a further
application covered later in this bundle.

# Related

- [harness engineering](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
- [system prompt design](/oks/agentic-sdlc-best-practices/agent-harness/system-prompt-design.md)
- [designing repo tools and middleware](/oks/agentic-sdlc-best-practices/applications/designing-repo-tools-and-middleware.md)

# Sources

- https://www.anthropic.com/engineering/writing-tools-for-agents
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
