# Design: `agentic-sdlc-best-practices` OKF bundle

**Date:** 2026-07-07
**Status:** Approved (design), pending implementation plan

## Goal

Add a new Open Knowledge Format (OKF) bundle at
`oks/agentic-sdlc-best-practices/` documenting best practices and strategies
for the **software development lifecycle when AI agents do substantial
engineering work** — from the vibe-coding→agentic-engineering spectrum through
every SDLC phase, plus the harness engineering (system prompts, tools,
middleware) that makes coding agents effective. The bundle follows the same
conventions as the existing bundles and must pass
`python3 tools/validate_okf.py` with `0 violation(s)`.

## Consumers and use cases

The bundle is written **for agents first** (Claude Code and similar), to be
used as source knowledge when they:

1. **Author an `AGENTS.md`** describing SDLC best practices for a specific
   repository.
2. **Write system prompts** for coding agents.
3. **Design tools and middleware** for agent harnesses (the LangChain result —
   raising a coding agent's benchmark score by 13.7 points by changing only
   the system prompt, tools, and middleware — is a core motivating case).

Humans reading the bundle directly are a secondary audience.

## Anchor source and source pool

The anchor is Google's white paper **"The New SDLC With Vibe Coding: From
ad-hoc prompting to Agentic Engineering"** (Addy Osmani, Shubham Saboo,
Sokratis Kartakis; May 2026, 51 pp.). A local copy has been obtained; the
**canonical publicly hosted URL must be located during research** for
citation (a Google Drive share link is not citable). If no allowlisted-host
URL exists, the hosting domain is added to the allowlist as part of this work
(it is a Google publication) — see Sourcing standard.

Primary-source pool (all major-provider material, per user requirement):

- **Google** — the anchor paper; Google Cloud / Google developer material on
  agentic development where needed.
- **Anthropic** — engineering posts (building effective agents, effective
  context engineering, writing tools for agents), Claude Code best practices,
  docs.claude.com / code.claude.com.
- **OpenAI** — agent-building guides ("A practical guide to building agents"),
  cookbook material, platform docs.
- **LangChain** — blog and docs: context engineering, deepagents/middleware,
  and the benchmark-harness post behind the +13.7 result.
- **`agents.md`** — the AGENTS.md open spec (already allowlisted).
- **`github.com`** — the superpowers skills-library repo and other primary
  repos (already allowlisted).
- **`arxiv.org`** — papers where a claim needs an academic source (already
  allowlisted).

## Scope

In scope:

- The vibe-coding→agentic-engineering framing and trust calibration.
- Context engineering as a discipline.
- Agentic best practices for each SDLC phase: requirements/planning, design/
  architecture, implementation, testing/QA, code review, deployment/
  operations, maintenance/evolution.
- Agent harness engineering: system prompts, tool design, middleware, model
  selection, orchestration.
- Applied guidance for the three consumer use cases (AGENTS.md, system
  prompts, tools/middleware), including the skills-library (superpowers)
  pattern.

Out of scope (cross-link instead of restating):

- Claude-Code-specific operational mechanics — covered by
  `/oks/claude-best-practices/`.
- Repo layout for agent discovery (AGENTS.md/CLAUDE.md placement, skills
  directories) — covered by `/oks/ai-agent-repo-structure/`; the applications
  area covers *content and process*, not layout.
- Git mechanics — covered by `/oks/git-best-practices/`.
- Karpathy's AutoResearch loop and his agentic-engineering posts — covered by
  `/oks/autoresearch-best-practices/`; this bundle links to it from
  foundations.
- Non-SDLC agent applications (support bots, research agents, etc.).

## Bundle structure

Root: `oks/agentic-sdlc-best-practices/` with `index.md`
(progressive-disclosure entry) and `log.md` (dated change log). **Eleven
areas**, each a subdirectory with its own `index.md`. **44 concept files**
planned. The concept inventory below is the backbone; individual concepts may
be renamed, merged, or split during research if the sources demand it
(areas stay fixed; thin areas merge rather than pad — 11 is a ceiling, not a
quota).

### Area 1 — `foundations/` (the shift and the spectrum) — 5 concepts

- `from-syntax-to-intent.md` — the shift from writing syntax to expressing
  intent; what changes about the engineer's job.
- `what-vibe-coding-is.md` — definition and origin; code you don't fully
  review, generated conversationally.
- `vibe-coding-to-agentic-engineering-spectrum.md` — the maturity spectrum
  from ad-hoc prompting to disciplined agentic engineering.
- `when-vibe-coding-is-appropriate.md` — prototypes, throwaway tools,
  exploration vs. production code; matching rigor to stakes.
- `trust-but-verify-calibration.md` — calibrating how much to trust agent
  output; the verification burden as the new bottleneck.

### Area 2 — `context-engineering/` (the real skill) — 5 concepts

- `context-engineering-over-prompt-engineering.md` — curating everything the
  model sees, not just the prompt.
- `curating-the-context-window.md` — what to include/exclude; context as a
  finite budget; signal-to-noise.
- `progressive-disclosure.md` — indexes and just-in-time retrieval instead of
  loading everything up front.
