# Profile · data_migration

**Use when:** Change stored data or its schema.

**Risk floor:** high · **PR prefix:** `migration:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. This profile adds:

| Check             | Stage     | Can be n/a | Proves                                                            |
| ----------------- | --------- | ---------- | ----------------------------------------------------------------- |
| `backup_verified` | 05-verify | no         | a restore from the backup was tested                              |
| `dry_run_on_copy` | 05-verify | no         | migration ran on a copy of production data; row counts reconciled |
| `rollback_script` | 03-build  | no         | down-migration exists and is tested                               |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Plan: forward and backward path; expected row counts; how long writes are affected.
- Build: down-migration exists and is tested (`rollback_script`).
- Verify: run on copy of production data, reconcile counts (`dry_run_on_copy`); restore backup once (`backup_verified`).

## Escalation hints

- Always high risk; `data_model` is set automatically from migration paths.
- Migration without backward path → `irreversible`.
