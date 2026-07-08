# Agentic SDLC Best Practices Bundle — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the OKF bundle `oks/agentic-sdlc-best-practices/` (9 areas, 40 concepts) documenting SDLC best practices when AI agents do substantial engineering work, per the approved spec (`docs/superpowers/specs/2026-07-07-agentic-sdlc-best-practices-bundle-design.md`), passing `python3 tools/validate_okf.py` with `0 violation(s)`.

**Architecture:** A research phase (parallel Sonnet subagents produce quote-or-drop notes: every claim carries a verbatim snippet + exact URL) feeds a writing phase (Opus/Fable-tier, one area per subagent) that produces cross-linked Markdown concept files. The validator is the structural test harness after every area; a separate citation-integrity gate (the validator cannot check truth or hosts) runs before registration. Areas are built in a validator-safe order: `# Related` links point only to already-existing files; forward links are added in the final wiring task.

**Tech Stack:** Markdown + YAML frontmatter (OKF), `tools/validate_okf.py` (Python 3), git, curl (citation gate). No application code.

## Global Constraints

Copied from the repo `CLAUDE.md` and the approved spec. Every task's requirements implicitly include this section.

- **Concept file format:** one markdown file per concept; path is identity. YAML frontmatter with all six fields: `type`, `title`, `description`, `resource`, `tags`, `timestamp`. Use `type: Agentic SDLC Practice` for concepts, `type: OKF Concept Index` for area indexes, `type: OKF Bundle Index` for the root index. `timestamp: 2026-07-07T00:00:00Z`. `tags` always include `agentic-sdlc` plus the area name (e.g. `agent-harness`).
- **Structure:** bundle root has `index.md` (progressive disclosure) and `log.md` (dated line per change). Each area subdirectory has its own `index.md`.
- **Cross-links:** plain root-relative markdown links only — `[text](/oks/...md)`. No `#fragments`, no `"titles"` in the parens. Every concept ends with `# Related`.
- **Sources:** every concept (not `index.md`/`log.md`) ends with `# Sources` citing primary sources on allowlisted hosts only. Post-expansion allowlist adds: `kaggle.com`, `openai.com`, `cdn.openai.com`, `langchain.com`, `docs.langchain.com` (exact final list confirmed by Task 1 research — see Task 2). Already allowlisted and used here: `anthropic.com`, `docs.claude.com`, `code.claude.com`, `agents.md`, `github.com`, `arxiv.org`, `cloud.google.com`. A non-obvious claim that cannot be cited to an allowlisted host is **dropped, not hedged**.
- **Paraphrase, not copy:** concepts are written in the repo's own voice from structured notes; any direct quote is short, quote-marked, and attributed inline. Never reproduce tables/figures/multi-sentence passages from sources.
- **Date volatile claims inline:** version-bound facts get in-prose dating ("as of the May 2026 paper…", "as of mid-2026…"). Prefer durable principles where the point survives at higher altitude.
- **Guardrail-pairing invariant:** every concept recommending increased autonomy (headless, auto-fix, auto-merge, CI agents, higher change velocity, async delegation) MUST link in `# Related` to at least one human-gate/verification/anti-reward-hacking concept AND to `/oks/claude-best-practices/safety/index.md`. Files this applies to are marked **[GUARDRAIL-PAIR]** in their content spec.
- **Anchor paper:** "The New SDLC With Vibe Coding" (Osmani, Saboo, Kartakis; Google, May 2026). Canonical citation URL: `https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding`. Reading copy: local PDF at `<scratchpad>/seed-doc.pdf`. Referred to below as **[PAPER]**.
- **Validator:** `python3 tools/validate_okf.py` must print `0 violation(s)` before every commit.
- **Commits:** atomic, Conventional Commits. Work on branch `feat/agentic-sdlc-bundle`.
- **Model policy:** research/extraction subagents `sonnet`; synthesis/writing and review subagents `opus` (Fable-tier where available).
- `<scratchpad>` = `/tmp/claude-1000/-home-kalen-okf-bundles/0992ea14-ecfe-4304-870a-865f1d3d9da6/scratchpad`.

## File Structure

Created (51 bundle files; 3 integration edits). **These 40 concept filenames are FROZEN** — `# Related` links are written against this exact set; any rename after Task 1 requires a link-fixup sweep across the bundle.

```
oks/agentic-sdlc-best-practices/
  index.md                                  # root entry (built LAST, Task 13)
  log.md                                    # created in Task 3, appended every area
  foundations/                              # Task 3 (7 concepts)
    index.md
    from-syntax-to-intent.md
    vibe-coding-and-the-spectrum.md
    when-vibe-coding-is-appropriate.md
    trust-calibration-and-the-80-percent-problem.md
    conductor-and-orchestrator-roles.md
    economics-of-agentic-development.md
    anatomy-of-a-coding-agent.md            # CANDIDATE — confirmed in Task 1
  context-engineering/                      # Task 4 (4 concepts)
    index.md
    context-engineering-over-prompt-engineering.md
    curating-the-context-window.md
    compaction-and-long-horizon-context.md
    memory-and-knowledge-capture.md
  requirements-and-planning/                # Task 5 (3 concepts)
    index.md
    specs-as-the-primary-artifact.md
    task-decomposition.md
    requirements-elicitation-with-ai.md
  design-and-architecture/                  # Task 6 (3 concepts)
    index.md
    architecture-decisions-with-ai.md
    design-docs-as-agent-context.md
    designing-for-agent-legibility.md
  implementation/                           # Task 7 (3 concepts)
    index.md
    tdd-as-agent-guardrail.md
    small-verifiable-increments.md
    human-in-the-loop-checkpoints.md
  verification-and-review/                  # Task 8 (5 concepts)
    index.md
    agent-written-tests-and-reward-hacking.md
    evals-for-agentic-changes.md
    reviewing-ai-generated-code.md
    adversarial-multi-agent-review.md
    securing-agent-generated-code.md
  operations-and-evolution/                 # Task 9 (3 concepts)
    index.md
    agents-in-ci-cd.md
    monitoring-rollback-and-progressive-delivery.md
    large-scale-refactors-and-migrations.md
  agent-harness/                            # Task 10 (7 concepts)
    index.md
    harness-engineering.md
    system-prompt-design.md
    tool-design-for-agents.md
    middleware-and-context-management.md
    model-selection-and-routing.md
    the-factory-model.md
    workflows-vs-agents.md                  # CANDIDATE — confirmed in Task 1
  applications/                             # Task 11 (5 concepts)
    index.md
    authoring-an-agents-md.md
    generating-system-prompts.md
    designing-repo-tools-and-middleware.md
    skills-libraries.md
    adopting-agentic-sdlc.md
```

