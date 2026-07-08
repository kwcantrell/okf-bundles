---
type: Claude Code Technique
title: Custom Slash Commands
description: Turning a prompt you keep retyping into a reusable `/command` you invoke by name instead of re-explaining the task each time.
resource: https://code.claude.com/docs/en/slash-commands
tags:
  - claude-code
  - automation
  - slash-commands
timestamp: 2026-07-07T00:00:00Z
---

# Custom Slash Commands

A slash command is a way of naming a task you'd otherwise type out in full
every time: instead of re-explaining "run the test suite, fix any failures,
then summarize what changed" in a fresh message each session, saving that
prompt as `/fix-tests` lets you invoke it directly. A file at
`.claude/commands/deploy.md` creates a `/deploy` command; a file at
`~/.claude/commands/deploy.md` creates the same command available across all
your projects. Project commands are checked into the repository and shared
with anyone working on it; personal commands stay local to you.

The signal that a prompt is worth capturing this way is repetition: if you
keep pasting the same instructions, checklist, or multi-step procedure into
chat, or a section of `CLAUDE.md` has grown into a step-by-step procedure
rather than a fact Claude should just know, that content is a candidate for
a command. Capturing it has two effects: you stop retyping it, and it stops
consuming context on every turn the way a bloated `CLAUDE.md` would, since
a command's body only loads into context when it's actually invoked.

Commands can take arguments, so the same saved prompt generalizes across
inputs instead of being rewritten per use. `$ARGUMENTS` expands to whatever
follows the command name at invocation, so a `/fix-issue` command whose body
reads "Fix GitHub issue $ARGUMENTS following our coding standards" becomes
"Fix GitHub issue 123 following our coding standards..." when run as
`/fix-issue 123`.

Custom commands in `.claude/commands/` continue to work today, but the
current recommended mechanism for this same capability is a skill —
a directory with a `SKILL.md` file — which supports everything a command
does plus optional supporting files and frontmatter controlling who can
invoke it and when it loads. A command and a skill that produce the same
`/name` behave the same way from the invoking side; the choice mostly
affects how much structure the definition needs. The
[file format, frontmatter fields, and hook wiring](/oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md)
behind both mechanisms are the same whether you reach for the lighter
command form or the fuller skill form.

# Related

- [headless mode](/oks/claude-best-practices/automation/headless-mode.md)
- [slash commands and hooks](/oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md)

# Sources

- https://code.claude.com/docs/en/slash-commands
