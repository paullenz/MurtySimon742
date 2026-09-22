# Residual mass six: supplement obstruction and equality closure

22 September 2026. Internal computer-assisted candidate proof. This closes the current r=6 product-equality kernels at a necessary B-layer, not by claiming that abstract source states are graphs. External adversarial review remains required.

## Supplement forcing rule

Fix an active physical B-source u and let L_u be the C-labels at which u is selected. If a B-edge uw is present, define

F(u,w) = {(u,i): i in L_u and w is adjacent to i}
         union {(w,j): j in L_w and u is adjacent to j}.

Every incidence in F(u,w) is a selected crosspair for which uw is a common-neighbour edge. A selected crosspair has exactly one common neighbour, so its selecting B-edge must be uw. But each B-edge selects exactly one legal triple. Therefore a usable B-edge must satisfy |F(u,w)|<=1; if it supplements (u,i), then F(u,w) must equal {(u,i)}.

An unlisted B-source is adjacent to every C-label unless it has a residual-free selected state on C. In each of the five source-supported r=6 equality orbits, the preceding exact enumeration found/asserted zero nonempty residual-free states. Hence a fresh unlisted source can supplement u only when |L_u|=1. When |L_u|>1, each selected incidence must have an active source w for which F(u,w) is exactly that singleton.

This is a necessary condition. Ignoring common A-neighbours, zero-label constraints and deletion criticality can only add apparent survivors.

## Exhaustive result

check_r6_supplements.py regenerates all 31 exact source multisets rather than relying on the truncated examples in the JSON handoff. It then applies the forcing rule to every selected incidence.

- (3,1,1,1), orbit 1: 6 tested, 0 feasible.
- (3,1,1,1), orbits 2 and 3: 1 each tested, 0 feasible.
- (2,2,1,1), sole orbit: 3 tested, 0 feasible.
- (2,1,1,1,1), surviving orbit 4: 20 tested, 0 feasible.

Thus none of the 31 necessary source populations admits even a B-layer supplement assignment. Combined with the exact optimistic core and source reductions, product equality at r=6 is impossible.

Therefore:

    1 <= r <= 6 implies f <= r-1.

## Consequences and trust boundary

Let D=floor(n^2/4)-b(n-b)>=0 and epsilon=m-floor(n^2/4). Since t=D+epsilon and S>=r+2t:
- any non-bipartite equality case has r>=7 and S>=7+2D;
- any strict counterexample has r>=7 and S>=9+2D;
- S<=8 proves the edge bound;
- S<=6 proves equality exactly for balanced complete bipartite graphs, using zero-demand rigidity for r=0.

The unrestricted strip, equality at S=7,8 and all r>=7 cases remain open. The claim is internal/computer-assisted, with deterministic scripts and exact JSON evidence, not externally verified theorem status.

Exact evidence: R6_EQUALITY_CORE_SCREEN.json, R6_EQUALITY_SOURCE_SCREEN.json, R6_SUPPLEMENT_SCREEN.json and their scripts.
