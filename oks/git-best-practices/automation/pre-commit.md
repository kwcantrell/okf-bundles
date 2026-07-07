---
type: Automation Practice
title: Pre-commit
description: The pre-commit hook inspects the staged snapshot before a commit is created and can abort it — the foundation for automated local quality gates.
resource: https://git-scm.com/docs/githooks
tags:
  - git
  - automation
  - hooks
  - pre-commit
timestamp: 2026-07-07T00:00:00Z
---

# Pre-commit

The `pre-commit` hook is the earliest place to catch problems: it runs on your
own machine, before a bad commit ever exists.

## When it runs and what it can do

The `pre-commit` hook is invoked by `git commit` **before the commit message
editor is shown and before the commit object is created**, which makes it the
right place to inspect the snapshot about to be committed. If the script **exits
with a non-zero status, `git commit` aborts** before creating the commit. It
takes no parameters and runs with `GIT_EDITOR=:` set.

The default sample `pre-commit` hook checks for non-ASCII filenames and trailing
whitespace; the non-ASCII filename check can be disabled by setting the
`hooks.allownonascii` config option to `true`.

## The escape hatch — and its cost

The check can be skipped entirely with `git commit --no-verify`. That is
occasionally necessary, but it means a local `pre-commit` hook is an aid, not a
guarantee: anyone can bypass it. Enforcement that *cannot* be bypassed belongs on
the [server side](/oks/git-best-practices/automation/git-hooks.md) or in
[CI](/oks/git-best-practices/automation/ci-integration.md) as a required check.

## Sharing hooks across a team

Because [hooks](/oks/git-best-practices/automation/git-hooks.md) live in
`.git/hooks`, they are **not copied when a repository is cloned** (though
`git init` templates can populate them in newly created repos). This is why the
popular **pre-commit framework** exists: it stores hook configuration in a file
committed to the repository and installs the actual `.git/hooks` scripts from it,
so every contributor runs the same checks — linters, formatters, and
[secret](/oks/git-best-practices/security/secret-management.md) scanners — without
manual setup.

# Related

- [git hooks](/oks/git-best-practices/automation/git-hooks.md)
- [ci integration](/oks/git-best-practices/automation/ci-integration.md)
- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)
- [gitignore hygiene](/oks/git-best-practices/security/gitignore-hygiene.md)

# Sources

- https://git-scm.com/docs/githooks
