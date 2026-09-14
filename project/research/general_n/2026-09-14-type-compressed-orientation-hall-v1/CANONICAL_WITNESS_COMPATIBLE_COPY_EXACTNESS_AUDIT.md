# Canonical-witness compatible-copy exactness — frozen internal audit

14 September 2026.

## Status

The theorem in [`CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md`](CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md) has passed a separately written, dependency-free finite verifier.

The promoted internal structural statement is:

> For the canonical maximal minimum Hall witness `M+`, the all-bands cut of the compatible-copy staircase-band network has exactly the original Hall margin `F(M+)`. Consequently the compatible-copy band network built from `M+` is feasible if and only if the original target-Hall network is feasible.

This is an exact statement inside the target-capacity Hall relaxation. It does not alter the canonical whole-state frontier and is not external mathematical acceptance.

## GitHub Actions record

```text
workflow:        verify canonical witness compatible-copy exactness
run id:          34847381427
head sha:        04050620ff5a03414bcb0a31241c1ba96cd3fec3
conclusion:      success
artifact id:     10348551926
artifact name:   canonical-witness-compatible-copy-exactness-verification
artifact digest: sha256:f20e97ec0021e788e0903a36e8ae67235e747dc3c7581b693fd6af76de7504d3
```

## Independent verifier totals

[`verify_canonical_witness_compatible_copy_exactness.py`](verify_canonical_witness_compatible_copy_exactness.py) reported:

```text
profiles checked:                              2,486
exhaustive profiles:                           1,286
random profiles:                               1,200
feasible profiles:                               968
infeasible profiles:                           1,518
canonical M+ nonempty:                         2,035
whole-staircase identity checks:               2,486
canonical feasibility-equivalence checks:      2,486
maximum distinct types tested:                     7
maximum vertices tested:                           7
```

The verifier independently reconstructed complete-type Hall margins, the union of all minimizers `M+`, sharp-hardness upset status, the generator staircase, compatible-copy band capacities, labelled selected-source max flow and refined-band max flow.

It checked that:

1. the union of minimum complete-type Hall cuts remains a minimum cut;
2. `M+` is a sharp-hardness up-set;
3. the all-bands compatible-copy margin equals `F(M+)` exactly;
4. labelled selected-source flow never exceeds compatible-copy band flow;
5. the compatible-copy network built from `M+` is feasible exactly when the original target-Hall system is feasible;
6. every deficient canonical `M+` is rejected by its all-bands cut.

## Consequence for the 15-state pilot

The previously observed `205,919/205,919` compatible-copy detection count is now a theorem-level consequence of the internally audited structural chain, not merely an empirical extrapolation. A fresh single-pass pilot replay remains useful as an integration audit of the scanner implementation.

## Trust boundary

This audit is internal finite verification. It inherits the upstream canonical bridge, target-capacity model, complete-type Hall theorem, sharp-hardness theorem and canonical maximal-witness theorem. External mathematical review, novelty assessment and independent third-party reproduction remain open.
