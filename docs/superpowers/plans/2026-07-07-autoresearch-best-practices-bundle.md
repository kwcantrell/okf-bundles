# AutoResearch Best Practices Bundle — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new OKF bundle at `oks/autoresearch-best-practices/` documenting Karpathy's AutoResearch autonomous-ML loop, how to run it with Claude Code, and the adjacent agentic-engineering discipline — passing `python3 tools/validate_okf.py` with `0 violation(s)`.

**Architecture:** A research phase (parallel Sonnet subagents extract source-attributed facts into a scratchpad notes file) feeds a writing phase (Opus, one area at a time) that produces cross-linked Markdown concept files following the repo's OKF conventions. The validator is the test harness: after each area is written, `python3 tools/validate_okf.py` must pass before committing. Files are built leaf-first (concepts and their area `index.md`) with the root `index.md` and router/README registration committed last, because the validator requires every root-relative link to resolve at every commit.

**Tech Stack:** Markdown + YAML frontmatter (OKF), `tools/validate_okf.py` (Python 3), git. No application code.

## Global Constraints

Copied verbatim from the repo's `CLAUDE.md` and the approved spec. Every task's requirements implicitly include this section.

- **Concept file format:** one markdown file per concept; its path is its identity. YAML frontmatter with all six fields: `type`, `title`, `description`, `resource`, `tags`, `timestamp`. `timestamp` is ISO-8601 UTC: `2026-07-07T00:00:00Z`.
- **Structure:** bundle root has `index.md` (progressive-disclosure entry) and `log.md` (dated change line per change). Each area subdirectory has its own `index.md`.
- **Cross-links:** plain root-relative markdown links **only** — `[atomic commits](/oks/git-best-practices/commits/atomic-commits.md)`. No `#fragments`, no `"titles"` inside the parens. Every concept ends with a `# Related` section.
- **Sources:** every concept (not `index.md`/`log.md`) ends with a `# Sources` section citing primary sources only. Allowed hosts (post-expansion): `git-scm.com`, `docs.github.com`, `atlassian.com`, `conventionalcommits.org`, `agents.md`, `docs.claude.com`, `code.claude.com`, `anthropic.com`, `cloud.google.com`, **`github.com`**, **`arxiv.org`**, **`x.com`**. No forums, Reddit, or unattributed blogs. Do not state a non-obvious claim you cannot cite to one of these.
- **Sourcing priority (from spec):** (1) `github.com/karpathy/autoresearch` repo for the loop mechanics; (2) `docs.claude.com`/`code.claude.com`/`anthropic.com` for Claude-Code operation; (3) `arxiv.org` for agentic-research context; (4) `x.com` (Karpathy's own posts) for the agentic-engineering framing, by direct attribution only. Secondary tech journalism is corroboration, never the sole citation — omit a claim rather than hang it on an unattributed blog.
- **Validator:** `python3 tools/validate_okf.py` must print `0 violation(s)` before every commit. It checks frontmatter/`type`, that every root-relative `.md` link resolves, that concepts carry `# Sources`, and that references in `README.md`, `CLAUDE.md`, and the router skill resolve. `log.md` is exempt from frontmatter and `# Sources`; `index.md` is exempt from `# Sources`.
- **Commits:** atomic, Conventional Commits (`build:`, `feat:`, `docs:`). Work on branch `feat/autoresearch-bundle`.
- **Model policy:** research/extraction subagents use `sonnet`; synthesis/writing subagents use `opus`.

## File Structure

Created (13 bundle files + notes; 3 integration edits):

```
oks/autoresearch-best-practices/
  index.md                              # root progressive-disclosure entry (built LAST)
  log.md                                # dated change log
  loop/
    index.md                            # area index
    agent-research-loop.md
    spec-script-split.md
    single-file-context-constraint.md
    keep-or-revert-with-git.md
  running-with-claude-code/
    index.md                            # area index
    claude-code-as-the-agent.md
    prompting-the-search.md
    time-boxing-and-guardrails.md
  agentic-engineering/
    index.md                            # area index
    vibe-coding-to-agentic-engineering.md
    engineering-discipline.md
    karpathy-guidelines.md
```

Integration edits (repo root):
- `CLAUDE.md` — expand the source allowlist (add `github.com`, `arxiv.org`, `x.com`).
- `.claude/skills/oks-bundles/SKILL.md` — add a decision-table row and extend the skill `description`.
- `README.md` — add the bundle to its list/cross-references.

Non-committed working file:
- `<scratchpad>/autoresearch-research.md` — source-attributed research notes. `<scratchpad>` = `/tmp/claude-1000/-home-kalen-okf-bundles/ee1e5ee6-2895-47ed-8623-92ab1573a068/scratchpad`.

**Build order (validator-safe):** allowlist → `loop/` → `running-with-claude-code/` → `agentic-engineering/` → root `index.md` + registration. Each concept's `# Related` links point only to files that already exist at that commit (earlier areas + same area, plus existing bundles). Any forward cross-links (earlier area → later area) are added in the final task, when all targets exist.

---

## Task 1: Research pass (parallel Sonnet subagents)

**Deliverable:** `<scratchpad>/autoresearch-research.md` — a notes file where every fact carries an inline source URL from an allowlisted host. Not committed.

**Model:** dispatch 4 subagents with `model: sonnet` (agentType `Explore` or `general-purpose`), one per source cluster, in a single message so they run concurrently.

**Interfaces:**
- Produces: `autoresearch-research.md` with four labeled sections (Repo, ClaudeCode, Agentic, Corroboration), each a bulleted list of `claim — <url>` lines. Later writing tasks consume these facts and their URLs verbatim for `# Sources`.

- [ ] **Step 1: Dispatch the four research subagents (Sonnet, concurrent)**

Cluster A — **Repo mechanics** (`model: sonnet`): "Fetch and read https://github.com/karpathy/autoresearch (README and any docs). Extract, each with the exact source URL: the loop steps (propose/edit → run experiment → measure → keep or `git revert`); the Markdown-instruction-file vs single `.py`-training-script split; the ~630-line / fits-in-context-window design rationale; validation loss as the objective; time-boxing and overnight autonomy; release date. Return a bulleted list of `claim — url` lines. Only report facts actually present at the URL."

Cluster B — **Claude Code operation** (`model: sonnet`): "From docs.claude.com and code.claude.com only, extract with source URLs: how to run Claude Code non-interactively/headless for autonomous loops; permission/safety controls for unattended runs; subagent/model selection; being specific in instructions. Return `claim — url` lines."

Cluster C — **Agentic-research context** (`model: sonnet`): "Search arxiv.org for peer/preprint work on autonomous LLM research agents and the ML-research lifecycle (e.g. researcher-agent benchmarks). Return 2–4 papers as `title/finding — arxiv url` lines. Only arxiv.org."

Cluster D — **Karpathy framing + corroboration** (`model: sonnet`): "Find Karpathy's own posts (x.com) on the shift from 'vibe coding' to 'agentic engineering' (the ~80/20 manual-to-agent shift) and the community 'Karpathy Guidelines' / CLAUDE.md self-check rules; note the primary URL (x.com, or a github.com repo hosting the guidelines). Separately, list reputable secondary coverage (DataCamp, MarkTechPost, etc.) that only *corroborates* repo facts — label these 'corroboration, not for citation'. Return `claim — url` lines with the host clearly shown."

- [ ] **Step 2: Consolidate into the notes file**

Merge the four returns into `<scratchpad>/autoresearch-research.md` under the four section headers. For each claim keep the URL. Flag any claim whose only source is a non-allowlisted host as **UNCITABLE — corroboration only**.

- [ ] **Step 3: Verify coverage (the "test" for this task)**

Confirm the notes contain at least one allowlisted-host citation for each concept planned in Tasks 3–5 (13 concepts). List any concept with no citable primary source. For any gap, either (a) re-dispatch a targeted Sonnet subagent, or (b) note the concept must be written more conservatively (claims trimmed to what is citable). Do not commit anything in this task.

---

## Task 2: Expand the source allowlist

**Files:** Modify `CLAUDE.md` (the source-allowlist bullet under rule 4).

**Interfaces:**
- Produces: three new allowlisted hosts available to all later `# Sources` sections.

- [ ] **Step 1: Edit the allowlist**

In `CLAUDE.md`, rule 4 ("Sources"), append `github.com`, `arxiv.org`, and `x.com` to the "Allowed hosts" list, keeping the existing formatting. Add a short clause noting these are for the AutoResearch bundle's primary sources (Karpathy's repo, arXiv, and Karpathy's own posts).

- [ ] **Step 2: Run the validator**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)` (allowlist text is not a link/path reference, so nothing breaks).

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "build: expand CLAUDE.md source allowlist for autoresearch bundle"
```

