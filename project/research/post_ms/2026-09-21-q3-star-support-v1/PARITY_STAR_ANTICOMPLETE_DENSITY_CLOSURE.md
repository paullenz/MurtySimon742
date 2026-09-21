# Parity-star anticompleteness closes the four-centre density bound

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

In the exactly-four-centre parity-plane branch, suppose no parity-coded vertex is adjacent in A to a star-coded vertex. Then m<=M(n) at every order.

Consequently any counterexample in the complete four-centre branch must contain a physical parity--star edge. This strictly extends the complete-P0--P1 closure: missing parity pairs and same-parity substitutions are allowed.

## Proof

Use t coordinate vertices, r>=1 P0 vertices, q>=0 P1 vertices and s>=4 stars; let N=t+r+q and a=N+s.

Coordinates have A-neighbours only in P0, so all coordinate-incident A-edges number at most rt. The parity substitution theorem gives

    e(P0)+e(P1)+e(P0,P1)<=rq.

With parity--star and coordinate--star edges absent, each star's unique undominated antipode must be bridged by another star. Thus the necessary star forest has no isolated vertices and contributes at most s-1 edges. Therefore

    e(A)<=rt+rq+s-1=r(t+q)+s-1
         <=floor(N^2/4)+s-1.

As in the complete-parity proof, N>=6 and s>=4 imply

    floor((N+s)^2/4)-floor(N^2/4)>=s+2.

Hence e(A)<=floor(a^2/4)-3, which is equivalent to m<=M(n) for the Q3 skeleton.

## Reduced live obstruction

A parity--star edge cannot be certified in isolation. A P0--star edge forces a P1 neighbour of that star and a missing P0--P1 pair with the star as unique common neighbour. It also forces an additional same-centre star nonneighbour to certify the affected P0--B centre spoke. The graph-level existence of such coupled physical configurations is now the sole density obstruction inside the exactly-four-centre branch.

No bounded search is used in the theorem. Exact SAT tests have found no parity--star edge in the tested six-coordinate fixtures through r=q=8 and with up to four copies of one star centre, but this remains diagnostic evidence only.
