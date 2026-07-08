# Design: `autoresearch-best-practices` OKF bundle

**Date:** 2026-07-07
**Status:** Approved (design), pending implementation plan

## Goal

Add a new Open Knowledge Format (OKF) bundle at
`oks/autoresearch-best-practices/` documenting Andrej Karpathy's **AutoResearch**
autonomous-ML-research loop and how to run it with **Claude Code**, plus the
adjacent Karpathy "agentic engineering" discipline. The bundle follows the same
conventions as the existing bundles (`git-best-practices`,
`ai-agent-repo-structure`, `claude-best-practices`) and must pass
`python3 tools/validate_okf.py` with `0 violation(s)`.

## Background: what AutoResearch is

Karpathy open-sourced [`autoresearch`](https://github.com/karpathy/autoresearch)
on 2026-03-07: a deliberately tiny (~630-line) tool that turns an ML research
workflow into a tight, automatable loop. An AI coding agent reads a Markdown
instruction file, edits a single `.py` training script, runs a time-boxed
experiment, measures validation loss, and **keeps or `git revert`s** the change —
then repeats, potentially overnight. The engineering task shifts from manually
tuning hyperparameters to *prompt-engineering the agent* to search the space
well. The single-file, fits-in-context design lets the agent hold a holistic
view of the training script. It went viral (66k+ GitHub stars within a month).

This bundle documents that loop, how to drive it with Claude Code specifically,
and Karpathy's broader "vibe coding → agentic engineering" framing that
surrounds it.

## Scope

In scope (approved: AutoResearch core **plus** adjacent Karpathy
agentic-engineering material):

- The AutoResearch loop mechanics.
- Operating the loop with Claude Code (headless/autonomous runs, prompting the
  search, guardrails).
- The adjacent Karpathy agentic-engineering discipline and community
  "Karpathy Guidelines."

Out of scope: unrelated Karpathy material (nanochat, Software 2.0/3.0, LLM OS,
Tesla/OpenAI history) except where it directly frames the loop.

## Bundle structure

Root: `oks/autoresearch-best-practices/` with `index.md` (progressive-disclosure
entry) and `log.md` (dated change log). Three areas, each a subdirectory with
its own `index.md`. 10 concept files total.

### Area 1 — `loop/` (what AutoResearch is: the mechanics)

- `agent-research-loop.md` — the propose → run experiment → measure →
  keep-or-revert cycle, run autonomously (potentially overnight).
- `spec-script-split.md` — the Markdown instruction file (the "what to try")
  separated from the single `.py` training script (the "thing being edited").
- `single-file-context-constraint.md` — why it is deliberately ~630 lines: the
  whole codebase fits in the agent's context window, so it keeps a holistic view.
- `keep-or-revert-with-git.md` — validation loss as the objective; `git revert`
  to discard any change that does not improve it.

### Area 2 — `running-with-claude-code/` (how to operate it)

- `claude-code-as-the-agent.md` — driving the loop with Claude Code
  (headless/autonomous runs).
- `prompting-the-search.md` — the shift from hand-tuning hyperparameters to
  prompt-engineering the agent to navigate the search space.
- `time-boxing-and-guardrails.md` — time-boxed experiments, budgets, and safely
  letting it run unattended.

### Area 3 — `agentic-engineering/` (the adjacent Karpathy discipline)

- `vibe-coding-to-agentic-engineering.md` — the 80/20 shift from vibe prompts to
  orchestrated agent workflows.
- `engineering-discipline.md` — spec design, diff review, eval design, security
  oversight, taste.
- `karpathy-guidelines.md` — the community CLAUDE.md rules (state assumptions,
  minimal code, the self-check protocol).

## Concept file conventions (per repo CLAUDE.md)

- Each concept is one markdown file; its path is its identity.
- YAML frontmatter with all six fields: `type`, `title`, `description`,
  `resource`, `tags`, `timestamp` (ISO-8601 UTC, e.g. `2026-07-07T00:00:00Z`).
- Body, then a `# Related` section (plain root-relative markdown links only —
  `[text](/oks/...md)`, no `#fragments` or `"titles"`), then a `# Sources`
  section.
- `index.md`/`log.md` are exempt from the `# Sources` requirement.

## Sourcing standard

The repo's `CLAUDE.md` allowlist will be **expanded** for this bundle. Add hosts:
`github.com`, `arxiv.org`, `x.com`. Claims are grounded in this priority order:

1. **`github.com` (Karpathy's `autoresearch` repo)** — primary source for the
   loop, the file split, and the ~630-line constraint.
2. **`docs.claude.com` / `code.claude.com` / `anthropic.com`** (already
   allowlisted) — all Claude-Code-specific operation: headless mode, autonomous
   runs, model choice.
3. **`arxiv.org`** — broader agentic-research context (researcher-agent
   benchmark literature).
4. **`x.com` (Karpathy's own posts)** — author's primary words for the
   agentic-engineering framing, cited by direct attribution only.

Secondary tech journalism (DataCamp, MarkTechPost, etc.) is treated as
**corroboration, not primary citation**. A claim that can only be hung on an
unattributed blog is left out. Every concept ends with a `# Sources` section.

## Execution & subagent/model plan

Match models to task complexity (per user instruction):

- **Research (parallel, `Explore`/general-purpose subagents on `sonnet`)** — one
  subagent per source cluster: (a) the GitHub repo, (b) Claude Code docs,
  (c) arXiv/agentic-research, (d) Karpathy posts + secondary corroboration.
  Straightforward extraction → Sonnet.
- **Synthesis + writing (`opus`)** — turning research into the 10 concept files
  in the repo's dense, cross-linked voice is the reasoning-heavy part → Opus
  (one subagent per area to keep each area in-context), or written directly by
  the main agent.
- **Validation (main loop)** — wire up cross-links, write `index.md`/`log.md`,
  update the router skill (`.claude/skills/oks-bundles/SKILL.md`), `README.md`,
  and the `CLAUDE.md` allowlist, then run `python3 tools/validate_okf.py` until
  it prints `0 violation(s)`.

## Integration points to update

Per repo CLAUDE.md rule 5 (adding a new bundle):

- `.claude/skills/oks-bundles/SKILL.md` — add a row to the decision table and
  extend the skill `description`.
- `README.md` — add the bundle to its bundle list / cross-references.
- `CLAUDE.md` — expand the source allowlist with `github.com`, `arxiv.org`,
  `x.com`.

## Acceptance criteria

- `oks/autoresearch-best-practices/` exists with `index.md`, `log.md`, three
  area subdirectories each with `index.md`, and the 10 concept files above.
- Every concept has complete frontmatter, a `# Related` section, and a
  `# Sources` section citing only allowlisted hosts.
- Router `SKILL.md`, `README.md`, and `CLAUDE.md` updated.
- `python3 tools/validate_okf.py` prints `0 violation(s)`.
- Commits are atomic with Conventional Commit messages.

## Commit plan

Atomic, Conventional Commits (mirroring the existing `claude-best-practices`
history — allowlist/scaffold first, then area by area, then router/README
registration last):

1. `build: expand CLAUDE.md source allowlist for autoresearch bundle`
2. `feat: scaffold autoresearch-best-practices bundle (index, log)`
3. `feat: add loop area to autoresearch-best-practices bundle`
4. `feat: add running-with-claude-code area to autoresearch-best-practices bundle`
5. `feat: add agentic-engineering area to autoresearch-best-practices bundle`
6. `feat: register autoresearch-best-practices bundle in router and README`
