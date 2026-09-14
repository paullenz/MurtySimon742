# Exterior-slack sharp-upset reduction — frozen internal audit

14 September 2026.

## Status

[`EXTERIOR_SLACK_UPSET_REDUCTION.md`](EXTERIOR_SLACK_UPSET_REDUCTION.md) has passed a separately written finite verifier.

The internally audited statement is that the strict residual-slack expansion outside the canonical maximal Hall witness need only be checked for nonempty sharp-hardness up-sets under the residual-cap order

```text
x >=_s y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and s_x>=s_y)].
```

Equivalently, if any nonempty exterior set has residual-slack margin at most zero, then a nonempty residual sharp up-set has residual-slack margin at most zero. The audit explicitly includes the delicate case in which the global residual minimum is zero and the empty set is also a minimizer.

No whole-state frontier count changes here.

## GitHub Actions record

```text
workflow:        verify exterior slack upset reduction
run id:          34851263359
head sha:        c9c32ae450cd247a2a8cd29b49544384c9641de7
conclusion:      success
artifact id:     10351022454
artifact name:   exterior-slack-upset-reduction-verification
artifact digest: sha256:07593a70d66198fad7a20e5f8d3d1a18820c0e675844d406baee87c72d9822ae
```

## Verification totals

```text
canonical profiles checked:                 2,314
canonical profiles with nonempty exterior:  1,263
canonical exterior subsets checked:        32,245
minimum canonical exterior margin:              1
residual profiles checked:                  2,314
residual violation profiles:                1,787
  negative-minimum cases:                   1,236
  zero-margin cases:                          551
random trials:                              1,600
```

The verifier checked that:

1. the union of labelled Hall minimizers is the unique maximal minimizer;
2. canonical labelled `M+` is a sharp up-set and never splits identical types;
3. every nonempty labelled exterior set has residual-slack margin at least one;
4. residual-slack margin is exactly the canonical addition marginal;
5. a nonempty residual margin `<=0` exists iff a nonempty residual sharp up-set with margin `<=0` exists;
6. zero-margin violations still yield a nonempty maximum-cardinality sharp-upset minimizer.

## Interpretation

A hypothetical canonical Hall failure can now be represented by two coupled staircase systems:

```text
primary P-staircase M+           deficient,
exterior residual-s staircase    required to remain strictly expanding.
```

This removes arbitrary exterior subset search from the structural formulation. The next analytic objective is to show that the Murty residual/source-cap budgets force some residual-slack staircase to violate the required `+1` expansion whenever the primary staircase is deficient.

## Trust boundary

This is internal finite verification, not external mathematical acceptance. The result inherits the labelled Hall submodularity, sharp exchange theorem, target-capacity model and, for its Murty-Simon application, the canonical graph-to-constraint bridge. External mathematical review, novelty assessment and genuinely independent third-party reproduction remain open.
