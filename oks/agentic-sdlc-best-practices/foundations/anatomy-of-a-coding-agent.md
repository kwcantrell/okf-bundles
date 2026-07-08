---
type: Agentic SDLC Practice
title: Anatomy Of A Coding Agent
description: A refresher on what an agent is — a model reasoning over context, acting through tools, in a perceive-plan-act-observe loop — as the groundwork for engineering the harness around it.
resource: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
tags:
  - agentic-sdlc
  - foundations
timestamp: 2026-07-07T00:00:00Z
---

# Anatomy Of A Coding Agent

Before engineering the scaffolding around an agent, it helps to be precise about
what an agent is. As of the May 2026 paper *The New SDLC With Vibe Coding*, "an AI
agent is a software system that perceives a goal, plans steps to reach it, takes
actions through tools, observes the results, and iterates until the goal is met or
it hits a stopping condition." The distinction from a chatbot is the iteration: an
agent keeps going toward the goal instead of waiting for the next prompt.

## The parts

The paper decomposes every agent, "however simple or sophisticated," into a small
set of parts. The **model** is the reasoning engine: it "reads the current
context, decides what should happen next, and produces the next thought, the next
tool call, or the next message." **Tools** are how it acts on the world beyond
text. **Context** is what it reads to decide — and, per Anthropic, the basic
building block underneath all of this is simply "an LLM enhanced with augmentations
such as retrieval, tools, and memory." An agent is that augmented model, driven in
a loop.

## The loop

What turns those parts into an agent is the loop that connects them. The paper
calls it "the beating heart of every agent": the parts "work together in a
continuous loop: get the mission, scan the scene, think it through, take action,
observe and iterate." Perceive, plan, act, observe — then around again, each pass
folding the last result back into context.

## Why this is the groundwork

The model is only one component of that picture, and in practice a small one. The
loop, the tools, the context policies, and the constraints around the model are
what determine whether an agent actually finishes a task well — and those are all
engineered, not given by the model. That engineered scaffolding around the model
is the harness, and building it well is the subject of the agent-harness area.

# Related

- [from syntax to intent](/oks/agentic-sdlc-best-practices/foundations/from-syntax-to-intent.md)

# Sources

- https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
- https://www.anthropic.com/engineering/building-effective-agents
