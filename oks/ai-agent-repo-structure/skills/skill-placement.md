---
type: Agent Skill Concept
title: Skill Placement
description: The directory locations skills load from — personal, project, plugin, enterprise — and how nested and symlinked skills resolve.
resource: https://docs.claude.com/en/docs/claude-code/skills
tags:
  - ai-agents
  - skills
  - placement
  - monorepo
timestamp: 2026-07-07T00:00:00Z
---

# Skill Placement

Where a `SKILL.md` folder lives determines who can use it and when it loads.

## The four locations

Claude Code loads skills from four locations, each with its own scope:

- **Enterprise** — via managed settings; available to all users in the
  organization.
- **Personal** — `~/.claude/skills/<skill-name>/SKILL.md`; available across all
  your projects.
- **Project** — `.claude/skills/<skill-name>/SKILL.md`; this project only.
- **Plugin** — `<plugin>/skills/<skill-name>/SKILL.md`; available wherever the
  plugin is enabled.

## Walking up and down the tree

Project skills load from `.claude/skills/` in your starting directory and in
every parent directory up to the repository root, so starting Claude in a
subdirectory still picks up skills defined at the root. Skills also load from
nested `.claude/skills/` directories *below* your working directory — for
example, skills in `packages/frontend/.claude/skills/` become available when
editing files there, which supports monorepo setups. A nested skill sharing a
name with another appears under a directory-qualified name like `apps/web:deploy`
so both stay invocable.

## Symlinks and live reloading

A `<skill-name>` entry in the enterprise, personal, or project locations can be a
symlink to a directory elsewhere on disk; Claude Code follows the symlink, and if
the same target is reachable from more than one location, it loads the skill
once. Claude Code also watches skill directories for live changes: adding,
editing, or removing a skill under `~/.claude/skills/`, project `.claude/skills/`,
or a `.claude/skills/` inside an `--add-dir` directory takes effect within the
current session without restarting — but creating a brand-new top-level skills
directory requires a restart.

## The --add-dir exception

The `--add-dir` flag (and `/add-dir` command) is an exception to its normal
"grant file access only" behavior: a `.claude/skills/` within an added directory
is loaded automatically. By contrast, `permissions.additionalDirectories` in
`settings.json` grants file access only and does not load skills.

## Skills do not sync across surfaces

Sharing scope differs by surface. Custom skills do not sync: skills uploaded to
claude.ai must be separately uploaded to the API, and Claude Code skills are
filesystem-based and separate from both. In Claude Code specifically, skills are
personal (`~/.claude/skills/`) or project-based (`.claude/skills/`) and can also
be shared via Claude Code Plugins.

# Related

- [project vs personal skills](/oks/ai-agent-repo-structure/skills/project-vs-personal-skills.md)
- [directory layout](/oks/ai-agent-repo-structure/conventions/directory-layout.md)
- [what is a skill](/oks/ai-agent-repo-structure/skills/what-is-a-skill.md)

# Sources

- https://docs.claude.com/en/docs/claude-code/skills
- https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
