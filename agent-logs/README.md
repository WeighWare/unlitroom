# Agent logs

Status: Active<br>
Owner: Bot HQ maintains; Daniel approves changes by merging<br>
Started: 2026-10-09

This is the canonical, company-neutral version, kept in `WeighWare/agent-rules`. Each opted-in repo carries a copy at its own agent-logs path (named in that repo's AGENTS.md), synced from this file by `agent-rules sync`. Do not edit a repo copy by hand; propose the change here.

This folder makes agent work traceable across Daniel's agents: Claude (Claude Code and Claude Cowork), Codex, Grok Bot, and Cursor. Each agent leaves one short entry per task, so any agent, or Daniel, can see who did what, where, and what was deliberately left alone.

## Layout

- `grok/`: Grok Bot entries.
- `claude/`: Claude entries.
- `codex/`: Codex entries.
- `cursor/`: Cursor cloud and local agent entries (a pointer to the PR is enough when the PR body carries the handoff manifest).
- `_template.md`: copy this to start an entry.

Use one folder per agent and one entry per agent per task. Filename: `YYYY-MM-DD-<task-slug>.md` in the agent's folder, lowercase kebab-case.

## Pointer entries

Some agents already keep per-task records elsewhere in the repo, such as review packets, execution records, run logs or handoff notes. Those records stay where they are. The agent-logs entry is then a short pointer: the repo-relative path of the record plus a one-line summary. History is not relocated, and no backfill is required. Claude and Codex records stay in their lanes (`claude/` and `codex/`), with pointers here when another agent did the work.

## Record format

Each entry is Markdown with a small YAML front-matter block, then five short sections, 5 to 15 lines of body in total.

Front-matter fields:
- `agent`: grok, claude, codex, or cursor
- `bot`: the named bot or session role
- `date`
- `task_slug`
- `repo`
- `systems_touched`: each system with its object IDs, such as commits, issue keys, CRM record IDs, Front conversation IDs or Drive file IDs
- `status`: done, partial or blocked

Sections:

1. Task as understood
2. Read
3. Changed (files, systems, record IDs)
4. Chose not to do and why
5. Open questions for Dan

Raw transcript content and local-only material never go into an entry. Use repo-relative paths only, never machine or workspace paths.

## Rules

- **Commit trailers.** Every agent commit carries an `Agent: <agent>/<bot>` trailer and an `Agent-Record: <path>` trailer pointing to its entry.
- **Bot authors.** Agent commits use a bot author: `Claude (agent) <claude@agents.invalid>`, `Codex (agent) <codex@agents.invalid>`, `Grok Bot (<bot name>) <bot-hq@agents.invalid>`, or `Cursor Agent <cursoragent@cursor.com>` (Cursor's default). That default is approved except on the repos in the next bullet.
  - On rgl8r/platform, and on any repo where only GitHub App identities are allowed as commit authors, the only allowed agent author is the GitHub App noreply identity, `<slug>[bot] <<id>+<slug>[bot]@users.noreply.github.com>`.
  - Existing tool trailers (for example `Claude-Session` or `Co-Authored-By`) may stay alongside these, unless a repo blocks them.
  - Past commits are not rewritten.
- **Read first.** Before starting work in an area, read the latest agent-logs entries for that area. Search entries by path, system or task slug.
- **Front.** Only where the system is used, bot actions in Front carry an `agent` tag and an internal comment saying which bot acted and why. The bot's agent-logs entry or action log lists those conversation IDs.
- **Bot register.** Bots are listed in the repo's bot register (path named in its AGENTS.md). Update the register before any bot is added or changed, not after.
- **Rule files.** `AGENTS.md`, `CLAUDE.md`, this README and any routing registry change only by a commit carrying the `Agent-Record` trailer, or by Daniel.

## Maintenance

- **Monthly rollup.**
  - Entries older than 90 days are rolled up into one summary file per agent per month at `<agent>/rollups/YYYY-MM.md`.
  - The originals move to `<agent>/archive/YYYY-MM/`. Entries are moved, never deleted.
- **Weekly check, Fridays.**
  - Codex compares the past week's agent commits (by `Agent` trailer or bot author) and Grok action logs against agent-logs entries, plus Front `agent` tags only where the system is used.
  - It flags missing records, records without matching commits or actions, and rule violations (em dashes, machine or workspace paths, any send without recorded approval).
  - It writes its own entry in `codex/`. Claude reviews the readout in `claude/`, and Bot HQ's Bot Auditor reads the result.
- **Monthly ten-record audit, first Friday of the month.**
  - Codex samples 10 agent-logs entries and checks each one against Git, and against Front and HubSpot only where the system is used: did the commits, tags, comments and record changes it claims actually happen, and nothing more?
  - Claude reviews the readout, and both write-ups are entries addressed to Daniel.

This is discipline, not enforcement: no hook blocks a commit for a missing record. The weekly check and the monthly audit are how gaps get found.
