# Stage 06 · Release

**Role:** operator. **Repo access:** merge and production deploy. No code edits. **Input:** `02-plan.md` (rollback and watch window), `05-verify.md`. **Output:** `06-release.md`.

Start only after go-live gate passed. Orchestrator has checked freeze calendar.

## Do

1. Record rollback point before changing anything.
2. Merge PR through repository's protected path: required checks green on merge result, branch up to date or merge queue. Set `merged` and `merge_commit`.
3. Deploy or publish per plan.
4. Watch plan's signals for full window. Record values, not "looks fine".
5. If signal crosses its threshold: execute plan's rollback at once, confirm production healthy, set `rolled_back: true`, return `fail`. Do not debug in production.

## Verdict

- `pass`: merged, deployed, watch window clean.
- `fail` with `merged: false` → `05-verify` (CI red on merge result, environment drift) or → `03-build` (merge conflict: resolving it is a code change).
- `fail` with `merged: true` and `rolled_back: true`: task ends as rolled back. Orchestrator files linked follow-up task and runs full retro.
- `blocked`: no deploy access, freeze, or failed rollback. Failed rollback is an incident: say so in first line.

## Do not

- Do not merge with red or missing checks. Do not bypass branch protection.
- Do not shorten watch window.

Common rules in `factory/stages/RULES.md` apply.
