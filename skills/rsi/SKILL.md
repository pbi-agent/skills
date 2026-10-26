---
name: rsi
description: Use when building or running a recursive self-improving (RSI) loop that evaluates a model, prompt, agent, or skill with a judge, diagnoses and clusters its failures into weaknesses, generates targeted training data from seed references, and retrains or updates the target in repeated rounds.
---

# RSI Loop

Build a recursive self-improving loop: Evaluate the target, Diagnose why it
fails, Generate data aimed at those weaknesses, train the target on it, and
repeat. Each round must be measured against a frozen held-out set so the loop
improves the target instead of overfitting to its own generated data.

## Loop Diagram

Keep this diagram as the canonical picture of the loop.

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "wrappingWidth": 200}} }%%
flowchart TB
    subgraph E["1 · Evaluate"]
        IN["Input"] --> M["Model"]
        M --> PR["Prediction"]
        M -- "Multiple rollouts" --> RO[["Rollout outputs"]]
        PR --> J1["Judge model"]
        J1 -- "Grade" --> OK["Correct"]
        J1 -- "Grade" --> KO["Wrong"]
        J1 -- "Grade" --> UN["Uncertain"]
        RO -- "High disagreement" --> UN
    end

    subgraph D["2 · Diagnose"]
        J2["Judge model<br/><i>per-sample failure attribution</i>"]
        subgraph CA["Cluster A"]
            F1["Failure reason 1"] --> W1[["Weakness A"]]
            F3["Failure reason 3"] --> W1
            F5["Failure reason 5"] --> W1
        end
        subgraph CB["Cluster B"]
            F2["Failure reason 2"] --> W2[["Weakness B"]]
            F4["Failure reason 4"] --> W2
            F6["Failure reason 6"] --> W2
        end
        J2 --> F1 & F3 & F5
        J2 --> F2 & F4 & F6
    end

    subgraph G["3 · Generate"]
        SD[["Seed data<br/><i>new reference each time</i>"]]
        SD --> S["Reference sample"]
        S -- "Match distribution" --> GM["Generator model"]
        GM -- "Targeted data" --> T[["Input + target"]]
    end

    KO --> J2
    UN --> J2
    W1 --> GM
    W2 --> GM
    T -- "Train" --> M

    classDef model fill:#5a4630,stroke:#c9a46a,color:#fff
    classDef judge fill:#46405a,stroke:#9a92b8,color:#fff
    classDef diag fill:#2e4a6b,stroke:#7fa3cc,color:#fff
    classDef data fill:#36553f,stroke:#7fb08c,color:#fff
    classDef ok fill:#2f4a3a,stroke:#7fb08c,color:#fff
    classDef bad fill:#5a3434,stroke:#c07a7a,color:#fff

    class M,UN,SD,S model
    class J1,J2,GM judge
    class F1,F2,F3,F4,F5,F6,W1,W2 diag
    class T data
    class OK ok
    class KO bad
```

## Load References

- Load `references/stages.md` for detailed Evaluate, Diagnose, Generate, and
  Train procedures, judge rubrics, and prompt templates.
- Load `references/artifacts.md` before creating or resuming a loop workspace.

## Startup

1. Identify the target (`Model`): a fine-tunable model, a prompt, an agent, or
   a skill. "Train" means fine-tune for models and edit instructions or
   few-shot examples for prompts, agents, and skills.
2. Identify the task, the input source, the grading criteria, and the judge
   and generator models. Ask only if the task or success criteria cannot be
   inferred.
3. Create or resume `rsi/<slug>/`; read `state.md` and the latest
   `rounds/<n>/summary.md` if present.
4. Freeze a held-out eval set and a seed set before round 1. Never train on,
   generate from, or edit the held-out set.

## Round Flow

1. Evaluate: run the target on the eval inputs with `k` rollouts per input.
   The judge grades each prediction against the rubric as `correct`, `wrong`,
   or `uncertain`. Force `uncertain` when rollouts disagree above the
   threshold, even if the graded prediction looks correct.
2. Diagnose: send only `wrong` and `uncertain` samples to the judge for
   per-sample failure attribution (one concrete reason each). Cluster the
   reasons into named weaknesses with counts, examples, and a one-line
   hypothesis of the missing capability.
3. Generate: for each weakness, draw a fresh reference sample from the seed
   data (rotate references every call), and have the generator produce new
   `input + target` pairs that match the seed distribution while exercising
   that weakness. Filter outputs with the judge before use.
4. Train: update the target on the accepted targeted data, mixed with replay
   data from earlier rounds and correct seed samples to avoid regressions.
5. Gate: re-run Evaluate on the frozen held-out set. Keep the new target only
   if the primary metric improves and no guardrail metric regresses beyond
   tolerance; otherwise revert and adjust Diagnose or Generate.

## Guardrails

- Judge and generator must not see held-out targets during generation.
- Deduplicate generated data against the held-out set (exact and near-dup).
- Cap each weakness's share of a round's data so one cluster cannot dominate.
- Spot-check judge grades by hand or with a second judge each round; track
  judge agreement and stop if it drops.
- Log every round: metrics, weakness clusters, data counts, accept/reject.
- Stop when the metric plateaus for 2 rounds, the budget is spent, or the
  remaining failures are label noise or out of scope.

## Output

At handoff, report the per-round metric table, the weaknesses fixed and still
open, the accepted target version, and the path to `rsi/<slug>/`.
