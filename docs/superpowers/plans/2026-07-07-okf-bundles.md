# OKF Bundles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build two OKF v0.1 bundles (`git-best-practices`, `ai-agent-repo-structure`) and a Claude Code router skill, all grounded in primary-source research.

**Architecture:** Each bundle is a directory of markdown "concept" files with YAML frontmatter, an `index.md` for progressive disclosure, a `log.md` for history, and root-relative markdown cross-links forming a concept graph. Research is done by Sonnet subagents (mechanical fetch/extract from official docs) and synthesized into concepts by higher-reasoning models. A validation script enforces OKF invariants after each authoring task.

**Tech Stack:** Markdown + YAML frontmatter; Python 3 (stdlib only) for the validator; git with Conventional Commits.

## Global Constraints

- OKF v0.1: every concept file has YAML frontmatter with **at least `type`**; standard fields populated: `type`, `title`, `description`, `resource`, `tags`, `timestamp`.
- `timestamp` = `2026-07-07T00:00:00Z` for all concepts authored in this effort (no fabricated dates).
- Cross-links are **root-relative** markdown links, e.g. `/oks/git-best-practices/commits/atomic-commits.md`.
- Every concept ends with a `# Sources` section citing **primary domains only**: `git-scm.com`, `docs.github.com`, `atlassian.com`, `anthropic.com`, `docs.claude.com`, `cloud.google.com`, `agents.md`, `conventionalcommits.org`. No forums/Reddit/unattributed blogs.
- All work on branch `feat/okf-bundles`; atomic Conventional Commits.
- Subagent model assignment: **Sonnet** for fetch/extract; **Opus/Fable** for synthesis/authoring judgment.
- Bundle roots: `oks/git-best-practices/`, `oks/ai-agent-repo-structure/`.

---

### Task 1: OKF validator + repo scaffolding

**Files:**
- Create: `tools/validate_okf.py`
- Create: `oks/git-best-practices/` and `oks/ai-agent-repo-structure/` (via first concept files in later tasks)
- Test: run the validator itself

**Interfaces:**
- Produces: `python3 tools/validate_okf.py [BUNDLE_DIR ...]` — exits non-zero if any `.md` concept (excluding `log.md`) lacks frontmatter/`type`, if any root-relative link target is missing, or if any concept (excluding `index.md`/`log.md`) has no `# Sources` section. Prints one line per violation. With no args, scans all of `oks/`.

- [ ] **Step 1: Write the validator**

```python
#!/usr/bin/env python3
"""Validate OKF bundles: frontmatter, required `type`, link resolution, Sources."""
import re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
FM = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK = re.compile(r"\]\((/[^)]+\.md)\)")

def concepts(root):
    return [p for p in root.rglob("*.md")]

def check(root):
    errors = []
    for p in concepts(root):
        text = p.read_text(encoding="utf-8")
        rel = p.relative_to(REPO)
        name = p.name
        m = FM.match(text)
        if name != "log.md":
            if not m:
                errors.append(f"{rel}: missing YAML frontmatter")
            elif not re.search(r"^type:\s*\S", m.group(1), re.MULTILINE):
                errors.append(f"{rel}: frontmatter missing required `type`")
        if name not in ("index.md", "log.md") and "# Sources" not in text:
            errors.append(f"{rel}: missing `# Sources` section")
        for target in LINK.findall(text):
            if not (REPO / target.lstrip("/")).exists():
                errors.append(f"{rel}: broken link -> {target}")
    return errors

def main():
    roots = [pathlib.Path(a) for a in sys.argv[1:]] or [REPO / "oks"]
    errors = []
    for r in roots:
        if r.exists():
            errors += check(r)
    for e in errors:
        print(e)
    print(f"\n{len(errors)} violation(s)")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run validator on empty oks/ to verify it passes cleanly**

Run: `mkdir -p oks && python3 tools/validate_okf.py`
Expected: `0 violation(s)` and exit 0.

- [ ] **Step 3: Sanity-check failure detection**

Run: `printf 'no frontmatter\n' > oks/_tmp.md && python3 tools/validate_okf.py; rm oks/_tmp.md`
Expected: prints `oks/_tmp.md: missing YAML frontmatter` and `oks/_tmp.md: missing \`# Sources\` section`, exit 1.

- [ ] **Step 4: Commit**

```bash
git add tools/validate_okf.py
git commit -m "build: add OKF bundle validator"
```

---

### Task 2: Research pass — git-best-practices (Sonnet fetchers)

**Files:**
- Create: `docs/superpowers/research/git-best-practices-notes.md` (working notes; committed for traceability)

**Interfaces:**
- Produces: a notes file with, per Bundle A concept, 3-6 bullet facts each paired with a primary-source URL. Consumed by Tasks 3-4.

- [ ] **Step 1: Dispatch parallel Sonnet research subagents**

