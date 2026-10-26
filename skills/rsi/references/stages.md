# RSI Stages

Detailed procedures for each stage of the loop in `SKILL.md`.

## 1. Evaluate

Inputs: frozen eval set, current target version, judge model, rubric.

1. For each input, sample `k` rollouts (default `k = 5`, temperature > 0) and
   one primary prediction (temperature 0 or the deployment setting).
2. Grade the primary prediction with the judge using the rubric. The judge
   returns `{grade, confidence, rationale}`.
3. Compute rollout disagreement: share of rollouts whose judged grade or
   normalized answer differs from the majority. Default threshold: `>= 0.4`.
4. Final label:
   - `correct`: judge says correct, confidence high, disagreement below
     threshold.
   - `wrong`: judge says wrong with high confidence.
   - `uncertain`: low judge confidence or disagreement at/above threshold.
5. Record metrics: accuracy, `wrong` rate, `uncertain` rate, and any
   task-specific guardrail metrics (format validity, latency, cost, safety).

Judge rubric template:

```text
Task: <task description>
Input: <input>
Reference target (if any): <target>
Prediction: <prediction>
Criteria: <explicit pass/fail criteria>
Return JSON: {"grade": "correct|wrong", "confidence": 0-1, "rationale": "..."}
```

## 2. Diagnose

Inputs: all `wrong` and `uncertain` samples with their rollouts.

1. Per-sample attribution: ask the judge for one concrete failure reason per
   sample, phrased as the missing capability, not the symptom.
   Bad: "answer was wrong". Good: "ignores the date filter in the question".
2. Cluster reasons: embed reasons and cluster, or ask the judge to group them.
   Merge clusters with the same root cause; drop singletons into `other`.
3. For each cluster, write a weakness card: name, count, share of failures,
   2-3 representative sample ids, hypothesis, and what data would fix it.
4. Rank weaknesses by `count * fixability`. Target the top clusters this
   round; leave the rest open.

Attribution prompt template:

```text
The model failed or was unstable on this sample.
Input: <input>
Prediction: <prediction>
Rollouts: <rollouts>
Expected behavior: <target or criteria>
State the single most likely missing capability in one sentence.
Return JSON: {"reason": "...", "evidence": "..."}
```

## 3. Generate

Inputs: weakness cards, seed data, generator model.

1. For every generation call, draw a new reference sample from the seed set.
   Never reuse the same reference across consecutive calls; rotation keeps
   generated data diverse and on-distribution.
2. Prompt the generator with the reference, the weakness card, and an
   instruction to match the reference's format, length, domain, and
   difficulty while exercising the weakness.
3. Produce `input + target` pairs. For tasks with verifiable answers, compute
   or check targets programmatically instead of trusting the generator.
4. Filter: judge each pair for correctness and relevance to the weakness;
   drop duplicates, near-duplicates of held-out items, and off-distribution
   samples.
5. Budget: default 50-500 accepted pairs per weakness per round, capped so
   no weakness exceeds ~40% of the round's data.

Generator prompt template:

```text
Reference sample (match its style and distribution):
<reference input + target>
Weakness to exercise: <weakness name and hypothesis>
Write N new samples that a model with this weakness would fail.
Each sample must be self-contained and have a correct target.
Return JSONL: {"input": "...", "target": "...", "weakness": "<name>"}
```

## 4. Train

- Fine-tunable model: train on accepted data plus replay (default 30-50%
  replay from earlier rounds and correct seed samples). Use small learning
  rates and few epochs; keep the previous checkpoint.
- Prompt, agent, or skill: turn each weakness into a concrete instruction
  rule and add 1-3 generated examples as few-shot demonstrations. Keep the
  prompt diff small and reviewable.
- Version every update (`v<n>`), and store the diff or checkpoint path.

## 5. Gate

- Re-evaluate the new version on the frozen held-out set with the same judge,
  rubric, `k`, and thresholds.
- Accept only if the primary metric improves beyond noise (re-run or use
  confidence intervals on small sets) and guardrail metrics stay within
  tolerance.
- On reject: revert, note the likely cause (bad data, judge drift, wrong
  weakness), and adjust the next round.
- Periodically refresh the judge check: grade a human-labeled slice and
  compare agreement against round 1.
