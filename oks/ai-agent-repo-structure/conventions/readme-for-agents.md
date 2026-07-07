---
type: Repo Convention
title: README for Agents
description: Treating AGENTS.md as a dedicated, predictable README for coding agents — what to put in it and how it differs from README.md.
resource: https://agents.md/
tags:
  - ai-agents
  - agents-md
  - readme
  - conventions
timestamp: 2026-07-07T00:00:00Z
---

# README for Agents

`AGENTS.md` is explicitly described as "a README for agents: a dedicated,
predictable place to provide the context and instructions" for AI coding agents —
distinct from `README.md`, which targets humans. Giving agents their own
predictable file is the core convention: the agent always knows where to look,
and the human README stays uncluttered.

## What goes in it

`AGENTS.md` complements README files by holding the extra, sometimes detailed
context coding agents need: build steps, tests, and conventions that would
otherwise clutter a human-facing README. Suggested sections include a project
overview, build and test commands, code style guidelines, testing instructions,
security considerations, commit message and PR guidelines, and deployment steps.

## No schema to satisfy

`AGENTS.md` has no required fields — it is just standard Markdown, and the agent
simply parses the text you provide rather than following a strict schema. That
low ceremony is deliberate: the value is in writing clear, useful context, not in
conforming to a format. The complementary guidance is to keep `README.md` concise
and focused on human contributors, moving agent-specific build, test, and
convention detail into the separate `AGENTS.md`.

## Making Claude Code read it

Claude Code does not read `AGENTS.md` directly — it reads `CLAUDE.md`. To share
one set of instructions across tools, a `CLAUDE.md` can import `AGENTS.md` with
`@AGENTS.md`, or a symlink can be created with `ln -s AGENTS.md CLAUDE.md`;
alternatively, running `/init` in a repo that already has an `AGENTS.md` causes
Claude Code to read it and incorporate the relevant parts into the generated
`CLAUDE.md`, alongside other tool configs such as `.cursorrules`, `.devin/rules/`,
and `.windsurfrules`. See
[AGENTS.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
for the trade-offs between these approaches.

# Related

- [AGENTS.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
- [docs for agents](/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md)
- [directory layout](/oks/ai-agent-repo-structure/conventions/directory-layout.md)

# Sources

- https://agents.md/
- https://docs.claude.com/en/docs/claude-code/memory
