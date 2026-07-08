---
type: Claude Code Practice
title: Choosing a Model
description: Match the model to task complexity — faster, cheaper models for simple well-scoped work and the most capable models for complex reasoning — for both your session and each subagent.
resource: https://code.claude.com/docs/en/model-config
tags:
  - claude-code
  - subagents
  - models
timestamp: 2026-07-07T00:00:00Z
---

# Choosing a Model

Claude Code lets you select which model answers, and the right choice depends on
the task. The model aliases the docs expose describe what each tier is suited
for: `haiku` uses the fast and efficient Haiku model for simple tasks, `sonnet`
uses the latest Sonnet model for daily coding tasks, `opus` uses the latest Opus
model for complex reasoning tasks, and `fable` uses Claude Fable 5 for your
hardest and longest-running tasks. That ordering is the whole heuristic: match
the model to the complexity of the work in front of you.

## The trade-off

Picking a model trades capability against cost and latency. For simpler,
well-scoped, high-volume work, a faster, cheaper model is the better fit — the
subagents documentation frames this directly as controlling costs by routing
tasks to faster, cheaper models like Haiku. For complex reasoning, planning, and
ambiguous problems, the most capable model earns its higher cost. Fable 5 is
described as the most capable model in Claude Code, suited to tasks larger than a
single sitting: it sustains long autonomous sessions, investigates before
acting, and verifies its work more often than smaller models. The docs
explicitly point it at ambiguous problems — root-cause investigations, outage
debugging, and architecture decisions — where the extra investigation and
verification pay off. Opus, in turn, is the alias for complex reasoning tasks
short of that, and Sonnet is the balanced default for everyday coding.

## Applies to your session and your subagents

This choice operates at two levels.

**Your session model.** Set it during a session with `/model <alias|name>`, at
startup with `claude --model <alias|name>`, through the `ANTHROPIC_MODEL`
environment variable, or permanently in your settings file's `model` field.
Running `/model` with no argument opens a picker. Since v2.1.153, `/model` saves
your choice as the default for new sessions; you can switch for the current
session only if you'd rather not change the default.

**Each subagent's model.** A subagent's `model` frontmatter field selects which
model it uses, accepting a model alias (`sonnet`, `opus`, `haiku`, `fable`), a
full model ID such as `claude-opus-4-8`, or `inherit`; omitting it defaults to
`inherit`, which uses the same model as the main conversation. This is the
concrete mechanism for matching a model to a delegated task: define a read-only
exploration subagent with `model: haiku` to keep that work on a lower-cost
model, or give a review or analysis subagent `model: opus` for more capable
reasoning, independent of whatever your main session is running. Claude Code
resolves a subagent's model in a fixed order — the `CLAUDE_CODE_SUBAGENT_MODEL`
environment variable first, then the per-invocation `model` parameter, then the
subagent definition's `model` frontmatter, and finally the main conversation's
model.

Because your own session and every subagent you dispatch each carry their own
model setting, the same match-to-complexity judgment applies at both levels: run
the heavy reasoning on a capable model, and push the high-volume, well-scoped
work down to a faster, cheaper one.

# Related

- [delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md)
- [extended thinking](/oks/claude-best-practices/planning/extended-thinking.md)

# Sources

- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/sub-agents
