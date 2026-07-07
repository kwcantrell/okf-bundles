# Design: OKF Bundles for Git Best Practices & AI-Agent Repo Structure

**Date:** 2026-07-07
**Status:** Approved (design phase)
**Repo:** `okf-bundles`

## Summary

Build two authoritative, thoroughly cross-linked [Open Knowledge Format (OKF) v0.1](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
bundles, plus one project-level Claude Code skill that teaches agents the OKF
format and routes them to the correct bundle.

1. `oks/git-best-practices` — git & GitHub workflows, conventions, and techniques (~20-25 concepts).
2. `oks/ai-agent-repo-structure` — best practices for structuring a repository so AI agents can discover and use skills, context files, and knowledge (~8-12 concepts).

All content is grounded **only in primary sources**: the official Git
documentation and Pro Git book, GitHub Docs, Anthropic's Claude Code / agent
documentation, the `AGENTS.md` open convention, and vendor engineering
guidance/white-papers from major providers (Google, Anthropic, Atlassian's
official git tutorials). Community forums, Reddit threads, and unattributed
blog posts are excluded.

## Goals

- Produce reusable, shareable OKF bundles that are equally readable by humans and parseable by AI agents.
- Every non-obvious claim cites a primary-source URL.
- Concepts form a navigable graph via markdown cross-links, not just a flat file list.
- A single skill gives agents a clear entry point and navigation strategy for the bundles.
- The repository dogfoods the very git practices it documents.

## Non-Goals

- No tooling/SDK to parse or serve the bundles (OKF is "just files"; consumption is out of scope).
- No coverage of niche/edge git plumbing beyond what a practitioner or agent realistically needs.
- No opinion wars: where multiple valid approaches exist (e.g. merge vs. rebase, monorepo vs. polyrepo), document trade-offs rather than mandate one.

## Background: OKF v0.1 in brief

- **Just markdown + YAML frontmatter + files.** Shippable as a tarball, hostable in git, mountable on any filesystem.
- A **bundle** is a directory of markdown files; each file is a **concept**, and its path is its identity.
- The **only required frontmatter field is `type`**. Standard optional fields: `title`, `description`, `resource`, `tags`, `timestamp`.
- `index.md` files enable **progressive disclosure** as an agent navigates the hierarchy.
- `log.md` files record chronological change history.
- Concepts link to each other with normal markdown links, forming a graph richer than parent/child directory nesting.

## Repository Layout

```
okf-bundles/
├── README.md                     # what this repo is; how bundles + skill relate
├── oks/
│   ├── git-best-practices/       # Bundle A
│   └── ai-agent-repo-structure/  # Bundle B
├── .claude/
│   └── skills/
│       └── oks-bundles/
│           └── SKILL.md          # router skill
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-07-07-okf-git-best-practices-bundles-design.md
```

## Bundle A — `oks/git-best-practices`

Proposed concept tree (final naming may adjust slightly during authoring):

```
index.md                         # progressive-disclosure entry point
log.md                           # bundle change history
fundamentals/
  index.md
  repository-model.md
  staging-area.md
  refs-and-objects.md
workflows/
  index.md
  github-flow.md
  git-flow.md
  trunk-based-development.md
  forking-workflow.md
branching/
  index.md
  naming-conventions.md
  branch-protection.md
  merge-vs-rebase.md
  resolving-conflicts.md
commits/
  index.md
  atomic-commits.md
  conventional-commits.md
  commit-message-style.md
  signing-commits.md
collaboration/
  index.md
  pull-requests.md
  code-review.md
  draft-prs.md
  codeowners.md
history/
  index.md
  rebasing.md
  interactive-rebase.md
  cherry-pick.md
  revert-vs-reset.md
  bisect.md
remote/
  index.md
  fetch-pull-push.md
  tracking-branches.md
  tags-and-releases.md
automation/
  index.md
  git-hooks.md
  ci-integration.md
  pre-commit.md
security/
  index.md
  secret-management.md
  gitignore-hygiene.md
  signed-tags.md
  credential-storage.md
scale/
  index.md
  monorepo-vs-polyrepo.md
  large-files-lfs.md
  sparse-checkout.md
```

**Primary sources:** git-scm.com (docs + Pro Git book), docs.github.com,
Atlassian official git tutorials, and vendor engineering guidance.

## Bundle B — `oks/ai-agent-repo-structure`

Proposed concept tree:

```
index.md
log.md
context-files/
  index.md
  agents-md-and-claude-md.md
  progressive-disclosure.md
  precedence-and-scope.md
skills/
  index.md
  what-is-a-skill.md
  skill-file-format.md
  skill-placement.md
  project-vs-personal-skills.md
conventions/
  index.md
  directory-layout.md
  naming-for-discoverability.md
  readme-for-agents.md
knowledge/
  index.md
  okf-bundles-in-repos.md
  docs-for-agents.md
  machine-readable-metadata.md
tooling/
  index.md
  mcp-and-tool-config.md
  slash-commands-and-hooks.md
practices/
  index.md
  determinism-and-reproducibility.md
  guardrails-and-permissions.md
```

**Primary sources:** Anthropic Claude Code / skills / agent documentation, the
`AGENTS.md` open convention, and Google/Anthropic engineering guidance.

## OKF Conventions Enforced

- Only `type` is strictly required, but every concept populates all six standard frontmatter fields (`type`, `title`, `description`, `resource`, `tags`, `timestamp`) for consistency.
- Each bundle root has an `index.md` (progressive disclosure) and a `log.md` (history). Subdirectories get an `index.md` where it aids navigation.
- Cross-links use root-relative markdown links, e.g. `[atomic commits](/oks/git-best-practices/commits/atomic-commits.md)`.
- Every concept ends with a **Sources** section; no non-obvious claim ships without a primary-source citation.
- `timestamp` values reflect authoring date (2026-07-07); no fabricated future/past dates.

## Router Skill — `.claude/skills/oks-bundles/SKILL.md`

- **Frontmatter:** `name: oks-bundles`, `description` with explicit triggers (git/GitHub questions; how to structure a repo for AI agents).
- **Body:**
  - 3-line explanation of OKF (markdown + frontmatter + links; start at `index.md`).
  - Instruction to **navigate by starting at the relevant bundle's `index.md` and following links**, rather than blind grepping.
  - A decision table:
    - git / GitHub / commits / branches / PRs / history → `oks/git-best-practices`
    - how to lay out a repo so agents find skills/context/knowledge → `oks/ai-agent-repo-structure`
  - A note that concepts cite their sources, so agents can verify or dig deeper.

## Research Execution & Model Assignment

- **Sonnet subagents** (parallel, one per topic cluster): mechanical fetch/extract from specific official-doc URLs — low reasoning, high throughput.
- **Opus/Fable** (main thread or dedicated subagents): synthesis, concept authoring, cross-link graph design, and any judgment-heavy structuring.
- Web research restricted to an allowlist of primary domains (git-scm.com, docs.github.com, anthropic.com, cloud.google.com, atlassian.com official tutorials). Forums/Reddit excluded by policy.

## Git Hygiene (Dogfooding)

The repository will be built using the conventions the bundle documents:
a feature branch, atomic [Conventional Commits](https://www.conventionalcommits.org/),
and a clean, reviewable history — so the repo demonstrates its own advice.

## Deliverables

1. `oks/git-best-practices/` — complete OKF bundle.
2. `oks/ai-agent-repo-structure/` — complete OKF bundle.
3. `.claude/skills/oks-bundles/SKILL.md` — router skill.
4. `README.md` — repo overview.
5. This design doc, committed.

## Verification

- Every concept file has valid YAML frontmatter with at least `type`.
- Every internal cross-link resolves to an existing file.
- Every concept has a Sources section citing primary domains only.
- The router skill's decision table references both bundles by correct path.
- `git log` shows atomic, conventional commits on a feature branch.
