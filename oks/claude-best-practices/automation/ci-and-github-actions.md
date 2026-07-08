---
type: Claude Code Technique
title: CI and GitHub Actions
description: The official Claude Code GitHub Action that runs Claude in CI, responding to `@claude` mentions on issues and pull requests or to scheduled and custom triggers.
resource: https://code.claude.com/docs/en/github-actions
tags:
  - claude-code
  - automation
  - ci
  - github
timestamp: 2026-07-07T00:00:00Z
---

# CI and GitHub Actions

Claude Code GitHub Actions brings the same agent into a GitHub workflow. With
a `@claude` mention in any PR or issue comment, Claude can analyze code,
create pull requests, implement features, and fix bugs while following the
project's own standards — it reads `CLAUDE.md` the same way an interactive
session would. The action is built on top of the Agent SDK, the same
programmatic interface that underlies `claude -p`; a workflow step is, in
effect, a headless Claude Code invocation triggered by a GitHub event instead
of a person typing a prompt.

## Setup

Running `/install-github-app` from a Claude Code session sets this up
interactively: it installs the Claude GitHub App on the repository (which
needs read & write access to Contents, Issues, and Pull requests) and walks
through adding the workflow file and the `ANTHROPIC_API_KEY` repository
secret. A basic workflow just needs the action pinned with an API key:

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    # Responds to @claude mentions in comments
```

The action auto-detects whether to respond interactively to `@claude`
mentions or run immediately with a supplied `prompt`, so the same action
covers both "answer this comment" and "run this fixed task on a schedule"
styles of automation. `claude_args` passes through arbitrary CLI options —
`--max-turns`, `--model`, `--mcp-config`, `--allowedTools` — the same flags
available to `claude -p`.

## Usage patterns

Common triggers include commenting `@claude implement this feature based on
the issue description` or `@claude fix the TypeError in the user dashboard
component` on an issue or PR; Claude analyzes the context and responds or
opens a PR. The `prompt` input can also invoke a skill directly, for example
running an installed `code-review` plugin's skill against every new or
updated pull request on a `pull_request` trigger rather than waiting for a
mention. A `schedule` trigger can run a fixed prompt with no human input at
all, such as generating a daily summary of commits and open issues.

Because each run consumes GitHub Actions minutes and API tokens, workflows
should set `--max-turns` and workflow-level timeouts to bound runaway jobs,
and use specific `@claude` commands rather than open-ended ones to keep token
usage predictable.

# Related

- [headless mode](/oks/claude-best-practices/automation/headless-mode.md)
- [independent review](/oks/claude-best-practices/verification/independent-review.md)

# Sources

- https://code.claude.com/docs/en/github-actions
