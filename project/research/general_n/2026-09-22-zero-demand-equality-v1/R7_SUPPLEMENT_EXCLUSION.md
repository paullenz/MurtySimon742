# Residual mass seven: supplement obstruction and equality closure

22 September 2026. Internal computer-assisted candidate proof. This extends the exact r=6 supplement method while explicitly allowing residual-free N-source types.

## Necessary forcing rule

For a proposed B-edge uw, collect every selected crosspair at u for which w is adjacent to the selected label, and symmetrically every selected crosspair at w for which u is adjacent. Each such crosspair would have uw as a common-neighbour edge. Because a selected crosspair has a unique common neighbour, uw must be its selecting edge. Since one B-edge selects only one triple, a usable edge can force at most one selected incidence.

Unlike the r=6 surviving kernels, two r=7 core orbits permit a nontrivial residual-free selected source on N-labels. The checker therefore includes every valid residual-free N-state as an unlimited potential fresh supplement type, not just a universal all-adjacent source. It optimistically ignores the new source's own remaining supplement obligations. This relaxation can only add survivors.

## Exact result

check_r7_supplements.py regenerates all 211 exact source populations across the 12 surviving core orbits. For every selected incidence it tests all active sources and every valid residual-free N-state for a B-edge forcing exactly that singleton.

All 211 populations fail:
- (4,1,1,1): 8 tested, 0 feasible;
- (2,2,1,1,1): 154 tested, 0 feasible;
- (2,1,1,1,1,1): 49 tested, 0 feasible.

Thus product equality at r=7 is impossible. Combined with the strict and lower-residual reductions:

    1 <= r <= 7 implies f <= r-1.

## Consequences

With D=floor(n^2/4)-b(n-b)>=0, epsilon=m-floor(n^2/4), t=D+epsilon and S>=r+2t:
- every non-bipartite equality case has r>=8 and S>=8+2D;
- every strict counterexample has r>=8 and S>=10+2D;
- S<=9 proves the edge bound;
- S<=7 proves equality exactly for balanced complete bipartite graphs, using zero-demand rigidity at r=0.

The full positive-demand strip and all r>=8 cases remain open. These are internal deterministic computer-assisted results, not external theorem status. Exact evidence: the r7 core, source and supplement JSON files and scripts.
