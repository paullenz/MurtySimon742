# Compatible-copy staircase-band Hall — frozen internal audit

14 September 2026.

## Status

The compatible-copy band theorem in [`COMPATIBLE_COPY_BAND_HALL.md`](COMPATIBLE_COPY_BAND_HALL.md) has now passed a separately written, dependency-free internal finite verifier.

This promotes the **compatible-copy aggregation lemma itself** into the package's internally audited structural chain. It does **not** promote any whole-state exclusion, does not alter the canonical `3,607` survivor frontier, and is not external mathematical acceptance.

## GitHub Actions record

```text
workflow:        verify compatible-copy band Hall refinement
run id:          34844598113
head sha:        af7a66d6e78ca3120a641abbb1827d2ab662acfb
conclusion:      success
artifact id:     10347286810
artifact name:   compatible-copy-band-hall-verification
artifact digest: sha256:ae554757781c696e75f52450266db7ce0f928c86465e1dc57a1b55b7e583ec06
```

## Independent verifier

[`verify_compatible_copy_band_hall.py`](verify_compatible_copy_band_hall.py) deliberately does not import the earlier Hall or staircase-band verifiers. It reconstructs:

- labelled directed compatibility;
- exact selected-source max flow;
- sharp-hardness up-sets;
- canonical staircase bands;
- coarse band capacities;
- compatible-copy band capacities;
- refined band max flow.

The green run reported:

```text
profiles checked:                         2,715
sharp up-sets checked:                   43,988
explicit labelled-pair capacity checks: 636,193
coarse monotonicity checks:              636,193
exact-to-refined flow-order checks:       43,988
state-226 fixture checks:                      1
```

The verifier checked that:

1. `K_{i,sigma}=n_sigma(C_{i,sigma}-delta_{i,sigma})` equals the explicit number of labelled compatible source-target pairs from band `i` to target type `sigma`;
2. every compatible-copy band edge capacity is at most the corresponding coarse generator-band capacity;
3. exact selected-source max flow never exceeds refined compatible-copy band max flow;
4. exact selected-source feasibility implies compatible-copy band feasibility;
5. the frozen state-226 fixture has selected demand `39`, exact selected-source flow `38`, and refined band flow `38`.

For state 226, the problematic band-1 to target-type-1 capacity is corrected to exactly `1`, removing the five spurious incidences identified in the dedicated diagnostic.

## Trust boundary

This is internal finite verification of the aggregation theorem, not independent third-party reproduction. The result inherits the upstream graph-to-constraint bridge, target-capacity definitions, sharp-hardness witness construction and staircase-band definitions. External mathematical review and novelty assessment remain open.

The separate full frozen-pilot replay of the compatible-copy instrumentation remains a distinct audit task. Until that replay is frozen, the `205,919/205,919` pilot-detection statement remains supported by the verified theorem plus the already frozen coarse-band pilot and state-226 diagnostic/monotonicity argument, rather than by a fresh single-pass compatible-copy pilot artifact.
