---
type: OKF Bundle Index
title: Agentic SDLC Best Practices
description: A cross-linked OKF bundle on the software development lifecycle when AI agents write the code — the vibe-coding-to-agentic-engineering spectrum, context engineering, phase-by-phase practices, harness engineering, and procedures for authoring AGENTS.md files, system prompts, and agent tooling.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
timestamp: 2026-07-07T00:00:00Z
---

# Agentic SDLC Best Practices

An [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
bundle on how the software development lifecycle changes once AI agents do the
engineering. It is anchored in
[The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding)
(Addy Osmani, Kanchan Saboo, and Stelios Kartakis; Google, May 2026), and grounds
each practice in that paper plus primary engineering material from Anthropic,
OpenAI, and LangChain. The through-line is that when an agent writes the syntax,
the engineer's job relocates toward expressing intent and verifying outcomes — and
that one shift reshapes every phase of the lifecycle.

Where the sibling
[claude-best-practices](/oks/claude-best-practices/index.md) bundle covers how to
*operate* one coding agent well and
[ai-agent-repo-structure](/oks/ai-agent-repo-structure/index.md) covers how to
*structure a repo* so agents can find context, this bundle is about the
*lifecycle and the harness*: what the SDLC looks like when agents build the code,
and how to engineer the scaffolding around them. It pays off in three consumer
procedures in [applications](/oks/agentic-sdlc-best-practices/applications/index.md):
authoring an `AGENTS.md`, generating a coding-agent system prompt, and designing
repo tools and middleware.

## Concept areas

- [foundations](/oks/agentic-sdlc-best-practices/foundations/index.md) — the mental model: the shift from syntax to intent, the vibe-coding-to-agentic-engineering spectrum, the new economics and roles, and what an agent actually is.
- [context-engineering](/oks/agentic-sdlc-best-practices/context-engineering/index.md) — curating everything the model sees as a discipline distinct from prompt-writing: the context window as a finite budget, long-horizon compaction, and knowledge that persists across sessions.
- [requirements-and-planning](/oks/agentic-sdlc-best-practices/requirements-and-planning/index.md) — the phase before code when the agent implements the spec literally: making specs precise, cutting work into agent-sized verifiable units, and sharpening requirements with AI.
- [design-and-architecture](/oks/agentic-sdlc-best-practices/design-and-architecture/index.md) — the most human-owned phase: using the agent as a design partner, writing design docs it consumes downstream, and shaping code to stay legible to an agent reading through a limited window.
- [implementation](/oks/agentic-sdlc-best-practices/implementation/index.md) — steering rather than typing: tests as the executable spec, small verified increments, and the human gates that never fully close.
- [verification-and-review](/oks/agentic-sdlc-best-practices/verification-and-review/index.md) — the phase that decides whether "looks done" is done: agent-gamed tests, evals that measure the harness, review economics under high-volume output, adversarial panels, and security for AI-authored changes.
- [operations-and-evolution](/oks/agentic-sdlc-best-practices/operations-and-evolution/index.md) — everything downstream of the merge: agents inside CI/CD, monitoring and rollback as the safety net for higher velocity, and large refactors run as supervised campaigns.
- [agent-harness](/oks/agentic-sdlc-best-practices/agent-harness/index.md) — the centerpiece: the system prompt, tools, middleware, context policies, and model-routing that make up the ~90% of an agentic system where most performance is won.
- [applications](/oks/agentic-sdlc-best-practices/applications/index.md) — the payoff: reusable procedures and templates for authoring an `AGENTS.md`, generating a coding-agent system prompt, designing repo tools and middleware, packaging skills, and staging adoption.

## How to read this bundle

Each concept file carries YAML frontmatter (type, title, description, a primary
`resource` URL, tags, and a timestamp), an explanatory body, a `# Related`
section of cross-links, and a `# Sources` section citing the primary material
behind its claims. If you want a procedure you can run right now, walk
[applications](/oks/agentic-sdlc-best-practices/applications/index.md) — its
concepts each carry an explicit checklist or template. If you want the practices
those procedures encode, walk the phase areas (requirements-and-planning through
operations-and-evolution) and the harness area, or start with
[foundations](/oks/agentic-sdlc-best-practices/foundations/index.md) if you're
new to the shift, since everything else builds on that model.
