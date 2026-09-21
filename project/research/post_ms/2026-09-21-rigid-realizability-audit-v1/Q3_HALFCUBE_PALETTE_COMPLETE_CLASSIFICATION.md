# Complete classification of the Q3-root odd-halfcube palette branch

Date: 2026-09-21

## Theorem

Let `G` be diameter-2-critical. Fix a root `v` with `B=N(v)` inducing `Q3`, and put `A=V(G)\(B∪{v})`. Assume that every `x∈A` has `N_B(x)` equal to one of the eight odd affine halfcubes of `Q3`.

Then G is exactly a dense parity-bridge blow-up as follows:

1. For each coordinate direction `j=1,2,3`, exactly one of the two coordinate halfcube orientations may occur, and that orientation occurs with positive multiplicity.
2. Coordinate-type A-vertices have **no A-neighbours**.
3. Parity-type A-vertices may occur on either or both parity sides.
4. A parity vertex can be adjacent in A only to the opposite parity side.
5. If both parity sides are nonempty, the A-graph between them is the complete bipartite graph `K_{p,q}`.
6. There are no other A-A edges.

Thus the family `X3_PARITY_BRIDGE_DENSE_BLOWUP_FAMILY.md` is not merely a construction: it is the **entire D2C branch inside the odd-halfcube Q3 palette**.

## Local A-B criticality lemma

Let `x∈A` and `H=N_B(x)`.

### Coordinate H

Suppose `H={s:s_j=epsilon}`. Fix an A-B edge `xs` with `s∈H`, and let `t=s xor e_j`, the unique cube neighbour of s outside H.

After deleting `xs`, the endpoint pair `(x,s)` still has B-mediated two-paths because the coordinate halfcube induces a square. The only possible B-vertex whose unique H-neighbour is s is t. Pairs involving a different A-vertex cannot become long: if another A-vertex z shares s then two odd halfcubes containing s intersect in at least two B-vertices, while if s is outside `H_z`, that halfcube dominates Q3 and supplies a B two-path from s to z.

Therefore criticality of `xs` forces `(x,t)` to be the broken pair. In particular no A-neighbour y of x may satisfy `t∈H_y`, or else `x-y-t` survives.

As s ranges over H, t ranges over the whole opposite coordinate halfcube `H^c`. Hence every A-neighbour y of x must have `H_y` disjoint from `H^c`. Since `H_y` is itself a 4-set halfcube, this means

`H_y=H`.

**Coordinate adjacency rule:** a coordinate-type A-vertex can only have A-neighbours of its exact same halfcube type.

### Parity H

Now let H be one parity side. H is independent in Q3. For an A-B edge `xs`, after deleting xs the endpoints x,s have no common B-neighbour. A nonendpoint B witness cannot work instead: every outside-parity cube vertex has three neighbours in H, so no H-entry edge is unique.

Thus `xs` can be critical only if the endpoints themselves lose all two-paths. Therefore no A-neighbour y of x may contain s in `H_y`. Requiring this for every `s∈H` forces every A-neighbour y of x to have a halfcube disjoint from H, namely the opposite parity side.

**Parity adjacency rule:** a parity-type A-vertex can only have A-neighbours on the opposite parity side.

## Coordinate vertices are A-isolated

Suppose two coordinate vertices x,y of the same halfcube H were adjacent. Their endpoints share all four B-neighbours, so the edge xy cannot be direct-critical. Any A-edge criticality certificate for xy would have to use an A-vertex z whose halfcube is disjoint from H, i.e. the opposite coordinate side, with one of x,y as the unique middle vertex of a two-path. But the coordinate adjacency rule forbids x or y from being adjacent to such a z. Hence xy is not critical, contradiction.

Therefore every coordinate-type A-vertex is A-isolated.

It follows immediately that opposite orientations of one coordinate direction cannot both occur: vertices on those two sides would have disjoint B-neighbourhoods and no A-edges, hence distance greater than two.

## Every coordinate direction occurs

Consider a cube edge in direction j. Root mediation keeps all B-B pairs within distance two after its deletion. An odd-halfcube A-vertex can have that cube edge as a unique H-entry edge only when its defining linear form has Hamming weight one and support exactly j. Parity halfcubes have three H-entry edges at every outside vertex.

Hence criticality of every direction-j cube edge requires at least one coordinate-j A-vertex. Together with the previous paragraph, exactly one orientation of each coordinate direction occurs, with positive multiplicity.

## The parity graph is complete bipartite

By the parity adjacency rule, the only possible parity A-edges run between the two opposite parity sides. Coordinate vertices are A-isolated.

If both parity sides occur, take x on one side and y on the other. Their B-neighbourhoods are disjoint. They therefore need A-distance at most two. But in a bipartite graph whose only edges run between the two parity sides, a nonadjacent opposite-side pair has no common A-neighbour: a common neighbour would have to lie simultaneously on both sides. Coordinate vertices cannot mediate because they are A-isolated.

Therefore every opposite-parity pair xy must itself be an edge. The parity A-graph is exactly `K_{p,q}`.

Conversely, `X3_PARITY_BRIDGE_DENSE_BLOWUP_FAMILY.md` proves edge-by-edge that every graph of this form is D2C. This completes the classification.

## Exact extremal form inside the palette

Write `a=|A|`, and let p,q be the two parity multiplicities. Then

`m=20+4a+pq`.

For fixed a, the classification shows the densest possible graph in the **entire odd-halfcube palette branch** has one vertex in each mandatory coordinate class and splits the remaining `a-3` vertices as evenly as possible between the parity sides:

`m_palette_max(a)=20+4a+floor((a-3)^2/4)`.

Therefore

`M(n)-m_palette_max(a)=floor(a^2/4)-floor((a-3)^2/4)-3`, `n=9+a`,

which is exactly

- `3a/2-5` for even a;
- `(3a-11)/2` for odd a.

So, except for X3 at n=12, this whole rooted palette branch is below M, and its best possible asymptotic deficit is linear with leading coefficient `3/2` in a.

## Significance

This closes a natural graph-level branch that the earlier scalar/rigid machinery did not distinguish. The mandatory X3 exception, its independent-A blow-ups, and the new dense parity-bridge escape are all manifestations of one completely classified Q3-root palette.

Most importantly, quadratic A-density is possible, but only in the opposite-parity complete-bipartite core. The three coordinate witness classes are forced to remain outside that core and A-isolated, producing the exact linear tax. Any Q3-root construction closer to M than this must therefore leave the odd-halfcube palette itself; it cannot be obtained by merely rearranging A-edges among these eight natural codes.

This theorem is graph-level and independent of the conditional rigid complete Hall-cut/source-tuple machinery.
