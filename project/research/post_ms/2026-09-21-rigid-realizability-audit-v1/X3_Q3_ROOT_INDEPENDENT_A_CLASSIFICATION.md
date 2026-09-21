# Classification of the Q3-root / independent-A branch

Date: 2026-09-21

## Statement

Let `G` be diameter-2-critical. Fix a root `v` such that `B=N(v)` induces the 3-cube `Q3`, and put `A=V(G)\(B∪{v})`. Assume `A` is independent.

Then, after identifying `B` with `F_2^3`, every `x∈A` has a B-neighbourhood of the form

`N_B(x)={s∈F_2^3 : l_x·s=epsilon_x}`

where `l_x` is one of the four odd-weight nonzero vectors

`100,010,001,111`.

For each of the four linear forms, at most one of its two affine sides can occur. Each of the three coordinate forms `100,010,001` must occur at least once. The parity form `111` is optional. Consequently `G` is exactly a member of the explicit A-layer blow-up family of `X3_A_LAYER_BLOWUP_FAMILY.md`.

In particular, if `a=|A|`, then

`n=9+a`, `m=4n-16`, `a>=3`,

and hence

`M(n)-m = floor((n-9)^2/4)-3`.

Therefore this whole branch exceeds `M(n)` only at `n=12`, where `a=3` and the graph is `X3` up to cube automorphism. At `n=13` it has `m=M(n)-1`; for all larger n the deficit grows quadratically.

## Proof

Write the antipode of `s∈B` as `bar s`.

### 1. Diameter two forces every A-neighbourhood to dominate Q3

Fix `x∈A` and write `H=N_B(x)`. Because `A` is independent and `v` has no neighbours in `A`, if `t∈B\H`, every two-path from `x` to `t` must have its middle vertex in `B`. Therefore `H` dominates `Q3`.

In particular `|H|>=2`; a singleton cannot dominate Q3.

### 2. Root-edge criticality forces antipodal-free A-neighbourhoods

Fix `s∈B` and delete the root edge `vs`.

The only possible new distance-greater-than-two pair involving the root and an A-vertex would be `(v,x)` with `N_B(x)={s}`. Step 1 rules this out.

Among B-vertices, an adjacent vertex remains adjacent to `s`; every distance-two cube vertex already has a cube common neighbour with `s`; and the antipode `bar s` is the unique B-vertex nonadjacent to `s` with no cube common neighbour with `s`. Pairs involving an A-vertex but not the root cannot use `vs` in a length-two path, because A has no root neighbours.

Hence criticality of `vs` forces `(s,bar s)` to lose its unique length-two path through `v`. Thus `s` and `bar s` have no common A-neighbour.

Equivalently, every `H=N_B(x)` contains at most one vertex from each antipodal pair, so `|H|<=4`.

Combining Steps 1 and 2, each A-neighbourhood is an antipodal-free dominating set of `Q3`.

### 3. Antipodal-free dominating sets of Q3 are exactly the eight odd affine halfcubes

No antipodal-free set of size at most three dominates `Q3`.

- Size one is immediate.
- A dominating 2-set in `Q3` must be an antipodal pair: only two disjoint closed neighbourhoods of size four can cover all eight cube vertices, and this occurs exactly for antipodes.
- For size three, translate one chosen vertex to `000`. Antipodal-freeness excludes `111`. To dominate `111`, one of the other two chosen vertices must have Hamming weight two; after permuting coordinates take it to be `110`, which excludes its antipode `001`. The third chosen vertex is then either a weight-one vertex among `100,010` (up to the symmetry fixing `110`) or a weight-two vertex among `101,011`; in either case one of `011,101` respectively is left undominated. Hence size three is impossible.

Therefore `|H|=4`. Antipodal-freeness then says H contains exactly one vertex from each antipodal pair.

Orient so that `000∉H`; then `111∈H`. Put

`a=1_H(100)`, `b=1_H(010)`, `c=1_H(001)`.

Antipodal transversality determines

`1_H(011)=1-a`, `1_H(101)=1-b`, `1_H(110)=1-c`.

Domination of `000` requires `(a,b,c)` to have positive weight. If `(a,b,c)` has weight two, say `a=b=1,c=0`, then `001` is outside H and all three of its cube neighbours `000,101,011` are outside H, contradiction. Thus the weight is one or three. Conversely, for odd weight,

`1_H(s)=a s_1 xor b s_2 xor c s_3 xor 1`

(up to the chosen orientation), so H is an affine halfcube defined by an odd-weight linear form. The four possible directions are exactly `100,010,001,111`, each with two sides.

### 4. A-A diameter forbids opposite sides of one direction

Two opposite affine sides of the same linear form are disjoint. Since `A` is independent and the root is not adjacent to A, two A-vertices carrying opposite sides would have no common neighbour and hence distance greater than two. Therefore at most one orientation of each of the four directions can occur.

Distinct directions have affine-halfcube intersection of size two, so no further diameter-two restriction is needed.

### 5. Criticality of cube edges forces all three coordinate directions

Let `st` be a cube edge flipping coordinate j. Deleting `st` cannot hurt any B-B distance because the root remains a common neighbour; it cannot hurt any A-A distance because their length-two paths use common B-neighbours and no cube edge; and it cannot hurt a root-A distance because those paths use root-B and B-A edges. Hence a criticality witness for `st` must be an A-B nonedge whose unique B-middle vertex is one endpoint of `st`.

For an A-vertex with halfcube `H={z:l·z=epsilon}`, if `t∉H`, the number of cube neighbours of `t` lying in H is exactly the Hamming weight `wt(l)`. Thus `st` can be the unique H-entry edge at `t` iff `wt(l)=1` and the unique support coordinate of l is j.

Therefore every cube direction j requires at least one A-vertex of coordinate type `e_j`. The parity direction `111` has weight three and cannot certify a cube edge, so it is optional.

This proves the classification.

## Exact extremal consequence

The classification gives exactly the construction of `X3_A_LAYER_BLOWUP_FAMILY.md`: the three coordinate types occur with positive multiplicity, the parity type with arbitrary nonnegative multiplicity, and A has no internal edges. Thus

`m=8+12+4a=20+4a=4n-16`.

With `M(n)=floor((n-1)^2/4)+1`,

`M(n)-m = floor((n-1)^2/4)-4n+17 = floor((n-9)^2/4)-3`.

Since `a=n-9>=3`, the only negative value is at `a=3` (`n=12`), where the graph is precisely the three-coordinate instance and hence isomorphic to X3. At `a=4` (`n=13`) the gap is one.

## Hostile-replay correction incorporated

An initial proof draft stated the root-edge argument before excluding the alternative certificate `(v,x)` with `N_B(x)={s}`. That ordering was too quick: deleting `vs` could indeed make `d(v,x)>2` if `x` had the singleton B-neighbourhood `{s}`. The diameter-two domination lemma above rules such a vertex out, so the theorem survives after putting domination first. This correction is recorded explicitly rather than silently erased.

## Scope

This theorem is graph-level and uses only D2C criticality, the rooted condition `G[B]=Q3`, and `A` independent. It does not use the rigid complete Hall-cut interface, source-tuple capacity, the H-U private-foot machinery, or the conditional 0.53 wedge. It therefore gives a clean structural explanation of the mandatory order-12 exception inside its natural rooted Q3 branch.
