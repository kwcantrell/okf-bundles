---
type: Claude Code Practice
title: Parallel Agents
description: Run multiple Claude sessions concurrently on independent tasks, isolating their edits with git worktrees, and use a fresh session to review another's work.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - subagents
  - parallelism
timestamp: 2026-07-07T00:00:00Z
---

# Parallel Agents

Everything about a single Claude session assumes one human, one Claude, and one
conversation — but Claude Code also scales horizontally. Once you're effective
with one Claude, you can multiply output by running multiple sessions in
parallel to speed up development, run isolated experiments, or start complex
workflows.

## Isolate parallel edits

The hazard with concurrent sessions is that their edits collide. The documented
options let you pick how much coordination you want to do yourself:

- **Worktrees** — run separate CLI sessions in isolated git checkouts so edits
  don't collide.
- **Desktop app** — manage multiple local sessions visually, each in its own
  worktree.
- **Claude Code on the web** — run sessions on Anthropic-managed cloud
  infrastructure in isolated VMs.
- **Agent teams** — automated coordination of multiple sessions with shared
  tasks, messaging, and a team lead.

Git worktrees are the core primitive here: because each session operates on its
own checkout, two agents can modify the same repository at once without
overwriting each other's work.

## When parallelism helps

Parallelism pays off when the tasks are genuinely independent — a large
migration fanned out across many files, or separate experiments you want to run
without interference. For batch work, you can loop `claude -p` over a task list,
using `--allowedTools` to scope permissions for unattended runs.

Beyond raw throughput, multiple sessions enable quality-focused workflows. A
fresh context improves code review, since Claude won't be biased toward code it
just wrote. The documented Writer/Reviewer pattern uses one session to implement
a feature and a second, independent session to review that implementation for
edge cases, race conditions, and consistency with existing patterns — then the
first session addresses the feedback. You can do the same with tests: one Claude
writes the tests, another writes code to pass them.

Parallelism is not free, though. Each session you spawn is one more context to
steer and one more stream of output to reconcile, so the coordination overhead
is only worth it when the work is truly separable. When tasks share state or
must happen in sequence, a single session is simpler and more reliable.

# Related

- [delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md)
- [independent review](/oks/claude-best-practices/verification/independent-review.md)

# Sources

- https://code.claude.com/docs/en/best-practices
