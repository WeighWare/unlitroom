# CLAUDE.md

@AGENTS.md

Read `AGENTS.md` (imported above) before acting. The hard rules are repeated below so they still apply if the import fails silently.

<!-- agent-rules claude-inline v2026.10.10 BEGIN -->
## Hard rules (inline copy)

1. Nothing is sent, shared, scheduled, or delivered as Daniel without his yes to that exact message and recipient. One yes covers one send; any edit needs a new yes. Draft by default.
2. No em dashes.
3. No machine paths, workspace paths, or box paths in anything that leaves the repo.
4. Raw transcripts stay local.
5. Fix the source of truth first, then rebuild.
6. Merges need Daniel's one-tap yes on that exact head. A new push needs a new yes. No agent merges its own work. Exception: Unlit auto-merge on `WeighWare/openclaw-content-machine` after a cross-family pass at that head, green checks, and a clean non-draft PR. If the author models cannot be established, it still needs the one-tap. The merge record names the author and models, the reviewer, the head SHA, the checks, and who merged.
7. Cross-family review before a merge. Families: Grok, GPT/Codex, Claude, Gemini; each open-weights maker is its own. Auto and Composer do not count. Versions of one family never review each other.
8. Never commit as Daniel. Use a bot author with `Agent:` and `Agent-Record:` trailers. On rgl8r/platform, and on any repo where only GitHub App identities are allowed as commit authors, use only the GitHub App noreply identity. Elsewhere, Cursor's default commit author is approved.
9. Preserve unrelated uncommitted work; stage only your own files by explicit path.
10. Never delete an unpushed branch or discard local commits. Push it to `wip/<name>` first. Deleting it after that needs Daniel's yes.
11. Never touch `.git` lock files.
12. Code changes go out as cloud-agent pull requests. Agent-logs records may be committed locally for Daniel to push. `agent-rules sync --apply` may commit locally and never pushes. Never push as Daniel. In a CallCorp repo, a local commit needs his yes for that action.
13. Never print or copy keys or tokens, including encoded copies. No secrets in files, commits, logs, or messages. A check reports only whether a value is set.
14. No API keys for Claude or Codex CLI runs. Plan sign-in only: no `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper`, `CODEX_API_KEY`, or `OPENAI_API_KEY`, and no `--bare`.
15. CallCorp data stays on the CallCorp laptop. Do not read, copy, or commit CallCorp or Simple.CX content anywhere else.
16. Checked recommendations that cost money, or that change infrastructure, machines, accounts, or direction, need facts from the real source and a different-family review before Daniel is asked to approve. Otherwise label it "first take, not yet checked".
<!-- agent-rules claude-inline v2026.10.10 END -->

## Repo-specific

Owned by this repo. `agent-rules sync` never touches anything below the END marker.

- none. Publishing notes are in the AGENTS.md Repo-specific section and in README.md.
