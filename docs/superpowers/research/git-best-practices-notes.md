# Research Notes: git-best-practices bundle

Primary-source facts (fact + URL) per concept. Consumed by authoring Tasks 3-4.
Generated 2026-07-07 by 5 parallel Sonnet research agents.

## repository-model
- Git stores data as snapshots of the entire project at commit time, not as file-based changes or deltas. — https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- If a file has not changed between commits, Git stores only a link to the previously stored identical file rather than duplicating it, so Git is more like a stream of snapshots than a series of diffs. — https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- Files in a Git project can be in one of three main states: modified (changed but not committed), staged (marked to go into the next commit snapshot), and committed (safely stored in the local database). — https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- A Git project has three main sections: the working tree (a single checkout of the project on disk), the staging area (a file called the index that records what will go into the next commit), and the Git directory (where Git stores metadata and the object database, and what gets copied when you clone). — https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- Most Git operations only need local files and resources and do not require information from a remote server. — https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- Everything in Git is checksummed before it is stored and is referred to by that checksum, a 40-character SHA-1 hash, making it impossible to change file contents without Git detecting it. — https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F

## staging-area
- Files in the working directory are either tracked (in the last snapshot or newly staged) or untracked (not in the last snapshot and not staged). — https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- `git add` is a multipurpose command used to begin tracking new files, stage modified files, and mark merge-conflicted files as resolved. — https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- Git stages a file exactly as it is at the moment `git add` is run; if you edit the file again afterward you must run `git add` again to stage the newest version before committing. — https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- The staging area lets you build commits incrementally by selectively choosing which modified files, or even which changes, to include in the next commit while leaving others unstaged. — https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- `git status` reports files in three groupings: "Changes to be committed" (staged), "Changes not staged for commit" (modified but unstaged), and "Untracked files". — https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- Running `git diff` with no arguments compares the working directory to the staging area (shows unstaged changes), while `git diff --staged` (or `--cached`) compares the staging area to the last commit (shows what will be in the next commit). — https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository

## refs-and-objects
- Git is a content-addressable filesystem: you can insert content and get back a unique SHA-1 key to retrieve it later; objects are stored under `.git/objects/` using the first two hash characters as a subdirectory and the remaining 38 as the filename. — https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
- There are three core object types: blob objects store file content only (not the filename), tree objects store directory structure and filenames by pointing to blobs/subtrees with a mode and name, and commit objects store a snapshot's tree pointer, parent commit SHA-1(s), author/committer info, and message. — https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
- A commit object points to exactly one tree (the project snapshot) and to zero or more parent commits, which is what creates the linked commit history graph. — https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
- References (refs) are simple named pointers to SHA-1 values, stored as files under `.git/refs`, with branches under `.git/refs/heads` and tags under `.git/refs/tags`, so users can use friendly names instead of raw hashes. — https://git-scm.com/book/en/v2/Git-Internals-Git-References
- HEAD is a symbolic reference that normally points at the current branch (e.g. its file content is `ref: refs/heads/master`); in a detached HEAD state it instead contains a commit SHA-1 directly. — https://git-scm.com/book/en/v2/Git-Internals-Git-References
- Lightweight tags are refs that never move and simply point at a commit, whereas annotated tags are full objects containing tagger, date, and message and can point at any Git object, not only commits. — https://git-scm.com/book/en/v2/Git-Internals-Git-References

## rebasing
- Rebasing works by finding the common ancestor of two branches, computing the diff introduced by each commit on the current branch, resetting the current branch to the target branch's tip, and reapplying each of those diffs in turn as new commits. — https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- Rebasing produces a cleaner, linear project history that looks as though the work happened in series, even when it actually happened in parallel on separate branches. — https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- The golden rule of rebasing is: do not rebase commits that exist outside your repository and that other people may have based work on. — https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- Rebasing public/shared commits causes problems because it abandons existing commits and creates new, similar-but-different ones, forcing collaborators to re-merge their work and producing confusing duplicate-looking history. — https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- `git rebase --onto master server client` replays only the commits unique to `client` (since it diverged from `server`) onto `master`, without requiring you to first check out the target branch. — https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- Safe practice is to rebase local changes to clean up work before pushing, but never rebase anything that has already been pushed and shared with others. — https://git-scm.com/book/en/v2/Git-Branching-Rebasing

## interactive-rebase
- Interactive rebase is invoked as `git rebase -i <after-this-commit>` and opens an editor listing the commits about to be replayed, letting you edit that list before the rebase runs; it can also be used to split a commit into multiple commits. — https://git-scm.com/docs/git-rebase
- The interactive rebase todo list supports the commands pick (use commit as-is), reword (use commit, edit its message), edit (use commit, stop to amend), squash (fold into previous commit, combine messages), fixup (fold into previous commit, discard its log message), drop (remove commit), exec (run a shell command), label, reset, and merge. — https://git-scm.com/docs/git-rebase
- Commits are listed in the todo editor in the reverse order from `git log` output — the oldest commit to be replayed appears at the top of the list. — https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
- Marking a commit `edit` causes Git to stop right after applying that commit, allowing `git commit --amend` to change it, followed by `git rebase --continue` to resume. — https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
- Reordering the lines in the interactive rebase todo list reorders the resulting commits, and deleting a line drops that commit entirely. — https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
- Because interactive rebase rewrites commits, it changes their SHA-1 hashes (and those of all descendant commits), so it should not be used on commits that have already been pushed to a shared/central repository. — https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History

