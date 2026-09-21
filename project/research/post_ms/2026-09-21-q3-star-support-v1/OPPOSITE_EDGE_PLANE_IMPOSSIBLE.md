# Opposite-parallel-edge four-star support is impossible

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

No diameter-two-critical graph in the Q3-antipodal-transversal setting has exactly the four star centres {0,1,6,7}. Thus the opposite-parallel-edge affine-plane orbit is eliminated for arbitrary physical multiplicities.

## Proof

The preceding raw argument shows that exactly one of C00,C01 occurs and the other is absent. Translate by cube vector 1 if necessary, so C00 occurs and C01 is absent. The missing-coordinate matching lemma then gives a physical perfect matching between S0 and S6. In particular, every S6 vertex has a unique A-neighbour whose code contains its undominated antipode 1, namely its matched S0 vertex. Therefore no C10 vertex can be adjacent to an S6 vertex, since 1 belongs to C10.

Let x be any physical C10 vertex; this class is mandatory. Consider its spoke x--1. The standard lost pair would be (x,3). If an A-neighbour of x contains 3, that certificate is destroyed. The only singleton-code replacement has star code S3, absent from the support, and the only reverse B-end replacement has code S6. The latter would require an x--S6 edge, which the preceding physical uniqueness excludes. Hence every A-neighbour of x avoids 3.

Now consider x--0. Its standard lost pair is (x,2). The singleton replacement S2 is absent. The reverse replacement would require an A-neighbour of code S7. But every S7 code contains 3, while the preceding paragraph proves that no A-neighbour of x may contain 3. Thus the reverse channel is also unavailable, and every A-neighbour of x avoids 2.

Among every code available in this support branch—C00,C10,C11,C20,C21,P0,P1,S0,S1,S6,S7—the only code avoiding both 2 and 3 is C10 itself. Consequently

    N_A(x) is contained in the physical C10 population

for every C10 vertex x.

The mandatory complementary class C11 is nonempty. A C10 vertex x and a C11 vertex y have disjoint B-neighbourhoods, so diameter two requires a common A-neighbour z. Since z is adjacent to x, it has code C10. Applying the same conclusion to z says all its A-neighbours have code C10, so z cannot be adjacent to y of code C11. Contradiction.

The C01-present orientation is symmetric. This completes the arbitrary-multiplicity exclusion.

## Trust boundary and consequence

The proof uses only physical matching uniqueness, the exhaustive local spoke-certificate classification, and diameter two. It does not use the conditional selected-source capacity theorem, Hall cuts, density inequalities or the bounded SAT search.

The SAT search was useful diagnostically but is now superseded for nonexistence: its exact exclusions through the tested multiplicities are consequences of this theorem. The earlier parity-factor reduction remains a valid conditional description but its antecedent is impossible.

Therefore an exactly four-centre star support can belong only to the parity-plane or coordinate-face orbit. The parity-plane orbit is realized at n=19; the coordinate-face orbit remains open and has n>=20.
