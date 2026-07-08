---
type: OKF Concept
title: Time-Boxing and Guardrails
description: Bounding an unattended AutoResearch run — pairing the loop's 10-minute experiment kill with Claude Code's permission modes, tool allowlists, and sandboxing to contain the blast radius.
resource: https://code.claude.com/docs/en/permission-modes
tags:
  - autoresearch
  - karpathy
  - claude-code
timestamp: 2026-07-07T00:00:00Z
---

# Time-Boxing and Guardrails

An autonomous loop that runs while you sleep needs bounds on two things: how long
any single experiment can burn, and what the agent is allowed to touch. AutoResearch
supplies the first bound itself; Claude Code supplies the second. Getting both right
is what makes it safe to walk away from the loop — the counterpart to the
[keep or revert with git](/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md)
accept/reject step that decides whether each experiment survives.

## Time-boxing comes from the loop

The experiment budget is written into `program.md`: "If a run exceeds 10 minutes,
kill it and treat it as a failure (discard and revert)." That single rule keeps a
runaway training run from consuming the whole night — a bad idea costs at most ten
minutes before it is killed, discarded, and the branch reset. Because each
experiment is time-boxed to roughly five minutes in the normal case, the agent can
complete around 100 of them over an average night's sleep. The time-box is a
loop-level guardrail, not a Claude Code feature; the agent just has to honor it.

## Blast radius comes from Claude Code's permissions

The other risk is scope: an autonomous agent editing code and running shell
commands unattended. Claude Code's permission system is the containment layer, and
it is enforced by Claude Code itself rather than by the model — prompt or CLAUDE.md
instructions shape what the agent *tries*, but only permission rules decide what
actually runs. For a locked-down loop, the relevant choices are:

- **Tool allowlists.** `--allowedTools` auto-approves only the specific tools the
  loop needs — for AutoResearch, roughly `Read`, `Edit`, and `Bash` to run
  `uv run train.py` and the `git` commands — so no prompt ever blocks an unattended
  run. Rules can be scoped with prefix syntax like `Bash(git commit *)`.
- **Permission modes.** The
  [permission modes](/oks/claude-best-practices/safety/permission-modes.md) range
  from `default` (manual approval) to `bypassPermissions` (no prompts at all). For
  scripted, locked-down runs the docs recommend `dontAsk`, which permits only
  pre-approved tools. `bypassPermissions` disables safety checks entirely and
  "offers no protection against prompt injection or unintended actions"; the docs
  restrict it to "isolated environments like containers, VMs, or dev containers
  without internet access, where Claude Code cannot damage your host system." Auto
  mode is the middle path: it runs largely uninterrupted with background classifier
  safety checks, and in non-interactive `-p` runs it aborts if the classifier
  repeatedly blocks actions, since there is no human to fall back to.

## Sandboxing for a true isolation boundary

Permission rules govern all tools; sandboxing adds OS-level enforcement around the
Bash tool and its child processes — Seatbelt on macOS, bubblewrap on Linux and
WSL2. The docs are explicit that a real boundary needs both halves: "Effective
sandboxing requires both filesystem and network isolation. Without network
isolation, a compromised agent could exfiltrate sensitive files like SSH keys.
Without filesystem isolation, a compromised agent could backdoor system resources
to gain network access." For an AutoResearch loop churning through 100 unreviewed
code edits overnight on one machine, running it inside such a sandbox — with write
access scoped to the working directory and network access limited to what the
training run genuinely needs — keeps a bad experiment or a prompt-injection from
reaching anything beyond the repo it is meant to be improving.

# Related

- [keep or revert with git](/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md)
- [permission modes](/oks/claude-best-practices/safety/permission-modes.md)

# Sources

- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/sandboxing
- https://code.claude.com/docs/en/best-practices
- https://github.com/karpathy/autoresearch/blob/master/program.md
