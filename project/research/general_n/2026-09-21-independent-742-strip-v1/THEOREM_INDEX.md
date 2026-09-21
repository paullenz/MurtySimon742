# Theorem and dependency index

## Candidate theorem A — improved maximum-degree thresholds

`FIRST_OBSTRUCTION_AND_39_67.md`

```text
n>=6, Delta>=250n/429   =>  e(G)<floor(n^2/4),
n>=4681, Delta>=39n/67  =>  e(G)<floor(n^2/4).
```

The full exact threshold/order ladder is in the proof.  Dependencies:

1. shared graph-to-profile lemma from the canonical `7/12` package;
2. rational scalar certificate `f(x)<121/1569`;
3. preserved candidate `7/12` theorem for the upper sub-branch; and
4. elementary convex degree assembly.

Trust: internal candidate, exact arithmetic green, external review open.

## Obstruction B — full-Hall rational plateau

`FULL_HALL_PLATEAU_OBSTRUCTION.md`

A demand-`1/4` plateau with `b/a=139/100` lies above the Turan requirement
but survives every aggregated condition tested, including simultaneous
selected/residual incidence graphicality and the full selected-incidence Hall
system.  It is not an actual graph.

Trust: exact asymptotic relaxation obstruction, not graph realizability.

## Candidate theorem C — selected-signature rigidity

`SIGNATURE_UNION_RIGIDITY.md` and `ROBUST_SIGNATURE_STABILITY.md`

For physical selected-source signatures `X_i` and total incidence signatures
`Y_i`, every F-edge `ij` forces `X_i subset Y_j`.  Consequently

```text
|union_{i in N_F(j)} X_i| <= C_j
```

and the exact global second-moment/codegree inequality (SU5) holds.  Plateau
bands therefore force linear average F-codegree; endpoint caps make the bound
unconditional in the stated band.

Trust: direct candidate set-theoretic consequence of the inherited raw
A-side domination lemma.

## Candidate corollary D — positive-density high-codegree cluster (scope corrected 22 September)

`POSITIVE_DENSITY_CODEGREE_CLUSTER.md`

Under the full exact plateau normalization stated in the corrected note
(including both selected-mass bounds, the lower endpoint/degree hypotheses and
the upper endpoint/degree cap), asymptotically more than 21.7% of selected pair
occurrences—and at least `0.00351a^2` distinct pairs—have F-codegree at least
`a/5`.  The original shorthand "plateau band" omitted hypotheses and must not
be used as a broader theorem.

Trust: exact arithmetic consequence of C under the corrected joint
hypotheses; not a general profile-band theorem.

## Hostile replay

`GRAPH_TO_THRESHOLD_HOSTILE_REPLAY.md`

The shared graph-to-profile spine was rederived without finding a blocker.
The supplement step requires the explicit residual-or-selected dichotomy
recorded there.  This is internal replay, not external verification.

## Next dependency to prove

Use raw D2C criticality to upper-bound or classify co-selected label pairs with
F-codegree at least `a/5`.  Beating the `0.00351a^2` lower density closes the
rational plateau band; a bounded blow-up classification would instead provide
the requested near-`1/2` survivor rigidity.
