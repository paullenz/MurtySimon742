# Boundary one-match vertices are independent and force a quadratic U-slack bill

Date: 2026-09-21

Status: raw structural theorem plus score consequence inside the repeated rigid one-code interface. Conditional on the exact near-equality face `e=u-k=p`; no graph-level reachability claim.

## 1. Setup

Use `ONE_CODE_BOUNDARY_REPAIR_RESERVOIR.md`. Thus

- `Y=A_d`, `y>=2`, `m>=2`, `L=empty`;
- `e=u-k=p`, so `u=p+k`;
- `U=K disjoint_union W`, with `K` the k complementary-code vertices (`c=bar d`) and
  `W={w_1,...,w_p}`, `c(w_i)=bar d xor e_i`;
- every `w_i` is A-anticomplete.

## 2. W is independent

Take distinct `w_i,w_j in W` and suppose `w_iw_j` were an edge.

Both lie in B=N(v), so the edge is triangular through the root v. In a D2C graph, triangle-edge criticality gives an orientation with an external witness a satisfying either

`N(w_i) cap N(a)={w_j}`

or

`N(w_j) cap N(a)={w_i}`.

A witness in B is impossible because it would share root v with the B-source, so the witness must lie in A. But every vertex of W is A-anticomplete, so no A-vertex is adjacent to the required head. Contradiction.

Therefore

> **`G[W]` is independent.**                             `(2.1)`

This uses only rooted B-edge criticality and the already proved A-anticompleteness of W.

## 3. Exact degree-deficit lower bound

The root degree is

`b=|B|=2p+u=3p+k`.

Each `w_i` has

- the root v as a neighbour;
- exactly one neighbour in each tight pair, hence p matched neighbours;
- no neighbours in A;
- no neighbours in W by `(2.1)`;
- at most k neighbours in K.

Thus

`deg(w_i) <= 1+p+k`,

and with the standard rooted deficit `epsilon_i=b-deg(w_i)`, we get

> **`epsilon_i >= 2p-1`.**                              `(3.1)`

Summing over the p physically distinct boundary vertices,

> **`E_U >= sum_{i=1}^p epsilon_i >= p(2p-1)`.**         `(3.2)`

This is a quadratic bill that was invisible in the aggregate scalar rooted-Q hostile family.

Equality in `(3.1)` for one w_i requires adjacency to every vertex of K; equality in `(3.2)` requires every boundary vertex to be complete to K.

## 4. Significance

The old exact hostile scalar family had k=0 and u=p. It was already killed by the diameter obstruction. The first repaired face `e=p` is now much more expensive than the scalar tuple suggests: even though the complementary repair set K can fix diameter-two failures, the p boundary vertices remain A-anticomplete and pairwise independent, forcing almost `2p` rooted degree deficit each.

Since the scorecard satisfies `S=L_A+E_U>=E_U`, every above-threshold candidate on this face must pay at least `p(2p-1)` against the global score ceiling. The companion repair-budget note derives the resulting explicit lower bound on k.

## 5. Scope

No source-tuple capacity theorem, global selected source-coordinate uniqueness, rooted-Q inequality, or H--U private-foot argument is used. The independence proof is direct raw D2C criticality. The degree bound uses only the rooted partition and tight transversality.
