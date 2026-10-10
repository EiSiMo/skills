---
name: keepup
description: Explain a term, component, command or concept from the current project in plain, non-technical language, so the user can follow along and make decisions about code they did not write themselves. Zooms out to show where the thing sits in the whole system, then zooms in on what it does and why it exists. Use when the user invokes "keepup", asks "what is X", "why do we have X", "how does X work", or is lost in a term Claude used while asking for a decision.
---

# Keepup

Answer one question well: **what is this thing, why do we have it, and what do I need to know to decide about it?** The user owns this project but did not write every line of it. Bring them up to speed on one piece, fast and in plain language, so they can answer a question or simply understand their own system.

This is a **read-only** skill. No edits, no new files, no commits. Reading files, searching and read-only git commands are fine.

## 1. Find the thing

The argument is the term to explain, e.g. `/keepup reparse`.

- **No argument** — take the term or decision from Claude's last question or message that the user most likely did not understand. Say which one you picked.
- **Check the conversation first.** If Claude used the term recently, that is the meaning that matters, and the surrounding question is the decision the user faces.
- **Then the code.** Search for the term in names, commands, config, docs and comments. Read enough to actually understand it, not just to find it.
- **Then the history.** `git log -S`, `git log --grep` and `git blame` show when and why it was added. The reason it exists is often there.
- **Ambiguous** — if the term means several things in this project, list them in one line each and ask which one. **Not found** — say so plainly and show the closest matches. Never invent an explanation.

## 2. Zoom out — the big picture

Start from the top, before any detail:

- What the whole system does, in one or two sentences, as you would explain it to a smart friend.
- The few big parts it consists of, and where this thing sits among them.
- A small text diagram helps when there is a flow: `input → [step] → [this thing] → [step] → result`. Keep it to one line or a handful of boxes.

## 3. Zoom in — the thing itself

- **What it is** — one sentence, no jargon.
- **What it does** — step by step in everyday words. An everyday analogy if one fits honestly; skip it if it would mislead.
- **Why we have it** — the problem it solves, and what would happen without it. Mention when it was added if that helps.
- **What it touches** — what depends on it and what it depends on, as far as it matters for understanding or deciding.
- **Worth knowing** — known costs, limits or quirks, only if they matter.

## 4. The decision (if there is one)

If Claude asked the user something that involves this thing, close the loop:

- Restate the question in plain words.
- The options, each with what it means in practice: what changes, what it costs, what it risks.
- Your recommendation and why, in one or two sentences.
- End by repeating the open question so the user can answer it directly.

If there is no pending decision, skip this section. The user is just curious.

## Language rules

- Plain, everyday language. Explain the effect, not the implementation.
- Every unavoidable technical term gets a short explanation in brackets the first time it appears. Never introduce a new term just to explain another one.
- No code unless the user asks. File paths only at the very end, as an optional "where it lives" line.
- Short. Aim for something readable in about a minute. The user can ask to go deeper.
- Mark what you inferred rather than read in the code: "probably", "it looks like".

## Output

- Chat only. Never write a file.
- Report in the language the user is using in the conversation.
- Structure: **Big picture** → **What it is** → **Why we have it** → (**Your decision**) → optional *Where it lives*.
