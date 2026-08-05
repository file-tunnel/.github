<!-- ore-org-baseline:begin -->
# Repository relationships for `file-tunnel`

This file is rendered from `repository-relationships.json`. The JSON registry is authoritative.

- Audience: `public`
- Repositories represented: **11**
- Relationships represented: **16**
- Inventory digest: `sha256:2916f802723122d7e756a4a2afabd75d4125d544bbcd3f946885e6e93b04720b`

## Immutable routing identity

| Field | Value |
|---|---|
| Mapping ID | `context:file-tunnel` |
| GitHub owner ID | `310631493` |
| Linear project ID | `0cb3346d-19e0-4aff-8758-c5d5a4a1ed80` |
| Linear team ID | `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |

## Repositories

| Repository | Visibility | Roles | Archived |
|---|---|---|---|
| `file-tunnel/.github` | `public` | `community-health`, `governance`, `relationship-registry` | no |
| `file-tunnel/file-tunnel.github.io` | `public` | `documentation-site` | no |
| `file-tunnel/ftnl-backend-api.rs` | `public` | `api-server` | no |
| `file-tunnel/ftnl-clients` | `public` | `clients` | no |
| `file-tunnel/ftnl-e2e` | `public` | `end-to-end-tests` | no |
| `file-tunnel/ftnl-infra` | `public` | `infrastructure` | no |
| `file-tunnel/ftnl-interfaces` | `public` | `interfaces` | no |
| `file-tunnel/ftnl-monorepo` | `public` | `monorepo` | no |
| `file-tunnel/ftnl-sync` | `public` | `sync` | no |
| `file-tunnel/ftnl-ui-components` | `public` | `repository` | no |
| `file-tunnel/ftnl-web-server.rs` | `public` | `web-server` | no |

## Relationships

| From | Type | To | Status | Required |
|---|---|---|---|---|
| `file-tunnel/.github` | `governs` | `file-tunnel/file-tunnel.github.io` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-backend-api.rs` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-clients` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-e2e` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-infra` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-interfaces` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-monorepo` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-sync` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-ui-components` | `declared` | yes |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-web-server.rs` | `declared` | yes |
| `file-tunnel/file-tunnel.github.io` | `documents` | `file-tunnel/.github` | `inferred` | no |
| `file-tunnel/ftnl-clients` | `depends_on` | `file-tunnel/ftnl-interfaces` | `inferred` | no |
| `file-tunnel/ftnl-e2e` | `tests` | `file-tunnel/ftnl-monorepo` | `inferred` | no |
| `file-tunnel/ftnl-infra` | `deploys` | `file-tunnel/ftnl-monorepo` | `inferred` | no |
| `file-tunnel/ftnl-sync` | `depends_on` | `file-tunnel/ftnl-interfaces` | `inferred` | no |
| `file-tunnel/ftnl-web-server.rs` | `depends_on` | `file-tunnel/ftnl-interfaces` | `inferred` | no |

## Editing relationships

Put reviewed public declarations in `repository-relationships.manual.json`; do not edit the generated registry directly.
Private repository names and private-only relationships belong in the private `approved-private-registry` mirror.
Inferred edges are advisory and must remain visibly labeled until reviewed.
<!-- ore-org-baseline:end -->
