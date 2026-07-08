---
type: Claude Code Practice
title: Managing The Context Window
description: The context window fills fast and performance degrades as it fills, so keeping it focused with /clear and compaction is central to getting good results from a session.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - context
timestamp: 2026-07-07T00:00:00Z
---

# Managing The Context Window

Claude's context window holds the entire conversation: every message, every
file Claude reads, and every command's output. A single debugging session or
codebase exploration can generate and consume tens of thousands of tokens.
This matters because LLM performance degrades as the context window fills —
when it's getting full, Claude may start "forgetting" earlier instructions or
making more mistakes. The context window is the most important resource in a
session to manage.

## Reset between tasks with `/clear`

Long sessions that accumulate irrelevant conversation, file contents, and
command output reduce performance and can distract Claude. Running `/clear`
frequently between unrelated tasks resets the context window entirely. A
recognizable failure pattern is the "kitchen sink session" — starting one
task, asking about something unrelated, then returning to the first — which
fills context with irrelevant information; the fix is the same: `/clear`
between unrelated tasks.

## Compaction

Claude Code automatically compacts conversation history as you approach
context limits, summarizing what matters most — code patterns, file states,
and key decisions — while freeing space. For more control, run
`/compact <instructions>` (for example, `/compact Focus on the API changes`)
to tell Claude what to preserve during summarization. You can also customize
compaction behavior from CLAUDE.md with an instruction such as "When
compacting, always preserve the full list of modified files and any test
commands," so critical context survives summarization automatically.

Project-root CLAUDE.md itself survives compaction: after `/compact`, Claude
re-reads it from disk and re-injects it into the session. Nested CLAUDE.md
files in subdirectories are not re-injected automatically — they reload the
next time Claude reads a file in that subdirectory.

## Keeping long sessions on track

For quick questions that don't need to stay in context, `/btw` answers from
what's already in the conversation without adding the question or answer to
conversation history, so you can check a detail without growing context. And
because subagents run in their own separate context windows and report back
only a summary, delegating research to a subagent ("use subagents to
investigate X") keeps the main conversation clean for implementation instead
of filling it with every file read along the way.

# Related

- [be specific in instructions](/oks/claude-best-practices/context/be-specific-in-instructions.md)
- [claude.md as memory](/oks/claude-best-practices/context/claude-md-as-memory.md)

# Sources

- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/memory
