---
type: OKF Bundle Index
title: AutoResearch Best Practices
description: A cross-linked OKF bundle on Andrej Karpathy's autoresearch — the autonomous ML-research loop, running it with Claude Code, and the agentic-engineering discipline it demands.
resource: https://github.com/karpathy/autoresearch
tags:
  - autoresearch
  - karpathy
  - agentic-engineering
  - claude-code
  - agentic-coding
timestamp: 2026-07-07T00:00:00Z
---

# AutoResearch Best Practices

An [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
bundle covering Andrej Karpathy's [autoresearch](https://github.com/karpathy/autoresearch):
a small but real LLM training setup that an AI agent experiments on
autonomously overnight, editing the code, training for a few minutes, checking
whether the result improved, and keeping or discarding the change. This bundle
breaks the project into three views — the mechanics of the loop itself, how to
drive that loop with Claude Code as the agent, and the broader engineering
discipline the loop is an instance of. Every concept is grounded in the
autoresearch repository's own files and Karpathy's own writing.

## Concept areas

- [loop](/oks/autoresearch-best-practices/loop/index.md) — the mechanics of the autonomous loop: the edit/run/measure/keep-or-reset cycle, the spec/script split, single-file discipline, and git as the accept/reject mechanism.
- [running-with-claude-code](/oks/autoresearch-best-practices/running-with-claude-code/index.md) — using Claude Code as the driving agent: headless mode, prompting the search, and time-boxing the blast radius of an unattended run.
- [agentic-engineering](/oks/autoresearch-best-practices/agentic-engineering/index.md) — the discipline around the loop: Karpathy's shift from "vibe coding" to "agentic engineering," why it is engineering rather than prompting, and the operating guidelines it implies.

## How to read this bundle

Each concept file carries YAML frontmatter (type, title, description, a
primary `resource` URL, tags, and a timestamp), an explanatory body, a
`# Related` section of cross-links, and a `# Sources` section citing the
primary material behind its claims. Start with `loop` to understand what
autoresearch actually does, then read `running-with-claude-code` to drive it
and `agentic-engineering` for the discipline that surrounds it.
