---
type: Security Practice
title: Secret Management
description: Detect and block credentials before they land in history with secret scanning and push protection, and remediate leaks by rotating the credential first.
resource: https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
tags:
  - git
  - github
  - security
  - secrets
timestamp: 2026-07-07T00:00:00Z
---

# Secret Management

A committed secret is a serious problem because Git history is permanent by
default — the credential is retrievable from any past commit, not just the current
files. The strategy has three layers: detect, block, and remediate.

## Detect: secret scanning

GitHub **secret scanning** automatically detects credential leaks — API keys,
passwords, tokens — across a repository's **entire Git history and all branches**,
so they can be secured before exploitation. It also inspects issue descriptions,
comments and titles, pull request content, Discussions, wikis, and secret gists,
not just committed files. GitHub partners with service providers to **validate**
detected secrets and reports valid partner secrets directly to the issuing
provider for revocation.

Secret scanning is automatically enabled and free for **public** repositories;
private and internal repositories require GitHub Secret Protection (Team or
Enterprise Cloud).

## Block: push protection

**Push protection** blocks a push *before it completes* when it detects a
potential secret, covering command-line pushes, the web UI, file uploads, and
REST API requests. It is enabled by default for individual user accounts on
GitHub.com to prevent pushing secrets to public repositories; repository- and
organization-level push protection must be turned on by an administrator. Anyone
with write access can **bypass** it by supplying a reason (such as "used in
tests," "false positive," or "I'll fix it later"), each of which affects how the
resulting alert is recorded.

## Remediate: rotate first

If a credential is committed, GitHub's guidance is to **first revoke or rotate the
credential** — a revoked secret cannot be used for access even if it remains in
history, making this the step that actually closes the exposure. Only then
rewrite history: GitHub recommends the **`git filter-repo`** tool (with its
`--sensitive-data-removal` flag) rather than `git filter-branch`. Even after
rewriting and force-pushing, the data can persist in existing clones, forks, and
GitHub's cached commit views, so you must coordinate with collaborators directly.

Prevention beats cure: keep secrets out of the tree in the first place with
[.gitignore hygiene](/oks/git-best-practices/security/gitignore-hygiene.md) and a
[pre-commit](/oks/git-best-practices/automation/pre-commit.md) scanner.

# Related

- [gitignore hygiene](/oks/git-best-practices/security/gitignore-hygiene.md)
- [credential storage](/oks/git-best-practices/security/credential-storage.md)
- [pre-commit](/oks/git-best-practices/automation/pre-commit.md)
- [branch protection](/oks/git-best-practices/branching/branch-protection.md)

# Sources

- https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
- https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
