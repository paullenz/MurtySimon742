# Saturated (8,7) deficit closure

24 September 2026. Status: internal graph-level proof for this fixed audited n=18, Delta=10 saturated profile. It does not by itself close the n=18 strip or the general Murty–Simon theorem.

This note continues `EXPLICIT_C_CAPACITY_DIAGNOSTIC.md` and `ROOT_EDGE_SINGLETON_OBSTRUCTION.md`.

Let the active labels be 0,1 with

    C_0={p,s},     C_1={q,r,s},

and let E be the six empty-type B-vertices. Partition E=Q union R according to whether the label-1 assigned source is q or r. The forced B-skeleton has p adjacent to every E and to s; s adjacent to p,q,r and to no E; p nonadjacent q,r; every e in Q adjacent q and not r; every e in R adjacent r and not q. The active labels 0 and 1 are nonadjacent.

The preceding root-edge argument forces distinct inactive A-vertices x_p,x_s with `C_{x_p}={p}` and `C_{x_s}={s}`. It also forces p to full degree Delta=10.

## Baseline deficit

Write `delta_z=Delta-d(z)`. Since A has seven vertices, an A-vertex with one B-neighbour has at most six A-neighbours.

The pair (label 1,p) has unique common neighbour s. Since x_p is adjacent p, x_p cannot be adjacent label 1. Hence

    delta_{x_p} >= 10-(1+5)=4.

No analogous active-label exclusion is needed for x_s, giving

    delta_{x_s} >= 10-(1+6)=3.

The active labels are nonadjacent. Label 0 has only two B-neighbours, so

    delta_0 >= 10-(2+5)=3.

Label 1 has three B-neighbours, is nonadjacent label 0, and is also nonadjacent x_p. Thus

    delta_1 >= 10-(3+4)=3.

Therefore these four vertices alone contribute at least

    4+3+3+3 = 13

to the total degree deficit.

## Any additional singleton root witness already closes the edge bound

If root edge vq or vr needs an A-side singleton witness x_b with `C_{x_b}={b}`, then b is an assigned endpoint for label 0. The unique-common-neighbour condition forces x_b nonadjacent label 0. Hence `delta_{x_b}>=4`, while label 0 loses one more possible A-neighbour and its deficit rises by at least one. Added to the baseline, total deficit is at least 18.

If a root edge ve with e in E needs a singleton witness x_e, then e is an assigned endpoint for both active labels. Thus x_e is nonadjacent to both labels, so `delta_{x_e}>=5`; the two active-label deficit floors each rise by one. The total deficit is then at least 20.

Consequently, any realization with total deficit below 18 must have no singleton root witness beyond x_p,x_s.

## What no additional singleton forces inside B

For e in Q, every B-nonneighbour other than r is blocked as a root-edge witness by a known common B-neighbour: s shares p with e, and every nonadjacent vertex of E shares p with e. Therefore r must be the B-side witness for ve. This forces `qr` to be a nonedge and forbids every cross-edge from e to R, since such a cross-neighbour would be a second common neighbour of e and r. Symmetrically every e in R forces no Q--R cross-edge.

For root edge vq, after p and r are blocked by the common neighbour s, a B-side witness can only lie in R; hence R is nonempty. Symmetrically Q is nonempty.

Thus in the only branch not already closed by a singleton-deficit charge:

    qr is absent,
    Q and R are both nonempty,
    G[E] has no Q--R edges.

## Residual E-deficit closes the last branch

Let k=|Q|, so 1<=k<=5 and |R|=6-k. A vertex e in Q can be adjacent, outside Q, only to the root, p, q and the three remaining inactive A-vertices: both active labels miss e, x_p has B-neighbourhood {p}, x_s has B-neighbourhood {s}, s misses E, r misses Q, and there are no Q--R edges. Hence

    d(e) <= 1 + 2 + (k-1) + 3 = k+5,
    delta_e >= max(0,5-k).

Similarly each e in R satisfies

    delta_e >= max(0,k-1).

Therefore

    sum_{e in E} delta_e
      >= k(5-k) + (6-k)(k-1)
      >= 4

for every 1<=k<=5 (the minimum 4 occurs at k=1 or 5).

Combining with the baseline gives total deficit at least 17. But

    D = sum_z (Delta-d(z)) = n Delta - 2e(G) = 180-2e(G)

is even. Hence `D>=18`, and therefore

    e(G) <= (180-18)/2 = 81 = floor(18^2/4).

So the saturated audited `(8,7)` profile cannot violate the Murty–Simon edge bound.

This is a fixed-profile closure only. It does not assert that every n=18, Delta=10 profile has been exhausted, and it does not strengthen the separately controlled equality theorem.
