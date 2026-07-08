---
type: Agentic SDLC Practice
title: Vibe Coding And The Spectrum
description: Vibe coding and agentic engineering are not a binary but endpoints on a spectrum, defined by how much structure, verification, and human judgment surrounds AI output.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - foundations
timestamp: 2026-07-07T00:00:00Z
---

# Vibe Coding And The Spectrum

"Vibe coding" names an approach where a developer accepts AI output wholesale and
simply feeds errors back to the model rather than reading the code — the original
sense was to "fully give in to the vibes, embrace exponentials, and forget that
the code even exists." Karpathy coined the term and later refined the arc; that
lineage is traced in
[vibe coding to agentic engineering](/oks/autoresearch-best-practices/agentic-engineering/vibe-coding-to-agentic-engineering.md)
and is not restated here.

As of the May 2026 paper *The New SDLC With Vibe Coding*, the term had become
overloaded — applied to everything from casual prompting to disciplined
AI-assisted development — which led Karpathy to coin "agentic engineering" for the
more disciplined end of the spectrum.

## Not a binary — a spectrum

The paper's central framing is that vibe coding and agentic engineering are not
two camps but two ends of a continuum. "The key differentiator is not whether you
use AI. It's how much structure, verification, and human judgment surrounds the
AI's output." Move along the spectrum by adding structure around the model:
specifications that state intent, guardrails that constrain behavior, evals that
define correctness, and review that gates what ships.

## Verification is the defining axis

If one dimension separates the ends, the paper says it is verification. "The
single biggest differentiator between the two ends is how outputs get verified.
In vibe coding, verification is optional; the developer runs the code and checks
if it seems right." At the agentic-engineering end, verification is not optional
and not eyeballed — it is encoded in tests and evals so correctness can be
checked automatically and repeatably.

That framing turns "which end should I be at?" into a practical question about the
stakes of the work — the subject of when vibe coding is actually appropriate.

# Related

- [vibe coding to agentic engineering](/oks/autoresearch-best-practices/agentic-engineering/vibe-coding-to-agentic-engineering.md)
- [when vibe coding is appropriate](/oks/agentic-sdlc-best-practices/foundations/when-vibe-coding-is-appropriate.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
