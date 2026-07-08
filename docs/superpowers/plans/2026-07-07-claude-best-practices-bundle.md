# claude-best-practices Bundle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Author a new OKF bundle at `oks/claude-best-practices/` documenting researched best practices, workflows, and techniques for *using Claude Code*, grounded only in primary sources, and register it in the repo.

**Architecture:** Standard OKF bundle layout already used in this repo: a bundle `index.md` + `log.md`, seven area subdirectories each with an `index.md`, and 21 concept files (one markdown file per concept, path = identity). Content is researched at execution time via `WebFetch` against official Claude Code / Anthropic docs; each concept cites only allowed primary hosts. Tasks are ordered so cross-links only ever point *backward* to already-created files (or the existing sibling bundle), keeping the validator green at every commit.

**Tech Stack:** Markdown with YAML frontmatter; `python3 tools/validate_okf.py` (the repo validator) as the per-task test; `git` with Conventional Commits.

## Global Constraints

- **Concept frontmatter** — every concept file has all six fields: `type`, `title`, `description`, `resource`, `tags`, `timestamp`. `timestamp` is ISO-8601 UTC `2026-07-07T00:00:00Z`.
- **Cross-links** — plain root-relative markdown links only: `[text](/oks/claude-best-practices/area/concept.md)`. No `#fragments`, no `"titles"` inside parens. Every concept ends with a `# Related` section.
- **Sources** — every concept (not `index.md`/`log.md`) ends with a `# Sources` section citing primary sources only. Allowed hosts for this bundle: `docs.claude.com`, `code.claude.com`, `anthropic.com`. Do not state a non-obvious claim you cannot cite to one of these. Verify each URL actually loads via `WebFetch` before citing it; drop any that 404 and find the current canonical page.
- **No forward links** — a concept's `# Related` may link only to files created earlier in this plan, files in the same task, or the existing sibling bundle `oks/ai-agent-repo-structure/`. Never link to a file a later task creates (the validator would fail).
- **Model selection when spawning research subagents** — Sonnet for single-page fetch/extract concepts; Opus/Fable for synthesis-heavy concepts (`choosing-a-model`, `extended-thinking`, all `index.md` files that summarize an area).
- **Per-task test** — `python3 tools/validate_okf.py` must print `0 violation(s)` before every commit.
- **Commits** — atomic, Conventional Commit messages (`feat:` for new bundle content, `docs:` acceptable for pure-doc registration). Work stays on branch `docs/claude-best-practices-bundle`.

## Reference: concept file template

Every concept file follows this shape (fill the researched body between frontmatter and `# Related`):

```markdown
---
type: <Concept type, e.g. "Claude Code Practice">
title: <Title Case>
description: <one sentence, used by the router/index>
resource: <single most authoritative source URL>
tags:
  - claude-code
  - <two or three more>
timestamp: 2026-07-07T00:00:00Z
---

# <Title>

<Researched prose. State claims plainly; every non-obvious claim must be
citable to a URL in # Sources. Use root-relative links to related concepts
inline where natural.>

# Related

- [<other concept>](/oks/claude-best-practices/<area>/<file>.md)

# Sources

- <primary URL 1>
- <primary URL 2>
```

Area `index.md` files use `type: OKF Concept Index`, list the area's concepts with one-line descriptions (mirror `oks/ai-agent-repo-structure/skills/index.md`), and have **no** `# Sources` section.

## File Structure

```
oks/claude-best-practices/
  index.md                 (Task 8)
  log.md                   (Task 8)
  context/                 (Task 1)
    index.md
    be-specific-in-instructions.md
    managing-the-context-window.md
    claude-md-as-memory.md
    referencing-files-urls-images.md
  planning/                (Task 2)
    index.md
    extended-thinking.md
    plan-mode.md
    spec-first-development.md
  verification/            (Task 3)
    index.md
    tests-and-checks-as-guardrails.md
    independent-review.md
  workflows/               (Task 4)
    index.md
    explore-plan-code-commit.md
    test-driven-development.md
    iterating-on-visual-targets.md
  subagents/               (Task 5)
    index.md
    delegating-to-subagents.md
    parallel-agents.md
    choosing-a-model.md
  automation/              (Task 6)
    index.md
    headless-mode.md
    ci-and-github-actions.md
    custom-slash-commands.md
  safety/                  (Task 7)
    index.md
    permission-modes.md
    allowlists-and-settings.md
    sandboxing-and-review.md
```

