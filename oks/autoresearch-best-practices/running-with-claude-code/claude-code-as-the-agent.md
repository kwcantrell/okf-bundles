---
type: OKF Concept
title: Claude Code as the Agent
description: Using Claude Code's headless mode as the autonomous coding agent that edits train.py, runs experiments, and iterates through the AutoResearch loop unattended.
resource: https://code.claude.com/docs/en/headless
tags:
  - autoresearch
  - karpathy
  - claude-code
timestamp: 2026-07-07T00:00:00Z
---

# Claude Code as the Agent

AutoResearch does not ship with or mandate any particular agent. Karpathy's repo
is deliberately agent-agnostic: `program.md` is "essentially a super lightweight
'skill'" that you point "your favorite coding agent" at. What the loop actually
requires is an autonomous coding agent that can do four things in a tight cycle —
edit a file, run a command, read the result, and decide to keep or discard the
change. Claude Code fits that shape, and this concept is about wiring it in as the
agent that drives the
[agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md).

## The agent's job in the loop

In AutoResearch the agent owns exactly one editable file. `train.py` "is the
single file the agent edits" — it contains the full GPT model, optimizer, and
training loop, and "everything is fair game: architecture, hyperparameters,
optimizer, batch size, etc." The agent tunes that file, `git commit`s the change,
runs `uv run train.py > run.log 2>&1`, reads `val_bpb` out of the output, and then
keeps the commit or `git reset`s it away. Those are all things Claude Code does
natively with its Edit and Bash tools: it edits the script, shells out to run the
experiment, and reads the log back.

## Running it headless for overnight loops

The loop's payoff is unattended runtime. `program.md` tells the agent it is
autonomous — "The human might be asleep... expects you to continue working
*indefinitely* until you are manually stopped" — and the README frames the win in
terms of sleep: at roughly five minutes per experiment the agent runs about 12 per
hour, "for a total of about 100 over the duration of the average human sleep."
That only works if the agent runs without a person answering prompts.

Claude Code's [headless mode](/oks/claude-best-practices/automation/headless-mode.md)
is the mechanism. Adding `-p` (or `--print`) to any `claude` command runs it
non-interactively: Claude Code executes the prompt, prints the result, and exits
instead of opening an interactive session. A kickoff along the lines of "have a
look at `program.md` and let's kick off a new experiment" becomes a headless
invocation that reads the instruction file and starts iterating. For scripted and
overnight use the docs recommend `--bare`, which skips auto-discovery of hooks,
skills, plugins, MCP servers, auto memory, and CLAUDE.md so a call produces the
same result on every machine.

Because the loop runs many experiments, you can also structure the work as
delegated sub-runs rather than one monolithic session — see
[delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md).
One practical constraint to know: a `claude -p` run waits for background
subagents and workflows, but that wait is capped at 10 minutes by default via
`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` — which lines up neatly with AutoResearch's
own rule that an experiment exceeding 10 minutes is killed and discarded.

# Related

- [the agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md)
- [headless mode](/oks/claude-best-practices/automation/headless-mode.md)
- [delegating to subagents](/oks/claude-best-practices/subagents/delegating-to-subagents.md)

# Sources

- https://code.claude.com/docs/en/headless
- https://github.com/karpathy/autoresearch/blob/master/README.md
- https://github.com/karpathy/autoresearch/blob/master/program.md
