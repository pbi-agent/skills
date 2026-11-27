# Profile · security_fix

**Use when:** Close vulnerability or harden control.

**Risk floor:** high · **PR prefix:** `security:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. Profile adds:

| Check          | Stage     | Can be n/a | Proves                                 |
| -------------- | --------- | ---------- | -------------------------------------- |
| `exploit_test` | 03-build  | no         | the exploit fails after the fix        |
| `audit_log`    | 05-verify | yes        | the security-relevant action is logged |

`factory.yaml` is source for this table; `factoryctl accept` enforces it.

## Stage notes

- Embargo: if issue not public, branch, PR and task folder must live in private fork or advisory workspace until release. Orchestrator decides this before `factoryctl new`.
- Build: prove exploit fails after fix (`exploit_test`). Keep exploit details out of public commit messages.
- Review: check sibling code paths for same weakness.
- Verify: security-relevant action is logged (`audit_log`).

## Escalation hints

- Always high risk: human approves work, approach and going live.
- Changes to authentication or permissions → `security_model`.
