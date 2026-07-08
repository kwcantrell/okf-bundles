---
type: Claude Code Workflow
title: Iterating On Visual Targets
description: Give Claude a screenshot or mock as the target, have it implement, then screenshot its own result and compare so the diff — not a description — drives the next iteration.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - workflows
  - frontend
timestamp: 2026-07-07T00:00:00Z
---

# Iterating On Visual Targets

A vague request like "make the dashboard look better" gives Claude no way to
know when it's done. Claude Code's documented fix is to turn a visual result
into a check the same way a test suite checks code: paste a screenshot of the
target design and ask Claude to compare its own output against it.

## Provide the mock, then close the loop

The documented pattern is: "\[paste screenshot] implement this design. take a
screenshot of the result and compare it to the original. list differences and
fix them." This is the same "give Claude a way to verify its work" principle
applied to UI — a
[test suite, a build, or a screenshot diff](/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md)
are all checks that let Claude read a pass/fail signal and iterate instead of
asserting the work looks done. A browser screenshot compared against a design
is explicitly listed alongside tests and linters as this kind of check.

## Getting the mock and the result in front of Claude

Images can reach the conversation by dragging and dropping them into the
terminal, pasting with `Ctrl+V`, or giving Claude a file path directly — see
[referencing files, urls, and images](/oks/claude-best-practices/context/referencing-files-urls-images.md).
Claude can use a design mock to generate the CSS or HTML structure to match
it, and separately, when Claude is connected to a browser, it can open the
running page itself, take a screenshot, and verify that a built UI matches
the source design — described as "design verification" in Claude Code's
Chrome integration.

## Why the diff matters more than the description

Comparing screenshots gives Claude a concrete list of differences to close
(spacing, color, alignment) rather than an open-ended aesthetic judgment,
which is the same reason a failing test is more useful than "the code doesn't
work." Each round of implement, screenshot, compare, and fix narrows the gap
between the two images directly.

# Related

- [referencing files, urls, and images](/oks/claude-best-practices/context/referencing-files-urls-images.md)
- [explore, plan, implement, commit](/oks/claude-best-practices/workflows/explore-plan-code-commit.md)

# Sources

- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/common-workflows
- https://code.claude.com/docs/en/chrome
