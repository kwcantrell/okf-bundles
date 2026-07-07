---
type: Branching Practice
title: Branch Naming Conventions
description: What characters Git and GitHub allow in branch names, and how to name branches so collaborators and tooling can read them at a glance.
resource: https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names
tags:
  - git
  - github
  - branching
  - naming
timestamp: 2026-07-07T00:00:00Z
---

# Branch Naming Conventions

A branch is just a [ref](/oks/git-best-practices/fundamentals/refs-and-objects.md) —
a named pointer to a commit — so Git is fairly permissive about what you may call
one. That freedom is exactly why a team convention helps: readable, predictable
names let both collaborators and tooling understand a branch at a glance.

## What Git and GitHub allow

Git itself has very few restrictions on branch names. The main hard rules are
that a name may not start or end with a slash, and may not contain consecutive
slashes. Every proposed name must also pass all the checks defined by
`git-check-ref-format`, which is what ultimately governs the allowed character
set.

In practice, keep to **safe characters**: the English alphabet, numbers, and a
limited set of punctuation — period, hyphen, underscore, and forward slash.
A few additional cautions:

- **Start the name with a letter.** This helps avoid confusion (for example,
  with option flags or numeric refs).
- **Avoid shell metacharacters** such as `$` and `;`. Shells interpret them
  specially — `$` expands variables and `;` separates commands — so they require
  escaping or quoting and cause avoidable friction on the command line.
- GitHub additionally **blocks names that resemble Git object IDs** (40
  hexadecimal characters), to avoid confusion with commit hashes, and blocks
  names beginning with `refs/`.

## Naming for humans

Beyond legality, a good convention communicates intent. The forward slash is
allowed specifically because it reads as a hierarchy, so many teams adopt a
`category/short-description` shape — for example `feature/user-login`,
`fix/null-pointer`, or `docs/api-guide`. GitHub flow's advice generalizes this:
give a branch a **short, descriptive name** so collaborators can see ongoing work
at a glance. If you gate branches by pattern (see
[branch protection](/oks/git-best-practices/branching/branch-protection.md),
which can match names with `fnmatch` patterns like `*release*`), a consistent
prefix scheme is what makes those rules possible.

There is no single mandated scheme — pick one the whole team follows and encode
it where people will see it (a CONTRIBUTING file or repository settings).

# Related

- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)
- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)
- [GitHub flow](/oks/git-best-practices/workflows/github-flow.md)

# Sources

- https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names
- https://git-scm.com/docs/git-branch