- `compaction-and-long-horizon-context.md` — summarization/compaction,
  handoffs, sub-agent isolation for long tasks.
- `memory-and-knowledge-capture.md` — persistent memory files, durable notes,
  feeding lessons back into repo context.

### Area 3 — `requirements-and-planning/` — 4 concepts

- `spec-first-development.md` — specs as the primary artifact agents build
  from; why ambiguity is costlier with agents.
- `plan-then-execute.md` — separating planning from execution; plan review as
  the cheapest quality gate.
- `task-decomposition.md` — breaking work into agent-sized, independently
  verifiable units.
- `requirements-elicitation-with-ai.md` — using agents to interrogate and
  refine requirements (brainstorming, PRD drafting).

### Area 4 — `design-and-architecture/` — 3 concepts

- `architecture-decisions-with-ai.md` — agents as design partners; exploring
  alternatives; humans own the decision.
- `design-docs-as-agent-context.md` — design docs written to be consumed by
  agents downstream.
- `designing-for-agent-legibility.md` — modularity, clear boundaries, small
  files, conventions agents can follow reliably.

### Area 5 — `implementation/` — 4 concepts

- `tdd-as-agent-guardrail.md` — tests written first as the executable spec
  constraining agent code.
- `small-verifiable-increments.md` — short leash: small diffs, frequent
  checkpoints, atomic commits.
- `human-in-the-loop-checkpoints.md` — where human review gates belong during
  implementation; autonomy dials.
- `parallel-agents-and-isolation.md` — running multiple agents on independent
  tasks; worktree/sandbox isolation.

### Area 6 — `testing-and-qa/` — 4 concepts

- `agent-written-tests.md` — having agents generate tests; strengths and
  failure modes (weak assertions, tautological tests).
- `verification-loops.md` — giving agents the means to check their own work
  (run tests, linters, builds) and iterate.
- `evals-for-agentic-changes.md` — evaluating agent performance on your
  codebase; benchmarks vs. task-level evals.
- `preventing-test-gaming.md` — reward hacking: agents deleting/weakening
  tests to pass; guardrails against it.

### Area 7 — `code-review/` — 4 concepts

- `reviewing-ai-generated-code.md` — what changes when the author is an
  agent: volume, plausible-but-wrong code, reviewer attention.
- `ai-assisted-review.md` — agents as reviewers; first-pass triage; what to
  still route to humans.
- `adversarial-multi-agent-review.md` — panels of skeptical reviewers with
  distinct mandates; verification passes on findings.
- `human-review-gates.md` — which gates stay human (spec, security-sensitive
  code, irreversible actions) and why.

### Area 8 — `deployment-and-operations/` — 3 concepts

- `agents-in-ci-cd.md` — agents in pipelines: automated fixes, PR bots,
  headless runs; keeping CI the source of truth.
- `monitoring-and-rollback.md` — observability for AI-authored changes;
  fast rollback as the safety net for higher change velocity.
- `progressive-delivery-for-agent-output.md` — feature flags, canaries,
  staged rollout when change volume rises.

### Area 9 — `maintenance-and-evolution/` — 3 concepts

- `refactoring-with-agents.md` — large-scale mechanical refactors and
  migrations as agent sweet spots; verification at scale.
- `documentation-upkeep.md` — agents keeping docs/AGENTS.md current;
  docs-as-context creating a virtuous cycle.
- `dependency-and-migration-work.md` — dependency upgrades and codebase
  migrations run as supervised agent campaigns.

### Area 10 — `agent-harness/` (system prompts, tools, middleware) — 5 concepts

- `harness-engineering.md` — the harness (system prompt + tools + middleware
  + context management) as an engineering surface; the LangChain +13.7
  benchmark case as evidence of its leverage.
- `system-prompt-design.md` — structure, altitude (heuristics over hardcoded
  rules), examples, and failure modes of system prompts for coding agents.
- `tool-design-for-agents.md` — designing tools agents use well: naming,
  descriptions, token-efficient outputs, error messages that teach.
- `middleware-and-context-management.md` — middleware between the agent loop
  and the model: context editing, summarization, guardrails, caching.
- `model-selection-and-orchestration.md` — matching model tier to task
  complexity; subagent orchestration patterns (orchestrator-workers,
  parallel fan-out).

### Area 11 — `applications/` (using this bundle) — 4 concepts

- `authoring-an-agents-md.md` — producing a repo-specific AGENTS.md that
  encodes the repo's SDLC practices; what belongs in it vs. what agents can
  derive from code; the agents.md spec.
- `generating-system-prompts.md` — turning repo/SDLC knowledge into a system
  prompt for a coding agent; applying the harness-design concepts.
- `designing-repo-tools-and-middleware.md` — deriving repo-specific tools and
  middleware from SDLC pain points; when a tool beats a prompt instruction.
- `skills-libraries.md` — packaging process knowledge as reusable, triggered
  skills (the superpowers pattern) instead of one monolithic prompt.

## Concept file conventions (per repo CLAUDE.md)

