---
type: OKF Concept Index
title: Automation
description: Running Claude Code outside an interactive session — scripted via `-p`, wired into GitHub CI, or invoked as a saved slash command.
resource: https://code.claude.com/docs/en/headless
tags:
  - claude-code
  - automation
timestamp: 2026-07-07T00:00:00Z
---

# Automation

Claude Code isn't only a chat interface. It can run non-interactively inside
scripts and pipelines, respond to events in a GitHub repository, and expose a
frequently-used prompt as a named command. These concepts cover the
mechanisms for driving Claude Code programmatically rather than turn by turn.

## Concepts

- [headless mode](/oks/claude-best-practices/automation/headless-mode.md) — running `claude -p` non-interactively, with structured `--output-format` for scripts and pipelines to consume.
- [ci and github actions](/oks/claude-best-practices/automation/ci-and-github-actions.md) — the official GitHub Action that runs Claude in CI, responding to `@claude` mentions or scheduled triggers.
- [custom slash commands](/oks/claude-best-practices/automation/custom-slash-commands.md) — capturing a repeated prompt as a reusable `/command` instead of retyping it each session.