---

## Task 3: `loop/` area — the AutoResearch mechanics

**Model:** one `opus` writing subagent (or main agent) for the whole area, consuming `autoresearch-research.md` Cluster A. Keep the area in one context.

**Files:**
- Create: `oks/autoresearch-best-practices/log.md`
- Create: `oks/autoresearch-best-practices/loop/index.md`
- Create: `oks/autoresearch-best-practices/loop/agent-research-loop.md`
- Create: `oks/autoresearch-best-practices/loop/spec-script-split.md`
- Create: `oks/autoresearch-best-practices/loop/single-file-context-constraint.md`
- Create: `oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md`

**Interfaces:**
- Consumes: `autoresearch-research.md` (Cluster A facts + URLs).
- Produces: four concept paths that later areas link back to; area `index.md`.

**Per-file content spec** (frontmatter: `type: OKF Concept` for concepts / `OKF Concept Index` for the area index; `timestamp: 2026-07-07T00:00:00Z`; `tags` include `autoresearch` + `karpathy`; `resource` = primary URL below):

- `agent-research-loop.md` — `resource:` the autoresearch repo URL. Body: the full propose → run time-boxed experiment → measure validation loss → keep-or-`git revert` cycle; runs autonomously, potentially overnight; the shift of human effort to prompt-engineering the search. `# Related`: the other three `loop/` concepts. `# Sources`: repo URL (+ any citable corroboration from Cluster A).
- `spec-script-split.md` — `resource:` repo URL. Body: the Markdown instruction file (what to try) vs the single `.py` training script (what gets edited); why the separation matters. `# Related`: `agent-research-loop.md`, `single-file-context-constraint.md`. `# Sources`: repo URL.
- `single-file-context-constraint.md` — `resource:` repo URL. Body: deliberately ~630 lines so the whole script fits the agent's context window and it keeps a holistic view; connect to the repo's own single-file discipline. `# Related`: `spec-script-split.md`, `agent-research-loop.md`. `# Sources`: repo URL.
- `keep-or-revert-with-git.md` — `resource:` repo URL. Body: validation loss as the accept/reject signal; `git revert` to discard any non-improving change; keeping only improvements. `# Related`: `agent-research-loop.md`, and cross-bundle `[atomic commits](/oks/git-best-practices/commits/atomic-commits.md)` (verify this path exists first with `ls`; if not, link to `/oks/git-best-practices/index.md`). `# Sources`: repo URL.
- `loop/index.md` — `type: OKF Concept Index`, `resource:` repo URL. Progressive-disclosure list linking the four concepts (mirror the style of `oks/claude-best-practices/subagents/index.md`). No `# Sources` needed.