## cherry-pick
- `git cherry-pick <commit>` applies the changes introduced by an existing commit and records them as a new commit on top of the current branch's tip. — https://git-scm.com/docs/git-cherry-pick
- The `-n`/`--no-commit` option applies a cherry-pick's changes to the working tree and index without creating a commit, letting you cherry-pick several commits and commit them together once. — https://git-scm.com/docs/git-cherry-pick
- The `-x` option appends a line "(cherry picked from commit ...)" to the new commit's message, indicating its origin; it is meant for cherry-picks between two public branches (e.g., backporting to a maintenance branch) and should be avoided when cherry-picking from a private branch. — https://git-scm.com/docs/git-cherry-pick
- Because a merge commit has multiple parents, you normally cannot cherry-pick it; the `-m`/`--mainline <parent-number>` option specifies which parent (numbered from 1) should be treated as the mainline for the replay. — https://git-scm.com/docs/git-cherry-pick
- When a cherry-pick cannot be applied cleanly, the branch and HEAD stay at the last successful commit, `CHERRY_PICK_HEAD` is set to point at the problematic commit, and conflicting files get conflict markers you must resolve before continuing. — https://git-scm.com/docs/git-cherry-pick

## revert-vs-reset
- `git revert` creates a new commit that records the reversal of an existing commit's changes, preserving history, whereas `git reset` moves the current branch pointer and can discard commits and uncommitted changes rather than adding a new commit. — https://git-scm.com/docs/git-revert
- `git reset` manipulates up to three trees in order — it always moves the branch HEAD points to, `--mixed` (the default) also updates the index to match the new HEAD, and `--hard` additionally overwrites the working directory to match, making `--hard` the only variant that is not working-directory-safe. — https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
- `git reset --soft <commit>` moves the branch reference but leaves the index and working directory untouched, so the diff between the old and new HEAD stays staged. — https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
- When a path is given to `git reset`, it skips moving HEAD and instead updates only the index (and optionally, for `checkout`, the working directory) for that path; for example `git reset file.txt` is shorthand for `git reset --mixed HEAD file.txt`, which unstages the file. — https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
- Reverting a merge commit requires the `-m`/`--mainline <parent-number>` option to tell `git revert` which parent should be treated as the mainline, since normally it cannot be inferred which side of a merge is mainline. — https://git-scm.com/docs/git-revert
- `git revert` is the appropriate tool for undoing commits that have already been published or shared, since it preserves history via a new commit rather than rewriting existing commits the way `reset` does. — https://git-scm.com/docs/git-revert

## bisect
- `git bisect` performs a binary search through commit history to find as quickly as possible the commit that introduced a bug, using a known bad commit and a known good commit as the search boundaries. — https://git-scm.com/docs/git-bisect
- The workflow is `git bisect start`, then `git bisect bad` to mark the current (broken) commit and `git bisect good <commit>` to mark a known-working commit; Git then checks out a commit in the middle of that range for you to test and mark good or bad, repeating until the first bad commit is found. — https://git-scm.com/docs/git-bisect
- `git bisect run <cmd> [<args>...]` automates the process by repeatedly running a script that must exit 0 for good commits and a code between 1 and 127 (excluding 125) for bad commits; exit code 125 tells bisect to skip an untestable commit. — https://git-scm.com/docs/git-bisect
- `git bisect reset` ends the bisect session and returns the working tree to the commit that was checked out before `git bisect start` began (or to a specified commit). — https://git-scm.com/docs/git-bisect
- The terms "good"/"bad" can be replaced with custom terms such as "old"/"new" via `git bisect start --term-old <term> --term-new <term>`, useful when bisecting for something other than a bug (e.g., a behavior change). — https://git-scm.com/docs/git-bisect

## github-flow
- GitHub flow is a lightweight, branch-based workflow useful for developers and non-developers alike collaborating on a project. — https://docs.github.com/en/get-started/using-github/github-flow
- The first step of GitHub flow is to create a branch with a short, descriptive name so collaborators can see ongoing work at a glance. — https://docs.github.com/en/get-started/using-github/github-flow
- Contributors commit and push changes to their branch, giving each commit a descriptive message so others understand what it contains. — https://docs.github.com/en/get-started/using-github/github-flow
- Once changes are pushed, contributors open a pull request to ask collaborators for feedback. — https://docs.github.com/en/get-started/using-github/github-flow
- Reviewers can comment on the whole pull request or on specific lines/files, and pushing new commits automatically updates the pull request. — https://docs.github.com/en/get-started/using-github/github-flow
- After the pull request is approved, the branch is merged into the default branch and then deleted, signaling completed work while preserving the historical record. — https://docs.github.com/en/get-started/using-github/github-flow

