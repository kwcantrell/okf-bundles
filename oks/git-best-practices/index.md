---
type: OKF Bundle Index
title: Git Best Practices
description: A cross-linked OKF bundle of primary-sourced Git and GitHub best practices, from the repository model to collaboration workflows.
resource: https://git-scm.com/doc
tags:
  - git
  - github
  - version-control
  - best-practices
timestamp: 2026-07-07T00:00:00Z
---

# Git Best Practices

An [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
bundle covering how Git works and how to use it well. Every concept is grounded
in primary sources (the Git documentation and Pro Git book, GitHub Docs,
Atlassian's official Git tutorials, and the Conventional Commits spec) and links
to related concepts so you can navigate the material as a graph rather than a
flat list.

Start here, pick the area closest to your question, and follow its `index.md`
into the individual concepts. Where more than one valid approach exists (merge
vs. rebase, Git Flow vs. trunk-based development), these notes present the
trade-offs rather than mandating one answer.

## Concept areas

The bundle is organized into ten areas. The first five below are available now;
the remaining five arrive in a later authoring pass.

- [fundamentals](/oks/git-best-practices/fundamentals/index.md) — how Git models data: snapshots, the three states, the staging area, refs, and objects.
- [workflows](/oks/git-best-practices/workflows/index.md) — branching models teams use: GitHub flow, Git Flow, trunk-based development, and the forking workflow.
- [branching](/oks/git-best-practices/branching/index.md) — branch naming, branch protection, merge vs. rebase, and resolving conflicts.
- [commits](/oks/git-best-practices/commits/index.md) — atomic commits, Conventional Commits, commit-message style, and signing commits.
- [collaboration](/oks/git-best-practices/collaboration/index.md) — pull requests, code review, draft PRs, and CODEOWNERS.
- history *(planned)* — rewriting and navigating history: rebasing, interactive rebase, cherry-pick, revert vs. reset, and bisect.
- remote *(planned)* — working with remotes: fetch/pull/push, tracking branches, and tags/releases.
- automation *(planned)* — Git hooks, CI integration, and the pre-commit framework.
- security *(planned)* — secret management, `.gitignore` hygiene, signed tags, and credential storage.
- scale *(planned)* — monorepo vs. polyrepo, Git LFS, and sparse checkout.

## How to read this bundle

Each concept file carries YAML frontmatter (type, title, description, a primary
`resource` URL, tags, and a timestamp), an explanatory body, a `# Related`
section of cross-links, and a `# Sources` section citing the primary
documentation behind its claims.