Integration edits (repo root):
- `CLAUDE.md` — expand the source allowlist (Task 2).
- `.claude/skills/oks-bundles/SKILL.md` — decision-table row + `description` triggers (Task 13).
- `README.md` — bundle list entry (Task 13).

Non-committed working files:
- `<scratchpad>/agentic-sdlc-research.md` — quote-or-drop research notes.
- `<scratchpad>/citation-audit.md` — Task 12 gate results.

**Build order (validator-safe):** allowlist → foundations → context-engineering → requirements-and-planning → design-and-architecture → implementation → verification-and-review → operations-and-evolution → agent-harness → applications → citation gate → root index + forward links + registration. Each area's `# Related` links point only to earlier/same-area files and existing bundles; genuinely-needed forward links (earlier area → later area) are listed in each area task and added in Task 13 when all targets exist.

**Known-good cross-bundle targets** (verified to exist; verify again with `ls` before use):
`/oks/claude-best-practices/planning/spec-first-development.md`, `planning/plan-mode.md`, `workflows/test-driven-development.md`, `workflows/explore-plan-code-commit.md`, `context/claude-md-as-memory.md`, `context/managing-the-context-window.md`, `context/be-specific-in-instructions.md`, `verification/tests-and-checks-as-guardrails.md`, `verification/independent-review.md`, `subagents/parallel-agents.md`, `subagents/choosing-a-model.md`, `subagents/delegating-to-subagents.md`, `safety/index.md`, `safety/permission-modes.md`, `safety/sandboxing-and-review.md`, `automation/ci-and-github-actions.md`, `automation/headless-mode.md` — all under `/oks/claude-best-practices/`.
`/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md`, `context-files/progressive-disclosure.md`, `context-files/precedence-and-scope.md`, `knowledge/docs-for-agents.md`, `skills/what-is-a-skill.md`, `skills/skill-file-format.md`, `practices/guardrails-and-permissions.md`.
`/oks/git-best-practices/commits/atomic-commits.md` (verify), `/oks/autoresearch-best-practices/agentic-engineering/vibe-coding-to-agentic-engineering.md`.

---

## Task 1: Research pass (parallel Sonnet subagents, quote-or-drop)

**Deliverable:** `<scratchpad>/agentic-sdlc-research.md`. Every entry has the form:

```
- CLAIM: <one-sentence fact in your own words>
  QUOTE: "<verbatim supporting snippet from the source>"
  URL: <exact url>   [AREA: <target area(s)>]
```

Synthesis tasks may only assert what has a QUOTE line. Not committed.

**Model:** dispatch 6 subagents with `model: sonnet` in a single message (concurrent).

**Interfaces:**
- Produces: `agentic-sdlc-research.md` with six labeled sections (Paper, Anthropic, OpenAI, LangChain, AgentsMd+Superpowers, Arxiv), a **final-host list** for Task 2, and a **candidate-concept verdict** (see Step 3).

- [ ] **Step 1: Dispatch the six research subagents (Sonnet, concurrent)**

Cluster **Paper** (`model: sonnet`): "Read the local PDF `<scratchpad>/seed-doc.pdf` (51 pages; use the Read tool's `pages` param, max 20/request — read it in 3 passes). It is Google's 'The New SDLC With Vibe Coding'. For EACH of these topics, extract 2-5 facts in quote-or-drop format (CLAIM / verbatim QUOTE / URL `https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding` plus page number / AREA): the syntax→intent shift; what vibe coding is + the spectrum to agentic engineering; when vibe coding is appropriate + the crossover point; the 80% problem + trust calibration; conductor vs orchestrator roles; the economics (CapEx/OpEx, hidden debt, context engineering as financial lever); the AI-agents refresher ('anatomy of an agent'); context engineering; each SDLC phase section (requirements/planning, design/architecture, implementation, testing/QA, code review & deployment, maintenance & evolution); the factory model; harness engineering ('what's in the harness', harness in SDLC, the ~10% model claim); intelligent model routing; dynamic context and skills; security/guardrails mentions; 'Where to start' (individuals, leaders, organizations). Also report the paper's exact page count, title, authors, and publication month as printed."

Cluster **Anthropic** (`model: sonnet`): "From anthropic.com, docs.claude.com, and code.claude.com ONLY, extract quote-or-drop facts (CLAIM/QUOTE/URL/AREA) from: (1) https://www.anthropic.com/engineering/building-effective-agents — especially the workflows-vs-agents distinction, when NOT to use agents, orchestrator-workers pattern; (2) https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — context curation, compaction, sub-agent isolation, just-in-time retrieval; (3) https://www.anthropic.com/engineering/writing-tools-for-agents — tool naming, descriptions, token-efficient outputs, error messages; (4) https://www.anthropic.com/engineering/claude-code-best-practices (or its code.claude.com equivalent) — TDD with agents, verification loops, small steps; (5) any anthropic.com material on system-prompt design altitude / heuristics-over-rules. Report exact final URLs after redirects."

Cluster **OpenAI** (`model: sonnet`): "Fetch https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf (landing: openai.com). Extract quote-or-drop facts (CLAIM/QUOTE/URL/AREA) on: agent definition and when to build one; model selection guidance; tool design; instruction/prompt design; single-agent vs multi-agent orchestration; guardrails (types, layered defense); human-in-the-loop escalation. Also check openai.com for any published material on AGENTS.md or agentic coding practices; report exact URLs and hosts."

