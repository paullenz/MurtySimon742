# Graph-level exclusion of stable index 50,740

24 September 2026. Status: internal graph-interface proof for the fixed
`n=18, Delta=10` profile

    d=x=h=(8,8),   D<=16.

It does not close the full row or the general theorem.

Let `v` be the maximum-degree root, `B=N(v)` with `|B|=10`, and let the two
active labels be `0,1` in `A`.  Put `C_i=N_B(i)`.  Since `h_i=8`, each
`|C_i|=2`; since `x_i=8`, saturation makes every vertex of `B\C_i` an assigned
endpoint for label `i`.

## Deficit rigidity

The strict-counterexample allowance is `D<=16`.  The two centre deficits
satisfy `delta_i<=h_i=8`, and each exact star inequality says

    8 delta_i + sum_{t in B\C_i} delta_t >= 8*3+35=59.

If some `delta_i<=7`, the noncentre deficit is at least three.  Even allowing
the other centre its maximum deficit eight gives `D>=7+8+3=18`.  Thus

    delta_0=delta_1=8

and every other vertex has deficit zero.  Consequently labels 0 and 1 have
degree two, exactly their two neighbours in `C_0,C_1`, and all other sixteen
vertices have degree `Delta=10`.

## The two C-sets must meet but cannot coincide

They cannot coincide.  If `C_0=C_1=C`, choose an assigned endpoint outside
`C`.  Its two assigned incidences require distinct physical source edges, one
for each label.  Both sources lie in `C`, so the label--endpoint pair has at
least two common neighbours, contradicting uniqueness.  Equivalently, this is
the private-source antichain lemma.

They cannot be disjoint either.  Pick `t in C_1` (hence `t notin C_0`) and let
`ut` be its assigned source edge for label 0, with `u in C_0`.  If `u notin
C_1`, saturation makes `u` an endpoint for label 1.  Then the same physical
edge `ut`, with `t in C_1`, is also the unique source edge for the label-1
incidence at `u`, violating one-use.  Hence `u in C_0 intersect C_1`, a
contradiction to disjointness.

Therefore, after relabelling,

    C_0={c,p},   C_1={c,q}.

Write `S=B\{c,p,q}`, so `|S|=7`.

## Forced B-skeleton and degree completion

For every `s in S`, the private source for label 0 must be `p`, and that for
label 1 must be `q`.  Therefore `p` and `q` are each adjacent to all seven
vertices of `S`.  The endpoint `q` for label 0 and endpoint `p` for label 1
force the edges `cq` and `cp`, respectively.  Uniqueness forbids `pq` and all
edges from `c` to `S`.

Thus `p` already has the ten neighbours

    v, 0, c, and all seven vertices of S,

and similarly `q` has `v,1,c` and all of `S`.  Both are full and have no
neighbour in the five inactive vertices `X=A\{0,1}`.

Vertex `c` is adjacent to `v,0,1,p,q` and misses every vertex of `S`.  Since
`d(c)=10`, it must be adjacent to all five vertices of `X`.

Now fix `z in X`.  It has degree ten, but is nonadjacent to `v`, to the two
degree-two active labels, and to the full vertices `p,q`.  Besides `c`, its
only possible neighbours are the other four vertices of `X` and the seven
vertices of `S`.  Therefore it has at least five neighbours in `S`.

## Root edge `vc` is not critical

The edge `vc` lies in triangles through `p` and `q`, so deleting it does not
separate its endpoints beyond distance two.  A diameter-two graph can lose
diameter two on deleting `vc` only if either

1. some `s in B\N_B(c)=S` has `v` as the unique common neighbour with `c`; or
2. some `z in A cap N(c)` has `c` as the unique common neighbour with `v`.

The first is impossible because every `s in S` shares both `p` and `q` with
`c`.  For the second, labels 0 and 1 share `p` and `q`, respectively, with
`v`; every inactive `z in X` has at least five neighbours in `S` in addition
to `c`.  Thus `c` is never unique.  Deleting `vc` leaves all vertex pairs at
distance at most two, contradicting diameter-two criticality.

Hence stable-index profile 50,740 is not graph-realizable.  Combined with the
exact v4 screen, the internal prefix may pass this isolated abstract survivor;
the next unchecked scalar index remains 52,451.
