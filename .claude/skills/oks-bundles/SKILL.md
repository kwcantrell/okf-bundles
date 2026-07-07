---
name: oks-bundles
description: Use when the user asks about git or GitHub workflows, conventions, commands, history, branching, merging, rebasing, pull requests, tags, hooks, or repo security — or when the user asks how to structure a repository so AI agents can discover skills, context files (AGENTS.md, CLAUDE.md), MCP tooling, or curated knowledge. Routes to the OKF bundles under oks/ that hold the answer.
---

# OKS Bundles Router

This repo ships Open Knowledge Format (OKF) bundles: cross-linked Markdown
concept files, each with YAML frontmatter, readable by humans and agents. The
only required frontmatter field is `type`; other fields (title, description,
resource, tags, timestamp) are conventional but optional.

## Navigation

Do not blind-grep the tree. Start at the relevant bundle's `index.md` below
and follow its root-relative links — each index links to area indexes, which
link to individual concepts (progressive disclosure). Read only what's on the
path to the answer.

## Decision table

| Topic | Start here |
| --- | --- |
| git, GitHub, commits, branches, merges, rebases, pull requests, tags, hooks, history, repo security | `oks/git-best-practices/index.md` |
| laying out a repo so AI agents find skills, context files (AGENTS.md, CLAUDE.md), MCP tooling, knowledge bundles | `oks/ai-agent-repo-structure/index.md` |

## Verifying claims

Every concept file ends with a `# Sources` section citing the primary
documentation it's grounded in — follow those links to verify a claim or go
deeper than the summary.
