---
type: History Practice
title: Bisect
description: Binary-search commit history to find the commit that introduced a bug, marking commits good or bad — and automate the search with git bisect run.
resource: https://git-scm.com/docs/git-bisect
tags:
  - git
  - history
  - debugging
timestamp: 2026-07-07T00:00:00Z
---

# Bisect

`git bisect` performs a **binary search** through commit history to find, as
quickly as possible, the commit that introduced a bug. You give it a known-bad
commit and a known-good commit as the search boundaries, and it repeatedly checks
out a commit in the middle for you to test.

## The manual workflow

```
git bisect start
git bisect bad            # mark the current (broken) commit
git bisect good <commit>  # mark a known-working commit
```

Git then checks out a commit halfway between the two. Test it, then mark it
`git bisect good` or `git bisect bad`. Git narrows the range and repeats until it
identifies the first bad commit. When finished, `git bisect reset` ends the
session and returns the working tree to the commit that was checked out before
`git bisect start` began.

## Automating it

`git bisect run <cmd> [<args>...]` automates the whole search by running a script
at each step. The script's exit code drives the decision:

- **0** — the commit is good.
- **1–127, excluding 125** — the commit is bad.
- **125** — the commit is untestable; skip it.

Point it at a test that reproduces the bug and Git finds the culprit
unattended — pairing naturally with a
[CI](/oks/git-best-practices/automation/ci-integration.md) test suite.

## Custom terms

When bisecting for something other than a bug (say, a behavior change), replace
"good"/"bad" with your own terms via
`git bisect start --term-old <term> --term-new <term>`, e.g. `old`/`new`.

## Trade-off

Bisect is only as reliable as your good/bad classification: a flaky or
intermittently failing test can send the search down the wrong half. A crisp,
deterministic reproduction is what makes it fast — often locating a regression
across thousands of commits in a handful of steps.

# Related

- [ci integration](/oks/git-best-practices/automation/ci-integration.md)
- [revert vs. reset](/oks/git-best-practices/history/revert-vs-reset.md)
- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md)

# Sources

- https://git-scm.com/docs/git-bisect
