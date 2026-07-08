---
type: Agentic SDLC Practice
title: Compaction And Long-Horizon Context
description: Long tasks outgrow a single window, so agents summarize and restart (compaction), hand off across sessions, and isolate subtasks into sub-agent context windows to keep the working set small.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - agentic-sdlc
  - context-engineering
timestamp: 2026-07-07T00:00:00Z
---

# Compaction And Long-Horizon Context

Curation keeps a single window lean, but some tasks run longer than any window
can hold — a migration across dozens of files, a debugging session that spans
hours. For those, the question shifts from *what to include* to *how to carry
state forward* when the raw history no longer fits. Three techniques do this
work: compaction, handoffs, and sub-agent isolation.

## Compaction: summarize and restart

Compaction is the core move. Anthropic defines it as "taking a conversation
nearing the context window limit, summarizing its contents, and reinitiating a
new context window with the summary" — the session continues, but seeded with a
distilled record instead of the full transcript. The tension to manage is how
much to throw away: Anthropic warns that "overly aggressive compaction can result
in the loss of subtle but critical context," discarding a detail that seemed
unimportant but turns out to matter later. Compact to preserve decisions,
modified files, and open threads; don't compact so hard that you erase the
reasoning behind them.

## Sub-agent isolation

The second technique keeps the main window from ever filling in the first place.
Rather than "one agent attempting to maintain state across an entire project,"
Anthropic describes letting "specialized sub-agents ... handle focused tasks with
clean context windows." A sub-agent explores in its own window and hands back
only "a condensed, distilled summary of its work (often 1,000-2,000 tokens)," so
the orchestrator's context absorbs the conclusion, not the search that produced
it. This is why delegating research to a subagent is a context-management move as
much as a division of labor —
[delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md)
covers the mechanics.

## Handoffs done automatically

In practice these techniques are often handled by the harness rather than the
prompt. As of mid-2026, LangChain ships a `SummarizationMiddleware` that runs
before the model and, "if message history exceeds a certain token threshold, its
contents are summarized before being passed to the model"; extensions of it
offload verbose tool inputs and outputs to the filesystem instead of holding them
in the window. Deep Agents combines "built-in offloading and summarization" with
sub-agents that isolate heavy subtasks into separate windows. The harness that
manages this continuously — middleware, offloading, and context policies — is its
own subject, deferred to the agent-harness area; here the point is that
long-horizon context management is a designed capability, not something the model
does on its own.

# Related

- [curating the context window](/oks/agentic-sdlc-best-practices/context-engineering/curating-the-context-window.md)
- [delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md)
- [middleware and context management](/oks/agentic-sdlc-best-practices/agent-harness/middleware-and-context-management.md)

# Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness
- https://docs.langchain.com/oss/python/deepagents/overview
