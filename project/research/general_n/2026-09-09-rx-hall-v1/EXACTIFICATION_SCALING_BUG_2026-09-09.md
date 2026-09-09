# Shared-potential exactification scaling bug — 9 September 2026

## Status

A real verification bug was found in the recent **shared staircase-potential exactification layer**. The affected exactification outputs must not be cited as exact rational/integer feasibility evidence unless and until replaced by a corrected rerun.

This finding does **not** affect:

- the fixed-order n=29 or n=30 candidate proofs;
- the exact integer-Farkas RX-Hall / pairwise contradiction certificates;
- the Hall projection or pairwise staircase validity lemmas;
- the floating-point support/minimum-support reconnaissance results.

It affects only the later step that attempted to turn a floating feasible shared-potential point into an exact rational point by scaling and rounding.

## Bug

The continuous shared-envelope LP has homogeneous structural rows with RHS `0` and one nonhomogeneous margin row per profile with RHS `-1`.

The old exactifiers formed integer numerators

```text
X_j = round(scale * x_j)
```

with intended rational interpretation `X_j / scale`.

For homogeneous rows, checking the integer numerator against RHS `0` is correct.

For a margin row, however, exact feasibility of `X/scale` requires

```text
sum a_j X_j <= -scale,
```

not merely

```text
sum a_j X_j <= -1.
```

The old scripts incorrectly compared the scaled numerator to the unscaled RHS `-1`. Therefore a reported integer margin such as `-999899` at `scale=1000000` corresponds to rational margin `-0.999899`, which does **not** satisfy the required `<= -1` inequality.

## Discovery

The bug was exposed by an internal consistency contradiction: the purportedly exact 14-shape n=29 common potential claimed to cover hard positions 0 and 1, while a later scan that froze its reported staircase weights could not find scalar/envelope feasibility for those same profiles. Auditing the scaling arithmetic identified the RHS error above.

## Affected recent outputs

At minimum, the following shared-potential exactification checkpoints were produced by the faulty acceptance rule and are **superseded / invalid as exact-feasibility evidence** pending corrected reruns:

- `checkpoints/N30_GLOBAL_NINE_EXACT_RUN_34362935743.json`;
- `checkpoints/N30_SHARED_PRUNED_EXACT_RUN_34362519565.json` (12-shape pruned support, if cited);
- `checkpoints/N29_COMMON_ACTIVE_EXACT_RUN_34369321096.json`;
- `checkpoints/N29_COMMON_14_EXACT_RUN_34369583832.json`.

Any downstream claim that specifically freezes staircase weights from one of those exactification outputs must be re-audited after corrected exactification. In particular, the later 994/996 n=29 fixed-weight scan is useful diagnostics but must not be described as freezing **validated exact** weights until its source checkpoint is corrected.

## Correction

The corrected exactifier will:

1. retain a denominator `scale` explicitly;
2. use a safety boost greater than one when converting a continuous feasible point to a rational proposal, which is valid because the structural rows are homogeneous and strengthens the negative profile margins;
3. check every row against the correctly scaled RHS `rhs * scale`;
4. repair only homogeneous envelope rounding residuals;
5. recheck every bound, every homogeneous row and every profile margin using Python integer arithmetic;
6. accept only when each profile margin numerator is at most `-scale`.

Historical faulty checkpoints are retained for auditability rather than deleted or silently rewritten.
