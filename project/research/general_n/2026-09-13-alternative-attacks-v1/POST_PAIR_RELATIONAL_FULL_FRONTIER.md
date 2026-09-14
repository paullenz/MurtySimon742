# Full post-pair relational frontier — checkpointed reconnaissance

14 September 2026. **Discovery protocol, not a promotion certificate. External mathematical review and genuinely independent third-party reproduction remain OPEN.**

## Purpose

After promotion of the 16-state relational recovery family, the ledger-current frozen generalisation frontier is

```text
1,971 exclusions / 3,607 survivors,
3,529 N34-derived survivors,
78 N35-derived survivors.
```

The next computational objective is to apply the stronger post-pair relational relaxation to every one of those 3,607 scalar survivors. The previous 1/32 pilot demonstrated that a long sequential shard is a poor durability unit: useful completed states can be stranded when a later state consumes the workflow timeout.

This checkpoint therefore changes the **execution architecture**, not the mathematics.

## Mathematics retained

For each admissible total excess `E` and enlarged-universe `q` profile, [`scan_post_pair_relational.cpp`](scan_post_pair_relational.cpp) applies, in order:

1. canonical/simple incoming caps and `TOTAL_EXCESS_SOURCE_CAP`;
2. `POTENTIAL_PAIR_CAPACITY`;
3. exact variable-`x` selected-incidence circulation;
4. unordered-pair Hall flow;
5. directed target-capacity Hall flow;
6. for all-positive-demand states, the weighted excess-budget orientation min-cost bound.

`RELATIONAL_EXCLUDED` means every profile in that relaxed scalar state fails at least one necessary condition. It remains conditional on the canonical bridge. `SURVIVES_RELATIONAL` means only that this relaxation has a witness; it is not graph feasibility.

## Durable execution rules

[`run_post_pair_relational_checkpointed.py`](run_post_pair_relational_checkpointed.py) runs each scalar state in its own subprocess. After every state it atomically rewrites:

- `SHARD_RESULTS.tsv` containing only successfully completed mathematical results;
- `SHARD_STATUS.json` containing completed IDs and every unresolved state with an explicit reason;
- a per-state input, result and replay record.

The discovery workflow uses 256 deterministic modulo shards. A single state receives a bounded wall-clock budget. If that budget is exceeded, the state is recorded as `STATE_TIMEOUT` and the shard continues. A timeout, cancellation, process error, malformed output or missing output is **never** interpreted as exclusion.

Artifacts are uploaded with `if: always()`, so completed checkpoints survive even if another state or later workflow step fails.

## Promotion boundary

This full-frontier pass is **reconnaissance**. Its primary implementation may identify new candidate whole-state exclusions, but none enters `WHOLE_STATE_LEDGER.tsv` directly.

Any new candidate family must instead pass the same promotion discipline used for the recovered 16 states:

1. ledger-current state reconstruction;
2. fresh primary replay;
3. independent type-count replay using [`scan_post_pair_relational_types.cpp`](scan_post_pair_relational_types.cpp);
4. exact agreement of all proof-relevant stage counts;
5. frozen hash-bound certificate and durable ledger guard;
6. only then canonical promotion and status synchronization.

If the discovery pass produces too many candidates for one audit matrix, the candidates will be partitioned deterministically and audited in batches. No sampling may stand in for exhaustive candidate-family audit.

## Structural objective

The finite scan is not an end in itself. Its certificate statistics should be mined for a symbolic explanation of the states rejected only after pair-choice Hall, target Hall, or excess-budget cost. The principal theoretical target remains a compact two-dimensional dominance/Hall inequality (or small extremal family of such cuts) that subsumes a substantial part of the exact flow computation.

## Trust boundary

The unrestricted Murty–Simon conjecture is not proved by this programme. Internal replay, cross-implementation agreement and GitHub publication are not external mathematical acceptance. The purpose of this protocol is to make every finite exclusion reproducible, auditable and difficult to overclaim.

## Canonical discovery-run provenance

The intended first full-frontier discovery experiment is GitHub Actions run `34818390230`, head `94f89d5d0147842f9d0c2e10606d2117e62400f5`. It was launched before the later layer-state checkpoint hardening; the downstream summarizer therefore reconstructs layer identity from each frozen shard input and rejects any unresolved ambiguity rather than guessing.

A later code update queued a redundant second full-frontier run before the expensive scan workflow was changed to manual-only. That duplicate run is noncanonical reconnaissance: it has no authority to change a ledger or headline count. The promotion path is gated entirely on the layer-safe aggregate/recovery/audit chain documented above.

## Promotion receipt — 14 September 2026

The separate promotion gate is now complete. Discovery run `34844403328` covered all 3,607 then-current survivors with zero unresolved states and identified 2,655 candidate closures. Independent audit run `34854911792` audited exactly the same byte-identical key set with two implementations and a successful aggregate requiring complete agreement. The reviewed ledger step found no overlap with the existing ledgers and promoted 2,580 N34 plus 75 N35 closures. The canonical finite frontier is therefore **4,626 exclusions / 952 survivors / 3,632 whole-state closures**, with 949 N34 and 3 N35 survivors. See [`POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.md`](POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.md) and [`POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.json`](POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.json). **The unrestricted conjecture is not claimed proved; external review remains open.**
