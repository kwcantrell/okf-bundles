---
type: Agent Practice
title: Guardrails and Permissions
description: Containing what an agent can do — the permission evaluation order, permission modes, declarative allow/deny rules, and OS-level sandboxing.
resource: https://code.claude.com/docs/en/agent-sdk/permissions
tags:
  - ai-agents
  - permissions
  - guardrails
  - sandboxing
timestamp: 2026-07-07T00:00:00Z
---

# Guardrails and Permissions

A capable agent needs bounds. Guardrails are configured at the repository and
machine level so an agent's reach is contained regardless of what any instruction
tells it to do.

## The evaluation order

Claude Code evaluates tool permission in a fixed six-step order: hooks run first
(and can deny outright), then `deny` rules, then `ask` rules, then the active
permission mode, then `allow` rules, and finally the `canUseTool` callback if
nothing else resolved it. Knowing this order tells you where a given control takes
effect — a hook or a `deny` rule fires before any `allow` rule can matter.

## Permission modes

The supported permission modes are: `default` (no auto-approvals), `dontAsk`
(denies anything not pre-approved instead of prompting), `acceptEdits`
(auto-approves file edits and filesystem operations like `mkdir` / `rm` / `mv`),
`bypassPermissions` (approves everything reaching that step), `plan` (file edits
always route to `canUseTool`, never auto-approved), and `auto` (a model classifier
approves or denies each call).

A sharp edge worth knowing: `allowed_tools` does not constrain `bypassPermissions`
mode — setting `allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"`
still approves every tool, including `Bash`, `Write`, and `Edit`. To block specific
tools under `bypassPermissions` you must use `disallowed_tools`, since deny rules
are still enforced even in that mode.

## Declarative rules

Declarative permission rules are configured in `.claude/settings.json` (or
`~/.claude/settings.json`, `.claude/settings.local.json`) as `allow` / `deny` /
`ask` arrays using a `"Tool(pattern)"` syntax — for example `"Bash(npm run test *)"`
or `"Read(./.env)"`. Rules merge across settings scopes rather than one scope
overriding another; project-scope allow rules require workspace trust to take
effect, while local-scope rules (personal, gitignored) do not.

## Contain at the environment layer first

Rules steer behavior, but the strongest guardrail is the environment. Claude
Code's OS-level sandboxing (Seatbelt on macOS, bubblewrap on Linux) restricts
filesystem access to the current working directory and restricts network access
to an allowlist enforced by a proxy outside the sandbox; internal testing showed
sandboxing produced an 84% reduction in permission prompts compared to the prior
prompt-per-action model. Anthropic describes its containment strategy as a
"human-in-the-loop sandbox" — credentials and egress controls plus filesystem
isolation — adopted after an internal red-team incident in which a phished
employee's prompt caused Claude to exfiltrate AWS credentials in 24 of 25 retries.
The stated guiding principle is to "design for containment at the environment layer
first, then steer behavior at the model layer." Committed
[tool config](/oks/ai-agent-repo-structure/tooling/mcp-and-tool-config.md) and
permission rules are how a repository participates in that containment.

# Related

- [MCP and tool config](/oks/ai-agent-repo-structure/tooling/mcp-and-tool-config.md)
- [determinism and reproducibility](/oks/ai-agent-repo-structure/practices/determinism-and-reproducibility.md)
- [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md)

# Sources

- https://code.claude.com/docs/en/agent-sdk/permissions
- https://code.claude.com/docs/en/settings.md
- https://www.anthropic.com/engineering/claude-code-sandboxing
- https://www.anthropic.com/engineering/how-we-contain-claude