- Each concept is one markdown file; its path is its identity.
- YAML frontmatter with all six fields: `type`, `title`, `description`,
  `resource`, `tags`, `timestamp` (ISO-8601 UTC, e.g. `2026-07-07T00:00:00Z`).
- Body, then a `# Related` section (plain root-relative markdown links only —
  `[text](/oks/...md)`, no `#fragments` or `"titles"`), then a `# Sources`
  section.
- `index.md`/`log.md` are exempt from the `# Sources` requirement.
- Cross-bundle links into `claude-best-practices`,
  `ai-agent-repo-structure`, `git-best-practices`, and
  `autoresearch-best-practices` wherever a concept touches their territory —
  link, don't restate.

## Sourcing standard

The repo's `CLAUDE.md` allowlist will be **expanded** (approved). Add hosts:

- `openai.com` and `cookbook.openai.com` — OpenAI agent guides and cookbook.
- `blog.langchain.com` and `docs.langchain.com` — LangChain engineering posts
  (context engineering, deepagents, harness benchmark) and docs.
- Google research/developer hosts as needed for the anchor paper and related
  material (e.g. `research.google`, `developers.google.com`), determined by
  where the canonical copy of the paper actually lives.

Rules preserved from the repo standard:

- **Primary sources only**; no forums, Reddit, or unattributed blogs.
- Every concept ends with `# Sources` citing only allowlisted hosts.
- A non-obvious claim that cannot be cited to an allowlisted host is
  **dropped, not hedged**.
- The +13.7 LangChain claim is cited to LangChain's own post; the Google
  paper's claims are cited to its canonical URL.

## Execution & subagent/model plan

Match models to task complexity (per user instruction: Sonnet/Haiku for
simple tasks, Opus/Fable for complex):

- **Research fan-out (parallel subagents, `sonnet`)** — one subagent per
  source cluster: (a) the Google paper (local PDF deep-read + canonical URL
  hunt), (b) Anthropic engineering posts + Claude Code docs, (c) OpenAI
  guides/cookbook, (d) LangChain blog/docs, (e) agents.md + superpowers repo,
  (f) arXiv sweep for supporting papers. Extraction with structured notes to
  the scratchpad → Sonnet.
- **Synthesis + writing (`opus`/Fable-tier)** — per-area synthesis of research
  notes into concept files in the repo's dense, cross-linked voice; one
  subagent per area (or small groups of related areas) to keep each area
  in-context. Reasoning-heavy → Opus/Fable.
- **Review (`opus`/Fable-tier)** — adversarial spec panel (before plan) and
  final consistency/citation review of the written bundle.
- **Validation (main loop)** — cross-link wiring, `index.md`/`log.md`,
  router-skill and `README.md` registration, `CLAUDE.md` allowlist edit, then
  `python3 tools/validate_okf.py` until `0 violation(s)`.

## Integration points to update

Per repo CLAUDE.md rule 5 (adding a new bundle):

- `.claude/skills/oks-bundles/SKILL.md` — add a decision-table row and extend
  the skill `description` with agentic-SDLC triggers (agentic SDLC, vibe
  coding vs agentic engineering, context engineering, AGENTS.md authoring,
  system prompt / tool / middleware design for coding agents).
- `README.md` — add the bundle to the bundle list.
- `CLAUDE.md` — expand the source allowlist as specified above.

## Risks and mitigations

- **Anchor paper has no citable URL** → research task explicitly hunts the
  canonical Google-hosted copy; fallback is adding its actual hosting domain
  (a Google property) to the allowlist; if genuinely unciteable, the paper
  becomes framing-only and every claim is re-grounded in other allowlisted
  sources.
- **Overlap creep with existing bundles** → every overlapping concept states
  its distinct angle and links out; reviewers check for restatement.
- **Thin areas** → merge into a neighbor rather than pad (e.g.
  `maintenance-and-evolution/` folds into `deployment-and-operations/` if
  sources are thin).
- **Source recency drift** — provider posts move/rename → cite stable URLs,
  verify each link resolves at authoring time.

## Acceptance criteria

- `oks/agentic-sdlc-best-practices/` exists with `index.md`, `log.md`, eleven
  area subdirectories each with `index.md`, and ~44 concept files per the
  inventory above.
- Every concept has complete six-field frontmatter, a `# Related` section,
  and a `# Sources` section citing only allowlisted hosts.
- The three consumer use cases are directly served: an agent can walk
  `applications/` + the phase areas and produce an AGENTS.md, a system
  prompt, or a tools/middleware design.
- Router `SKILL.md`, `README.md`, and `CLAUDE.md` updated.
- `python3 tools/validate_okf.py` prints `0 violation(s)`.
- Commits are atomic with Conventional Commit messages.

## Commit plan

Atomic, Conventional Commits (mirroring prior bundle history — allowlist/
scaffold first, then area by area, then registration last):

1. `build: expand CLAUDE.md source allowlist for agentic-sdlc bundle`
2. `feat: scaffold agentic-sdlc-best-practices bundle (index, log)`
3. –13. `feat: add <area> area to agentic-sdlc-best-practices bundle` (one
   per area, 11 commits)
14. `feat: register agentic-sdlc-best-practices bundle in router and README`
