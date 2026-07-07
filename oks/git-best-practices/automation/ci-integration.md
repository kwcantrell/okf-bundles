---
type: Automation Practice
title: CI Integration
description: Run builds and tests automatically on repository events using GitHub Actions workflows defined as YAML in .github/workflows.
resource: https://docs.github.com/en/actions/writing-workflows/about-workflows
tags:
  - git
  - github
  - automation
  - ci
timestamp: 2026-07-07T00:00:00Z
---

# CI Integration

Continuous integration runs your build and tests automatically whenever the
repository changes, catching problems before they reach the default branch. On
GitHub, this is done with **GitHub Actions workflows**.

## Anatomy of a workflow

A workflow is a configurable automated process made up of one or more **jobs**,
defined in a **YAML file** placed in the **`.github/workflows`** directory at the
root of the repository. When a triggering event occurs, GitHub scans that
directory and runs every workflow whose trigger conditions match.

- Each **job** runs on a runner machine and consists of one or more **steps**.
- Each **step** either runs a script or invokes an **action** — a reusable unit
  of automation.

## Triggering workflows

Workflows are triggered via the **`on`** key in the YAML. Triggers include:

- events within the repository (e.g. a push or a
  [pull request](/oks/git-best-practices/collaboration/pull-requests.md)),
- external events via `repository_dispatch`,
- a defined **schedule**, or
- **manual** invocation.

## Where CI fits

CI is the automated half of quality control. Wiring test results into
[branch protection](/oks/git-best-practices/branching/branch-protection.md) as
**required status checks** turns a passing build into a merge precondition — the
mechanism that makes [trunk-based
development](/oks/git-best-practices/workflows/trunk-based-development.md) safe at
speed, since automated tests provide a layer of preemptive review. CI is also the
natural place to run [secret scanning](/oks/git-best-practices/security/secret-management.md)
and the same checks a local [pre-commit](/oks/git-best-practices/automation/pre-commit.md)
hook runs, so nothing depends on every developer remembering to run them.

# Related

- [git hooks](/oks/git-best-practices/automation/git-hooks.md)
- [pre-commit](/oks/git-best-practices/automation/pre-commit.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)
- [trunk-based development](/oks/git-best-practices/workflows/trunk-based-development.md)

# Sources

- https://docs.github.com/en/actions/writing-workflows/about-workflows
