# file-tunnel organization handbook

> Shared operating defaults for repositories maintained under **file-tunnel**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

file-tunnel maintains secure, reliable file-transfer, tunneling, client, server, and infrastructure software. This `.github` repository is the canonical home for shared policy, reusable templates, community health files, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported transports and platforms, development and test commands, authoritative protocol and metadata formats, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Transfer components should also document authentication and encryption, framing and chunking, integrity verification, resume semantics, ordering, backpressure, retries, quotas, expiration, deletion, observability, and degraded modes.

## Change workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, confidentiality and compatibility risk, validation, migration, and rollback.
4. Test empty, large, corrupt, interrupted, resumed, duplicated, reordered, expired, unauthorized, overloaded, and partial-failure paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves auditability.

## Evidence, security, and documentation

Pull requests should include reproducible commands, synthetic fixtures, expected and observed checksums and transfer states, negative-path and load evidence, documentation updates, and CI or local-equivalent results. Never commit credentials, private keys, production files, or sensitive logs. Follow `SECURITY.md` for private reporting. Keep trust boundaries, limits, protocol compatibility, retention, deletion, and important security and operational decisions explicit.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profiles, descriptions, topics, and READMEs are current.
- [ ] Community health files and reusable issue/PR guidance are present.
- [ ] Authentication, encryption, integrity, resume, limits, expiry, deletion, and recovery are documented.
- [ ] Required checks cover corruption, interruption, authorization, load, compatibility, and supply-chain risk.
- [ ] Stale repositories are archived or clearly marked.
- [ ] GitHub Project and Linear links resolve and reflect completed work.
