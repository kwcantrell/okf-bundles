---
type: OKF Concept Index
title: Running With Claude Code
description: Operating Karpathy's autonomous-research loop with Claude Code as the driving agent — running it headless, prompting the search, and time-boxing the blast radius.
resource: https://code.claude.com/docs/en/headless
tags:
  - autoresearch
  - karpathy
  - claude-code
timestamp: 2026-07-07T00:00:00Z
---

# Running With Claude Code

AutoResearch is agent-agnostic: Karpathy's repo tells you to "point your favorite
coding agent at `program.md`" and let it go. The loop itself just needs an
autonomous coding agent that can edit a file, run a command, read the result, and
decide to keep or discard — over and over, unattended. This area is about using
**Claude Code** as that agent: how its headless mode, prompting, and permission
controls support driving the
[agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md)
without a human in the seat.

## Concepts

- [claude code as the agent](/oks/autoresearch-best-practices/running-with-claude-code/claude-code-as-the-agent.md) — running Claude Code non-interactively with `claude -p` so it edits `train.py`, runs experiments, and iterates through an overnight loop unattended.
- [prompting the search](/oks/autoresearch-best-practices/running-with-claude-code/prompting-the-search.md) — reframing the hyperparameter and architecture search as prompt engineering: specific, well-scoped instructions steer the agent through the space with fewer corrections.
- [time-boxing and guardrails](/oks/autoresearch-best-practices/running-with-claude-code/time-boxing-and-guardrails.md) — pairing the loop's own 10-minute experiment kill with Claude Code's permission modes and sandboxing to bound the blast radius of an unattended run.
