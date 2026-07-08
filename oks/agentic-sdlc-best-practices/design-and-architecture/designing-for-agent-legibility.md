---
type: Agentic SDLC Practice
title: Designing For Agent Legibility
description: An agent works in a codebase the way a new teammate would — through a limited context window — so the structural choices that make code legible to a newcomer (modularity, clear boundaries, small focused files, consistent conventions) are the same ones that let an agent work in it reliably.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - design-and-architecture
timestamp: 2026-07-07T00:00:00Z
---

# Designing For Agent Legibility

An agent reads a codebase through a finite context window: it can hold only so
much of the system in view at once, and it works from what it can see plus what
you point it at. That makes legibility an architectural property, not just a
matter of taste. A structure that a new human teammate could navigate — where
responsibilities are separated, boundaries are clear, and files are small enough
to hold in your head — is also the structure an agent can work in without
losing the thread. The question the paper poses for context engineering carries
over directly to architecture: "what would a new team member need to know to
contribute effectively" (Osmani, Saboo, and Kartakis, *The New SDLC With Vibe
Coding*, May 2026)? Design for that reader and you have designed for the agent.

## Structure the agent can hold in view

The choices that pay off are the familiar ones, now with a sharper reason
behind them:

- **Modularity and clear boundaries** — when each module owns a bounded
  responsibility, an agent can change one without loading the rest. Blurred
  boundaries force it to pull in more of the system to make a safe edit, and a
  context window has a limit.
- **Small, focused files** — a file that does one thing is one an agent can
  read whole and reason about completely. A sprawling file gets partially read,
  and partial reads are where subtle mistakes hide.
- **Consistent conventions** — when patterns repeat, the agent can generalize
  from what it has already seen and produce code that matches. When every corner
  is a special case, there's nothing to generalize from, and each edit is a
  fresh negotiation with the codebase.

The same discipline is what keeps unstructured generation from compounding into
what the paper calls AI-generated "spaghetti" — code that later takes days to
reverse-engineer precisely because nobody, human or agent, can read it in one
pass.

## Legibility is written down, then structural

Legibility has two layers. The written layer is the durable context an agent
loads to orient itself — the design that
[explains constraints and interfaces](/oks/agentic-sdlc-best-practices/design-and-architecture/design-docs-as-agent-context.md)
and the
[AGENTS.md / CLAUDE.md files](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
that tell it the conventions to follow. The structural layer is the code itself
being shaped so those conventions are easy to honor. The two reinforce each
other: convention files describe the patterns, and a legible structure makes the
patterns cheap to follow. Get both right and an agent can work in the codebase
reliably; neglect either and it's guessing.

# Related

- [design docs as agent context](/oks/agentic-sdlc-best-practices/design-and-architecture/design-docs-as-agent-context.md)
- [agents.md and claude.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://agents.md/
