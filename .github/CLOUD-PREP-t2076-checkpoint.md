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
