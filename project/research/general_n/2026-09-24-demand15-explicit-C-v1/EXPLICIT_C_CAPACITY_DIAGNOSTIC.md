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
- `d=x=(8,6,1)`, `h=(8,6,1)`, `|C|=(2,4,9)`: feasible in this coarse model;
- `d=x=(8,5,2)`, `h=(8,5,2)`, `|C|=(2,5,8)`: feasible in this coarse model;
- `d=x=(5,5,5)`, `h=(5,5,5)`, `|C|=(5,5,5)`: feasible, minimum deficit 16.

The infeasible `(d,x)=((8,7),(8,8))` profile has a direct graph explanation.

## Singleton-source saturation obstruction

Let the two active labels be `0,1`. Here `|C_0|=2`, `|C_1|=1`, and `x_0=x_1=8` with `Delta=10`.

Because each assigned endpoint for label `i` is a non-neighbour of `i`, the `x_0=8` incidences exhaust `B\C_0`, which also has size 8. The two endpoint sets both have size 8 in a 10-set, so they share an endpoint. At a shared endpoint the unique source for label 1 must be private to `C_1`, hence the unique vertex `u in C_1` is not in `C_0`. Therefore `u` lies in `B\C_0`, so saturation forces `u` itself to be an assigned endpoint for label 0.

All eight label-1 incidences must use the same unique source `u`, giving eight distinct B-edges incident with `u`, all assigned to label 1. In addition `u` is adjacent to the root and to label 1. Since `u` is also an assigned endpoint for label 0, it has a further incoming assigned source edge. That edge cannot coincide with any of the eight label-1 edges because a physical edge is assigned only once. Hence

    d(u) >= 8 + 1 + 1 + 1 = 11 > Delta=10,

contradiction.

## Saturated membership-step lemma

There is a stronger purely combinatorial consequence when every active label is saturated, meaning

    x_i = |B\C_i|.

For `t in B`, write `K(t)={i:t in C_i}`. If `i` is not in `K(t)`, saturation makes `t` an assigned endpoint for label `i`; let `u_i t` be its assigned physical source edge. Then

    K(u_i) = K(t) union {i}.

Indeed `u_i in C_i`. If `j in K(t)` but `u_i` were not in `C_j`, saturation would make `u_i` an endpoint for `j`; the edge `t u_i`, with `t in C_j`, would then be the unique common-neighbour source edge for `j--u_i`, but it is already assigned to `i--t`, violating one-use of a physical edge. Conversely, if `j` is not in `K(t)` and `j!=i` but `u_i in C_j`, then `u_i t` is the unique common-neighbour source edge for `j--t` as well as for `i--t`, again impossible. Thus the source type is exactly one Boolean-lattice step upward.

Consequently the support of the membership counts `c_K=|{t:K(t)=K}|` is upward closed: whenever `c_K>0` and `i notin K`, also `c_{K union {i}}>0`.

### Two-point C obstruction for three saturated labels

For three saturated labels `0,1,2`, suppose `|C_0|=2` and both `C_1,C_2` are proper subsets of `B`. Upward closure is impossible.

The top type `012` must occur. Since the total mass in types containing label 0 is exactly two, either:

- `c_012=2` and no other 0-containing type occurs. Then the only possible type outside label 0 is `12`, so every vertex lies in both `C_1` and `C_2`, contrary to both being proper; or
- `c_012=1` and exactly one of `c_0,c_01,c_02` equals one. Type `0` is impossible because upward closure requires both `01` and `02`. If type `01` is the extra type, every possible occurring type contains label 1, so `C_1=B`; if type `02` is the extra type, similarly `C_2=B`.

Thus no such three-label saturated configuration exists.

This immediately excludes, at the graph interface, both audited n=18 saturated profiles

- `d=x=(8,6,1)`, where `|C|=(2,4,9)`;
- `d=x=(8,5,2)`, where `|C|=(2,5,8)`.

An independently built individual-B-vertex MILP imposing simple physical B-edges, exact `C_i` cardinalities, source-edge one-use, endpoint nonadjacency, unique common B-neighbour and degree consistency also returned both profiles infeasible and retained `(8,7)` feasible; the proof above is preferable because it isolates the exact graph mechanism without relying on that computation. The attempted code-file publication for this diagnostic was blocked by the connector, so no claim of preserved executable code is made.

## Rigid surviving two-label geometry

For the saturated `(8,7)` profile, `|C_0|=2`, `|C_1|=3`. The same upward-closure lemma forces the four membership-type counts uniquely:

    c_empty=6, c_0=1, c_1=2, c_01=1.

Hence the unique type-0 vertex must source all six empty-type endpoints for label 0, the two type-1 vertices collectively source all six empty-type endpoints for label 1, and the unique type-01 vertex supplies the required source edge to the type-0 vertex and to both type-1 vertices. This is a rigid local geometry, but it is not yet a contradiction.

## Remaining live geometry

At this stage the corrected graph-interface route has eliminated the `(8,8)` two-label profile and the two three-label profiles with a two-point `C_0`. The `(8,7)` local geometry survives and `(5,5,5)` is not excluded by upward closure alone. The repository already contains a separately audited staged exact D2C exclusion of the fixed `(5,5,5)` geometry; that result is not rederived here and should not be conflated with this independent local route.

Balanced complete-bipartite equality controls and the `X_3` negative control are unchanged. General theorem and equality characterization remain open.
