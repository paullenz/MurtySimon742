# Coordinate-face four-star support is impossible

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

No diameter-two-critical graph in the Q3-antipodal-transversal setting has exactly the four star centres {0,1,2,3}. Thus the coordinate-face affine-plane orbit is eliminated for arbitrary physical multiplicities.

## Proof

The preceding orientation theorem proves that C21 occurs and C20 is absent. Absence of C20 forces physical perfect matchings S0--S3 and S1--S2. Each matched partner is the other's unique A-neighbour whose code contains its undominated antipode.

Let x be a physical C10 vertex, which is mandatory. Consider its spoke x--4. Its standard outside target is 6. The singleton replacement S6 is absent from the support. The only reverse B-end replacement is an adjacent S3 vertex. But the undominated antipode of S3 is 4, which belongs to C10; the S0--S3 matching already supplies the unique A-neighbour of each S3 vertex whose code contains 4. Hence no C10--S3 edge exists. Criticality of x--4 therefore forces every A-neighbour of x to avoid 6.

Similarly, for x--5 the standard outside target is 7, singleton S7 is absent, and the reverse replacement S2 is unavailable: S2 has undominated antipode 5 in C10 and its unique such neighbour is its matched S1 vertex. Thus every A-neighbour of x avoids 7.

Among the available codes C00,C01,C10,C11,C21,P0,P1,S0,S1,S2,S3, exactly C10,S0,S1 avoid both 6 and 7. Therefore every A-neighbour of every C10 vertex has one of these three codes.

The mandatory complementary class C11 is nonempty and has B-code disjoint from C10. Diameter two requires a common A-neighbour z of any physical C10 vertex x and any physical C11 vertex y.

- If z has code C10, applying the preceding restriction to z forbids adjacency to y, whose code contains 6 and 7.
- If z has code S0, adjacency to y is impossible because y's C11 code contains the undominated antipode 7 of S0, while S0's matched S3 partner is its unique A-neighbour whose code contains 7.
- If z has code S1, adjacency to y is impossible because C11 contains the undominated antipode 6 of S1, while its matched S2 partner is uniquely responsible for that bridge.

No common A-neighbour exists, contradiction. Other coordinate faces are cube-isometric copies.

## Consequence

Together with `OPPOSITE_EDGE_PLANE_IMPOSSIBLE.md` and the affine-plane necessity theorem, this leaves only the two parity planes as exactly four-centre star supports. They are realized by the explicit families in this package. Hence exactly four star centres occur if and only if, up to cube isometry, their support is a parity class, subject to the standing Q3-antipodal-transversal hypotheses.

The proof is independent of SAT and of the conditional Hall/source-tuple machinery. The bounded coordinate-face search is retained only as historical diagnostic evidence.
