---
type: OKF Concept
title: The Karpathy Guidelines
description: A widely-copied community CLAUDE.md distilled from Karpathy's observations about how LLMs fail at coding — its four principles, and how they serve as the operating discipline around an autonomous loop.
resource: https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md
tags:
  - autoresearch
  - karpathy
  - agentic-engineering
timestamp: 2026-07-07T00:00:00Z
---

# The Karpathy Guidelines

The "Karpathy Guidelines" are a popular `CLAUDE.md` rule set that circulates under
Karpathy's name — but they are not text Karpathy authored. They are a
**community-authored distillation**: a contributor packaged the file, and its own
README states plainly that the rules are *derived from* Karpathy's observations
about LLM coding pitfalls rather than written by him. Getting the attribution
right matters, because the two layers have different sources. This concept treats
the rule set as a practical codification of the
[engineering discipline](/oks/autoresearch-best-practices/agentic-engineering/engineering-discipline.md)
an autonomous loop needs — not as a Karpathy quotation.

## The observations underneath

The raw material is a thread Karpathy posted noting recurring ways LLMs fail when
coding: they make silent, sometimes wrong assumptions on your behalf; they do not
manage or surface their own confusion; they fail to ask for clarification when
they should; they do not flag inconsistencies; and they present a single answer
instead of laying out the tradeoffs or pushing back. Those are Karpathy's own
stated observations. The rule set below is one community's attempt to convert them
into standing instructions an agent can follow.

## The four principles

As hosted in the community repository, the distilled `CLAUDE.md` organizes those
observations into four principles:

- **Think Before Coding** — do not assume; state your assumptions instead of
  acting on them silently, do not hide confusion, ask when genuinely unsure, and
  surface tradeoffs rather than committing to one path unannounced.
- **Simplicity First** — write the minimum code that solves the stated problem,
  and nothing speculative built for imagined future needs.
- **Surgical Changes** — touch only what the task requires, and clean up only the
  mess you yourself made.
- **Goal-Driven Execution** — define explicit success criteria up front and loop
  until they are verifiably met.

Read against AutoResearch, these are not abstract style advice. "Goal-Driven
Execution" is precisely the loop's keep-or-reset rule against `val_bpb`.
"Simplicity First" mirrors the repo's own simplicity criterion, where a change's
complexity cost is weighed against its improvement. "Surgical Changes" is the
single-file discipline that keeps each diff reviewable. The guidelines read like a
generalization of the same instincts Karpathy baked into the loop itself.

## Where they fit around the loop

A `CLAUDE.md` shapes what the agent *tries*, not what it is *allowed* to do; it is
persistent instruction, not enforcement. That distinction is the point:
guidelines like these steer the agent toward stating assumptions and staying in
scope, but the hard bounds on an unattended run still come from
[time-boxing and guardrails](/oks/autoresearch-best-practices/running-with-claude-code/time-boxing-and-guardrails.md).
Understanding a project-level instruction file as durable, load-bearing context —
rather than a one-off prompt — is covered in
[CLAUDE.md as memory](/oks/claude-best-practices/context/claude-md-as-memory.md).
The Karpathy Guidelines are best used as one well-worn starting point for that
file, distilled from real observations about how agents go wrong.

# Related

- [engineering discipline](/oks/autoresearch-best-practices/agentic-engineering/engineering-discipline.md)
- [time-boxing and guardrails](/oks/autoresearch-best-practices/running-with-claude-code/time-boxing-and-guardrails.md)
- [CLAUDE.md as memory](/oks/claude-best-practices/context/claude-md-as-memory.md)

# Sources

- https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md
- https://github.com/forrestchang/andrej-karpathy-skills
- https://x.com/karpathy/status/2015883857489522876
