# Canonical Hall marginals — frozen internal audit

14 September 2026.

## Status

The local optimality statements in [`CANONICAL_HALL_MARGINALS.md`](CANONICAL_HALL_MARGINALS.md) have passed a separately written finite verifier.

The internally audited conclusions are:

- every complete type outside the canonical maximal minimizer `M+` has **strictly positive integer** addition marginal;
- its target-capacity gain is at least `n_tau q_tau + 1`;
- this gain is exactly the compatible unsaturated-slack sum from the theorem note;
- every outside source copy therefore has raw directed-compatible degree at least `q_tau+1`;
- removing a type inside `M+` loses at most `n_tau q_tau` receiver capacity;
- types lying in the minimal minimizer `M-` satisfy the strict removal version.

These are exact statements inside the target-Hall model. No whole-state frontier count changes here.

## GitHub Actions record

```text
workflow:        verify canonical Hall marginals
run id:          34848012710
head sha:        f42b818f1cf90f5e8d269eccb44e6be50f5f244b
conclusion:      success
artifact id:     10348686628
artifact name:   canonical-hall-marginals-verification
artifact digest: sha256:78556898b8d77c321df95942c9a7aca925c0245f1084e5619175233c2e38274f
```

## Independent verifier totals

```text
profiles checked:             2,486
exhaustive profiles:          1,286
random profiles:              1,200
feasible profiles:              974
infeasible profiles:          1,512
exterior types checked:       3,142
interior types checked:       5,585
M- types checked:             3,148
maximum distinct types:           7
minimum observed exterior gap:    1
```

The observed minimum exterior Hall-margin increase was exactly `1`, showing the integrality strengthening is sharp on the finite audit suite.

## Trust boundary

This is internal finite verification, not independent third-party review. The result inherits the complete-type Hall theorem and canonical maximal/minimal minimizer theory, and its Murty-Simon application inherits the canonical graph-to-constraint bridge and target-capacity definitions. External mathematical review and novelty assessment remain open.