**Task order rationale (backward-link safety):** context → planning → verification → workflows → subagents → automation → safety → integration. Foundational concepts others reference (context, planning, verification) are built first; the bundle `index.md`/`log.md` and registration come last, after every area index exists.

---

### Task 1: `context/` area (4 concepts + index)

**Files:**
- Create: `oks/claude-best-practices/context/index.md`
- Create: `oks/claude-best-practices/context/be-specific-in-instructions.md`
- Create: `oks/claude-best-practices/context/managing-the-context-window.md`
- Create: `oks/claude-best-practices/context/claude-md-as-memory.md`
- Create: `oks/claude-best-practices/context/referencing-files-urls-images.md`

**Interfaces:**
- Produces: the four `context/*.md` paths above, linked to by Tasks 2–8.
- Consumes: existing sibling bundle path `oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md` (for `claude-md-as-memory` cross-link).

- [ ] **Step 1: Research sources** (Sonnet subagents — single-page fetches)

Fetch and extract key points from:
- `https://www.anthropic.com/engineering/claude-code-best-practices` (sections: "Be specific in your instructions", "Course correct", `/clear` context usage, using CLAUDE.md).
- `https://docs.claude.com/en/docs/claude-code/memory` (CLAUDE.md files, `#` quick-add, `/memory`, imports).
- `https://docs.claude.com/en/docs/claude-code/common-workflows` (referencing files, passing images/URLs, resuming, `/clear`).
- `https://docs.claude.com/en/docs/claude-code/costs` OR analytics page (context/compaction) — verify it loads; drop if not.

- [ ] **Step 2: Write the four concept files**

Per-concept guidance (use the template above):

- `be-specific-in-instructions.md` — `type: Claude Code Practice`. Cover: specific up-front instructions reduce course-correction; give examples of vague vs. specific prompts; mention course-correcting early (Escape to interrupt, edit previous prompt). tags: `claude-code`, `prompting`, `context`. resource: the best-practices article. Related: `managing-the-context-window`, `/oks/claude-best-practices/planning/plan-mode.md` **is Task 2 — do NOT link (forward)**; instead link `referencing-files-urls-images`.
- `managing-the-context-window.md` — Cover: why a focused context matters, `/clear` between tasks, compaction/`/compact`, keeping long sessions on-track. tags: `claude-code`, `context`. Related: `be-specific-in-instructions`, `claude-md-as-memory`.
- `claude-md-as-memory.md` — Cover: `CLAUDE.md` as auto-loaded memory, the `#` shortcut to append a memory, `/memory` to edit, tuning/iterating on it; usage angle only. tags: `claude-code`, `context`, `memory`. Related: `managing-the-context-window`, and sibling `[agents.md and CLAUDE.md](/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md)`.
- `referencing-files-urls-images.md` — Cover: pointing Claude at files/paths, pasting or passing images (screenshots, diagrams), giving URLs for it to fetch, tab-completion of paths. tags: `claude-code`, `context`. Related: `be-specific-in-instructions`.

Each ends with `# Sources` citing only the URLs actually used (from Step 1).

- [ ] **Step 3: Write `context/index.md`**

`type: OKF Concept Index`, `title: Context`. One-line intro, then a `## Concepts` list linking all four files with their descriptions. No `# Sources`.

- [ ] **Step 4: Run the validator**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`. The validator has **no "unreferenced bundle" check** — it only validates frontmatter/`type`, `# Sources` presence, and that every root-relative link resolves. Because these files are link-closed (backward + sibling links only), the whole-repo run passes cleanly even though the bundle isn't registered until Task 8.

If any violation names these files (bad frontmatter, unresolved link, missing `# Sources`), fix inline and re-run until it prints `0 violation(s)`.

- [ ] **Step 5: Commit**

```bash
git add oks/claude-best-practices/context/
git commit -m "feat: add context area to claude-best-practices bundle"
```

---

### Task 2: `planning/` area (3 concepts + index)

**Files:**
- Create: `oks/claude-best-practices/planning/index.md`
- Create: `oks/claude-best-practices/planning/extended-thinking.md`
- Create: `oks/claude-best-practices/planning/plan-mode.md`
- Create: `oks/claude-best-practices/planning/spec-first-development.md`

