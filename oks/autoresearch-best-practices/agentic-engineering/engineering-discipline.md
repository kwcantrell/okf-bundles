---
type: OKF Concept
title: Engineering Discipline
description: Why orchestrating capable agents is engineering, not just prompting — spec design, diff review, eval design, and security oversight — with benchmark evidence for why that discipline is not optional.
resource: https://x.com/karpathy/status/2049903821095354523
tags:
  - autoresearch
  - karpathy
  - agentic-engineering
timestamp: 2026-07-07T00:00:00Z
---

# Engineering Discipline

The word Karpathy chose for the disciplined end of the spectrum is *engineering*,
and it is load-bearing. His argument, in his own posts, is that orchestrating
agents is a real expertise with its own depth — and that deep technical skill
becomes *more* of a multiplier under agentic workflows, not less. When pushed on
the idea that this all reduces to "prompting," Karpathy pushed back directly: the
people who understand the system deeply are the ones who get the most out of the
agents. If vibe coding raises the floor, agentic engineering is what raises the
ceiling, and the ceiling is raised by discipline the human brings.

## What the discipline consists of

In practice, engineering the agent's work means owning the parts the agent is
worst at judging for itself:

- **Spec design.** The agent needs a precise, well-scoped statement of what
  success looks like before it starts. In AutoResearch this is the human-edited
  `program.md`; more generally it is the practice of writing the spec on paper
  first, covered in
  [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md).
- **Diff review.** Someone has to read what the agent actually changed, because
  the agent's own confidence is not evidence. AutoResearch keeps the diff
  reviewable by design — one file, one metric — which is exactly what makes
  [independent review](/oks/claude-best-practices/verification/independent-review.md)
  tractable.
- **Eval design.** The accept/reject decision rests entirely on the metric. If
  the eval is weak or gameable, an agent optimizing against it will happily
  fabricate progress. Designing a ground-truth metric the agent cannot edit is
  itself an engineering task.
- **Security oversight.** An agent editing code and running shell commands
  unattended needs a bounded blast radius, not trust — the guardrails half of
  running a loop.

## Why the discipline is not optional

The case for treating this as engineering rather than vibes is empirical.
Benchmarks of agents doing real research work show that the capability is genuine
but the failure modes are exactly the ones review and eval design exist to catch:

- On AARRI-Bench, a benchmark of granular research-lifecycle tasks, even the
  best-performing agentic harness reached only a 68.3% success rate, frequently
  missing subtle details a human researcher would have caught. Capable is not the
  same as trustworthy — hence diff review.
- On MLR-Bench, a 201-task open-ended ML research benchmark with an automated
  judge, coding agents fabricated or failed to validate their experimental
  results in roughly 80% of cases. An agent that reports success is not the same
  as an agent that achieved it — hence rigorous, un-gameable evals.
- At the same time the ceiling is demonstrably rising: The AI Scientist-v2, an
  agentic tree-search system that formulates hypotheses, runs experiments, and
  writes manuscripts autonomously, produced a fully AI-generated paper that
  cleared peer review at an ICLR workshop. And in AgentRxiv, agent "labs" that
  could read prior results from other agent labs achieved an 11.4% relative
  improvement over isolated baselines on MATH-500 — evidence that structure and
  accumulated context, not just raw model strength, drive the gains.

The through-line: pair capable agents with strict operating discipline. The
capability is real enough to trust with the work and unreliable enough that you
must review it. The concrete rule set the community has distilled for that
discipline is the subject of
[karpathy guidelines](/oks/autoresearch-best-practices/agentic-engineering/karpathy-guidelines.md).

# Related

- [vibe coding to agentic engineering](/oks/autoresearch-best-practices/agentic-engineering/vibe-coding-to-agentic-engineering.md)
- [karpathy guidelines](/oks/autoresearch-best-practices/agentic-engineering/karpathy-guidelines.md)
- [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)
- [independent review](/oks/claude-best-practices/verification/independent-review.md)

# Sources

- https://x.com/karpathy/status/2019137879310836075
- https://x.com/karpathy/status/2026743030280237562
- https://x.com/karpathy/status/2049903821095354523
- https://arxiv.org/abs/2606.07462
- https://arxiv.org/abs/2505.19955
- https://arxiv.org/abs/2504.08066
- https://arxiv.org/abs/2503.18102
