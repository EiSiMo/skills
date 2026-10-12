---
name: exists
description: Check what already exists before building something. Use whenever the user is considering, planning or about to start building something and it is unclear whether comparable projects, products or libraries already exist. Triggers include an explicit "exists" call and phrases like "does this already exist", "is there something like this".
---

# Exists

Answer: **does this already exist, and what is closest to it?** Be honest and opinionated — the point is to save wasted effort, not to reassure.

## 1. Pin down the idea

One sentence: core capability, audience, form (product, CLI, library, …) and platform. If something is missing, ask 1–3 questions first. Fix what "similar" means here: same problem, same audience or same mechanism.

## 2. Research in parallel

Launch subagents in one batch, by default one per angle:

1. **Commercial** — products and paid services.
2. **Open source** — repos, packages, plugins.
3. **Adjacent** — forum threads, hobby and abandoned projects, research, how people solve it today without a dedicated tool.

Each brief repeats the idea and audience, asks to over-collect rather than pre-filter, and to return raw findings as a table: **name · link · description · maker · license/price · last activity · popularity · similar how · differs how**. No verdict — you decide.

## 3. Rank and profile

Merge and rank by closeness to the core capability, then maintenance and reach. Profile the top 3, keep the rest as a one-line longlist.

## 4. Compare

Against our idea: similarities, differences, and gaps none of them cover.

## 5. Verdict

Take a stance: use it or contribute upstream, build a deliberate niche or reuse it as a building block, or green light. Flag close but abandoned projects. State confidence and what would change the answer.

## Output

Chat only, in the user's language. Every candidate with a link.