**Interfaces:**
- Consumes: `context/*` (Task 1).
- Produces: `planning/*.md`, linked to by Tasks 3–8.

- [ ] **Step 1: Research sources**

- `extended-thinking.md` (Opus/Fable — synthesis of two sources): `https://www.anthropic.com/engineering/claude-code-best-practices` ("think" / "think hard" / "think harder" / "ultrathink" escalating thinking budget) and `https://docs.claude.com/en/docs/build-with-claude/extended-thinking` (what extended thinking is). Verify both load.
- `plan-mode.md` (Sonnet): `https://docs.claude.com/en/docs/claude-code/common-workflows` and/or interactive-mode / overview page describing plan mode (read-only, Shift+Tab to cycle modes). Verify current URL.
- `spec-first-development.md` (Sonnet): best-practices article (write a plan/spec, have Claude make a plan before coding, "explore, plan, code, commit").

- [ ] **Step 2: Write the three concept files**

- `extended-thinking.md` — `type: Claude Code Technique`. Cover: prompting words map to increasing thinking budget; when extra reasoning helps (planning, debugging, architecture); trade-off (latency/cost). tags: `claude-code`, `planning`, `reasoning`. Related: `plan-mode`, `spec-first-development`, and `/oks/claude-best-practices/context/be-specific-in-instructions.md`.
- `plan-mode.md` — Cover: read-only mode that plans without editing; how to enter it; when to use (unfamiliar code, risky changes); pairs with extended thinking. tags: `claude-code`, `planning`, `plan-mode`. Related: `extended-thinking`, `spec-first-development`.
- `spec-first-development.md` — Cover: ask Claude to produce a plan/spec doc first, review it, then implement; ties to explore-plan-code-commit (do NOT link workflows yet — forward). tags: `claude-code`, `planning`. Related: `plan-mode`, `extended-thinking`.

- [ ] **Step 3: Write `planning/index.md`** (as in Task 1 Step 3).

- [ ] **Step 4: Run validator** — `python3 tools/validate_okf.py`, resolve any violation naming these files.

- [ ] **Step 5: Commit**

```bash
git add oks/claude-best-practices/planning/
git commit -m "feat: add planning area to claude-best-practices bundle"
```

---

### Task 3: `verification/` area (2 concepts + index)

**Files:**
- Create: `oks/claude-best-practices/verification/index.md`
- Create: `oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md`
- Create: `oks/claude-best-practices/verification/independent-review.md`

**Interfaces:**
- Consumes: `context/*`, `planning/*`.
- Produces: `verification/*.md`, linked to by Tasks 4–8.

- [ ] **Step 1: Research sources**

- `https://www.anthropic.com/engineering/claude-code-best-practices` (give Claude a target/verifiable feedback — tests, expected outputs; using subagents to verify; independent review).
- `https://docs.claude.com/en/docs/claude-code/sub-agents` (a code-reviewer subagent, verification via a separate agent).
- Optional: `https://www.anthropic.com/engineering/building-effective-agents` (verification loops) — cite only if used.

- [ ] **Step 2: Write the two concept files**

- `tests-and-checks-as-guardrails.md` — `type: Claude Code Practice`. Cover: verifiable feedback loops let Claude self-correct (tests, linters, type checks, expected output); give it a way to check its own work. tags: `claude-code`, `verification`, `testing`. Related: `independent-review`, `/oks/claude-best-practices/planning/spec-first-development.md`.
- `independent-review.md` — Cover: use a fresh subagent (or `/code-review`) with clean context to review a change; why independent context catches more; separation of author/reviewer. tags: `claude-code`, `verification`, `code-review`. Related: `tests-and-checks-as-guardrails`.

- [ ] **Step 3: Write `verification/index.md`.**

- [ ] **Step 4: Run validator**, resolve violations for these files.

- [ ] **Step 5: Commit**

```bash
git add oks/claude-best-practices/verification/
git commit -m "feat: add verification area to claude-best-practices bundle"
```

---

### Task 4: `workflows/` area (3 concepts + index)

**Files:**
- Create: `oks/claude-best-practices/workflows/index.md`
- Create: `oks/claude-best-practices/workflows/explore-plan-code-commit.md`
- Create: `oks/claude-best-practices/workflows/test-driven-development.md`
- Create: `oks/claude-best-practices/workflows/iterating-on-visual-targets.md`

