---
type: Security Practice
title: Credential Storage
description: How Git stores and retrieves the credentials it uses for remotes — built-in helpers, OS-native secure stores, and personal access tokens.
resource: https://git-scm.com/docs/gitcredentials
tags:
  - git
  - github
  - security
  - credentials
timestamp: 2026-07-07T00:00:00Z
---

# Credential Storage

Every time Git talks to a remote over HTTPS it needs a credential. How that
credential is stored ranges from insecure to secure, and the difference matters.

## The credential interface and helpers

`git credential` exposes Git's internal credential storage/retrieval interface
via four actions — `fill`, `approve`, `reject`, and `capability`. The **`fill`**
action returns a matching credential by first consulting configured helpers and,
if a value is still missing, prompting the user; **`approve`** sends a
successfully used credential to helpers to be stored, and **`reject`** tells
helpers to erase a credential that turned out to be invalid.

Git ships two **built-in** credential helpers:

- **`cache`** holds credentials in memory for a short period.
- **`store`** saves credentials **indefinitely in a plaintext file on disk** —
  convenient but insecure, and best avoided for real secrets.

## Secure, OS-native storage

Prefer platform-specific secure helpers that store credentials in the operating
system's native secure store rather than plaintext:
**`git-credential-osxkeychain`** (macOS), **`git-credential-wincred`** (Windows),
and **`git-credential-libsecret`** (Linux). **Git Credential Manager (GCM)** is a
cross-platform helper that ships automatically with Git for Windows and can be
installed on macOS and Linux; it uses the OS-native secure store and supports
browser-based OAuth authentication with GitHub.

Multiple helpers can be configured together via repeated `credential.helper`
entries, and Git tries each in sequence until it obtains both a username and a
password.

## Personal access tokens

Personal access tokens function as a **password replacement** for Git operations
over HTTPS: when prompted for a password, enter the token instead, and treat it
like a password. GitHub recommends adding an **expiration** to tokens, and
**fine-grained** tokens can be scoped to a single user or organization and to
specific repositories — unlike classic tokens, which grant broad access across
all accessible repositories. Scoping and expiry limit the blast radius if a token
leaks, which ties back to
[secret management](/oks/git-best-practices/security/secret-management.md).

# Related

- [secret management](/oks/git-best-practices/security/secret-management.md)
- [fetch, pull, push](/oks/git-best-practices/remote/fetch-pull-push.md)
- [signed tags](/oks/git-best-practices/security/signed-tags.md)

# Sources

- https://git-scm.com/docs/git-credential
- https://git-scm.com/docs/gitcredentials
- https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
