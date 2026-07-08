---
type: OKF Concept
title: The Agent Research Loop
description: AutoResearch's core cycle — the agent edits train.py, commits, runs a time-boxed experiment, reads val_bpb, and keeps or resets the change — run autonomously overnight.
resource: https://github.com/karpathy/autoresearch
tags:
  - autoresearch
  - karpathy
  - research-loop
timestamp: 2026-07-07T00:00:00Z
---

# The Agent Research Loop

AutoResearch gives an AI agent a small but real LLM training setup and lets it
experiment autonomously. The README states the idea directly: the agent
"modifies the code, trains for 5 minutes, checks if the result improved, keeps or
discards, and repeats. You wake up in the morning to a log of experiments and
(hopefully) a better model." The whole system is an outer loop wrapped around a
single training script.

## The cycle

`program.md` spells out the loop the agent runs, step by step:

1. **Look at the git state** to see where the current best result stands.
2. **Tune `train.py` with an experimental idea** by directly hacking the code —
   the agent edits one file (see [single-file discipline](/oks/autoresearch-best-practices/loop/single-file-discipline.md)).
3. **`git commit`** the change, so the experiment corresponds to a commit.
4. **Run the experiment**: `uv run train.py > run.log 2>&1`. The run is
   time-boxed — a run exceeding 10 minutes is killed and treated as a failure.
5. **Read out the results**, in particular `val_bpb` (validation bits per byte),
   the single metric the loop optimizes.
6. **Keep or reset**: if `val_bpb` improved (lower), the agent "advances" the
   branch, keeping the commit; if it is equal or worse, the agent runs
   `git reset` back to where it started. This accept/reject step is the heart of
   the loop — see [keep or revert with git](/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md).
7. **Repeat**, proposing the next idea.

Each run is appended to a `results.tsv` log with a `keep` / `discard` / `crash`
status, so the morning after leaves a legible trail of what was tried.

## Autonomous and overnight

The loop is designed to run without a human in the seat. `program.md` includes a
`NEVER STOP` rule: once the experiment loop has begun, the agent must not pause to
ask the human whether to continue — "The human might be asleep, or gone from a
computer and expects you to continue working *indefinitely* until you are
manually stopped. You are autonomous." The README frames the payoff in terms of
sleep: at roughly 5 minutes per experiment the agent can run about 12 per hour,
"for a total of about 100 over the duration of the average human sleep." The user
wakes to a batch of completed results.

## The shift in human effort

The point of the setup is to move human effort up a level. Instead of
hand-tuning hyperparameters and architecture, the human authors and iterates on
the instruction file: as the README puts it, "you are programming the
`program.md` Markdown files that provide context to the AI agents and set up your
autonomous research org." The human writes the intent and the search guidance;
the agent runs the experiments. The division of labor between the human-edited
spec and the agent-edited script is covered in
[spec/script split](/oks/autoresearch-best-practices/loop/spec-script-split.md).

# Related

- [spec/script split](/oks/autoresearch-best-practices/loop/spec-script-split.md)
- [single-file discipline](/oks/autoresearch-best-practices/loop/single-file-discipline.md)
- [keep or revert with git](/oks/autoresearch-best-practices/loop/keep-or-revert-with-git.md)
- [claude code as the agent](/oks/autoresearch-best-practices/running-with-claude-code/claude-code-as-the-agent.md)

# Sources

- https://github.com/karpathy/autoresearch/blob/master/README.md
- https://github.com/karpathy/autoresearch/blob/master/program.md
