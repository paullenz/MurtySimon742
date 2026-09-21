# Exact substitution bound inside the two parity populations

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

In a parity-plane four-star graph, let R be the physical P0 population and T the physical P1 population, with |R|=r and |T|=q. Then

    e(R)+e(T)+e(R,T) <= rq.

Thus the complete bipartite parity block used by the explicit families is extremal among all edges internal to R union T, even when same-parity edges are allowed.

## Proof

A same-P0 edge xy cannot be direct-critical because its endpoint codes intersect. A parity halfcube has no undominated B target. Therefore criticality requires a third A vertex t of complementary code P1: for one orientation, say source x and head y,

    xt is absent and N_A(x) intersect N_A(t)={y}.

Charge xy to the missing cross-parity pair xt. The identical statement holds with the parity roles reversed for every same-P1 edge.

This charge is injective. A fixed missing pair xt has at most one common A-neighbour, because it can receive a charge only when that common-neighbour set is the displayed singleton. That unique common neighbour determines both the charged same-parity edge and its orientation. Moreover the same missing R--T pair cannot receive one charge from each parity side: that would require two distinct common neighbours, one in R and one in T, contradicting singleton uniqueness.

Hence

    e(R)+e(T) <= rq-e(R,T).

Rearranging proves the theorem.

Star or coordinate common neighbours do not create an exception: their presence would enlarge the common-neighbour set and destroy the certificate rather than create extra charge capacity.

## Consequence

Any density proof in the exactly-four-centre branch may replace the full induced parity edge term by rq<=floor((r+q)^2/4). The remaining uncontrolled interface is parity--star incidence and its competition with antipode-bridge uniqueness; coordinate--P0 edges already obey the complementary-code substitution bound and the star subgraph is a star forest.
