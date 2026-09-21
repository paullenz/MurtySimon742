# Q3 antipodal transversals and the star-code certificate fan

Date: 2026-09-21

## Scope

Let `G` be diameter-2-critical. Fix a root `v` with `B=N(v)` inducing `Q3`, and put `A=V(G)\(B∪{v})`. In this note assume only that every `x∈A` has a four-element B-neighbourhood `H_x=N_B(x)` meeting every antipodal pair of Q3 in exactly one vertex. No rigid-cut, Hall, source-tuple, or selected-system hypothesis is used.

The purpose is to identify the first graph-level branch outside the odd affine halfcube palette.

## 1. The 16 antipodal transversals split 8+8

Q3 has four antipodal pairs. Hence there are exactly `2^4=16` four-sets meeting each antipodal pair exactly once.

Exactly eight are the odd affine halfcubes

`{z : l(z)=epsilon}`

for `l∈{100,010,001,111}` and `epsilon∈F_2`.

The other eight are precisely the closed cube neighbourhoods

`S_c=N_Q[c]={c,c⊕e_1,c⊕e_2,c⊕e_3}`,

one for each `c∈F_2^3`.

Proof: translate so that a chosen transversal contains `000`. The remaining choices select one vertex from each of `(001,110)`, `(010,101)`, `(100,011)`. The four affine choices through `000` are the three coordinate faces and the even-parity halfcube; the other four are the stars centred at `000,001,010,100`. Complementing gives the remaining eight. Equivalently, direct enumeration gives the same disjoint 8+8 partition.

Thus the complete odd-halfcube classification leaves only one type of antipodal-transversal code to understand: a star `S_c`.

## 2. General edge-criticality observation

If an edge `xs` with `x∈A`, `s∈B` is deleted, any newly long pair must contain `x` or `s`: every length-at-most-two path using `xs` is of the form `x-s-z` or `s-x-z`.

Let `x` have star code `H_x=S_c=N_Q[c]`. Every edge `xs`, `s∈S_c`, has an internal B two-path after deletion:

- for `s=c`, the three leaves of `S_c` are common B-neighbours of x and c;
- for a leaf `s=c⊕e_i`, the centre c is a common B-neighbour of x and s.

So no star A-B edge is direct-critical at its own endpoints.

For a newly long pair `(x,z)` with `z∈A` adjacent to s, a necessary condition is

`H_x ∩ H_z = {s}`;

otherwise another common B-neighbour survives.

For a newly long pair `(s,y)` with `y∈A` adjacent to x, a necessary condition is

`H_y ∩ N_Q[s] = ∅`;

otherwise either `sy` itself or a B-mediated two-path survives.

The B-vertex and root alternatives cannot be critical pairs here: at the centre all cube neighbours already lie in `S_c`; at a leaf each outside cube neighbour has a second neighbour in `S_c`; and x has three other B-neighbours for the root pair.

These observations give an exact code-level dichotomy for every star A-B edge.

## 3. Exact four-spoke star certificate fan

For each `s∈S_c`, define `D_s` to be the unique antipodal transversal with

`D_s ∩ S_c = {s}`.

Then `D_s` is always an odd affine halfcube:

- for the centre `s=c`, `D_c` is the parity halfcube containing c;
- for the leaf `s=c⊕e_i`, `D_s` is the coordinate halfcube on the side opposite c in coordinate i.

Also the unique antipodal transversal disjoint from `N_Q[s]` is

`Q3 \ N_Q[s] = N_Q[bar s]=S_{bar s}`.

Therefore criticality of the physical edge `xs` forces at least one of the following two mechanisms:

### Halfcube-side certificate

There is a vertex `z∈A` with code `H_z=D_s` such that deletion of `xs` can make `(x,z)` long. In particular xz must be a nonedge and no other common A-neighbour may survive.

### Star-neighbour certificate

There is a vertex `y∈A` adjacent to x with code

`H_y=S_{bar s}=N_Q[bar s]`,

so deletion of `xs` can make `(s,y)` long. Again the full D2C certificate additionally requires no surviving A-mediated two-path.