- [ ] **Step 1: Verify any cross-bundle link targets exist**

Run: `ls oks/git-best-practices/commits/atomic-commits.md`
If it does not exist, use `/oks/git-best-practices/index.md` in `keep-or-revert-with-git.md` instead.

- [ ] **Step 2: Write `log.md`**

Mirror `oks/claude-best-practices/log.md`. First line: `# Change Log — AutoResearch Best Practices bundle`. Add: `2026-07-07 — bundle created` and a short paragraph noting initial authoring of the `loop/` area (subsequent tasks append lines).

- [ ] **Step 3: Write the four concept files + `loop/index.md`**

Author each file per the content spec above, grounding every non-obvious claim in a Cluster A URL. Frontmatter complete (all six fields). Plain root-relative `# Related` links only. Each concept ends with `# Sources`.

- [ ] **Step 4: Run the validator**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`. (All `# Related` links point within `loop/` or to existing bundles, so everything resolves.) Fix any reported violation and re-run until clean.

- [ ] **Step 5: Commit**

```bash
git add oks/autoresearch-best-practices/log.md oks/autoresearch-best-practices/loop/
git commit -m "feat: add loop area to autoresearch-best-practices bundle"
```

---

## Task 4: `running-with-claude-code/` area — operating the loop

**Model:** one `opus` writing subagent, consuming Cluster B (+ A) facts.

