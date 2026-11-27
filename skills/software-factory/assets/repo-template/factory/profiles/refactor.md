# Profile · refactor

**Use when:** Structure changes, behavior does not.

**Risk floor:** medium · **PR prefix:** `refactor:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. Profile adds:

| Check                | Stage     | Can be n/a | Proves                                                           |
| -------------------- | --------- | ---------- | ---------------------------------------------------------------- |
| `behavior_unchanged` | 03-build  | no         | tests untouched and green, or characterization tests added first |
| `perf_baseline`      | 05-verify | yes        | no regression against the recorded baseline                      |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Plan: name behavior that must not change and tests that pin it. If coverage is thin, add characterization tests first.
- Build: do not edit existing tests in same commit as code they test.
- Review: any behavior change is `major` finding.
- Verify: compare against performance baseline.

## Escalation hints

- Module boundaries move → `architecture`.
- Public signature changes → `public_api`; no longer a pure refactor.
