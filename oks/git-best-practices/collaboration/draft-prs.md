---
type: Collaboration Practice
title: Draft Pull Requests
description: Work-in-progress pull requests that cannot be merged and don't auto-request code-owner review, useful for signaling that work is not yet ready.
resource: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request
tags:
  - git
  - github
  - collaboration
  - pull-requests
timestamp: 2026-07-07T00:00:00Z
---

# Draft Pull Requests

A draft pull request is a
[pull request](/oks/git-best-practices/collaboration/pull-requests.md) explicitly
marked as *not ready to merge*. When you create a pull request, you can choose to
make it a draft — a clear signal to collaborators that the work is still in
progress, while still letting them see it and comment.

## What "draft" changes

- **It cannot be merged.** No one can merge a pull request while it is a draft;
  it must first be marked as ready for review.
- **Code owners are not auto-requested.** Draft pull requests do not automatically
  request review from [code owners](/oks/git-best-practices/collaboration/codeowners.md),
  which avoids pulling reviewers in before the work is worth their time.

## Moving between stages

- **Ready for review.** Mark a draft as ready by clicking the "Ready for review"
  button in the merge box, or via the GitHub CLI command `gh pr ready`. Doing so
  will request reviews from any code owners defined for the changed code —
  effectively the moment [code review](/oks/git-best-practices/collaboration/code-review.md)
  begins in earnest.
- **Convert back to draft.** A pull request can be converted to a draft at any
  time — for example if it was opened by mistake instead of as a draft, or if
  feedback shows that further changes are needed before review should continue.
  While it is a draft, it again cannot be merged until marked ready.

## When to use drafts

Open a draft when you want early feedback on direction, when you want CI to run
against work in progress, or simply to make ongoing work visible without
signaling "please review and merge this." It is the polite way to share
unfinished work: collaborators can look, but the tooling makes clear it isn't
done.

# Related

- [pull requests](/oks/git-best-practices/collaboration/pull-requests.md)
- [code review](/oks/git-best-practices/collaboration/code-review.md)
- [CODEOWNERS](/oks/git-best-practices/collaboration/codeowners.md)

# Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request
