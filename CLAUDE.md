# okf-bundles — agent guide

This repo hosts **Open Knowledge Format (OKF)** bundles under `oks/`, a router
skill at `.claude/skills/oks-bundles/`, and a validator at
`tools/validate_okf.py`. Load the router skill for how to *consume* a bundle;
this file is about *editing* them.

## When you add or modify any OKF bundle

Follow these rules, then validate. Deeper rationale lives in the bundle itself:
[ai-agent-repo-structure](/oks/ai-agent-repo-structure/index.md).

1. **Concept file format** — each concept is one markdown file whose path is its
   identity, with YAML frontmatter. Populate all six fields (`type` is the only
   strictly required one, but keep the set consistent): `type`, `title`,
   `description`, `resource`, `tags`, `timestamp`. Use an ISO-8601 UTC value for
   `timestamp` (e.g. `2026-07-07T00:00:00Z`) on new or edited concepts.

2. **Structure** — each bundle root has an `index.md` (progressive-disclosure
   entry linking its areas) and a `log.md` (append a dated line whenever you
   change the bundle). Each area subdirectory has its own `index.md`.

3. **Cross-links** — link concepts with **plain root-relative markdown links
   only**: `[atomic commits](/oks/git-best-practices/commits/atomic-commits.md)`.
   Do **not** add `#fragments` or `"titles"` inside the parens — the validator
   only resolves plain `](/....md)` links, so anything else is silently
   unchecked and can rot. Every concept ends with a `# Related` section.

4. **Sources** — every concept (except `index.md`/`log.md`) ends with a
   `# Sources` section citing **primary sources only**: official docs or
   major-provider engineering material. Allowed hosts: `git-scm.com`,
   `docs.github.com`, `atlassian.com`, `conventionalcommits.org`, `agents.md`,
   `docs.claude.com`, `code.claude.com`, `anthropic.com`, `cloud.google.com`, `github.com`, `arxiv.org`, `x.com`,
   `kaggle.com`, `cdn.openai.com`, `langchain.com`, `docs.langchain.com`.
   `github.com`, `arxiv.org`, `x.com` serve the AutoResearch bundle's primary
   sources (Karpathy's repo, arXiv papers, Karpathy's X posts); `kaggle.com`
   (Google-published whitepapers), `cdn.openai.com` (OpenAI guides), and
   `langchain.com`/`docs.langchain.com` serve the agentic-SDLC bundle's
   provider primary sources.
   No forums, Reddit, or unattributed blogs. Do not state a non-obvious claim
   you cannot cite to one of these.

5. **Adding a new area or bundle** — update the parent `index.md` to link it. If
   you add a whole bundle, also update the router skill's decision table
   (`.claude/skills/oks-bundles/SKILL.md`) and `README.md`.

## Before you commit — always

```bash
python3 tools/validate_okf.py
```

It must print `0 violation(s)`. It checks frontmatter/`type`, that every
root-relative `.md` link resolves, that concepts carry a `# Sources` section,
and the cross-references in `README.md`, `CLAUDE.md`, and the router skill. CI
runs the same command on every push and pull request.

## Commit hygiene

Make **atomic commits** with **Conventional Commit** messages (`docs:`, `feat:`,
`fix:`, `build:`) — this repo documents these practices, so follow its own
advice: [git-best-practices](/oks/git-best-practices/index.md).

## How we work

Non-trivial work follows the superpowers SDLC — **don't jump straight to code**:

**brainstorm → spec (`docs/superpowers/specs/`) → plan (`docs/superpowers/plans/`) →
implement.** Small, obvious fixes can skip ahead, but design-bearing changes get a
spec first.

### Adversarial review of the spec

Before `spec → plan`, run an **adversarial panel on the spec** — the earliest,
least-reversible artifact, where catching a wrong assumption is cheapest. A flawed
spec makes a *perfect* plan build the wrong thing.

Fan out (via `dispatching-parallel-agents`) reviewers with **distinct** mandates —
not clones:

- **Requirements** — what could be built into the wrong thing?
- **Assumptions** — what's assumed true but unverified?
- **Failure & abuse** — how does this break or get misused? Threat model?
- **Scope & simpler design** — what's over-built (YAGNI), what simpler approach is skipped?

Calibrate them **skeptical** — default to finding a path to a wrong/broken outcome
before approving (the opposite of the stock "approve unless broken" reviewers).
Then **synthesize** (dedup, resolve conflicts, rank by severity) and feed that into
the user's spec-review gate — the panel *arms* the human gate, it doesn't replace it.

Keep plan review as-is (single reviewer: spec coverage, decomposition, buildability).
Only add a *lighter* adversarial pass on the plan — scoped to architecture/decomposition,
**not** requirements — if real design decisions leak downstream into the plan.

