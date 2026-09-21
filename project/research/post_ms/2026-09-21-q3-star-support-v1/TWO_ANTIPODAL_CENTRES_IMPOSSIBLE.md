# No Q3-transversal D2C graph has star support in one antipodal centre pair

Date: 21 September 2026. Status: internally derived, pending independent external review.

## Theorem

Let G be a finite simple diameter-two-critical graph, v a vertex, B=N(v) inducing Q3, and A=V(G) minus (B union {v}). Assume every H_x=N(x) intersect B, x in A, is an antipodal transversal of Q3. If at least one star code occurs, its set of centres cannot be contained in {c, c-bar} for any c. Coordinate and parity multiplicities are unrestricted.

Thus the previous minimal two-opposite-star-class density bound is strengthened to nonexistence of that entire star-support branch. This is not a theorem about arbitrary Q3 codes, other roots, or the eventual D2C problem.

## Notation and raw certificate facts

Translate the cube so c=000 and c-bar=111. Its 16 transversals are the six coordinate faces C_i^epsilon, the two parity classes P_epsilon, and the eight closed stars S_c=N_Q[c]. Only S_0 and S_7 may occur in this theorem. P_0 has even Hamming weight. All arguments below are necessary conditions and allow arbitrary copies of each permitted code.

For a coordinate source x of code C_i^epsilon and s in that face, write t=s xor e_i. Deleting xs can be certified only by:

1. the pair (x,t), with no A-neighbour of x whose code contains t;
2. a nonadjacent A vertex of star code S_t, with no other common A-neighbour;
3. an adjacent A vertex of star code S_(s-bar), with the required unique intermediate.

For a parity source x of code P_epsilon and s in P_epsilon, the corresponding alternatives are:

1. direct endpoint (x,s), with no A-neighbour code containing s;
2. a nonadjacent star S_s;
3. an adjacent star S_(s-bar).

These facts follow by listing the pairs whose length-at-most-two paths use xs. B-B pairs retain v; x-v retains three other intermediates. A-target pairs require singleton code intersection; reverse B-end pairs require a code avoiding N_Q[s]. The required singleton/avoidance codes are unique. Full adjacency uniqueness is necessary in each case; discarding it only weakens the restrictions used below.

## 1. Forced coordinate and parity neighbour restrictions

For a source of type C_i^0, exactly two of its four spokes have neither star alternative available: their outside targets are the two weight-two vertices containing bit i. Every A-neighbour must avoid both targets. Among the allowed codes this leaves only

    N_A(C_i^0) has types in {C_i^0, P_1, S_0}.

Complementing gives

    N_A(C_i^1) has types in {C_i^1, P_0, S_7}.

For P_0, the three weight-two spokes lack both star alternatives. Hence its neighbours avoid all weight-two cube vertices, leaving only {P_1,S_0}. Similarly P_1 neighbours have types in {P_0,S_7}.

Adjacency is symmetric. In particular there are no coordinate-parity edges, no edges between distinct coordinate types, and the only possible coordinate-star edges are C_i^0--S_0 or C_i^1--S_7. The restrictions hold even if one of the two star types is absent, because allowing an extra star alternative could only weaken them.

## 2. Coordinate vertices are A-isolated

For an A-edge xy, every newly long pair contains x or y. From the x side there are only:

- the direct pair (x,y), requiring H_x and H_y disjoint;
- a B target undominated by H_x, contained in H_y;
- a third A target z, with H_z disjoint from H_x and yz an edge (and xz a nonedge with unique common neighbour y).

Coordinate and parity codes dominate B. A coordinate code's only disjoint transversal is its opposite face. A star S_0's only undominated vertex is 7 and its only disjoint transversal is S_7.

A same-coordinate edge cannot be certified directly or via B. A third-A certificate would require an edge between opposite coordinate types, already forbidden. It is therefore impossible.

For a C_i^0--S_0 edge, the coordinate endpoint could only use a third target of type C_i^1, which would need to be adjacent to S_0, forbidden above. The S_0 endpoint cannot use a direct certificate; its antipode 7 is absent from C_i^0; and its third-A certificate would require a C_i^0--S_7 edge, also forbidden. Thus no certificate exists. Complementation eliminates C_i^1--S_7 edges.

Every coordinate vertex is consequently isolated in G[A].

The same reasoning eliminates P_0--S_0 and P_1--S_7: a parity endpoint would need a complementary-parity target adjacent to the star, forbidden by Step 1; the star endpoint would need its opposite star adjacent to the parity vertex, also forbidden, and its antipode is not in that parity code. This additional fact is useful for the one-centre case.

## 3. Both opposite star types give a diameter contradiction

For x of type S_0, criticality of each leaf spoke x e_i requires either a nonadjacent C_i^1 vertex or an adjacent star of centre 7 xor e_i. The latter is absent, so C_i^1 occurs for every i. For S_7 the three C_i^0 types are likewise forced.

But C_i^0 and C_i^1 vertices have disjoint B-neighbourhoods and are both A-isolated. They are not adjacent, share no B neighbour, and share no A neighbour; neither is adjacent to v. Their distance exceeds two, contradiction.

## 4. A single star-centre type is also impossible

If only S_0 occurs, Steps 1–2 prohibit its coordinate and parity neighbours. An edge inside S_0 has no direct or antipode-B certificate; a third-A certificate requires S_7, which is absent. Hence each star vertex has no A neighbours at all. It cannot reach the undominated cube antipode 7 in two steps. The S_7-only case is symmetric.

This completes the theorem. The star-free branch remains the previously classified odd-halfcube family.

## Audit boundary and next action

The proof uses the complete raw A-B certificate classification, not the conditional rigid/Hall machinery. A separate finite type replay should reconstruct the restrictions directly from cube bitsets. Next investigate two nonopposite centres and whether their coordinate/parity restrictions also force an absent bridge. Preserve the older face bounds as historical conditional consequences; do not delete them.
