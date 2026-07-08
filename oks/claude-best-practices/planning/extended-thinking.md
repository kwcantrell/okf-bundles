---
type: Claude Code Technique
title: Extended Thinking
description: The reasoning Claude emits before answering, controlled mainly by effort level, with an `ultrathink` keyword for one-off deeper reasoning.
resource: https://code.claude.com/docs/en/model-config
tags:
  - claude-code
  - planning
  - reasoning
timestamp: 2026-07-07T00:00:00Z
---

# Extended Thinking

Extended thinking is the reasoning Claude emits before it responds. On models
that support adaptive reasoning, the model decides whether and how much to think
on each step based on task complexity, so it can answer routine prompts quickly
and reserve deeper thinking for steps that benefit from it. This makes extra
reasoning most valuable exactly where it pays off: planning a change, debugging,
and architectural decisions, rather than on simple, mechanical edits.

## Effort level is the primary control

On adaptive-reasoning models, the [effort level](https://code.claude.com/docs/en/model-config)
is the primary control for how much thinking happens. Lower effort is faster and
cheaper for straightforward tasks, while higher effort provides deeper reasoning
for complex problems. Claude Code exposes levels of `low`, `medium`, `high`,
`xhigh`, and `max`; `high` is the default on most current models. `low` is for
short, latency-sensitive work that is not intelligence-sensitive, while `max`
gives the deepest reasoning with no constraint on token spending but may show
diminishing returns and is prone to overthinking. You set the level with
`/effort`, the effort slider in `/model`, the `--effort` flag, or the
`CLAUDE_CODE_EFFORT_LEVEL` environment variable.

## The `ultrathink` keyword

For a single turn, include `ultrathink` anywhere in your prompt to request deeper
reasoning without changing your session effort setting. Claude Code recognizes
the keyword and adds an in-context instruction; the effort level sent to the API
is unchanged. Note that other phrases such as "think", "think hard", and "think
more" are passed through as ordinary prompt text and are not recognized as
keywords. If you want Claude to think more or less often in general, you can say
so directly in your prompt or in `CLAUDE.md`, and the model responds to that
guidance within its current effort setting.

## The trade-off

Thinking is not free: you are charged for all thinking tokens generated, even
when they are collapsed or redacted in the display. Higher effort and deeper
reasoning therefore trade latency and token cost for capability, which is why the
default suits most coding tasks and you raise it deliberately when a problem
warrants it. Extended thinking can be toggled for a session with `Option+T`
(macOS) or `Alt+T` (Windows and Linux), or set as a global default via `/config`
(saved as `alwaysThinkingEnabled`).

# Related

- [plan mode](/oks/claude-best-practices/planning/plan-mode.md)
- [spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)
- [be specific in instructions](/oks/claude-best-practices/context/be-specific-in-instructions.md)

# Sources

- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/interactive-mode