Cluster **LangChain** (`model: sonnet`): "From langchain.com and docs.langchain.com, extract quote-or-drop facts (CLAIM/QUOTE/URL/AREA) from: (1) https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering — the +13.7-point Terminal-Bench-2.0 result (52.8%→66.5%, model fixed at GPT-5.2-Codex), what harness changes drove it (system prompt, tools, middleware), the definition of harness engineering; (2) docs.langchain.com deepagents/middleware docs — what middleware is, context-management middleware (summarization, context editing); (3) LangChain's context-engineering material IF it lives on langchain.com or docs.langchain.com — if it only exists on blog.langchain.dev, report that fact explicitly with the URL and DO NOT extract from it (host decision needed). Report the exact host of every URL used."

Cluster **AgentsMd+Superpowers** (`model: sonnet`): "Extract quote-or-drop facts (CLAIM/QUOTE/URL/AREA) from: (1) https://agents.md/ — what AGENTS.md is, what belongs in it, placement/precedence, relation to README; (2) https://github.com/obra/superpowers — what the superpowers skills library is, how skills are structured/triggered, the process-skills-first idea (README + representative skill files). Only agents.md and github.com URLs."

Cluster **Arxiv** (`model: sonnet`): "Search arxiv.org for 2-4 papers directly supporting these bundle topics: LLM agents gaming/reward-hacking tests or evaluation; benchmark evaluation of coding agents (e.g. SWE-bench, Terminal-Bench lineage); security of LLM-generated code. Return CLAIM/QUOTE (from abstract)/URL lines. Only arxiv.org. These are supporting citations, not anchors — 2-4 max."

- [ ] **Step 2: Consolidate into the notes file**

Merge the six returns into `<scratchpad>/agentic-sdlc-research.md` under six section headers, preserving CLAIM/QUOTE/URL/AREA structure. Add a `## Final host list` section: the exact set of new hosts actually needed by the collected URLs (expected: `kaggle.com`, `openai.com`, `cdn.openai.com`, `langchain.com`, `docs.langchain.com`; add/remove only per evidence — e.g. if LangChain context-engineering exists only on a `langchain.dev` host, decide: prefer docs.langchain.com equivalents; only add a host if a concept genuinely needs it).

- [ ] **Step 3: Candidate-concept verdict + coverage check (the "test" for this task)**

(a) **Candidates:** confirm `anatomy-of-a-coding-agent.md` (paper's agent refresher + harness-contents material) and `workflows-vs-agents.md` (Anthropic's building-effective-agents distinction) each have ≥2 quote-backed claims with distinct content not already in another planned concept or existing bundle. Record verdict in the notes file. If either fails, drop it from the inventory (adjust Task 3/10 file lists and Task 13 counts) and **report the shortfall to the user before proceeding past this task** (spec: no padding; user asked to be told).
(b) **Coverage:** confirm every one of the 40 planned concepts has ≥1 quote-backed claim on an allowlisted host. For gaps: re-dispatch one targeted Sonnet subagent, or trim that concept's planned claims to what is citable. List any concept still uncovered — same user report as (a).

---

## Task 2: Expand the source allowlist

**Files:** Modify `CLAUDE.md` (rule 4, "Sources").

**Interfaces:**
- Consumes: `## Final host list` from Task 1.
- Produces: expanded allowlist for all later `# Sources` sections.

- [ ] **Step 1: Edit the allowlist**

In `CLAUDE.md` rule 4, append the Task-1-confirmed hosts (expected: `kaggle.com`, `openai.com`, `cdn.openai.com`, `langchain.com`, `docs.langchain.com`) to the "Allowed hosts" list, keeping the existing formatting. Replace the existing sentence "These three are for the AutoResearch bundle's primary sources…" with a compact note covering both bundles, e.g.: "`github.com`, `arxiv.org`, `x.com` serve the AutoResearch bundle (Karpathy's repo, papers, his posts); `kaggle.com` (Google-published whitepapers), `openai.com`/`cdn.openai.com`, and `langchain.com`/`docs.langchain.com` serve the agentic-SDLC bundle's provider primary sources."

- [ ] **Step 2: Run the validator**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`.

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "build: expand CLAUDE.md source allowlist for agentic-sdlc bundle"
```

---

## Task 3: `foundations/` area

**Model:** one `opus` writing subagent for the whole area, consuming the Paper section of the notes (plus Anthropic for spectrum corroboration). Give it: the notes file path, the frozen inventory (File Structure above), the Global Constraints, and the per-file specs below.

**Files:**
- Create: `oks/agentic-sdlc-best-practices/log.md`
- Create: `oks/agentic-sdlc-best-practices/foundations/index.md`
- Create: the 7 `foundations/` concepts listed in File Structure (6 if `anatomy-of-a-coding-agent.md` was dropped in Task 1).

**Interfaces:**
- Consumes: notes file; existing-bundle paths (verify with `ls`).
- Produces: 7 concept paths that later areas back-link; `foundations/index.md`; `log.md`.

**Per-file content spec** (all: frontmatter per Global Constraints; `resource:` = [PAPER] URL unless stated; `# Sources` = [PAPER] URL + any other note-backed URLs used):

- `from-syntax-to-intent.md` — the job shift from writing syntax to expressing intent and verifying outcomes; what the engineer still owns. Dated framing: "as of the May 2026 paper". `# Related`: `vibe-coding-and-the-spectrum.md`, `conductor-and-orchestrator-roles.md`.
- `vibe-coding-and-the-spectrum.md` — what vibe coding is and the paper's maturity spectrum to agentic engineering (structure: specs, guardrails, evals, review). Karpathy's coinage/arc is linked, not restated: `# Related` includes `/oks/autoresearch-best-practices/agentic-engineering/vibe-coding-to-agentic-engineering.md`, plus `when-vibe-coding-is-appropriate.md`.
- `when-vibe-coding-is-appropriate.md` — prototypes/throwaway vs production; the crossover point where vibe coding gets more expensive per feature than engineering rigor. `# Related`: `vibe-coding-and-the-spectrum.md`, `economics-of-agentic-development.md`.
- `trust-calibration-and-the-80-percent-problem.md` — verification burden as the new bottleneck; the paper's 80% problem (impressive demo ≠ shippable last mile); calibrating review depth to stakes. `# Related`: `when-vibe-coding-is-appropriate.md`; forward link to `/oks/agentic-sdlc-best-practices/verification-and-review/reviewing-ai-generated-code.md` deferred to Task 13.
- `conductor-and-orchestrator-roles.md` **[GUARDRAIL-PAIR]** — the developer's evolving role: conductor (hands-on, real-time direction) vs orchestrator (async multi-agent delegation); which mode fits which work. `# Related`: `from-syntax-to-intent.md`, `/oks/claude-best-practices/subagents/delegating-to-subagents.md`, `/oks/claude-best-practices/safety/index.md`; forward link to `implementation/human-in-the-loop-checkpoints.md` deferred to Task 13.
- `economics-of-agentic-development.md` — vibe coding = low CapEx / high OpEx (hidden debt), agentic engineering = the reverse; context engineering as a financial lever. `# Related`: `when-vibe-coding-is-appropriate.md`; forward link to `context-engineering/context-engineering-over-prompt-engineering.md` deferred to Task 13.
- `anatomy-of-a-coding-agent.md` (if confirmed) — model + tools + context + loop; the paper's refresher framing of what an agent is, as groundwork for harness engineering. `# Related`: `from-syntax-to-intent.md`; forward link to `agent-harness/harness-engineering.md` deferred to Task 13.
- `foundations/index.md` — `type: OKF Concept Index`; progressive-disclosure list of the area's concepts with one-line summaries (mirror `oks/claude-best-practices/planning/index.md` style).

