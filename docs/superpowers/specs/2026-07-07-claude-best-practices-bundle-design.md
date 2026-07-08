# Design: `claude-best-practices` OKF bundle

**Date:** 2026-07-07
**Author:** Kalen Cantrell (with Claude Code)
**Status:** Approved for planning

## Purpose

Add a new Open Knowledge Format (OKF) bundle at `oks/claude-best-practices/`
capturing researched best practices, workflows, and techniques for **using
Claude Code effectively**. The bundle is grounded exclusively in primary
sources (official Claude Code / Anthropic documentation and engineering
material) and follows every convention already established in this repo.

## Scope

**In scope:** how to *drive* Claude Code well — task workflows, context
management, planning techniques, subagents (including model selection),
verification, automation, and safety/permissions.

**Out of scope (delegated to the sibling `ai-agent-repo-structure` bundle):**
how to *structure a repository* for agents — skill authoring, `AGENTS.md`/
`CLAUDE.md` as files, MCP server setup, and hook/slash-command file formats.
Where these topics touch a usage workflow, this bundle covers the *usage angle*
and cross-links to the repo-structure bundle for depth rather than re-covering
it.

This boundary was chosen deliberately (option "Usage workflows & techniques")
to complement, not duplicate, the existing bundle.

## Structure

Standard OKF bundle layout used elsewhere in this repo:

- Bundle root: `index.md` (progressive-disclosure entry linking each area) and
  `log.md` (dated change log).
- Each area is a subdirectory with its own `index.md` linking its concepts.
- Each concept is one markdown file whose path is its identity.

### Areas and concepts (7 areas, 21 concepts)

**`workflows/`** — how to run a task
- `explore-plan-code-commit.md` — read-first, plan, implement, commit loop
- `test-driven-development.md` — write tests → confirm they fail → implement to green
- `iterating-on-visual-targets.md` — supply a mock/screenshot and iterate against it

**`context/`** — managing what Claude knows
- `be-specific-in-instructions.md` — clear, detailed direction up front reduces rework
- `managing-the-context-window.md` — `/clear`, compaction, keeping context focused
- `claude-md-as-memory.md` — tuning `CLAUDE.md`, quick-add with `#`, `/memory` (usage angle; cross-links to repo-structure bundle)
- `referencing-files-urls-images.md` — feeding files, URLs, and images as context

**`planning/`**
- `extended-thinking.md` — "think" / "think hard" / "ultrathink" thinking budgets
- `plan-mode.md` — read-only planning mode before edits
- `spec-first-development.md` — write a spec/plan doc, then implement against it

**`subagents/`**
- `delegating-to-subagents.md` — offloading investigation to preserve main context
- `parallel-agents.md` — multiple agents + git worktrees for concurrent work
- `choosing-a-model.md` — Sonnet for simpler tasks, Opus/Fable for complex reasoning; cost/latency trade-offs

**`verification/`**
- `tests-and-checks-as-guardrails.md` — verifiable feedback loops (tests, linters, types)
- `independent-review.md` — fresh subagent / `/code-review` to review changes

**`automation/`**
- `headless-mode.md` — `claude -p`, output formats, non-interactive runs
- `ci-and-github-actions.md` — Claude Code in CI / GitHub Actions
- `custom-slash-commands.md` — reusable prompt commands for repeated flows (cross-links to repo-structure bundle)

**`safety/`**
- `permission-modes.md` — default / acceptEdits / plan / bypassPermissions
- `allowlists-and-settings.md` — `/permissions`, `settings.json`, tool allow/deny
- `sandboxing-and-review.md` — isolation and reviewing agent actions before trusting them

## Conventions (must-follow)

Per this repo's `CLAUDE.md`:

1. **Concept file format** — YAML frontmatter with all six fields (`type`,
   `title`, `description`, `resource`, `tags`, `timestamp`), timestamp in
   ISO-8601 UTC (`2026-07-07T00:00:00Z`).
2. **Structure** — bundle `index.md` + `log.md`; each area has an `index.md`.
3. **Cross-links** — plain root-relative markdown links only
   (`[text](/oks/claude-best-practices/area/concept.md)`), no `#fragments` or
   `"titles"` in the parens. Every concept ends with a `# Related` section.
4. **Sources** — every concept ends with a `# Sources` section citing primary
   sources only, from allowed hosts. For this bundle the realistic set is:
   `docs.claude.com`, `code.claude.com`, `anthropic.com`. No forums or
   unattributed blogs. Do not state a non-obvious claim without a citation.
5. **Registration** — update the router skill decision table
   (`.claude/skills/oks-bundles/SKILL.md`) and `README.md` to list the new
   bundle. Add cross-links from/to the sibling bundle where natural (e.g.
   `claude-md-as-memory`, `custom-slash-commands`).

## Research method

Research is grounded in official material only. During implementation, spawn
research subagents with model selection matched to task complexity:

- **Sonnet** for straightforward fetch/extract tasks (pulling facts from a
  single doc page).
- **Opus / Fable** for synthesis-heavy concepts that combine multiple sources
  and require careful reasoning (e.g. `choosing-a-model`, `extended-thinking`,
  the area indexes and bundle `index.md`).

Primary source anchors (non-exhaustive):
- Anthropic engineering: "Claude Code Best Practices", "Building effective
  agents".
- Claude Code docs (`docs.claude.com` / `code.claude.com`): common workflows,
  sub-agents, headless, GitHub Actions, settings, IAM/permissions, slash
  commands, memory, extended thinking.
- Model overview / pricing docs for `choosing-a-model`.

## Verification / success criteria

- `python3 tools/validate_okf.py` prints `0 violation(s)`.
- Every concept has full frontmatter, a `# Related` section, and a `# Sources`
  section citing only allowed hosts.
- Router skill and `README.md` list the new bundle.
- `log.md` records bundle creation.
- Work committed as atomic Conventional Commits (`docs:`/`feat:`).

## Out of scope / non-goals

- No changes to the validator or existing bundles beyond adding cross-links and
  registration entries.
- No secondary-source citations (blogs, forums, Reddit).
- Not a comprehensive Claude Code reference — repo-structure topics stay in the
  sibling bundle.
