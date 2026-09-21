# Complete parity block closes the four-centre density bound

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

In the exactly-four-centre branch, suppose every P0 vertex is adjacent to every P1 vertex. This includes P1 empty. Then

    m<=M(n)=floor((n-1)^2/4)+1

for every order.

Thus any counterexample in the sole realizable parity-plane orbit must contain a missing physical P0--P1 pair.

## Proof

Use t coordinate vertices, r>=1 P0 vertices, q>=0 P1 vertices and s>=4 star vertices. Put N=t+r+q, so a=N+s.

Completeness gives M=0 in the missing-pair ledger. The parity substitution theorem forces e(P0)+e(P1)=0. Every P0--star edge needs a missing P0--P1 pair as its third-target certificate, so none exists.

There is also no P1--star edge. For a star vertex x, criticality of its centre spoke requires a P0 singleton target p nonadjacent to x with no common A-neighbour. If x had a P1 neighbour y, completeness gives py, making y a common A-neighbour of x,p and destroying that sole centre-spoke certificate. (The odd opposite-centre reverse star is absent.)

Coordinates have A-neighbours only in P0, so their incident edge count is at most rt. The parity block has exactly rq edges. Every star must bridge its undominated antipode; with no parity--star or coordinate--star edges, the star forest has no isolated vertices and in particular has at most s-1 edges. Hence

    e(A) <= rt+rq+s-1 = r(t+q)+s-1.

Since r(t+q)<=floor(N^2/4),

    e(A) <= floor(N^2/4)+s-1.

Here t>=5 and r>=1, so N>=6; also s>=4. The elementary floor inequality

    floor((N+s)^2/4)-floor(N^2/4) >= s+2

holds throughout N>=6,s>=4 (the left-minus-right expression is increasing from the boundary cases). Therefore

    e(A) <= floor(a^2/4)-3.

Using m=20+4a+e(A) and M(n)=floor(a^2/4)+4a+17 gives m<=M(n).

## Consequence and scope

Both explicit parity-plane families lie in this closed branch: their P0--P1 blocks are complete. The only remaining exactly-four-centre density risk has M>0 and must exploit the missing-pair capacity quantified in `PARITY_STAR_MISSING_PAIR_LEDGER.md`. This is a graph-level closure at the stated rooted code scope, independent of the conditional rigid-Hall/source-tuple theorem.
