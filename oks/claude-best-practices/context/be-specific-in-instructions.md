---
type: Claude Code Practice
title: Be Specific In Instructions
description: Precise, concrete prompts reduce the number of corrections a Claude Code session needs, and correcting early keeps a session from drifting further off track.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - claude-code
  - prompting
  - context
timestamp: 2026-07-07T00:00:00Z
---

# Be Specific In Instructions

Claude can infer intent, but it cannot read your mind. The more precise an
instruction is, the fewer corrections a session needs afterward. Anthropic's
guidance on this is to scope the task (which file, which scenario, which
testing preference), point Claude to sources that already answer a question,
reference existing patterns in the codebase to imitate, and describe symptoms
concretely rather than vaguely.

A few before/after examples from Anthropic's best-practices guide illustrate
the difference:

- Vague: *"add tests for foo.py"* — Specific: *"write a test for foo.py
  covering the edge case where the user is logged out. avoid mocks."*
- Vague: *"add a calendar widget"* — Specific: *"look at how existing widgets
  are implemented on the home page to understand the patterns.
  HotDogWidget.php is a good example. follow the pattern..."*
- Vague: *"fix the login bug"* — Specific: *"users report that login fails
  after session timeout. check the auth flow in src/auth/, especially token
  refresh. write a failing test that reproduces the issue, then fix it"*

Vague prompts aren't always wrong — a prompt like *"what would you improve in
this file?"* can surface things you wouldn't have thought to ask about — but
they only pay off when you can afford to course-correct afterward.

## Course-correct early and often

Tight feedback loops produce better results than letting a session run long
on a wrong assumption. Claude Code gives you several ways to interrupt and
redirect:

- **`Esc`** stops Claude mid-action while preserving context, so you can
  redirect immediately.
- **`Esc` twice, or `/rewind`** opens a menu to restore previous conversation
  and code state, or to summarize from a selected message.
- **Telling Claude "undo that"** reverts its changes directly.
- **`/clear`** resets context entirely, which is the right move once you've
  corrected the same issue more than twice in one session — at that point the
  context is cluttered with failed approaches, and a clean session with a
  more specific prompt that incorporates what you learned almost always
  outperforms continuing to correct.

# Related

- [managing the context window](/oks/claude-best-practices/context/managing-the-context-window.md)
- [referencing files, urls, and images](/oks/claude-best-practices/context/referencing-files-urls-images.md)

# Sources

- https://code.claude.com/docs/en/best-practices
