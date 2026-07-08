---
type: Claude Code Practice
title: Referencing Files, URLs, And Images
description: Pointing Claude directly at files, images, and URLs gives it rich context without waiting for it to search or read things itself.
resource: https://code.claude.com/docs/en/common-workflows
tags:
  - claude-code
  - context
timestamp: 2026-07-07T00:00:00Z
---

# Referencing Files, URLs, And Images

Rather than describing where code lives or what a design looks like, give
Claude Code the file, image, or link directly.

## Files and directories

Use `@` to reference a file or directory without waiting for Claude to read
it first: `@` triggers file path autocomplete, and `@src/utils/auth.js`
includes the full file content in the conversation, while `@src/components`
provides a directory listing rather than file contents. File paths can be
relative or absolute, and multiple files can be referenced in one message.
`@` file references also pull in the `CLAUDE.md` files from the referenced
file's directory and its parent directories. `@server:resource` references
MCP resources the same way.

## Images

Images can be added to the conversation by dragging and dropping them into
the terminal window, copying and pasting with `Ctrl+V` (or the
platform-specific paste shortcut), or by giving Claude a path directly, such
as "Analyze this image: /path/to/your/image.png". This works for screenshots
of errors, UI mockups, and diagrams — for example, pasting a design screenshot
and asking Claude to implement it, or a database schema image and asking how
to modify it for a new feature. Multiple images can be present in a
conversation at once.

## URLs

Give Claude URLs directly for documentation and API references it should
fetch, and use `/permissions` to allowlist domains you point Claude at
frequently so it doesn't need approval each time.

## Piping data

Data can also be piped straight into a session rather than referenced by
path: `cat error.log | claude` or `git log --oneline -20 | claude -p
"summarize these recent commits"` send file or command output directly into
the conversation, which is useful for CI and batch processing. Claude can
also fetch what it needs itself using Bash commands, MCP tools, or by reading
files directly when told to.

# Related

- [be specific in instructions](/oks/claude-best-practices/context/be-specific-in-instructions.md)

# Sources

- https://code.claude.com/docs/en/common-workflows
- https://code.claude.com/docs/en/best-practices
