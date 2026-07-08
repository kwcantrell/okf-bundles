---
type: Agentic SDLC Practice
title: Small Verifiable Increments
description: Keeping the agent on a short leash — small diffs, frequent checkpoints, verify before continuing — so mistakes surface while they are one step deep and cheap to correct, rather than buried under a large multi-file change.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - implementation
timestamp: 2026-07-07T00:00:00Z
---

# Small Verifiable Increments

An agent can produce "multi-file changes that work together correctly" from a
single description ([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 22), and that capability is exactly what makes an unsupervised long run
dangerous. The more the agent generates between checks, the more a single wrong
assumption compounds — and because the paper's central implementation risk is that
AI-generated code "looks right" while being subtly wrong (p. 34), a large diff
buries that error under a lot of plausible-looking code. The discipline is to keep
each step small enough that its output can be verified before the next one starts.

## Small diffs, verify, then continue

The implementation phase is best understood not as writing code but as steering:
the paper describes AI as transforming implementation "from writing to reviewing,
guiding, and verifying" ([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 22). Steering only works if you can see where you are. A short leash means each
increment is a small, self-contained change with a check attached — run the tests,
run the build, read the diff — before the agent is allowed to move on. If the
increment is wrong, it's one step deep and cheap to throw away; if it's right, it
becomes a stable base for the next one. This is the difference between reviewing a
20-line change against a known-good state and reverse-engineering a 600-line change
after the fact.

## Checkpoint cadence

Checkpoints are where the loop closes. A natural cadence is one verifiable unit of
work per checkpoint: implement, verify, and only then continue — never chaining
several unverified steps in the hope they all held. The unit itself comes from
[task decomposition](/oks/agentic-sdlc-best-practices/requirements-and-planning/task-decomposition.md):
cutting the work into agent-sized, independently verifiable pieces up front is what
makes short increments possible during implementation. And pairing each increment
with [TDD as agent guardrail](/oks/agentic-sdlc-best-practices/implementation/tdd-as-agent-guardrail.md)
gives the checkpoint an automated pass/fail bar instead of relying on a human
eyeballing every diff.

## Commit hygiene, linked not restated

A verified increment is a natural commit boundary — small, coherent, and easy to
revert if a later step reveals it was wrong. The mechanics of doing this well
(one logical change per commit, clear messages) are covered in
[atomic commits](/oks/git-best-practices/commits/atomic-commits.md) and are not
repeated here; the point for implementation is only that the checkpoint cadence and
the commit cadence want to be the same rhythm.

# Related

- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)
- [TDD as agent guardrail](/oks/agentic-sdlc-best-practices/implementation/tdd-as-agent-guardrail.md)
- [task decomposition](/oks/agentic-sdlc-best-practices/requirements-and-planning/task-decomposition.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://code.claude.com/docs/en/best-practices
