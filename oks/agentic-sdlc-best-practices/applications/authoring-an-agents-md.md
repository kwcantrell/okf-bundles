---
type: Agentic SDLC Practice
title: Authoring An AGENTS.md
description: A repo-specific AGENTS.md is the static-instruction layer an agent loads on every task, so it should encode what the repository actually does — build and test commands, conventions, SDLC gates, guardrails — derived from evidence in the repo, not from ideals asserted as fact.
resource: https://agents.md/
tags:
  - agentic-sdlc
  - applications
timestamp: 2026-07-07T00:00:00Z
---

# Authoring An AGENTS.md

AGENTS.md is "a README for agents" — the file a coding agent reads before it
touches a repository. It is not the human-facing README: README.md holds quick
starts and contribution guidelines for people, while AGENTS.md holds "the extra,
sometimes detailed context agents need" (agents.md). The two complement rather
than duplicate — keep human onboarding out of AGENTS.md and agent-specific
context out of README.md. The format has broad reach (agents.md reports use
across tens of thousands of open-source projects) and is now stewarded by a
neutral foundation rather than a single vendor, so an AGENTS.md you write is
portable across the agents that read it.

The failure mode this procedure guards against is writing an *aspirational*
AGENTS.md — one that describes the repository you wish existed. If the file
claims "all changes go through TDD" but the repo has no test suite, the agent
will confidently follow a rule the codebase can't support. Encode what is
actually there; flag the gap as a recommendation, clearly labelled as such.

## Procedure: producing a repo-specific AGENTS.md

1. **Derive from evidence first — inspect before you assert.** Read the target
   repo and record what is *actually* true, not what should be:
   - Are there tests? What command runs them, and does it currently pass?
   - Is there a review flow (PR template, CODEOWNERS, required approvals)?
   - Is there CI? What does it gate on (lint, build, tests, security scans)?
   - What is the commit-message and branch style in recent history?
   - What build/run/lint commands appear in package manifests or task files?
   Encode each observed practice as an instruction. Where a practice is *absent
   but advisable*, write it under a clearly-marked "Recommendations" heading —
   never phrase an ideal as current practice. This mirrors the provider guidance
   to derive instructions from existing operating procedures and documents
   rather than inventing them (cdn.openai.com).

2. **Default the output to conservative autonomy.** Because trust is earned per
   task type and the last 20% of a change is where models fail
   ([trust calibration](/oks/agentic-sdlc-best-practices/foundations/trust-calibration-and-the-80-percent-problem.md)),
   start the AGENTS.md granting the least autonomy that still lets the agent
   work: require the human-review and verification gates the repo already has,
   and add a checkpoint before anything irreversible
   ([human-in-the-loop checkpoints](/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md)).
   You can widen autonomy later as the agent demonstrates reliability; you cannot
   easily un-break a repo an over-trusted agent damaged.

3. **Decide what belongs in the file vs. what the agent derives from code.** Put
   in AGENTS.md the things an agent cannot reliably infer by reading source:
   build/test/lint commands, project conventions, the SDLC gates it must respect,
   and hard guardrails (agents.md lists project overview, build and test
   commands, code style, testing instructions, and security considerations).
   Leave out anything the agent reads faster from the code itself — implementation
   detail, per-function behaviour — so the static file stays high-signal.

4. **Write hard guardrails as hard constraints.** Guardrails are one of the core
   context types — "hard constraints, formatting rules, and safety validations"
   (kaggle.com). State the non-negotiables plainly ("never commit secrets";
   "never force-push `main`"). Pair this file with a defense-in-depth safety
   posture rather than relying on prose alone
   ([Claude safety](/oks/claude-best-practices/safety/index.md)).

5. **Handle placement and precedence.** This concept produces the *content*; the
   *where and which-wins* is handed off to the repo-structure bundle. In a
   monorepo, place a nested AGENTS.md per package — the agent reads the nearest
   file to what it is editing (agents.md). For the full placement and precedence
   rules, see
   [AGENTS.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
   and
   [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md).

6. **Start small and grow by correction.** The recommended starting size is
   roughly ten lines — stack, conventions, hard rules, workflow — with a new rule
   added "every time the agent does something it should not do again"
   (kaggle.com). Treat the file as versioned and living, not a one-time
   write.

## Skeleton AGENTS.md template

Section headings with one-line guidance for each — instantiate in the repo's own
words; do not copy prose from any source.

```markdown
# AGENTS.md

## Project overview
> One or two lines: what this repo is and its primary language/framework.

## Setup & commands
> The exact commands to install, build, run, lint, and test — as they work today.

## Conventions
> Code style, naming, and structural patterns observed in the existing codebase.

## SDLC gates
> The workflow steps a change must pass (spec/plan, review, CI) before it merges.

## Guardrails
> Hard constraints: what the agent must never do (secrets, destructive git, etc.).

## Autonomy & checkpoints
> Where the agent may act freely vs. where it must stop and ask a human.

## Recommendations (not yet current practice)
> Advisable practices the repo lacks today — labelled so they aren't read as fact.
```

# Related

- [AGENTS.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
- [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md)
- [trust calibration and the 80% problem](/oks/agentic-sdlc-best-practices/foundations/trust-calibration-and-the-80-percent-problem.md)
- [human-in-the-loop checkpoints](/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md)
- [Claude safety](/oks/claude-best-practices/safety/index.md)

# Sources

- https://agents.md/
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