**Files:**
- Create: `oks/autoresearch-best-practices/running-with-claude-code/index.md`
- Create: `oks/autoresearch-best-practices/running-with-claude-code/claude-code-as-the-agent.md`
- Create: `oks/autoresearch-best-practices/running-with-claude-code/prompting-the-search.md`
- Create: `oks/autoresearch-best-practices/running-with-claude-code/time-boxing-and-guardrails.md`
- Modify: `oks/autoresearch-best-practices/log.md` (append a dated line for this area)

**Interfaces:**
- Consumes: `loop/` concept paths (for `# Related` backlinks — they exist now), Cluster B facts + URLs, existing `claude-best-practices` concepts.
- Produces: three concept paths the final area/root link back to.

**Per-file content spec:**

- `claude-code-as-the-agent.md` — `resource:` a `code.claude.com` headless/CLI docs URL. Body: Claude Code as the agent that edits the script and runs experiments; running it non-interactively for autonomous/overnight loops. `# Related`: `/oks/autoresearch-best-practices/loop/agent-research-loop.md`; cross-bundle `[headless mode](/oks/claude-best-practices/automation/headless-mode.md)` and `[delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md)`. `# Sources`: the `code.claude.com` URL(s) from Cluster B.
- `prompting-the-search.md` — `resource:` repo URL or a `docs.claude.com` "be specific" URL. Body: hyperparameter/architecture search reframed as prompt-engineering the agent to navigate the space; specific instructions beat vague ones. `# Related`: `/oks/autoresearch-best-practices/loop/agent-research-loop.md`; cross-bundle `[be specific in instructions](/oks/claude-best-practices/context/be-specific-in-instructions.md)`. `# Sources`: repo + `docs.claude.com` URLs.
- `time-boxing-and-guardrails.md` — `resource:` a `code.claude.com` permissions/safety URL. Body: time-boxed experiments, budgets, and safely letting the loop run unattended; permission modes / allowlists to contain blast radius. `# Related`: `/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md`; cross-bundle `[permission modes](/oks/claude-best-practices/safety/permission-modes.md)` (verify path). `# Sources`: `code.claude.com` URLs.
- `running-with-claude-code/index.md` — `type: OKF Concept Index`, area index linking the three concepts.

- [ ] **Step 1: Verify cross-bundle link targets exist**

Run a plain `ls` on each of: `oks/claude-best-practices/automation/headless-mode.md`, `oks/claude-best-practices/context/be-specific-in-instructions.md`, `oks/claude-best-practices/safety/permission-modes.md`, `oks/claude-best-practices/subagents/delegating-to-subagents.md`. For any path that does not exist, substitute the nearest existing file or the relevant area `index.md`.

- [ ] **Step 2: Write the three concept files + area `index.md`; append the `log.md` line**

Author per spec, grounding Claude-Code claims in Cluster B URLs. Append to `log.md`: `2026-07-07 — added running-with-claude-code area`.

