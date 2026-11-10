# CLOUD-PREP-t2076 3-4 checkpoint

Repo: WeighWare/unlitroom
Base: main @ 1705fc59bb6f36e93133f17de1248cf7e8c27eb3
Branch: cursor/html-wellformed-ci-5c15
Kind: draft PR only. Do not mark ready. Do not merge. Do not deploy.

## Conditions in force

- `on: pull_request` only. No `push`. No `schedule`.
- `permissions: contents: read`
- `timeout-minutes: 5`
- `concurrency` group `${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true`
- Every action pinned by full commit SHA. No unpinned `npx` or `pip`.
- Stdlib `html.parser` well-formedness check. No site copy changes. Pages untouched.
- `chmod -x` only the two `*.cursor.co-author` hooks. `commit-msg.cursor` left untouched. Plain `git commit`.

## Log

1. Session start. Removed the execute bit from `commit-msg.cursor.co-author` and `prepare-commit-msg.cursor.co-author`. Left `commit-msg.cursor` executable. Confirmed `pages-build-deployment` (id 320484548) is the only workflow and left it unchanged. Checkout pin `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` is tag `v7.0.1`.
2. Checkpoint written before any workflow or checker edit.
3. Added `scripts/check_html.py` (stdlib `html.parser` only) and `.github/workflows/html-wellformed.yml` (`pull_request` only, `contents: read`, `timeout-minutes: 5`, concurrency with cancel-in-progress, checkout pinned by SHA). No setup-python, no npx, no pip. No site copy edits. Pages workflow not modified.
4. Local check: `python3 scripts/check_html.py` passed for `index.html`, `privacy.html`, and `terms.html`. Negative fixtures (missing doctype, unclosed element, mismatched end tag, void end tag, missing head, duplicate body, text after `</html>`, self-closed non-void, empty file) failed as intended. CI result is reported on the draft PR after the single push, so this file is not updated again just to record that run.