- [ ] **Step 1: Verify cross-bundle link targets** — `ls` each existing-bundle path used above; substitute the nearest existing file or area index for any miss.
- [ ] **Step 2: Write `log.md`** — `# Change Log — Agentic SDLC Best Practices bundle`; first line: `2026-07-07 — bundle created; foundations area authored`.
- [ ] **Step 3: Write the concepts + area index** per spec, every non-obvious claim backed by a QUOTE line in the notes; paraphrase-not-copy.
- [ ] **Step 4: Run the validator** — `python3 tools/validate_okf.py` → `0 violation(s)`; fix and re-run until clean.
- [ ] **Step 5: Commit**

```bash
git add oks/agentic-sdlc-best-practices/log.md oks/agentic-sdlc-best-practices/foundations/
git commit -m "feat: add foundations area to agentic-sdlc-best-practices bundle"
```

---

## Task 4: `context-engineering/` area

**Model:** one `opus` subagent; consumes Paper + Anthropic + LangChain notes.

**Files:** Create `context-engineering/index.md` + the 4 concepts; append `log.md` line `2026-07-07 — added context-engineering area`.

**Interfaces:** Consumes `foundations/` paths; produces 4 concept paths.

**Per-file content spec:**

- `context-engineering-over-prompt-engineering.md` — `resource:` Anthropic context-engineering URL. Curating everything the model sees (instructions, files, tools, history), not just the prompt; the paper's "context engineering: the real skill". `# Related`: `/oks/agentic-sdlc-best-practices/foundations/from-syntax-to-intent.md`, `curating-the-context-window.md`.
- `curating-the-context-window.md` — `resource:` Anthropic context-engineering URL. Include/exclude decisions; context as finite budget; signal-to-noise; just-in-time retrieval. Links progressive-disclosure mechanics instead of restating: `# Related`: `/oks/ai-agent-repo-structure/context-files/progressive-disclosure.md`, `/oks/claude-best-practices/context/managing-the-context-window.md`, `compaction-and-long-horizon-context.md`.
- `compaction-and-long-horizon-context.md` — `resource:` Anthropic context-engineering URL. Summarization/compaction, handoffs, sub-agent context isolation for long tasks (Anthropic + LangChain middleware notes). `# Related`: `curating-the-context-window.md`, `/oks/claude-best-practices/subagents/delegating-to-subagents.md`; forward link to `agent-harness/middleware-and-context-management.md` deferred to Task 13.
- `memory-and-knowledge-capture.md` — `resource:` best note-backed URL (Anthropic or [PAPER]). What to persist across sessions and feed back into repo context (decisions, conventions, lessons); the discipline, not the Claude-specific mechanics. `# Related`: `/oks/claude-best-practices/context/claude-md-as-memory.md`, `/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md`, `curating-the-context-window.md`.
- `context-engineering/index.md` — area index.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls` each).
- [ ] **Step 2: Write the concepts + area index; append the `log.md` line.**
- [ ] **Step 3: Run the validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/context-engineering/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add context-engineering area to agentic-sdlc-best-practices bundle"
```

---

## Task 5: `requirements-and-planning/` area

**Model:** one `opus` subagent; consumes Paper (requirements/planning phase section) + OpenAI (instruction design) notes.

**Files:** Create `requirements-and-planning/index.md` + the 3 concepts; append `log.md` line `2026-07-07 — added requirements-and-planning area`.

**Per-file content spec:**

- `specs-as-the-primary-artifact.md` — `resource:` [PAPER] URL. Specs as what agents build from; ambiguity costs multiply when the builder is an agent; plan review as the cheapest quality gate; plan-then-execute separation. Named deliberately to avoid colliding with the Claude-specific file it links. `# Related`: `/oks/claude-best-practices/planning/spec-first-development.md`, `/oks/claude-best-practices/planning/plan-mode.md`, `task-decomposition.md`.
- `task-decomposition.md` — `resource:` [PAPER] URL (or Anthropic building-effective-agents URL if better backed). Agent-sized, independently verifiable units; decomposition as the orchestrator's core skill. `# Related`: `specs-as-the-primary-artifact.md`, `/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md`; forward link to `implementation/small-verifiable-increments.md` deferred to Task 13.
- `requirements-elicitation-with-ai.md` — `resource:` [PAPER] URL. Agents interrogating/refining requirements (brainstorming, PRD drafting, surfacing unstated assumptions); human owns acceptance. `# Related`: `specs-as-the-primary-artifact.md`.
- `requirements-and-planning/index.md` — area index.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls`).
- [ ] **Step 2: Write files; append `log.md` line.**
- [ ] **Step 3: Validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/requirements-and-planning/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add requirements-and-planning area to agentic-sdlc-best-practices bundle"
```

---

## Task 6: `design-and-architecture/` area

**Model:** one `opus` subagent; consumes Paper (design/architecture phase) notes.

