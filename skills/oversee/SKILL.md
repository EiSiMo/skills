---
name: oversee
description: Watch a long-running job on this machine — a database backfill, thousands of AI prompts, a long computation. Starts it as a systemd service if it is not running, checks it on a fixed schedule, investigates problems with subagents, applies only no-brainer fixes and restarts, otherwise stops the job and writes a report with the options. Protects already computed data above all. Use when the user invokes "oversee" or asks to babysit, supervise or watch over a long-running process.
---

# Oversee

## Data first

Already computed data must never be put at risk. Copy these rules verbatim into every subagent brief:

- Never delete, overwrite, truncate or move produced output.
- Stop gracefully (SIGTERM, wait), never SIGKILL first.
- Restart only if the job resumes without redoing or duplicating finished work.
- A fix must not change how results are produced (prompt, model, logic, schema).
- Back up the latest output state before a fix touches code that writes data.
- When unsure, treat it as a hard decision.

## Helper

Use `scripts/oversee` (next to this file): `start`, `adopt`, `check`, `stop`, `restart`, `note`, `list`. Run it without arguments for usage. State, logs and journal go to `/tmp/oversee/<name>/`.

Nothing goes into the project folder. Extra helper scripts, backups and the report go into `/tmp/oversee/<name>/`. The only project changes allowed are fixes to the job's code.

## 1. Understand

Before watching, know: the command, where results go, whether it resumes after a restart, what "done" and what healthy (rate, normal error noise) look like. Find a read-only command that prints progress as one number and pass it as `--progress`. Ask the user only what you cannot find out.

## 2. Start or adopt

- Running → `oversee adopt`. Do not restart it.
- Not running → `oversee start` (systemd user unit).

## 3. Schedule

Check at now, +5, +10, +20 min, then every 30 min. After any crash, fix or restart, start the schedule over. Never wait in the foreground between checks.

## 4. Check

Run `oversee check` and judge it, including a look at the newest results. Silent garbage counts as a failure.

- Healthy → one line to the user.
- Finished → verify completeness, write the report, stop.
- Problem → if it is damaging data or burning money, stop it first. Then investigate.

## 5. Investigate

A read-only subagent finds root cause with evidence, a concrete fix, and whether a restart resumes safely. You decide:

- **No-brainer** — cause certain, fix small and reversible, results unchanged, restart resumes cleanly. A fix subagent applies it without restarting anything. Review the diff, then restart.
- **Hard** — everything else, and any problem that comes back after a fix. Stop the job, stop watching, write the report.

At most three automatic fixes per session.

## 6. Report

`/tmp/oversee/<name>/report.md`, in the user's language: status, how much data is done and what is safe or suspect, timeline, the problem, the options with their risks, your recommendation, the exact commands to resume.
