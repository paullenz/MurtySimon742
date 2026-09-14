# Post-pair relational pilot recovery and audit

14 September 2026. **Audit checkpoint. External mathematical review and genuinely independent third-party reproduction remain OPEN.**

## 1. Why this checkpoint exists

GitHub Actions run `34789806859` launched the first 1/32-shard post-pair relational pilot from commit `4a72d5815739750a5c6878f691392b605e874df5`. The job was cancelled at the workflow timeout while processing the shard; cancellation is not a mathematical result and no unfinished state is treated as excluded.

Before cancellation, the scanner printed complete `RELATIONAL_EXCLUDED` results for the following 16 states:

```text
961, 1025, 2620, 2706,
2897, 3007, 3139, 3202,
3302, 3359, 3480, 3599,
4145, 4559, 4654, 4994.
```

Those log lines are **recovery candidates only**. They are not part of the canonical whole-state ledger until the audit gates below pass.

## 2. Mathematical layer being checked

For each admissible total excess `E` and each enlarged-universe `q` profile, the primary scanner applies necessary conditions in the following order:

1. canonical/simple incoming caps plus `TOTAL_EXCESS_SOURCE_CAP`;
2. `POTENTIAL_PAIR_CAPACITY`;
3. variable selected-incidence lower-bound circulation;
4. unordered-pair Hall flow;
5. directed target-capacity Hall flow;
6. in all-positive-demand branches, the weighted excess-budget orientation min-cost bound.

A state is `RELATIONAL_EXCLUDED` only if **every** admissible profile fails one of these necessary conditions. Passing the relaxation is not graph feasibility.

## 3. Recovery audit gates

No state from the interrupted run may be promoted unless all of the following are satisfied.

### Gate A — ledger-current reconstruction

`prepare_post_pair_targets.py` must recover the state from the current frozen survivor source after removing every already-promoted N34 closure from `WHOLE_STATE_LEDGER.tsv`. The preparation record includes source, ledger and emitted-input hashes.

### Gate B — fresh primary replay

`scan_post_pair_relational.cpp` must rerun the state to completion in its own workflow job. Timeout, cancellation, solver status, partial output or missing output is failure, not proof.

### Gate C — independent representation

`scan_post_pair_relational_types.cpp` must rerun the same state. It differs from the primary program in three proof-relevant implementation choices:

- equal-`rho` `q` profiles are enumerated by multiplicities `m_q`, not nondecreasing `q` vectors;
- potential-pair degrees use the closed type-count formula rather than pair-by-pair degree construction;
- the min-cost target flow uses reduced-cost Dijkstra with vertex potentials rather than the primary queue-based shortest-path routine.

This is an implementation cross-check, not independent mathematical review.

### Gate D — exact count agreement

For an excluded state both scanners exhaust the entire profile universe, so `compare_post_pair_relational.py` requires exact agreement on:

- `Emax`;
- total profiles tested;
- pass/fail counts at every relational stage;
- final exclusion status;
- absence of a surviving witness.

Any disagreement blocks promotion.

### Gate E — durable certificate

Only after Gates A-D pass may a state be added to `WHOLE_STATE_LEDGER.tsv`. The promoted family must have a preserved audit record, exact state list and a durability check preventing silent removal.

## 4. Original interrupted-run evidence

The interrupted run completed 38 states before cancellation. Sixteen printed `RELATIONAL_EXCLUDED`; the remaining completed states printed `SURVIVES_RELATIONAL`. Because the final aggregation and artifact-upload step never ran, this recovery checkpoint deliberately does not infer a complete shard result from the partial log.

The original run therefore supplies reconnaissance and provenance only. The fresh targeted replays are the proof-relevant computation.

## 5. Scope and trust boundary

The relational scan checks necessary conditions derived inside the canonical selected/residual bridge. A successful exclusion is therefore conditional on those structural lemmas. It does not provide external specialist acceptance of the bridge, novelty, or the unrestricted Murty-Simon conjecture.

The unrestricted conjecture remains open in this project.

## 6. Current status

**At creation of this checkpoint:** 16 recovery candidates identified; **0 newly promoted from this interrupted pilot**. Canonical frontier remains `1,955 exclusions / 3,623 survivors` until the audit gates above are completed and recorded.
