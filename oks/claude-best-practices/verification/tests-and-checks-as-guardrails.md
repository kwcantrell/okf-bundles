---
type: Claude Code Practice
title: Tests And Checks As Guardrails
description: Give Claude a check it can run — a test suite, build, linter, or screenshot diff — so it can verify its own work instead of just declaring it done.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - verification
  - testing
timestamp: 2026-07-07T00:00:00Z
---

# Tests And Checks As Guardrails

Claude stops when the work "looks done." Without a check it can run itself,
that impression is the only signal available, and a human becomes the
verification loop — every mistake waits for someone to notice it. Giving
Claude something that returns a pass/fail result closes the loop: Claude does
the work, runs the check, reads the result, and iterates until the check
passes.

A check is anything that produces a signal Claude can read in the
conversation: a test suite, a build's exit code, a linter, a script that
diffs output against a fixture, or a screenshot compared against a design.
The practical difference shows up in how a task is phrased. Instead of
"implement a function that validates email addresses," specify verification
criteria directly: "write a validateEmail function. example test cases:
user@example.com is true, invalid is false, user@.com is false. run the
tests after implementing." The same pattern applies to UI work — pasting a
screenshot and asking Claude to compare its result against it and list
differences — and to bug fixes, where pasting the actual error and asking
Claude to verify the fix (rather than just asserting the build passes)
targets the root cause instead of a symptom.

Once a check exists, it can gate a session with varying strength: run and
iterate on it within a single prompt, use a `/goal` condition that a
separate evaluator re-checks after every turn, use a Stop hook that blocks
the turn from ending until a script passes, or route the result through a
verification subagent that has a fresh model try to refute the finding
before it counts as done. Whichever gate is used, having Claude show
evidence — test output, the command it ran and what it returned, or a
screenshot — rather than merely asserting success is faster to review than
re-running the verification independently, and it works even for sessions
that ran unattended.

# Related

- [independent review](/oks/claude-best-practices/verification/independent-review.md)
- [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)

# Sources

- https://code.claude.com/docs/en/best-practices
