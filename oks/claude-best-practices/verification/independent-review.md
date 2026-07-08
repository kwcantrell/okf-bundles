---
type: Claude Code Practice
title: Independent Review
description: Have a fresh subagent with clean context review a diff, since a reviewer that did not write the code evaluates it on its own terms rather than defending prior reasoning.
resource: https://code.claude.com/docs/en/sub-agents
tags:
  - claude-code
  - verification
  - code-review
timestamp: 2026-07-07T00:00:00Z
---

# Independent Review

The longer Claude works unattended, the more an independent check matters
before the work counts as done. A reviewer running in a fresh subagent
context sees only the diff and the criteria it is given, not the reasoning
that produced the change, so it evaluates the result on its own terms
instead of being biased toward code it just wrote. Subagents run in their
own context window with their own system prompt and tool access, so
delegating review to one keeps the reviewer's judgment separate from the
implementer's assumptions.

For a general correctness check, the bundled `/code-review` skill reviews
the current diff for bugs in a fresh subagent and returns findings to the
session. To check a diff against a specific plan instead, write the review
prompt directly, naming the work to check, the plan to check it against, and
what counts as a finding — for example: "Use a subagent to review the rate
limiter diff against PLAN.md. Check that every requirement is implemented,
the listed edge cases have tests, and nothing outside the task's scope
changed. Report gaps, not style preferences." Because the reviewer runs as a
subagent, the implementing session receives the gaps directly and can fix
and re-review without anyone copying findings between windows.

The same separation extends to defining a standing subagent for this role.
A `code-reviewer` subagent can be configured with a `description` such as
"Expert code reviewer. Use proactively after code changes," restricted
`tools` (for example `Read, Grep, Glob, Bash`) and a system prompt directing
it to focus on code quality, security, and best practices. Claude delegates
to it automatically when a task matches that description, or it can be
invoked explicitly, such as "Have the code-reviewer subagent look at my
recent changes." A reviewer prompted to find gaps will usually report some
even when the work is sound, since that is what it was asked to do —
chasing every finding risks over-engineering, so only gaps affecting
correctness or stated requirements should be treated as blocking.

# Related

- [tests and checks as guardrails](/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md)

# Sources

- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/best-practices