**Files:** Create `design-and-architecture/index.md` + the 3 concepts; append `log.md` line `2026-07-07 — added design-and-architecture area`.

**Per-file content spec (all `resource:` [PAPER] URL unless a better note-backed URL exists):**

- `architecture-decisions-with-ai.md` — agents as design partners: exploring alternatives, stress-testing trade-offs; humans own the decision and its rationale. `# Related`: `/oks/agentic-sdlc-best-practices/requirements-and-planning/specs-as-the-primary-artifact.md`, `design-docs-as-agent-context.md`.
- `design-docs-as-agent-context.md` — design docs written to be consumed by agents downstream (explicit constraints, interfaces, non-goals); docs as durable context, not ceremony. `# Related`: `/oks/agentic-sdlc-best-practices/context-engineering/memory-and-knowledge-capture.md`, `/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md`.
- `designing-for-agent-legibility.md` — modularity, clear boundaries, small focused files, consistent conventions — architecture choices that make codebases agents can work in reliably. `# Related`: `design-docs-as-agent-context.md`, `/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md`.
- `design-and-architecture/index.md` — area index.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls`).
- [ ] **Step 2: Write files; append `log.md` line.**
- [ ] **Step 3: Validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/design-and-architecture/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add design-and-architecture area to agentic-sdlc-best-practices bundle"
```

---

## Task 7: `implementation/` area

**Model:** one `opus` subagent; consumes Paper (implementation phase) + Anthropic (claude-code best practices) notes.

**Files:** Create `implementation/index.md` + the 3 concepts; append `log.md` line `2026-07-07 — added implementation area`.

**Per-file content spec:**

- `tdd-as-agent-guardrail.md` — `resource:` Anthropic claude-code-best-practices URL (or [PAPER]). Tests-first as the executable spec constraining agent code; provider-general framing; the Claude-specific workflow is linked, not restated. `# Related`: `/oks/claude-best-practices/workflows/test-driven-development.md`, `small-verifiable-increments.md`; forward link to `verification-and-review/agent-written-tests-and-reward-hacking.md` deferred to Task 13.
- `small-verifiable-increments.md` — `resource:` [PAPER] URL. Short leash: small diffs, checkpoint cadence, verify-then-continue; commit hygiene linked, not restated. `# Related`: `/oks/git-best-practices/commits/atomic-commits.md` (verify; else `/oks/git-best-practices/index.md`), `tdd-as-agent-guardrail.md`, `/oks/agentic-sdlc-best-practices/requirements-and-planning/task-decomposition.md`.
- `human-in-the-loop-checkpoints.md` — `resource:` OpenAI guide URL (human-in-the-loop/escalation section) or [PAPER]. THE cross-cutting "which gates stay human" concept: spec approval, security-sensitive code, irreversible/outward-facing actions; autonomy dials; escalation triggers. `# Related`: `/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md`, `/oks/claude-best-practices/safety/permission-modes.md`; forward links to `verification-and-review/adversarial-multi-agent-review.md` and `operations-and-evolution/agents-in-ci-cd.md` deferred to Task 13.
- `implementation/index.md` — area index.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls`).
- [ ] **Step 2: Write files; append `log.md` line.**
- [ ] **Step 3: Validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/implementation/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add implementation area to agentic-sdlc-best-practices bundle"
```

---

## Task 8: `verification-and-review/` area

**Model:** one `opus` subagent; consumes Paper (testing/QA + code-review phases) + OpenAI (guardrails) + Arxiv notes.

**Files:** Create `verification-and-review/index.md` + the 5 concepts; append `log.md` line `2026-07-07 — added verification-and-review area`.

**Per-file content spec:**

- `agent-written-tests-and-reward-hacking.md` — `resource:` [PAPER] URL (+ arXiv if note-backed). Agent-generated tests and their failure modes (weak/tautological assertions); agents gaming tests (weakening/deleting to pass); guardrails: protected test files, human review of test diffs, mutation-style spot checks. `# Related`: `/oks/agentic-sdlc-best-practices/implementation/tdd-as-agent-guardrail.md`, `/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md`.
- `evals-for-agentic-changes.md` — `resource:` [PAPER] URL or LangChain URL. Task-level evals on your codebase vs public benchmarks; evals as the harness's regression suite (the +13.7 case was measured, not vibes — cite LangChain). `# Related`: `agent-written-tests-and-reward-hacking.md`; forward link to `agent-harness/harness-engineering.md` deferred to Task 13.
- `reviewing-ai-generated-code.md` — `resource:` [PAPER] URL. What changes when the author is an agent: volume, plausible-but-wrong code, reviewer-attention economics; AI-assisted first-pass triage; what still goes to humans. `# Related`: `/oks/agentic-sdlc-best-practices/foundations/trust-calibration-and-the-80-percent-problem.md`, `/oks/claude-best-practices/verification/independent-review.md`, `adversarial-multi-agent-review.md`.
- `adversarial-multi-agent-review.md` — `resource:` best note-backed URL (Anthropic orchestrator-workers or [PAPER]). Panels of skeptical reviewers with distinct mandates; verification passes on findings; why diverse lenses beat redundant clones. `# Related`: `reviewing-ai-generated-code.md`, `/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md`, `/oks/claude-best-practices/subagents/parallel-agents.md`.
- `securing-agent-generated-code.md` — `resource:` OpenAI guide URL (guardrails) or [PAPER]. Security posture for AI-authored changes: layered guardrails, dependency/injection review, provenance of generated code; security-sensitive diffs always human-gated. `# Related`: `reviewing-ai-generated-code.md`, `/oks/claude-best-practices/safety/sandboxing-and-review.md`, `/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md`.
- `verification-and-review/index.md` — area index.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls`).
- [ ] **Step 2: Write files; append `log.md` line.**
- [ ] **Step 3: Validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/verification-and-review/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add verification-and-review area to agentic-sdlc-best-practices bundle"
```

---

## Task 9: `operations-and-evolution/` area

**Model:** one `opus` subagent; consumes Paper (code review & deployment + maintenance & evolution phases) notes.

**Files:** Create `operations-and-evolution/index.md` + the 3 concepts; append `log.md` line `2026-07-07 — added operations-and-evolution area`.

