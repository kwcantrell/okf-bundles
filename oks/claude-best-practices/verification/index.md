---
type: OKF Concept Index
title: Verification
description: Closing the loop on Claude Code's work — giving it a check it can run, and getting an independent second opinion before treating changes as done.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - verification
timestamp: 2026-07-07T00:00:00Z
---

# Verification

Claude stops when work "looks done." These concepts cover how to make that
judgment checkable: giving Claude a pass/fail signal it can run itself, and
bringing in a fresh, independent reviewer before counting a change as
finished.

## Concepts

- [tests and checks as guardrails](/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md) — verifiable feedback loops (tests, linters, expected output, screenshots) let Claude self-correct instead of just asserting success.
- [independent review](/oks/claude-best-practices/verification/independent-review.md) — using a fresh subagent or `/code-review` with clean context to review a diff, separating author from reviewer.
