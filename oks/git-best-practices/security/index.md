---
type: OKF Concept Index
title: Security
description: Keeping secrets out of history and authenticating trust — secret management, .gitignore hygiene, signed tags, and credential storage.
resource: https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
tags:
  - git
  - security
timestamp: 2026-07-07T00:00:00Z
---

# Security

Version control touches security in two ways: keeping sensitive data *out* of the
repository, and proving that commits, tags, and network access come from who they
claim to. These concepts cover both — preventing and remediating leaked secrets,
ignoring files that should never be tracked, cryptographically signing releases,
and storing the credentials Git uses to talk to remotes.

## Concepts

- [secret management](/oks/git-best-practices/security/secret-management.md) — detecting, blocking, and remediating credentials committed to a repository.
- [gitignore hygiene](/oks/git-best-practices/security/gitignore-hygiene.md) — keeping generated, local, and sensitive files untracked.
- [signed tags](/oks/git-best-practices/security/signed-tags.md) — cryptographically signing release tags and verifying them.
- [credential storage](/oks/git-best-practices/security/credential-storage.md) — how Git stores and retrieves the credentials it uses for remotes.