## git-flow
- The Gitflow Workflow defines a strict branching model designed around the project release, first published in a 2010 blog post by Vincent Driessen at nvie. — https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
- Instead of a single main branch, Gitflow uses two long-running branches: main stores the official release history, and develop serves as an integration branch for features. — https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
- Feature branches are branched off develop and are merged back into develop once the feature is complete. — https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
- Release branches support preparation of a new production release and are merged into both main and develop. — https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
- Hotfix branches provide a dedicated channel for patching production, and a hotfix branch is merged into both main and develop. — https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
- Running "git flow init" (from the git-flow extension library) on an existing repository creates the develop branch. — https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

## trunk-based-development
- Trunk-based development is a version control management practice where developers merge small, frequent updates to a core "trunk" (main) branch. — https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- It is a more open model since all developers have access to the main code, enabling teams to iterate quickly and implement CI/CD. — https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- Gitflow has fallen in popularity in favor of trunk-based workflows, which are now considered best practice for modern continuous software delivery and DevOps. — https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- In trunk-based development, code review is performed immediately rather than being placed into an asynchronous system for later review. — https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- Automated tests provide a layer of preemptive code review in trunk-based development. — https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
- Trunk-based development is currently the standard for high-performing engineering teams since it sets and maintains a software release cadence via a simplified branching strategy. — https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development

## forking-workflow
- The Forking Workflow gives every developer their own server-side repository instead of relying on one single central repository. — https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
- Each contributor ends up with two git repositories: a private local one and a public server-side one (their fork). — https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
- No other developer is allowed to push to another user's public fork, but anyone can pull from it. — https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
- Contributors push finished commits to their own public fork, then file a pull request with the main repository to let the maintainer know an update is ready to be integrated. — https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
- The project maintainer pulls a contributor's changes into their local repository, verifies they don't break the project, merges into the local main branch, then pushes main to the official repository. — https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
- The Forking Workflow is commonly used in public open-source projects. — https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow

## naming-conventions
- Git has very few restrictions on branch names, other than not starting or ending a name with a slash and not allowing consecutive slashes. — https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names
- Safe characters for branch and tag names are limited to the English alphabet, numbers, and a limited set of punctuation: period, hyphen, underscore, and forward slash. — https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names
- Starting a branch name with a letter helps avoid confusion. — https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names
- Special characters like $ and ; require escaping or quoting in branch names because shells interpret them specially ($ expands variables, ; separates commands). — https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names
- GitHub prevents pushing branch or tag names that resemble Git object IDs (40 hexadecimal characters) to avoid confusion with commit hashes, and blocks names beginning with "refs/". — https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names
- A new branch name must pass all checks defined by git-check-ref-format, which restricts which characters are allowed in a branch name. — https://git-scm.com/docs/git-branch

## branch-protection
- Branch protection rules let you enforce that all pull requests receive a specific number of approving reviews before someone can merge into the protected branch. — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Required status checks must show a successful, skipped, or neutral status before collaborators can make changes to a protected branch. — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- When commit signing is required, contributors and bots can only push commits that have been signed and verified to the branch. — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Linear history enforcement requires that pull requests merged into the protected branch use a squash merge or a rebase merge, blocking merge commits. — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- By default GitHub blocks force pushes to protected branches, though administrators can selectively enable them for specific users or teams. — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- A branch protection rule can target a specific branch, all branches, or any branch matching a name pattern specified with fnmatch syntax, such as "*release*". — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
- Administrators can restrict who can push to matching branches by specifying which people, teams, or apps are allowed. — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule

## merge-vs-rebase
- Both git rebase and git merge solve the same problem of integrating changes from one branch into another, just in very different ways. — https://www.atlassian.com/git/tutorials/merging-vs-rebasing
- Merging creates a new merge commit that ties together the histories of both branches without changing the existing branches, a non-destructive operation. — https://www.atlassian.com/git/tutorials/merging-vs-rebasing
- Rebasing moves the entire feature branch to begin on the tip of the main branch, creating brand-new commits for each commit in the original branch. — https://www.atlassian.com/git/tutorials/merging-vs-rebasing
- Rebasing produces a cleaner, perfectly linear project history by eliminating the extraneous merge commits that git merge requires. — https://www.atlassian.com/git/tutorials/merging-vs-rebasing
- Rebasing loses the context provided by a merge commit, since you can't see when upstream changes were incorporated into the feature branch. — https://www.atlassian.com/git/tutorials/merging-vs-rebasing
- Interactive rebasing lets you alter commits as they are moved to the new branch, commonly used to clean up messy history before merging into main. — https://www.atlassian.com/git/tutorials/merging-vs-rebasing

