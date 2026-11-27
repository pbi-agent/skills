---
# Stamped by the orchestrator (factoryctl start). Do not edit.
task_id: "{{task_id}}"
stage: 04-review
version: {{version}}
inputs: {{inputs}}
model: {{model}}
run_by: sub-agent # always a new agent, never the builder
started: "{{started}}"
# Filled by the stage agent.
verdict: # pass | fail | blocked
return_to: # on fail only: 03-build | 02-plan
proposes: {} # optional changes to the task record: risk, change_size, flags
---

# {{task_id}} · 04-review

## Task
{{header}}

## Input summary

<!-- Max three lines: what you received, what you took from it. -->

## Work done

### Findings

<!-- Severity: blocker | major | minor | note. Any blocker or major means verdict: fail. "none" row if clean. -->

| Severity | Finding | Location | Required change |
| -------- | ------- | -------- | --------------- |
|          |         |          |                 |

### Plan adherence

<!-- Does diff do what plan says, and nothing else? -->

### Evidence check

<!-- Did you re-run or independently confirm build checks? Which ones, what result? -->

### Verdict and reason

## Evidence

<!-- Links, file paths with line numbers, logs in assets/. "n/a" plus a reason if none. -->

## Open questions / blockers

<!-- "none", or one line per item. A blocker means verdict: blocked. -->

## Handoff to next stage

<!-- What next stage must know that is not in sections above. -->
