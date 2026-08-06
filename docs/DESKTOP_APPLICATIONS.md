# File Tunnel desktop applications

Verified **2026-08-06**.

## Required pair

- Rust: [`file-tunnel/ftnl-desktop.rs`](https://github.com/file-tunnel/ftnl-desktop.rs) — **planned**, not yet verified as published.
- Flutter: [`file-tunnel/ftnl-flutter`](https://github.com/file-tunnel/ftnl-flutter) — **planned**, not yet verified as published.

These names supersede the earlier `file-tunnel-desktop.rs` and `file-tunnel-flutter` proposals. Do not mark either implementation live until the remote, native build, packaging, tests, and platform matrix are verified.

## Rust desktop kit: GPUI, fully native

The Rust application uses **GPUI** with no embedded WebView.

Rust owns transfer/session state, encryption and integrity, authentication, filesystem access, resumability, bandwidth control, persistence, deep-link parsing, and privileged operations. GPUI owns native presentation, virtualized queues, progress rendering, keyboard navigation, drag/drop surfaces, tray windows, and low-latency interaction.

The future Rust repository must contain `docs/DESKTOP_TOOLKIT.md` covering the GPUI version policy, no-WebView rule, transfer/security boundary, native integrations, performance budgets, deep-link contract, packaging matrix, and Flutter companion.

## Parallel Rust and Flutter development

Both applications are first-class implementations developed against the same product features. They exist to compare native performance and integration against Flutter portability/mobile reuse, accessibility, developer velocity, packaging, security, and long-term maintenance.

Every desktop-facing feature must inspect both repositories, share acceptance criteria and fixtures, and normally update both. A one-sided change requires an explicit no-change rationale and parity gap. The future `ftnl-desktop.rs` README, `AGENTS.md`, pull-request template, and `docs/DESKTOP_TOOLKIT.md` must state this rule prominently.

## HTTPS-first deep links

Canonical route family:

```text
https://<verified-file-tunnel-owned-host>/open/<route>?<bounded-query>
```

Fallback scheme:

```text
ftnl://<route>?<bounded-query>
```

Rust and Flutter must consume the same versioned route types and fixtures from the File Tunnel interfaces package.

Required behavior:

- cold-start and already-running/single-instance delivery;
- exact host, route/version, transfer/share identifier, action, and bounded-query validation;
- browser fallback when the app is absent;
- authenticated resume after sign-in;
- replay, expiry, tenant/recipient, and unsafe-return validation;
- explicit confirmation before accepting, importing, overwriting, or opening transferred files; and
- macOS, Windows, Linux, Android, and iOS tests.

URLs may carry only bounded identifiers or short-lived, single-use, audience-bound handoff codes. File bytes, filesystem paths containing private data, passwords, bearer tokens, encryption keys, transfer secrets, and credentials are prohibited in URLs.

## Product boundary

Both implementations should converge on:

- tray state and notifications;
- drag/drop and filesystem integration;
- share creation and recipient approval;
- resumable transfers and integrity verification;
- progress, bandwidth, pause/resume/cancel, and retry behavior;
- secure clipboard links and browser fallback;
- transfer history, audit receipts, schemas, manifests, fixtures, and network-failure conformance tests.

## Project routing

- GitHub Project: [`file-tunnel-project` — Project 1](https://github.com/orgs/file-tunnel/projects/1)
- Linear project: `github.com/file-tunnel`
- Central registry: [`desktop-applications.json`](https://github.com/ORESoftware/project-registry/blob/main/registry/desktop-applications.json)
- Toolkit strategy: [`rust-desktop-strategies.md`](https://github.com/ORESoftware/project-registry/blob/main/docs/rust-desktop-strategies.md)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, toolkit changes, deep-link changes, renames, transfers, archival, or platform-status changes must update this document, Linear, the central registry/strategy, and both companion repositories together.
