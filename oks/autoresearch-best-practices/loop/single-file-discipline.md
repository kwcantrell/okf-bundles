---
type: OKF Concept
title: Single-File Discipline
description: In AutoResearch the agent edits only one ~630-line file, train.py; the repository's stated rationale is manageable scope, reviewable diffs, and a self-contained setup — "One GPU, one file, one metric."
resource: https://github.com/karpathy/autoresearch
tags:
  - autoresearch
  - karpathy
  - simplicity
timestamp: 2026-07-07T00:00:00Z
---

# Single-File Discipline

AutoResearch constrains the agent to edit a single file. The README puts it as a
design principle: "**Single file to modify.** The agent only touches `train.py`.
This keeps the scope manageable and diffs reviewable." That one file is
`train.py`, which holds the full GPT model, the optimizer, and the training
loop, and is 630 lines long.

## Why one file

The rationale the repository states is about scope and review, not about any
particular capacity limit. Two properties follow from confining all changes to
one file:

- **Manageable scope.** Every experiment is a change to the same file, so the
  search space is bounded and the agent never has to reason across a sprawling
  codebase to make a change.
- **Reviewable diffs.** Because each experiment is a commit that touches one
  file, its diff is small and legible — a human (or the agent) can see exactly
  what an experiment changed. This is what makes the keep-or-reset decision in
  [keep or revert with git](/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md)
  auditable after the fact.

The setup is also deliberately self-contained. The README describes it as
"**Self-contained.** No external dependencies beyond PyTorch and a few small
packages. No distributed training, no complex configs. One GPU, one file, one
metric." The single editable file sits alongside a fixed evaluation harness and a
human-edited instruction file — see
[spec/script split](/oks/autoresearch-best-practices/loop/spec-script-split.md) —
so the one file the agent changes is cleanly separated from the parts that must
stay constant.

# Related

- [spec/script split](/oks/autoresearch-best-practices/loop/spec-script-split.md)
- [the agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md)

# Sources

- https://github.com/karpathy/autoresearch/blob/master/README.md
- https://github.com/karpathy/autoresearch/blob/master/train.py
