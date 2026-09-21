# All three-centre star supports are impossible

Date: 21 September 2026. Status: internally proved at stated scope; external review open.

## Theorem

Let G be diameter-two-critical with root neighbourhood Q3 and every A-to-B code an antipodal transversal. If any star code occurs, at least **four distinct star centres** occur. There is no restriction on physical multiplicities of the permitted codes.

One- and two-centre supports were excluded in `AT_LEAST_THREE_STAR_CENTRES.md`. Here we exclude all three-centre supports.

## Primitive tests used below

For a coordinate code H=C_i^epsilon, s in H and t=s xor e_i, an A-neighbour code K containing t kills the standard certificate of the spoke xs. Replacement then needs either a nonadjacent star S_t or an adjacent star S_(bar s).

For a parity code P, a neighbour containing s in P kills the direct certificate of xs; replacement needs S_s nonadjacent or S_(bar s) adjacent.

For an A-edge with endpoint codes H,K, at least one endpoint must have: a disjoint-code direct certificate; an undominated B target in the other code; or a disjoint-code third target adjacent to the other endpoint. Halfcubes dominate B, while S_c has sole undominated target bar c. The only disjoint transversal is the complementary code.

These are necessary conditions from raw edge deletion. The finite neighbour lists below follow by applying them symmetrically; no assumption about code multiplicity or shared witnesses is used.

### Clean cube-entry lemma

For a cube edge st in direction i, deletion can only be witnessed by a pair (x,t) with x of coordinate type containing s, or symmetrically (y,s) from the opposite coordinate type. In either case the coordinate vertex's A-neighbours must all avoid the outside target. Root-B and B-B pairs retain their other root/cube paths; A-A paths of length two cannot use a B-B edge; stars and parity codes have no unique cube entry. Thus if neither coordinate orientation has a clean physical witness, st is noncritical.

## Three symmetry types

The unordered distance triples of three distinct cube vertices are exactly (1,1,2), (1,2,3), and (2,2,2), represented by {0,1,2}, {0,1,6}, and {0,3,5}. Translations and coordinate permutations send every triple to one of these. There are respectively 24, 24 and 8 labelled supports.

## Case I: centres {0,1,2}

Write C00={0,2,4,6}, C01={1,3,5,7}; bit index 0 is the least significant bit.

The primitive A-B tests give N_A(C00) types contained in {C00,S0}. Same-C00 edges fail A-edge criticality: their only possible third-A certificate would require a forbidden C00--C01 edge. Hence

    N_A(C00) has types in {S0}.

For C01 the initial symmetric A-B list is {C01,C11,C21,P1,S0,S1,S2}. The A-edge test eliminates C01,C11,C21 and P1: each endpoint's complementary-code third target has no allowed adjacency to the other endpoint. It also eliminates S1: C00--S1 is forbidden, S1's antipode 6 is outside C01, and S6 is absent. Therefore

    N_A(C01) has types in {S0,S2}.

The direction-0 leaf of S0 forces C01 (the replacement star S6 is absent). The direction-0 leaf of S1 forces C00 (S7 absent). Thus both coordinate types occur. Every vertex in either class must have an A-neighbour, because it must be within distance two of a vertex of the complementary code.

Consider the cube edge 0--1. Any C00 witness has an A-neighbour of type S0, whose code contains outside target 1. Any C01 witness has an A-neighbour of type S0 or S2, both containing outside target 0. Neither side has a clean cube-entry witness. The edge 0--1 is noncritical, contradiction.

## Case II: centres {0,1,6}

Use direction 1, C10={0,1,4,5} and C11={2,3,6,7}.

The initial symmetric A-B tests give

    N_A(C10) has types in {C10,S1},
    C10--S6 is forbidden.

If a C10 vertex x is adjacent to S1, the spoke x1 loses its standard outside-target certificate 3. Its singleton replacement would need absent S3. Its reverse B-end replacement needs a C10--S6 edge, already forbidden. Hence C10--S1 is impossible. Same-C10 edges then have no A-edge certificate, since C10--C11 is forbidden. Thus every C10 vertex is A-isolated.

S0's direction-1 leaf forces C11 (replacement S5 absent). S6's direction-1 leaf forces C10 (replacement S3 absent). These forced complementary codes cannot be within distance two when the C10 vertex is A-isolated. Contradiction.

## Case III: centres {0,3,5}

All three centres have even parity. The initial symmetric A-B tests yield:

- no coordinate-star or inter-coordinate-type edges;
- each coordinate type can have neighbours only in its own type and, for C01,C10,C20, additionally P0;
- P1 can neighbour only P0;
- P0 can additionally neighbour the three stars and C01,C10,C20.

A same-coordinate edge cannot have a complementary-coordinate third target. A coordinate--P0 edge cannot be certified from the coordinate side (its opposite coordinate cannot neighbour P0), or from the parity side (P1 cannot neighbour that coordinate). Hence all coordinate vertices are A-isolated.

For a P0--S_c edge, P1 cannot neighbour S_c, bar c is odd and outside P0, and S_(bar c) is absent. It has no A-edge certificate. Hence parity and star populations are anticomplete.

Same-centre star edges have no certificate because their opposite star type is absent. All remaining A-edges involving stars therefore run between different classes among S0,S3,S5. These centre distances are all two, so every such neighbour contains the source's antipode.

The following coordinate types are forced by star leaf spokes whose alternate star centre is absent:

| Source star | Leaf | Forced coordinate |
|---|---:|---|
| S0 | 1 | C01 |
| S3 | 1 | C10 |
| S5 | 1 | C20 |

Because coordinates are A-isolated, their complementary types C00,C11,C21 cannot occur. The remaining leaf spokes now force each star vertex to have a neighbour in **each** of the other two star classes:

| Source | First required neighbour type | Second required neighbour type |
|---|---|---|
| S0 | S3 (leaf 4) | S5 (leaf 2) |
| S3 | S0 (leaf 7) | S5 (leaf 2) |
| S5 | S0 (leaf 7) | S3 (leaf 4) |

Every star vertex has at least two antipode bridges. But a cross-class star edge has intersecting B-codes, no opposite-star third target, and can be critical only as the **unique** antipode bridge of at least one endpoint. Both endpoints have at least two bridges. No star edge is critical, contradiction.

## Consequence

All 56 three-centre supports are excluded by these three bounded hand arguments. Together with the previous theorem, any nonempty star support has at least four distinct centres. The full antipodal-transversal branch remains open: four or more centres and nontransversal codes are not settled here.

The companion raw code-relation replay is a finite audit of the necessary neighbour lists, not a substitute for the physical-vertex arguments above. It retains X3 and the star-free parity-bridge family as positive controls.
