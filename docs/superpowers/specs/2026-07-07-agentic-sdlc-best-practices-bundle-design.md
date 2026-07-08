# Design: `agentic-sdlc-best-practices` OKF bundle

**Date:** 2026-07-07
**Status:** Approved (design); revised after adversarial spec panel; pending
user spec-review gate and implementation plan

## Goal

Add a new Open Knowledge Format (OKF) bundle at
`oks/agentic-sdlc-best-practices/` documenting best practices and strategies
for the **software development lifecycle when AI agents do substantial
engineering work** — from the vibe-coding→agentic-engineering spectrum through
every SDLC phase, plus the harness engineering (system prompts, tools,
middleware) that makes coding agents effective. The bundle follows the same
conventions as the existing bundles and must pass
`python3 tools/validate_okf.py` with `0 violation(s)`.

The bundle name is anchored in the research already done: the anchor paper's
own framing is "The New SDLC" and "agentic engineering," so
`agentic-sdlc-best-practices` follows both the paper and the repo's
`*-best-practices` naming convention.

## Consumers and use cases

The bundle is written **for agents first** (Claude Code and similar), to be
used as source knowledge when they:

1. **Author an `AGENTS.md`** describing SDLC best practices for a specific
   repository.
2. **Write system prompts** for coding agents.
3. **Design tools and middleware** for agent harnesses (the LangChain result —
   raising a coding agent's Terminal-Bench-2.0 score by 13.7 points, model
   held fixed, by changing only the system prompt, tools, and middleware — is
   a core motivating case; verified against LangChain's own post).

Humans reading the bundle directly are a secondary audience.

**Actionability requirement (panel: requirements).** The three use cases must
be *executable*, not gestured at: every `applications/` concept must contain
an explicit reusable procedure (ordered checklist, annotated skeleton, or
template) that an agent instantiates — not only descriptive prose. See
Acceptance criteria.

## Anchor source and source pool

The anchor is Google's white paper **"The New SDLC With Vibe Coding: From
ad-hoc prompting to Agentic Engineering"** (Addy Osmani, Shubham Saboo,
Sokratis Kartakis; May 2026, 51 pp.). A local PDF copy is in hand; the
canonical public URL is **verified**:
`https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding` (published
via Kaggle, a Google subsidiary, as part of Kaggle's AI-Agents course
series). The allowlist therefore adds `kaggle.com`, scoped in intent to
Google-published whitepapers.

Primary-source pool (all major-provider material, per user requirement):

- **Google** — the anchor paper; Google Cloud / Google developer material on
  agentic development where needed.
- **Anthropic** — engineering posts on the already-allowlisted
  `anthropic.com` (building effective agents; effective context engineering;
  writing tools for agents — all verified live), Claude Code best practices,
  `docs.claude.com` / `code.claude.com`.
- **OpenAI** — "A practical guide to building agents" (verified: landing on
  `openai.com`, PDF on `cdn.openai.com`) and platform material.
- **LangChain** — the harness-engineering post behind the +13.7 result
  (verified at `langchain.com/blog/...` — note: **not** `blog.langchain.com`)
  and `docs.langchain.com` (context engineering, deepagents/middleware).
- **`agents.md`** — the AGENTS.md open spec (already allowlisted).
- **`github.com`** — the superpowers skills-library repo and other primary
  repos (already allowlisted).
- **`arxiv.org`** — papers where a claim needs an academic source (already
  allowlisted).

**Source-type interpretation (panel: requirements — for user ratification).**
The user asked for "published papers/white papers from major providers." Read
literally this is unsatisfiable: the user's own seed material (the LangChain
+13.7 post, the superpowers repo) exists only as engineering blog posts and
repositories. This spec interprets the constraint as **authoritative primary
material from the named providers** — papers, white papers, official
engineering blogs/docs, and canonical repos — and excludes everything the
repo standard already bans (forums, Reddit, unattributed blogs, secondary
journalism). This interpretation is flagged for explicit approval at the
spec-review gate.

## Scope

In scope:

- The vibe-coding→agentic-engineering framing: the spectrum, trust
  calibration, the developer's evolving role (conductor/orchestrator), and
  the economics of agentic development (CapEx/OpEx, hidden debt of vibe
  coding).
- Context engineering as a discipline.
- Agentic best practices along the SDLC phases: requirements/planning,
  design/architecture, implementation, verification & review,
  operations & evolution.
- Agent harness engineering: system prompts, tool design, middleware, model
  routing, the factory model.
- Applied guidance for the three consumer use cases, including the
  skills-library (superpowers) pattern and adoption paths.