## resolving-conflicts
- When a merge conflict occurs, Git inserts conflict markers into the file using <<<<<<<, =======, and >>>>>>> delimiters to separate "ours" from "theirs". — https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging
- Git marks conflicted files with a "UU" (unmerged) status visible in "git status" output. — https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging
- During a conflicted merge, Git stores three versions of a file in the index as numbered stages: stage 1 is the common ancestor, stage 2 is your version, and stage 3 is the version from the branch being merged in. — https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging
- The merge strategy options -Xignore-all-space and -Xignore-space-change let Git automatically resolve conflicts caused only by whitespace differences. — https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging
- The git merge-file command can manually merge three file versions (ours, base, theirs) to produce a resolved result. — https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging
- A merge commit can be undone with "git revert -m 1 HEAD", which creates a new commit reversing the merge rather than rewriting history. — https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging

## atomic-commits
- Git's guidance is to make each commit a logically separate changeset rather than combining unrelated work into one massive commit. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- If some of the changes you want to commit modify the same file, `git add --patch` can be used to partially stage a file so unrelated changes end up in separate commits. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- The project snapshot at the tip of a branch is identical whether the work is one commit or five, as long as all the changes are added at some point, so splitting work into logical commits only helps reviewers, it doesn't change the final tree. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- Making commits logically separate also makes it easier to pull out or revert one of the changesets later if needed. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- `git rebase -i` can be used to squash work down to a single commit or rearrange work across commits before submitting it. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- Before committing, running `git diff --check` identifies possible whitespace errors and lists them so they can be cleaned up prior to the commit. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project

## conventional-commits
- The Conventional Commits message format is `<type>[optional scope]: <description>` followed optionally by a blank line, body, and footer(s). — https://www.conventionalcommits.org/en/v1.0.0/
- Commits MUST be prefixed with a type (a noun such as `feat` or `fix`), followed by an optional scope, an optional `!`, and a required terminal colon and space. — https://www.conventionalcommits.org/en/v1.0.0/
- The type `feat` MUST be used when a commit adds a new feature to the application or library. — https://www.conventionalcommits.org/en/v1.0.0/
- The type `fix` MUST be used when a commit represents a bug fix for the application. — https://www.conventionalcommits.org/en/v1.0.0/
- A scope MUST consist of a noun describing a section of the codebase, surrounded by parentheses, e.g. `fix(parser):`. — https://www.conventionalcommits.org/en/v1.0.0/
- A description MUST immediately follow the colon and space after the type/scope prefix, and a commit body, if present, MUST begin one blank line after the description. — https://www.conventionalcommits.org/en/v1.0.0/
- Breaking changes MUST be indicated either in the type/scope prefix (via `!` before the colon) or as a footer entry, and a breaking-change footer MUST consist of the uppercase text `BREAKING CHANGE`, followed by a colon, space, and description. — https://www.conventionalcommits.org/en/v1.0.0/
- Conventional Commits types and scopes MUST NOT be treated as case-sensitive by implementors, with the exception of `BREAKING CHANGE`, which MUST be uppercase; `BREAKING-CHANGE` MUST be treated as synonymous with `BREAKING CHANGE` in a footer token. — https://www.conventionalcommits.org/en/v1.0.0/

## commit-message-style
- A commit message subject line should start with a single line no more than about 50 characters that concisely describes the changeset. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- The subject line should be written in the imperative mood, e.g. "Fix bug" rather than "Fixed bug" or "Fixes bug," matching the style Git itself uses for commit messages generated by commands like `git merge` and `git revert`. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- The subject line must be followed by a blank line before any detailed explanation; this blank line separating summary from body is critical because tools like rebase get confused if the two are run together. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- The body of the message should be wrapped to about 72 characters or so. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- The Git project requires that the detailed explanation include the motivation for the change and contrast its implementation with previous behavior. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- Further paragraphs in a commit message come after blank lines, and bullet points (using a hyphen or asterisk followed by a single space, with blank lines between them) are acceptable. — https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project

## signing-commits
- Git supports signing commits and tags with GPG, SSH, or S/MIME signatures that can be cryptographically verified. — https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification
- GitHub marks a commit "Verified" when the commit is signed and the signature was successfully verified, and "Unverified" when the commit is signed but the signature could not be verified. — https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification
- SSH signature verification requires Git 2.34 or later, and S/MIME verification requires Git 2.19 or later. — https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification
- A verification record is stored alongside a commit once its signature is verified upon push, and this record persists even if the signing key is later rotated or revoked, or the contributor leaves the organization. — https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification
- To sign an individual commit with GPG, add the `-S` flag, e.g. `git commit -S -m "YOUR_COMMIT_MESSAGE"`; to sign all commits by default, set `git config commit.gpgsign true` (per-repository, Git 2.0.0+) or `git config --global commit.gpgsign true` (for all repositories). — https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits
- In the git CLI, tags are signed with the lowercase `-s` flag (e.g. `git tag -s <tag-name> -m '<message>'`) while commits use the capital `-S` flag, and a signed tag can be checked with `git tag -v <tag-name>`. — https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
- `git log --show-signature` displays signature information in the commit log, and `git merge --verify-signatures <branch>` will refuse to merge unless all commits on the branch have trusted GPG signatures. — https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

