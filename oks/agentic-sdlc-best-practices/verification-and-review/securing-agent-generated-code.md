---
type: Agentic SDLC Practice
title: Securing Agent-Generated Code
description: AI writes vulnerabilities as fluently as it writes features, so security posture for agent-authored changes is layered rather than single-check — dependency and injection review, provenance of what the agent pulled in, and a hard human gate on anything security-sensitive.
resource: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
tags:
  - agentic-sdlc
  - verification-and-review
timestamp: 2026-07-07T00:00:00Z
---

# Securing Agent-Generated Code

An agent generates secure and insecure code with equal fluency; nothing in the
generation process distinguishes them. The paper states the consequence plainly:
"without an automated evaluation harness, the rapid generation of code leads to the
rapid generation of vulnerabilities. The cost of fixing a security flaw in production
is exponentially higher than catching it during the design phase"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 41). This is not hypothetical: an empirical study of Copilot-generated code merged
into real GitHub projects found "their usage presents security challenges, often
resulting in insecure code merging into the code base"
([Security Weaknesses of Copilot-Generated Code](https://arxiv.org/abs/2310.02059)),
spanning many distinct weakness categories. Faster generation without a matching
security posture is faster generation of vulnerabilities.

## Layered guardrails, not a single check

No single check catches everything, so the security posture has to be layered. OpenAI
is direct about this: "think of guardrails as a layered defense mechanism. While a
single one is unlikely to provide sufficient protection, using multiple, specialized
guardrails together creates more resilient agents"
([A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 25). The layers combine deterministic and model-based checks — "simple deterministic
measures (blocklists, input length limits, regex filters) to prevent known threats like
prohibited terms or SQL injections" (p. 27) alongside classifiers that catch what rules
cannot. And guardrails are only part of the picture: they "should be coupled with
robust authentication and authorization protocols, strict access controls, and standard
software security measures" (p. 24). The generated code lands inside the same
defense-in-depth every other change is subject to; being AI-authored does not exempt it.

## Dependency and injection review

Two attack surfaces deserve targeted attention on agent output. The first is
dependencies: an agent can hallucinate a package that does not exist, or reach for one
that does but should not be trusted, so the paper flags "extra attention to hallucinated
dependencies" as a specific review concern for AI-generated code (p. 44). Every
dependency the agent introduces is a supply-chain decision that needs checking, not an
implementation detail. The second is injection — the classic classes (SQL injection and
similar) that agents reproduce as readily as any other pattern they have seen, which is
why deterministic filters for them sit in the guardrail stack. Agent-authored code is
not more trustworthy on either front than code pulled from an unknown contributor.

## Provenance and a hard human gate

Two practices close the posture.

- **Provenance of what the agent pulled in.** Know where the generated code and its
  dependencies came from — which package, which version, which source the agent drew a
  pattern from. Provenance is what lets you reason about trust and audit a decision after
  the fact rather than accepting an opaque diff.
- **Human-gate the security-sensitive diffs, always.** OpenAI's tool-risk framing rates
  each action "based on factors like read-only vs. write access, reversibility, required
  account permissions, and financial impact" and uses that rating to trigger "escalating
  to a human if needed" before high-risk actions (p. 26). Applied to code review, changes
  touching authentication, authorization, secrets, payments, or anything irreversible do
  not merge on an agent's say-so or a passing test — they route to a human. Automated
  layers raise the floor; the security-sensitive ceiling stays human. The Claude Code
  sandboxing and permission mechanics that enforce these gates in practice are covered
  elsewhere.

# Related

- [reviewing AI-generated code](/oks/agentic-sdlc-best-practices/verification-and-review/reviewing-ai-generated-code.md)
- [human-in-the-loop checkpoints](/oks/agentic-sdlc-best-practices/implementation/human-in-the-loop-checkpoints.md)
- [sandboxing and review](/oks/claude-best-practices/safety/sandboxing-and-review.md)
- [guardrails and permissions](/oks/ai-agent-repo-structure/practices/guardrails-and-permissions.md)

# Sources

- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://arxiv.org/abs/2310.02059
