# Profile · performance

**Use when:** Make something measurably faster or cheaper.

**Risk floor:** medium · **PR prefix:** `perf:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. Profile adds:

| Check                    | Stage     | Can be n/a | Proves                                                 |
| ------------------------ | --------- | ---------- | ------------------------------------------------------ |
| `benchmark_before_after` | 03-build  | no         | same benchmark, before and after, same hardware        |
| `load_test`              | 05-verify | yes        | target load sustained in a production-like environment |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Intake: criteria carry numbers — metric, target, workload.
- Build: same benchmark before and after, same hardware, at least 5 runs each; report spread.
- Verify: load test in production-like environment.

## Escalation hints

- Caching or concurrency changes behavior under failure → raise risk.
- Trading correctness or cost for speed → `design_tradeoff`.
