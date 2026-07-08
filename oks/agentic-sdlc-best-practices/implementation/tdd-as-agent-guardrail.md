---
type: Agentic SDLC Practice
title: TDD As Agent Guardrail
description: Tests written before the code become an executable specification the agent must satisfy, turning "looks right" into "passes" and giving the agent an automated check it can iterate against without a human watching every step.
resource: https://code.claude.com/docs/en/best-practices
tags:
  - agentic-sdlc
  - implementation
timestamp: 2026-07-07T00:00:00Z
---

# TDD As Agent Guardrail

When an agent writes the implementation, the hardest failures are the ones that
look correct. AI errors have shifted from syntax mistakes a compiler catches to
conceptual failures that are "harder to detect precisely because the code 'looks
right' and may even pass basic tests" ([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 34). A prose prompt can't close that gap on its own, because the agent can
satisfy the words while missing the intent. A test can: it states what "correct"
means in a form the agent can run, fail, and be held to.

## Tests are the executable spec

Writing the tests first inverts the usual order for a reason. The test suite
becomes the contract the generated code has to satisfy, not a check bolted on
afterward — "a well-written eval suite tells the AI what 'correct' means and
provides an automated way to verify it" ([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 23). The paper's advice to individual developers is blunt: "Write the tests
and evals before generating the code. Together they are the contract with the
AI" (p. 43). A failing test is a concrete, unambiguous target; a paragraph of
requirements is not. The tests constrain the space of "code that looks done" down
to "code that actually satisfies the stated behavior."

## Give the agent a check it can run

The point of tests-first isn't only to catch the agent — it's to let the agent
catch itself. Anthropic frames the whole difference in terms of runnable checks:
"Give Claude a check it can run: tests, a build, a screenshot to compare. It's the
difference between a session you watch and one you walk away from"
([Claude Code best practices](https://code.claude.com/docs/en/best-practices)).
With a suite in place, the agent's implement–run–fix loop has a ground truth to
converge on instead of the agent's own judgment about whether it's finished. Make
the criteria concrete in the prompt rather than implicit — naming example cases
(such as which inputs are valid and which are rejected) and telling the agent to
run the tests after implementing gives it an unambiguous bar to clear.

## Framing, not a specific workflow

This is provider-general: the principle is that behavior gets specified as
executable checks before generation, whichever agent or language you use. The
concrete Claude Code workflow for doing this in a session — red/green cadence,
watching the agent against a failing test — lives in
[test-driven-development](/oks/claude-best-practices/workflows/test-driven-development.md)
and is not restated here.

One caveat that TDD alone does not resolve: when the same agent writes both the
tests and the code, it can write weak tests, or shape code to pass a test rather
than to be correct — reward hacking. Tests-first raises the floor, but it does not
remove the need for independent review of the tests themselves (a
verification-and-review concern covered elsewhere in this bundle).

# Related

- [test-driven-development](/oks/claude-best-practices/workflows/test-driven-development.md)
- [small verifiable increments](/oks/agentic-sdlc-best-practices/implementation/small-verifiable-increments.md)
- [agent-written tests and reward hacking](/oks/agentic-sdlc-best-practices/verification-and-review/agent-written-tests-and-reward-hacking.md)

# Sources

- https://code.claude.com/docs/en/best-practices
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
