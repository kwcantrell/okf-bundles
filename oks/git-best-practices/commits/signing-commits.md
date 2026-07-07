---
type: Commit Practice
title: Signing Commits
description: Cryptographically sign commits and tags with GPG, SSH, or S/MIME so their authorship can be verified, and configure signing by default.
resource: https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification
tags:
  - git
  - github
  - commits
  - security
  - signing
timestamp: 2026-07-07T00:00:00Z
---

# Signing Commits

By default, the author name and email on a commit are just text that anyone can
set to anything. Signing adds cryptographic proof: Git supports signing commits
and tags with **GPG, SSH, or S/MIME** signatures that can be verified, so
consumers can trust that a commit really came from who it claims.

## How verification appears

On GitHub, a signed commit is marked **"Verified"** when the signature was
successfully verified, and **"Unverified"** when the commit is signed but the
signature could not be verified. Once a commit's signature is verified upon push,
a verification record is stored alongside it — and that record **persists even if
the signing key is later rotated or revoked**, or the contributor leaves the
organization. Note version requirements: SSH signature verification requires
Git 2.34 or later, and S/MIME requires Git 2.19 or later.

## Signing commits and tags

- **Sign one commit:** add the `-S` (capital S) flag, e.g.
  `git commit -S -m "YOUR_COMMIT_MESSAGE"`.
- **Sign every commit by default:** set `git config commit.gpgsign true` for a
  single repository (Git 2.0.0+), or `git config --global commit.gpgsign true`
  for all repositories.
- **Sign a tag:** tags use the **lowercase** `-s` flag, e.g.
  `git tag -s <tag-name> -m '<message>'`. (Mind the case: commits use `-S`, tags
  use `-s`.) A signed tag can be checked with `git tag -v <tag-name>`.

## Inspecting and enforcing signatures

- `git log --show-signature` displays signature information in the commit log.
- `git merge --verify-signatures <branch>` will refuse to merge unless all
  commits on the branch have trusted GPG signatures.
- On the server side, requiring signed commits via
  [branch protection](/oks/git-best-practices/branching/branch-protection.md)
  means contributors and bots can only push signed, verified commits to the
  protected branch — turning signing from an individual habit into an enforced
  policy.

## Trade-offs

Signing raises the bar for authorship integrity, which matters most on
high-trust branches and for released tags. The cost is setup: contributors must
generate and register a key and configure their client. Many teams make signing
the default locally and enforce it only on protected branches, balancing
assurance against onboarding friction.

# Related

- [commit-message style](/oks/git-best-practices/commits/commit-message-style.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)

# Sources

- https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification
- https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits
- https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