**Interfaces:**
- Consumes: `planning/*`, `verification/*`, `context/*`.
- Produces: `workflows/*.md`, linked to by Tasks 5–8.

- [ ] **Step 1: Research sources**

- `https://www.anthropic.com/engineering/claude-code-best-practices` (the "Explore, plan, code, commit" workflow; "Write tests, commit; code, iterate"; "Write code, screenshot result, iterate" / visual mocks).
- `https://docs.claude.com/en/docs/claude-code/common-workflows` (corroborating workflow steps).

- [ ] **Step 2: Write the three concept files**

- `explore-plan-code-commit.md` — `type: Claude Code Workflow`. Cover: read/understand first (no coding yet), make a plan (link plan-mode/extended-thinking), implement, commit; the canonical loop. tags: `claude-code`, `workflows`. Related: `/oks/claude-best-practices/planning/plan-mode.md`, `/oks/claude-best-practices/planning/spec-first-development.md`, `test-driven-development`.
- `test-driven-development.md` — Cover: ask for tests first, confirm they fail (don't implement yet), commit tests, then implement to green, iterate; keep Claude from over-fitting to tests. tags: `claude-code`, `workflows`, `testing`. Related: `/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md`, `explore-plan-code-commit`.
- `iterating-on-visual-targets.md` — Cover: give a visual mock/screenshot as target, have Claude implement, take a screenshot (via MCP/manual), compare, iterate; 2–3 iterations improve results. tags: `claude-code`, `workflows`, `frontend`. Related: `/oks/claude-best-practices/context/referencing-files-urls-images.md`, `explore-plan-code-commit`.

- [ ] **Step 3: Write `workflows/index.md`.**

- [ ] **Step 4: Run validator**, resolve violations for these files.

- [ ] **Step 5: Commit**

```bash
git add oks/claude-best-practices/workflows/
git commit -m "feat: add workflows area to claude-best-practices bundle"
```

---

### Task 5: `subagents/` area (3 concepts + index)

**Files:**
- Create: `oks/claude-best-practices/subagents/index.md`
- Create: `oks/claude-best-practices/subagents/delegating-to-subagents.md`
- Create: `oks/claude-best-practices/subagents/parallel-agents.md`
- Create: `oks/claude-best-practices/subagents/choosing-a-model.md`

**Interfaces:**
- Consumes: `context/*`, `workflows/*`, `verification/*`.
- Produces: `subagents/*.md`, linked to by Tasks 6–8.

- [ ] **Step 1: Research sources**

- `https://docs.claude.com/en/docs/claude-code/sub-agents` (what subagents are, separate context windows, configuration).
- `https://www.anthropic.com/engineering/claude-code-best-practices` (use subagents to preserve context / verify; multiple Claudes / git worktrees for parallel work).
- For `choosing-a-model` (Opus/Fable — synthesis): `https://docs.claude.com/en/docs/about-claude/models/overview` (model strengths: Opus most capable/reasoning, Sonnet balanced, Haiku fastest/cheapest) and `https://docs.claude.com/en/docs/about-claude/pricing` (relative cost). Verify current URLs; if a page moved, find the canonical one on `docs.claude.com`. Do not cite specific dollar figures unless the page confirms them.

- [ ] **Step 2: Write the three concept files**

- `delegating-to-subagents.md` — `type: Claude Code Practice`. Cover: offload investigation/search to a subagent with its own context so the main thread stays focused; when to delegate; you get the conclusion, not the file dumps. tags: `claude-code`, `subagents`, `context`. Related: `/oks/claude-best-practices/context/managing-the-context-window.md`, `parallel-agents`, `choosing-a-model`.
- `parallel-agents.md` — Cover: running multiple agents concurrently for independent tasks; git worktrees to isolate parallel edits; when parallelism helps vs. adds overhead. tags: `claude-code`, `subagents`, `parallelism`. Related: `delegating-to-subagents`, `/oks/claude-best-practices/verification/independent-review.md`.
- `choosing-a-model.md` — Cover: match model to task complexity — Sonnet (or Haiku) for simpler, well-scoped, high-volume tasks; Opus/Fable for complex reasoning, planning, ambiguous problems; trade-offs in cost and latency; applies both to your session model and to models you assign subagents. tags: `claude-code`, `subagents`, `models`. Related: `delegating-to-subagents`, `/oks/claude-best-practices/planning/extended-thinking.md`.

- [ ] **Step 3: Write `subagents/index.md`.**

- [ ] **Step 4: Run validator**, resolve violations for these files.

- [ ] **Step 5: Commit**

```bash
git add oks/claude-best-practices/subagents/
git commit -m "feat: add subagents area to claude-best-practices bundle"
```

---

### Task 6: `automation/` area (3 concepts + index)

**Files:**
- Create: `oks/claude-best-practices/automation/index.md`
- Create: `oks/claude-best-practices/automation/headless-mode.md`
- Create: `oks/claude-best-practices/automation/ci-and-github-actions.md`
- Create: `oks/claude-best-practices/automation/custom-slash-commands.md`

**Interfaces:**
- Consumes: `subagents/*`, `workflows/*`; existing sibling `oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md`.
- Produces: `automation/*.md`, linked to by Tasks 7–8.

- [ ] **Step 1: Research sources**

- `https://docs.claude.com/en/docs/claude-code/headless` (`claude -p`, `--output-format`, non-interactive, streaming JSON).
- `https://docs.claude.com/en/docs/claude-code/github-actions` (Claude Code GitHub Action, `@claude` in PRs/issues, CI usage).
- `https://docs.claude.com/en/docs/claude-code/slash-commands` (custom project/personal commands, `.claude/commands/`, arguments).

- [ ] **Step 2: Write the three concept files**

- `headless-mode.md` — `type: Claude Code Technique`. Cover: `claude -p "<prompt>"` for non-interactive/programmatic runs; output formats (text/json/stream-json); piping and scripting; use in build/lint/triage pipelines. tags: `claude-code`, `automation`, `headless`. Related: `ci-and-github-actions`, `/oks/claude-best-practices/subagents/delegating-to-subagents.md`.
- `ci-and-github-actions.md` — Cover: the official GitHub Action; tagging `@claude` on issues/PRs; automated review/implementation; runs headless under the hood. tags: `claude-code`, `automation`, `ci`, `github`. Related: `headless-mode`, `/oks/claude-best-practices/verification/independent-review.md`.
- `custom-slash-commands.md` — Cover: capture a repeated prompt/workflow as a reusable `/command`; project vs. personal; arguments; usage angle. tags: `claude-code`, `automation`, `slash-commands`. Related: `headless-mode`, and sibling `[slash commands and hooks](/oks/ai-agent-repo-structure/tooling/slash-commands-and-hooks.md)`.

- [ ] **Step 3: Write `automation/index.md`.**

- [ ] **Step 4: Run validator**, resolve violations for these files.

- [ ] **Step 5: Commit**

```bash
git add oks/claude-best-practices/automation/
git commit -m "feat: add automation area to claude-best-practices bundle"
```

---

### Task 7: `safety/` area (3 concepts + index)

**Files:**
- Create: `oks/claude-best-practices/safety/index.md`
- Create: `oks/claude-best-practices/safety/permission-modes.md`
- Create: `oks/claude-best-practices/safety/allowlists-and-settings.md`
- Create: `oks/claude-best-practices/safety/sandboxing-and-review.md`

**Interfaces:**
- Consumes: `automation/*`, `subagents/*`.
- Produces: `safety/*.md`, linked to by Task 8.

- [ ] **Step 1: Research sources**

- `https://docs.claude.com/en/docs/claude-code/iam` (permission modes: default, acceptEdits, plan, bypassPermissions; permission rules).
- `https://docs.claude.com/en/docs/claude-code/settings` (`settings.json`, allow/deny tool rules, `/permissions`).
- `https://www.anthropic.com/engineering/claude-code-best-practices` (safe use of auto-accept / containers / reviewing agent actions).

- [ ] **Step 2: Write the three concept files**

- `permission-modes.md` — `type: Claude Code Practice`. Cover: the modes and what each allows; when to use plan vs. acceptEdits; caution around `bypassPermissions`. tags: `claude-code`, `safety`, `permissions`. Related: `allowlists-and-settings`, `sandboxing-and-review`.
- `allowlists-and-settings.md` — Cover: `/permissions`, allow/deny rules in `settings.json`, tuning which tools/commands run without prompting; project vs. user settings. tags: `claude-code`, `safety`, `permissions`, `settings`. Related: `permission-modes`, and sibling `[guardrails and permissions](/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md)` (verify this sibling path exists before linking; if not, drop it).
- `sandboxing-and-review.md` — Cover: isolate risky/auto-accept runs (containers, worktrees, limited network), review agent actions before trusting; the risk of unattended `bypassPermissions`. tags: `claude-code`, `safety`, `sandboxing`. Related: `permission-modes`, `/oks/claude-best-practices/automation/headless-mode.md`.

- [ ] **Step 3: Write `safety/index.md`.**

- [ ] **Step 4: Run validator**, resolve violations for these files.

- [ ] **Step 5: Commit**

```bash
git add oks/claude-best-practices/safety/
git commit -m "feat: add safety area to claude-best-practices bundle"
```

---

### Task 8: Bundle entry points + registration

**Files:**
- Create: `oks/claude-best-practices/index.md`
- Create: `oks/claude-best-practices/log.md`
- Modify: `.claude/skills/oks-bundles/SKILL.md` (decision-table row)
- Modify: `README.md` (bundle listing)

**Interfaces:**
- Consumes: every area `index.md` from Tasks 1–7.

- [ ] **Step 1: Write `oks/claude-best-practices/index.md`**

Mirror `oks/ai-agent-repo-structure/index.md`: `type: OKF Bundle Index`, `title: Claude Best Practices`, description, `resource: https://www.anthropic.com/engineering/claude-code-best-practices`, tags, timestamp. Body: a short intro (grounded in primary sources; distinct from the repo-structure bundle), then a `## Concept areas` list linking all seven area `index.md` files with one-line descriptions, then a "How to read this bundle" note. No `# Sources`.

- [ ] **Step 2: Write `oks/claude-best-practices/log.md`**

Mirror `oks/ai-agent-repo-structure/log.md`: a `# Change Log — Claude Best Practices bundle` header and a `2026-07-07 — bundle created` entry summarizing the seven areas and 21 concepts.

- [ ] **Step 3: Update the router skill decision table**

In `.claude/skills/oks-bundles/SKILL.md`, add a row to the decision table:

```
| using Claude Code effectively — workflows, context management, planning, subagents and model choice, verification, automation, permissions/safety | `/oks/claude-best-practices/index.md` |
```

Also extend the skill `description` frontmatter to mention Claude Code usage best practices so the router matches those questions.

- [ ] **Step 4: Update `README.md`**

Read `README.md` first to match its existing format for listing bundles, then add `claude-best-practices` alongside the other two bundles with a one-line summary and a link to `/oks/claude-best-practices/index.md`.

- [ ] **Step 5: Run the full validator**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`.
This is the authoritative gate — it checks frontmatter/`type`, that every root-relative `.md` link resolves, that concepts carry `# Sources`, and the cross-references in `README.md`, `CLAUDE.md`, and the router skill. Fix any violation and re-run until it prints `0 violation(s)`.

- [ ] **Step 6: Commit**

```bash
git add oks/claude-best-practices/index.md oks/claude-best-practices/log.md .claude/skills/oks-bundles/SKILL.md README.md
git commit -m "feat: register claude-best-practices bundle in router and README"
```

- [ ] **Step 7: Final full-tree verification**

Run: `python3 tools/validate_okf.py` once more on the whole tree; confirm `0 violation(s)`. Confirm `git status` is clean and all eight commits are present with `git log --oneline -8`.

---

## Self-Review (performed against the spec)

**Spec coverage:** All 7 areas and 21 concepts from the spec map to Tasks 1–7; bundle `index.md`/`log.md` and router/README registration map to Task 8; frontmatter/cross-link/sources conventions are in Global Constraints; model-selection-for-subagents is both a concept (`choosing-a-model`, Task 5) and an execution instruction (Global Constraints + per-task research steps). Validator gate is in every task and finalized in Task 8. No spec requirement is unmapped.

**Placeholder scan:** No "TBD"/"TODO". Concept bodies are researched at execution (content is the deliverable and must come from live primary sources), but each concept has a fully specified frontmatter type/tags/resource, exact source URLs to fetch, explicit coverage bullets, and exact `# Related` targets — no vague "add content here".

**Type/path consistency:** All cross-link targets are backward-only (checked per task against build order context → planning → verification → workflows → subagents → automation → safety). File paths in `# Related` blocks match the File Structure section exactly. Two sibling-bundle links (`guardrails-and-permissions`, `slash-commands-and-hooks`, `agents-md-and-claude-md`) are flagged to verify-before-linking.
