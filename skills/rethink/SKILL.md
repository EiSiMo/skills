---
name: rethink
description: Step back from an existing codebase and judge it from the top — does the architecture still hold, is the code good and idiomatic, and what would a professional build today knowing the requirements? Use when a codebase has grown over time and accumulated architectural creep, when the user asks whether to rewrite or refactor, or when they invoke "rethink". Read-only — it never edits, refactors or migrates.
---

# Rethink

Answer: **if this were built again today, knowing the full requirements, what would change — and what should we actually do?**

Read-only until the user leaves this mode: no edits, files, commits or installs. Read-only analysis tools are fine.

## 1. Scope and recon

Default scope is the whole repo, or the area the user names. Map it yourself first: stack, entry points, main modules and boundaries, where the domain logic lives. This decides how to split the team.

## 2. Team

Launch subagents in one batch:

- **Horizontal**, one per lens: architecture & coupling; intent & requirements (reconstructed from tests, docs, history); target picture (what a professional would build today — keep, reshape, discard).
- **Vertical**, one per major subsystem (or per language) for code quality and idiom.

Scale the count to the codebase. Each brief names the paths and languages in scope and asks for raw findings with evidence (path, symbol, observation), not a verdict.

## 3. Merge

Separate essential complexity (belongs to the problem, keep it) from accidental complexity (grown weight, remove it). Evidence over volume and taste.

Judge quality by: consistency, readability, duplication vs. premature abstraction, error handling, dead code, tests on critical paths, coupling, dependency hygiene, and idiom of the respective language.

## 4. Verdict

Neutral. Recommend the smallest change that genuinely solves the problem, and say "leave it" when that is true. Possible verdicts, often combined: leave it, targeted changes, partial restructure, full rebuild.

## Output

Short and high-level, verdict first, key findings after. State confidence and what would change the answer. Chat only, in the user's language.
