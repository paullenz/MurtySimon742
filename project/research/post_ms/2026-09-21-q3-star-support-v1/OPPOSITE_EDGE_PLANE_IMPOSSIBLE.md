# Opposite-parallel-edge four-star support is impossible

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open. Corrected after same-session hostile replay.

## Theorem

No diameter-two-critical graph in the Q3-antipodal-transversal setting has exactly the four star centres {0,1,6,7}. Thus the opposite-parallel-edge affine-plane orbit is eliminated for arbitrary physical multiplicities.

## Proof

The preceding raw argument shows that exactly one of C00,C01 occurs. Translate by cube vector 1 if necessary, so C00 occurs and C01 is absent. The missing-coordinate matching lemma then gives a physical perfect matching between S0 and S6. Every S6 vertex has a unique A-neighbour whose code contains its undominated antipode 1, namely its matched S0 vertex. Therefore no C10 vertex can be adjacent to S6, since 1 belongs to C10.

Let x be any physical C10 vertex; this class is mandatory. For its spoke x--1, the standard lost pair is (x,3), singleton S3 is absent, and the reverse replacement S6 is forbidden by the physical uniqueness above. Hence every A-neighbour of x avoids 3.

For x--0, the standard pair is (x,2), singleton S2 is absent, and reverse S7 is unavailable because S7 contains 3. Hence every A-neighbour of x avoids 2. Among available codes, exactly C10 and C21 avoid both 2 and 3. Thus

    N_A(x) has code in {C10,C21}.

In particular x is not adjacent to any C11 vertex y. Since C10 and C11 have disjoint B-codes, diameter two requires a common A-neighbour z. It cannot have code C10: applying the same neighbour restriction to z would prohibit its adjacency to y, whose C11 code contains 2 and 3. Therefore z has code C21.

This holds for every physical pair x in C10, y in C11. Consequently every C10 vertex has a C21 neighbour, and every C11 vertex has a C21 neighbour.

Now consider cube edge 4--6 in direction 1. A clean entry from its C10 side would require a physical C10 vertex all of whose A-neighbours avoid the outside target 6. Every such vertex has a C21 neighbour, and C21 contains 6. No C10 entry is clean. Symmetrically, a clean C11 entry would require all its A-neighbours to avoid outside target 4, but every C11 vertex has a C21 neighbour and C21 contains 4. No C11 entry is clean. The clean cube-entry lemma says these are the only possible criticality orientations for edge 4--6. The edge is noncritical, contradiction.

The C01-present orientation is symmetric. This completes the arbitrary-multiplicity exclusion.

## Correction record and trust boundary

The first same-session draft incorrectly said C10 was the only available code avoiding both 2 and 3; C21 also does. Hostile replay caught this before final preservation. Retaining C21 exposes the forced bridge above, which yields the clean cube-edge obstruction. The corrected proof has been replayed against the primitive bitset tables.

The theorem uses physical matching uniqueness, exhaustive spoke certificates, diameter two and cube-edge criticality. It does not use SAT, Hall cuts or the conditional selected-source capacity theorem. The earlier parity-factor reduction is now vacuous for actual graphs.
