# Contributing

1. Read the target repository's README, agent instructions, and local contribution guide.
2. Open focused changes with tests or an explicit verification plan.
3. Preserve public APIs, data formats, and operational behavior unless the change intentionally migrates them.
4. Keep generated files reproducible and identify their source.
5. Never resolve conflicts by blindly choosing "ours" or "theirs". Inspect the base, both branches, nearby history, tests, and downstream consumers; then construct the smallest coherent combined result.
6. Do not commit credentials, private keys, tokens, production data, or personal information.

## AI-assisted pull-request promotion

This policy applies to AI agents and AI-assisted automation. Repository-specific rules may be stricter and take precedence.

An AI agent may merge only when all of the following are true:

1. All required status checks and all relevant tests pass on the exact commit to be merged.
2. The source branch is current with its target, and there are no merge conflicts.
3. There are no unresolved review threads, requested changes, missing required approvals, or known security, privacy, compliance, or data-integrity blockers.
4. The change matches the approved issue and pull-request scope, and compatibility, migration, observability, and rollback implications are understood.
5. The AI records an exact confidence percentage and a concise evidence-based rationale in the pull request.

Confidence is an additional gate, not a substitute for tests, reviews, approvals, or branch protection. Never bypass protections, force-merge, dismiss valid reviews, or represent a skipped, cancelled, neutral, stale, or failing check as passing.

### Exact-tree and base-freshness evidence

PR-head CI is necessary but is not sufficient when the target branch can move before a squash or merge commit is created.

- The tested PR head must contain the **live target tip** immediately before merge. Protected production branches should require branches to be up to date before merging.
- A successful workflow with no executed jobs or steps is not validation evidence. Treat zero-step, startup-failure, skipped, cancelled, neutral, or stale results as non-passing.
- Record the exact tested head SHA and, after merge, the resulting Git tree SHA. If the merge tree differs from the tested PR-head tree, require successful validation on the exact merged SHA before treating the merge as qualified.
- If the source organization cannot execute Actions because of minutes/budget or runner exhaustion, use a reviewed private carrier in an organization with available capacity. Re-create the **exact source Git tree**, verify the destination root tree SHA equals the source tree SHA, and run the carrier with its own token/minutes.
- Never give the carrier a token or secret that can read the private source repository. Transfer content-addressed Git objects through the authorized control plane, keep source secrets out of the carrier, and bind evidence to the source tree SHA, carrier commit SHA, workflow run attempt, jobs, and executed steps.

### Feature branch to `dev`

When every gate above passes and the AI's calibrated confidence that the feature is correct, complete, and safe is **strictly greater than 99.1%**, retarget the pull request if necessary and merge it into `dev`, the integration branch.

If confidence is 99.1% or lower, cannot be calibrated, or depends on an unresolved assumption, leave the pull request open and request human review. If the repository has no `dev` branch, do not invent a substitute or merge to production; establish `dev` or follow a stricter repository-specific integration-branch policy first.

### `dev` to `main` or `master`

When every gate above passes for the exact `dev` head commit, all release-level tests pass, and the AI's calibrated confidence that the integrated result is production-ready is **strictly greater than 99.7%**, open or update the promotion pull request and merge `dev` into the repository's production branch: `main` when that is the production branch, otherwise `master`.

If confidence is 99.7% or lower, leave the promotion pull request open and request human review. Do not merge a feature branch directly into `main` or `master` under this confidence policy.

### Confidence discipline

The confidence assessment must account for test relevance and coverage, review findings, security and privacy risk, backward compatibility, data migrations, deployment behavior, observability, and rollback readiness. Do not round up to cross a threshold. Any material unknown or unverifiable assumption keeps confidence below the applicable threshold.

### Merge record

Use the repository's permitted merge method. Re-evaluate all gates whenever the head SHA changes. In the pull request, record the source and target branches, tested SHA, check results, confidence percentage, and rationale before merging.

<!-- ore-org-baseline:begin -->
Thank you for contributing to repositories owned by [`file-tunnel`](https://github.com/file-tunnel). Repository-local instructions take precedence when they are stricter.

## Before proposing a change

1. Read the repository README, contribution notes, lowercase `agents.md`, architecture documentation, linked issues, and relevant [Linear project](https://linear.app/denman/project/githubcomfile-tunnel-f46884af1012).
2. Confirm the authoritative source repository and whether files are generated, vendored, mirrored, or owned by another repository.
3. Fetch current remote state and preserve concurrent work. Avoid git rebase in favor of git merge.
4. Do not use `git stash`, `git reset`, `git clean`, `git filter-repo`, force-push, destructive worktree/submodule operations, or broad deletion/rewrite commands without exact authorization.
5. Never include secrets, credentials, customer data, legal records, or other private information in issues, commits, test fixtures, screenshots, or logs.

## Pull requests

Use a focused feature branch and a draft pull request. Link the relevant issue or Linear work; explain behavior, risk, security impact, migration and rollback considerations, tests, and cross-repository dependencies. Resolve conflicts semantically with full context—normally including the merge base and 3–10 relevant commits—rather than selecting one side wholesale. Run all affected checks and scan the complete worktree for conflict markers.

External GitHub Actions must be pinned to full commit SHAs. Workflows must use explicit least-privilege permissions, explicit timeouts, and non-persisted checkout credentials.
<!-- ore-org-baseline:end -->

## Rust-first scripts and automation

**Do not add Python scripts. Use Rust for first-party automation**, including CI/build/test helpers, code generators, database and infrastructure migrations, audits, release/deployment tasks, and repository maintenance. Prefer maintainable Rust CLIs or `cargo xtask` tasks; shell/YAML may be used as thin wrappers when unavoidable.

**Existing Python automation is migration debt** and must not be deleted before equivalent Rust functionality is proven. Record all callers and usage, preserve arguments and exit codes, error handling, formats, security properties and supported platforms, and demonstrate positive/negative regressions plus real CLI/workflow smoke tests on the exact changed head. Policy documentation does not imply scripts were ported.

**Python application code remains an exceptional, reviewed use case** only when an accountable owner documents purpose, scope, rationale and review criteria. Application-specific tests can share a permitted exception; build/test automation, codegen and maintenance scripts cannot masquerade as app code.

New Rust tools should document reproducible Cargo workflows, including appropriate `cargo fmt --check`, `cargo clippy -- -D warnings`, `cargo test` and end-to-end checks. Never claim unexecuted or source-free checks establish functional coverage.

Canonical `.github` community-health/contributor guidance is not automatic GitHub inheritance for `AGENTS.md` or custom CI enforcement. Explicitly synchronize repo-local guidance and configure policy gates per repository as needed.

