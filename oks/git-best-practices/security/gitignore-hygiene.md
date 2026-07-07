---
type: Security Practice
title: .gitignore Hygiene
description: Use .gitignore and its sibling ignore files to keep generated, local, and sensitive files untracked — and understand why ignoring an already-tracked file needs an extra step.
resource: https://git-scm.com/docs/gitignore
tags:
  - git
  - github
  - security
  - gitignore
timestamp: 2026-07-07T00:00:00Z
---

# .gitignore Hygiene

A `.gitignore` file specifies intentionally untracked files that Git should
ignore. Keeping it disciplined is the first line of defense against committing
build artifacts, local editor cruft, and — most importantly —
[secrets](/oks/git-best-practices/security/secret-management.md).

## How patterns match

Patterns are matched relative to the location of the `.gitignore` file unless
they contain no slash. A few rules to know:

- A **trailing slash** (e.g. `frotz/`) restricts the match to directories only.
- **`**`** matches zero or more directories, so `a/**/b` matches at arbitrary
  depth.
- A **`!` prefix negates** a pattern, re-including a previously excluded file —
  but this **cannot** re-include a file if one of its parent directories is
  already excluded.

Ignore rules are read from multiple sources in precedence order: command-line
patterns, `.gitignore` files in the directory and its parents,
`$GIT_COMMON_DIR/info/exclude`, and the file named by `core.excludesFile`.

## Where different rules belong

- **Shared, project-wide rules** go in the committed `.gitignore`.
- **Machine- or editor-specific files** (personal, not the project's concern)
  belong in the global ignore file at `~/.config/git/ignore`, set via
  `core.excludesFile`.
- **Repository-specific rules you don't want to share** go in
  `.git/info/exclude`, which is never committed.

GitHub maintains an official collection of recommended `.gitignore` templates for
many languages, environments, and operating systems in the `github/gitignore`
repository — a good starting point for any project.

## The already-tracked gotcha

Adding a rule to `.gitignore` **does not stop Git from tracking a file that is
already tracked.** To ignore such a file, first untrack it with
`git rm --cached <file>`, then commit the removal. This is a common trap with
secrets that were committed before an ignore rule was added — and a reminder that
ignoring is not the same as [removing sensitive
data](/oks/git-best-practices/security/secret-management.md).

# Related

- [secret management](/oks/git-best-practices/security/secret-management.md)
- [pre-commit](/oks/git-best-practices/automation/pre-commit.md)
- [the staging area](/oks/git-best-practices/fundamentals/staging-area.md)
- [large files and Git LFS](/oks/git-best-practices/scale/large-files-lfs.md)

# Sources

- https://git-scm.com/docs/gitignore
- https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files
