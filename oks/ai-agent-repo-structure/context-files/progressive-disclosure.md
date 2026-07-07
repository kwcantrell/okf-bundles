---
type: Agent Context File
title: Progressive Disclosure
description: Structuring context so an agent loads lightweight identifiers up front and pulls detail into context only when a task needs it.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - ai-agents
  - progressive-disclosure
  - context-engineering
timestamp: 2026-07-07T00:00:00Z
---

# Progressive Disclosure

Progressive disclosure means agents "incrementally discover relevant context
through exploration," gradually assembling understanding layer by layer rather
than loading all information upfront. Instead of memorizing an entire corpus, an
agent maintains lightweight identifiers — file paths, stored queries, web links
— and uses tools to dynamically load data into context at runtime, mirroring how
humans rely on external organization systems rather than memorizing everything.

## Why it matters for repo structure

How you lay out a repository determines how cheaply an agent can navigate it.
Primitives like glob and grep let Claude navigate its environment and retrieve
additional files just-in-time, so a well-organized tree with predictable names
is itself a form of progressive disclosure. Claude Code applies this strategy for
data analysis: rather than loading full databases into context, the model writes
targeted queries, stores results, and uses Bash commands like `head` and `tail`
to analyze large data volumes without ever loading full data objects.

## The trade-off with CLAUDE.md

Not everything should be disclosed progressively. `CLAUDE.md` files are "naively
dropped into context up front" — every session pays for them regardless of
relevance. That is exactly right for a small set of always-true facts, and wrong
for knowledge that is only relevant sometimes. Best-practice guidance recommends
using [skills](/oks/ai-agent-repo-structure/skills/what-is-a-skill.md) — rather
than `CLAUDE.md` — for domain knowledge or workflows that are only occasionally
relevant, since skills are loaded on demand without bloating every conversation.

## Applying it to skills and reference files

The same principle shapes how skill content is authored. For Agent Skills, only
the `name` and `description` metadata from all skills is pre-loaded into the
system prompt at startup; Claude reads the full `SKILL.md` body only once the
skill becomes relevant, and reads additional bundled files only as needed.
Authoring guidance therefore recommends keeping `SKILL.md` as an overview that
points to detailed materials (like a table of contents), keeping its body under
500 lines, splitting content into separate reference files as it grows, and
keeping file references one level deep so Claude reads complete files rather than
partially previewing deeply nested ones. Reference files longer than 100 lines
should include a table of contents at the top so Claude can see the full scope of
available information even when previewing with partial reads.

# Related

- [AGENTS.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
- [skill file format](/oks/ai-agent-repo-structure/skills/skill-file-format.md)
- [docs for agents](/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md)

# Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- https://www.anthropic.com/engineering/claude-code-best-practices