## pull-requests
- Pull requests are proposals to merge code changes into a project and are described as GitHub's foundational collaboration feature for discussing and reviewing changes before merging. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- A pull request's Conversation tab displays a description of the changes, a timeline of events, and comments and reviews from collaborators. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- The Commits tab shows all commits made to the pull request branch in chronological order, and the Checks tab displays the status of automated tests, builds, or other CI workflows triggered by pushes to the branch. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- The Files Changed tab shows the differences between the proposed changes and the existing code. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- When creating a pull request, a contributor can choose to make it a draft pull request, which cannot be merged and does not automatically request review from code owners. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- GitHub generates temporary read-only git references for a pull request, including one pointing to its latest commit and an optional simulated merge branch when there are no conflicts. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests

## code-review
- Pull request reviews are one of the primary ways people collaborate on GitHub, letting reviewers comment on changes, suggest improvements, and approve or request changes before code is merged. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- After a pull request is opened, anyone with read access to the repository can review and comment on the changes it proposes. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- Reviewers can suggest specific changes to lines of code, which the pull request author can then apply directly from the pull request. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- A review can be submitted as one of three types: "Comment" (general feedback without explicit approval or change requests), "Approve" (feedback plus approval to merge), or "Request changes" (feedback that must be addressed before the pull request can be merged). — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- Repository administrators can require approvals before pull requests are merged, which helps ensure code quality and prevent accidental merges. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- When code owners are defined for the code being changed, they are automatically requested as reviewers on a pull request that modifies that code. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews

## draft-prs
- When you create a pull request, you can choose to make it a draft pull request; draft pull requests cannot be merged and code owners are not automatically requested to review them. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- No one can merge a pull request until it is marked as ready for review again after being converted to a draft. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request
- Marking a draft pull request as ready for review will request reviews from any code owners defined for the changed code. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request
- A pull request can be converted to a draft at any time, for example if it was opened by mistake instead of as a draft, or if received feedback shows further changes are needed. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request
- A draft pull request can be marked as ready for review by clicking the "Ready for review" button in the merge box, or via the GitHub CLI command `gh pr ready`. — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request

## codeowners
- A CODEOWNERS file defines individuals or teams that are responsible for code in a repository, and code owners are automatically requested for review when a pull request modifies code they own. — https://docs.github.com/articles/about-code-owners
- To use a CODEOWNERS file, create it in the `.github/`, root, or `docs/` directory of the repository; if files exist in more than one location, GitHub searches in that order and uses the first one it finds. — https://docs.github.com/articles/about-code-owners
- CODEOWNERS syntax follows most of the same pattern rules used in `.gitignore` files, with exceptions: escaping `#` with a backslash doesn't work, `!` negation is not supported, and character ranges with `[ ]` don't function; patterns are case-sensitive. — https://docs.github.com/articles/about-code-owners
- The people or teams listed as code owners must have write permissions for the repository; for a team to be a code owner, the team itself must have write permissions, even if all individual team members already have write permissions. — https://docs.github.com/articles/about-code-owners
- In a CODEOWNERS file, order is important: the last matching pattern in the file takes the most precedence over earlier matching patterns. — https://docs.github.com/articles/about-code-owners
- People with admin or owner permissions can require that pull requests be approved by code owners before they can be merged. — https://docs.github.com/articles/about-code-owners
- CODEOWNERS files must be under 3 MB in size; a file over this limit will not be loaded, meaning code owner information will not be shown and code owners will not be requested to review changes. — https://docs.github.com/articles/about-code-owners

## fetch-pull-push
- `git fetch <remote>` downloads all new data from a remote repository and updates remote-tracking branches (e.g. `pb/master`) without touching your working files or merging anything into your current branch. — https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
- `git pull` is effectively `git fetch` followed by `git merge`, and it only works automatically when the current branch is set up to track a remote branch. — https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
- Cloning a repository automatically sets up your local `master` (or default) branch to track the remote `master` branch on the server you cloned from. — https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
- Since Git 2.27, `git pull` expects the `pull.rebase` configuration variable to be set explicitly (`false` for merge, `true` for rebase) to avoid a warning. — https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
- `git push <remote> <branch>` uploads local commits to a remote repository and is rejected if someone else has pushed to that branch in the meantime, requiring you to fetch and incorporate their work first. — https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes

## tracking-branches
- A remote-tracking branch is a local reference (named `<remote>/<branch>`, e.g. `origin/master`) that Git moves automatically during network communication to reflect the state of the branch on the remote. — https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches
- A tracking (upstream) branch is a local branch with a direct relationship to a remote branch, so that a plain `git pull` on it knows automatically which server to fetch from and which branch to merge. — https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches
- Running `git checkout serverfix` (or `git checkout --track origin/serverfix`) automatically creates a local branch that tracks the matching remote branch when the name matches exactly one remote branch. — https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches
- The upstream relationship for an existing local branch can be set or changed with `git branch -u origin/serverfix` (i.e. `--set-upstream-to`). — https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches
- `git branch -vv` lists local branches together with their tracked remote branch and ahead/behind counts, e.g. `serverfix ... [teamone/server-fix-good: ahead 3, behind 1]`, but these numbers only reflect the last fetch and require `git fetch --all` first for accuracy. — https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches

