---
type: Agent Skill Concept
title: What Is a Skill
description: A skill is a filesystem folder of instructions, scripts, and resources an agent discovers and loads on demand to specialize at a task.
resource: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
tags:
  - ai-agents
  - skills
  - claude-code
timestamp: 2026-07-07T00:00:00Z
---

# What Is a Skill

A skill is an organized folder of instructions, scripts, and resources that
agents can discover and load dynamically to perform better at specific tasks.
Put another way, skills are "reusable, filesystem-based resources that provide
Claude with domain-specific expertise: workflows, context, and best practices
that transform general-purpose agents into specialists." Each skill packages
instructions, metadata, and optional resources (scripts, templates) that Claude
uses automatically when relevant — and Claude will only access a skill when it is
relevant to the task at hand.

## The four defining attributes

Skills are described as:

- **Composable** — skills stack together; Claude automatically identifies which
  skills are needed and coordinates their use.
- **Portable** — build once, use across Claude apps, Claude Code, and the API.
- **Efficient** — only what is needed is loaded, when it is needed.
- **Powerful** — skills can include executable code for tasks where traditional
  programming is more reliable than token generation.

## In Claude Code

In Claude Code, skills extend what Claude can do: you create a `SKILL.md` file
with instructions and Claude adds it to its toolkit. Claude uses skills when
relevant, or you can invoke one directly with `/skill-name`. Claude Code skills
follow the Agent Skills open standard, which works across multiple AI tools — so
a skill authored for one surface is not locked to it.

## When to create one

Create a skill when you keep pasting the same instructions, checklist, or
multi-step procedure into chat, or when a section of `CLAUDE.md` has grown into a
*procedure* rather than a *fact*. This is the practical dividing line: durable,
always-true facts belong in
[context files](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md),
while occasionally-relevant procedures belong in a skill that loads on demand and
does not tax every conversation.

# Related

- [skill file format](/oks/ai-agent-repo-structure/skills/skill-file-format.md)
- [skill placement](/oks/ai-agent-repo-structure/skills/skill-placement.md)
- [progressive disclosure](/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md)

# Sources

- https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://www.anthropic.com/news/skills
- https://docs.claude.com/en/docs/claude-code/skills
