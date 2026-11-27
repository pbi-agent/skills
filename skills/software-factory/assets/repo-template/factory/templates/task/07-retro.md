---
# Stamped by the orchestrator (factoryctl start). Do not edit.
task_id: "{{task_id}}"
stage: 07-retro
version: {{version}}
inputs: {{inputs}}
model: {{model}}
run_by: orchestrator
started: "{{started}}"
# Filled by the stage agent.
verdict: # pass
retro_mode: {{retro_mode}} # light | full
factory_change: # none | <task id of the factory_change task filed>
---

# {{task_id}} · 07-retro

## Task
{{header}}

## Outcome

<!-- Was the goal met? Each acceptance criterion: met / not met. -->

## Timeline

<!-- Generated from events.jsonl. Do not edit. -->
{{timeline}}

## Loops and why
{{loops}}

## Escalations and why

<!-- Generated list first. Then: needed? Rule tighter or looser? -->
{{escalations}}

## What went well

## What to change in the factory

<!-- Only problems seen in at least 2 tasks (cite them) or 1 rollback. Otherwise "n/a — no recurring problem". -->

| Target (stage / profile / check / rule / template) | Change | Seen in tasks | Factory task |
| -------------------------------------------------- | ------ | ------------- | ------------ |
|                                                    |        |               |              |

## Cross-task patterns

<!-- From `factoryctl index`, not from memory. "n/a" plus a reason in light mode. -->
