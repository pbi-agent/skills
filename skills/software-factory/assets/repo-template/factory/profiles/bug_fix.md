# Profile · bug_fix

**Use when:** Something that worked, or was specified to work, does not.

**Risk floor:** low · **PR prefix:** `fix:`

## Checks

Baseline checks (`ci_green`, `secrets_scan`, `acceptance_proven`) always apply. This profile adds:

| Check              | Stage    | Can be n/a | Proves                             |
| ------------------ | -------- | ---------- | ---------------------------------- |
| `reproduce`        | 03-build | yes        | a test fails before the fix        |
| `fix_test`         | 03-build | no         | the same test passes after the fix |
| `regression_suite` | 03-build | no         | existing suite still green         |

`factory.yaml` is source for this table; `factoryctl accept` enforces it.

## Stage notes

- Triage: reproduce first. Unreproducible bug is `blocked` or `reject`, not a guess.
- Plan: fix cause, not symptom. Name the test failing today.
- Build: commit failing test before fix, so `reproduce` and `fix_test` are visible in history.
- Verify: replay original report's steps in staging.

## Escalation hints

- Fix needs schema or API change → flag it; task is no longer a small fix.
- Same bug class exists elsewhere → note it for follow-up task; do not widen this one.
