# File Tunnel desktop applications

Verified **2026-08-09**.

## Required pair

- Rust: [`file-tunnel/ftnl-desktop-app.rs`](https://github.com/file-tunnel/ftnl-desktop-app.rs) — **published**; native source, Nix, and Linux/macOS/Windows CI verified at `c8da8e9f89bfd04c57160f29a44aa0416d430a71`.
- Flutter: [`file-tunnel/ftnl-flutter`](https://github.com/file-tunnel/ftnl-flutter) — **planned**, not yet verified as published.

The Rust receiver complements rather than replaces the planned Flutter app. Do
not mark Flutter live until its remote, native build, packaging, tests, and
platform matrix are verified.

## Rust desktop kit: egui/eframe, fully native

The Rust application uses **egui/eframe** with no embedded WebView.

Rust owns transfer/session state, integrity checks, authentication, filesystem
access, safe atomic persistence, and privileged operations. The egui host owns
native presentation and delegates reusable render state to
`ftnl-ui-components`. The current protocol supports snapshot reconciliation but
does not yet claim byte-offset download resume.

The Rust repository README documents its no-WebView rule, transfer/security
boundary, native integration, validation matrix, and Flutter companion. Future
packaging and deep-link work must preserve those boundaries.

## Parallel Rust and Flutter development

Both applications are first-class implementations developed against the same product features. They exist to compare native performance and integration against Flutter portability/mobile reuse, accessibility, developer velocity, packaging, security, and long-term maintenance.

Every desktop-facing feature must inspect both repositories, share acceptance
criteria and fixtures, and normally update both. A one-sided change requires an
explicit no-change rationale and parity gap. The `ftnl-desktop-app.rs` README,
agent instructions, and pull-request template must state this rule prominently.

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
- Central registry: approved private portfolio registry (opaque internal locator; no private repository URL is committed here)
- Toolkit strategy: approved private desktop strategy (opaque internal locator; no private repository URL is committed here)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, toolkit changes, deep-link changes, renames, transfers, archival, or platform-status changes must update this document, Linear, the central registry/strategy, and both companion repositories together.
