---
type: Agent Knowledge Practice
title: Machine-Readable Metadata
description: Using YAML frontmatter as a structured discovery index that agents and query tooling parse before reading any body content.
resource: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
tags:
  - ai-agents
  - metadata
  - frontmatter
  - yaml
timestamp: 2026-07-07T00:00:00Z
---

# Machine-Readable Metadata

Across agent-facing formats, YAML frontmatter plays the same role: a small,
structured block an agent parses to decide what a file is and whether to read it,
distinct from the prose body underneath.

## Frontmatter as a discovery index

Anthropic's documentation states the agent pre-loads the `name` and `description`
of every installed skill into its system prompt at startup, using YAML
frontmatter as a lightweight discovery index before any body content is read. A
Claude Code `SKILL.md` file must begin with YAML frontmatter; only `description`
is recommended, while `name`, `disable-model-invocation`, `allowed-tools`, and
other fields are optional structured metadata that Claude parses to decide when
and how to use the skill.

## The metadata block is parsed separately from the body

The separation is real, not cosmetic: if a `SKILL.md` file's frontmatter YAML is
malformed, Claude Code loads the skill body with empty metadata — so the skill can
still be invoked by name, but Claude has no `description` left to match against.
The frontmatter is a distinct metadata block from the body, and getting it right
is what makes a file discoverable at all.

## Scoping with metadata

Metadata can also scope *when* a file applies. Claude Code project rules use YAML
frontmatter with a `paths` field of glob patterns so a rule file is loaded only
when Claude works with matching files, for example `paths: ["src/api/**/*.ts"]`.

## OKF's minimal contract

OKF takes the same approach with a deliberately small surface: its frontmatter is
YAML with one required field (`type`) and several reserved fields (`title`,
`description`, `resource`, `tags`, `timestamp`) that both agents and query tooling
can read as structured metadata alongside the Markdown body. This
minimally-opinionated design mandates only `type` while leaving all other
structured metadata producer-defined — prioritizing a shared machine-readable
contract over any specific tool or schema. Every concept file in this bundle
follows that contract, which is what lets the
[validator](/oks/ai-agent-repo-structure/knowledge/okf-bundles-in-repos.md) and
future tooling read it mechanically.

# Related

- [skill file format](/oks/ai-agent-repo-structure/skills/skill-file-format.md)
- [OKF bundles in repos](/oks/ai-agent-repo-structure/knowledge/okf-bundles-in-repos.md)
- [naming for discoverability](/oks/ai-agent-repo-structure/conventions/naming-for-discoverability.md)

# Sources

- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://docs.claude.com/en/docs/claude-code/slash-commands
- https://docs.claude.com/en/docs/claude-code/memory
- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
