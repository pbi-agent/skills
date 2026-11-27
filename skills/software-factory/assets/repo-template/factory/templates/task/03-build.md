---
# Stamped by the orchestrator (factoryctl start). Do not edit.
task_id: "{{task_id}}"
stage: 03-build
version: {{version}}
inputs: {{inputs}}
model: {{model}}
run_by: sub-agent
started: "{{started}}"
# Filled by the stage agent.
verdict: # pass | fail | blocked
return_to: # on fail only: 02-plan
proposes: {} # optional changes to the task record: risk, change_size, flags
---

# {{task_id}} · 03-build

## Task
{{header}}

## Input summary

<!-- Max three lines: what you received and took from it. -->

## Work done

### Changes made

### Branch / commits

### Deviations from plan

<!-- "n/a — none" if none. Deviation changing scope or risk goes into proposes. -->

### Rework addressed

<!-- v2+: each failing-stage item and how it was fixed. v1: "n/a — first build". -->

## Evidence

<!-- One row per required check (see the brief). Result: pass | fail | n/a (reason in Method). -->

| Check | Result | Method / command | Commit | Log (URL or assets/ path, sha256) |
| ----- | ------ | ---------------- | ------ | --------------------------------- |
|       |        |                  |        |                                   |

## Open questions / blockers

<!-- "none", or one line per item. A blocker means verdict: blocked. -->

## Handoff to next stage

<!-- What next stage must know that is not in sections above. -->
