---
type: Agent Knowledge Practice
title: OKF Bundles in Repos
description: Shipping Open Knowledge Format bundles as versioned Markdown that lives in git next to the code it describes.
resource: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
tags:
  - ai-agents
  - okf
  - knowledge
  - version-control
timestamp: 2026-07-07T00:00:00Z
---

# OKF Bundles in Repos

Some knowledge is too large and too durable to sit in a startup context file, yet
too valuable to leave undocumented. The Open Knowledge Format (OKF) is a way to
curate that knowledge as plain files an agent can read on demand.

## Just files, just Markdown

OKF v0.1 represents a bundle of documents as "just files" that can be shipped as a
tarball or hosted in any git repo — with no complex compression scheme, no new
runtime, and no required SDK. Because a bundle is just Markdown, it is readable in
any text editor, renders directly on GitHub, and is indexable by ordinary search
tools without special tooling. The only required frontmatter field is `type`; the
reserved-but-optional fields are `title`, `description`, `resource`, `tags`, and
`timestamp`, keeping the format minimally opinionated for producers.

## Co-located with the code

Because OKF bundles are version controlled, they can live in git alongside the
code they describe, keeping curated knowledge and code changes co-located and
reviewable together. That is the key structural benefit for an agent repo: the
knowledge an agent needs ships in the same pull request as the change it explains,
so the two never drift.

Treating a knowledge bundle as a first-class versioned artifact means the same
[version-control practices](/oks/git-best-practices/index.md) you apply to code —
small reviewable changes, meaningful commit messages, protected branches — apply
to the knowledge too. A bundle committed this way is reviewed like code and
evolves with it.

## Tooling around the format

Google shipped reference implementations alongside the OKF spec: an enrichment
agent that walks BigQuery datasets and drafts OKF documents, a static HTML
visualizer that turns any OKF bundle into an interactive graph view, and three
sample bundles (GA4 e-commerce, Stack Overflow, and Bitcoin public datasets).
Google Cloud's Knowledge Catalog was also updated to ingest OKF bundles and serve
that curated knowledge to agents — evidence that the format is meant to be
consumed programmatically, not just read by hand.

# Related

- [docs for agents](/oks/ai-agent-repo-structure/knowledge/docs-for-agents.md)
- [machine-readable metadata](/oks/ai-agent-repo-structure/knowledge/machine-readable-metadata.md)
- [directory layout](/oks/ai-agent-repo-structure/conventions/directory-layout.md)
- [git best practices](/oks/git-best-practices/index.md)

# Sources

- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
