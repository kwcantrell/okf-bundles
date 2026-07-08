---
type: OKF Bundle Index
title: Claude Best Practices
description: A cross-linked OKF bundle on using Claude Code effectively — managing context, planning before coding, verifying results, and scaling with subagents and automation.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - best-practices
  - agentic-coding
  - subagents
  - automation
timestamp: 2026-07-07T00:00:00Z
---

# Claude Best Practices

An [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
bundle covering how to *use* Claude Code well, once it's already running in a
repository. Where the sibling
[ai-agent-repo-structure](/oks/ai-agent-repo-structure/index.md) bundle covers
how to *structure* a repo so agents can find context, skills, and tooling,
this bundle covers the operator side: how to manage a session's context, get
Claude to plan before it codes, close the loop with verification, delegate to
subagents, automate Claude outside an interactive session, and control what it
can do without asking. Every concept is grounded in Anthropic's official
Claude Code documentation.

## Concept areas

- [context](/oks/claude-best-practices/context/index.md) — managing what Claude knows in a session: precise instructions, a clean context window, `CLAUDE.md` as memory, and rich inline references.
- [planning](/oks/claude-best-practices/planning/index.md) — separating thinking from doing: extended thinking, plan mode, and spec-first development.
- [verification](/oks/claude-best-practices/verification/index.md) — closing the loop with a check Claude can run itself, and an independent review before calling work done.
- [workflows](/oks/claude-best-practices/workflows/index.md) — repeatable end-to-end loops: explore/plan/implement/commit, test-driven development, and iterating against a visual target.
- [subagents](/oks/claude-best-practices/subagents/index.md) — delegating work to separate context windows, running agents in parallel, and matching the model to the task.
- [automation](/oks/claude-best-practices/automation/index.md) — running Claude outside an interactive session: headless mode, CI/GitHub Actions, and custom slash commands.
- [safety](/oks/claude-best-practices/safety/index.md) — controlling what Claude can do without asking, and containing the blast radius when you let it do more.

## How to read this bundle

Each concept file carries YAML frontmatter (type, title, description, a
primary `resource` URL, tags, and a timestamp), an explanatory body, a
`# Related` section of cross-links, and a `# Sources` section citing the
primary documentation behind its claims. Start with whichever area matches
your question, or read `context` and `planning` first if you're new to
Claude Code — most other areas build on managing context and planning well.
