---
type: Agent Tooling
title: Slash Commands and Hooks
description: Defining custom slash commands as Markdown files and wiring event hooks in settings JSON to extend and gate an agent's workflow.
resource: https://code.claude.com/docs/en/slash-commands
tags:
  - ai-agents
  - slash-commands
  - hooks
  - tooling
timestamp: 2026-07-07T00:00:00Z
---

# Slash Commands and Hooks

Two more repository-level mechanisms shape what an agent does: custom slash
commands (things *you* trigger) and hooks (things that fire automatically on
events).

## Custom slash commands

Custom slash commands are created as Markdown files in `.claude/commands/`
(project scope) or `~/.claude/commands/` (personal scope); a file at
`.claude/commands/deploy.md` creates the `/deploy` command. These files still work
even though commands have been merged into
[skills](/oks/ai-agent-repo-structure/skills/what-is-a-skill.md) as the current
recommended approach. Command and skill content supports argument substitution via
`$ARGUMENTS` (all arguments as typed), `$ARGUMENTS[N]` / `$N` (individual
positional arguments by 0-based index), and named `$name` substitutions declared
in an `arguments` frontmatter list.

## Hooks fire on events

Hooks are configured in JSON settings files (`~/.claude/settings.json`,
`.claude/settings.json`, or `.claude/settings.local.json`) under a `hooks` key,
nested by event name (for example `PreToolUse`), then by `matcher` (a tool-name
pattern), then by an array of hook handler objects. A `matcher` field can be an
exact tool name, a pipe-separated list (`Edit|Write`), `"*"` / empty / omitted to
match everything, or an unanchored regex for other cases (for example
`mcp__memory__.*` to match all tools from an MCP server named "memory").

## Controlling a tool call from a hook

For `PreToolUse` hooks, exit code `2` blocks the tool call and feeds stderr back
to Claude, while other non-zero exit codes are non-blocking and just show stderr
in the transcript. Exit code `0` lets Claude Code parse stdout as JSON for
fine-grained control — for example `permissionDecision`, `decision`, and
`additionalContext`. Both hooks and MCP servers receive a `CLAUDE_PROJECT_DIR`
environment variable pointing at the project root, so a hook script can reference
project-local paths (for example `${CLAUDE_PROJECT_DIR}/.claude/hooks/validate-rm.sh`)
regardless of the current working directory. Because a hook can *block* an action,
it is the bridge from advisory tooling to
[deterministic enforcement](/oks/ai-agent-repo-structure/practices/determinism-and-reproducibility.md).

# Related

- [MCP and tool config](/oks/ai-agent-repo-structure/tooling/mcp-and-tool-config.md)
- [determinism and reproducibility](/oks/ai-agent-repo-structure/practices/determinism-and-reproducibility.md)
- [project vs personal skills](/oks/ai-agent-repo-structure/skills/project-vs-personal-skills.md)

# Sources

- https://code.claude.com/docs/en/slash-commands
- https://code.claude.com/docs/en/hooks