The two code types are unique. Thus a star vertex carries four distinct physical certificate spokes:

- centre c: parity halfcube through c **or** adjacent opposite-centre star `S_{bar c}`;
- leaf `c⊕e_i`: opposite-coordinate halfcube in direction i **or** adjacent star `S_{bar(c⊕e_i)}`.

No one typed vertex can discharge two different spokes.

A star code is not a dominating set of Q3: its unique undominated B-vertex is `bar c`. Diameter two therefore additionally forces x to have an A-neighbour whose B-code contains `bar c`.

## 4. Cube-edge control remains coordinate-halfcube only

A star transversal cannot by itself provide the unique B-entry certificate for a cube edge. For a star `S_c`, an outside vertex at distance two from c has two neighbours in `S_c`, while the antipode `bar c` has none. A parity halfcube gives three entries at every outside vertex. Only a coordinate halfcube has an outside vertex with a unique neighbour across a cube edge.

Consequently, in any D2C graph satisfying the antipodal-transversal hypothesis, cube-edge criticality still forces at least one coordinate-halfcube A-vertex in each of the three coordinate directions.

## 5. Coordinate-star collision lemma

Let `z` have coordinate-halfcube code `C={u:u_i=1-c_i}` and let `x` have star code `S_c`. Their B-codes meet in exactly the leaf `s=c⊕e_i`. Suppose `xz` is an A-edge.

Consider the physical A-B edge `zs`. Its usual coordinate certificate is the outside cube vertex c, because s is the unique C-neighbour of c. But `z-x-c` survives after deleting `zs`.

Could another certificate replace it? Under the transversal hypothesis:

- the unique transversal meeting C exactly in `{s}` is the star `S_c` itself, but that vertex x is adjacent to z, so `(z,x)` cannot become long;
- a B-end certificate `(s,y)` with `y∈N_A(z)` requires `H_y` to avoid `N_Q[s]`, hence requires a star `S_{bar s}`.

Therefore, **if no `S_{bar s}` star vertex is available as an A-neighbour of z, the edge `zs` is noncritical.**

This is the first exact collision between the antipode bridge needed by a star and the coordinate witnesses needed by cube-edge/star-spoke criticality.

## 6. No star can occur when `|A|<=6`

The immediate four-spoke fan gives `|A|>=5`. The two remaining small cases can be eliminated structurally.

### `|A|=5` is impossible

Let x have star code `S_c`. Its four other A-vertices must discharge its four distinct spokes exactly once. Since every halfcube-side spoke witness must be a nonneighbour of x, diameter from x to the undominated antipode `bar c` forces at least one spoke to use a star-neighbour witness y.

If y discharges a **leaf** spoke of x, then among the three vertices remaining besides x,y one must discharge x's centre spoke. That vertex is parity-type or another star, so at most two of the remaining three vertices are coordinate halfcubes. But cube-edge criticality needs all three coordinate directions. Contradiction.

If y discharges the **centre** spoke, then `H_y=S_{bar c}`. The three remaining vertices must discharge the three leaf spokes of x. For y, x in turn discharges y's centre spoke. The remaining three y-spokes are its three leaves. The x-leaf halfcube options are the coordinate sides opposite c; the y-leaf halfcube options are the opposite coordinate sides. The corresponding star options are likewise different (`S_{bar(c⊕e_i)}` versus `S_{c⊕e_i}`). Hence no one of the three remaining typed vertices can discharge the same leaf-direction spoke for both x and y. Contradiction.

Thus `|A|=5` is impossible.

### `|A|=6` is impossible: one-star case

Assume first that x is the only star vertex. Then all four spokes of x must use halfcube-side witnesses: the parity halfcube `P_c` through c and the three opposite coordinate halfcubes `C_i`. Those four witness vertices are nonadjacent to x.

The sixth A-vertex must provide the x-to-`bar c` diameter bridge. The only possibilities are:

1. the opposite parity halfcube `P_bar`, adjacent to x; or
2. a second copy of one of the `C_i`, with one copy kept nonadjacent as the spoke witness and the other copy adjacent to x.

