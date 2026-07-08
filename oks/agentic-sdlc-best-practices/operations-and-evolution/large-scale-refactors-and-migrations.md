---
type: Agentic SDLC Practice
title: Large-Scale Refactors And Migrations
description: Running mechanical sweeps, dependency upgrades, and framework migrations as supervised agent campaigns — work that used to be too tedious and risky to attempt — with verification that scales to the size of the change through sampling plus a full-suite gate.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - operations-and-evolution
timestamp: 2026-07-07T00:00:00Z
---

# Large-Scale Refactors And Migrations

Maintenance is where the paper sees the most underestimated change. Legacy codebases
"that were once impenetrable to new team members can now be navigated, understood, and
modified with AI assistance," and code once considered "too risky to touch because only
its original authors understood it can now be safely refactored, modernized, and
extended"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 24). Concretely, agents "can systematically migrate codebases between frameworks,
update deprecated APIs, and modernize test suites — tasks that were previously so
tedious and risky that they simply never happened" (p. 24). The unlock is real: work
that never got prioritized because it was slow and error-prone becomes tractable.

## Treat it as a supervised campaign, not a single prompt

A large sweep is not one big autonomous run. It is a campaign: a well-specified
objective, executed in bounded pieces, each verified before the next proceeds — the
same short-leash discipline that keeps ordinary implementation honest (see
[small verifiable increments](/oks/agentic-sdlc-best-practices/implementation/small-verifiable-increments.md)).
Because the change is mechanical and repetitive across many files, it parallelizes
well: independent slices of the codebase can be worked concurrently in isolated
contexts and reviewed separately, which is exactly what
[parallel agents](/oks/claude-best-practices/subagents/parallel-agents.md) are for. The
supervision is what keeps a migration from turning a hundred correct edits and ten
subtly wrong ones into one un-reviewable diff.

## Verify at the scale of the change

The hard part of a large sweep is not making the edits — it is knowing they are all
correct. Reviewing every changed file by hand defeats the point, and rubber-stamping
them defeats the safety. The workable middle is layered: sample the diffs for human
review to catch the systematic mistakes (a bad transform repeats identically across
files, so a small sample surfaces it), and gate the whole campaign on the full test
suite so nothing merges until the mechanical change is proven not to have broken
behavior. This mirrors the paper's insistence on both output and trajectory checks — a
change that compiles and looks right but skipped its verification is the more dangerous
failure (p. 22). For a migration, that means the green full-suite run, not the plausible
diff, is what says the campaign is done. Rolling the finished campaign out is itself an
operational event; stage it and watch it, as with any high-volume change (see
[agents in CI/CD](/oks/agentic-sdlc-best-practices/operations-and-evolution/agents-in-ci-cd.md)).

# Related

- [agents in CI/CD](/oks/agentic-sdlc-best-practices/operations-and-evolution/agents-in-ci-cd.md)
- [small verifiable increments](/oks/agentic-sdlc-best-practices/implementation/small-verifiable-increments.md)
- [parallel agents](/oks/claude-best-practices/subagents/parallel-agents.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
