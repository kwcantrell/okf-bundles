---
type: Agentic SDLC Practice
title: Generating System Prompts
description: A coding-agent system prompt is repo and SDLC knowledge compiled into the model's static instruction layer — gathered from the AGENTS.md and docs, set at the right altitude, wired to the repo's gates and verification loops, and then evaluated against evals rather than tuned by vibes.
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags:
  - agentic-sdlc
  - applications
timestamp: 2026-07-07T00:00:00Z
---

# Generating System Prompts

Where an AGENTS.md is the portable, repo-facing instruction file, a system prompt
is the instruction layer of a specific harness — the always-loaded static context
that shapes how one agent behaves across every task. Much of its raw material
already exists: the repo's conventions, gates, and guardrails were captured while
[authoring an AGENTS.md](/oks/agentic-sdlc-best-practices/applications/authoring-an-agents-md.md).
This procedure compiles that knowledge into a prompt and then holds it to a bar —
"a passing eval suite proves it succeeds reliably" where a demo only proves it can
succeed once (kaggle.com). The design principles it applies live in
[system prompt design](/oks/agentic-sdlc-best-practices/agent-harness/system-prompt-design.md);
this is the authoring loop that produces one.

## Procedure: turning repo/SDLC knowledge into a system prompt

1. **Gather the raw material.** Pull the durable facts from the AGENTS.md, design
   docs, and conventions: the stack, the build/test/lint commands, the SDLC gates,
   the guardrails. Prefer deriving instructions from existing operating documents
   over inventing them (cdn.openai.com) — the prompt should restate what the repo
   already knows, compressed.

2. **Set the altitude.** Aim for the middle band between rigid and vague: "specific
   enough to guide behavior effectively, yet flexible enough to provide the model
   with strong heuristics" (anthropic.com). Encode behavioural heuristics, not a
   brittle if/else tree — over-specified rules rot as the repo changes, and
   under-specified ones fail to steer.

3. **Encode the SDLC gates and verification loops.** State the phased shape of the
   work explicitly — a harness that earned double-digit benchmark gains structured
   the prompt into Planning & Discovery, Build, Verify, and Fix stages
   (langchain.com). Make verification a required step, not an optional one: give
   the agent a check it can run and tell it to iterate until the check passes
   rather than stopping when the work "looks done" (code.claude.com). Route agent
   changes to
   [evals for agentic changes](/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md)
   as the definition of "correct."

4. **Add examples.** Concrete example cases — e.g. spelled-out test inputs and
   expected outputs — reduce interpretation error more than abstract description
   (code.claude.com). Include a small number of high-signal examples of the
   behaviour you want, especially for the edge cases the repo cares about.

5. **Evaluate and iterate — evals, not vibes.** Establish a baseline against an
   eval suite, then change one thing at a time and re-measure (cdn.openai.com).
   Set the quality bar at the eval, not the demo (kaggle.com). Only keep a prompt
   change that moves the suite; discard changes that merely *feel* better.

## Skeleton system-prompt structure

```markdown
# Role & altitude
> Who the agent is and the level it operates at — heuristics, not a rule tree.

# Repo facts
> Stack, key commands, conventions — compiled from the AGENTS.md and docs.

# Workflow stages
> Planning & Discovery -> Build -> Verify -> Fix, stated as required steps.

# Verification
> The check the agent must run and iterate against before claiming done.

# Guardrails
> Hard constraints and the points where it must hand back to a human.

# Examples
> A few concrete input/expected-output cases, including edge cases.
```

# Related

- [system prompt design](/oks/agentic-sdlc-best-practices/agent-harness/system-prompt-design.md)
- [authoring an AGENTS.md](/oks/agentic-sdlc-best-practices/applications/authoring-an-agents-md.md)
- [evals for agentic changes](/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md)

# Sources

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