## tags-and-releases
- Git supports two tag types: lightweight tags, which are just a pointer (commit checksum) to a commit, and annotated tags, which are full objects storing the tagger name, email, date, and message, and which can be GPG-signed. — https://git-scm.com/book/en/v2/Git-Basics-Tagging
- An annotated tag is created with `git tag -a v1.4 -m "my version 1.4"`, while a lightweight tag is created with just `git tag v1.4-lw`. — https://git-scm.com/book/en/v2/Git-Basics-Tagging
- `git push` does not transfer tags to a remote by default; a specific tag must be pushed with `git push origin v1.5`, or all tags at once with `git push origin --tags` (note `--follow-tags` pushes only annotated tags). — https://git-scm.com/book/en/v2/Git-Basics-Tagging
- Checking out a tag (e.g. `git checkout v2.0.0`) puts the repository in a "detached HEAD" state, so a new branch (`git checkout -b version2 v2.0.0`) should be created to make changes safely. — https://git-scm.com/book/en/v2/Git-Basics-Tagging
- GitHub Releases are built on top of Git tags to mark specific points in a repository's history, though a release's creation date can differ from its underlying tag's date since they are created independently. — https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- A GitHub release can include release notes plus binary file assets, and GitHub automatically generates downloadable ZIP and tarball archives of the repository at the tagged point, with admins able to control whether Git LFS objects are included in those archives. — https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- A single GitHub release supports up to 1,000 assets, with each individual file capped at 2 GiB. — https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

## git-hooks
- Git hooks are scripts stored in the `hooks` subdirectory of the Git directory (by default `.git/hooks`, or wherever `core.hooksPath` points), and a hook is enabled by placing an appropriately named, executable file there (sample scripts ship with a `.sample` extension and must be renamed to activate). — https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks ; https://git-scm.com/docs/githooks
- Hook scripts can be written in any scripting language capable of being executed as a program (shell, Ruby, Python, Perl, etc.), not just shell. — https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
- Client-side hooks (such as `pre-commit`, `commit-msg`, `post-commit`, `pre-push`) are triggered by local operations like committing, merging, and pushing, and are not copied to a new clone of a repository. — https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
- Server-side hooks (`pre-receive`, `update`, `post-receive`) run on the remote when a push is received: `pre-receive` can reject the entire push, `update` runs once per branch and can reject just that reference, and `post-receive` runs after the push completes and is often used to trigger notifications or CI. — https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
- The `pre-push` hook runs during `git push`, after the remote refs have been updated but before any objects have been transferred, and can be used to halt a push. — https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks

## ci-integration
- A GitHub Actions workflow is a configurable automated process made up of one or more jobs, defined in a YAML file placed in the `.github/workflows` directory at the root of the repository. — https://docs.github.com/en/actions/writing-workflows/about-workflows
- Workflows can be triggered by events within the repository, external events via `repository_dispatch`, a defined schedule, or manual invocation, using the `on` key in the workflow YAML to declare the trigger. — https://docs.github.com/en/actions/writing-workflows/about-workflows
- Each job in a workflow runs on a runner machine and consists of one or more steps, where each step either runs a script or invokes an action (a reusable unit of automation). — https://docs.github.com/en/actions/writing-workflows/about-workflows
- When a triggering event occurs, GitHub scans the repository's `.github/workflows` directory and runs any workflow whose trigger conditions match that event. — https://docs.github.com/en/actions/writing-workflows/about-workflows

## pre-commit
- The `pre-commit` hook is invoked by `git commit` before the commit message editor is shown and before the commit object is created, making it suitable for inspecting the snapshot about to be committed. — https://git-scm.com/docs/githooks
- The default sample `pre-commit` hook checks for non-ASCII filenames and trailing whitespace, and the non-ASCII filename check can be disabled by setting the `hooks.allownonascii` config option to true. — https://git-scm.com/docs/githooks
- If the `pre-commit` script exits with a non-zero status, `git commit` aborts before creating the commit; this check can be skipped entirely with `git commit --no-verify`. — https://git-scm.com/docs/githooks
- The `pre-commit` hook takes no parameters and is run with the environment variable `GIT_EDITOR=:` set. — https://git-scm.com/docs/githooks
- Hooks such as `pre-commit` are not copied when a repository is cloned, since `.git/hooks` content is local-only (though `git init` templates can populate them in newly created repos). — https://git-scm.com/docs/githooks

