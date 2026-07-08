---
type: Agentic SDLC Practice
title: Trust Calibration And The 80 Percent Problem
description: Verification is the new bottleneck — agents produce roughly 80% of a feature fast, but the last 20% is the hard part, and review depth has to be calibrated to the stakes.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - foundations
timestamp: 2026-07-07T00:00:00Z
---

# Trust Calibration And The 80 Percent Problem

Once the machine writes the syntax, the bottleneck moves to verifying it. As of
the May 2026 paper *The New SDLC With Vibe Coding*, this is captured as the "80%
problem": AI agents can rapidly generate roughly 80% of the code for a feature,
"but the remaining 20% — the edge cases, error handling, integration points, and
subtle correctness requirements — demands deep contextual knowledge that current
models often lack." An impressive demo is not a shippable feature; the last mile
is where the real difficulty concentrates.

## Why the failures are harder to catch

The nature of AI errors has shifted. They are no longer obvious syntax mistakes
that a compiler flags — they are conceptual failures, and the paper notes these
"are harder to detect precisely because the code 'looks right' and may even pass
basic tests." Fluent, plausible, test-passing output that is subtly wrong is more
dangerous than an obvious break, because nothing prompts you to look closer.

## Verification as the real cost

This is why speed gains are not automatic. The paper cites a METR study in which
experienced developers using AI assistants "actually took 19% longer on certain
tasks, largely because of the time spent verifying, debugging, and correcting AI
output." The generation was fast; the verification was not, and it dominated.

## Calibrating trust to stakes

The response is not to accept everything nor to distrust everything, but to
calibrate. The paper observes that the most effective developers "don't try to be
faster by accepting everything the AI produces. They try to be faster by focusing
their expertise where it matters most" — reserving human attention for ambiguous
requirements, architectural trade-offs, and correctness verification, and spending
review depth in proportion to the stakes of the code. Disposable code earns a
glance; code handling money or user data earns scrutiny. Turning that principle
into a concrete review practice is the work of the verification-and-review area.

# Related

- [when vibe coding is appropriate](/oks/agentic-sdlc-best-practices/foundations/when-vibe-coding-is-appropriate.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