- [ ] **Step 3: Run the validator**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`. Fix and re-run until clean.

- [ ] **Step 4: Commit**

```bash
git add oks/autoresearch-best-practices/running-with-claude-code/ oks/autoresearch-best-practices/log.md
git commit -m "feat: add running-with-claude-code area to autoresearch-best-practices bundle"
```

---

## Task 5: `agentic-engineering/` area — the adjacent discipline

**Model:** one `opus` writing subagent, consuming Cluster D (+ C) facts.

**Files:**
- Create: `oks/autoresearch-best-practices/agentic-engineering/index.md`
- Create: `oks/autoresearch-best-practices/agentic-engineering/vibe-coding-to-agentic-engineering.md`
- Create: `oks/autoresearch-best-practices/agentic-engineering/engineering-discipline.md`
- Create: `oks/autoresearch-best-practices/agentic-engineering/karpathy-guidelines.md`
- Modify: `oks/autoresearch-best-practices/log.md` (append a dated line)

**Interfaces:**
- Consumes: Cluster C/D facts + URLs; `loop/` and `running-with-claude-code/` paths for backlinks.
- Produces: three concept paths the root index links to.

**Per-file content spec** (these lean on `x.com` primary + `arxiv.org` context; every claim must trace to an allowlisted URL, else trim it):

- `vibe-coding-to-agentic-engineering.md` — `resource:` a Karpathy `x.com` post URL. Body: the shift from "vibe coding" (Karpathy's own coinage) to orchestrated agent workflows; the roughly 80/20 manual→agent shift, attributed directly to Karpathy. `# Related`: `/oks/autoresearch-best-practices/loop/agent-research-loop.md`, `engineering-discipline.md`. `# Sources`: `x.com` URL(s) (+ `arxiv.org` context if used).
- `engineering-discipline.md` — `resource:` `x.com` or `arxiv.org` URL. Body: agentic engineering as a discipline — spec design, diff review, eval design, security oversight, taste; pair capable agents with strict operating discipline. `# Related`: `vibe-coding-to-agentic-engineering.md`, `karpathy-guidelines.md`; cross-bundle `[spec-first development](/oks/claude-best-practices/planning/spec-first-development.md)` and `[independent review](/oks/claude-best-practices/verification/independent-review.md)` (verify paths). `# Sources`: `x.com`/`arxiv.org` URLs.
- `karpathy-guidelines.md` — `resource:` the primary URL hosting the guidelines (`github.com` repo if one hosts them, else Karpathy's `x.com` post). Body: the community CLAUDE.md rules — state assumptions, surface tradeoffs, minimal code (nothing speculative), the self-check protocol; frame as the operating discipline around autonomous loops. `# Related`: `engineering-discipline.md`, `/oks/autoresearch-best-practices/running-with-claude-code/time-boxing-and-guardrails.md`; cross-bundle `[CLAUDE.md as memory](/oks/claude-best-practices/context/claude-md-as-memory.md)` (verify path). `# Sources`: the primary URL (+ corroboration only if attributable).
- `agentic-engineering/index.md` — `type: OKF Concept Index`, area index linking the three concepts.

- [ ] **Step 1: Verify cross-bundle link targets exist**

Run a plain `ls` on each of: `oks/claude-best-practices/planning/spec-first-development.md`, `oks/claude-best-practices/verification/independent-review.md`, `oks/claude-best-practices/context/claude-md-as-memory.md`. Substitute the nearest existing file or area `index.md` for any that do not exist.

- [ ] **Step 2: Check citability before writing**

For each of the three concepts, confirm `autoresearch-research.md` has at least one allowlisted-host URL (`x.com`, `github.com`, or `arxiv.org`). If a claim's only support is secondary journalism, either soften/omit it or attribute it explicitly to Karpathy with the `x.com` URL. Do not invent sources.

- [ ] **Step 3: Write the three concept files + area `index.md`; append the `log.md` line**

Append to `log.md`: `2026-07-07 — added agentic-engineering area`.

- [ ] **Step 4: Run the validator**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`. Fix and re-run until clean.

- [ ] **Step 5: Commit**

```bash
git add oks/autoresearch-best-practices/agentic-engineering/ oks/autoresearch-best-practices/log.md
git commit -m "feat: add agentic-engineering area to autoresearch-best-practices bundle"
```

---

## Task 6: Root `index.md`, forward cross-links, and registration

**Files:**
- Create: `oks/autoresearch-best-practices/index.md`
- Modify: (optional) earlier concept files to add forward `# Related` links now that all targets exist
- Modify: `.claude/skills/oks-bundles/SKILL.md`
- Modify: `README.md`
- Modify: `oks/autoresearch-best-practices/log.md` (append final line)

**Interfaces:**
- Consumes: all three area `index.md` files (they exist now).
- Produces: the bundle's public entry point and its registration in the router + README.

- [ ] **Step 1: Write the root `index.md`**

`type: OKF Bundle Index`, `title: AutoResearch Best Practices`, `resource:` the autoresearch repo URL, full frontmatter. Mirror `oks/claude-best-practices/index.md`: an intro paragraph (link the OKF blog post `https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing`), a "Concept areas" list linking the three area `index.md` files with one-line summaries, and a "How to read this bundle" note. No `# Sources` required (it is an index).

- [ ] **Step 2: Add forward cross-links (optional polish)**

Where an earlier-area concept would naturally reference a later-area concept (e.g. `loop/agent-research-loop.md` → `running-with-claude-code/claude-code-as-the-agent.md`), add the link to that file's `# Related` section now. All targets exist, so links resolve. Keep it light — only genuinely related pairs.

- [ ] **Step 3: Register in the router skill**

In `.claude/skills/oks-bundles/SKILL.md`: (a) extend the frontmatter `description` with a clause for AutoResearch (autonomous ML-research loops, running them with Claude Code, agentic engineering); (b) add a decision-table row: `| Karpathy AutoResearch, autonomous ML-research loops, running research agents with Claude Code, agentic engineering | \`/oks/autoresearch-best-practices/index.md\` |`.

- [ ] **Step 4: Register in README**

In `README.md`, add the bundle to the bundle list/cross-references, mirroring how the other three bundles are listed, pointing to `/oks/autoresearch-best-practices/index.md`.

- [ ] **Step 5: Append the final `log.md` line**

Append: `2026-07-07 — added root index and registered bundle in router and README`.

- [ ] **Step 6: Run the validator (full repo)**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)` — including the aux-file reference checks on `README.md`, `CLAUDE.md`, and the router skill.

- [ ] **Step 7: Commit**

```bash
git add oks/autoresearch-best-practices/index.md oks/autoresearch-best-practices/ .claude/skills/oks-bundles/SKILL.md README.md
git commit -m "feat: register autoresearch-best-practices bundle in router and README"
```

---

## Task 7: Final verification

- [ ] **Step 1: Full validation**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`.

