# Exact star-side certificate classification for incident A-edges in the Q3 transversal branch

Date: 2026-09-21

## Scope

Let `G` be diameter-2-critical, `v` a root with `B=N(v)=Q3`, and `A=V(G)\(B∪{v})`. Assume every `A`-vertex has an antipodal-transversal B-code. Fix a star vertex x with

`H_x=S_c=N_Q[c]`.

This note classifies every possible critical-pair mechanism **on the x side** of an incident A-edge `xy`. It uses only raw edge-criticality and the 16-code transversal universe.

## General form

Delete an A-edge `xy`. Any newly long pair must contain x or y, because every path using the deleted edge has one of those endpoints. Restrict attention to newly long pairs containing x. There are exactly three forms.

### X1. Direct endpoint certificate `(x,y)`

After deleting xy, x and y can be farther than two only if they have no surviving common neighbour. In particular their B-codes must be disjoint:

`H_y ∩ S_c = ∅`.

Among the 16 antipodal transversals of Q3, the unique transversal disjoint from `S_c` is

`S_{bar c}`.

Hence a direct endpoint certificate on the x side is possible only when y is an **opposite-centre star**. It additionally requires x and y to have no common A-neighbour.

### X2. Antipode-B certificate `(x,t)`

Suppose `t∈B` and the deleted edge destroys the two-path `x-y-t`, so `t∈H_y`. For `(x,t)` to become long, t must have no surviving B-mediated two-path from x. Thus

`t∉S_c` and `N_Q(t)∩S_c=∅`.

The star `S_c` dominates every cube vertex except the antipode `bar c`. Therefore necessarily

`t=bar c`.

So an incident A-edge can be certified on the x side by a B-target only when y is an antipode bridge:

`bar c∈H_y`.

Moreover y must be the **unique** A-neighbour of x whose code contains `bar c`; otherwise another two-path from x to `bar c` survives. Consequently:

> A fixed physical star vertex x can use its antipode-B mechanism X2 for at most one incident A-edge.

### X3. Third-A certificate `(x,z)`

Suppose z is an A-neighbour of y and deletion of xy is intended to make `(x,z)` long. Then xz must be a nonedge. Also x and z can have no common B-neighbour, so

`H_z∩S_c=∅`.

Again the unique transversal disjoint from `S_c` is `S_{bar c}`. Therefore z must be an **opposite-centre star**. In addition:

- `yz` is an edge;
- `xz` is a nonedge;
- x and z have no common A-neighbour other than y before deletion / none after deletion.

Thus every X3 certificate comes with an explicit missing edge from x to an opposite-centre star.

## Star-star edge corollary

Let both endpoints be stars, with centres c and d. Every critical star-star edge xy must be certified by one of the X1-X3 mechanisms from x, or by the symmetric mechanisms from y.

This gives a sharp centre-level trichotomy.

1. **Opposite centres (`d=bar c`).** Direct endpoint certification X1 is available, provided there is no common A-neighbour. This is the only star-star centre pair for which direct certification is possible.
2. **Distance two or three centres.** Antipode certification X2 is available because `bar c∈S_d`; but each physical endpoint has capacity one for this mechanism.
3. **Distance zero or one centres.** Neither X1 nor X2 is available on the x side. Any x-side certificate must therefore be X3 and must invoke a star of centre `bar c` that is adjacent to y and nonadjacent to x. Symmetrically, a y-side certificate invokes centre `bar d`.

In particular, same-centre and distance-one star-star edges are never locally cheap: unless certified entirely from the other endpoint by its own unique antipode bridge, they force an explicit opposite-centre witness/nonedge configuration.

## Density interpretation

The star-star bridge subgraph has only two genuinely cheap resources:

- direct edges between opposite centre classes; and
- at most one antipode-bridge edge per physical star vertex.

All remaining critical star-star edges must be supported by third-star witness geometry that simultaneously creates nonedges to opposite-centre stars. This is the first exact charging framework for turning star propagation into an A-edge deficit.

The natural next step is to orient each star-star edge by one chosen endpoint certificate and count: direct opposite-centre edges separately, at most one X2-oriented edge per star, and all other oriented edges against X3 witness/nonedge incidences. A successful bounded-multiplicity charge would force the asymptotic star subsystem toward a union of opposite-centre bipartite blocks.
