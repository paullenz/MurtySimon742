# C5 reassessment in the rooted partial-Boolean branch

Date: 2026-09-18

Status: strategic correction / structural lemma.

The main witness-slot note records the 2025 Lin--Wang theorem that sufficiently-large C5-free D2C graphs at the second-extremal threshold are complete bipartite. On closer inspection, that external result gives **no additional exclusion in the live triangle-containing partial-Boolean branch once `p>=2`**: rooted B-edge criticality itself already forces a 5-cycle.

## Lemma — every rooted B-edge forces a C5 when `p>=2`

Work around the live maximum-degree root `v`. Assume there are at least two tight antipode pairs (`p>=2`) and `Q=e(G[B])>0`.

Choose any edge `xy in E(G[B])`. By the rooted witness-slot theorem, orient it so that there is `z in A` with

> `N(x) cap N(z)={y}`.                                    `(C5-1)`

In particular `xz` is a nonedge and `yz` is an edge.

Every A-vertex selects one endpoint from each tight antipode pair, so

> `d_B(z)>=p>=2`.                                         `(C5-2)`

Choose

> `w in N_B(z)\{y}`.                                     `(C5-3)`

Because `xz` is a nonedge, `w!=x`. Hence the five vertices

> `v, x, y, z, w`

are distinct and the edges

> `vx, xy, yz, zw, wv`

form a `C5`.

Therefore

> `p>=2` and `Q>0`  implies  `C5 subseteq G`.             `(C5-4)`

No inducedness is claimed or needed; `C5-free` in the Lin--Wang theorem is the ordinary cycle-free condition.

## Consequence for strategy

The live branch is triangle-containing, and in the partial-Boolean regime with `p>=2` that means `Q>0` at the chosen rooted triangle interface. Thus the Lin--Wang C5-free theorem is a useful external consistency check but **not a new source of leverage** for the current attack: the branch already contains a C5 for the simplest possible local reason.

Accordingly, the next move should remain the source-local witness-slot / Hamming-budget synthesis, not an attempt to exploit the existence of C5 as an additional rare structure.

The published `X_3` graph is consistent with this lemma (`p=4`, `Q=12`) and indeed contains 5-cycles.