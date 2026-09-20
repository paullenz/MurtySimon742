# Exact second-strict unloaded buffer: initial physical reduction

Date: 2026-09-20

Status: internal follow-on to `FIRST_STRICT_COMPLETE_CLOSURE.md`. No claim below is a global eventual theorem; the 20 September audit boundary and zero-positive-rigid-cut caveat remain binding.

## 1. Setup

The first-strict complete closure raises the unloaded buffer floor to

`epsilon_b>=p-g+2`.

At exact equality write

`h_X=e_bar({b},X)`, `h_o=e_bar({b},U_o)`.

The exact defect identity gives

`h_X+h_o=2`.

The `(0,2)` subtype is already excluded in the companion closure note, so only

- **two-X-hole:** `(h_X,h_o)=(2,0)`;
- **mixed-hole:** `(h_X,h_o)=(1,1)`

remain.

## 2. Mixed-hole subtype: at most one reverse buffer edge

Assume `(h_X,h_o)=(1,1)`. Let `a_0` be the unique X non-neighbour of `b` and `z_0` the unique `U_o` non-neighbour of `b`.

For an actual buffer edge `bx`, all reverse-witness locations except `U_o` are excluded exactly as in the first-strict theorem: root/matched vertices, `U_-`, Y and X each carry a fixed extra common neighbour with `b`. Within `U_o`, only `z_0` is nonadjacent to `b`.

Thus every reverse certificate for a buffer--X edge must use the same physical pair `(b,z_0)`. Its common-neighbour set is graph-fixed, so it can be a singleton `{x}` for at most one X-head.

Therefore:

> **at most one edge of `b--(X\{a_0})` is reverse-certified.** `(MIX-REV1)`

Since `b` has `x-1` such X-edges, at least

> `x-2`

of them require Orientation-A certificates.

Matched Orientation A remains unavailable by the preserved matched-channel collapse, so those `x-2` edges have outside-U certificates using vertices of `U_o\{z_0}` that are adjacent to `b`.

## 3. Every outside-certified mixed-hole head is Type R

Fix one of those outside-certified heads `x`, with witness `z`:

`bz in E`, `xz notin E`, `N(x) cap N(z)={b}`, `c(z)=bar c(x)`.

For each coordinate `i` where `c(x)_i=d_i`, the rooted edge `zq_i` has the same self-pricing property used in the first-strict funnel: any singleton A-witness must be an X-vertex nonadjacent to `b`.

There is still exactly one such vertex, `a_0`. Hence the local F/R orientation classification applies unchanged to this outside-certified edge.

Its Type-F alternative is impossible by the upstream Type-F elimination: if `I_x={i} subseteq S_0`, then `z` and `a_0` share an additional tight matched neighbour at every coordinate of nonempty `I_0`, contradicting the claimed forward singleton.

Therefore every outside-certified mixed-hole head is Type R:

> `empty != I_x subseteq I_0`,
> `xa_0 notin E`,
> `za_0 in E`.                                          `(MIX-R)`

Consequently

> **`d_X(a_0)<=1`.**                                    `(MIX-A0-DEG1)`

The only possible X-neighbour of `a_0` is the unique head, if any, whose buffer edge uses the exceptional reverse witness `z_0`.

This converts the mixed exact-second-strict layer into a one-exception all-R geometry rather than an arbitrary one-hole configuration.

## 4. Why the first-strict all-R closure cannot simply be copied

The upstream first-strict proof used a matched edge `xq_j` with `j in S_0` and showed that no outside class could rescue its criticality because every Type-R block lies in `I_0`.

In the mixed layer, `z_0` is a new physical exception: it is nonadjacent to `b`, so the fixed `b` extra-common-neighbour obstruction that excluded an outside witness in the `q_j -> x` orientation no longer applies. Depending on `c(z_0)` and its X-neighbourhood, it may certify some of those matched edges.

Therefore the mathematically correct next target is to bound the **matched-edge certification capacity of the single exceptional vertex `z_0`**, not to cite the first-strict closure verbatim.

A fixed ordered pair `(q_j,z_0)` can certify at most one X-head for each coordinate `j`; ordered `(x,z_0)` pairs are likewise graph-fixed. Any closure must account for these physical obligations rather than treating `z_0` as an unlimited exception.

## 5. Two-X-hole subtype: two-foot funnel

Assume `(h_X,h_o)=(2,0)` and name the two buffer--X holes `a_0,a_1`. Then `b` is complete to `U_o`.

The first-strict reverse-witness exclusion applies unchanged, so every actual buffer--X edge uses an outside-U Orientation-A certificate. There are exactly `x-2` such edges.

Fix `bx` with outside witness `z`. For every coordinate `i` with `c(x)_i=d_i`, the rooted edge `zq_i` again has the self-pricing property: every singleton A-witness must be an X-vertex nonadjacent to `b`.

Now there are exactly two choices. Hence for each such coordinate, raw criticality assigns at least one of the two physical feet `a_0,a_1` through one of the two singleton orientations

- `N(z) cap N(a_j)={q_i}` (forward), or
- `N(q_i) cap N(a_j)={z}` (reverse).

Thus every outside-certified head carries a **two-foot coordinate cover** of its agreement set `I_x`.

For a fixed pair `(z,a_j)`, the forward singleton can occur for at most one matched head `q_i`, because the common-neighbour set of that physical pair is fixed. Reverse coordinates for the same foot impose the same code-support compatibility as in the old Type-R argument.

So the `(2,0)` subtype is not a free two-hole generalization: each head's tight agreement coordinates must be routed through only two graph-fixed physical pairs, with at most one forward coordinate per foot.

## 6. Next targets

The exact second-strict frontier is now sharply separated:

1. **mixed `(1,1)`:** one exceptional reverse vertex `z_0`, at least `x-2` Type-R outside-certified heads, and `d_X(a_0)<=1`; attack the total number of `S_0` matched-edge obligations that `z_0` can rescue;
2. **two-X-hole `(2,0)`:** every surviving buffer edge is outside-certified and each head has a two-foot coordinate cover; derive the exact two-foot support normal form and feed it into the rooted residual ledger.

The `(0,2)` subtype is empty. Loaded-buffer, `z=2` and four-exception branches remain subordinate until this exact second-strict layer is resolved.