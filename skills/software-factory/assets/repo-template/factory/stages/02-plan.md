# Stage 02 · Plan

**Role:** planner. **Repo access:** read. **Input:** `01-triage.md`. **Output:** `02-plan.md`.

## Do

1. Choose approach. Record at least one alternative and why it lost. If two designs are both acceptable and choice matters later, add flag `design_tradeoff`.
2. List every file and component builder may touch. Anything outside this list is a deviation.
3. Write ordered steps a builder with no other context can follow.
4. Fill "Checks per acceptance criterion": every criterion gets at least one check, stage where it runs (`03-build` or `05-verify`) and how to run it. Include every required check of the profile (see brief).
5. Write rollback: exact steps, and signal that triggers them.
6. Write watch window: signals, thresholds and duration after release.
7. If plan reveals more than triage saw, raise risk, size or flags in `proposes`.

## Verdict

- `pass`: every criterion has a check and rollback is defined.
- `fail` → `01-triage`: findings wrong or too thin to plan on.
- `blocked`: decision only a human can take.

## Do not

- Do not write the code.
- Do not change acceptance criteria silently. Propose and explain the change; criteria are frozen after this stage.

Common rules in `factory/stages/RULES.md` apply.