(An extra halfcube not containing `bar c` cannot repair the missing distance.)

**Opposite-parity bridge.** `P_c` and `P_bar` have disjoint B-codes, so they must be at A-distance at most two. They cannot use x because `xP_c` is forbidden by the centre-spoke certificate. If `P_cP_bar` is an edge, then after deleting `xc` the intended pair `(x,P_c)` still has the path `x-P_bar-P_c`, so `xc` is noncritical. If instead a coordinate witness `C_i` is a common A-neighbour of `P_c,P_bar`, then the direction-i cube edge `c(c⊕e_i)` loses its only coordinate certificate: the `C_i-P_c-c` path survives after that cube edge is deleted, and no star/parity code can supply a unique cube entry. Contradiction.

**Duplicate-coordinate bridge.** If a second copy of `C_i` is joined to x to reach `bar c`, apply the coordinate-star collision lemma to that adjacent copy. There is no second star in this case, so the physical A-B edge at its unique intersection with `S_c` is noncritical. Contradiction.

Hence the one-star `|A|=6` case is impossible.

### `|A|=6` is impossible: at least two stars

If there are exactly two distinct star centres c,d and one star discharges a spoke of the other, then the relation is symmetric and `d∈N_Q[bar c]`.

- If `d=bar c`, the x-y star edge discharges the centre spoke for both. The remaining three leaf spokes of x require the three coordinate orientations opposite c, while those of y require the three opposite orientations. These are six distinct halfcube types, but only four nonstar vertices remain.
- If `d` is at distance two from c, the mutual star edge discharges one leaf spoke for each. The two remaining leaf directions require four distinct coordinate halfcube orientations, while the two centre spokes share at most one parity-halfcube type (the centres have the same parity). Thus at least five distinct halfcube types are required, again exceeding the four available nonstar vertices.

If the two stars have the same centre, neither can discharge any spoke of the other. Both therefore require the same four halfcube spoke types, all nonadjacent to each star. Neither then has an A-neighbour containing `bar c`: the other same-centre star does not contain it, the centre-parity witness does not contain it, and the three coordinate witnesses that do contain it are forced nonneighbours. Diameter two fails.

Finally, three or more stars leave at most three nonstar vertices. Cube-edge criticality forces those three to be coordinate halfcubes, so every star centre spoke must be discharged by an opposite-centre star. Opposite centres therefore have to occur in antipodal types. With only three star occurrences this either leaves some centre without its antipode or uses two antipodal centre types with multiplicity; in the latter case the two antipodal stars require opposite coordinate orientations for all three leaf spokes, which the same three coordinate vertices cannot simultaneously supply.

Thus no star occurs for `|A|<=6`.

### Small-order corollary

Under the antipodal-transversal hypothesis, any Q3-root D2C graph containing a star code satisfies

`|A|>=7`, hence `n=9+|A|>=16`.

So for `n<=15`, the independently verified odd-halfcube palette classification is automatically the **complete antipodal-transversal classification**, not merely one branch.

## 7. Diagnostic finite check

As a diagnostic only, an exhaustive bitset replay over all multisets of at most five antipodal-transversal codes, all A-edge subsets, and the fixed Q3-root skeleton found no star-containing D2C fixture. The unrestricted `a=5` scan first exceeded the local 60-second execution budget; after pruning by the necessary three-coordinate-direction condition it completed exhaustively. The proof above supersedes that finite observation for `a<=6`; the scan is retained only as a regression hint.

## 8. Consequence for the live programme

The independently replayed odd-halfcube theorem closes one half of the 16 antipodal-transversal codes. The star-fan theorem isolates the only remaining half and now proves that this branch cannot even begin before `n=16`.

The next high-value step is the `|A|>=7` star regime: determine whether the antipode bridge plus four certificate spokes necessarily forces recursive star propagation, both coordinate orientations, or a population/edge tax linear in `|A|`. Any of those outcomes would extend the graph-level Q3 control beyond the odd-halfcube palette in the asymptotic direction that matters for the eventual problem.