## monorepo-vs-polyrepo
- GitHub's own guidance favors having regular collaborators work from a single shared repository, creating pull requests between branches, and reserves forking (separate repository copies) for contributors unaffiliated with the project, such as open-source contributors. — https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
- A Git submodule lets you keep one Git repository as a subdirectory of another, treating the two as independent projects with separate commit histories while still being able to consume one from within the other — a mechanism for composing multiple repositories, as an alternative to a single monorepo. — https://git-scm.com/book/en/v2/Git-Tools-Submodules
- Adding a submodule with `git submodule add <url>` creates a `.gitmodules` file mapping the subdirectory to the external repository's URL, and cloning a superproject requires `git clone --recurse-submodules` (or a separate `git submodule init` and `git submodule update`) to populate the submodule content. — https://git-scm.com/book/en/v2/Git-Tools-Submodules
- Submodule-based multi-repo setups have documented friction: switching branches can leave submodule directories showing as untracked, and pushing changes requires coordinating commits across both the submodule and the parent (superproject) repository. — https://git-scm.com/book/en/v2/Git-Tools-Submodules
- GitHub documents a supported path for going from a monorepo-style layout to a polyrepo layout: turning a single folder within a repository into its own brand-new repository using `git filter-repo --path FOLDER-NAME/` or `git filter-repo --subdirectory-filter FOLDER-NAME`, though the new repository will not retain the original repository's branches and tags. — https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository

## large-files-lfs
- Git Large File Storage (Git LFS) is an open source Git extension that lets large files be versioned like other text files by storing a small pointer file in the Git repository instead of the file's actual contents. — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- The LFS pointer file records the Git LFS version in use, a unique object identifier (oid) for the file, and the file's size; when the repository is cloned, GitHub uses this pointer as a map to fetch the actual large file. — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- Maximum per-file size for Git LFS on GitHub varies by plan: 2 GB on GitHub Free and Pro, 4 GB on GitHub Team, and 5 GB on GitHub Enterprise Cloud, and any file above the absolute 5 GB ceiling is rejected by Git LFS with an error. — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- Git LFS cannot be used with GitHub Pages sites or with template repositories. — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- To track a file type with Git LFS, a repository must run `git lfs track` followed by the file extension, after Git LFS itself has been downloaded and installed separately from Git. — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- GitHub's repository best-practices guidance recommends using Git LFS to track large files for performance reasons, noting that GitHub limits the sizes of files allowed in ordinary repositories. — https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories

## sparse-checkout
- `git sparse-checkout` changes a working tree from containing all tracked files to containing only a defined subset of them, and can be used to switch which subset is present or to restore the full working copy. — https://git-scm.com/docs/git-sparse-checkout
- Cone mode (the default, enabled via `core.sparseCheckoutCone`) only accepts directories as input and includes all files under each specified directory at any depth, plus files immediately under any leading/toplevel directories, using a faster hash-based matching algorithm; non-cone mode accepts arbitrary gitignore-style patterns but is deprecated due to O(N*M) matching cost and pattern-semantics pitfalls. — https://git-scm.com/docs/git-sparse-checkout
- `git sparse-checkout set <dir1> <dir2> ...` switches the repository into sparse-checkout mode restricted to the given directories and automatically enables the `core.sparseCheckout`, `core.sparseCheckoutCone`, and `index.sparse` configuration settings. — https://git-scm.com/docs/git-sparse-checkout
- `git sparse-checkout init` is a deprecated command (kept for compatibility) that behaves like calling `set` with no paths, since historically both `init` and `set` were needed but `set` now performs all necessary configuration itself. — https://git-scm.com/docs/git-sparse-checkout
- `git sparse-checkout list` prints the directories or patterns currently defining the sparse-checkout, showing only the recursive directories when in cone mode. — https://git-scm.com/docs/git-sparse-checkout
- A "sparse index" (enabled via `set --sparse-index` and driven by `index.sparse`) shrinks the Git index itself to align with the sparse-checkout definition, giving significant performance advantages for commands like `git status` and `git add` in large repositories. — https://git-scm.com/docs/git-sparse-checkout

## secret-management
- GitHub secret scanning automatically detects credential leaks such as API keys, passwords, and tokens across a repository's entire Git history and all branches so they can be secured before exploitation. — https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
- Secret scanning also inspects issue descriptions, comments, titles, pull request content, GitHub Discussions, wikis, and secret gists, not just committed file content. — https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
- Secret scanning is automatically enabled and free for public repositories, while private and internal repositories require GitHub Secret Protection (Team or Enterprise Cloud). — https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
- GitHub partners with service providers to validate detected secrets and reports valid partner secrets directly to the issuing provider for revocation. — https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
- Push protection blocks a push before it completes when it detects a potential secret in the pushed content, covering command-line pushes, the web UI, file uploads, and REST API requests. — https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- Push protection is enabled by default for individual user accounts on GitHub.com to prevent pushes of secrets to public repositories, while repository- and organization-level push protection must be turned on by an administrator. — https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- Anyone with write access can bypass push protection by supplying a reason such as "used in tests," "false positive," or "I'll fix it later," each of which affects how the resulting alert is recorded. — https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- If sensitive data such as a credential is committed, GitHub's guidance is to first revoke or rotate that credential, since a revoked secret cannot be used for access even if it remains in history. — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- GitHub recommends using the `git filter-repo` tool (with its `--sensitive-data-removal` flag) rather than `git filter-branch` to rewrite history and remove sensitive data from a repository. — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- After rewriting and force-pushing history to remove sensitive data, the data can still persist in existing clones, forks, and GitHub's cached views of commits, so collaborators must be coordinated with directly. — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

