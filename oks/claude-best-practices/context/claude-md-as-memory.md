---
type: Claude Code Practice
title: CLAUDE.md As Memory
description: CLAUDE.md is a persistent, auto-loaded instructions file you write and tune over time, complemented by auto memory that Claude writes to itself.
resource: https://code.claude.com/docs/en/memory
tags:
  - claude-code
  - context
  - memory
timestamp: 2026-07-07T00:00:00Z
---

# CLAUDE.md As Memory

Each Claude Code session begins with a fresh context window, so `CLAUDE.md`
is what carries knowledge across sessions: it is a plain Markdown file that
gives Claude persistent instructions for a project, a personal workflow, or
an entire organization, and Claude reads it at the start of every session.
`CLAUDE.md` and its personal counterpart `CLAUDE.local.md` are treated as
context Claude reads and tries to follow, not enforced configuration — for an
action that must be blocked regardless of what Claude decides, use a hook
instead.

## Viewing and editing with `/memory`

Run `/memory` in a session to list every CLAUDE.md, CLAUDE.local.md, and
rules file currently loaded, toggle auto memory on or off, and open the auto
memory folder. Selecting any file opens it in your editor. If a file you
expect isn't listed, Claude can't see it, which is the first thing to check
when instructions aren't being followed. You can also just ask Claude
directly — "add this to CLAUDE.md" — and it edits the file for you.

## Auto memory

Alongside CLAUDE.md, Claude Code maintains auto memory: notes Claude writes
to itself as it works, based on your corrections and preferences, without you
writing anything by hand. When you tell Claude something like "always use
pnpm, not npm," Claude saves it to auto memory rather than to CLAUDE.md
unless you ask for CLAUDE.md specifically. Auto memory is stored as a
`MEMORY.md` index plus topic files; only the first 200 lines (or 25KB) of
`MEMORY.md` load automatically each session, while topic files load on demand
when Claude needs them.

## Tuning CLAUDE.md over time

Because CLAUDE.md is context rather than enforced configuration, how you
write it affects how reliably Claude follows it:

- **Add to it** when Claude makes the same mistake twice, when a review
  catches something Claude should have known, or when you type the same
  correction into chat that you typed last session.
- **Keep it concise** — target under 200 lines. Longer files consume more
  context and reduce adherence; move detailed or path-specific instructions
  into `.claude/rules/` or a skill instead.
- **Review and prune periodically.** If Claude keeps ignoring a rule, the
  file is probably too long and the rule is getting lost; if Claude asks
  questions already answered in CLAUDE.md, the phrasing may be ambiguous.
  Treat CLAUDE.md like code: review it when things go wrong.

CLAUDE.md files can be placed at the user level (`~/.claude/CLAUDE.md`), the
project level (`./CLAUDE.md`, checked into git and shared with the team), or
as personal, gitignored `./CLAUDE.local.md` notes — the [agents.md and
CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)
concept covers how CLAUDE.md relates to the cross-tool AGENTS.md convention.

# Related

- [managing the context window](/oks/claude-best-practices/context/managing-the-context-window.md)
- [agents.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)

# Sources

- https://code.claude.com/docs/en/memory