**Per-file content spec (all `resource:` [PAPER] URL unless better backed):**

- `agents-in-ci-cd.md` **[GUARDRAIL-PAIR]** — agents in pipelines: automated fixes, PR bots, headless runs; CI stays the source of truth; never let the agent own its own merge gate. `# Related`: `/oks/claude-best-practices/automation/ci-and-github-actions.md`, `/oks/claude-best-practices/automation/headless-mode.md`, `/oks/agentic-sdlc-best-practices/verification-and-review/agent-written-tests-and-reward-hacking.md`, `/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md`, `/oks/claude-best-practices/safety/index.md`.
- `monitoring-rollback-and-progressive-delivery.md` **[GUARDRAIL-PAIR]** — observability and fast rollback as the safety net for higher change velocity; flags/canaries/staged rollout when agent-authored change volume rises. `# Related`: `agents-in-ci-cd.md`, `/oks/agentic-sdlc-best-practices/verification-and-review/reviewing-ai-generated-code.md`, `/oks/claude-best-practices/safety/index.md`.
- `large-scale-refactors-and-migrations.md` — mechanical sweeps, dependency upgrades, migrations as supervised agent campaigns; verification at scale; sampling + full-suite gates. `# Related`: `agents-in-ci-cd.md`, `/oks/agentic-sdlc-best-practices/implementation/small-verifiable-increments.md`, `/oks/claude-best-practices/subagents/parallel-agents.md`.
- `operations-and-evolution/index.md` — area index.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls`).
- [ ] **Step 2: Write files; append `log.md` line.**
- [ ] **Step 3: Validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/operations-and-evolution/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add operations-and-evolution area to agentic-sdlc-best-practices bundle"
```

---

## Task 10: `agent-harness/` area

**Model:** one `opus` subagent; consumes LangChain + Anthropic + OpenAI + Paper (harness engineering, factory model, model routing) notes. This is the bundle's centerpiece area — give the subagent the full LangChain and Anthropic note sections.

**Files:** Create `agent-harness/index.md` + the 7 concepts (6 if `workflows-vs-agents.md` was dropped in Task 1); append `log.md` line `2026-07-07 — added agent-harness area`.

**Per-file content spec:**

- `harness-engineering.md` — `resource:` LangChain harness-engineering URL. The harness (system prompt + tools + middleware + context management) as an engineering surface; the paper's "model is ~10% of the system" thesis; the LangChain case: +13.7 points on Terminal Bench 2.0 (52.8%→66.5%, GPT-5.2-Codex fixed) from harness changes alone — dated "as of late 2026"/per notes. `# Related`: `/oks/agentic-sdlc-best-practices/foundations/anatomy-of-a-coding-agent.md` (if present, else `from-syntax-to-intent.md`), `system-prompt-design.md`, `tool-design-for-agents.md`, `middleware-and-context-management.md`, `/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md`.
- `system-prompt-design.md` — `resource:` best note-backed Anthropic/OpenAI URL. Structure, altitude (heuristics over hardcoded rules), examples, common failure modes (over-specification, stale instructions). `# Related`: `harness-engineering.md`; forward link to `applications/generating-system-prompts.md` deferred to Task 13.
- `tool-design-for-agents.md` — `resource:` Anthropic writing-tools-for-agents URL. Naming, descriptions as prompts, token-efficient outputs, error messages that teach the agent; consolidation over proliferation. `# Related`: `harness-engineering.md`; forward link to `applications/designing-repo-tools-and-middleware.md` deferred to Task 13.
- `middleware-and-context-management.md` — `resource:` docs.langchain.com middleware URL. Middleware between loop and model: summarization/compaction, context editing, guardrail hooks, caching; dated inline ("LangChain's middleware API as of mid-2026"). `# Related`: `harness-engineering.md`, `/oks/agentic-sdlc-best-practices/context-engineering/compaction-and-long-horizon-context.md`.
- `model-selection-and-routing.md` — `resource:` [PAPER] URL (intelligent model routing). Matching model tier to task complexity as a cost/quality lever; routing simple work down, hard work up. `# Related`: `harness-engineering.md`, `/oks/claude-best-practices/subagents/choosing-a-model.md`.
- `the-factory-model.md` — `resource:` [PAPER] URL. Building the system that builds the software: invest in harness, evals, and skills, not just output; treat the agent+harness as a product with its own SDLC. `# Related`: `harness-engineering.md`, `/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md`; forward link to `applications/skills-libraries.md` deferred to Task 13.
- `workflows-vs-agents.md` (if confirmed) — `resource:` Anthropic building-effective-agents URL. When a predefined workflow beats an autonomous agent: deterministic orchestration for known shapes, agency for open-ended work; start simple. `# Related`: `harness-engineering.md`, `/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md`.
- `agent-harness/index.md` — area index.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls`).
- [ ] **Step 2: Write files; append `log.md` line.**
- [ ] **Step 3: Validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/agent-harness/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add agent-harness area to agentic-sdlc-best-practices bundle"
```

---

## Task 11: `applications/` area

**Model:** one `opus` subagent. This area is the bundle's payoff: **every concept must contain an explicit reusable procedure — a numbered checklist or annotated template — not just prose** (spec actionability requirement). Give the subagent the AgentsMd+Superpowers notes plus the full frozen inventory (its procedures reference the other areas).

**Files:** Create `applications/index.md` + the 5 concepts; append `log.md` line `2026-07-07 — added applications area`.

**Per-file content spec:**

