# Profile · dependency_update

**Use when:** Upgrade, add or remove third-party dependency.

**Risk floor:** low · **PR prefix:** `deps:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. Profile adds:

| Check            | Stage    | Can be n/a | Proves                                              |
| ---------------- | -------- | ---------- | --------------------------------------------------- |
| `changelog_scan` | 03-build | no         | upstream changelog read; breaking changes listed    |
| `license_check`  | 03-build | no         | licenses of new or changed dependencies are allowed |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Triage: read upstream changelog between the two versions. List breaking changes.
- Plan: one dependency (or one coherent group) per task.
- Build: lockfile changes only from package manager, never by hand.
- Verify: smoke-test features using the dependency.

## Escalation hints

- Adding dependency → `new_dependency` (set automatically from manifest files).
- Major version jump or license change → raise risk; `cost_or_license` for license change.
