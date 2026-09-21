# A four-centre star support must be an affine plane

Date: 21 September 2026. Status: internally proved at Q3-transversal scope; external review open.

## Theorem

Let G be a diameter-two-critical graph with root neighbourhood Q3 and all outside codes antipodal transversals. If exactly four distinct star centres occur, their set T is an affine plane in F_2^3. Equivalently,

    xor of the four centres = 000.

Together with `THREE_CENTRE_SUPPORTS_IMPOSSIBLE.md`, this says that the smallest remaining star support has four centres with forced additive structure. This is a necessary condition, not an existence theorem for those 14 planes.

## A clean-entry obstruction

Suppose complementary coordinate types H,H' both occur, neither can be adjacent directly to the other, and every possible common A-neighbour of an H vertex and an H' vertex has one fixed star code S_c. Consider a cube edge st in that direction with s in H, t in H', and s,t both in S_c.

If an H vertex were a clean entry to t, none of its A-neighbours could have a code containing t. But its distance-two path to any physical H' vertex must use S_c, which contains t. Thus no H vertex is clean. The same argument with s excludes a clean H' entry. Hence st is noncritical. This is a multiplicity-free obstruction: every physical complementary pair must have a common neighbour, and all possible types of that neighbour are blocked.

An A-isolated mandatory coordinate type is an even simpler obstruction when its complement is also mandatory.

## Cube-isometry classification

There are six isometry classes of four-element cube subsets. Three are affine planes:

- coordinate face, representative {0,1,2,3}: 6 supports;
- two opposite parallel edges, {0,1,6,7}: 6 supports;
- parity tetrahedron, {0,3,5,6}: 2 supports.

The remaining classes have nonzero xor:

- claw {0,1,2,4}: 8 supports;
- length-three path {0,1,2,5}: 24 supports;
- {0,1,2,7}: 24 supports.

Translations and coordinate permutations cover all 70 subsets. The three nonplane classes are excluded below using the same raw spoke and A-edge certificate tests as in the three-centre proof.

## Case I: claw {0,1,2,4}

The raw necessary neighbour lists imply:

    N_A(C00) has types in {S0};
    C00--C01 is forbidden.

Consequently any common A-neighbour of a C00 and C01 pair has type S0. Both coordinate types are forced: the direction-0 leaf of S0 forces C01 (alternative S6 absent); that of S1 forces C00 (alternative S7 absent).

The cube edge 0--1 has both endpoints in S0. The clean-entry obstruction applies, contradiction.

The list N_A(C00)={S0} is checked from the primitive tests: initially only C00 and S0 survive symmetric A-B restrictions; a same-C00 edge has no certificate since a complementary C01 target cannot be adjacent to C00. No parity or other star code survives the A-B tests at C00.

## Case II: path {0,1,2,5}

The necessary neighbour lists give

    N_A(C10) has types in {S0};
    C10--C11 is forbidden.

Here C10 is bit 1 equal to zero. S2's direction-1 leaf at 0 forces C10 (alternative S7 absent). S1's direction-1 leaf at 3 forces C11 (alternative S4 absent). Any common A-neighbour of a complementary C10,C11 pair therefore has type S0.

Both endpoints of the cube edge 0--2 lie in S0. Clean-entry criticality fails, contradiction.

The coordinate list follows by the symmetric raw A-B tests and then the A-edge tests. Any temporary extra candidate must supply a complementary-coordinate third target, an undominated B target, or an opposite-star third target; none is available except for C10--S0. The companion finite replay reconstructs this list from the cube, rather than hard-coding it.

## Case III: support {0,1,2,7}

The raw certificate tests make every C20 vertex A-isolated. C20 is the face with bit 2 equal to zero.

Both C20 and C21 are forced: S7's direction-2 leaf at 3 requires C20 (alternative S4 absent), while S0's direction-2 leaf at 4 requires C21 (alternative S3 absent). They have disjoint B-codes and no possible distance-two connection through an A-isolated endpoint. Contradiction.

## Conclusion and trust boundary

The 56 nonplane four-centre supports are excluded for arbitrary multiplicities of all allowed codes. The remaining 14 four-centre supports are precisely the affine planes. No claim is made that any of them is realizable. Five through eight centres and nontransversal A-codes remain open.

This finite geometry reduction should guide the next structural work: analyze the three affine-plane orbits directly, keeping physical witness uniqueness and cube-edge criticality explicit. It is stronger than a finite search over bounded graph sizes, because each excluded support covers unbounded code multiplicities.
