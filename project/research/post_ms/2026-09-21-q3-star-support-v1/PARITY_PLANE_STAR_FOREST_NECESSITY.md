# Parity-plane star edges necessarily form a star forest

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

Suppose the distinct star centres are exactly one parity class of Q3, with arbitrary positive multiplicities. Then the graph induced by all star-coded A vertices is a disjoint union of stars and isolated vertices. In particular, if s is the number of physical star vertices and c_S the number of nontrivial star components, then

    e(S)=s_nonisolated-c_S <= s-1.

The star-forest condition in the explicit construction is therefore necessary, not merely a convenient sufficient hypothesis.

## Proof

Normalize the centres to the four even vertices. Same-centre star edges are impossible. Their B-codes intersect, so the deleted edge's endpoints do not form a direct witness. The sole undominated B vertex of S_c is bar(c), which is not in a second copy of S_c. A third-A certificate would require the disjoint code S_bar(c), whose odd centre is absent.

Any two distinct even centres have cube distance two. If x has code S_c and y has code S_d with c!=d, then bar(c) belongs to S_d and bar(d) belongs to S_c. Thus every cross-centre star edge is an antipode bridge for both endpoints.

Such an edge again has no direct certificate and no third-A certificate through an odd opposite-centre star. It can be critical only through an undominated B target: y must be x's unique A-neighbour whose code contains bar(c), or x must be y's unique A-neighbour whose code contains bar(d). In the first case x has star-degree one; in the second y has star-degree one. Therefore every edge of G[S] has an endpoint of degree one in G[S].

A finite simple graph in which every edge has a degree-one endpoint has no path on four vertices and no cycle. Every nontrivial connected component is a star K_1,k. This proves the theorem.

Nonstar A-neighbours containing an endpoint's antipode only make uniqueness harder and do not weaken the conclusion.

## Consequences

- The explicit `PARITY_PLANE_STAR_FOREST_FAMILY.md` realizes the only possible abstract form of the star subgraph.
- Any density optimization in the four-centre branch may replace an arbitrary star-star edge term by the linear bound e(S)<=s-1.
- At n=19, all four stars must bridge their antipodes, and the unique model has two K_2 components, agreeing with `ORDER_19_UNIQUENESS.md`.
