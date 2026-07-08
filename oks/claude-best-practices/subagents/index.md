---
type: OKF Concept Index
title: Subagents
description: Delegating work to Claude Code subagents — offloading investigation to separate context windows, running agents in parallel, and matching the model to the task.
resource: https://code.claude.com/docs/en/sub-agents
tags:
  - claude-code
  - subagents
timestamp: 2026-07-07T00:00:00Z
---

# Subagents

Subagents let Claude Code do work outside your main conversation: research and
side tasks run in their own context windows and report back only a summary.
These concepts cover when to delegate, how to run multiple agents at once, and
how to pick the right model for each piece of work.

## Concepts

- [delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md) — offload investigation and search to a subagent with its own context so the main thread stays focused, and you get the conclusion instead of the file dumps.
- [parallel agents](/oks/claude-best-practices/subagents/parallel-agents.md) — run multiple sessions concurrently on independent tasks, isolate their edits with git worktrees, and use a fresh session to review another's work.
- [choosing a model](/oks/claude-best-practices/subagents/choosing-a-model.md) — match the model to task complexity for both your own session and each subagent, trading capability against cost and latency.
