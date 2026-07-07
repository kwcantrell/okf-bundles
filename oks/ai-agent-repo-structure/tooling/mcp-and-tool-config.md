---
type: Agent Tooling
title: MCP and Tool Config
description: Configuring MCP servers via a committed .mcp.json, the three installation scopes, environment-variable expansion, and trust prompts.
resource: https://code.claude.com/docs/en/mcp
tags:
  - ai-agents
  - mcp
  - tooling
  - configuration
timestamp: 2026-07-07T00:00:00Z
---

# MCP and Tool Config

The Model Context Protocol (MCP) is how an agent reaches external tools. Wiring
those tools into a repository is a configuration task, and doing it as committed
config lets a whole team share the same capabilities.

## The .mcp.json file and its scopes

MCP servers are configured in a `.mcp.json` file at the project root, using a
`mcpServers` object; this file is designed to be checked into version control so
all team members share the same tools. Claude Code supports three MCP installation
scopes:

- **local** (default) — stored in `~/.claude.json`, private to the current
  project.
- **project** — stored in `.mcp.json`, shared via version control.
- **user** — stored in `~/.claude.json`, private but available across all your
  projects.

Committing the project scope is what turns "the tools I set up" into "the tools
the team has."

## Portable configuration

`.mcp.json` supports environment-variable expansion with `${VAR}` and
`${VAR:-default}` syntax in the `command`, `args`, `env`, `url`, and `headers`
fields — so a committed config can reference machine-specific values without
hardcoding them. If a required variable has no default and is not set, Claude Code
fails to parse the config. A per-server tool execution timeout can be set with a
`timeout` field in milliseconds (for example `"timeout": 600000` for ten minutes),
overriding the `MCP_TOOL_TIMEOUT` environment variable for that server only.

## Trust before connecting

Because a committed `.mcp.json` can bring in servers written by anyone, Claude
Code treats them cautiously. It displays a warning before connecting to any MCP
server and advises users to verify they trust it, since servers that fetch
external content can expose users to prompt-injection risk. For project-scoped
servers loaded from a committed `.mcp.json`, Claude Code prompts for approval
before use, and `claude mcp list` / `claude mcp get` show them as "Pending
approval" until the workspace is trusted. Treating tool config as
[a guardrail surface](/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md),
not just plumbing, is the right posture.

# Related

- [slash commands and hooks](/oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md)
- [guardrails and permissions](/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md)
- [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md)

# Sources

- https://code.claude.com/docs/en/mcp
