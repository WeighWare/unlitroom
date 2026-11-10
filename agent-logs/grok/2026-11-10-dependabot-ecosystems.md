# PM4 checkpoint — dependabot.yml

- Goal: Add `.github/dependabot.yml` only for ecosystems actually present (github-actions, plus the package manager in use), weekly, `open-pull-requests-limit: 5`, minor/patch grouped.
- Done-when: That file matches only those ecosystems, or this report if none are present. No settings, Pages, workflow, or other file changes.
- Blocking criteria: Do not invent an ecosystem. Do not edit workflows. If a workflow Dependabot pull requests would trigger is not already pull-request-only, name it in the PR body and leave the file unchanged.
- Size: 1

## Result

Premise is false. Nothing to configure.

Tree inspected at `1705fc5` (`origin/main`). Tracked files: `README.md`, `icon.png`, `index.html`, `privacy.html`, `terms.html`.

- Package manager: none. Scan for manifests and lockfiles (`package.json`, npm/pnpm/yarn locks, `requirements.txt`, `Pipfile`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `Gemfile`, `composer.json`, `pom.xml`, Gradle, `*.csproj`, `Package.swift`, `pubspec.yaml`, `mix.exs`, `Dockerfile`, any `*.yml`/`*.yaml`) returned 0 files.
- GitHub Actions: none. No `.github/` directory and no `workflows` directory.
- Existing `dependabot.yml`: none.

No `.github/dependabot.yml` added. No workflow fails the pull-request-only check, because the repo has no workflows.

## Tests

No test suite. `find` for `*test*` / `*spec*` outside `.git` returned 0 files.

Not run: unit, integration, lint, and build. There is no test runner or package script to invoke.
