# Escalation rules

Every gate passes automatically unless a rule below fires. Thresholds and lists live in `factory.yaml` (`gates`, `classification`, `controls`). This file explains them and defines the human procedure. If the two disagree, `factory.yaml` wins; this file has a bug.

## Gates

| Gate          | Evaluated       | Question for the human                                                  |
| ------------- | --------------- | ----------------------------------------------------------------------- |
| `worth-doing` | after 01-triage | Is this work worth doing as scoped?                                     |
| `approach`    | after 02-plan   | Is this the right approach?                                             |
| `scope-drift` | after 03-build  | The built change is bigger or riskier than what was approved. Continue? |
| `go-live`     | after 05-verify | Release to production?                                                  |

`scope-drift` fires only if classification changed since the `approach` gate. Exists because agents classify work before doing it, and the real diff can say otherwise.

## When a human must approve

Gate escalates when any one of these is true:

- **Risk is high.**
- **Change size is major or structural.** Major: measured on real diff (`size_thresholds`). Structural: follows from any structural flag.
- **Any flag is set.**
  - Structural change: `architecture`, `public_api`, `data_model`, `new_dependency`, `security_model`.
  - Important decision: `product_scope`, `irreversible`, `cost_or_license`, `design_tradeoff`.
- **The task is expedited** (at `go-live` only).
- **A human put the task on hold.**

Two more escalations, not tied to a gate:

- **Loop limit:** one stage sent task back `max_loops_per_stage` times, or task has `max_loops_per_task` loops in total.
- **Budget:** task cost more than `max_cost_per_task_usd`.

## How the classification is set

1. Intake sets type. Profile's `default_risk` is a floor.
2. Triage, plan, build and review can **raise** risk, size and flags through `proposes`. Proposals to lower them are ignored and logged.
3. After build, `factoryctl classify-diff` raises flags from changed paths (`path_triggers`) and size from diff. Agents cannot override this.
4. Change to goal or acceptance criteria after 02-plan sets `product_scope`.
5. Only a human can lower anything: `factoryctl set <task> --risk ... --by <name> --reason "..."`. Risk never goes below profile floor.

## What the human receives

Orchestrator posts one comment on task PR (or tracker issue, before a PR exists):

- gate and its question,
- reasons gate fired, from `state.yaml: pending.reasons`,
- Task header (goal, criteria, classification),
- link to stage document to read: `01-triage.md`, `02-plan.md`, `03-build.md` plus the diff, or `05-verify.md`,
- for `go-live`: rollback and watch window from plan.

## How the human answers

- **Approve:** PR review approval or comment by an authorized person. Orchestrator records it with `factoryctl approve --by --evidence <url>`. Approval without a link is not valid.
- **Deny:** task is cancelled. Branch is closed without merging.
- **Send back:** deny not needed; ask orchestrator to `sendback` to a stage with a reason.

Who may approve: factory owners in `.github/CODEOWNERS` for `factory/**`; for product gates, code owners of paths the PR touches.

## Expedite

For production incidents. Human sets `--expedite` at task creation. Same stages, none skipped. What changes: task jumps queue, `go-live` always needs a human, retro is always full.

## Audit of auto-passed tasks

A share of tasks that passed every gate automatically (`controls.audit_sample_rate`) is marked `audit: pending` when it finishes. A factory owner reads task folder and records `agreed` or `disagreed` with `factoryctl audit`. Disagreement is a reason for a factory change. Disagreement rate shows whether auto gates can be trusted.

## Changing these rules

Through a `factory_change` task, on a `factory/` branch, merged by a human. A change that loosens a rule must say so in the PR's first line.
