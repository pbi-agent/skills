# Stage 07 · Retro

**Role:** curator. **Run by:** orchestrator. **Input:** every file in task folder, `state.yaml`, `events.jsonl`. **Output:** `07-retro.md`.

Work from files, not session memory. Timeline, loops and escalations are generated for you from `events.jsonl`.

## Light mode

Front matter says `retro_mode: light` when task had no loops, no escalations, no rollback and was not expedited. Then write: outcome per criterion, one line on what went well, `n/a` plus reason in other sections. Set `factory_change: none`.

## Full mode

1. Outcome: goal met? Each criterion met or not met.
2. For each loop: real cause. Which earlier stage could have caught it?
3. For each escalation: was human needed? Would tighter or looser rule have been right?
4. Cross-task patterns: run `factoryctl index`, read retros of similar tasks. Cite task ids.
5. Factory changes: propose one only when same problem appears in at least 2 tasks (cite them) or task was rolled back. Describe change and its target: stage, profile, check, rule or template.

## Filing a factory change

Do not edit `factory/` here. File new task with `factoryctl new --factory-change --source retro --link <this task>`. It runs through same pipeline on a `factory/` branch; a human merges it. Put its id in `factory_change` and in the table.

## Verdict

`pass`, with `factory_change: none` or id of task you filed.
