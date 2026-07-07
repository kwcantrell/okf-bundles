---
type: Agent Knowledge Practice
title: Docs for Agents
description: Writing documentation that serves an agent audience — concise, well-structured, and loaded at the right time — often from the same file humans read.
resource: https://docs.claude.com/en/docs/claude-code/memory
tags:
  - ai-agents
  - documentation
  - knowledge
timestamp: 2026-07-07T00:00:00Z
---

# Docs for Agents

Documentation an agent reads has different constraints from documentation a human
reads, because every token an agent loads competes for a finite context budget.
A few source-backed guidelines shape how to write it.

## Concise and well-structured beats exhaustive

`CLAUDE.md` content is delivered as a user message after the system prompt, not as
part of it, so specific, concise, well-structured writing directly affects how
reliably an agent follows it. Documentation guidance recommends targeting under
200 lines per `CLAUDE.md` file, because longer files consume more context and
reduce adherence. The AGENTS.md guidance points the same direction from the other
side: keep READMEs concise and focused on human contributors while moving
agent-specific build, test, and convention detail into the separate `AGENTS.md`.

## Load reference material only when needed

A Claude Code skill's Markdown body loads only when it is used, so long reference
material costs almost nothing until you need it; the docs recommend keeping
`SKILL.md` under 500 lines and moving detailed reference into separate supporting
files. This is one instance of the broader three-level progressive-disclosure
pattern for agent-facing docs: skill metadata (name/description) loaded into the
system prompt at startup, full `SKILL.md` content loaded only when relevant, and
supplementary files loaded on demand. Write the always-loaded layer tight, and
let depth live in files that load just-in-time — see
[progressive disclosure](/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md).

## One file, two audiences

Documentation does not always need a separate agent edition. OKF documents are
designed to serve both audiences from the same file: agents parse the directory,
read YAML frontmatter, follow Markdown links, and update files, while humans
browse in any text editor, view on GitHub, or use static visualizers — no
separate translation layer required. That dual-audience design is a practical
goal for any repo documentation: write once, readable by both.

# Related

- [progressive disclosure](/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md)
- [README for agents](/oks/ai-agent-repo-structure/conventions/readme-for-agents.md)
- [OKF bundles in repos](/oks/ai-agent-repo-structure/knowledge/okf-bundles-in-repos.md)

# Sources

- https://docs.claude.com/en/docs/claude-code/memory
- https://agents.md/
- https://docs.claude.com/en/docs/claude-code/slash-commands
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
