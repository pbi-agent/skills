# Stage 03 · Build

**Role:** builder. **Repo access:** write, on task branch only. **Input:** `02-plan.md`; on rework, also failing stage's file. **Output:** `03-build.md`.

## Do

1. Follow plan's steps. Stay inside plan's file list.
2. Run every build-stage check in brief. Record each in evidence table: check id, result, command, commit it ran on, log (CI URL, or file in `assets/` with its sha256).
3. Record every deviation from plan. If deviation changes scope or risk, add flag or raise size in `proposes`.
4. On rework: answer each finding of failing stage under "Rework addressed", one by one.
5. Leave branch pushed and CI running on head commit.

## Verdict

- `pass`: every required build check in table with result `pass` (or `n/a` with reason, where check allows it).
- `fail` → `02-plan`: plan cannot work. Say what you tried and why it fails.
- `blocked`: missing access, missing decision.

## Do not

- Do not touch `factory/`, CI configuration not in plan, or another task's folder. Branch guard rejects it.
- Do not weaken, skip or delete a test to get green. If test is wrong, say so; let review decide.
- Do not report a check you did not run. Review re-runs a sample; CI is source of truth.

Common rules in `factory/stages/RULES.md` apply.
