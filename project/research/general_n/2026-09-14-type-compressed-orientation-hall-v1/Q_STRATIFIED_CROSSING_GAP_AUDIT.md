# q-stratified crossing-gap identity — frozen internal audit

14 September 2026.

## Status

[`Q_STRATIFIED_CROSSING_GAP.md`](Q_STRATIFIED_CROSSING_GAP.md) has passed a separately written finite verifier.

The internally audited statement is that, in the current post-pair target-cap model, for every labelled Hall source set `S`, the gap between the exact receiver capacity and the q-only comonotone receiver-layer upper bound is exactly

```text
C_q(S)=sum_{q,m} min(H^S_{q,m},L^O_{q,m}),
```

where `H^S_{q,m}` counts selected targets in the equal-`(q,m)` preincoming block with `P>=m`, and `L^O_{q,m}` counts unselected targets in the same block with `P<m`.

Equivalently,

```text
U_q(S)-H(S)=C_q(S).
```

This identifies the exact information lost by forgetting selected status after retaining q. It does **not** assert that `C_q=0` universally.

## GitHub Actions record

```text
workflow:        verify q-stratified crossing gap
run id:          34858775228
head sha:        16ba2b1b7ec12e50a1c73eb1c247d6d78f283e93
conclusion:      success
artifact id:     10354099276
artifact name:   q-stratified-crossing-gap-verification
artifact digest: sha256:31f8e577259699dbac4779f8227d98d5dced610ad1abf1c9d91fa320d6dc6be6
```

## Verification totals

```text
exhaustive cases:                       384,612
exhaustive maximum length:                    5
exhaustive value range:                    0..4
exhaustive positive-gap cases:           60,301
exhaustive maximum gap:                       2
nontrivial crossing blocks encountered: 606,568
random trials:                           20,000
random seed:                            7420914
random positive-gap cases:                4,142
random maximum gap:                           5
result:                                    PASS
```

The exhaustive verifier ranges over every nondecreasing target-cap sequence and every nondecreasing pre-diagonal incoming sequence through length five with values in `0..4`, together with every selected-bit pattern compatible with nonnegative actual incoming counts. It compares direct receiver capacity, q-only comonotone rearrangement and the claimed crossing statistic exactly.

The random phase independently samples longer blocks through length 24 and larger values through 14.

The many positive-gap cases are an important hostile check: the verifier is not merely reproducing the `C_q=0` phenomenon seen in the Murty frozen pilot.

## Preserved negative example

[`Q_STRATIFIED_EXACTNESS_COUNTEREXAMPLE.md`](Q_STRATIFIED_EXACTNESS_COUNTEREXAMPLE.md) gives a concrete canonical Hall profile with

```text
C_q=1,
U_q-H=1,
```

so q-only exactness is explicitly not promoted as an abstract theorem.

## Research consequence

The remaining Murty-specific target is now sharply stated:

```text
control or exclude C_q>0
```

using the canonical graph-to-constraint bridge, selected-excess budget, residual/source caps and canonical maximality. [`CANONICAL_EQUAL_Q_SWAP_RIGIDITY.md`](CANONICAL_EQUAL_Q_SWAP_RIGIDITY.md) gives the first structural consequence of `C_q>0`: every crossing forces an equal-q swap saturation wall.

## Trust boundary

This is internal finite verification of the exact crossing identity, not external mathematical acceptance. The result inherits fixed-q monotonicity of the current post-pair target cap and the exact directed compatibility relation. Its Murty-Simon application inherits the canonical graph-to-constraint bridge. External mathematical review, novelty assessment and genuinely independent third-party reproduction remain open.
