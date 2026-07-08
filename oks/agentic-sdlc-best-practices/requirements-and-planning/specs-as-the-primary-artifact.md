---
type: Agentic SDLC Practice
title: Specs As The Primary Artifact
description: When an agent is the builder, the spec is what it builds from — so ambiguity that a human teammate would quietly resolve instead gets implemented literally, which makes the written plan the cheapest place to catch a wrong direction.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - requirements-and-planning
timestamp: 2026-07-07T00:00:00Z
---

# Specs As The Primary Artifact

When a human writes code, the spec is a starting point they interpret with
judgment: they notice a contradiction, ask a question, or fill a gap with what
the team obviously meant. When an *agent* writes the code, the spec is closer to
the actual program. The agent conditions on what you wrote, not on what you
meant, so every unstated assumption is a place the build can go a direction you
did not intend. That shift is why the May 2026 SDLC paper describes requirements
as no longer a static hand-off but the live object of the work: requirements
"stop being a document handed off between teams" and instead "become a
conversation between humans and AI that produces specification and initial
implementation simultaneously."

## Ambiguity costs more when the builder is an agent

A vague requirement handed to a colleague is usually survivable — they close the
gap with context. Handed to an agent, the same vagueness gets resolved by the
model's default guess, which may be plausible, confidently wrong, and expensive
to unwind later. This is the same reason Anthropic advises that prompts
"reference specific files, mention constraints, and point to example patterns":
the agent "can infer intent, but it can't read your mind." The spec is where that
intent gets pinned down before any code exists, so the effort you spend making it
precise is effort you don't spend debugging a fluent-looking implementation of
the wrong thing.

## Separate planning from implementation

The cheapest quality gate in agentic work is reviewing the plan, not the diff.
Anthropic's recommended workflow separates work into explore, plan, implement,
and commit precisely to "separate research and planning from implementation to
avoid solving the wrong problem." A plan is small, fast to read, and cheap to
correct; a finished multi-file change built on a flawed premise is none of those.
Reviewing the approach first catches a wrong direction while it is still a
paragraph rather than a pull request. The mechanics of doing this in a session
live in [plan mode](/oks/claude-best-practices/planning/plan-mode.md), and the
practice of writing the spec down before generating code is
[spec-first development](/oks/claude-best-practices/planning/spec-first-development.md).

This separation is not free, and it should not be applied uniformly. Anthropic's
own guidance is that planning overhead pays off when the approach is uncertain,
spans multiple files, or touches unfamiliar code — and that for a trivially
scoped change you should skip it: "if you could describe the diff in one
sentence, skip the plan." The spec is the primary artifact for design-bearing
work; it is overhead for a one-line fix. Deciding which units are worth planning
in the first place is the job of [task decomposition](/oks/agentic-sdlc-best-practices/requirements-and-planning/task-decomposition.md).

# Related

- [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)
- [plan mode](/oks/claude-best-practices/planning/plan-mode.md)
- [task decomposition](/oks/agentic-sdlc-best-practices/requirements-and-planning/task-decomposition.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://code.claude.com/docs/en/best-practices
