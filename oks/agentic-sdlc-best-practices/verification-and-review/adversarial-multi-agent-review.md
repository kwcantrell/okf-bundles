---
type: Agentic SDLC Practice
title: Adversarial Multi-Agent Review
description: A panel of skeptical reviewers with distinct mandates finds more than one reviewer run many times, because diverse lenses cover different failure modes while redundant clones just repeat the same blind spots. A verification pass over the findings keeps the panel honest.
resource: https://www.anthropic.com/engineering/building-effective-agents
tags:
  - agentic-sdlc
  - verification-and-review
timestamp: 2026-07-07T00:00:00Z
---

# Adversarial Multi-Agent Review

Independent review says the agent that did the work should not be the one grading it.
Adversarial multi-agent review pushes that further: for a change important enough to
justify it, run *several* reviewers at once, each told to find a different way the
change is wrong. The gain comes not from more reviewers but from *different* ones —
reviewers whose mandates do not overlap, so their coverage adds up instead of piling
onto the same spot.

## A panel of skeptical reviewers with distinct mandates

The structural move is to give each reviewer a narrow, adversarial charge rather than
a general "does this look okay?" One reviewer hunts for requirements the change fails
to meet; another attacks the assumptions the change takes for granted; another threat-
models how it breaks or gets abused; another argues it is over-built and a simpler
design exists. Each is calibrated skeptical — its default is to find a path to a wrong
or broken outcome before approving, the opposite of a reviewer that approves unless
something is obviously broken. This maps naturally onto the orchestrator-workers
pattern, in which "a central LLM dynamically breaks down tasks, delegates them to
worker LLMs, and synthesizes their results"
([Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)):
the orchestrator fans the diff out to worker reviewers with distinct mandates and then
synthesizes their findings — deduping overlap, resolving conflicts, and ranking what
remains by severity.

## Why diverse lenses beat redundant clones

Running the same reviewer prompt three times mostly reproduces the same result three
times — identical strengths, and identical blind spots. Whatever the first pass fails
to see, the clones fail to see too, and the extra runs buy confidence without buying
coverage. Distinct mandates change that: a requirements reviewer and a threat-model
reviewer fail in different places, so a gap invisible to one is squarely in the other's
charge. Anthropic's advice to use worker LLMs "for tasks whose subtasks can't be
predicted in advance," synthesizing their varied results, is the same logic — the value
is in the *variety* of the workers, not their count. A panel is a way to buy coverage
across failure modes; cloning is a way to buy repetition.

## Verify the findings, don't just collect them

A skeptical reviewer that is rewarded for finding problems will find problems whether
or not they are real, and an unverified pile of findings is its own kind of noise — it
re-creates the reviewer-attention problem it was meant to solve. So the panel's output
is not the final word; it is input to a verification pass. Anthropic frames the general
principle as having "a fresh model try to refute the result, so the agent doing the work
isn't the one grading it"
([Claude Code best practices](https://code.claude.com/docs/en/best-practices)) — applied
here, that means checking each flagged finding against the actual diff before it reaches
a human, discarding the ones that do not hold up. The panel *arms* the human gate with a
ranked, verified list of real concerns; it does not replace the human's decision. The
mechanics of running reviewers concurrently in separate context windows are a Claude Code
subject covered elsewhere.

# Related

- [reviewing AI-generated code](/oks/agentic-sdlc-best-practices/verification-and-review/reviewing-ai-generated-code.md)
- [human-in-the-loop checkpoints](/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md)
- [parallel agents](/oks/claude-best-practices/subagents/parallel-agents.md)

# Sources

- https://www.anthropic.com/engineering/building-effective-agents
- https://code.claude.com/docs/en/best-practices
