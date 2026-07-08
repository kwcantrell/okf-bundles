---
type: Claude Code Practice
title: Permission Modes
description: Choosing the permission mode that fits the risk of a session — from reviewing every action to skipping checks entirely.
resource: https://code.claude.com/docs/en/permission-modes
tags:
  - claude-code
  - safety
  - permissions
timestamp: 2026-07-07T00:00:00Z
---

# Permission Modes

When Claude wants to edit a file, run a shell command, or make a network
request, Claude Code pauses and asks for approval. Permission modes control
how often that pause happens, trading oversight for convenience. Switch modes
mid-session by pressing Shift+Tab to cycle `default` → `acceptEdits` →
`plan` in the CLI (other enabled modes such as `bypassPermissions` and `auto`
slot into the same cycle), or set a `defaultMode` in settings to make one the
project default.

`default` mode (labeled **Manual** in the CLI and IDE extensions) only
auto-approves reads; every edit, Bash command, or MCP tool call prompts for
approval. This is the starting point for sensitive work or an unfamiliar
codebase.

`acceptEdits` mode auto-approves file edits and common filesystem Bash
commands (`mkdir`, `touch`, `mv`, `cp`, `sed`, etc.) for paths inside the
working directory, while everything else still prompts. It suits iterating on
code you plan to review afterward with `git diff` rather than approving each
edit inline.

`plan` mode restricts Claude to reads and read-only shell exploration: Claude
researches and proposes a plan but does not edit source files. Use it when
you're uncertain about the approach, the change touches multiple files, or
you're unfamiliar with the code being modified — the docs recommend skipping
it for changes small enough to describe as a one-line diff. Approving a plan
exits plan mode into whichever follow-on mode you choose (auto, accept edits,
or manual review of each edit).

`bypassPermissions` mode skips permission prompts and safety checks entirely,
so tool calls execute immediately. Even in this mode, explicit `ask` rules
still force a prompt, and destructive removals targeting the filesystem root
or home directory (`rm -rf /`, `rm -rf ~`) still trigger a prompt as a circuit
breaker against model error. The documentation is explicit that
`bypassPermissions` "offers no protection against prompt injection or
unintended actions" and should be used only in isolated environments such as
containers or VMs where Claude Code cannot damage the host system — never on
a developer's primary machine or with production access. Claude Code also
refuses to start in this mode when running as root or under `sudo` on Linux
and macOS, unless it detects a recognized sandbox.

# Related

- [allowlists and settings](/oks/claude-best-practices/safety/allowlists-and-settings.md)
- [sandboxing and review](/oks/claude-best-practices/safety/sandboxing-and-review.md)

# Sources

- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/best-practices
