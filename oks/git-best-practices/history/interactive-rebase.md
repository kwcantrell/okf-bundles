---
type: History Practice
title: Interactive Rebase
description: Use git rebase -i to reorder, squash, reword, edit, and drop commits — cleaning up local history before you share it.
resource: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
tags:
  - git
  - history
  - rebase
timestamp: 2026-07-07T00:00:00Z
---

# Interactive Rebase

Interactive rebase is the tool for polishing a series of commits before you share
them. Invoke it as `git rebase -i <after-this-commit>`; Git opens an editor
listing the commits about to be replayed, and you edit that list to control what
happens to each one.

## The todo list

Commits appear in the editor in the **reverse order from `git log`** — the oldest
commit to be replayed is at the top. Each line starts with a command:

- **pick** — use the commit as-is.
- **reword** — use the commit, but edit its message.
- **edit** — use the commit, but stop so you can amend it.
- **squash** — fold into the previous commit, combining both messages.
- **fixup** — fold into the previous commit, discarding this one's message.
- **drop** — remove the commit entirely (also achieved by deleting its line).
- **exec** — run a shell command.
- plus `label`, `reset`, and `merge` for more advanced reshaping.

**Reordering the lines reorders the resulting commits**, and deleting a line
drops that commit.

## Editing and splitting

Marking a commit `edit` causes Git to stop right after applying it, letting you
run `git commit --amend` to change it, then `git rebase --continue` to resume.
The same stop point lets you **split** one commit into several: reset it, then
stage and commit the pieces separately.

## The safety caveat

Because interactive rebase rewrites commits, it **changes their SHA-1 hashes**
(and those of every descendant commit). Like all
[rebasing](/oks/git-best-practices/history/rebasing.md), it must not be used on
commits already pushed to a shared repository. Its natural home is cleaning up
[atomic commits](/oks/git-best-practices/commits/atomic-commits.md) and squashing
work-in-progress before opening a
[pull request](/oks/git-best-practices/collaboration/pull-requests.md).

# Related

- [rebasing](/oks/git-best-practices/history/rebasing.md)
- [atomic commits](/oks/git-best-practices/commits/atomic-commits.md)
- [commit-message style](/oks/git-best-practices/commits/commit-message-style.md)
- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
- https://git-scm.com/docs/git-rebase
