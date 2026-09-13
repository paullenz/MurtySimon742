# Aggregate total-excess DP — canonical frontier result

13 September 2026. **Preserved negative/triage result. External mathematical review and independent computational reproduction remain OPEN.**

This note records the first canonical full-frontier run of [`TOTAL_EXCESS_AGGREGATE_DP.md`](TOTAL_EXCESS_AGGREGATE_DP.md) and [`scan_total_excess_aggregate_dp.py`](scan_total_excess_aggregate_dp.py).

GitHub Actions run `34788382367` completed successfully on the canonical frozen survivor stream.

## Result

Input after removing the 16 already-recorded N34 whole-state closures:

```text
4,568 scalar survivors
= 4,490 N34 equality-derived states
+    78 N35 m=306-derived states.
```

Aggregate DP result:

```text
whole scalar states excluded by this relaxation: 0
states surviving the aggregate relaxation:       4,568
first surviving excess E=0:                      4,568
```

Thus the aggregate source-capacity theorem is **not**, by itself, a new whole-state closure mechanism on the present frontier.

This is not a failed computation. The dynamic programme completed normally and the negative result is structurally informative: every current survivor admits at least one source-degree total at `E=0` under the aggregate capacity bookkeeping, even though much stronger exact incidence/orientation machinery can reject individual `E=0` states.

## Layer pruning

Although no complete scalar state is closed by the aggregate DP, it removes nontrivial excess layers in the tightest states. In particular, the two narrowest N34 survivors in the first canonical run were states `13518` and `13519`:

```text
S=89,
Emax=18,
surviving E = 0,1,2,3,4,8,9,10,11,12,18.
```

So only 11 of their 19 aggregate-admissible excess layers survive. These states were therefore promoted to the first exact tests of the stronger [`EXCESS_BUDGET_ORIENTATION_COST.md`](EXCESS_BUDGET_ORIENTATION_COST.md) machinery.

## Interpretation

The result separates two effects cleanly:

1. **Total incoming capacity is not the live obstruction.** Once source identities, orientation compatibility and selected-incidence competition are forgotten, every scalar state has an `E=0` aggregate survivor.
2. **The next useful information must be relational.** The new directed compatibility graph, pair uniqueness, selected-incidence Hall constraints and the weighted excess budget are not optional refinements; they are the information that can distinguish the live states.
3. **The aggregate DP remains useful as triage.** Its layer exclusions can be used before exact `q` enumeration, and its narrowest survivors provide principled targets rather than arbitrary state selection.

## Audit boundary

`SURVIVES_AGGREGATE` does not mean that a `q` profile exists, still less that a selected incidence system, missing-edge orientation or diameter-two edge-critical graph exists. Conversely, no state is promoted to the canonical closure ledger from this run because the aggregate relaxation closed none.

The full JSON/DP output is produced reproducibly by the committed workflow; no solver timeout, floating-point infeasibility or unsuccessful search is used as proof.
