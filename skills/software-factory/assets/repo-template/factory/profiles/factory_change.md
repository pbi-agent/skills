# Profile · factory_change

**Use when:** Change to factory itself: stages, profiles, checks, rules, templates, tooling.

**Risk floor:** high · **PR prefix:** `factory:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. This profile adds:

| Check           | Stage     | Can be n/a | Proves                                                   |
| --------------- | --------- | ---------- | -------------------------------------------------------- |
| `factory_check` | 03-build  | no         | factoryctl check and the factoryctl test suite pass      |
| `dry_run_task`  | 05-verify | no         | a sample task ran through the changed factory end to end |

`factory.yaml` is source for this table; `factoryctl accept` enforces it.

## Stage notes

- Filed by retro or human. Runs on `factory/` branch created with `factoryctl new --factory-change`.
- Triage: cite tasks that show problem. One task is anecdote unless it was rollback.
- Build: `factoryctl check` and factoryctl tests pass (`factory_check`). Bump `TEMPLATE_VERSION` when skeleton changes; always bump `factory.version`.
- Verify: run sample task end to end through changed factory (`dry_run_task`).

## Escalation hints

- Always high risk; human merges (CODEOWNERS).
- Any change loosening gate, check or limit must say so in PR's first line.
