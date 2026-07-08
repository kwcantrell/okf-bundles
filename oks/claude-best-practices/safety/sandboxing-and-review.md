---
type: Claude Code Practice
title: Sandboxing and Review
description: Isolating risky or auto-accepted Claude Code runs at the OS level, and reviewing agent actions rather than trusting them blindly.
resource: https://code.claude.com/docs/en/sandboxing
tags:
  - claude-code
  - safety
  - sandboxing
timestamp: 2026-07-07T00:00:00Z
---

# Sandboxing and Review

Permission modes and allowlists decide whether Claude Code prompts before an
action; sandboxing decides what an approved action can actually reach.
Claude Code's built-in Bash sandbox enforces filesystem and network
boundaries at the OS level (Seatbelt on macOS, bubblewrap on Linux and WSL2)
for every Bash command and its child processes. By default a sandboxed
command can write only to the working directory and the session temp
directory, and no network domain is pre-allowed — the first time a command
needs a new domain, Claude Code prompts for approval. Because enforcement
happens at the OS level rather than by Claude Code inspecting the command
string, the boundary holds even if a prompt injection convinces Claude to
try something the command's name doesn't suggest. Sandboxing complements,
rather than replaces, permission rules: rules stop Claude from attempting
access to a restricted resource, while the sandbox stops a Bash command from
reaching it even if a rule is bypassed.

Anthropic's engineering guidance separates isolation from review. Running
with fewer prompts — accept-edits, auto mode, or `bypassPermissions` — trades
oversight for uninterrupted throughput, and that trade is only safe once the
blast radius is contained: an isolated container or VM without production
access and, ideally, without direct internet access, so that a mistaken or
manipulated action can't reach anything that matters. `bypassPermissions`
mode in particular disables essentially every safety check and is documented
as offering "no protection against prompt injection or unintended actions" —
it belongs only inside that kind of isolated environment, never on a machine
with live credentials or write access to shared infrastructure.

Isolation reduces the blast radius of a mistake; it does not replace
checking that the mistake didn't happen. Anthropic's best-practices guidance
recommends giving Claude something that produces a pass/fail signal — tests,
a build, a screenshot comparison — so a session can verify its own work, and
adding an adversarial review step before treating unattended work as done: a
subagent (or a second, fresh-context session) reviews the diff against the
stated plan and reports gaps, since a reviewer that didn't produce the
change evaluates it on its own terms rather than the reasoning that produced
it. This matters more, not less, as sessions run longer unattended — the
same instinct that isolates a risky run into a container should also gate
whether its output gets trusted without a second look.

# Related

- [permission modes](/oks/claude-best-practices/safety/permission-modes.md)
- [headless mode](/oks/claude-best-practices/automation/headless-mode.md)

# Sources

- https://code.claude.com/docs/en/sandboxing
- https://code.claude.com/docs/en/best-practices
