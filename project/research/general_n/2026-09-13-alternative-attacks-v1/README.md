# Alternative attacks v1 — quantifier-correct whole-state programme

13 September 2026. **Research checkpoint. Candidate hand lemmas and exact finite reductions; external mathematical review, novelty assessment and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

## Current result

The programme attacks the missing quantifier in fixed-pattern residual arguments: rejecting one selected quasi-edge geometry does not exclude the underlying scalar state because another legal selected geometry may exist.

The canonical ledger now has **977 quantified N34-derived whole-state exclusions**: 18 earlier individually/family audited closures plus a cross-implementation-audited **943-state potential-pair capacity family**. The exact 943 IDs are preserved in [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv), with audit provenance in [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](PAIR_CAPACITY_FRONTIER_AUDIT.md).

The canonical union of all closure lines is recorded in [`WHOLE_STATE_LEDGER.tsv`](WHOLE_STATE_LEDGER.tsv); that ledger, rather than local ordinal wording in individual notes, controls the headline count.

The frozen frontier is now

```text
1,971 exclusions / 3,607 survivors,
```

split as

```text
3,529 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are scalar states in a frozen generalisation experiment, not individual surviving graphs. The fixed-order N34/N35 candidate proofs are unchanged.

The durability checker [`../../../../tools/check_n34_whole_state_ledger.py`](../../../../tools/check_n34_whole_state_ledger.py) protects the 18 earlier closures plus the hash-pinned 943-state potential-pair family and verifies the ledger provenance of every promoted family member. New closures may be added, but an accidental later ledger/README rewrite must not silently remove a preserved closure.

<!-- CANONICAL-WHOLE-STATE-LEDGER:START -->
### Canonical closure ledger

The canonical [`WHOLE_STATE_LEDGER.tsv`](WHOLE_STATE_LEDGER.tsv) contains **961 quantified whole-state exclusions**. The large current family is documented in [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](PAIR_CAPACITY_FRONTIER_AUDIT.md), with exact IDs in [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv).

Two full-frontier implementations—expanded source vectors with pairwise directed compatibility, and independent `(rho,q)` type-count enumeration using the closed-form potential degree—agree exactly on the 943 promoted exclusions and their exhaustive certificate statistics.

Canonical frontier: **1,971 exclusions / 3,607 survivors** (`3,545` N34-derived plus `78` N35-derived).

The durability checker [`../../../../tools/check_n34_whole_state_ledger.py`](../../../../tools/check_n34_whole_state_ledger.py) hash-pins the 943-state certificate and checks ledger provenance.
<!-- CANONICAL-WHOLE-STATE-LEDGER:END -->

## Core selected-excess mechanism

See [`SELECTION_FREE.md`](SELECTION_FREE.md). For every selected positive-demand incidence,

```text
p_u-rho_u+1 <= e_i := x_i-s_i.                       (1)
```

If

```text
h_l=#{i:e_i>=l},
```

then

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

The early whole-state closures used the `l=2` member as a high-excess tail screen. The later work retains progressively more of the information in (1) instead of summing it away.

## Current refinement hierarchy

The present architecture is:

1. **Refined baseline-three accounting** — [`REFINED_BASELINE3_LEMMA.md`](REFINED_BASELINE3_LEMMA.md) keeps the exact selected-source score `rho_u+q_u-1` and the negative contribution of zero-excess demand-two labels.
2. **Exact-demand endpoint order** — [`ZERO_EXCESS_ENDPOINT_ORDER.md`](ZERO_EXCESS_ENDPOINT_ORDER.md) gives `C_i>=max(d,L_(d))` for a zero-excess demand-`d` label.
3. **Capacity-order endpoint bound** — [`CAPACITY_ORDER_ENDPOINT_LEMMA.md`](CAPACITY_ORDER_ENDPOINT_LEMMA.md) converts the existence of `d` cheap eligible endpoints into a scalar incoming-capacity loss and gives the exact minimum `d`-th endpoint load inside the independent source-cap relaxation.
4. **Demand-compatible excess order** — [`DEMAND_COMPATIBLE_EXCESS_ORDER.md`](DEMAND_COMPATIBLE_EXCESS_ORDER.md) replaces global threshold counts by the compatible excess order statistic. In an all-positive-demand branch,

   ```text
   p_u <= rho_u-1 + eta_(q_u)^(rho_u),
   ```

   where `eta_q^(rho)` is the `q`-th largest excess among labels with `0<s_i<=rho`.
5. **Threshold incidence capacity** — [`THRESHOLD_INCIDENCE_CAPACITY.md`](THRESHOLD_INCIDENCE_CAPACITY.md) accounts for competition between different sources for the finite selected-degree capacity of high-excess compatible labels:

   ```text
   sum_{u:q_u>0, rho_u<=R, L_u>=ell} q_u
    <= sum_{i:0<s_i<=R, e_i>=ell} x_i,
   ```

   with `L_u=max(0,p_u-rho_u+1)`.
6. **Forced low-score incidence** — [`FORCED_INCIDENCE_SCORE.md`](FORCED_INCIDENCE_SCORE.md) turns a Hall/pigeonhole overload into a sharper bound on a particular label's `d_i` when that label is forced to receive an incidence from a low-score source.
7. **Orientation target capacity** — [`ORIENTATION_TARGET_CAPACITY.md`](ORIENTATION_TARGET_CAPACITY.md) links the selected-label constraints back to the actual missing-edge orientation. For every oriented missing pair `u->w`, `q_u-1<=q_w+rho_w`; hence low-cross-degree targets have a Hall-type incoming-capacity restriction.
8. **Exact orientation Hall flow** — [`ORIENTATION_FLOW_HALL.md`](ORIENTATION_FLOW_HALL.md) keeps the companion endpoint inequality, proves the exact directed compatibility relation and records why the full relation is two-dimensional rather than Ferrers in general.
9. **Total-excess source capacity** — [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md) interpolates the exact-demand incoming cap across every total-excess layer.
10. **Potential-pair capacity** — [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md) forgets the orientation but retains which unordered pairs could possibly be missing, giving `p_u+q_u<=d_KD(u)`; this is the mechanism behind the audited 943-state frontier family.
11. **Low-c/high-q threshold obstruction** — [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md) extracts the compact all-order candidate inequality `Q+ell_r*u_r<=binom(b,2)` for every threshold `r`.

The progression is therefore

```text
threshold scarcity
 -> exact-demand availability
 -> endpoint order statistics
 -> demand-compatible excess order
 -> incidence-capacity competition
 -> forced low-score rigidity
 -> missing-edge orientation / flow capacity
 -> potential-pair capacity
 -> low-c/high-q threshold obstruction.