- [ ] **Step 2: Structure check**

Run: `find oks/autoresearch-best-practices -type f | sort`
Expected: 14 files — root `index.md` + `log.md`, and each of the three areas with its `index.md` plus its concepts (4 + 3 + 3).

- [ ] **Step 3: Sources-host audit**

Run: `grep -rhoE 'https?://[^ )]+' oks/autoresearch-best-practices | sed -E 's#https?://([^/]+)/?.*#\1#' | sort -u`
Expected: every host appears in the Global Constraints allowlist. Any host not on the list is a violation — fix the offending `# Sources` entry (replace with an allowlisted primary source or remove the claim) and re-run Task 7.

- [ ] **Step 4: Confirm clean tree and branch**

Run: `git status` and `git log --oneline -7`
Expected: clean working tree on `feat/autoresearch-bundle`; commits for allowlist, three areas, and registration present.

---

## Self-Review (completed by plan author)

- **Spec coverage:** allowlist expansion (Task 2) ✓; 3 areas / 10 concepts (Tasks 3–5) ✓; sourcing standard enforced (Global Constraints + Task 5 Step 2 + Task 7 Step 3) ✓; subagent/model policy (Task 1 Sonnet, Tasks 3–5 Opus) ✓; router + README + CLAUDE.md integration (Tasks 2, 6) ✓; validator green + atomic Conventional Commits (every task) ✓.
- **Placeholder scan:** no "TBD/handle appropriately" — each concept has a concrete content spec, resource, and source-host plan. Concept *prose* is written at execution from Task 1's researched, source-attributed notes (unavoidable for a research bundle) but each file's claims, `resource`, `# Related` targets, and citable hosts are specified.
- **Consistency:** area/concept paths are identical everywhere they appear (File Structure, per-file specs, `# Related` targets, commit `git add` lines). Build order is validator-safe: links only ever point to already-created files; forward links deferred to Task 6.
- **Note on ordering vs. spec commit plan:** the spec listed "scaffold (index, log)" second; this plan moves the *root* `index.md` to the final task (Task 6) so its links to area indexes resolve, and creates `log.md` with the first area (Task 3). Same end state, validator-green at every commit.
