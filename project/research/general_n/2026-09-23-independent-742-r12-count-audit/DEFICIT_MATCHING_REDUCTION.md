# Degree-deficit matching reduction for an exact-H obstruction

Let Delta be the maximum degree, rho=2Delta-n>0, and delta_x=Delta-d(x). Let L be an inclusion-minimal exact-H maximizer and form the bipartite private-witness graph W between L and B: an edge i--t records a private certificate edge u--t in P_i, so N(i) intersect N(t)={u}.

## Local deficit inequality

Because i and t are nonadjacent and have exactly one common neighbor,

d(i)+d(t)-1 = |N(i) union N(t)| <= n-2.

Therefore
delta_i+delta_t = 2Delta-d(i)-d(t) >= rho+1
for every edge of W.

## Strict-counterexample deficit budget

Write D=sum_x delta_x=nDelta-2m. If m>floor(n^2/4), then

- for even n: D <= n rho/2 - 2;
- for odd n: D <= (n rho-3)/2.

In particular D<n rho/2.

Every matching of size r in W uses disjoint vertices, so summing the local inequality gives r(rho+1)<=D. Hence

nu(W) <= floor(D/(rho+1)).

By Konig's theorem, W has a vertex cover X union Y, with X subset L and Y subset B, of the same size. Every label i outside X has all its private missed endpoints in Y. Since |P_i|>=floor(h_i/2)+1, this forces

h_i <= 2|Y|-1  for every i in L minus X.

This is the next structural branch: either the cover consumes many active labels, or all uncovered labels have uniformly bounded deficit h_i.

## Negative control

The observed top-H graph n=40, seed 611, root 15 has Delta=21, rho=2 and H=10, but only m=171 edges versus floor(n^2/4)=400. Its total maximum-degree deficit is D=498, whereas a strict counterexample at these n,Delta would require D<=38. Thus the deficit budget correctly distinguishes the sparse high-H negative control, but the concentrated-cover branch remains unresolved.

No general strip theorem is claimed.
