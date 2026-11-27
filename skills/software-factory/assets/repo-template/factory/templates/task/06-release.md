---
# Stamped by the orchestrator (factoryctl start). Do not edit.
task_id: "{{task_id}}"
stage: 06-release
version: {{version}}
inputs: {{inputs}}
model: {{model}}
run_by: sub-agent
started: "{{started}}"
# Filled by the stage agent.
verdict: # pass | fail | blocked
return_to: # on fail only: 05-verify | 03-build — only when merged is false
merged: # true | false — did the PR reach main?
merge_commit: # sha on main, when merged
rolled_back: # true | false — required when merged and verdict is fail
---

# {{task_id}} · 06-release

## Task
{{header}}

## Input summary

<!-- Max three lines: what you received, what you took from it. -->

## Work done

### Released

<!-- What, where, version, merge commit. -->

### Rollback point

<!-- Exact version or commit to return to. -->

### Watch window

<!-- Duration, signals watched, thresholds, result. -->

### Rollback performed

<!-- "n/a — not needed", or what was rolled back, when, and proof production is healthy again. -->

## Evidence

<!-- Links, file paths with line numbers, logs in assets/. "n/a" plus a reason if none. -->

## Open questions / blockers

<!-- "none", or one line per item. A blocker means verdict: blocked. -->

## Handoff to next stage

<!-- What next stage must know that is not in sections above. -->