## gitignore-hygiene
- A `.gitignore` file specifies intentionally untracked files that Git should ignore, with patterns matched relative to the location of the `.gitignore` file unless they contain no slash. — https://git-scm.com/docs/gitignore
- Gitignore patterns are read from multiple sources in a defined precedence order: command-line patterns, `.gitignore` files in the directory and its parents, `$GIT_COMMON_DIR/info/exclude`, and the file named by `core.excludesFile`. — https://git-scm.com/docs/gitignore
- A trailing slash in a pattern (e.g. `frotz/`) restricts the match to directories only, while `**` can be used to match zero or more directories or match with arbitrary depth (e.g. `a/**/b`). — https://git-scm.com/docs/gitignore
- A `!` prefix negates a pattern, re-including a previously excluded file, but this cannot re-include a file if one of its parent directories is excluded. — https://git-scm.com/docs/gitignore
- Git will ignore files and directories listed in the personal global configuration file at `~/.config/git/ignore` (set via `core.excludesFile`), which is useful for machine- or editor-specific files that shouldn't be shared with a project's other contributors. — https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files
- Repository-specific ignore rules that should not be committed and shared with others can instead be placed in `.git/info/exclude`. — https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files
- GitHub maintains an official collection of recommended `.gitignore` templates for many languages, environments, and operating systems in the `github/gitignore` repository. — https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files
- Adding a rule to `.gitignore` does not stop Git from tracking a file that is already tracked; to ignore such a file it must first be untracked with `git rm --cached <file>`. — https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files

## signed-tags
- Passing `-s` or `--sign` to `git tag` creates a tag that is cryptographically signed using the signing key configured for the user, with the signing backend determined by the `gpg.format` configuration variable (defaults to OpenPGP). — https://git-scm.com/docs/git-tag
- Passing `-u <key-id>` (or `--local-user=<key-id>`) to `git tag` creates a cryptographically signed tag using the specified key instead of the default one. — https://git-scm.com/docs/git-tag
- Using `-a`, `-s`, or `-u <key-id>` causes `git tag` to create a full tag object (rather than a lightweight tag), which requires a tag message and records a tagger name, email, and date. — https://git-scm.com/docs/git-tag
- `git tag -v <tagname>` (or `--verify`) verifies the cryptographic signature of the named tag(s). — https://git-scm.com/docs/git-tag
- Setting the boolean configuration variable `tag.gpgSign` to true makes Git sign all tags with GPG by default, unless overridden with `--no-sign`. — https://git-scm.com/docs/git-tag
- To sign a tag, the user must first configure a signing key via `git config --global user.signingkey <key-id>`, generated for example with `gpg --gen-key`. — https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
- Creating a signed tag uses `-s` in place of `-a`, for example `git tag -s v1.5 -m 'my signed 1.5 tag'`, and the signature can be inspected with `git show v1.5` or verified with `git tag -v v1.4.2.1` provided the signer's public key is in the local keyring. — https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
- `git merge --verify-signatures <branch>` will verify every commit's signature being merged in and abort the merge if any commit is not signed or does not have a valid signature. — https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

## credential-storage
- `git credential` exposes Git's internal credential storage/retrieval interface via four actions — `fill`, `approve`, `reject`, and `capability` — that scripts can use to obtain and report on credentials the same way Git internally does. — https://git-scm.com/docs/git-credential
- The `fill` action returns a matching credential by first consulting configured helpers and, if a value is still missing, prompting the user; `approve` sends a used credential to helpers to be stored, and `reject` tells helpers to erase a credential that turned out to be invalid. — https://git-scm.com/docs/git-credential
- Git ships two built-in credential helpers: `cache`, which holds credentials in memory for a short period, and `store`, which saves credentials indefinitely in a plaintext file on disk. — https://git-scm.com/docs/gitcredentials
- Platform-specific secure helpers such as `git-credential-osxkeychain` (macOS), `git-credential-wincred` (Windows), and `git-credential-libsecret` (Linux) store credentials in the operating system's native secure credential store rather than in plaintext. — https://git-scm.com/docs/gitcredentials
- Multiple credential helpers can be configured together via repeated `credential.helper` entries, and Git will try each in sequence until it obtains both a username and a password. — https://git-scm.com/docs/gitcredentials
- Git Credential Manager (GCM) is a cross-platform credential helper that ships automatically with Git for Windows and can be installed on macOS and Linux to store credentials in the OS-native secure store and support browser-based OAuth authentication with GitHub. — https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git
- GitHub recommends adding an expiration to personal access tokens for additional security, and fine-grained personal access tokens can be scoped to a single user or organization's resources and to specific repositories, unlike classic tokens which grant broad access across all accessible repositories. — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- Personal access tokens function as a password replacement for Git operations over HTTPS: when prompted for a password during an HTTPS operation, the user enters the token instead, and GitHub advises treating access tokens like passwords. — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

