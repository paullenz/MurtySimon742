# The four-centre fan tax for parity-star incidence

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

Let z be the number of physical P1 vertices having at least one star neighbour. Retain M=rq-e(P0,P1) and I=e(P0)+e(P1).

## Theorem

Every active P1 vertex has neighbours in all four star-centre classes. Consequently

    e(P1,S)>=4z,
    4z<=s+M-I.

Moreover, if a P0--star edge exists, then r>=2 and the incident star centre has physical multiplicity at least two.

## Proof of the fan

Let t of code P1 be adjacent to x of code S_c, with c even. The three odd leaves b of S_c belong to P1. For each spoke t--b, adjacency to x destroys the direct certificate. The singleton replacement has odd-centred code S_b, absent from the four-centre support. The reverse B-end replacement has code S_bar(b), whose centre is one of the other three even vertices. Therefore t must be adjacent to a physical star in each of those three classes, in addition to S_c.

The joint missing-pair ledger proves

    e(P1,S)+e(S)<=s+(M-I).

Dropping the nonnegative star-edge term and combining with the fan lower bound gives 4z<=s+M-I.

## Proof of replication

Suppose p in P0 is adjacent to x in S_c. For the star centre spoke x--c, the sole available singleton halfcube target has code P0 and must be nonadjacent to x. Since p is adjacent, another P0 vertex is required, so r>=2.

Also consider the P0 spoke p--c. The neighbour x contains c and destroys its direct certificate. The reverse odd-centred star is absent. The singleton replacement must therefore be a different physical S_c vertex nonadjacent to p and sharing no A-neighbour with p. Hence the S_c multiplicity is at least two.

## Consequence

Parity-star density cannot be added freely to an otherwise dense parity block. It requires missing parity pairs, four-centre P1 fans and physical replication. The n=26 positive fixture realizes the smallest pattern found in the bounded grid and demonstrates that the inequalities are obligations rather than a nonexistence proof.
