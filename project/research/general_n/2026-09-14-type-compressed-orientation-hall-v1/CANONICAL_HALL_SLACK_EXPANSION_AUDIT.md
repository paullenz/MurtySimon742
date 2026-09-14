# Canonical Hall slack expansion — frozen internal audit

14 September 2026.

## Status

The strict exterior slack-expansion theorem in [`CANONICAL_HALL_SLACK_EXPANSION.md`](CANONICAL_HALL_SLACK_EXPANSION.md) has passed a separately written finite verifier.

The internally audited statement is that for the canonical maximal minimum Hall witness `M+`, every nonempty complete-type set `T` outside `M+` satisfies

```text
sum_sigma n_sigma min(s_sigma,K_T(sigma)) >= D(T)+1,
```

where `s_sigma=(P_sigma-y_sigma(M+))_+` is the residual receiver slack left at the canonical cut and `K_T(sigma)` is the exact additional compatible-source multiplicity contributed by `T`, including the diagonal deletion. The dual removal inequalities for subsets of `M+` and the strict version on `M-` were also checked.

No whole-state frontier count changes here.

## GitHub Actions record

```text
workflow:        verify canonical Hall slack expansion
run id:          34849028879
head sha:        e0b58e850a1fcf161fa211271d860f38f743af79
conclusion:      success
artifact id:     10349605144
artifact name:   canonical-hall-slack-expansion-verification
artifact digest: sha256:d3969ae17e063c17b9df5f29db0ca7b3c0f4816b419f05f630b0bcfe98f06a7d
```

## Verification totals

```text
profiles checked:             2,086
exhaustive profiles:          1,286
random profiles:                800
infeasible profiles:          1,193
exterior subsets checked:    11,828
whole-exterior checks:          934
interior subsets checked:    16,121
M- subsets checked:           6,125
maximum distinct types:           7
minimum exterior gap:              1
```

The minimum observed strict exterior gap was exactly one, so the `+1` strengthening is sharp on the audit suite.

## Interpretation

A hypothetical target-Hall-deficient profile must simultaneously support an exact deficient canonical staircase and a strictly expanding residual receiver system on every nonempty exterior type collection. This is stronger than the previously audited one-type marginal conditions and gives a global packing constraint on the complement of the canonical witness.

## Trust boundary

This is internal finite verification, not external mathematical acceptance. The result inherits the complete-type Hall theorem, canonical maximal/minimal minimizer theory and target-capacity model; its Murty-Simon use also inherits the canonical graph-to-constraint bridge. External mathematical review, novelty assessment and independent third-party reproduction remain open.
