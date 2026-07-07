---
type: Scale Practice
title: Monorepo vs. Polyrepo
description: One shared repository or many separate ones — GitHub's guidance, submodules for composing repos, and the supported path for splitting a folder out.
resource: https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
tags:
  - git
  - github
  - scale
  - monorepo
timestamp: 2026-07-07T00:00:00Z
---

# Monorepo vs. Polyrepo

A fundamental structural choice: keep many projects in one repository (a
monorepo) or split them across many (a polyrepo). Neither is universally right,
and Git provides mechanisms for composing and reshaping either way.

## GitHub's collaboration guidance

GitHub's own guidance favors having **regular collaborators work from a single
shared repository**, creating [pull
requests](/oks/git-best-practices/collaboration/pull-requests.md) between
branches, and reserves **forking** (separate repository copies) for contributors
*unaffiliated* with the project, such as open-source contributors — the
[forking workflow](/oks/git-best-practices/workflows/forking-workflow.md). A
shared repo keeps collaboration and history in one place.

## Composing repos with submodules

A **Git submodule** keeps one Git repository as a subdirectory of another,
treating the two as independent projects with separate commit histories while
still consuming one from within the other — a way to compose multiple repositories
as an alternative to a monorepo. Adding one with `git submodule add <url>` creates
a `.gitmodules` file mapping the subdirectory to the external repo's URL, and
cloning a superproject requires `git clone --recurse-submodules` (or a separate
`git submodule init` and `git submodule update`) to populate submodule content.

Submodules carry documented friction: switching branches can leave submodule
directories showing as untracked, and pushing changes requires **coordinating
commits across both** the submodule and the parent (superproject) repository.
That coordination cost is the central trade-off against a monorepo's single,
atomic history.

## Splitting a folder into its own repo

GitHub documents a supported path from a monorepo layout toward a polyrepo one:
turn a single folder into its own new repository using
`git filter-repo --path FOLDER-NAME/` or
`git filter-repo --subdirectory-filter FOLDER-NAME`. Note the new repository will
**not retain** the original's branches and tags.

## Trade-offs

A monorepo gives atomic cross-project changes and one place to review and
[test in CI](/oks/git-best-practices/automation/ci-integration.md), at the cost of
a large working tree — often managed with
[sparse checkout](/oks/git-best-practices/scale/sparse-checkout.md). A polyrepo
gives independent versioning and access control, at the cost of coordinating
changes that span repositories.

# Related

- [large files and Git LFS](/oks/git-best-practices/scale/large-files-lfs.md)
- [sparse checkout](/oks/git-best-practices/scale/sparse-checkout.md)
- [forking workflow](/oks/git-best-practices/workflows/forking-workflow.md)
- [ci integration](/oks/git-best-practices/automation/ci-integration.md)

# Sources

- https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
- https://git-scm.com/book/en/v2/Git-Tools-Submodules
- https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository
