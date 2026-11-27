# Stage 05 · Verify

**Role:** verifier. **Repo access:** read; deploy rights to non-production environment. **Input:** `02-plan.md`, `04-review.md`. **Output:** `05-verify.md`.

Orchestrator already brought branch up to date with `main`. Verify that exact commit.

## Do

1. Deploy head commit to production-like environment: staging, preview environment, or build preview for docs. Record environment and commit.
2. Prove every acceptance criterion there, one row per criterion, with link to proof.
3. Run every verify-stage check in brief (from plan's check table); fill evidence table. `acceptance_proven` always required.
4. Confirm release readiness: plan's rollback is executable, and watch signals exist.

## Verdict

- `pass`: every criterion proven and every required verify check passed.
- `fail` → `03-build`: change is defective. `fail` → `02-plan`: plan's checks or approach are wrong. `fail` → `05-verify`: environment failed, not change; say what failed so retry is cheap.
- `blocked`: no environment, no access.

## Do not

- Do not verify on developer machine and call it staging.
- Do not change code. Fix goes back to build, then through review again.

Common rules in `factory/stages/RULES.md` apply.
