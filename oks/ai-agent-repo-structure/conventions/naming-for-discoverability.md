---
type: Repo Convention
title: Naming for Discoverability
description: How file paths and names become the primary discovery signal — from the nearest AGENTS.md to a skill's directory name to OKF cross-links.
resource: https://docs.claude.com/en/docs/claude-code/slash-commands
tags:
  - ai-agents
  - naming
  - discoverability
  - conventions
timestamp: 2026-07-07T00:00:00Z
---

# Naming for Discoverability

For an agent, a name is not decoration — it is often the thing the agent matches
against to decide what to read or run. Naming and placement are load-bearing.

## Placement selects which instructions apply

Because agents automatically read the *nearest* `AGENTS.md` file in the directory
tree, the placement and naming of that file — root versus per-package — directly
determines which instructions an agent applies to a given piece of work. Naming a
file correctly and putting it in the right directory is how you scope its
influence.

## A skill's directory name is its command

In Claude Code, the directory name of a skill becomes the command typed to invoke
it: `.claude/skills/deploy-staging/SKILL.md` becomes `/deploy-staging`. The
frontmatter `name` field, by contrast, only sets the display label shown in skill
listings. When a nested skill shares a name with a root-level skill, the nested
one is exposed under a directory-qualified name such as `apps/web:deploy` so both
remain invocable without collision.

## Name and description are the trigger signal

Skill authors are told to pay special attention to the `name` and `description`
of a skill, since Claude uses these when deciding whether to trigger the skill —
making those two fields the primary discoverability signal. The same instinct
applies to rule files: `.claude/rules/` guidance recommends a descriptive
filename like `testing.md` or `api-design.md` so a rule's topical scope is
discoverable from its filename alone.

## Paths as identity in OKF

In OKF, a concept's file path *is* its identity, and concepts cross-link to each
other using ordinary Markdown links (for example a column description linking to a
`customers` table at `/tables/customers.md`). The relationship graph is discoverable
purely through file and path naming plus links — which is why the concept files
in this bundle use plain, descriptive names and root-relative links.

# Related

- [directory layout](/oks/ai-agent-repo-structure/conventions/directory-layout.md)
- [README for agents](/oks/ai-agent-repo-structure/conventions/readme-for-agents.md)
- [machine-readable metadata](/oks/ai-agent-repo-structure/knowledge/machine-readable-metadata.md)

# Sources

- https://agents.md/
- https://docs.claude.com/en/docs/claude-code/slash-commands
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://docs.claude.com/en/docs/claude-code/memory
- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