Out of scope (cross-link instead of restating — and where a planned concept
would survive only as a restatement, it is **cut**, per the panel's scope
review; the cuts are recorded in the inventory below):

- Claude-Code-specific operational mechanics — covered by
  `/oks/claude-best-practices/`.
- Repo layout for agent discovery (AGENTS.md/CLAUDE.md placement, skills
  directories, progressive disclosure mechanics) — covered by
  `/oks/ai-agent-repo-structure/`; this bundle covers *content and process*.
- Git mechanics — covered by `/oks/git-best-practices/`.
- Karpathy's AutoResearch loop and his vibe-coding coinage/arc — covered by
  `/oks/autoresearch-best-practices/`; this bundle's spectrum concept links
  to it for origin and keeps the Google paper's maturity framing as its own
  distinct content.
- Non-SDLC agent applications (support bots, research agents, etc.).

## Bundle structure

Root: `oks/agentic-sdlc-best-practices/` with `index.md`
(progressive-disclosure entry) and `log.md` (dated change log). **Nine
areas**, each a subdirectory with its own `index.md`. **38 concept files.**

The inventory below is the product of the adversarial panel's dedup pass
(11 areas / 44 concepts → 9 areas / 38 concepts: ~10 pure-duplication
concepts cut or merged, offset by paper-grounded concepts the first draft
missed — factory model, conductor/orchestrator, the 80% problem, economics,
model routing, security, adoption). **Filenames below are frozen once the
plan is approved** — cross-links are written against this set, and any
post-freeze rename requires a link-fixup sweep (panel: failure).

### Area 1 — `foundations/` — 6 concepts

- `from-syntax-to-intent.md` — the shift from writing syntax to expressing
  intent; what changes about the engineer's job. [paper: "The shift from
  syntax to intent"]
- `vibe-coding-and-the-spectrum.md` — what vibe coding is and the maturity
  spectrum to agentic engineering, per the Google paper's framing. Links
  `/oks/autoresearch-best-practices/agentic-engineering/vibe-coding-to-agentic-engineering.md`
  for Karpathy's coinage/arc rather than restating it. [merged from two
  planned concepts]
- `when-vibe-coding-is-appropriate.md` — prototypes vs. production; the
  crossover point where vibe coding gets expensive. [paper]
- `trust-calibration-and-the-80-percent-problem.md` — verification burden as
  the new bottleneck; the paper's "80% problem." [merged]
- `conductor-and-orchestrator-roles.md` — the developer's evolving role:
  hands-on real-time direction vs. async multi-agent delegation. [paper]
- `economics-of-agentic-development.md` — vibe coding as low-CapEx/high-OpEx,
  agentic engineering as the reverse; hidden debt; context engineering as a
  financial lever. [paper]

### Area 2 — `context-engineering/` — 4 concepts

- `context-engineering-over-prompt-engineering.md` — curating everything the
  model sees, not just the prompt. [paper; Anthropic; LangChain]
- `curating-the-context-window.md` — include/exclude decisions; context as a
  finite budget; links `/oks/ai-agent-repo-structure/` for
  progressive-disclosure mechanics instead of restating them. [absorbs the
  cut `progressive-disclosure.md`]
- `compaction-and-long-horizon-context.md` — summarization/compaction,
  handoffs, sub-agent context isolation for long tasks. [Anthropic;
  LangChain]
- `memory-and-knowledge-capture.md` — what to persist across sessions and
  feed back into repo context; scoped to the *discipline*, links
  `/oks/claude-best-practices/context/claude-md-as-memory.md` for mechanics.

### Area 3 — `requirements-and-planning/` — 3 concepts

- `specs-as-the-primary-artifact.md` — specs as what agents build from; why
  ambiguity is costlier with agents; plan-review as the cheapest quality
  gate. Renamed from `spec-first-development.md` to avoid colliding with
  `/oks/claude-best-practices/planning/spec-first-development.md`, which it
  links. [absorbs the cut `plan-then-execute.md`]
- `task-decomposition.md` — breaking work into agent-sized, independently
  verifiable units.
- `requirements-elicitation-with-ai.md` — using agents to interrogate and
  refine requirements.

### Area 4 — `design-and-architecture/` — 3 concepts

- `architecture-decisions-with-ai.md` — agents as design partners; humans own
  the decision.
- `design-docs-as-agent-context.md` — design docs written to be consumed by
  agents downstream.
- `designing-for-agent-legibility.md` — modularity, boundaries, small files,
  conventions agents can follow reliably.

### Area 5 — `implementation/` — 3 concepts