```

## Whole-state exclusions

### State 227

[`STATE_227_WHOLE_STATE.md`](STATE_227_WHOLE_STATE.md) / [`STATE_227_REPLAY.md`](STATE_227_REPLAY.md)

```text
s=2^4,3^11,
rho=1^7,2,3^10,
r=39, S=41.
```

Exact integer enumeration covers the low-excess region; two equality profiles are removed by hand rigidity. The relaxed threshold tail closes the remaining feasible excess layers. Frontier step: `994/4,584 -> 995/4,583`.

### State 279

[`STATE_279_WHOLE_STATE.md`](STATE_279_WHOLE_STATE.md) / [`STATE_279_REPLAY.md`](STATE_279_REPLAY.md)

```text
s=2^3,3^12,
rho=1^7,3^11,
r=40, S=42.
```

Exact low-excess replay plus three rigidity cases closes the low region; the threshold tail closes the rest. This state exposed the first reusable zero-excess source-availability mechanism. Frontier: `995/4,583 -> 996/4,582`.

### State 588

[`STATE_588_WHOLE_STATE.md`](STATE_588_WHOLE_STATE.md) / [`STATE_588_REPLAY.md`](STATE_588_REPLAY.md)

```text
s=3^15,
rho=1^5,2,3^12,
r=43, S=45.
```

A cheap tail screen leaves only two exceptional excess layers; exact replay closes them, and the one coarse low-excess equality is excluded by the cross-degree sum. Frontier: `996/4,582 -> 997/4,581`.

### State 526

[`STATE_526_WHOLE_STATE.md`](STATE_526_WHOLE_STATE.md) / [`STATE_526_REPLAY.md`](STATE_526_REPLAY.md)

```text
s=2,3^14,
rho=1^5,2^2,3^11,
r=42, S=44.
```

The lone coarse equality forces all fourteen zero-excess demand-three labels onto high-load sources, giving a direct cross-degree contradiction. Frontier: `997/4,581 -> 998/4,580`.

### State 382

[`STATE_382_WHOLE_STATE.md`](STATE_382_WHOLE_STATE.md) / [`STATE_382_REPLAY.md`](STATE_382_REPLAY.md)

```text
s=2^2,3^13,
rho=1^6,2,3^11,
r=41, S=43.
```

Retaining the negative baseline-three contribution of zero-excess demand-two labels makes the refined tail strict; exact low-excess profiles are already excluded. Frontier: `998/4,580 -> 999/4,579`.

### State 519

[`STATE_519_WHOLE_STATE.md`](STATE_519_WHOLE_STATE.md) / [`STATE_519_REPLAY.md`](STATE_519_REPLAY.md)

```text
s=2,3^14,
rho=1^6,3^12,
r=42, S=44.
```

Three exceptional layers survive the coarse profile relaxation. The exact-demand endpoint-order mechanism closes them by optimizing the two eligible source endpoints jointly with the incoming ledger. GitHub Actions run `34773463128` is green on the state-519 proof-critical stages. Frontier: `999/4,579 -> 1,000/4,578`.

### States 230, 282 and 385 — adjacent-family closure

See [`INCIDENCE_CAPACITY_FAMILY_CLOSURE.md`](INCIDENCE_CAPACITY_FAMILY_CLOSURE.md) and the final exact verifier [`scan_incidence_capacity_family.cpp`](scan_incidence_capacity_family.cpp).

The profiles are

```text
state 230: s=2^4,3^11, rho=1^6,2^3,3^9,  r=39, S=41
state 282: s=2^3,3^12, rho=1^6,2^2,3^10, r=40, S=42
state 385: s=2^2,3^13, rho=1^5,2^3,3^10, r=41, S=43
```

The demand-compatible excess-order cap reduces the old low-excess obstruction dramatically. Threshold incidence capacity and forced low-score source incidences remove the last equality cases.

A complete local replay of

```text
3 states * 35 excess layers = 105 checks
```

has a positive gap in every layer; the minimum whole-layer gap is `+1` for each state. The committed workflow [`scan-incidence-capacity-family.yml`](../../../../.github/workflows/scan-incidence-capacity-family.yml) recompiles the verifier and independently requires all 105 gaps to be positive.

Frontier steps:

```text
state 230: 1,000/4,578 -> 1,001/4,577
state 282: 1,001/4,577 -> 1,002/4,576
state 385: 1,002/4,576 -> 1,003/4,575
```

The four active companions identified by the original adjacent-family scan,

```text
230, 282, 385, 519,
```

are now all closed.

### Latest closures: states 77 and 60

The joint endpoint-class Hall refinement makes every formerly weak positive-excess layer strict in both states, leaving only `E=0`. The orientation target-capacity lemma then closes the exact-demand fibres without fixing selected-label identities.

The exact verifier [`verify_e0_orientation_capacity.py`](verify_e0_orientation_capacity.py) enumerates the full nondecreasing `q` frontier:

```text
state 77: 201,670 E=0 q-profiles, 0 pass, best cut 32 < Q=38;
state 60: 253,001 E=0 q-profiles, 0 pass, best cut 31 < Q=37.
```

Thus even the closest profile has a six-incidence target-capacity deficit. Whole-state records are [`STATE_77_WHOLE_STATE.md`](STATE_77_WHOLE_STATE.md) and [`STATE_60_WHOLE_STATE.md`](STATE_60_WHOLE_STATE.md).

## Default family-screening strategy

The programme should now use the following order:

1. run the refined threshold/baseline screen;
2. add capacity-order endpoint availability whenever exact-demand labels occur;
3. replace global excess counts by demand-compatible excess order statistics;
4. exact-enumerate only branches still non-strict;
5. impose threshold selected-incidence capacities;
6. impose missing-edge orientation target-capacity cuts before escalating to a graph-level model;
7. when equality survives, use forced-incidence/source-score rigidity or the strongest exact Hall/flow test available;
8. only then return to stronger shared-residual/pair geometry.

The frozen survivor extraction utility [`extract_frozen_survivors.py`](extract_frozen_survivors.py) is transport/replay infrastructure only; it does not itself apply a theorem.

## General lesson from the 16 closures

The newer closures suggest that the useful object is not merely a scalar ledger but a **capacitated selected source-label incidence system coupled to a capacitated orientation of the missing-edge graph**.

- high excess is scarce and limits incoming load;
- low residual-degree sources see only restricted demand classes;
- labels have finite selected-degree capacity `x_i`, so sources compete for compatible high-excess labels;
- exact-demand labels require enough low-p endpoints;
- endpoint lower and upper order statistics interact through the same source margins;
- equality can force low-score sources onto specific labels, sharply reducing positive correction bounds;
- a source with large `q_u` cannot orient a missing edge into a target with insufficient cross-degree, producing a second Hall/flow constraint on the same margins.

The natural generalisation is therefore Hall/flow-like rather than another collection of isolated state-specific inequalities. The next structural question is whether the allowed source-target relation has enough Ferrers/threshold structure that the full orientation feasibility problem reduces to a small family of prefix cuts.

## Raw candidate capacity and independent route

The selection-free package also gives raw candidate-label subset capacities; these remain a secondary graph-level projection route without choosing representatives.

[`MAXCUT_ROUTE.md`](MAXCUT_ROUTE.md) records the independent identity

```text
e(G)=|X||Y|+I-M.
```

A direct one-edge/one-nonedge matching proof is false and remains preserved as a failed route; any viable maximum-cut proof must use aggregate charging or stability.

## Audit boundaries and current priority

[`AUDIT.md`](AUDIT.md) records invalidated shortcuts and proof-status boundaries. None of the 16 whole-state closures relies on numerical solver infeasibility: proof-critical computation is exact integer enumeration/dynamic programming, with explicit structural arguments at equality boundaries.

External mathematical review of the canonical bridge and all new lemmas remains open. Independent computational reproduction remains open until a separate environment has replayed the committed artifacts.

**Current priority:** generalise and red-team the orientation target-capacity lemma; derive the strongest exact Hall/flow or threshold-prefix formulation justified by the canonical bridge; then combine it with the joint endpoint-class and incidence-capacity machinery to rescan the remaining **3,607** frozen scalar survivors. States 77 and 60 are closed and must not be retargeted as live obligations.

## Post-pair relational recovery promotion — 14 September 2026

The cancelled pilot has been recovered under the audit protocol in [`POST_PAIR_RELATIONAL_RECOVERY.md`](POST_PAIR_RELATIONAL_RECOVERY.md). Sixteen states are now promoted after exact agreement between the primary scanner and an independent type-count implementation. The frozen aggregate certificate is [`POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv`](POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv), SHA-256 `c1ce4e645edf9dcc3e2f39ef42bd85030449b161549978877eb2e15ab2abe832`. Canonical frontier is **1,971 exclusions / 3,607 survivors**.

The earlier low-residual-reservoir scan remains a preserved negative result: 3,421 of the then-current 3,623 states were in scope, but it excluded zero whole states. The active route is therefore the stronger relational Hall/min-cost layer, not further tuning of that coarse reservoir bound.
