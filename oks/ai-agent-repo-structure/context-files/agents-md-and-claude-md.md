---
type: Agent Context File
title: AGENTS.md and CLAUDE.md
description: The two context-file conventions agents read for project instructions, and how to make both read the same source without duplication.
resource: https://agents.md/
tags:
  - ai-agents
  - agents-md
  - claude-md
  - context-files
timestamp: 2026-07-07T00:00:00Z
---

# AGENTS.md and CLAUDE.md

A context file is a plain-Markdown file that tells a coding agent how a project
works — the build steps, tests, and conventions that would clutter a
human-facing README. Two conventions dominate, and a repository can serve both
from a single source of truth.

## AGENTS.md — the cross-tool convention

`AGENTS.md` is a simple, open format for guiding coding agents, adopted by over
60,000 open-source projects. It complements `README.md` by holding the extra,
sometimes detailed context coding agents need — build steps, tests, and
conventions. It is *just* standard Markdown with no required fields or fixed
headings; the agent simply parses whatever text you provide.

The format is stewarded by the Agentic AI Foundation under the Linux Foundation
and is supported across many agents and tools, including those from OpenAI,
Google, Cognition, UiPath, JetBrains, VS Code, Cursor, and GitHub Copilot. That
breadth is the reason to reach for it: one file, read by most of the ecosystem.

## CLAUDE.md — what Claude Code reads

Claude Code reads `CLAUDE.md`, not `AGENTS.md`. `CLAUDE.md` files are Markdown
files that give Claude persistent instructions for a project, a personal
workflow, or an entire organization, and Claude reads them at the start of every
session.

## Serving both from one file

If a repo already has an `AGENTS.md`, the recommended approach is to create a
`CLAUDE.md` that imports it with the `@AGENTS.md` syntax — optionally appending
Claude-specific instructions below the import — so both tools read the same
instructions without duplication. A plain symlink (`ln -s AGENTS.md CLAUDE.md`)
also works when no Claude-specific content is needed, though on Windows this
requires Administrator privileges or Developer Mode, which is why the
`@AGENTS.md` import is usually preferred.

The trade-off is small but real: the import lets you add a Claude-only section;
the symlink guarantees the two files can never drift because they are literally
the same file. Choose the import when you need Claude-specific nuance, the
symlink when you want strict single-sourcing.

Running `/init` in a repository that already has an `AGENTS.md` reads it and
incorporates the relevant parts into the generated `CLAUDE.md`; `/init` also
reads other tool configs such as `.cursorrules`, `.devin/rules/`, and
`.windsurfrules`.

# Related

- [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md)
- [README for agents](/oks/ai-agent-repo-structure/conventions/readme-for-agents.md)
- [directory layout](/oks/ai-agent-repo-structure/conventions/directory-layout.md)

# Sources

- https://agents.md/
- https://docs.claude.com/en/docs/claude-code/memory
