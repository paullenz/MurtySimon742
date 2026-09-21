# Joint missing-pair ledger for parity and star edges

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

Let R=P0, T=P1 and S be the physical star populations in the four-centre parity-plane branch. Write r=|R|, q=|T|,

    M = rq-e(R,T),
    I = e(R)+e(T).

Then I<=M and

    e(R,S)+e(T,S)+e(S) <= s+2(M-I),

where s=|S|. Consequently

    e(G[R union T union S]) <= rq+M+s-I <= rq+M+s.

This is a physical-incidence bound. It does not settle the full density problem because M may be large.

## Proof

The parity substitution theorem injects the I same-parity edges into I distinct missing R--T pairs. Call those pairs occupied.

An R--S edge rs has only one possible A-edge certificate. The R endpoint needs a complementary T target t such that rt is missing and

    N_A(r) intersect N_A(t)={s}.

The star endpoint has no usable B target because its antipode is odd and outside P0, and its disjoint opposite-star code is absent. Charge rs to rt. The charge is injective and cannot use an occupied pair: a fixed missing rt has at most one common neighbour, and an occupied pair's singleton common neighbour is a parity vertex rather than s. Hence e(R,S)<=M-I.

For a star vertex s of centre c, call any A-neighbour whose code contains bar(c) an antipode bridge. Every T-neighbour and every different-centre even star neighbour is such a bridge.

A T--S edge ts can be critical in only two ways:

1. t is s's unique antipode bridge; or
2. the T endpoint uses an R target r with rt missing and N_A(r) intersect N_A(t)={s}.

Edges of the second kind inject into unoccupied missing pairs, so there are at most M-I of them.

Every S--S edge must be certified from an endpoint that has exactly one antipode bridge. Combine these with the first-kind T--S edges. Each such edge has a star endpoint of total bridge degree one. Assign the edge to one such endpoint; a star vertex receives at most one assignment. Thus their combined count is at most s.

Adding the R--S charge, second-kind T--S charge and bridge-leaf charge proves the first inequality. Adding e(R,T)+I=rq-M+I yields the displayed induced-block bound.

Coordinates containing a star antipode can only increase total bridge degree and invalidate a leaf certificate; ignoring them is safe for this upper bound.

## Interpretation

Relative to the complete bipartite parity block of rq edges, each missing R--T pair has residual capacity at most two parity--star arms, for a net gain of at most one, while the leaf bridge layer contributes only s. The next density step must bound M using centre-spoke obligations, coordinate incidence or the rooted residual defect; treating M as free is too weak.
