# Q3 star-bridge propagation and forced star-nonneighbour bill

Date: 2026-09-21

## Scope

Let `G` be diameter-2-critical, let `v` be a root with `B=N(v)` inducing `Q3`, and put `A=V(G)\(B∪{v})`. Assume every `A`-vertex has a four-element B-neighbourhood that is an antipodal transversal of `Q3`. Thus every code is either an odd affine halfcube or a star `S_c=N_Q[c]`.

This note uses only raw diameter two and the already-derived complete local A-B certificate table. It does not use the rigid-cut/Hall/source-tuple machinery.

## The bridge problem for a star

Fix a star vertex `x` with code

`H_x=S_c=N_Q[c]`.

Its unique B-vertex not dominated by `S_c` is `bar c`. Hence diameter two forces an A-neighbour `y` of x with

`bar c ∈ H_y`.

Call such a neighbour an **antipode bridge** for x. There are only three code-level possibilities.

### 1. Star bridge

If y has star code `S_d`, then `bar c∈S_d` gives

`d ∈ S_{bar c}`,

so `dist_Q(c,d)∈{2,3}`. Thus a star-star antipode bridge can only go to a centre at Hamming distance two or three.

### 2. Coordinate-halfcube bridge

Suppose

`H_y=C_i={u:u_i=1-c_i}`.

Then `H_y∩S_c={s}` where `s=c⊕e_i`. Consider the physical edge `ys`. Its standard coordinate certificate uses the outside cube vertex c, because s is the unique `C_i`-neighbour of c. But x is adjacent to y and c belongs to `S_c`, so after deleting `ys` the path

`y-x-c`

survives. Hence the standard certificate is destroyed.

By the complete local certificate table, `ys` must instead use one of exactly two star-supported mechanisms:

- a nonadjacent star `z` of code `S_c`; or
- an adjacent star `z` of code `S_{bar s}`.

In either case `z` is a **second physical star vertex**. More strongly,

`xz` is necessarily a nonedge.

Indeed, in the first mechanism `(y,z)` is the critical pair and x is adjacent to y; if xz were an edge, `y-x-z` would survive. In the second mechanism `(s,z)` is the critical pair and x is adjacent to s; if xz were an edge, `s-x-z` would survive.

Therefore every coordinate-halfcube antipode bridge for x forces at least one star nonneighbour of x.

### 3. Opposite-parity bridge

Suppose `H_y=P_bar` is the parity halfcube opposite the parity side through c. Then

`H_y∩S_c={s_1,s_2,s_3}`

where `s_i=c⊕e_i` are the three leaves of `S_c`.

For every i, the direct parity certificate for the physical edge `ys_i` is destroyed by the surviving path

`y-x-s_i`.

The local table leaves exactly two replacements:

- a nonadjacent star of type `S_{s_i}`; or
- an adjacent star of type `S_{bar s_i}`.

For distinct i these six code types are pairwise distinct: relative to c the `s_i` have Hamming weight one and the `bar s_i` have Hamming weight two. Hence the three physical edges require **three distinct star vertices** `z_1,z_2,z_3`, one for each i.

Moreover every `z_i` is nonadjacent to x. In the nonadjacent-star mechanism, otherwise x would be a common A-neighbour of y and `z_i`; in the adjacent-star mechanism, otherwise `s_i-x-z_i` would survive the deletion of `ys_i`.

Thus every opposite-parity antipode bridge forces at least three distinct star nonneighbours of x.

## The propagation theorem

For every physical star vertex x of centre c, at least one of the following holds:

1. x has a star antipode bridge whose centre is at Hamming distance two or three from c;
2. x has a coordinate-halfcube antipode bridge and at least one other star vertex is nonadjacent to x;
3. x has an opposite-parity antipode bridge and at least three other star vertices, in three distinct star code types, are nonadjacent to x.

In particular, the no-singleton-star theorem is recovered immediately, but the stronger conclusion is a **bridge/deficit dichotomy**: avoiding a star-star bridge necessarily creates explicit missing edges from x into the star population.

## Why this matters for density

Inside the full antipodal-transversal branch,

`m(G)=20+4|A|+e(A)`.

Hence all remaining density freedom is in `e(A)`. The theorem above converts the previously qualitative statement “stars propagate” into a physical missing-edge bill:

- coordinate-halfcube bridging costs at least one star nonedge at x;
- parity bridging costs at least three star nonedges at x;
- the only way to avoid that immediate bill is a star-star bridge in the finite centre relation `dist_Q(c,d)>=2`.

The next object to analyse is therefore the star-star bridge subgraph itself. A useful complementary fact is that, from the viewpoint of a star `S_c`, the only B-target that can certify an incident A-edge is the unique undominated antipode `bar c`; this can be the unique bridge certificate for at most one incident edge. Dense star-star adjacency must therefore use endpoint-disjoint/direct or third-A certificates on almost all remaining edges. That is the next charging target.