Use the Agent tool (`subagent_type: general-purpose`, `model: sonnet`), one per topic cluster, in a single message for concurrency. Cluster → allowed domains:
- fundamentals + history → `git-scm.com` (Pro Git book, reference)
- workflows + branching → `docs.github.com`, `atlassian.com`
- commits + collaboration → `git-scm.com`, `docs.github.com`, `conventionalcommits.org`
- remote + automation + scale → `git-scm.com`, `docs.github.com`
- security → `docs.github.com`, `git-scm.com`

Each subagent prompt: "Extract concrete, citable best-practice facts for concepts [list]. For each fact give a one-line statement and the exact source URL. Use ONLY these domains: [list]. Return markdown bullets grouped by concept. Do not editorialize; facts + URLs only."

- [ ] **Step 2: Consolidate subagent outputs into the notes file**

Write each subagent's returned bullets under a `## <concept>` heading. Every bullet must carry a URL on an allowed domain.

- [ ] **Step 3: Verify coverage**

Run: `grep -c '^## ' docs/superpowers/research/git-best-practices-notes.md`
Expected: ≥ 20 (one per Bundle A concept). If short, dispatch a follow-up subagent for the missing concepts.

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/research/git-best-practices-notes.md
git commit -m "docs: research notes for git-best-practices bundle"
```

---

### Task 3: Author git-best-practices — structure, index, and half the concepts

**Files:**
- Create: `oks/git-best-practices/index.md`, `log.md`
- Create: `fundamentals/`, `workflows/`, `branching/`, `commits/`, `collaboration/` concept files + their `index.md` (per spec tree)

**Interfaces:**
- Consumes: `git-best-practices-notes.md`.
- Produces: concept files following the frontmatter + `# Sources` contract; `index.md` links to every subdir index.

- [ ] **Step 1: Write the bundle `index.md`**

Frontmatter (`type: OKF Bundle Index`, title, description, resource `https://git-scm.com/doc`, tags, timestamp `2026-07-07T00:00:00Z`) + a body that lists each concept area with a one-line summary and a root-relative link to each subdirectory `index.md`. No `# Sources` required for `index.md`.

- [ ] **Step 2: Write `log.md`**

Plain markdown (no frontmatter required): a dated entry `2026-07-07 — bundle created` summarizing initial scope.

- [ ] **Step 3: Author concepts for fundamentals, workflows, branching, commits, collaboration**

For each concept file in these five areas (per the spec tree), write: full frontmatter; body explaining the practice with concrete guidance and trade-offs (no mandates where valid alternatives exist); `# Related` links to sibling concepts; `# Sources` citing the notes' URLs for that concept. Use Opus/Fable-level judgment for structure and cross-linking. Each subdir gets an `index.md` linking its concepts.

- [ ] **Step 4: Validate**

Run: `python3 tools/validate_okf.py oks/git-best-practices`
Expected: `0 violation(s)`.

- [ ] **Step 5: Commit**

```bash
git add oks/git-best-practices
git commit -m "docs: add git-best-practices bundle (fundamentals..collaboration)"
```

---

### Task 4: Author git-best-practices — remaining concepts

**Files:**
- Create: `history/`, `remote/`, `automation/`, `security/`, `scale/` concept files + their `index.md`
- Modify: `oks/git-best-practices/index.md` (ensure all five areas are linked)

**Interfaces:**
- Consumes: `git-best-practices-notes.md`; sibling concepts from Task 3 for cross-links.
- Produces: a complete Bundle A.

- [ ] **Step 1: Author concepts for history, remote, automation, security, scale**

Same contract as Task 3 Step 3. Cross-link into Task 3 concepts where relevant (e.g. `rebasing` ↔ `merge-vs-rebase`, `signing-commits` ↔ `signed-tags`).

- [ ] **Step 2: Confirm the bundle index links all ten areas**

Run: `grep -c '](/oks/git-best-practices/.*index.md)' oks/git-best-practices/index.md`
Expected: `10`.

- [ ] **Step 3: Validate full bundle**

Run: `python3 tools/validate_okf.py oks/git-best-practices`
Expected: `0 violation(s)`.

- [ ] **Step 4: Commit**

```bash
git add oks/git-best-practices
git commit -m "docs: complete git-best-practices bundle (history..scale)"
```

---

### Task 5: Research pass — ai-agent-repo-structure (Sonnet fetchers)

**Files:**
- Create: `docs/superpowers/research/ai-agent-repo-structure-notes.md`

**Interfaces:**
- Produces: per-concept facts + primary-source URLs for Bundle B. Consumed by Task 6.

- [ ] **Step 1: Dispatch parallel Sonnet research subagents**

Agent tool (`model: sonnet`), clusters → domains:
- context-files (AGENTS.md / CLAUDE.md, precedence, progressive disclosure) → `agents.md`, `docs.claude.com`, `anthropic.com`
- skills (format, placement, project vs personal) → `docs.claude.com`, `anthropic.com`
- conventions + knowledge (directory layout, OKF-in-repos, machine-readable metadata) → `docs.claude.com`, `cloud.google.com`, `agents.md`
- tooling + practices (MCP, slash commands, hooks, guardrails) → `docs.claude.com`, `anthropic.com`

