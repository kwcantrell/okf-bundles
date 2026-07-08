# Change Log — Claude Best Practices bundle

2026-07-07 — bundle created

Initial authoring of the `claude-best-practices` OKF bundle. This entry covers
all seven concept areas and the bundle entry points:

- Added the bundle `index.md` (progressive-disclosure entry point listing all
  seven concept areas) and this `log.md`.
- Authored **context** (be specific in instructions, managing the context
  window, `CLAUDE.md` as memory, referencing files/URLs/images) — 4 concepts.
- Authored **planning** (extended thinking, plan mode, spec-first
  development) — 3 concepts.
- Authored **verification** (tests and checks as guardrails, independent
  review) — 2 concepts.
- Authored **workflows** (explore/plan/implement/commit, test-driven
  development, iterating on visual targets) — 3 concepts.
- Authored **subagents** (delegating to subagents, parallel agents, choosing
  a model) — 3 concepts.
- Authored **automation** (headless mode, CI and GitHub Actions, custom slash
  commands) — 3 concepts.
- Authored **safety** (permission modes, allowlists and settings, sandboxing
  and review) — 3 concepts.

21 concepts total across the seven areas, each grounded in Anthropic's Claude
Code documentation. The bundle cross-links into the sibling
`ai-agent-repo-structure` bundle where natural (guardrails and permissions,
slash commands and hooks, `AGENTS.md`/`CLAUDE.md`), and is registered in the
router skill (`.claude/skills/oks-bundles/SKILL.md`) and `README.md`.
