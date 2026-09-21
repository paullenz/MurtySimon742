# Coordinate-face star support forces the outward coordinate code

21 September 2026. Internally proved at Q3-transversal scope; external review open.

Suppose the four star centres are exactly the lower coordinate face T={0,1,2,3}. Then C21 (the opposite, upper face) occurs and C20 (the centre-containing lower face) does not occur. Moreover C00,C01,C10,C11,P0,P1 all occur, so n>=20. No existence or optimal-density claim is made for this support orbit.

## 1. The inward face C20 is A-isolated

For a C20 spoke at lower vertex s, its standard outside target is s xor 4 in the upper face. A singleton-star replacement would need an upper-centred star; a reverse B-end replacement would also need an upper-centred star. Neither is available. Thus every A-neighbour of a C20 vertex must avoid all four upper cube vertices. Among four-element codes this permits only C20 itself.

A same-C20 edge has no direct certificate, no undominated B target, and no complementary-code third-A certificate, because a C20--C21 edge has already been excluded. Hence every C20 vertex is A-isolated. C20 and C21 cannot both occur, since their disjoint codes then give a diameter-two failure.

Cube-edge criticality in direction 2 requires at least one of these two coordinate codes. Exactly one occurs.

## 2. The inward-only case forces a physical star matching

Suppose C20 occurs and C21 is absent. For each physical star vertex x of lower centre c, its direction-2 leaf at s=c xor 4 lacks its halfcube witness. It must use an adjacent star y of centre bar(s)=c xor 3. The certificate says x is y's unique bridge to y's antipode. Applying the same missing-code requirement to y gives the reverse uniqueness. Thus S0,S3 and S1,S2 are physically perfectly matched, and every star has exactly one antipode bridge.

This statement is about physical vertices. It follows from absence of C21, not merely adjacency to one C21 copy.

## 3. Stars must then be anticomplete to halfcubes

A halfcube neighbour whose code contains a star's antipode is forbidden by the unique matching bridge. Suppose instead its code H avoids that antipode. The star-halfcube edge has intersecting B-codes and cannot be certified directly. On the star side it has neither a B-target certificate nor an opposite-star third-A target, since opposite centres are upper and absent. On the halfcube side there is no undominated B target. Its only remaining certificate would require a complementary-H neighbour of the star; that complementary code contains the antipode and is forbidden. Thus no star-halfcube edge exists.

## 4. Mandatory complementary coordinates become isolated

All four codes C00,C01,C10,C11 are forced by the direction-0 and direction-1 star leaf spokes: their reverse star alternatives have upper centres and are absent. Both parity codes are forced by centre spokes for the same reason.

Take any coordinate vertex of type C_i^epsilon for i=0 or 1. At its two upper spokes, the singleton replacement stars have upper centres and are absent; reverse replacements would require star neighbours, excluded above. Its A-neighbour codes must therefore avoid both upper vertices on the opposite i-side. Among halfcubes the only such types are C_i^epsilon and C20. The latter is isolated. A same-code edge has no certificate because the complementary coordinate cannot be adjacent to the endpoint. Hence every vertex of C_i^epsilon is A-isolated.

Both complementary orientations are mandatory, contradicting diameter two. The inward-only case is impossible. Therefore C21 occurs and C20 is absent.

## Multiplicity caution and remaining work

If C21 has exactly one physical vertex, it cannot be adjacent to a star: such an edge would need to be that star's unique antipode bridge, while the star's direction-2 spoke would then require a second bridge from the diagonal star class. But this argument does NOT extend to multiple C21 copies: a nonadjacent second copy can be a singleton spoke witness. Any subsequent proof must preserve that physical distinction.

The lower order count is four star centres, four other coordinate codes, two parity codes and at least one C21 vertex: at least eleven A vertices and hence n>=20. Realizability, multiple outward-face copies and sharp density remain open.

## Superseded branch status

`COORDINATE_FACE_PLANE_IMPOSSIBLE.md` subsequently eliminates the outward orientation for arbitrary physical multiplicities. This file remains the necessary first half of that proof.
