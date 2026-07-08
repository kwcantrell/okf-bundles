---
type: Agentic SDLC Practice
title: Skills Libraries
description: Packaging process knowledge as small, triggered, composable skills rather than one monolithic prompt lets an agent load deep procedural detail only when a task matches — the dynamic-context pattern that keeps the static prompt lean and the token cost down.
resource: https://github.com/obra/superpowers
tags:
  - agentic-sdlc
  - applications
timestamp: 2026-07-07T00:00:00Z
---

# Skills Libraries

A monolithic prompt pays for all its knowledge on every task — every token loaded
whether or not the current task needs it. A skills library inverts that. A skill
is a portable package of procedural knowledge that the agent loads *only when the
task calls for it*: the agent sees lightweight metadata at startup, loads full
instructions when a task matches, and pulls deep reference material only when
explicitly needed (kaggle.com). This is the dynamic-context lever — the paper's
recommended way to "truly optimize OpEx," via skills or tool calling rather than
static context (kaggle.com) — and it is why skills, not a bigger system prompt,
are the right home for reusable process knowledge. For the underlying concept and
file mechanics, see
[what is a skill](/oks/ai-agent-repo-structure/skills/what-is-a-skill.md) and
[skill file format](/oks/ai-agent-repo-structure/skills/skill-file-format.md).

## The superpowers pattern

Superpowers is "a complete software development methodology for your coding
agents, built on top of a set of composable skills and some initial instructions"
(github.com) — not a single prompt. Its shape is worth copying:

- **Process skills first.** The library leads with *how to work* skills —
  brainstorming, writing-plans, test-driven-development — one directory per skill
  under `skills/`, each with a `SKILL.md` (github.com).
- **Triggers, not summaries.** A skill's `description` is written as an imperative
  trigger — *when to invoke it* — so the agent can match it against the current
  task, e.g. "You MUST use this before any creative work..." (github.com).
- **Mandatory, gated workflows.** Skills encode hard gates: brainstorming forbids
  any implementation action "until you have presented a design and the user has
  approved it," and TDD enforces "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"
  (github.com). The agent checks for relevant skills before any task — a mandatory
  step, not a suggestion (github.com).

This is the same factory-model discipline of building the system that builds the
software, applied to reusable procedure —
[the factory model](/oks/agentic-sdlc-best-practices/agent-harness/the-factory-model.md).

## Procedure: extracting a monolithic prompt into skills

1. **Find the triggerable procedures.** In your big prompt, find each block that is
   really a *procedure for a situation* ("when refactoring...", "before
   committing...") rather than an always-true fact.
2. **Give each a trigger description.** Write the `description` as an imperative
   condition the agent can match — when to fire, not what it contains.
3. **Move the detail into progressive disclosure.** Keep the SKILL.md body lean;
   push long reference material behind it so it loads only when needed.
4. **Leave only always-true facts in the static prompt.** Stack, hard guardrails,
   and the trigger metadata stay static; everything situational becomes a skill.
5. **Verify triggers fire.** Give the agent a task that should match and confirm it
   loads the skill — an unfired trigger is a dead skill.

## Minimal skill-file skeleton

```markdown
---
name: writing-plans
description: >
  Use when you have a spec for a multi-step task, before touching code.
  Imperative trigger — when to invoke, matched against the current task.
---

# Writing Plans

> Lean body: the procedure's core steps.
> Push long reference material to linked files so it loads only when needed.
```

# Related

- [what is a skill](/oks/ai-agent-repo-structure/skills/what-is-a-skill.md)
- [skill file format](/oks/ai-agent-repo-structure/skills/skill-file-format.md)
- [the factory model](/oks/agentic-sdlc-best-practices/agent-harness/the-factory-model.md)

# Sources

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
