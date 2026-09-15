# Threshold-Hall normal form pilot v1

15 September 2026. Discovery/audit hardening only; **no canonical frontier promotion**.

This checkpoint asks whether the generic flow computations appearing after the new forced-core screen can be replaced, on the difficult audited N34 closure family, by explicit Hall-type inequalities that are short enough to expose the obstruction structurally.

The source state and `q` conventions are exactly those of [`../2026-09-15-forced-core-canonical-scan-v1`](../2026-09-15-forced-core-canonical-scan-v1/README.md). The exact input is that package's frozen `TARGET_INPUT.txt`. The present verifier retains the forced-core test and pair-capacity screen, but replaces three later generic flow decisions by explicit necessary cut inequalities.

## Three explicit threshold cuts

Let `D_ij` be the existing directed compatibility indicator and `P_j` the existing target capacity. For any set `X` of sources, every feasible realization must satisfy the corresponding Hall/min-cut necessary inequalities. The pilot uses the nested source family

```text
X(R,k) = { i : rho_i >= R and q_i >= k }.
```

### 1. Selected-incidence suffix cut

For a demand threshold `d`, put

```text
L_d = { i : s_i >= d }.
```

A source `u` can contribute to at most

```text
min(q_u, |{ i in L_d : s_i <= rho_u }|)
```

incidences inside `L_d`. Therefore every realization obeys

```text
sum_{i in L_d} s_i
  <= sum_u min(q_u, |{ i in L_d : s_i <= rho_u }|).
```

This is a direct cut of the selected-incidence bipartite network; no max-flow computation is needed to certify a violation.

### 2. Pair-slot threshold cut

Each unordered pair slot `{i,j}` has capacity one. For `X=X(R,k)`, let `N_pair(X)` be the set of unordered pairs for which at least one endpoint in `X` has a compatible directed arc to the other endpoint. Then

```text
sum_{i in X} q_i <= |N_pair(X)|.
```

Violation is an explicit Hall deficiency for the pair-slot routing problem.

### 3. Target-capacity threshold cut

For `X=X(R,k)`, let

```text
deg_X(j) = |{ i in X : D_ij = 1 }|.
```

Target `j` can receive at most `P_j` units in total and at most one unit from each source in `X`, hence

```text
sum_{i in X} q_i
  <= sum_j min(P_j, deg_X(j)).
```

Again, violation is an explicit min-cut certificate, not a solver status.

These inequalities are only **necessary** conditions. Passing them is never treated as proof of realizability. They are deliberately weaker than the generic flow solvers, so using them for exclusion is safe.

## Exact replay result

`THRESHOLD_REPLAY_23.tsv` records complete exact enumeration of 23 of the 24 independently audited whole-state forced-core exclusions from `forced-core-canonical-audit-v1`. The omitted state is `N34:152`: it is structurally different and much heavier in this implementation, so this checkpoint makes no new threshold-normal-form claim about it.

Across the 23 replayed states:

```text
complete q profiles enumerated: 92,922,346
states closed by forced-core + pair-capacity + threshold cuts alone: 22
states with any profile left after threshold cuts: 1  (state 2812)
profiles left after all threshold cuts: 3
```

For every one of the 22 threshold-closed states, the counts at the selected-incidence, pair-slot and target-capacity stages agree exactly with the corresponding generic-flow stage counts in `INDEPENDENT_CLOSURE_MATCHES.tsv`. Thus, on this replayed family, the generic flow failures admit witnesses from the explicit threshold families above.

State `2812` is the sole exception. The threshold cuts leave exactly three profiles, all at `E=6`. `COST_REMAINDERS_2812.tsv` records them. The existing exact target-cost calculation gives minimum costs `74,74,75`, while the exact excess envelope is `60` in each case, so all three are excluded by the already-established cost inequality. The verifier has an exact min-cost fallback only for profiles that survive the threshold cuts; it is not used by the 22 threshold-closed states.

## What this establishes

This is a structural simplification of the audited finite closure evidence, not a new canonical closure count and not an all-order theorem. It shows that a large, difficult N34 family previously expressed through generic flows can instead be certified by a small menu of monotone threshold cuts, with only three exceptional profiles delegated to the pre-existing cost bound.

The result is particularly suggestive for the long-plateau states whose demand vector has a large `s_i=5` block and whose residual degrees concentrate in a few levels. In those states the threshold source sets `X(R,k)` are natural candidates for a general exchange/compression theorem: if an arbitrary deficient source set can be compressed to a `rho`/`q` threshold set without increasing its available capacity, the flow stage could be removed symbolically rather than only replayed computationally.

That compression statement is **not proved here**. It is the next mathematical target.

## Reproduction

From repository root, using the exact canonical forced-core target input:

```bash
g++ -O3 -std=c++17 -Wall -Wextra \
  project/research/general_n/2026-09-15-threshold-hall-normal-form-v1/scan_threshold_hall_v1.cpp \
  -o /tmp/scan_threshold_hall_v1

while read id; do
  /tmp/scan_threshold_hall_v1 \
    project/research/general_n/2026-09-15-forced-core-canonical-scan-v1/TARGET_INPUT.txt \
    "$id"
done < project/research/general_n/2026-09-15-threshold-hall-normal-form-v1/REPLAY_IDS.txt
```

The output fields are

```text
state_id
profiles_tested
forced_core_fail
pair_capacity_fail
incidence_threshold_fail
pair_slot_threshold_fail
target_threshold_fail
remaining_after_thresholds
fallback_target_hall_fail
fallback_cost_fail
final_remaining
```

The source intentionally enumerates complete admissible equal-`rho` partition types exactly. It does not infer exclusion from search failure, timeout, floating arithmetic or sampling.

## Status discipline

- canonical frontier before and after this checkpoint: **4,626 exclusions / 952 survivors / 3,632 whole-state closures**;
- no forced-core closure is promoted here;
- state `152` is excluded from the new threshold-normal-form replay claim;
- the authoritative 306-state workflow `34950746007` remains the coverage authority until it completes and aggregates;
- external mathematical review of the canonical bridge, forced-core routing theorem, and any proposed compression-to-threshold theorem remains OPEN.
