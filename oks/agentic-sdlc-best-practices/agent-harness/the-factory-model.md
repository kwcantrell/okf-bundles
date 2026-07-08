---
type: Agentic SDLC Practice
title: The Factory Model
description: When agents write the code, the engineer's real output is the system that produces code — the harness, evals, and skills. The factory model says to invest there, and to treat the agent-plus-harness as a product with its own SDLC.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - agent-harness
timestamp: 2026-07-07T00:00:00Z
---

# The Factory Model

Once agents generate most of the code, the highest-leverage thing an engineer builds is no
longer the code — it is the machine that produces it. The paper names this the factory
model: "in this model, the developer's primary output is not code — it's the system that
produces code"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 24). The analogy it draws is a factory manager who "does not assemble every widget by
hand. They design the assembly line and ensure quality control. The modern developer designs
the development system and ensures that its output meets the required standard"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 25).

## Build the system, not just the output

The concrete shift is where you spend effort: not on hand-crafting each artifact, but on the
[harness](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md), the eval
suites, and the reusable skills that let the agent produce good artifacts repeatably. The
mode of instruction changes to match: "success comes from giving agents success criteria
rather than step-by-step instructions, then letting them iterate"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 25). You define
what "done" and "good" mean — the criteria and the checks — and let the factory run against
them.

## The assembly line needs quality control

A factory without quality control just produces defects faster, and the paper is explicit
about the risk: "without an automated evaluation harness, the rapid generation of code leads
to the rapid generation of vulnerabilities"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 41). This is why
[evals](/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md)
are load-bearing in the factory model rather than an afterthought — they are the quality-control
station on the line. The advice to leaders sharpens it: "set the bar at the eval, not the demo.
A working demo proves an agent can succeed once. A passing eval suite proves it succeeds
reliably"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 44).

## Treat the agent-plus-harness as a product with its own SDLC

The deepest implication is recursive: the factory is itself a piece of software, so it gets
its own software lifecycle. It is specified, built, tested against evals, deployed, observed,
and iterated — the same phases you apply to the products it makes. This is why organizations
are urged to "treat AI-assisted development as an engineering investment, not a productivity
feature," pairing tooling with "eval coverage, observability, and clear architectural
standards"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 45). The harness
is a product; its evals are its test suite; its skills are its features. Investing in the
factory is investing in every artifact it will ever produce.

Building and packaging reusable skills libraries for the factory is a further application
covered later in this bundle.

# Related

- [harness engineering](/oks/agentic-sdlc-best-practices/agent-harness/harness-engineering.md)
- [evals for agentic changes](/oks/agentic-sdlc-best-practices/verification-and-review/evals-for-agentic-changes.md)
- [skills libraries](/oks/agentic-sdlc-best-practices/applications/skills-libraries.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
