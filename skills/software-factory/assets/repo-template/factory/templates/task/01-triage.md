---
# Stamped by the orchestrator (factoryctl start). Do not edit.
task_id: "{{task_id}}"
stage: 01-triage
version: {{version}}
inputs: {{inputs}}
model: {{model}}
run_by: sub-agent
started: "{{started}}"
# Filled by the stage agent.
verdict: # pass | fail | blocked | reject
return_to: # on fail only: 00-intake
proposes: {} # optional changes to the task record: type, secondary_types, risk, change_size, flags, goal, acceptance_criteria
---

# {{task_id}} · 01-triage

## Task
{{header}}

## Input summary

<!-- Max three lines: what you received and took from it. -->

## Work done

### Findings

### Root cause / scope

### Risk and change size

<!-- Justify each. Name every structural change or important decision as a flag. -->

### Unknowns

<!-- Resolved and unresolved. An unresolved blocking unknown means verdict: blocked. -->

## Evidence

<!-- Links, file paths with line numbers, logs in assets/. "n/a" plus a reason if none. -->

## Open questions / blockers

<!-- "none", or one line per item. A blocker means verdict: blocked. -->

## Handoff to next stage

<!-- What next stage must know beyond sections above. -->
