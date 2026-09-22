# Residual-mass-six product-equality core screen

22 September 2026. Exact enumeration of an optimistic necessary relaxation. Candidate cores are not graphs. This does not extend the equality theorem beyond S<=5.

At r=6 and t=0, screen_r6_equality.py enumerates every residual partition, every simple graph on its positive-residual support, and every possible N-slack vector consistent with the exact core ledger. For R_i>=2 in N, it optimistically permits enough zero-residual neighbours to realize any degree up to R_i. Unit columns cannot have zero-residual neighbours by the proved (0,1)-edge exclusion. It also imposes edge charge and selected-source capacity.

Previously proved strict cases are removed: independent residual support, a unit-residual cycle component, and the all-unit equality case. The remaining exact relaxation counts are:

- (3,1,1,1): 7 labelled candidates in 3 equal-weight permutation orbits;
- (2,2,1,1): 1 candidate/orbit;
- (2,1,1,1,1): 109 labelled candidates in 9 orbits;
- every other partition: zero candidates.

Thus product equality at residual mass six is reduced to 13 optimistic residual-core/slack orbits. The output records core edges, core and actual degrees, P/N split, slack vector, selected lower bounds and labelled multiplicity.

This is deliberately only a classification handoff. The slack vector does not encode the actual zero-residual attachment hypergraph. Physical B-source states, legal supplements, deletion criticality, maximum-root realizability and balanced-equality control must still be imposed. Zero survivors in a subsequent source screen could close r=6 equality; surviving source patterns would remain non-graph candidates.

Exact output: R6_EQUALITY_CORE_SCREEN.json. Reproduce with python screen_r6_equality.py. Next: screen the 13 orbits through exact residual source-state multisets, handling zero-residual attachments only through constraints that are necessary for every realization.
