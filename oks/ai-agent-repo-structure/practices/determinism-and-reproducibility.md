---
type: Agent Practice
title: Determinism and Reproducibility
description: Using hooks for actions that must happen every time, and pass/fail checks plus parseable output for reproducible, verifiable agent runs.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - ai-agents
  - determinism
  - reproducibility
  - hooks
timestamp: 2026-07-07T00:00:00Z
---

# Determinism and Reproducibility

Instructions in a context file are advisory — a strong nudge, not a guarantee.
When an outcome must be certain, structure the repository to *enforce* it rather
than *request* it.

## Advisory instructions vs. deterministic hooks

Anthropic's guidance draws the line explicitly: "Hooks run scripts automatically
at specific points in Claude's workflow. Unlike CLAUDE.md instructions which are
advisory, hooks are deterministic and guarantee the action happens." Reserve
[hooks](/oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md) for
actions that must happen every time with zero exceptions — formatting, secret
scanning, a required check — and leave genuinely advisory guidance in context
files.

## Give the agent a check it can run

Reproducible, verifiable behavior comes from giving Claude a check it can run — a
test, a build, a linter, or a script that diffs output against a fixture — so the
agent gets a pass/fail signal instead of relying on subjective judgement of when
work "looks done." A committed check is itself part of repo structure: it turns
"looks right" into "passes." The validator that gates this very bundle is an
example of exactly that pattern.

## Parseable output for unattended runs

Automation needs structured output, not prose. Non-interactive mode
(`claude -p "prompt"`) supports `--output-format json` or
`--output-format stream-json --verbose` specifically so results can be parsed
programmatically in CI pipelines, pre-commit hooks, or scripts. For batch or
scripted automation across many files, the `--allowedTools` CLI flag scopes
exactly which tools a non-interactive invocation may use — which matters when you
are running unattended.

## Shared, versioned context

Reproducibility also depends on everyone starting from the same context.
Best-practice guidance recommends checking `CLAUDE.md` into git so a team can
contribute to and share the same persistent project context, noting that "the file
compounds in value over time." Settings files support a `$schema` field (for
example `"https://json.schemastore.org/claude-code-settings.json"`) for
autocomplete and validation in editors, and most settings keys — including
`permissions` and `hooks` — reload without a restart when the file changes, while
`model` and `outputStyle` require a restart or `/model` / `/clear`.

# Related

- [slash commands and hooks](/oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md)
- [guardrails and permissions](/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md)
- [precedence and scope](/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md)

# Sources

- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/settings.md
