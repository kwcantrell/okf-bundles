---
type: Agentic SDLC Practice
title: Reviewing AI-Generated Code
description: When the author is an agent, code review changes shape — the volume goes up, the errors get more plausible, and reviewer attention becomes the scarce resource. AI can triage the first pass, but the judgment calls still belong to humans.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - verification-and-review
timestamp: 2026-07-07T00:00:00Z
---

# Reviewing AI-Generated Code

Code review was designed around a human author who understood every line they wrote
and produced changes at human speed. When the author is an agent, both assumptions
break: the change may be larger than any human would have written in the time, and
no human necessarily understood it line by line before it arrived. Review does not
become optional — the paper is explicit that "AI-generated code requires the same or
greater scrutiny than human-written code, with extra attention to hallucinated
dependencies, inadequate error handling, and subtle correctness gaps that look right
at a glance"
([The New SDLC With Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding),
p. 44). What changes is *how* that scrutiny has to be organized.

## What changes when the author is an agent

Three things shift at once.

- **Volume.** Agents generate more code, faster, than the humans reviewing it can
  read at the same pace. Review capacity, not authoring capacity, becomes the
  bottleneck — and a bottleneck that is tempting to widen by reviewing less
  carefully.
- **Plausible-but-wrong output.** The characteristic agent error is not a syntax
  mistake a compiler catches but a conceptual one, "harder to detect precisely
  because the code 'looks right' and may even pass basic tests"
  ([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 34).
  Fluency is not correctness. A change that reads smoothly and passes CI can still be
  wrong in a way that only shows up under a condition the tests never exercised.
- **Reviewer-attention economics.** Put those together and the scarce resource is
  human attention. A reviewer facing a steady stream of large, plausible-looking
  diffs cannot sustain deep scrutiny on all of them, and plausible-but-wrong code is
  exactly what slips through a tired skim. This is not a security worry alone — an
  empirical study of Copilot-generated code merged into real GitHub projects found
  "their usage presents security challenges, often resulting in insecure code merging
  into the code base"
  ([Security Weaknesses of Copilot-Generated Code](https://arxiv.org/abs/2310.02059)),
  a concrete measurement of what gets through when review does not keep up.

## AI-assisted first-pass triage

The way to spend scarce attention well is to not spend it on what a machine can
screen. The paper describes "AI serving as a first-pass reviewer that can identify
potential bugs, style violations, security vulnerabilities, and performance issues
before a human reviewer sees the code"
([paper](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding), p. 23) —
without replacing human review. First-pass triage clears the mechanical findings and
surfaces the suspicious spots, so the human arrives at the diff already pointed at
what deserves thought rather than reading every line cold. The point is to *route*
attention, not to remove it.

## What still goes to humans

Triage narrows the field; it does not decide. The judgment calls the paper reserves
for the human author of the architecture — trade-offs that "depend on business
context, organisational constraints, and long-term strategic considerations that AI
cannot fully grasp" (p. 21) — are the same calls a reviewer has to make about whether
a change is *right for this system*, not merely internally consistent. Correctness
under the cases the tests miss, fit with the intended design, and anything
security-sensitive or irreversible stay with a human. Because the same agent that
wrote the code is not a trustworthy grader of it, the review that matters is an
independent one — ideally by a fresh reviewer, and for the highest-stakes changes, by
more than one lens. Those are the subjects of the concepts that follow.

# Related

- [trust calibration and the 80% problem](/oks/agentic-sdlc-best-practices/foundations/trust-calibration-and-the-80-percent-problem.md)
- [independent review](/oks/claude-best-practices/verification/independent-review.md)
- [adversarial multi-agent review](/oks/agentic-sdlc-best-practices/verification-and-review/adversarial-multi-agent-review.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://arxiv.org/abs/2310.02059
