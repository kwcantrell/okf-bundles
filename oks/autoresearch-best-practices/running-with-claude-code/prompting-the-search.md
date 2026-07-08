---
type: OKF Concept
title: Prompting the Search
description: Reframing AutoResearch's hyperparameter and architecture search as prompt engineering — specific, well-scoped instructions steer the agent through the space with fewer corrections.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - autoresearch
  - karpathy
  - claude-code
timestamp: 2026-07-07T00:00:00Z
---

# Prompting the Search

In AutoResearch the human does not tune hyperparameters directly — the human tunes
the *instructions*. As the README puts it, "you are programming the `program.md`
Markdown files that provide context to the AI agents." The search over
architecture, optimizer, and hyperparameters is therefore a prompt-engineering
problem: the quality of the exploration depends on how well the instruction file
steers the agent through the space. This concept is about writing those
instructions well when Claude Code is the agent running the
[agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md).

## The search space is wide, so the prompt has to shape it

`program.md` deliberately opens the whole script to change: "Everything is fair
game: model architecture, optimizer, hyperparameters, training loop, batch size,
model size, etc." An unbounded space plus a vague instruction produces wandering.
The repo counters this with concrete guidance — a `val_bpb` objective, a
simplicity criterion, and a fallback for when the agent stalls: "If you run out of
ideas, think harder — read papers referenced in the code, re-read the in-scope
files for new angles, try combining previous near-misses, try more radical
architectural changes." Those are search directives, written as prose.

## Specific instructions beat vague ones

This is exactly where Claude Code's own prompting guidance applies. The official
best-practices docs put it plainly: "The more precise your instructions, the fewer
corrections you'll need. Claude can infer intent, but it can't read your mind.
Reference specific files, mention constraints, and point to example patterns."
Translated to the loop, that means naming the knobs to try (or to leave alone),
pointing at the papers or prior near-misses to draw from, and stating the accept
criterion in the same terms the agent will measure — see
[be specific in instructions](/oks/claude-best-practices/context/be-specific-in-instructions.md).

The docs also note the flip side: vague prompts are useful precisely when you are
exploring and can afford to course-correct — "A prompt like 'what would you improve
in this file?' can surface things you wouldn't have thought to ask about." An
autonomous overnight loop is the opposite regime. Nobody is watching to
course-correct, so the instruction file has to carry the specificity up front:
what to search over, what "better" means (a lower `val_bpb`), and what to do when a
direction dries up. The more of that intent you bake into `program.md`, the more of
the unattended run is spent on productive experiments rather than misread goals.

# Related

- [the agent research loop](/oks/autoresearch-best-practices/loop/agent-research-loop.md)
- [be specific in instructions](/oks/claude-best-practices/context/be-specific-in-instructions.md)

# Sources

- https://code.claude.com/docs/en/best-practices
- https://github.com/karpathy/autoresearch/blob/master/README.md
- https://github.com/karpathy/autoresearch/blob/master/program.md
