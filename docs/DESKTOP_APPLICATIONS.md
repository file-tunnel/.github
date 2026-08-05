# Desktop application allocation

Verified **2026-08-05**.

File Tunnel is a **strong candidate** for paired native desktop transfer applications:

- Rust: [`file-tunnel/file-tunnel-desktop.rs`](https://github.com/file-tunnel/file-tunnel-desktop.rs) — **proposed**, not yet verified as a published repository.
- Flutter: [`file-tunnel/file-tunnel-flutter`](https://github.com/file-tunnel/file-tunnel-flutter) — **proposed**, not yet verified as a published repository.

These names are proposed allocation targets, not proof that either remote exists and not a claim that implementation is approved or complete. Promote the pair from proposed to planned only when scope, ownership, milestones, threat model, and repository creation are accepted in Linear.

## Product boundary

The pair should cover semantic parity for tray state, drag-and-drop intake, share creation, resumable transfers, progress and bandwidth controls, filesystem integration, notifications, secure clipboard links, authentication, encryption boundaries, retry/recovery, and transfer history.

A shared Rust transfer engine may sit behind an explicit library, FFI, or local-service boundary, but the Flutter application remains independently buildable, testable, and releasable. Shared schemas, transfer manifests, clients, fixtures, network-failure scenarios, golden receipts, and conformance tests should be versioned deliberately.

## Feature-delivery rule

Once planned, every desktop-facing change must inspect both implementations, define shared acceptance and security criteria, update both or record an explicit no-change rationale, and report Rust and Flutter status separately. Filesystem, clipboard, tray, and notification behavior must be verified per operating system.

## Project routing

- GitHub Project: [`file-tunnel-project` — Project 1](https://github.com/orgs/file-tunnel/projects/1)
- Linear project: `github.com/file-tunnel`
- Central registry: [`ORESoftware/project-registry`](https://github.com/ORESoftware/project-registry/blob/main/registry/desktop-applications.json)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Promotion, repository creation, renames, transfers, archival, or platform-status changes must update this document, Linear, the central registry, and both companion repositories together.
