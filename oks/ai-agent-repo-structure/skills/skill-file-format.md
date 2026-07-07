---
type: Agent Skill Concept
title: Skill File Format
description: The SKILL.md file — required YAML frontmatter plus a Markdown body — and the three-level progressive-disclosure model that governs load timing.
resource: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
tags:
  - ai-agents
  - skills
  - skill-md
  - frontmatter
timestamp: 2026-07-07T00:00:00Z
---

# Skill File Format

Every skill needs a `SKILL.md` file with two parts: YAML frontmatter between
`---` markers that tells Claude when to use the skill, and Markdown content with
the instructions Claude follows when the skill runs. The frontmatter is loaded
into the system prompt at startup, so it must begin the file.

## Required frontmatter

The required frontmatter fields are `name` and `description`:

- `name` allows a maximum of 64 characters, only lowercase letters, numbers, and
  hyphens, no XML tags, and cannot contain the reserved words "anthropic" or
  "claude".
- `description` must be non-empty, at most 1024 characters, contain no XML tags,
  and should state both *what* the skill does and *when* Claude should use it.

Claude Code's full frontmatter field set additionally includes optional keys such
as `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`,
`user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`,
`context`, `agent`, `hooks`, `paths`, and `shell` — all optional, though
`description` is recommended.

## Three levels of progressive disclosure

Skill content loads in three levels with different timing and token cost:

- **Level 1 — metadata** (`name`/`description`, ~100 tokens): always loaded at
  startup into the system prompt.
- **Level 2 — the SKILL.md body** (instructions/guidance, under ~5k tokens):
  loaded only when the skill is triggered.
- **Level 3+ — bundled resources and scripts** (effectively unlimited token
  cost): loaded or executed only as needed via bash.

Scripts are especially cheap: when Claude runs a bundled script such as
`validate_form.py`, the script's code never loads into the context window — only
its output consumes tokens — which makes scripts more efficient than generated
code for deterministic work.

## Authoring for the format

Keep `SKILL.md` under 500 lines and move detailed reference material to separate
files. A typical layout is a `pdf-skill/` folder containing `SKILL.md` (main
instructions), supporting guides like `FORMS.md` and `REFERENCE.md`, and a
`scripts/` directory — with `SKILL.md` referencing each supporting file by name so
Claude knows what it contains and reads it only when relevant. This is
[progressive disclosure](/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md)
applied at the file level.

# Related

- [what is a skill](/oks/ai-agent-repo-structure/skills/what-is-a-skill.md)
- [skill placement](/oks/ai-agent-repo-structure/skills/skill-placement.md)
- [machine-readable metadata](/oks/ai-agent-repo-structure/knowledge/machine-readable-metadata.md)

# Sources

- https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- https://docs.claude.com/en/docs/claude-code/skills
