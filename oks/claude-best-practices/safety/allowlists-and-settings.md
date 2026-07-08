---
type: Claude Code Practice
title: Allowlists and Settings
description: Tuning which tools and commands Claude Code runs without prompting via /permissions and settings.json allow/deny rules.
resource: https://code.claude.com/docs/en/permissions
tags:
  - claude-code
  - safety
  - permissions
  - settings
timestamp: 2026-07-07T00:00:00Z
---

# Allowlists and Settings

Beyond picking a permission mode, Claude Code lets you tune permissions at the
level of individual tools and commands using rules stored in `settings.json`
and managed through the `/permissions` command. `/permissions` opens a UI
that lists every active allow, ask, and deny rule and which settings file each
one comes from.

Rules take the form `Tool` or `Tool(specifier)` — for example
`Bash(npm run test *)`, `Read(./.env)`, or `WebFetch(domain:example.com)`.
**Allow** rules let a matching call run without a prompt; **ask** rules force
a prompt every time; **deny** rules block the call outright. Rules are
evaluated in a fixed order — deny, then ask, then allow — and the first match
wins regardless of how specific a competing rule is, so a broad deny like
`Bash(git push *)` cannot be carved around by a narrower allow rule.
Permission rules are enforced by Claude Code itself, not by the model:
instructions in a prompt or CLAUDE.md shape what Claude attempts, but only
`/permissions` rules, a permission mode, or a `PreToolUse` hook change what
Claude Code actually allows.

Settings live in a layered hierarchy. `.claude/settings.json` is project
settings, checked into git and shared with the team; `.claude/settings.local.json`
is local, gitignored, personal overrides for one project; `~/.claude/settings.json`
is user settings applying across all projects; and managed settings
(deployed by an organization) sit above all of them and cannot be overridden.
Permission rules are unusual among settings in that they *merge* across
scopes rather than the highest-precedence scope simply winning — rules from
managed, project, local, and user settings all combine, with deny always
taking priority. Project-level allow rules only take effect once you accept
Claude Code's workspace trust dialog for that folder, so a malicious
repository can't silently grant itself permissions just by being checked out.

# Related

- [permission modes](/oks/claude-best-practices/safety/permission-modes.md)
- [guardrails and permissions](/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md)

# Sources

- https://code.claude.com/docs/en/permissions
