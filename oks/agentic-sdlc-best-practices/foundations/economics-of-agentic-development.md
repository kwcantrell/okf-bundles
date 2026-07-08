---
type: Agentic SDLC Practice
title: Economics Of Agentic Development
description: Vibe coding is low CapEx / high OpEx with hidden debt; agentic engineering front-loads investment for lower ongoing cost — and context engineering is the financial lever between them.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - foundations
timestamp: 2026-07-07T00:00:00Z
---

# Economics Of Agentic Development

The choice of where to sit on the spectrum is, at bottom, a cost-of-ownership
decision. As of the May 2026 paper *The New SDLC With Vibe Coding*, the framing is
Total Cost of Ownership split between "Capital Expenditure (CapEx) — the upfront
investment to build something — and Operational Expenditure (OpEx) — the ongoing
cost to run, fix, and maintain." The two workflows land on opposite sides of that
ledger.

## Vibe coding: low CapEx, high OpEx

Vibe coding is cheap to start and expensive to keep. Its low upfront cost hides a
"maintenance tax": the paper notes that code written through ad-hoc prompting
"often lacks structural consistency," so "when a bug arises six months later,
human engineers must spend days reverse-engineering unstructured, AI-generated
'spaghetti' code." The bill arrives later, as OpEx, and compounds.

## Agentic engineering: the reverse

Agentic engineering flips the ledger, paying upfront to save later. Its CapEx,
per the paper, "includes designing API schemas, building deterministic test
suites, and, most importantly, structuring the agent's context." That deliberate
front-loading — schemas, tests, context — is what buys the lower ongoing cost of
maintenance and change.

## Context engineering as a financial lever

The most important line item is context. Because LLMs charge per token, context
is not only a technical concern but a financial one: the paper states that "in the
token economy, context engineering is not just a technical skill — it is a
financial strategy," because "passing an entire 100,000-token repository into
every prompt is financially unviable at scale." Curating what the model sees
directly controls the token bill on every call, which is why context engineering
is the lever that moves OpEx. The context-engineering area develops that discipline
in full.

# Related

- [when vibe coding is appropriate](/oks/agentic-sdlc-best-practices/foundations/when-vibe-coding-is-appropriate.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
