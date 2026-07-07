---
type: Repo Convention
title: Directory Layout
description: Where context files, skills, and rules sit in the tree so agents read the nearest instructions — including monorepo layouts.
resource: https://agents.md/
tags:
  - ai-agents
  - directory-layout
  - monorepo
  - conventions
timestamp: 2026-07-07T00:00:00Z
---

# Directory Layout

Agents find context by location, so the layout of a repository is part of its
interface. A few conventions place each kind of file where the agent expects it.

## Context files at the root and per package

`AGENTS.md` should be created at the root of the repository. For monorepos, place
another `AGENTS.md` inside each package; agents automatically read the nearest
file in the directory tree, with the closest one taking precedence. `CLAUDE.md`
follows the same broad-to-narrow layering across managed policy
(`/etc/claude-code/CLAUDE.md`), user (`~/.claude/CLAUDE.md`), project
(`./CLAUDE.md` or `./.claude/CLAUDE.md`), and local (`./CLAUDE.local.md`) scopes.

## Rules as one topic per file

For larger projects, instructions can be organized into a `.claude/rules/`
directory with one topic per file (for example `testing.md`, `api-design.md`).
All `.md` files there are discovered recursively, including subdirectories such
as `frontend/` or `backend/`. This keeps each concern small and independently
loadable rather than piling everything into one long context file.

## Skills across scopes and nesting

Skills live in per-scope directory layouts: personal
(`~/.claude/skills/<skill-name>/SKILL.md`), project
(`.claude/skills/<skill-name>/SKILL.md`), plugin
(`<plugin>/skills/<skill-name>/SKILL.md`), and enterprise (via managed settings).
Skills also load from nested `.claude/skills/` directories below the working
directory, so a monorepo package such as `packages/frontend/.claude/skills/` can
provide its own skills that apply when working on that package. See
[skill placement](/oks/ai-agent-repo-structure/skills/skill-placement.md) for the
full resolution rules.

## Knowledge as a directory hierarchy

Curated knowledge follows the same file-per-unit shape. OKF bundles organize
concepts as a directory hierarchy of Markdown files — one file per concept — with
optional `index.md` files for progressive disclosure and optional `log.md` files
for chronological change history (for example `sales/datasets/index.md`,
`sales/tables/orders.md`). This bundle is itself laid out that way.

# Related

- [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md)
- [naming for discoverability](/oks/ai-agent-repo-structure/conventions/naming-for-discoverability.md)
- [OKF bundles in repos](/oks/ai-agent-repo-structure/knowledge/okf-bundles-in-repos.md)

# Sources

- https://agents.md/
- https://docs.claude.com/en/docs/claude-code/memory
- https://docs.claude.com/en/docs/claude-code/slash-commands
- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
