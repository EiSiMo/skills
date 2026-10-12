---
name: keepup
description: Explain a term, component, command or concept from the current project in plain, non-technical language, so the user can follow along and make decisions about code they did not write themselves. Zooms out to show where the thing sits in the whole system, then zooms in on what it does and why it exists. Use when the user invokes "keepup", asks "what is X", "why do we have X", "how does X work", or is lost in a term Claude used while asking for a decision.
---

# Keepup

The user owns this project but did not write every line. Explain one thing so they understand it and can decide about it. Read-only: no edits, no files, no commits.

## 1. Find the thing

- The argument is the term. Without one, take the term from your last message the user most likely did not understand, and say which.
- Check the conversation first: if you used the term recently, that meaning and the pending question are what matter.
- Then the code, then the history (`git log -S`, `git blame`) for why it exists.
- Ambiguous → list the meanings and ask. Not found → say so. Never invent.

## 2. Zoom out

What the whole system does in one or two sentences, its few big parts, and where this thing sits. A one-line flow diagram if it helps.

## 3. Zoom in

What it is, what it does, why we have it (what breaks without it), what it touches, and quirks only if they matter.

## 4. The decision

If a question of yours involves it: restate the question plainly, the options with what each changes, costs and risks, your recommendation, then repeat the question. Otherwise skip this.

## Style

- Everyday language, effects over implementation. Unavoidable terms get a short explanation in brackets.
- No code. File paths only in an optional last line.
- Readable in about a minute. Mark inferences ("probably").
- Chat only, in the user's language.
