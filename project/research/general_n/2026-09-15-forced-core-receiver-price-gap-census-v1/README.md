# Forced-core receiver-price gap census v1

Date: 15 September 2026.

Status: **research census launched; no canonical promotion and no unrestricted theorem claim.**

This package stress-tests the aggregate receiver-capacity / receiver-price necessary conditions from [`../2026-09-15-forced-core-canonical-audit-v2/RECEIVER_PRICE_LEMMA.md`](../2026-09-15-forced-core-canonical-audit-v2/RECEIVER_PRICE_LEMMA.md) against the complete type-profile universes of all **170 forced-core discovery candidate exclusions**.

The purpose is to answer one sharply defined question:

> Among profiles rejected by the exact labelled receiver-partition DP, is any rejection genuinely invisible to the scalar capacity inequality and fractional receiver-price inequality?

The earlier local stress test had eight complete exclusions with

```text
partition_only_fail      = 0
partition_high_only_fail = 0
```

This package replaces that small sample by a full 170-state census.

## Classification

For every enumerated type profile, the scanner first checks the aggregate conditions.

1. **`CAPACITY_SCALAR`** if
   \[
   \sum_v \min(c_v,m)<hm.
   \]
2. **`HIGH_RECEIVER_PRICE`** if the exact fractional cover optimum `F_tau` gives
   \[
   R_\tau-\lceil F_\tau\rceil<D_\tau.
   \]
3. Only if neither aggregate condition rejects the profile does the scanner call the exact symmetric labelled-partition DP from the independent type-multiplicity implementation.
   - an exact capacity failure there is counted as `partition_only_fail`;
   - an exact high-threshold failure there is counted as `partition_high_only_fail`.

A nonzero partition-only count is **not** treated as a failed experiment. It is a useful counterexample to aggregate exactness and is preserved in `GAP_WITNESSES.tsv` with the first exact certificate and compressed type profile.

## Exact arithmetic for the fractional cover

The receiver-price relaxation has one covering constraint and box constraints `0<=x_v<=1`. Its optimum is the fractional-knapsack optimum obtained by sorting receivers by `loss_v/c_v`. The implementation uses exact integer cross-products for the ordering and computes `ceil(F_tau)` without floating-point arithmetic.

## Audit against the authoritative discovery

The census reuses the pinned 306-state discovery inputs and isolates the same 170 candidate states through the audit-v2 preparation code. Candidate states are complete enumerations: unlike surviving states, their primary scans did not terminate early on a witness.

For every state the aggregate gate requires:

- the same `S` and `Emax` as the authoritative discovery;
- the **exact same complete `profiles_tested` count**;
- internal profile accounting
  ```text
  aggregate_fail + partition_gap_fail + exact_core_pass = profiles_tested;
  ```
- internal core accounting
  ```text
  aggregate_fail + partition_gap_fail = predicted_core_fail;
  ```
- and, critically,
  ```text
  predicted_core_fail = authoritative primary core_fail.
  ```

That final equality prevents an implementation error in the aggregate test from masquerading as successful coverage: aggregate false positives would make the predicted core-failure total exceed the authoritative exact total.

The workflow prioritizes states whose authoritative final core certificate has `h=5` or `h=4`, then enumerates the remainder. Jobs are deliberately capped below the audit-v2 parallelism so the independent 170-state certification run remains the first operational priority.

## Interpretation gate

If the final summary reports

```text
ZERO_GAP_ON_COMPLETE_170_CANDIDATE_UNIVERSES
```

then the correct conclusion is **finite empirical exactness on these 170 complete candidate universes**. It would be strong evidence for seeking a Hall/flow-duality or integrality theorem explaining why the fractional receiver-price relaxation is exact in the structured forced-core setting. It is **not**, by itself, a proof of such a theorem.

If the summary reports

```text
PARTITION_ONLY_GAPS_FOUND
```

then the first priority becomes studying the minimal preserved gap witness and identifying the missing structural statistic.

## Canonical status

This census does not promote any state. The canonical ledger remains

```text
4,626 exclusions / 952 survivors / 3,632 whole-state closures
```

until the separate full independent audit of the 170 forced-core candidates completes and a reviewed promotion commit is made.
