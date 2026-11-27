# Profile · docs

**Use when:** Documentation only. No behavior change.

**Risk floor:** low · **PR prefix:** `docs:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. This profile adds:

| Check          | Stage    | Can be n/a | Proves                    |
| -------------- | -------- | ---------- | ------------------------- |
| `links`        | 03-build | no         | no broken links           |
| `style`        | 03-build | yes        | style and lint rules pass |
| `examples_run` | 03-build | yes        | code examples execute     |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Build: links resolve, style passes, examples run.
- Verify: read rendered preview, not source.

## Escalation hints

- Docs describing behavior code does not have → feature or bug; reclassify.
- Public commitments (SLA, pricing, legal text) → `product_scope`.
