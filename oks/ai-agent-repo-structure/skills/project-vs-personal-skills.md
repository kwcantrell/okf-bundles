---
type: Agent Skill Concept
title: Project vs Personal Skills
description: Choosing between team-shared project skills committed to the repo and personal skills in your home directory, and how names resolve when they collide.
resource: https://docs.claude.com/en/docs/claude-code/skills
tags:
  - ai-agents
  - skills
  - project
  - personal
timestamp: 2026-07-07T00:00:00Z
---

# Project vs Personal Skills

The same skill format serves two very different purposes depending on where you
put it: shared with a team, or private to you.

## Personal skills

Personal skills live under `~/.claude/skills/<skill-name>/SKILL.md`. The
getting-started example creates one with `mkdir -p ~/.claude/skills/summarize-changes`,
and personal skills are available across all your projects. Because they live only
in your home directory, they never travel with the repository — they are the right
home for your own workflow preferences that no teammate needs.

## Project skills

Project skills live under `.claude/skills/<skill-name>/SKILL.md` and apply to
*this project only*. They are meant to be shared with a team by committing them to
version control — commit `.claude/skills/` alongside the code. This makes a
project skill a natural companion to a
[committed knowledge bundle](/oks/ai-agent-repo-structure/knowledge/okf-bundles-in-repos.md):
both are versioned artifacts that a team reviews and evolves together.

## When names collide

Precedence resolves collisions predictably:

- Across levels, **enterprise overrides personal, and personal overrides
  project**.
- A skill at any of these levels also overrides a bundled skill with the same
  name — for example, a `code-review` skill in your project's `.claude/skills/`
  replaces the bundled `/code-review`.
- **Plugin** skills use a `plugin-name:skill-name` namespace, so they cannot
  conflict with other levels.
- If a skill and a command (from `.claude/commands/`) share the same name, the
  **skill takes precedence**.

The practical guidance: put anything the team depends on in project scope so it is
reviewed and shared, and keep personal-preference skills in personal scope so they
do not surprise teammates — while remembering that a personal skill will shadow a
project skill of the same name on your machine.

# Related

- [skill placement](/oks/ai-agent-repo-structure/skills/skill-placement.md)
- [slash commands and hooks](/oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md)
- [OKF bundles in repos](/oks/ai-agent-repo-structure/knowledge/okf-bundles-in-repos.md)

# Sources

- https://docs.claude.com/en/docs/claude-code/skills
