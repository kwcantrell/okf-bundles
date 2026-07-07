---
type: OKF Concept Index
title: Skills
description: Packaging expertise as Agent Skills that agents discover and load on demand — what they are, their format, placement, and scope.
resource: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
tags:
  - ai-agents
  - skills
  - claude-code
timestamp: 2026-07-07T00:00:00Z
---

# Skills

A skill packages instructions, metadata, and optional scripts into a folder an
agent can discover and load only when a task calls for it. These concepts cover
what a skill is, the `SKILL.md` file format, where skills live on disk, and the
choice between project-shared and personal skills.

## Concepts

- [what is a skill](/oks/ai-agent-repo-structure/skills/what-is-a-skill.md) — filesystem-based, composable, on-demand expertise for an agent.
- [skill file format](/oks/ai-agent-repo-structure/skills/skill-file-format.md) — the `SKILL.md` frontmatter and body, and the three-level progressive-disclosure model.
- [skill placement](/oks/ai-agent-repo-structure/skills/skill-placement.md) — the directory locations and scopes skills load from.
- [project vs personal skills](/oks/ai-agent-repo-structure/skills/project-vs-personal-skills.md) — team-shared skills in the repo versus personal skills in your home directory.
