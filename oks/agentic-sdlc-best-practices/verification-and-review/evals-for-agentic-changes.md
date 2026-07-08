---
type: Agentic SDLC Practice
title: Evals For Agentic Changes
description: Unit tests check whether a change is correct; evals check whether the agent that produces changes still works. Task-level evals on your own codebase become the harness's regression suite — and the gains they measure are numbers, not vibes.
resource: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
tags:
  - agentic-sdlc
  - verification-and-review
timestamp: 2026-07-07T00:00:00Z
---

# Evals For Agentic Changes

Tests answer "is this change correct?" Evals answer a different question: "does the
agent that produces changes still perform?" Once an agent — and the harness around
it — is the thing generating your code, the harness itself becomes a system that can
regress, and you need a way to measure that. The paper's advice to engineering
leaders is to set the quality bar there: "Set the bar at the eval, not the demo. A
working demo proves an agent can succeed once. A passing eval suite proves it
succeeds reliably"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 44).

## Task-level evals on your codebase, not public leaderboards

Public benchmarks are useful for calibration, and they are getting genuinely hard:
Terminal-Bench 2.0 is "a carefully curated hard benchmark composed of 89 tasks in
computer terminal environments... frontier models and agents score less than 65% on
the benchmark"
([Terminal-Bench](https://arxiv.org/abs/2601.11868)), and SWE-Bench Pro extends the
lineage to "long-horizon tasks that may require hours to days for a professional
software engineer to complete, often involving patches across multiple files" on a
"contamination-resistant testbed"
([SWE-Bench Pro](https://arxiv.org/abs/2509.16941)). But a public leaderboard tells
you how an agent does on *someone else's* tasks. What you need to know is how it does
on *yours* — the recurring shapes of work in your repository, your conventions, your
failure modes. That means building evals out of representative tasks on your own
codebase and grading the agent's output against them.

## Evals as the harness's regression suite

The reason this is worth the effort is that harness changes are measurable, and their
effects are not obvious by inspection. When you tune a prompt, add a middleware, or
change a tool, the honest question is whether the agent got better or worse — and the
only way to answer it is to re-run the eval suite. The paper describes exactly this
as a continuous flywheel: "evaluate against a benchmark suite, diagnose failures by
clustering root causes, optimize the prompts or tools that caused them, verify fixes
against a regression suite, and monitor production traffic for new failure modes.
Each cycle compounds"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 23).
The eval suite is the regression suite for the harness itself.

## The gains are measured, not vibes

The strongest argument for this discipline is that it turns "the agent feels better"
into a number. LangChain reports improving "deepagents-cli (our coding agent) 13.7
points from 52.8 to 66.5 on Terminal Bench 2.0"
([Improving Deep Agents with Harness Engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)) —
and, crucially, "we only tweaked the harness and kept the model fixed, gpt-5.2-codex"
(as reported in that post). A +13.7-point move attributable entirely to harness
changes, with the model held constant, is only knowable because it was measured
against a fixed eval. Without the eval, the same set of changes would have been a
collection of plausible-sounding tweaks with no way to tell which helped, which hurt,
and by how much. Evals are what let you attribute an improvement to a cause instead
of guessing.

Building the eval suite is itself part of engineering the harness — a subject this
bundle takes up in its own right.

# Related

- [agent-written tests and reward hacking](/oks/agentic-sdlc-best-practices/verification-and-review/agent-written-tests-and-reward-hacking.md)

# Sources

- https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://arxiv.org/abs/2601.11868
- https://arxiv.org/abs/2509.16941
