# The order-19 four-star graph is unique up to cube symmetry

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

Let G be diameter-two-critical with root neighbourhood Q3, antipodal-transversal outside codes, and exactly four distinct star centres. If n=19, then after a cube isometry its A-code multiset and A-edges are

    C00,C01,C10,C11,C20,S0,S3,S5,S6,P0,

    S0--S3, S5--S6,
    P0--C00, P0--C01, P0--C10, P0--C11.

Thus the explicit 19-vertex, 66-edge construction is the unique equality graph in this rooted branch, up to cube isometry and relabelling physical vertices.

## Proof

The four-centre classification forces a parity plane; normalize it to the even centres {0,3,5,6}. The order lower-bound proof forces all four star types, P0, and at least five of the six coordinate codes. Since |A|=10 at n=19, each forced type occurs exactly once, precisely one coordinate code is absent, and P1 is absent.

Normalize the absent coordinate to C21. Its missing-code physical matching forces the star edge S0--S3. Every star must bridge its unique undominated cube antipode. The remaining S5 and S6 vertices cannot use an odd-centred opposite star, and their unique available physical bridge is each other. Thus S5--S6 is forced.

Each star edge is critical only when it is the unique antipode bridge of at least one endpoint: the star codes intersect, there is no opposite-star third target, and the only B target is the endpoint's undominated antipode. Once the two forced edges match all four physical stars, every additional star edge would give both endpoints a second bridge and would be noncritical. Hence the star subgraph is exactly this perfect matching.

The raw spoke and A-edge classification permits a coordinate vertex to meet only P0 in this code population. The two present complementary coordinate pairs C00,C01 and C10,C11 have disjoint B-codes and are not adjacent. Diameter two therefore forces their unique vertices to share the sole P0 vertex, giving all four displayed coordinate--P0 edges.

The remaining coordinate C20 has absent complement C21. A C20--P0 edge has no certificate: their B-codes intersect; halfcubes have no undominated B target; the missing C21 eliminates the coordinate-side complementary third target; and absent P1 eliminates the parity-side complementary target. Thus C20 is A-isolated.

A P0--star edge similarly has intersecting B-codes, no usable undominated B target, absent P1 on the parity side, and absent odd opposite-star code on the star side. No other A-edge survives the exhaustive certificate alternatives. This determines G[A]. Direct inspection gives six A-edges and hence

    m=20+4(10)+6=66.

Other choices of the missing coordinate are cube-isometric and give the correspondingly relabelled perfect matching.

## Independent finite replay

`check_order_19_uniqueness.py` checks all six possible missing coordinate codes. After applying only the independently audited necessary type relation, each case has 15 possible A-edges and 2^15 subsets. Exactly one subset is D2C in each labelled case, always with six edges and the structure above. This finite replay audits the hand classification; it is not the proof.
