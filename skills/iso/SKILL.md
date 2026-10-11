---
name: iso
description: Do the task in an isolated git worktree on its own branch, leaving main untouched until the user has inspected the result and decides to merge. After a merge, always delete the branch and the worktree. Use when the user invokes "iso" or asks to work in a separate worktree or branch.
---

# Iso

Work on this task in isolation. Main stays untouched until the user decides.

1. Create a new branch with a short descriptive name and a git worktree for it, outside the main checkout (e.g. `../<repo>-<branch>`). Branch off the current `main`.
2. Do all work, edits and commits inside that worktree only. Never touch the main checkout.
3. When done, stop and report: branch name, worktree path, what changed, and how to try it. Do not merge.
4. The user inspects the result and decides. Wait for an explicit go before merging.
5. If the user says merge: merge the branch into `main`, then always remove the worktree (`git worktree remove`) and delete the branch (`git branch -d`). Confirm both are gone.
6. If the user rejects it: ask whether to delete the branch and worktree or keep them.