- `tdd-as-agent-guardrail.md` — tests-first as the executable spec
  constraining agent code; provider-general framing, links
  `/oks/claude-best-practices/workflows/test-driven-development.md` for the
  Claude Code workflow.
- `small-verifiable-increments.md` — short leash: small diffs, checkpoint
  cadence for agents; links
  `/oks/git-best-practices/commits/atomic-commits.md` rather than restating
  commit hygiene.
- `human-in-the-loop-checkpoints.md` — the single cross-cutting "which gates
  stay human" concept (spec review, security-sensitive code, irreversible
  actions); autonomy dials. [absorbs the cut `code-review/human-review-gates.md`]

Cut from this area: `parallel-agents-and-isolation.md` — pure duplication of
`/oks/claude-best-practices/subagents/parallel-agents.md`; a cross-link
serves instead.

### Area 6 — `verification-and-review/` — 5 concepts

[Merged from the planned `testing-and-qa/` + `code-review/` areas, which the
dedup pass left thin; mirrors the paper's own grouping.]

- `agent-written-tests-and-reward-hacking.md` — agent-generated tests, their
  failure modes (weak/tautological assertions), and agents gaming tests to
  pass; guardrails against both. [merged from two planned concepts]
- `evals-for-agentic-changes.md` — evaluating agent performance on your
  codebase; benchmark vs. task-level evals.
- `reviewing-ai-generated-code.md` — what changes when the author is an
  agent: volume, plausible-but-wrong code, AI-assisted first-pass triage.
  [absorbs the cut `ai-assisted-review.md`]
- `adversarial-multi-agent-review.md` — panels of skeptical reviewers with
  distinct mandates; verification passes on findings.
- `securing-agent-generated-code.md` — security review posture for
  AI-authored changes; provenance; guardrails in the loop. [paper; OpenAI
  guide's guardrails material]

Cut from this area: `verification-loops.md` — duplication of
`/oks/claude-best-practices/verification/tests-and-checks-as-guardrails.md`.

### Area 7 — `operations-and-evolution/` — 3 concepts

[Merged from the planned `deployment-and-operations/` +
`maintenance-and-evolution/` areas — the panel's thin-area prediction,
applied up front.]

- `agents-in-ci-cd.md` — agents in pipelines: automated fixes, PR bots,
  headless runs; CI as the source of truth. Subject to the guardrail-pairing
  invariant (below).
- `monitoring-rollback-and-progressive-delivery.md` — observability, fast
  rollback, flags/canaries as the safety net for higher change velocity.
  [merged from two planned concepts]
- `large-scale-refactors-and-migrations.md` — mechanical sweeps, dependency
  upgrades, migrations as supervised agent campaigns; verification at scale.
  [merged from two planned concepts]

Cut from this area: `documentation-upkeep.md` — duplication of
`/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md`.

### Area 8 — `agent-harness/` — 6 concepts

- `harness-engineering.md` — the harness (system prompt + tools + middleware
  + context management) as an engineering surface; the paper's
  "model is ~10% of the system" thesis; the LangChain +13.7 case as
  evidence of leverage.
- `system-prompt-design.md` — structure, altitude (heuristics over hardcoded
  rules), examples, failure modes.
- `tool-design-for-agents.md` — naming, descriptions, token-efficient
  outputs, error messages that teach. [Anthropic "writing tools for agents"]
- `middleware-and-context-management.md` — middleware between loop and model:
  context editing, summarization, guardrails, caching. [LangChain]
- `model-selection-and-routing.md` — matching model tier to task complexity;
  intelligent model routing as a cost/quality lever; links
  `/oks/claude-best-practices/subagents/choosing-a-model.md`. [paper]
- `the-factory-model.md` — building the system that builds the software:
  investing in the harness, evals, and skills rather than only the output.
  [paper]

### Area 9 — `applications/` — 5 concepts

[Every concept here carries an explicit reusable procedure or template —
the actionability requirement.]

- `authoring-an-agents-md.md` — a procedure for producing a repo-specific
  AGENTS.md that encodes the repo's SDLC practices. Opens with a
  **derive-from-evidence step** (panel: failure/abuse): inspect the target
  repo's actual practices (tests, review flow, CI, commit style) and
  calibrate to them, flagging gaps as recommendations rather than asserting
  ideals as current practice. Hands off placement/discovery **inline** to
  `/oks/ai-agent-repo-structure/` so the procedure is complete end-to-end.
- `generating-system-prompts.md` — a procedure for turning repo/SDLC
  knowledge into a system prompt for a coding agent, applying the
  agent-harness concepts.
- `designing-repo-tools-and-middleware.md` — a procedure for deriving
  repo-specific tools and middleware from SDLC pain points; when a tool
  beats a prompt instruction.
- `skills-libraries.md` — packaging process knowledge as reusable, triggered
  skills (the superpowers pattern; the paper's "dynamic context and skills")
  instead of one monolithic prompt.
- `adopting-agentic-sdlc.md` — staged adoption paths for individual
  developers, engineering leaders, and organizations. [paper: "Where to
  start"]

## Concept file conventions (per repo CLAUDE.md, plus panel additions)

- Each concept is one markdown file; its path is its identity.
- YAML frontmatter with all six fields: `type`, `title`, `description`,
  `resource`, `tags`, `timestamp` (ISO-8601 UTC).
- Body, then `# Related` (plain root-relative markdown links only), then
  `# Sources`.
- `index.md`/`log.md` are exempt from the `# Sources` requirement.
- Cross-bundle links wherever a concept touches another bundle's territory —
  link, don't restate.
- **Paraphrase, not copy (panel: failure).** Concepts state claims in the
  repo's own voice. Any direct quote is short, quote-marked, and attributed
  inline. No reproduction of tables, figures, or multi-sentence passages
  from source PDFs/posts. Synthesis agents write from structured notes,
  never by editing pasted source text.
- **Guardrail-pairing invariant (panel: failure).** Every concept that
  recommends increased autonomy (headless runs, auto-fix, auto-merge, CI
  agents, higher change velocity) MUST link in `# Related` to at least one
  human-gate / verification / anti-reward-hacking concept and to
  `/oks/claude-best-practices/safety/index.md`. Checked by name in the final
  review pass.
- **Date volatile claims inline (panel: failure).** Product-specific,
  version-bound claims (named APIs, benchmarks, product names) are dated in
  prose ("as of the May 2026 paper…", "LangChain's middleware API as of
  mid-2026…") so consumers can weigh recency; prefer durable principles
  where the point survives at higher altitude.

## Sourcing standard

The repo's `CLAUDE.md` allowlist will be **expanded** (approved; hosts
corrected by the panel's verification pass). Add:

- `kaggle.com` — the anchor paper's canonical, verified home
  (Google-published whitepapers).
- `openai.com` and `cdn.openai.com` — OpenAI's agents guide (landing page +
  PDF host).
- `langchain.com` and `docs.langchain.com` — LangChain engineering posts
  (the blog lives under `langchain.com/blog/`, **not** `blog.langchain.com`)
  and docs.

Not added: `cookbook.openai.com`, `research.google`,
`developers.google.com` — no concept currently needs them; add during
implementation only if a citation actually lands there (no speculative
allowlist entries).

Rules preserved from the repo standard: primary sources only; every concept
ends with `# Sources` citing only allowlisted hosts; a non-obvious claim
that cannot be cited to an allowlisted host is **dropped, not hedged**.

**Citation-integrity gate (panel: failure — critical).** The validator
checks structure only (frontmatter, link resolution, `# Sources` presence);
it does **not** verify hosts, URL liveness, or claim accuracy. Therefore:

1. **Quote-or-drop at research time.** Research subagents must capture, for
   every extracted claim, a verbatim supporting snippet plus its exact URL
   in the scratchpad notes. Synthesis may only assert what has a captured
   snippet.
2. **Verification pass before the final commit.** Every distinct `# Sources`
   URL is fetched and confirmed to (a) resolve, (b) sit on an allowlisted
   host, and (c) actually support the claims citing it (spot-checked against
   the captured snippets). Precise numbers (e.g. +13.7) are re-verified
   against the live source.
3. This gate is an acceptance criterion, independent of `validate_okf.py`.

## Execution & subagent/model plan

Match models to task complexity (per user instruction: Sonnet/Haiku for
simple tasks, Opus/Fable for complex):

- **Research fan-out (parallel subagents, `sonnet`)** — one subagent per
  source cluster: (a) the anchor paper (local PDF deep-read; quote-or-drop
  notes per area), (b) Anthropic engineering posts + Claude docs, (c) OpenAI
  guide, (d) LangChain posts/docs, (e) agents.md + superpowers repo,
  (f) arXiv sweep. Output: structured notes with verbatim snippets + URLs in
  the scratchpad.
- **Synthesis + writing (`opus`/Fable-tier)** — per-area synthesis of notes
  into concept files; one subagent per area (or small related groups), each
  given the **frozen filename inventory** so `# Related` links target real
  paths. Cross-link correctness is then owned by a single main-loop wiring
  pass after all files exist (two-phase: files first, link audit second).
- **Review (`opus`/Fable-tier)** — final consistency review: citation gate
  (above), guardrail-pairing check, paraphrase check, overlap check against
  existing bundles.
- **Validation (main loop)** — `index.md`/`log.md`, router + `README.md`
  registration, `CLAUDE.md` allowlist edit, `python3 tools/validate_okf.py`
  until `0 violation(s)`.

## Integration points to update

- `.claude/skills/oks-bundles/SKILL.md` — add a decision-table row **scoped
  by a distinguishing axis** (panel: failure): this bundle owns *SDLC
  practices/process when agents do the engineering* (vibe coding vs. agentic
  engineering, agentic SDLC phases, harness engineering, AGENTS.md/system
  prompt/tool-middleware authoring); `claude-best-practices` keeps
  Claude-Code *operational mechanics*. Triggers must not reuse generic terms
  already owned by another row (planning, subagents, verification alone stay
  with `claude-best-practices`). Sanity-check a handful of sample queries
  for ambiguous routing before committing.
- `README.md` — add the bundle to the bundle list.
- `CLAUDE.md` — expand the source allowlist as specified above.

## Risks and mitigations

- **Kaggle page is a JS SPA** — the canonical URL resolves publicly but
  content is client-rendered; cite the URL as the paper's home and keep the
  local PDF as the reading copy. If the page ever gates behind login,
  fall back to citing Osmani's announcement plus re-grounding claims in
  other allowlisted sources.
- **Overlap creep with existing bundles** — dedup already applied at spec
  level (cuts recorded above); the final review pass re-checks that each
  surviving concept carries distinct content.
- **Cross-link rot under parallel authoring** — mitigated by the filename
  freeze + single-owner link audit (two-phase execution).
- **Hallucinated/miscited claims** — mitigated by the citation-integrity
  gate (quote-or-drop + verification pass).
- **Staleness** — volatile claims dated inline; harness area (fastest-moving
  surface) gets an as-of note.

## Acceptance criteria

- `oks/agentic-sdlc-best-practices/` exists with `index.md`, `log.md`, nine
  area subdirectories each with `index.md`, and the 38 concept files above
  (frozen names).
- Every concept has complete six-field frontmatter, `# Related`, and
  `# Sources` citing only allowlisted hosts.
- **Actionability:** each `applications/` concept contains an explicit
  reusable procedure or template; an agent given only this bundle can
  produce a non-generic, repo-grounded AGENTS.md, system prompt, or
  tools/middleware design.
- **Citation integrity:** every `# Sources` URL fetched and verified
  (resolves; allowlisted host; supports the claim); precise figures
  re-verified against live sources.
- **Guardrail pairing:** every autonomy-recommending concept links a
  human-gate/verification counterweight.
- Router `SKILL.md` row uses the distinguishing axis; no ambiguous routing
  on sample queries; `README.md` and `CLAUDE.md` updated.
- `python3 tools/validate_okf.py` prints `0 violation(s)`.
- Commits are atomic with Conventional Commit messages.

## Commit plan

**Pre-flight (panel: failure):** the working tree currently carries an
uncommitted user edit to `CLAUDE.md` (the "How we work" section). Before
commit #1, that edit is committed separately (its own `docs:` commit, with
user's go-ahead) or stashed — the allowlist commit must contain only the
allowlist hunk.

Atomic, Conventional Commits:

1. `build: expand CLAUDE.md source allowlist for agentic-sdlc bundle`
2. `feat: scaffold agentic-sdlc-best-practices bundle (index, log)`
3. –11. `feat: add <area> area to agentic-sdlc-best-practices bundle`
   (one per area, 9 commits)
12. `feat: register agentic-sdlc-best-practices bundle in router and README`

## Panel disposition (summary)

Adversarial panel (requirements / assumptions / failure & abuse /
scope-YAGNI) ran 2026-07-07; all four reviewers' findings are incorporated
above. Two items are explicitly deferred to the user's spec-review gate:

1. **Source-type interpretation** (papers/white papers → authoritative
   primary provider material) — needs ratification.
2. **Scale delta** — dedup cuts land the inventory at 9 areas / 38 concepts
   vs. the originally approved "8+ areas / 40+ concepts." Areas satisfy the
   choice; the concept count is slightly under because ~10 planned concepts
   were pure duplication of existing bundles, partially offset by 7
   paper-grounded concepts the first draft missed. Padding back to 40 would
   violate the repo's cross-link-don't-restate rule.
