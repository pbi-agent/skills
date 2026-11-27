---
# Stamped by the orchestrator (factoryctl start). Do not edit.
task_id: "{{task_id}}"
stage: 05-verify
version: {{version}}
inputs: {{inputs}}
model: {{model}}
run_by: sub-agent
started: "{{started}}"
# Filled by the stage agent.
verdict: # pass | fail | blocked
return_to: # on fail only: 03-build | 02-plan | 05-verify (retry after an environment flake)
proposes: {} # optional changes to the task record: risk, flags
---

# {{task_id}} · 05-verify

## Task
{{header}}

## Input summary

<!-- At most three lines: what you received and took from it. -->

## Work done

### Environment

<!-- Staging, preview, canary dry run... and the commit deployed there. -->

### Scenarios run

### Results per acceptance criterion

| Criterion | Result | Link (URL or assets/) |
| --------- | ------ | --------------------- |
|           |        |                       |

### Release readiness

<!-- Rollback rehearsed? Watch signals available? Anything the operator must know. -->

## Evidence

<!-- One row per required check (see the brief). Result: pass | fail | n/a (reason in Method). -->

| Check | Result | Method / command | Commit | Log (URL or assets/ path, sha256) |
| ----- | ------ | ---------------- | ------ | --------------------------------- |
|       |        |                  |        |                                   |

## Open questions / blockers

<!-- "none", or one line per item. A blocker means verdict: blocked. -->

## Handoff to next stage

<!-- What next stage must know that sections above omit. -->
