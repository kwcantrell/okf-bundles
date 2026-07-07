---
type: Agent Context File
title: Precedence and Scope
description: The four scopes context files live at, how Claude Code concatenates them by walking up the tree, and what override actually means.
resource: https://docs.claude.com/en/docs/claude-code/memory
tags:
  - ai-agents
  - precedence
  - scope
  - claude-md
timestamp: 2026-07-07T00:00:00Z
---

# Precedence and Scope

Context files can exist at several scopes at once, and knowing how they combine
is essential to putting an instruction where it will actually take effect.

## The four scopes

`CLAUDE.md` files can live at four scopes, listed broadest to most specific:

- **Managed policy** — organization-wide, e.g. `/etc/claude-code/CLAUDE.md` on
  Linux/WSL.
- **User instructions** — `~/.claude/CLAUDE.md`, personal preferences across all
  projects.
- **Project instructions** — `./CLAUDE.md` or `./.claude/CLAUDE.md`, team-shared
  via source control.
- **Local instructions** — `./CLAUDE.local.md`, personal and gitignored.

## Concatenation, not override

Claude Code reads `CLAUDE.md` files by walking up the directory tree from the
working directory. Discovered files are concatenated — not overriding one another
— ordered from the filesystem root down to the working directory, so instructions
closer to where Claude was launched are read last, and within a directory
`CLAUDE.local.md` is appended after `CLAUDE.md`. Files in the hierarchy *above*
the working directory load in full at launch, but files in subdirectories load on
demand only when Claude reads files in those subdirectories.

A managed policy `CLAUDE.md` (deployed via MDM/Group Policy or a `claudeMd` key
in `managed-settings.json`) applies to every session on the machine, loads before
user and project `CLAUDE.md`, and cannot be excluded by individual settings —
unlike ordinary ancestor `CLAUDE.md` files, which can be skipped in monorepos via
the `claudeMdExcludes` setting.

## Advisory, not enforced

`CLAUDE.md` content is delivered as a user message *after* the system prompt, not
as part of it, and both `CLAUDE.md` and auto memory are treated by Claude as
context rather than enforced configuration. There is no guarantee of strict
compliance, especially for vague or conflicting instructions across files. When
an action must happen every time, prefer a
[deterministic hook](/oks/ai-agent-repo-structure/practices/determinism-and-reproducibility.md)
over an advisory instruction.

## Settings precedence is different

`settings.json` (as distinct from `CLAUDE.md`) *does* use override-based
precedence, applied highest to lowest: Managed > command-line arguments > Local
(`.claude/settings.local.json`) > Project (`.claude/settings.json`) > User
(`~/.claude/settings.json`). Permission rules are a stated exception — rather than
one scope overriding another, permission rules merge across scopes.

## AGENTS.md precedence

For `AGENTS.md`, in nested/monorepo structures the closest file to the edited
file wins, and explicit user chat prompts override everything — which lets each
package in a monorepo ship tailored instructions.

# Related

- [AGENTS.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
- [directory layout](/oks/ai-agent-repo-structure/conventions/directory-layout.md)
- [guardrails and permissions](/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md)

# Sources

- https://docs.claude.com/en/docs/claude-code/memory
- https://docs.claude.com/en/docs/claude-code/settings
- https://agents.md/
