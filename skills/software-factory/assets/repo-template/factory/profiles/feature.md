# Profile · feature

**Use when:** New user-visible or API-visible behavior.

**Risk floor:** medium · **PR prefix:** `feat:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. Profile adds:

| Check              | Stage     | Can be n/a | Proves                                              |
| ------------------ | --------- | ---------- | --------------------------------------------------- |
| `acceptance_tests` | 03-build  | no         | automated test per acceptance criterion             |
| `docs_updated`     | 03-build  | yes        | user and developer docs match the new behavior      |
| `ux_check`         | 05-verify | yes        | user flow walked through in the preview environment |

`factory.yaml` is source for this table. `factoryctl accept` enforces it.

## Stage notes

- Intake: criteria describe behavior requester can observe. Ask rather than assume.
- Triage: confirm with requester that goal and criteria are right before planning — wrong criterion passes every later check.
- Plan: one automated acceptance test per criterion. Include docs.
- Verify: walk user flow in preview environment (`ux_check`).

## Escalation hints

- Any change to existing behavior → `product_scope`.
- New endpoint or changed contract → `public_api`.
