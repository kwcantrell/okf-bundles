---
type: OKF Concept Index
title: The AutoResearch Loop
description: The mechanics of Karpathy's autoresearch autonomous-ML-research loop — the edit/run/measure/keep-or-reset cycle, the spec/script split, single-file discipline, and git as the accept/reject mechanism.
resource: https://github.com/karpathy/autoresearch
tags:
  - autoresearch
  - karpathy
timestamp: 2026-07-07T00:00:00Z
---

# The AutoResearch Loop

AutoResearch gives an AI agent a small but real LLM training setup and lets it
experiment autonomously overnight: it edits the code, trains for a few minutes,
checks whether the result improved, keeps or discards the change, and repeats.
These concepts cover the moving parts of that loop — the cycle itself, how the
repository is split so the loop is safe to run, why the agent edits only one
file, and how git commits serve as the accept/reject mechanism.

## Concepts

- [agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md) — the full edit → commit → time-boxed run → read `val_bpb` → keep-or-reset cycle, run autonomously overnight, and the shift of human effort from hand-tuning to authoring the instruction file.
- [spec/script split](/oks/autoresearch-best-practices/loop/spec-script-split.md) — the three-file layout: `program.md` (human-edited instructions), `train.py` (the file the agent edits), and `prepare.py` (the fixed evaluation harness the agent must not touch).
- [single-file discipline](/oks/autoresearch-best-practices/loop/single-file-discipline.md) — the agent edits only one ~630-line file; the stated rationale is manageable scope, reviewable diffs, and a self-contained setup.
- [keep or revert with git](/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md) — `val_bpb` as the accept/reject signal, advancing the branch to keep an improvement or `git reset` to discard it, the 10-minute timeout, and the simplicity criterion.
