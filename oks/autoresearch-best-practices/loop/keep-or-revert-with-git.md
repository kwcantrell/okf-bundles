---
type: OKF Concept
title: Keep or Revert with Git
description: AutoResearch uses val_bpb as the accept/reject signal — advancing the git branch to keep an improvement or running git reset to discard it — with a 10-minute timeout and a simplicity criterion weighing complexity against gains.
resource: https://github.com/karpathy/autoresearch/blob/master/program.md
tags:
  - autoresearch
  - karpathy
  - git
timestamp: 2026-07-07T00:00:00Z
---

# Keep or Revert with Git

Each experiment in AutoResearch ends with a decision: keep the change or throw it
away. That decision is made against a single number and executed with git.

## The accept/reject signal

The metric is `val_bpb` (validation bits per byte). Lower is better, and because
bits per byte is vocab-size-independent, architectural changes are compared
fairly against one another. `program.md` reduces the whole objective to one line:
"**The goal is simple: get the lowest val_bpb.**" The metric is computed by the
`evaluate_bpb` function in `prepare.py`, which the agent may not modify — it is
"the ground truth metric," which is why the fixed evaluation harness is held
apart in [spec/script split](/oks/autoresearch-best-practices/loop/spec-script-split.md).

## Keep by advancing, discard by resetting

Because every experiment is committed before it runs (see
[the agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md)),
the accept/reject step is a git operation:

- **If `val_bpb` improved** (lower), the agent "advances" the branch, keeping the
  git commit. The improvement becomes the new baseline the next experiment builds
  on.
- **If `val_bpb` is equal or worse**, the agent runs `git reset` back to where it
  started, discarding the change. Note this is `git reset` — moving the branch
  pointer back to the previous commit — not a new revert commit on top.

Using commits as the unit of experiment, and keeping or discarding each one
cleanly, is a training-research analogue of the general practice of
[atomic commits](/oks/git-best-practices/commits/atomic-commits.md): one commit
is one self-contained, reversible change.

## Guardrails on the decision

Two rules keep the accept/reject loop well-behaved:

- **Timeout.** Runtime is bounded: "If a run exceeds 10 minutes, kill it and
  treat it as a failure (discard and revert)." A too-slow experiment is thrown
  away rather than allowed to stall the loop.
- **Simplicity criterion.** A lower `val_bpb` is not automatically worth keeping.
  `program.md` adds: "**Simplicity criterion**: All else being equal, simpler is
  better ... When evaluating whether to keep a change, weigh the complexity cost
  against the improvement magnitude." A large gain justifies added complexity; a
  marginal one may not.

# Related

- [the agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md)
- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)

# Sources

- https://github.com/karpathy/autoresearch/blob/master/program.md
