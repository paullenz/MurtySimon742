# Exactness of the subset-union Hall envelope

Status: internally proved at the graph-level certificate-selection interface. This statement does not replace the audited bridge from a strict Murty--Simon counterexample to such a selection.

Let C_i be the physical G[B]-edge set capable of carrying label i, and let h_i be the label deficit. Define

H=max_{L subseteq A} (2|union_{i in L}C_i|-sum_{i in L}h_i),

including the empty set, whose value is zero. Let S* be the maximum of sum_i max(0,2x_i-h_i) over assignments in which every physical edge is assigned to at most one incident label i.

## Theorem

S*=H.

## Upper bound

For any assignment, let P be the labels of positive demand. Assigned edges counted for P are distinct and lie in union_{i in P}C_i, so
S <= 2|union_{i in P}C_i|-sum_{i in P}h_i <= H.

## Attainment

Choose an inclusion-minimal subset L attaining H. If H=0, the empty assignment attains it. Otherwise, for every i in L, minimality gives

2|C_i minus union_{j in L minus {i}} C_j|-h_i > 0.

Thus each i has strictly more than h_i/2 edges private to i relative to L. Assign every such private edge to i. Now every label in L is positive. Assign each remaining edge of union_{i in L}C_i to any one incident label. Positivity persists, every union edge is assigned exactly once, and the resulting demand is

2|union_{i in L}C_i|-sum_{i in L}h_i=H.

Therefore the upper bound is sharp.

## Independent finite replay

The first fresh batch's 169 live-strip maximum-root states were all recomputed by explicit count-vector dynamic programming. Every exact maximum equalled H; there were zero mismatches. The largest DP contained 4,150 reachable count vectors. The two scalar E>=15 false positives have exact maxima H=5 and H=7.

## Consequence and trust limit

At this interface, a strict counterexample requiring S>=15 necessarily and sufficiently has H>=15. The remaining challenge is graph structural: exclude H>=15 in the unresolved degree strip, while retaining both parity equality controls. Finite searches below are evidence only.
