---
type: Claude Code Practice
title: Delegating to Subagents
description: Offload investigation and search to a subagent that works in its own context window and returns only a summary, keeping the main conversation focused.
resource: https://code.claude.com/docs/en/sub-agents
tags:
  - claude-code
  - subagents
  - context
timestamp: 2026-07-07T00:00:00Z
---

# Delegating to Subagents

A subagent is a specialized assistant that Claude Code delegates a task to.
Each subagent runs in its own context window with a custom system prompt,
specific tool access, and independent permissions; it works independently and
returns its results to the main conversation. Reach for one when a side task
would flood your main conversation with search results, logs, or file contents
you won't reference again — the subagent does that work in its own context and
returns only the summary.

The reason this matters is that context is Claude Code's fundamental
constraint: performance degrades as the context window fills. When Claude
researches a codebase directly, it reads many files, and all of that content
consumes your context. Subagents run in separate context windows and report
back summaries, so the exploration doesn't accumulate in the conversation
you're implementing from. You get the conclusion, not the file dumps.

## When to delegate

Delegating is most valuable for read-heavy investigation. The official guidance
is to delegate research with a prompt like *"use subagents to investigate X"* —
they explore in a separate context, keeping your main conversation clean for
implementation. For example, asking a subagent to investigate how the
authentication system handles token refresh, and whether existing OAuth
utilities exist to reuse, has the subagent read the relevant files and report
findings without cluttering the main conversation.

Delegation is also the documented fix for *infinite exploration* — asking Claude
to "investigate" something unscoped, which can make it read hundreds of files
and fill the context. Scoping investigations narrowly, or using subagents so the
exploration doesn't consume your main context, avoids that failure. Subagents
are equally useful after implementation: a fresh subagent can review code for
edge cases without the reasoning that produced the change biasing it.

Beyond one-off delegation, Claude Code ships built-in subagents — Explore, Plan,
and general-purpose — and lets you define custom subagents as Markdown files in
`.claude/agents/`, each with its own tools, permissions, and model. Defining a
custom subagent pays off when you keep spawning the same kind of worker with the
same instructions. Which model each subagent runs on is itself a lever worth
choosing deliberately.

# Related

- [managing the context window](/oks/claude-best-practices/context/managing-the-context-window.md)
- [parallel agents](/oks/claude-best-practices/subagents/parallel-agents.md)
- [choosing a model](/oks/claude-best-practices/subagents/choosing-a-model.md)

# Sources

- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/best-practices
