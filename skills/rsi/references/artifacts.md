# RSI Artifacts

Workspace layout for one loop, under `rsi/<slug>/` unless the project already
has an equivalent location.

```text
rsi/<slug>/
├── state.md                 # target, task, judge/generator, thresholds, current version, status
├── data/
│   ├── heldout.jsonl        # frozen eval set; never edited or trained on
│   ├── seed.jsonl           # seed references for generation
│   └── generated/
│       └── round-<n>.jsonl  # accepted input + target pairs per round
└── rounds/
    └── <n>/
        ├── eval.jsonl       # per-sample grade, confidence, disagreement, label
        ├── failures.jsonl   # per-sample failure reason for wrong/uncertain
        ├── weaknesses.md    # weakness cards with counts and examples
        ├── train.md         # data mix, version, checkpoint or prompt diff
        └── summary.md       # metrics, gate decision, open weaknesses, next step
```

## state.md

- Target type and current accepted version.
- Task description and rubric.
- Judge model, generator model, `k`, disagreement threshold.
- Primary metric and guardrail metrics with tolerances.
- Budget and stop criteria.
- Status: `running`, `blocked`, or `done`, plus the next action.

## summary.md

```markdown
# Round <n>

| Metric | Prev | New | Delta |
| --- | --- | --- | --- |
| Accuracy | | | |
| Uncertain rate | | | |

- Weaknesses targeted: ...
- Data: <accepted>/<generated> pairs, replay share ...
- Gate: accepted | rejected (reason)
- Open weaknesses: ...
- Next: ...
```

## Resume Rules

- Read `state.md` and the latest `summary.md` before any new round.
- Start a new round directory; never overwrite a finished round.
- If the held-out set must change, start a new loop slug instead.
