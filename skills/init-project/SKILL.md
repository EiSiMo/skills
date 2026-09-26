---
name: init-project
description: Initialize a new programming project with folder, git repo, MIT license, .gitignore, .env.example, a minimal README and an AGENTS.md containing the owner's coding rules. Use this whenever the user wants to start, create, set up, scaffold or bootstrap a new project, repo or codebase, even if AGENTS.md is not mentioned.
---

# Init Project

## 1. Ask

Ask only for what the user has not already provided:
- **Project name** (kebab-case, used for folder and repo)
- **Goal**: one sentence describing what the project will be when finished

Do not choose a tech stack yet. That happens later, under the AGENTS.md rules.

## 2. Scaffold

Create the project folder if it does not exist. Never overwrite existing files.

1. `git init` with default branch `main` (skip if already a repo).
2. `LICENSE`: standard MIT text, `Copyright (c) <current year> Moritz (github.com/EiSiMo)`.
3. `.gitignore` containing `.env`. Stack-specific entries are added later.
4. `.env.example`, empty.
5. `README.md` and `AGENTS.md` from the templates below.

Both documents describe the **end goal**, never the current state. Write "A CLI tool for searching library catalogs", not "The repo currently contains two scripts".

## 3. Commit & push

1. Commit everything: `chore: initialize project`.
2. If no remote exists and `gh` is authenticated, run `gh repo create EiSiMo/<name> --private --source . --push`. Otherwise ask the user for a remote URL and push.

## README.md template

````markdown
# <name>

## What it does
<Goal, one or two sentences.>

## Usage
<!-- Fill in once the project is usable. -->

## License
MIT, see [LICENSE](LICENSE).
````

## AGENTS.md template

````markdown
# AGENTS.md

## Goal
<Goal, one sentence.>

## Principles
- Maintainability, modularity and best practices come first. Code is not cheap.
- Deep modules: simple interfaces hiding substantial functionality. Avoid many shallow modules. Design interfaces before implementations.
- Use one consistent domain vocabulary across code, tests and docs.
- Choose languages, tools and libraries by current industry standard: widely adopted, maintained, well documented.
- Challenge me when my requests or technical decisions are suboptimal. Propose the better option before implementing.
- Before non-trivial features, ask questions until requirements are unambiguous.

## Workflow
- Small, verifiable steps. Never outrun the feedback loop.
- TDD: failing test, make it pass, refactor. Test behavior via module interfaces, not internals.
- Test what matters, not every line. Few, meaningful tests keep development fast.
- Once the stack is chosen, add a "Stack & Commands" section to this file (languages, frameworks, exact test/lint/build commands) and keep it current.
- Once the stack is chosen, set up pre-commit hooks for formatter, linter, type checks and tests. Never bypass them.
- Commit and push autonomously after each meaningful green step. Use Conventional Commits.

## Conventions
- Code, identifiers, comments, strings and commit messages in English. User-facing text lives in localization resources, never hardcoded.
- Fail loudly: handle errors or propagate them with context, never swallow them.
- Logging via the ecosystem's standard logging library, with levels. No print debugging. Never log secrets.
- Few dependencies, each justified. Commit lockfiles.
- Secrets only in `.env` at project root (gitignored). Keep `.env.example` with keys, no values.
- License: MIT.
- README has only "What it does", "Usage", "License". Docs describe the goal, not the current state.
````
