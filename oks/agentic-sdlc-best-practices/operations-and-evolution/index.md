---
type: OKF Concept Index
title: Operations And Evolution
description: What happens after the code is written and merged — when agents run inside CI/CD pipelines, when change velocity climbs and the deployment safety net has to climb with it, and when whole codebases get migrated or refactored as supervised agent campaigns. The through-line is that speed on the way in demands stronger guardrails on the way out.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - operations-and-evolution
timestamp: 2026-07-07T00:00:00Z
---

# Operations And Evolution

The earlier areas cover how an agent gets a change written, reviewed, and merged.
This one is about everything downstream of the merge — the operational surface that
absorbs agent-authored change once it starts flowing faster than before. The paper
frames two shifts here. Deployment pipelines become "AI-aware," with agents able to
"monitor deployment health, automatically roll back problematic releases, and predict
deployment risks"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 23). And maintenance — "perhaps the most underestimated transformation" (p. 24) —
opens up work that used to be too tedious and risky to attempt at all: migrations,
dependency upgrades, and modernizing legacy code.

The common thread across these concepts is a trade: agents let more change move
through the system faster, so the operational guardrails around that change — the CI
gates, the observability, the rollback path — have to get stronger, not weaker. None
of them let the agent become the final authority over its own release.

## Concepts

- [agents in CI/CD](/oks/agentic-sdlc-best-practices/operations-and-evolution/agents-in-ci-cd.md) — putting agents inside the pipeline (automated fixes, PR bots, headless runs) while keeping CI as the source of truth and never letting the agent own the gate that approves its own merge.
- [monitoring, rollback, and progressive delivery](/oks/agentic-sdlc-best-practices/operations-and-evolution/monitoring-rollback-and-progressive-delivery.md) — observability and a fast rollback path as the safety net that makes higher change velocity survivable, staging releases so a bad agent-authored change is caught small.
- [large-scale refactors and migrations](/oks/agentic-sdlc-best-practices/operations-and-evolution/large-scale-refactors-and-migrations.md) — running mechanical sweeps, dependency upgrades, and framework migrations as supervised agent campaigns, with verification that scales to the size of the change.
