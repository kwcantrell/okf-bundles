---
type: OKF Concept Index
title: Verification And Review
description: When an agent writes the code, verification is the phase that decides whether "looks done" is actually done. This area covers what changes when the author is an agent — tests that the agent can game, evals that measure the harness itself, review economics under high-volume plausible output, adversarial review panels, and the security posture for AI-authored changes.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - verification-and-review
timestamp: 2026-07-07T00:00:00Z
---

# Verification And Review

The paper puts verification at the center of the whole shift: "the single biggest
differentiator between the two ends is how outputs get verified"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 14). When an agent is the author, the dangerous failures are the ones that "look
right" and pass basic tests (p. 34), which means the checks wrapped around generation
have to be stronger, not weaker, than they were for human-written code. This area is
about those checks — and about the specific ways each one bends when the code, and even
the tests, are agent-generated.

## Concepts

- [agent-written tests and reward hacking](/oks/agentic-sdlc-best-practices/verification-and-review/agent-written-tests-and-reward-hacking.md) — when the agent authors the tests that grade it, the suite stops being an independent check; protect the tests and review test diffs so a green checkmark still means something.
- [evals for agentic changes](/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md) — task-level evals on your own codebase become the harness's regression suite, turning "the agent feels better" into a measured number (the +13.7-point case was measured, not vibes).
- [reviewing AI-generated code](/oks/agentic-sdlc-best-practices/verification-and-review/reviewing-ai-generated-code.md) — what changes when the author is an agent: volume, plausible-but-wrong output, and reviewer attention as the scarce resource; AI triages the first pass, humans keep the judgment calls.
- [adversarial multi-agent review](/oks/agentic-sdlc-best-practices/verification-and-review/adversarial-multi-agent-review.md) — a panel of skeptical reviewers with distinct mandates, plus a verification pass over their findings, because diverse lenses cover different failure modes while redundant clones repeat the same blind spots.
- [securing agent-generated code](/oks/agentic-sdlc-best-practices/verification-and-review/securing-agent-generated-code.md) — layered guardrails, dependency and injection review, provenance of what the agent pulled in, and a hard human gate on anything security-sensitive.
