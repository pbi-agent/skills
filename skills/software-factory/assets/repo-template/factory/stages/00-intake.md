# Stage 00 · Intake

**Role:** intake. **Repo access:** none. **Input:** `assets/request.md` (raw request). **Output:** `00-intake.md`.

## Do

1. Restate request in own words. Keep requester's wording where it matters.
2. Choose profile (`type`) from `factory.yaml`. If work spans several, pick one with highest risk floor as `type`; list others as `secondary_types`.
3. Write one goal sentence: outcome, not activity.
4. Write acceptance criteria. Each must be testable by someone who never saw request and must name observable result. Three to seven is typical.
5. Write what is out of scope.
6. Put `type`, `goal` and `acceptance_criteria` into `proposes`. Orchestrator copies them into task record.

## Verdict

- `pass`: type, goal and criteria set.
- `blocked`: request too ambiguous to write testable criteria. Ask precise question.
- `reject`: not software work, duplicate the orchestrator missed, or request to change `factory/` that arrived on `task/` branch (must be refiled as factory change).

## Do not

- Do not investigate code. That is triage.
- Do not invent requirements absent from request. Put doubts under open questions.

Common rules in `factory/stages/RULES.md` apply.
