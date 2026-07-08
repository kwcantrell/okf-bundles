# okf-bundles

A collection of [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
(OKF) bundles, plus a Claude Code router skill that makes them discoverable to
agents.

OKF is a simple pattern for durable, sourced knowledge: Markdown files with
YAML frontmatter, cross-linked into a graph, readable by both humans and AI
agents without any special tooling.

## Bundles

- [`oks/git-best-practices/`](oks/git-best-practices/index.md) — Git and
  GitHub best practices, from the repository model to collaboration
  workflows.
- [`oks/ai-agent-repo-structure/`](oks/ai-agent-repo-structure/index.md) — how
  to structure a repository so AI coding agents can discover context, load
  skills, and work reliably.
- [`oks/claude-best-practices/`](oks/claude-best-practices/index.md) — how to
  use Claude Code effectively, from managing context and planning to
  verification, subagents, automation, and permissions/safety.
- [`oks/autoresearch-best-practices/`](oks/autoresearch-best-practices/index.md) — Karpathy's
  autoresearch autonomous ML-research loop, running it with Claude Code, and
  the agentic-engineering discipline around it.

## Router skill

[`.claude/skills/oks-bundles/`](.claude/skills/oks-bundles/SKILL.md) is a
Claude Code skill that routes questions to the right bundle. Its
`description` carries explicit triggers (git/GitHub topics, or repo layout
for AI agents) so Claude Code loads it automatically when relevant, and its
body gives a decision table pointing at each bundle's `index.md`.

## How to consume a bundle

Start at a bundle's `index.md` and follow its links — each index links to
area indexes, which link to individual concept files (progressive
disclosure). Every concept file ends with a `# Sources` section citing the
primary documentation behind its claims, so you can verify or go deeper.

To check structural integrity (frontmatter, required `type` field, link
resolution), run the validator:

```bash
python3 tools/validate_okf.py
```

With no arguments it checks every concept under `oks/` plus the cross-references
in `README.md` and the router skill; pass a bundle path (e.g.
`tools/validate_okf.py oks/git-best-practices`) to check just that bundle. The
same command runs in CI on every push and pull request
(`.github/workflows/validate.yml`).

## Design docs

See [`docs/superpowers/`](docs/superpowers/) for the design spec and
implementation plan behind this repo.
