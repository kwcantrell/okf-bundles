---
type: Agentic SDLC Practice
title: Agents In CI/CD
description: Putting agents to work inside the pipeline — automated fixes, PR-review bots, and headless runs triggered on events — while keeping CI as the source of truth and never letting the agent own the gate that approves its own merge.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - operations-and-evolution
timestamp: 2026-07-07T00:00:00Z
---

# Agents In CI/CD

Once an agent can run without an interactive session, the pipeline is a natural
place to put it. The paper describes deployment pipelines becoming "AI-aware," with
agents that "monitor deployment health, automatically roll back problematic releases,
and predict deployment risks based on the nature and scope of changes"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 23). Earlier in the lifecycle, the same non-interactive capability shows up as an
agent acting as a first-pass reviewer that flags "potential bugs, style violations,
security vulnerabilities, and performance issues before a human reviewer sees the
code" (p. 23). In practice these become pipeline citizens: a bot that opens a PR with
a proposed fix, a job that comments review findings, a headless run triggered on a
push or a failing check.

## CI stays the source of truth

The critical design rule is that adding an agent to the pipeline does not change what
the pipeline is *for*. CI remains the deterministic, replayable authority on whether a
change is allowed to ship — the tests, the build, the security scan. The agent is
another producer of candidate changes and another source of advisory signal, not a
replacement for the gate. This is the same reason the paper insists that a fluent
output which skipped its verification steps is "a more dangerous failure than one with
a visible error" (p. 22): when the author is an agent, the automated checks wrapped
around its output have to be stronger, not weaker.

## Never let the agent own its own merge gate

The failure mode to design against is an agent that both writes a change and controls
whether that change merges. That collapses the independence the check depends on — it
is the pipeline version of letting the agent grade its own work, the same problem that
makes agent-authored test suites untrustworthy when the agent can edit them (see
[agent-written tests and reward hacking](/oks/agentic-sdlc-best-practices/verification-and-review/agent-written-tests-and-reward-hacking.md)).
Keep the merge decision on the far side of a check the agent cannot rewrite: a
required human approval, a protected branch, or a status gate whose configuration the
agent has no write access to. The deterministic hooks the harness runs — for example,
"blocking a commit if the agent tries to push a hard-coded password" (p. 30) — belong
here too: they are guardrails the agent runs *into*, not switches it can flip. Which
gates stay human as autonomy rises is its own decision; see
[human-in-the-loop checkpoints](/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md).

# Related

- [ci and github actions](/oks/claude-best-practices/automation/ci-and-github-actions.md)
- [headless mode](/oks/claude-best-practices/automation/headless-mode.md)
- [agent-written tests and reward hacking](/oks/agentic-sdlc-best-practices/verification-and-review/agent-written-tests-and-reward-hacking.md)
- [human-in-the-loop checkpoints](/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md)
- [safety](/oks/claude-best-practices/safety/index.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
