---
type: OKF Concept Index
title: Implementation
description: The phase where the agent writes the code, reframed as steering rather than typing. When AI can generate most of a feature but the wrong parts "look right," implementation discipline is about the checks that surround generation — tests as the spec, small verified steps, and the human gates that never fully close.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - implementation
timestamp: 2026-07-07T00:00:00Z
---

# Implementation

When the agent is the one writing the code, implementation work shifts "from
writing to reviewing, guiding, and verifying" ([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 22). The agent can generate most of a feature fast, but the dangerous failures
are the ones that look correct — so the practices that matter are the checks
wrapped around generation, not the generation itself. This area covers three:
turning intended behavior into tests the agent must pass, keeping each step small
enough to verify before the next, and deciding which decisions stay with a human
regardless of how autonomous the agent becomes.

## Concepts

- [TDD as agent guardrail](/oks/agentic-sdlc-best-practices/implementation/tdd-as-agent-guardrail.md) — tests written first become an executable spec the agent must satisfy, turning "looks right" into a runnable pass/fail check.
- [small verifiable increments](/oks/agentic-sdlc-best-practices/implementation/small-verifiable-increments.md) — a short leash of small diffs and frequent checkpoints so mistakes surface one step deep instead of buried in a large change.
- [human-in-the-loop checkpoints](/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md) — the cross-cutting question of which gates stay human — spec approval, security-sensitive code, irreversible actions — plus autonomy dials and escalation triggers.
