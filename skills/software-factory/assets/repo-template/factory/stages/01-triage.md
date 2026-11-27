# Stage 01 · Triage

**Role:** investigator. **Repo access:** read. **Input:** `00-intake.md`. **Output:** `01-triage.md`.

## Do

1. Investigate until you can say what is wrong or must change, and where. Bug: reproduce it or explain exactly why you cannot.
2. Set classification in `proposes`; justify each value:
   - `risk`: what breaks, for whom, how hard to undo. Never below profile floor.
   - `change_size`: `minor`, `major` (many files or modules) or `structural`.
   - `flags`: every foreseeable structural change (`architecture`, `public_api`, `data_model`, `new_dependency`, `security_model`) and every foreseeable important decision (`product_scope`, `irreversible`, `cost_or_license`, `design_tradeoff`).
3. Correct type, goal or criteria if intake got them wrong. Say why.
4. List unknowns: resolved and unresolved.

## Verdict

- `pass`: no blocking unknown left.
- `fail` → `00-intake`: intake misread request so badly it must be redone.
- `blocked`: unknown only a human can resolve.
- `reject`: not worth doing — cannot reproduce and no evidence, already fixed, or cost clearly exceeds value. Give evidence.

## Do not

- Do not design the solution. Name constraints planner must respect.
- Do not under-classify to avoid a gate. Orchestrator re-classifies from real diff after build.

Common rules in `factory/stages/RULES.md` apply.
