---
type: OKF Bundle Index
title: AI Agent Repo Structure
description: A cross-linked OKF bundle on structuring a repository so AI coding agents can discover context, load skills, and work reliably.
resource: https://agents.md
tags:
  - ai-agents
  - repository-structure
  - claude-code
  - agents-md
  - skills
timestamp: 2026-07-07T00:00:00Z
---

# AI Agent Repo Structure

An [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
bundle covering how to structure a repository so AI coding agents — Claude Code
and the broader ecosystem that reads `AGENTS.md` — can find the right context,
load the right capabilities, and behave predictably. Every concept is grounded
in primary sources (agents.md, the Claude Code documentation, Anthropic's
engineering writing, and the OKF announcement) and cross-links to related
concepts so you can navigate the material as a graph.

Start here, pick the area closest to your question, and follow its `index.md`
into the individual concepts. Where more than one valid approach exists
(`AGENTS.md` import vs. symlink, project vs. personal skills, advisory context
vs. deterministic hooks), these notes present the trade-offs rather than
mandating one answer.

## Concept areas

- [context files](/oks/ai-agent-repo-structure/context-files/index.md) — the instruction files agents read at startup: `AGENTS.md`, `CLAUDE.md`, progressive disclosure, and precedence across scopes.
- [skills](/oks/ai-agent-repo-structure/skills/index.md) — packaging expertise as on-demand Agent Skills: what they are, their file format, where they live, and project vs. personal scope.
- [conventions](/oks/ai-agent-repo-structure/conventions/index.md) — repository layout, naming for discoverability, and treating `AGENTS.md` as a README for agents.
- [knowledge](/oks/ai-agent-repo-structure/knowledge/index.md) — curating durable knowledge in the repo: OKF bundles, docs written for agents, and machine-readable metadata.
- [tooling](/oks/ai-agent-repo-structure/tooling/index.md) — configuring an agent's tools: MCP servers, slash commands, and hooks.
- [practices](/oks/ai-agent-repo-structure/practices/index.md) — working reliably: determinism and reproducibility, and guardrails and permissions.

## How to read this bundle

Each concept file carries YAML frontmatter (type, title, description, a primary
`resource` URL, tags, and a timestamp), an explanatory body, a `# Related`
section of cross-links, and a `# Sources` section citing the primary
documentation behind its claims.