- `authoring-an-agents-md.md` **[GUARDRAIL-PAIR]** — `resource:` `https://agents.md/`. A numbered procedure for producing a repo-specific AGENTS.md. MUST open with the **derive-from-evidence step**: inspect the target repo (tests present? review flow? CI? commit style?) and encode its *actual* practices, flagging gaps as recommendations, not asserting ideals as current practice; default the output AGENTS.md to conservative autonomy. Then: what belongs (build/test commands, conventions, SDLC gates, guardrails) vs what agents derive from code; placement/precedence handed off inline to `/oks/ai-agent-repo-structure/context-files/agents-md-and-claude-md.md` and `/oks/ai-agent-repo-structure/context-files/precedence-and-scope.md`. Include a skeleton AGENTS.md template (section headings + one-line guidance each, in the repo's own words — not copied from any source). `# Related`: those two repo-structure files, `/oks/agentic-sdlc-best-practices/foundations/trust-calibration-and-the-80-percent-problem.md`, `/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md`, `/oks/claude-best-practices/safety/index.md`. `# Sources`: agents.md (+ any note-backed provider URL).
- `generating-system-prompts.md` — `resource:` best note-backed URL (Anthropic/OpenAI). A numbered procedure for turning repo/SDLC knowledge into a coding-agent system prompt: gather (from AGENTS.md/docs), set altitude, encode gates and verification loops, add examples, evaluate and iterate (evals, not vibes). `# Related`: `/oks/agentic-sdlc-best-practices/agent-harness/system-prompt-design.md`, `authoring-an-agents-md.md`, `/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md`.
- `designing-repo-tools-and-middleware.md` — `resource:` LangChain harness-engineering URL. A numbered procedure: mine SDLC pain points → decide prompt-instruction vs tool vs middleware (when a tool beats an instruction) → design per tool-design principles → measure with evals (the +13.7 case as the motivating example). `# Related`: `/oks/agentic-sdlc-best-practices/agent-harness/tool-design-for-agents.md`, `/oks/agentic-sdlc-best-practices/agent-harness/middleware-and-context-management.md`, `generating-system-prompts.md`.
- `skills-libraries.md` — `resource:` `https://github.com/obra/superpowers`. Packaging process knowledge as reusable, triggered skills instead of one monolithic prompt; the superpowers pattern (process skills first, checklists, trigger descriptions); the paper's "dynamic context and skills" as the economics rationale. Include a minimal skill-file skeleton. `# Related`: `/oks/ai-agent-repo-structure/skills/what-is-a-skill.md`, `/oks/ai-agent-repo-structure/skills/skill-file-format.md`, `/oks/agentic-sdlc-best-practices/agent-harness/the-factory-model.md`.
- `adopting-agentic-sdlc.md` — `resource:` [PAPER] URL ("Where to start"). Staged adoption paths: individual developers → engineering leaders → organizations; start where verification is cheap; grow autonomy with demonstrated trust. `# Related`: `/oks/agentic-sdlc-best-practices/foundations/vibe-coding-and-the-spectrum.md`, `/oks/agentic-sdlc-best-practices/foundations/economics-of-agentic-development.md`, `authoring-an-agents-md.md`.
- `applications/index.md` — area index; states explicitly that these concepts carry procedures for the bundle's three consumer use cases.

- [ ] **Step 1: Verify cross-bundle link targets** (`ls`).
- [ ] **Step 2: Write files; append `log.md` line.** Check each concept contains a numbered procedure or template block before moving on.
- [ ] **Step 3: Validator** → `0 violation(s)`.
- [ ] **Step 4: Commit**

```bash
git add oks/agentic-sdlc-best-practices/applications/ oks/agentic-sdlc-best-practices/log.md
git commit -m "feat: add applications area to agentic-sdlc-best-practices bundle"
```

---

## Task 12: Citation-integrity gate (spec: the validator cannot check truth)

**Deliverable:** `<scratchpad>/citation-audit.md` with a PASS/FAIL per URL. Nothing committed by this task except fixes it forces.

- [ ] **Step 1: Host audit**

Run: `grep -rhoE 'https?://[^ )]+' oks/agentic-sdlc-best-practices | sed -E 's#https?://([^/]+)/?.*#\1#' | sort -u`
Expected: every host is on the post-Task-2 allowlist. Fix any offender (swap to an allowlisted primary source or drop the claim).

- [ ] **Step 2: Liveness check**

Extract every distinct URL: `grep -rhoE 'https?://[^ )]+' oks/agentic-sdlc-best-practices | sort -u`. For each, `curl -sIL -o /dev/null -w "%{http_code} " --max-time 30` (note: kaggle.com may reject HEAD — retry with `curl -sL ... | head -c 200` and accept if the page returns content/title). Record results in `citation-audit.md`. Any 404/410: replace or drop.

- [ ] **Step 3: Claim spot-check (Opus subagent)**

Dispatch one `opus` subagent: "For each concept file in `oks/agentic-sdlc-best-practices/`, take its 1-2 most load-bearing claims and check them against `<scratchpad>/agentic-sdlc-research.md`: does a QUOTE line support the claim, and is the QUOTE's URL in the file's `# Sources`? Re-verify every precise number (e.g. +13.7, 52.8%→66.5%) against the live source with WebFetch. Return a table: file — claim — VERIFIED/UNSUPPORTED — fix needed."

- [ ] **Step 4: Guardrail-pairing + paraphrase check**

For each **[GUARDRAIL-PAIR]** file (`conductor-and-orchestrator-roles.md`, `agents-in-ci-cd.md`, `monitoring-rollback-and-progressive-delivery.md`, `authoring-an-agents-md.md`): confirm `# Related` contains `/oks/claude-best-practices/safety/index.md` plus a verification/human-gate concept. Spot-check 5 random concepts against the notes' QUOTE lines for multi-sentence verbatim lifts (short attributed quotes are fine).

- [ ] **Step 5: Fix and re-validate**

Apply any fixes from Steps 1-4, re-run `python3 tools/validate_okf.py` → `0 violation(s)`, and amend files in place. Commit fixes (if any):

```bash
git add oks/agentic-sdlc-best-practices/
git commit -m "fix: citation-audit corrections in agentic-sdlc bundle"
```

(Skip the commit if the audit found nothing.)

---

## Task 13: Root `index.md`, forward cross-links, and registration

**Files:**
- Create: `oks/agentic-sdlc-best-practices/index.md`
- Modify: earlier concepts to add the **deferred forward links** listed in Tasks 3-10 (all targets exist now)
- Modify: `.claude/skills/oks-bundles/SKILL.md` (new row + description clause + **narrow the existing autoresearch row**, see Step 3), `README.md`
- Modify: `oks/agentic-sdlc-best-practices/log.md` (append final line)

- [ ] **Step 1: Write the root `index.md`**

`type: OKF Bundle Index`, `title: Agentic SDLC Best Practices`, `resource:` the [PAPER] URL, full frontmatter. Mirror `oks/claude-best-practices/index.md`: intro paragraph naming the anchor paper and the three consumer use cases (author an AGENTS.md / generate system prompts / design tools & middleware — point at `applications/`), a "Concept areas" list linking all nine area `index.md` files with one-line summaries, and a "How to read this bundle" note (walk `applications/` for the procedures; walk the phase areas for the practices they encode).

- [ ] **Step 2: Add the deferred forward links**

Add each forward link named in Tasks 3-10 (search this plan for "deferred to Task 13") to the named file's `# Related` section. Keep only genuinely related pairs.

- [ ] **Step 3: Register in the router skill (disambiguation axis — spec requirement)**

In `.claude/skills/oks-bundles/SKILL.md`:
(a) Extend the frontmatter `description` with: "— or when the user asks about the agentic SDLC (vibe coding vs agentic engineering, AI-era lifecycle phases, harness engineering — system prompts, tool design, middleware — context engineering as a discipline, or authoring AGENTS.md files / system prompts / tools for coding agents)".
(b) Add the decision-table row:
`| agentic SDLC — vibe coding vs agentic engineering, SDLC practices when agents write the code, harness engineering (system prompts, tools, middleware), authoring AGENTS.md / system prompts / repo tooling for agents | \`/oks/agentic-sdlc-best-practices/index.md\` |`
(c) **Narrow the existing autoresearch row (plan-review F4):** the live table currently assigns the bare phrase "agentic engineering / vibe coding" to `autoresearch-best-practices`, which now collides with this bundle. Edit that row (and the matching clause in the frontmatter `description`) to its Karpathy-specific sense — e.g. "Karpathy AutoResearch, autonomous ML-research loops, running research agents with Claude Code, Karpathy's vibe-coding coinage / agentic-engineering posts" — so the general vibe-coding/agentic-SDLC sense routes to the new bundle.
(d) **Disambiguation check:** confirm the new row does NOT claim bare terms owned by other rows ("planning", "subagents", "verification" alone stay with `claude-best-practices`; "repo layout/AGENTS.md placement" stays with `ai-agent-repo-structure`; "Karpathy/AutoResearch" stays with `autoresearch-best-practices`). Sanity-check these 7 queries against the table — each should route unambiguously: "how do I run Claude Code headless" → claude-bp; "where does AGENTS.md live" → repo-structure; "what should my repo's AGENTS.md say about our SDLC" → agentic-sdlc; "what is harness engineering" → agentic-sdlc; "how do I use plan mode" → claude-bp; "what is the vibe-coding to agentic-engineering spectrum" → agentic-sdlc; "what is Karpathy's AutoResearch loop" → autoresearch. Adjust wording until true.

- [ ] **Step 4: Register in README**

Add to `README.md`'s bundle list, mirroring existing entries: `- [\`oks/agentic-sdlc-best-practices/\`](oks/agentic-sdlc-best-practices/index.md) — SDLC best practices when AI agents do the engineering: the vibe-coding→agentic-engineering spectrum, context engineering, phase-by-phase practices, harness engineering, and procedures for authoring AGENTS.md files, system prompts, and agent tooling.`

- [ ] **Step 5: Append the final `log.md` line**

`2026-07-07 — added root index, forward links; registered bundle in router and README`.

- [ ] **Step 6: Run the validator (full repo)**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)` including aux-file checks on `README.md`, `CLAUDE.md`, router skill.

- [ ] **Step 7: Commit**

```bash
git add oks/agentic-sdlc-best-practices/ .claude/skills/oks-bundles/SKILL.md README.md
git commit -m "feat: register agentic-sdlc-best-practices bundle in router and README"
```

---

## Task 14: Final verification

- [ ] **Step 1: Full validation** — `python3 tools/validate_okf.py` → `0 violation(s)`.
- [ ] **Step 2: Structure check** — `find oks/agentic-sdlc-best-practices -type f | sort | wc -l` → expected **51** (root index + log + 9 area indexes + 40 concepts); 49 if a candidate concept was dropped in Task 1 (then also confirm the user was told at Task 1).
- [ ] **Step 3: Sources-host audit (repeat)** — same grep as Task 12 Step 1; every host allowlisted.
- [ ] **Step 4: Actionability check** — `grep -L -E '^[0-9]+\.|^- \[ \]|```' oks/agentic-sdlc-best-practices/applications/*.md | grep -v index.md` → expected empty (every applications concept contains a numbered procedure or template block).
- [ ] **Step 5: Clean tree and branch** — `git status` clean on `feat/agentic-sdlc-bundle`; `git log --oneline -14` shows allowlist, 9 areas, (optional audit fix), registration.
- [ ] **Step 6: Wrap up** — use superpowers:finishing-a-development-branch to merge/PR per user preference.

---

## Self-Review (completed by plan author)

- **Spec coverage:** allowlist w/ evidence-confirmed hosts (T1/T2) ✓; 9 areas / 40 frozen concepts incl. 2 candidates with verdict + user report (T1, T3-T11) ✓; quote-or-drop protocol (T1) ✓; paraphrase/staleness/guardrail-pairing conventions (Global Constraints, enforced T12) ✓; applications actionability (T11 + T14 Step 4) ✓; citation-integrity gate (T12) ✓; router disambiguation + sample queries (T13 Step 3) ✓; README/CLAUDE.md integration (T2, T13) ✓; validator + atomic Conventional Commits every task ✓; model policy (Sonnet research, Opus writing/review) ✓; derive-from-evidence AGENTS.md rule (T11) ✓.
- **Placeholder scan:** no TBDs; every concept has resource, content outline, `# Related` targets, and source-host plan. Prose is written at execution from quote-backed notes (inherent to a research bundle); claims allowed are bounded by Task 1's QUOTE lines.
- **Consistency:** paths in File Structure, per-file specs, forward-link list, and `git add` lines match; frozen-filename rule stated once and referenced; build order validator-safe (forward links deferred to T13, where each is enumerated by its authoring task).
- **Ordering vs spec commit plan:** spec's "scaffold" commit is folded into Task 3 (log.md + first area) and the root index moved last so links always resolve — same end state, validator-green at every commit (same adaptation the autoresearch plan used).
