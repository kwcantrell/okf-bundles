---
type: Claude Code Workflow
title: Test-Driven Development
description: Write or reproduce a failing test before asking Claude to implement, then have Claude run the suite and iterate until it passes.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - workflows
  - testing
timestamp: 2026-07-07T00:00:00Z
---

# Test-Driven Development

Claude Code's own [best practices](/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md)
guidance centers on giving Claude "a check it can run": a test suite is the
clearest form of that check, because it turns "looks done" into a pass/fail
signal Claude can read and act on without you watching the session.

## Lead with a failing test

For bug fixes, the documented pattern is to describe the symptom and ask for
a reproduction before a fix: "users report that login fails after session
timeout. check the auth flow in src/auth/, especially token refresh. write a
failing test that reproduces the issue, then fix it." Writing the failing
test first pins down what "fixed" means before any implementation code
exists, so Claude (and you) can tell the difference between the bug being
fixed and the test merely being changed to pass.

For new work, the equivalent is supplying verification criteria up front —
naming the test cases a function must satisfy — for example: "write a
validateEmail function. example test cases: user@example.com is true,
invalid is false, user@.com is false. run the tests after implementing." In
the bug-fix case the failing test is written and confirmed to fail before
the fix; in the new-work case the criteria are named up front but the tests
are run only after the implementation exists, to confirm it.

## Run, read, iterate

Once tests exist, Claude Code's documented recipe for a test suite is the
same as for any other check: run it, read the result, and keep iterating
until it passes, rather than asserting success without evidence. The
`common-workflows` test recipe follows this shape directly — identify
untested code, generate scaffolding, add meaningful test cases for edge
conditions, then run the new tests and fix any failures.

## Split writing tests from writing implementation

Because a single session that writes both the tests and the code to satisfy
them can bias the implementation toward whatever the tests happen to check,
Claude Code's guidance on running multiple sessions describes doing the two
halves separately: "have one Claude write tests, then another write code to
pass them." A separate implementing session only sees the tests as a
specification to satisfy, not as code it just authored, which keeps it from
quietly narrowing the implementation to fit known test cases.

# Related

- [tests and checks as guardrails](/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md)
- [explore, plan, implement, commit](/oks/claude-best-practices/workflows/explore-plan-code-commit.md)

# Sources

- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/common-workflows
