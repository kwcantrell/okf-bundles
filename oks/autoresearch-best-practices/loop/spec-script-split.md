---
type: OKF Concept
title: The Spec/Script Split
description: AutoResearch splits its repository into three files — human-edited instructions (program.md), the single file the agent edits (train.py), and a fixed evaluation harness (prepare.py) — so mutable code, fixed measurement, and human intent stay separate.
resource: https://github.com/karpathy/autoresearch
tags:
  - autoresearch
  - karpathy
  - repo-structure
timestamp: 2026-07-07T00:00:00Z
---

# The Spec/Script Split

AutoResearch keeps three things apart: what the human wants tried, what the agent
is allowed to change, and how a result is measured. That separation is expressed
as three files, and the discipline of the loop depends on it.

## Three files, three roles

- **`program.md` — human-edited instructions.** It holds the baseline
  instructions for one agent: "Point your agent here and let it go." The README
  is explicit that "This file is edited and iterated on by the human," and
  describes it as "essentially a super lightweight 'skill'." This is where human
  intent and search guidance live, not in the code being optimized.
- **`train.py` — the single file the agent edits.** It "Contains the full GPT
  model, optimizer (Muon + AdamW), and training loop," and the README states
  plainly that "This file is edited and iterated on by the agent." Everything in
  it is fair game for the search — architecture, hyperparameters, optimizer,
  batch size, and so on.
- **`prepare.py` — the fixed evaluation harness.** It holds "fixed constants,
  one-time data prep ... and runtime utilities (dataloader, evaluation)," and the
  README marks it "Not modified." Because it defines how results are measured, it
  must stay constant across experiments.

## Why the split matters

Separating the mutable script from fixed evaluation and human-authored intent is
what makes the loop trustworthy. If the agent could edit the evaluation harness,
`val_bpb` would stop being a stable yardstick — the agent could "improve" the
metric by changing how it is computed rather than by improving the model.
Holding `prepare.py` fixed keeps the accept/reject decision in
[keep or revert with git](/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md)
honest. Keeping human intent in `program.md` — separate from the code — is what
lets the human iterate on the research direction without touching the model, and
lets the agent iterate on the model without renegotiating intent. The agent edits
exactly one file, a constraint covered in
[single-file discipline](/oks/autoresearch-best-practices/loop/single-file-discipline.md),
and drives the full cycle in
[the agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md).

# Related

- [the agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md)
- [single-file discipline](/oks/autoresearch-best-practices/loop/single-file-discipline.md)

# Sources

- https://github.com/karpathy/autoresearch/blob/master/README.md
