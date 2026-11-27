# Profile · test_coverage

**Use when:** Add or repair tests. No production code change.

**Risk floor:** low · **PR prefix:** `test:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. Profile adds:

| Check            | Stage    | Can be n/a | Proves                                    |
| ---------------- | -------- | ---------- | ----------------------------------------- |
| `tests_pass`     | 03-build | no         | new tests pass and are not flaky (3 runs) |
| `coverage_delta` | 03-build | yes        | coverage did not drop                     |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Build: new tests pass 3 times in a row; each fails when code under test is broken on purpose.
- Review: tests asserting nothing are `major` finding.

## Escalation hints

- Test reveals real bug → file `bug_fix` task; do not fix here.
- Production code must change to be testable → `refactor` as secondary type.
