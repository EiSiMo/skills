---
name: rethink
description: Step back from an existing codebase and judge it from the top — does the architecture still hold, is the code good and idiomatic, and what would a professional build today knowing the requirements? Use when a codebase has grown over time and accumulated architectural creep, when the user asks whether to rewrite or refactor, or when they invoke "rethink". Read-only — it never edits, refactors or migrates.
---

# Rethink

Answer one question well: **if this codebase had to be built again today, knowing the full requirements, what would change — and what should we actually do about it?** Look at everything from the top, honestly and without bias, and take a proportional stance.

This is a **read-only** skill. It observes and judges, it never changes anything. No edits, no new files, no commits, no installs, no destructive commands. Read-only analysis tools are allowed; anything that writes is not. Stay fully in this mode until the user leaves it.

## 1. Scope

Default: the whole repository. If the user names a subsystem, module or area, look at only that, and say so at the top.

## 2. Recon first

Before spawning anyone, the main agent builds the ground truth:

- Languages, frameworks, build and runtime setup.
- Entry points, top-level modules, and the main boundaries between them.
- Size and shape: what is big, what is central, what is peripheral.
- Where the domain logic lives versus the plumbing.

This decides how the team is split. Never dispatch on a codebase you have not mapped.

## 3. The team

Launch several `general` subagents **in the same batch** so they run concurrently. Each starts with fresh context, so every brief must be fully self-contained: name the exact language(s), the exact paths or subsystem in scope, and what to report. A hybrid split, unless repeated evidence says otherwise:

**Horizontal — the global picture.** One agent per cross-cutting lens:

1. **Architecture & coupling** — layering, boundaries, cycles, cohesion, where structural creep has accumulated.
2. **Intent & requirements** — reconstruct what the system actually does and must do, from tests, docs, config and git history; mark what is uncertain rather than guessed.
3. **Target picture** — how a professional would shape this today, knowing the requirements.

**Vertical — depth where breadth cannot reach.** One agent per major subsystem for **quality and idiom**, because good code cannot be judged for a whole large codebase by a single reader. When the repo spans several languages, bundle idiom knowledge per language instead of per subsystem.

Scale the count to the codebase: narrow scope and a single language mean fewer agents; broad scope and many languages mean more. Keep it bounded. Small scopes may need only the horizontal lenses.

Every brief must ask for: **raw findings with evidence** (path, symbol, concrete observation), a per-dimension assessment, and — for the target-picture agent — what it would keep, reshape and discard. Raw findings, not a verdict. The main agent decides.

## 4. Tools

The agents may run read-only analysis: dependency graphs, complexity and duplication scanners, linters, coverage, `git log`/`git blame`. Prefer what is already present. Nothing that installs or writes.

## 5. Merge

Merge and de-duplicate findings. Separate:

- **Essential complexity** — belongs to the problem, would survive any rewrite. Preserve it.
- **Accidental complexity** — grown weight, designing can remove it.

Weigh evidence over volume. A strong finding rests on concrete observations, not on taste.

## 6. Quality & idiom rubric

Judge each area against the same stack-agnostic list, and against the conventions of its own language — idiomatic Go is not idiomatic Python.

- Consistency of names, structure and recurring patterns.
- Readability: naming, function size, nesting, comments that explain the *why*.
- Duplication versus premature abstraction.
- Error handling.
- Dead code and unused abstractions.
- Test quality and coverage of critical paths.
- Coupling and cohesion.
- Dependency hygiene: outdated, unnecessary, risky.
- Idiom: does the code use its language's built-ins and ecosystem, or fight them?

## 7. Verdict

Be neutral. Do not default to keeping things or to rebuilding. Recommend the **smallest change that genuinely solves the problem**, and be equally willing to say "leave it". The verdict is a scale, and a mixed recommendation is normal:

- **Leave it** — it is fine as it is; say so honestly.
- **Targeted changes** — just these one, two, three things.
- **Partial restructure** — reshape certain areas, leave the rest.
- **Full rebuild** — only if the findings truly carry it.

The recommendation may combine these: keep most of it, recut module X, rebuild subsystem Y.

## Output

- A short, high-level, as non-technical as the finding allows. The assessment and the verdict lead; the key findings follow briefly.
- Chat only. Never write a file.
- State confidence, and what would change the answer.
- Report in the language the user is using in the conversation.
