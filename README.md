# The Unlit Room

This repository is the public website for The Unlit Room. It is a GitHub Pages site. The pages are static HTML. There is no build step, package manager, or application server.

## How it is published

GitHub Pages serves the default branch. A push to `main` is what publishes. Pull requests do not publish.

- Source branch: `main`
- Source folder: `/` (legacy Pages, the repository root)
- Live site: https://weighware.github.io/unlitroom/
- Workflow: GitHub's `pages-build-deployment`. There is no workflow file in this repo. GitHub runs that workflow on a push to `main`.

Do not change the Pages source, custom domain, or visibility from a content edit.

## Files an agent edits

- `index.html` is the landing page
- `privacy.html` is the privacy policy
- `terms.html` is the terms of service
- `icon.png` is the site icon

Change those files on a branch and open a pull request. After the pull request is merged to `main`, Pages deploys the repository root as the site.

## Agents

When `AGENTS.md` and `CLAUDE.md` are on the branch, read them before changing this repo. Those files carry the shared agent rules (stamp v2026.10.10) from WeighWare/agent-rules pull request #1, which is not merged. Do not merge your own pull request.