Same "facts + URLs only, allowed domains only" prompt shape as Task 2.

- [ ] **Step 2: Consolidate into the notes file** (one `## <concept>` heading each).

- [ ] **Step 3: Verify coverage**

Run: `grep -c '^## ' docs/superpowers/research/ai-agent-repo-structure-notes.md`
Expected: ≥ 8.

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/research/ai-agent-repo-structure-notes.md
git commit -m "docs: research notes for ai-agent-repo-structure bundle"
```

---

### Task 6: Author ai-agent-repo-structure bundle

**Files:**
- Create: `oks/ai-agent-repo-structure/index.md`, `log.md`, and all concept files + subdir `index.md` per the spec tree.

**Interfaces:**
- Consumes: `ai-agent-repo-structure-notes.md`.
- Produces: complete Bundle B. Cross-links to Bundle A where relevant (e.g. `knowledge/okf-bundles-in-repos` → `/oks/git-best-practices/index.md`).

- [ ] **Step 1: Write bundle `index.md` and `log.md`** (same contract as Task 3 Steps 1-2; resource `https://agents.md`).

- [ ] **Step 2: Author all Bundle B concepts** (frontmatter + body + `# Related` + `# Sources`), with subdir `index.md` files.

- [ ] **Step 3: Validate**

Run: `python3 tools/validate_okf.py oks/ai-agent-repo-structure`
Expected: `0 violation(s)`.

- [ ] **Step 4: Commit**

```bash
git add oks/ai-agent-repo-structure
git commit -m "docs: add ai-agent-repo-structure bundle"
```

---

### Task 7: Router skill + README

**Files:**
- Create: `.claude/skills/oks-bundles/SKILL.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: both bundle roots (paths must be correct).
- Produces: a discoverable skill routing agents to bundles.

- [ ] **Step 1: Write `SKILL.md`**

YAML frontmatter: `name: oks-bundles`; `description:` with explicit triggers ("Use when the user asks about git or GitHub workflows/conventions, or how to structure a repository so AI agents can discover skills, context files, and knowledge."). Body: 3-line OKF explanation; instruction to start at the relevant bundle's `index.md` and follow links (not blind grep); a decision table mapping git/GitHub topics → `/oks/git-best-practices/index.md` and agent-repo-layout topics → `/oks/ai-agent-repo-structure/index.md`; note that concepts cite primary sources.

- [ ] **Step 2: Expand `README.md`**

Describe the repo: what OKF is (1-2 lines), the two bundles with their paths and one-line purpose, the router skill, and how to consume a bundle (start at `index.md`).

- [ ] **Step 3: Verify skill references resolve**

Run: `python3 tools/validate_okf.py && grep -o '/oks/[a-z-]*/index.md' .claude/skills/oks-bundles/SKILL.md | sort -u | while read p; do test -f ".${p}" && echo "ok $p" || echo "MISSING $p"; done`
Expected: two `ok` lines, no `MISSING`.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/oks-bundles/SKILL.md README.md
git commit -m "feat: add oks-bundles router skill and repo README"
```

---

### Task 8: Final verification pass

**Files:** none (verification only).

- [ ] **Step 1: Full-repo OKF validation**

Run: `python3 tools/validate_okf.py`
Expected: `0 violation(s)`.

- [ ] **Step 2: Concept count check against spec targets**

Run: `find oks/git-best-practices -name '*.md' | wc -l && find oks/ai-agent-repo-structure -name '*.md' | wc -l`
Expected: Bundle A ≥ 20, Bundle B ≥ 8 (counting concepts; indexes/log are additional).

- [ ] **Step 3: Source-domain audit**

Run: `grep -rhoE 'https?://[a-zA-Z0-9.-]+' oks/ | sed -E 's#https?://##; s#/.*##' | sort -u`
Expected: only allowed primary domains appear (git-scm.com, docs.github.com, atlassian.com, anthropic.com, docs.claude.com, cloud.google.com, agents.md, conventionalcommits.org). Any other domain is a violation to fix.

- [ ] **Step 4: Review git history**

Run: `git log --oneline`
Expected: atomic Conventional Commits, one per task deliverable.

---

## Self-Review

**Spec coverage:** Bundle A tree → Tasks 3-4; Bundle B tree → Task 6; OKF conventions → validator (Task 1) + authoring contracts; router skill → Task 7; README → Task 7; research (primary-source, model assignment) → Tasks 2 & 5; dogfooding (branch + conventional commits) → Global Constraints + every task's commit step; verification section → Task 8. No gaps.

**Placeholder scan:** No TBD/TODO. Authoring steps reference the concrete spec tree and the research notes rather than inventing content inline (content is research-derived, so it cannot be literal-coded in advance — the contract each concept must satisfy is fully specified: frontmatter fields, `# Related`, `# Sources`, allowed domains, validated by `tools/validate_okf.py`).

**Type consistency:** Validator invocation `python3 tools/validate_okf.py [DIR]` is identical across all tasks; link format `/oks/<bundle>/.../*.md` is consistent; frontmatter field set and timestamp value are identical everywhere.
