---
type: Agentic SDLC Practice
title: Human-In-The-Loop Checkpoints
description: Deciding which gates stay human as agent autonomy rises — spec approval, security-sensitive code, and irreversible or outward-facing actions — plus the autonomy dials and escalation triggers that route the agent back to a person before it does damage.
resource: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
tags:
  - agentic-sdlc
  - implementation
timestamp: 2026-07-07T00:00:00Z
---

# Human-In-The-Loop Checkpoints

The other implementation concepts in this area — tests as guardrails, small
verified increments — are about how the agent works. This one cuts across all of
them: it's about which decisions never fully leave the human, no matter how
capable the agent gets. Human review isn't a limitation to be automated away; OpenAI
frames it as "a critical safeguard enabling you to improve an agent's real-world
performance without compromising user experience... especially important early in
deployment" ([A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf),
p. 31). The design task is to place the human gates deliberately rather than
letting them erode as trust grows.

## Which gates stay human

Three kinds of decision warrant a human in the loop even for an otherwise
autonomous agent:

- **Spec approval.** The spec is where a wrong direction is cheapest to catch,
  because the agent will implement it literally. Approving what gets built — before
  the agent builds it — is the highest-leverage human gate.
- **Security-sensitive code.** AI-generated code "requires the same or greater
  scrutiny than human-written code, with extra attention to hallucinated
  dependencies, inadequate error handling, and subtle correctness gaps that look
  right at a glance" ([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
  p. 44). Anything touching auth, secrets, or data exposure stays human-reviewed.
- **Irreversible or outward-facing actions.** OpenAI's rule of thumb is that
  "actions that are sensitive, irreversible, or have high stakes should trigger
  human oversight until confidence in the agent's reliability grows" (p. 31).
  Deployments, destructive migrations, payments, and anything visible to real users
  fall here.

The common thread is reversibility and blast radius: the harder it is to undo and
the further it reaches, the more it belongs behind a human gate.

## Autonomy dials and escalation triggers

Autonomy is a dial, not a switch, and it can be turned per action rather than per
agent. OpenAI's tool-risk approach makes this concrete: assign each tool a risk
rating "based on factors like read-only vs. write access, reversibility, required
account permissions, and financial impact," then use those ratings to trigger
"pausing for guardrail checks before executing high-risk functions or escalating to
a human if needed" (p. 26). A read-only lookup can run freely; a high-risk write
pauses for approval.

Two triggers should hand control back to a person. The first is **exceeding a
failure threshold**: "Set limits on agent retries or actions. If the agent exceeds
these limits... escalate to human intervention" (p. 31) — an agent thrashing on the
same problem is a signal to stop, not to retry harder. The second is a **high-risk
action** matching the gates above. When either fires, the agent should "gracefully
transfer control" — for a coding agent, "this means handing control back to the
user" (p. 31) — rather than pressing on.

These gates connect to the roles in
[conductor and orchestrator roles](/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md):
the human sets direction and owns the gates while the agent does the implementation
between them. The enforcement mechanism in a Claude Code session is
[permission modes](/oks/claude-best-practices/safety/permission-modes.md), which
decide which actions run automatically and which pause for approval — the concrete
dial for the autonomy this concept describes.

Two of these gates deepen in later areas of this bundle — adversarial multi-agent
review as a verification gate, and human approval as a release gate in CI/CD — and
are covered there rather than here.

# Related

- [conductor and orchestrator roles](/oks/agentic-sdlc-best-practices/foundations/conductor-and-orchestrator-roles.md)
- [permission modes](/oks/claude-best-practices/safety/permission-modes.md)
- [adversarial multi-agent review](/oks/agentic-sdlc-best-practices/verification-and-review/adversarial-multi-agent-review.md)
- [agents in CI/CD](/oks/agentic-sdlc-best-practices/operations-and-evolution/agents-in-ci-cd.md)

# Sources

- https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
