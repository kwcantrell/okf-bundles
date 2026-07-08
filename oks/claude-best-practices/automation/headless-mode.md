---
type: Claude Code Technique
title: Headless Mode
description: Running Claude Code non-interactively with `claude -p` so scripts, pipelines, and other programs can drive it and consume its output.
resource: https://code.claude.com/docs/en/headless
tags:
  - claude-code
  - automation
  - headless
timestamp: 2026-07-07T00:00:00Z
---

# Headless Mode

Adding `-p` (or `--print`) to any `claude` command runs it non-interactively:
Claude Code executes the prompt, prints the result, and exits, instead of
opening an interactive session. This is the entry point for using Claude Code
as a building block inside scripts, build pipelines, and other programs
rather than as a chat interface a person drives turn by turn.

Non-interactive mode reads stdin, so it composes with ordinary shell
pipelines. Piping a build log in and redirecting the response to a file —
`cat build-error.txt | claude -p 'concisely explain the root cause of this
build error' > output.txt` — works the same as any other command-line tool.
That composability is what makes headless mode useful as a project-specific
linter or reviewer: a `package.json` script can pipe a diff into Claude and
have it report typos or flag issues, with Claude never needing shell
permission to read the diff itself since the data arrives on stdin.

`--output-format` controls how the response comes back, which matters once a
program (rather than a person) is the consumer:

- `text` (default) — plain text output.
- `json` — a structured payload with the result, a session ID, and metadata
  such as `total_cost_usd`, so a caller can track spend per invocation.
  Combined with `--json-schema`, the response's `structured_output` field
  conforms to a caller-supplied JSON Schema.
- `stream-json` — newline-delimited JSON events for real-time streaming,
  typically read with `--verbose --include-partial-messages` and filtered
  with a tool like `jq`.

For CI and other scripted calls, add `--bare` to skip auto-discovery of
hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md, so the run
depends only on flags passed explicitly and behaves the same on every
machine. `--allowedTools` (or a permission mode such as `--permission-mode
acceptEdits`) lets a headless run auto-approve the specific tools it needs —
for example `--allowedTools "Bash,Read,Edit"` to run a test suite and fix
failures — without a person present to answer permission prompts.
User-invoked skills and custom commands still work in `-p` mode by including
`/skill-name` in the prompt string.

These pieces combine into pipeline stages: a headless `claude -p` call reads
piped input or repo state, does the work with an explicit, minimal tool
allowlist, and returns text or structured JSON that the surrounding script or
CI job consumes. That is also the mechanism the official GitHub Action runs
under the hood.

# Related

- [ci and github actions](/oks/claude-best-practices/automation/ci-and-github-actions.md)
- [delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md)

# Sources

- https://code.claude.com/docs/en/headless
