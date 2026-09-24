# Explicit C-overlap/private-source capacity diagnostic

24 September 2026. Status: internal graph-level necessary-condition work; not a complete realizability theorem.

## Correction to the first checkpoint

The first coarse set-count experiment in this file used the wrong cardinality convention, setting `|C_i|=h_i`. The proved source-union lemma defines

    C_i = N(i) intersect B,     |C_i| = Delta - h_i.

Therefore the first five-profile feasibility output was an invalid model and is retained only as a failed-route record. It must not be used as mathematical evidence.

A corrected model was then built from the graph-level assigned-witness interface.

## Corrected joint vertex-type model

Each physical vertex `u in B=N(v)` is assigned a joint type `(K,L,z)` where

- `K` is the active-label membership set: `i in K` iff `u in C_i`;
- `L` is the exact assigned-witness endpoint-incidence set `I_u`;
- `z=Delta-d(u)` is its degree deficit.

The following are necessary graph conditions:

1. `K cap L` is empty, because an assigned incidence `i--u` has `i` nonadjacent to `u`.
2. `sum_{u: i in K_u} 1 = |C_i| = Delta-h_i`.
3. `sum_{u: i in L_u} 1 = x_i`.
4. Distinct incidences at endpoint `u` have distinct B-sources, so

       d(u) >= 1 + |K| + |L|,

   accounting for the root edge, all known active-label neighbours, and the `|L|` distinct incoming assigned source edges.
5. A source vertex of type `(K,L,z)` has at most

       Delta - z - 1 - |K| - |L|

   additional physical B-edges available to serve as sources elsewhere. Source-edge capacity is shared globally across labels and target endpoint classes; a physical edge is never double-assigned.
6. A source used for label `i` at an endpoint with incidence set `J` must lie in `C_i` and in no `C_j` for `j in J\{i}`.
7. The preceding endpoint-deficit/source-union and demand constraints are retained.

This is still a necessary-condition model rather than a full graph realization: it aggregates vertices of identical joint type and does not yet encode every simple-graph/self-loop exclusion or every non-witness adjacency.

## Corrected test on the five audited n=18, Delta=10, rho=2 profiles

With `|C_i|=Delta-h_i`, four leading profiles remain feasible at the previous deficit objective, but one is eliminated:

- `d=x=(8,7)`, `h=(8,7)`, `|C|=(2,3)`: feasible, minimum deficit 17;
- `d=(8,7), x=(8,8)`, `h=(8,9)`, `|C|=(2,1)`: **INFEASIBLE**;
- `d=x=(8,6,1)`, `h=(8,6,1)`, `|C|=(2,4,9)`: feasible, minimum deficit 17;
- `d=x=(8,5,2)`, `h=(8,5,2)`, `|C|=(2,5,8)`: feasible, minimum deficit 18;
- `d=x=(5,5,5)`, `h=(5,5,5)`, `|C|=(5,5,5)`: feasible, minimum deficit 16.

The infeasible `(d,x)=((8,7),(8,8))` profile has a direct graph explanation.

## Singleton-source saturation obstruction

Let the two active labels be `0,1`. Here `|C_0|=2`, `|C_1|=1`, and `x_0=x_1=8` with `Delta=10`.

Because each assigned endpoint for label `i` is a non-neighbour of `i`, the `x_0=8` incidences exhaust `B\C_0`, which also has size 8. The two endpoint sets both have size 8 in a 10-set, so they share an endpoint. At a shared endpoint the unique source for label 1 must be private to `C_1`, hence the unique vertex `u in C_1` is not in `C_0`. Therefore `u` lies in `B\C_0`, so saturation forces `u` itself to be an assigned endpoint for label 0.

All eight label-1 incidences must use the same unique source `u`, giving eight distinct B-edges incident with `u`, all assigned to label 1. In addition `u` is adjacent to the root and to label 1. Since `u` is also an assigned endpoint for label 0, it has a further incoming assigned source edge. That edge cannot coincide with any of the eight label-1 edges because a physical edge is assigned only once. Hence

    d(u) >= 8 + 1 + 1 + 1 = 11 > Delta=10,

contradiction.

This closes that dense abstract profile at the graph interface without reconstructing the external e+disj+X proof.

## Reusable lemma form

If an active label `j` has `|C_j|=1` with unique source vertex `u`, then all `x_j` assigned incidences use distinct physical edges from `u`. Thus `d(u)>=x_j+2` from those edges plus the root and label `j`. If `u` is also an assigned right endpoint for another label, the endpoint's incoming assigned source edge is an additional physical edge, so `d(u)>=x_j+3`. Consequently, when `x_j>=Delta-2`, the unique `C_j` vertex cannot be an assigned endpoint of another label. Combined with endpoint-set saturation for a second label, this can force a contradiction exactly as above.

## Remaining live profiles

The corrected joint model still leaves `(8,7)`, `(8,6,1)`, `(8,5,2)` and `(5,5,5)` at their previous minimum deficits. The next bounded step is to exploit simple-graph/self-incidence restrictions and source-capacity sharing on those four actual joint geometries, rather than return to scalar enumeration.

Balanced complete-bipartite equality controls and the `X_3` negative control are unchanged. General theorem and equality characterization remain open.
