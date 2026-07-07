---
type: Security Practice
title: Signed Tags
description: Cryptographically sign release tags so consumers can verify their origin, configure a signing key, and enforce signature verification on merges.
resource: https://git-scm.com/docs/git-tag
tags:
  - git
  - security
  - tags
  - signing
timestamp: 2026-07-07T00:00:00Z
---

# Signed Tags

A [tag](/oks/git-best-practices/remote/tags-and-releases.md) marks a release, and
signing it adds cryptographic proof of who created that release — essential when
downstream consumers pin to a tag and need to trust it.

## Creating a signed tag

- Pass **`-s` / `--sign`** to `git tag` to create a tag cryptographically signed
  with your configured signing key. The signing backend is determined by the
  `gpg.format` configuration variable, which defaults to OpenPGP. For example:
  `git tag -s v1.5 -m 'my signed 1.5 tag'`.
- Pass **`-u <key-id>`** (`--local-user`) to sign with a specific key instead of
  the default.
- Using `-a`, `-s`, or `-u` causes `git tag` to create a **full tag object**
  (rather than a lightweight tag), which requires a tag message and records a
  tagger name, email, and date.

Before you can sign, configure a signing key with
`git config --global user.signingkey <key-id>` (generated, for example, with
`gpg --gen-key`).

## Signing by default

Set the boolean configuration variable **`tag.gpgSign`** to `true` to make Git
sign all tags with GPG by default, unless overridden with `--no-sign`.

## Verifying

- **`git tag -v <tagname>`** (`--verify`) verifies the cryptographic signature of
  the named tag(s), provided the signer's public key is in your local keyring.
  You can also inspect a signature with `git show v1.5`.
- **`git merge --verify-signatures <branch>`** verifies every commit's signature
  being merged in and aborts the merge if any commit is unsigned or has an invalid
  signature.

Signed tags are the tag-level counterpart to
[signing commits](/oks/git-best-practices/commits/signing-commits.md): mind the
case difference — commits use capital `-S`, tags use lowercase `-s`.

# Related

- [signing commits](/oks/git-best-practices/commits/signing-commits.md)
- [tags and releases](/oks/git-best-practices/remote/tags-and-releases.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)
- [refs and objects](/oks/git-best-practices/fundamentals/refs-and-objects.md)

# Sources

- https://git-scm.com/docs/git-tag
- https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
