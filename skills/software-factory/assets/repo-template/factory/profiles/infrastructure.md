# Profile · infrastructure

**Use when:** Change to environments, pipelines, cloud resources or deployment.

**Risk floor:** high · **PR prefix:** `infra:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. This profile adds:

| Check             | Stage     | Can be n/a | Proves                                                   |
| ----------------- | --------- | ---------- | -------------------------------------------------------- |
| `plan_diff`       | 03-build  | no         | infrastructure plan output attached and matches the plan |
| `dry_run`         | 05-verify | no         | applied successfully in a non-production environment     |
| `rollback_tested` | 05-verify | no         | rollback executed once in a non-production environment   |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Plan: attach expected plan output. Name what is destroyed or replaced.
- Build: `plan_diff` must match plan exactly; stop on unexpected resource change.
- Verify: apply in non-production (`dry_run`) and execute rollback once (`rollback_tested`).

## Escalation hints

- Always high risk.
- Anything that deletes data or cannot be recreated → `irreversible`.
- New paid service or larger instances → `cost_or_license`.
