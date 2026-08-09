# `file-tunnel` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **12**
- Private repository names withheld: **1**
- Relationship edges: **39**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/file-tunnel/.github) | `organization_governance` | `active` |
| [`ftnl-interfaces`](https://github.com/file-tunnel/ftnl-interfaces) | `interfaces` | `active` |
| [`ftnl-clients`](https://github.com/file-tunnel/ftnl-clients) | `client_sdk` | `active` |
| [`ftnl-backend-api.rs`](https://github.com/file-tunnel/ftnl-backend-api.rs) | `api_service` | `active` |
| [`ftnl-sync`](https://github.com/file-tunnel/ftnl-sync) | `sync_service` | `active` |
| [`ftnl-web-server.rs`](https://github.com/file-tunnel/ftnl-web-server.rs) | `web_bff` | `active` |
| [`ftnl-cli`](https://github.com/file-tunnel/ftnl-cli) | `cli` | `active` |
| [`file-tunnel.github.io`](https://github.com/file-tunnel/file-tunnel.github.io) | `site` | `active` |
| [`ftnl-infra`](https://github.com/file-tunnel/ftnl-infra) | `infrastructure` | `active` |
| [`ftnl-e2e`](https://github.com/file-tunnel/ftnl-e2e) | `end_to_end_tests` | `active` |
| [`ftnl-monorepo`](https://github.com/file-tunnel/ftnl-monorepo) | `composition_workspace` | `active` |
| [`ftnl-ui-components`](https://github.com/file-tunnel/ftnl-ui-components) | `uncategorized` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `file-tunnel/.github` | `governs` | `file-tunnel/file-tunnel.github.io` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-backend-api.rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-cli` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-clients` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-e2e` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-infra` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-interfaces` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-monorepo` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-sync` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-ui-components` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/.github` | `governs` | `file-tunnel/ftnl-web-server.rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `file-tunnel/ftnl-backend-api.rs` | `implements_contracts_from` | `file-tunnel/ftnl-interfaces` | `inferred` / `role-convention`: service boundary implements canonical contracts |
| `file-tunnel/ftnl-cli` | `calls` | `file-tunnel/ftnl-backend-api.rs` | `inferred` / `role-convention`: client uses the product service boundary |
| `file-tunnel/ftnl-clients` | `generated_from` | `file-tunnel/ftnl-interfaces` | `inferred` / `role-convention`: SDK bindings derive from canonical contracts |
| `file-tunnel/ftnl-e2e` | `tests` | `file-tunnel/file-tunnel.github.io` | `inferred` / `role-convention`: black-box compatibility verification |
| `file-tunnel/ftnl-e2e` | `tests` | `file-tunnel/ftnl-backend-api.rs` | `inferred` / `role-convention`: black-box compatibility verification |
| `file-tunnel/ftnl-e2e` | `tests` | `file-tunnel/ftnl-cli` | `inferred` / `role-convention`: black-box compatibility verification |
| `file-tunnel/ftnl-e2e` | `tests` | `file-tunnel/ftnl-sync` | `inferred` / `role-convention`: black-box compatibility verification |
| `file-tunnel/ftnl-e2e` | `tests` | `file-tunnel/ftnl-web-server.rs` | `inferred` / `role-convention`: black-box compatibility verification |
| `file-tunnel/ftnl-infra` | `deploys` | `file-tunnel/ftnl-backend-api.rs` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `file-tunnel/ftnl-infra` | `deploys` | `file-tunnel/ftnl-cli` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `file-tunnel/ftnl-infra` | `deploys` | `file-tunnel/ftnl-sync` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `file-tunnel/ftnl-infra` | `deploys` | `file-tunnel/ftnl-web-server.rs` | `inferred` / `role-convention`: product infrastructure declares runtime resources |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/file-tunnel.github.io` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-backend-api.rs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-cli` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-clients` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-e2e` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-infra` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-interfaces` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-sync` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-ui-components` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-monorepo` | `composes` | `file-tunnel/ftnl-web-server.rs` | `inferred` / `role-convention`: development workspace and release bill of materials |
| `file-tunnel/ftnl-sync` | `synchronizes_with` | `file-tunnel/ftnl-backend-api.rs` | `inferred` / `role-convention`: sync exchanges state through the product service boundary |
| `file-tunnel/ftnl-sync` | `uses_contracts_from` | `file-tunnel/ftnl-interfaces` | `inferred` / `role-convention`: sync payloads follow canonical schemas |
| `file-tunnel/ftnl-web-server.rs` | `calls` | `file-tunnel/ftnl-backend-api.rs` | `inferred` / `role-convention`: client uses the product service boundary |
| `organization://file-tunnel` | `reconciles_via` | `platform://opto-sync` | `platform-default` / `platform-policy`: product sync wraps the generic reconciliation engine |
| `organization://file-tunnel` | `deployed_via` | `platform://ORESoftware/k8s-cluster` | `platform-default` / `platform-policy`: immutable artifacts are promoted by digest through GitOps |
| `organization://file-tunnel` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
