---
type: Branching Practice
title: Resolving Merge Conflicts
description: How to read Git's conflict markers, understand the three staged versions of a conflicted file, and finish or undo a conflicted merge.
resource: https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging
tags:
  - git
  - branching
  - merge
  - conflicts
timestamp: 2026-07-07T00:00:00Z
---

# Resolving Merge Conflicts

A conflict happens when two branches change the same region of a file in
incompatible ways and Git cannot decide which version to keep. Conflicts are
normal, not a sign that something went wrong — they are Git asking you to make a
judgment call it cannot make for you.

## Recognizing a conflict

When a merge conflict occurs, Git marks the conflicted files with a **`UU`
(unmerged)** status, visible in `git status`, and inserts **conflict markers**
into each affected file. The markers use three delimiters to separate "ours"
from "theirs":

```
<<<<<<< HEAD
your version of the lines
=======
the other branch's version of the lines
>>>>>>> other-branch
```

You resolve the conflict by editing the file so it contains the correct final
content and removing all three marker lines, then staging the file with
`git add` (which is how you tell Git the conflict is resolved — see the
[staging area](/oks/git-best-practices/fundamentals/staging-area.md)).

## The three versions Git keeps

During a conflicted merge, Git stores **three** versions of each conflicted file
in the index as numbered stages:

- **Stage 1** — the common ancestor (the base).
- **Stage 2** — your version ("ours").
- **Stage 3** — the version from the branch being merged in ("theirs").

Knowing this explains the more advanced tools: `git merge-file` can manually
merge three file versions (ours, base, theirs) to produce a resolved result, and
diff tools use the base to show *how* each side diverged rather than just *that*
they differ.

## Shortcuts and escape hatches

- **Whitespace-only conflicts.** The merge strategy options `-Xignore-all-space`
  and `-Xignore-space-change` let Git automatically resolve conflicts caused only
  by whitespace differences — handy after a reformatting change.
- **Undoing a completed merge.** If a merge has already been committed and you
  need to reverse it, `git revert -m 1 HEAD` creates a new commit that reverses
  the merge rather than rewriting history — the safe choice on shared branches.

Both [merge and rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)
surface conflicts and resolve them with the same markers and staging step; the
difference is only in how many times you may encounter them.

# Related

- [merge vs. rebase](/oks/git-best-practices/branching/merge-vs-rebase.md)
- [staging area](/oks/git-best-practices/fundamentals/staging-area.md)

# Sources

- https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging
