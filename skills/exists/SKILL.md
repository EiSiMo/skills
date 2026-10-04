---
name: exists
description: Check what already exists before building something. Use whenever the user is considering, planning or about to start building something and it is unclear whether comparable projects, products or libraries already exist. Triggers include an explicit "exists" call and phrases like "does this already exist", "is there something like this".
---

# Exists

Answer one question well: **does this already exist, and what is the closest thing to it?** Do this before any building starts. Be honest and opinionated — the point is to save wasted effort, not to reassure.

## 1. Pin down the idea

State the idea in one sentence: the core capability and its benefit, the target audience, and the form (product, service, CLI, library, plugin) and platform.

If any of these is missing, ask 1–3 focused questions first. Never search on a vague idea.

Also fix what "similar" means here: the same problem, the same audience, or the same mechanism. This decides what counts as a match.

## 2. Research in parallel

Launch several `general` subagents **in the same batch** so they run concurrently. Each subagent starts with fresh context, so every brief must be fully self-contained and must repeat the one-sentence idea and the audience.

Default: three subagents, one per angle.

1. **Commercial** — products and paid services, including pricing, positioning and target market.
2. **Open source** — GitHub projects, package registries, libraries and plugins, including license, activity and maintenance.
3. **Adjacent & community** — forum and community threads, hobby projects, abandoned tools, partial workarounds, academic or research work, and how people solve the problem today when no dedicated tool exists.

Use fewer angles for narrow ideas, more for broad ones, but keep it bounded.

Every brief must ask for:

- The one-sentence idea, audience, form and category/synonym terms.
- A thorough websearch, followed by webfetch on the most promising hits.
- Over-collecting candidates rather than pre-filtering; prefer recent and maintained, and flag anything abandoned.
- A result table with one row per candidate and these columns: **name · link · one-line description · who makes it · license or price · last activity · rough popularity · how it is similar · how it differs · evidence link**.
- Raw findings and links, not a final verdict. The main agent decides.

## 3. Merge, rank, select

Merge and de-duplicate the candidates. Rank by closeness to the core capability first, then by maintenance, reach and license. Take only the top 3 for full profiles; keep the rest as a one-line longlist.

## 4. Profiles

For each of the top candidates write a short profile: name and link, one sentence, who is behind it, what problem it solves exactly, form and platform, license or price, maturity and last activity, reach, and its closeness to our idea.

## 5. Compare

Against our idea, lay out:

- **Similarities** — what it already does the same way.
- **Differences** — dimension by dimension: core function, audience, scope, openness/license, price, platform, maturity, extensibility, philosophy.
- **Gaps** — what none of them covers.

## 6. Verdict

Take a clear stance and give a recommendation:

- Nearly identical and healthy → use it, or contribute upstream.
- Partial overlap → build a deliberate niche, or reuse it as a building block.
- Nothing comparable → green light to build.
- Anything close but abandoned → say so and explain the trade-off.

State your confidence and what would change the answer.

## Output

- Report in the language the user is using in the conversation.
- Chat only. Do not create a file unless the user asks for a report.
- Always link sources. No profile without a link.
