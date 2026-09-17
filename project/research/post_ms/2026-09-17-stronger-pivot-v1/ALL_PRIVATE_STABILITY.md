# All-private stability in a maximum-degree rooted D2C graph

17 September 2026. **Internal candidate hand theorem; external mathematical and novelty review open.**

This continues the root-edge antipode/private-foot dichotomy. It treats the branch in which **every** triangle-active `B`-vertex has a private `A`-foot and yields a substantially sharper constraint than the earlier quadratic edge bound.

## 1. Setup

Let `G` be diameter-2-critical, rooted at a maximum-degree vertex `v`.

`B=N(v)`, `A=V(G)\N[v]`, `b=|B|`, `a=|A|`,

`F=G[A]`, `f=e(F)`, `Q=e(G[B])`.

Use the canonical residual identity

`sum_{u in B} h_u = Q+r`,

where `h_u` is the number of missing `A`-neighbours at `u`, and

`delta=r-f=b(n-b)-m`.

Let `T` be the set of triangle-active vertices of `B`, i.e. the endpoints of edges of `G[B]`, and put `t=|T|`. Assume `Q>0`, hence `t>=2`.

Assume the **all-private branch**: for every `u in T` there is a vertex `x_u in A` with

`N(x_u) intersect B={u}`.

These private feet are automatically distinct.

## 2. Private feet force cross-deficit mass

Each private foot `x_u` is nonadjacent to exactly `b-1` vertices of `B`. Since the feet are distinct, their missing cross incidences are disjoint as incidences. Therefore

`Q+r = number of missing A-B incidences >= t(b-1)`.       (2.1)

This is stronger than merely charging private feet to nonisolated vertices of `F`.

## 3. Maximum degree bounds internal A-mass

Every `x in A` has degree at most `b`, because the root has maximum degree. Summing degrees over `A` gives

`e(A,B)+2f <= ab`.

But the number of missing A-B incidences is `Q+r`, so

`e(A,B)=ab-(Q+r)`.

Hence

`2f <= Q+r`.

Using `r=f+delta`,

`f <= Q+delta`.                                          (3.1)

Consequently

`Q+r = Q+f+delta <= 2Q+2delta`.                          (3.2)

## 4. All-private gap inequality

All `Q` edges of `G[B]` have both endpoints in `T`, so

`Q <= binom(t,2)`.

Combine this with (2.1)-(3.2):

`t(b-1) <= Q+r <= 2Q+2delta <= t(t-1)+2delta`.

After cancellation:

> **ALL-PRIVATE GAP THEOREM**
>
> `t(b-t) <= 2 delta`.                                  (APG)

Thus an all-private branch cannot have a medium-sized triangle-active core unless the canonical defect pays quadratically for the inactive part.

Immediate consequence: if

`2delta < b-1`,

then `t=b`; indeed every integer `1<=t<=b-1` has `t(b-t)>=b-1`.

Since here `t>=2`, slightly sharper case-specific forms can be used if desired, but the symmetric bound above is cleaner.

## 5. Exact-defect rigidity

Assume now `delta=0`. Since `Q>0`, (APG) forces

`t=b`.

The inequality chain becomes

`b(b-1) <= Q+r = Q+f <= 2Q <= b(b-1)`.

Therefore equality holds throughout:

`Q=binom(b,2)`,

`f=Q`,

`r=f`,

and the private feet account for **all** missing A-B incidences.

So:

1. `G[B]=K_b`;
2. there are `b` distinct private feet `x_u`;
3. every other `A`-vertex, if any, is adjacent to every vertex of `B`;
4. equality in the maximum-degree sum gives `deg(x)=b` for every `x in A`;
5. hence each private foot has `F`-degree `b-1`, while every nonprivate A-vertex has `F`-degree zero;
6. consequently the private feet induce `K_b` in `F` and have no `F`-edges to nonprivate A-vertices.

Thus the exact branch has a rigid double-clique-plus-matching form around the root: `B=K_b`, the private-foot set `X=K_b`, and `x_u` is adjacent to exactly its matched `u` in `B`.

## 6. Exact-defect branch is not D2C

Take any edge `uw` of `G[B]` (there is one because `Q>0`). Remove `uw`.

The endpoints `u,w` remain at distance two through the root `v`.

The only vertices adjacent to `w` but not to `u` in the rigid structure are its private foot `x_w`; after deleting `uw`,

`u-x_u-x_w`

is a two-edge path because the private feet form a clique. Symmetrically, `w` remains within distance two of `x_u`. Every other vertex was either adjacent to both `u,w` or is unaffected by the deletion.

Hence deleting `uw` leaves diameter at most two, contradicting diameter-2-criticality.

Therefore:

> **EXACT ALL-PRIVATE EXCLUSION.** A non-bipartite maximum-degree-root branch with `Q>0`, all triangle-active vertices private-supported, and `delta=0` does not exist in a D2C graph.

This is a genuine strengthening of the earlier PRIVATE bound: the all-private obstruction cannot occupy the exact defect boundary at all.

## 7. Near-exact stability when t=b

If `t=b`, write

`Q=binom(b,2)-s`, `s>=0`.

From the same chain,

`s<=delta`.

Thus `G[B]` is missing at most `delta` edges from a clique.

Moreover

`binom(b,2)+s-delta <= f <= binom(b,2)-s+delta`.

The total maximum-degree slack on `A` is

`sum_{x in A} (b-deg(x)) = Q+delta-f <= 2(delta-s) <=2delta`.

The missing A-B incidences not already forced by the `b` private feet are likewise at most `2(delta-s)`.

So once APG forces `t=b`, small `delta` gives a quantitative near-rigidity statement: both `B` and the private-foot side are close to the exact double-clique model which D2C criticality forbids at `delta=0`.

This is the natural next point for a stability contradiction: price each surviving `B`-edge criticality witness against the at-most-`O(delta)` defects from the rigid model.

## 8. Regression

`check_all_private_stability_atlas.py` scans all NetworkX graph-atlas isomorphism classes through order 7, retains D2C graphs, and tests every maximum-degree root lying in a triangle.

Frozen result:

- D2C isomorphism classes through order 7: 21;
- maximum-degree triangle roots: 9;
- all-private roots: 3;
- APG violations: 0;
- all-private roots with `delta=0`: 0.

This is regression evidence only.

## 9. Trust boundary

The algebraic proof of APG and the exact-defect rigidity argument are hand arguments using the canonical residual identity and maximum-degree root setup. They remain internal until independently checked. No eventual second-extremal theorem is claimed.
