---
# Stamped by the orchestrator (factoryctl start). Do not edit.
task_id: "{{task_id}}"
stage: 02-plan
version: {{version}}
inputs: {{inputs}}
model: {{model}}
run_by: sub-agent
started: "{{started}}"
# Filled by the stage agent.
verdict: # pass | fail | blocked
return_to: # on fail only: 01-triage
proposes: {} # optional changes to the task record: risk, change_size, flags, goal, acceptance_criteria
---

# {{task_id}} · 02-plan

## Task
{{header}}

## Input summary

<!-- Max three lines: what you received, what you took from it. -->

## Work done

### Approach

### Alternatives considered

### Files and components

<!-- Every path builder may touch. Anything else = deviation. -->

### Steps

1.

### Checks per acceptance criterion

| Criterion | Check | Stage (03-build / 05-verify) | How to run |
| --------- | ----- | ---------------------------- | ---------- |
|           |       |                              |            |

### Rollback

<!-- Exact steps to undo release, plus signal that triggers them. -->

### Watch window

<!-- Signals to watch after release, thresholds, duration. -->

## Evidence

<!-- Links, file paths with line numbers, logs in assets/. "n/a" plus reason if none. -->

## Open questions / blockers

<!-- "none", or one line per item. A blocker means verdict: blocked. -->

## Handoff to next stage

<!-- What next stage must know that is not in sections above. -->
