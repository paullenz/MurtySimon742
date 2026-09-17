# Boolean coding and an order cutoff for the zero-residual boundary

17 September 2026. Research directed by Paul Lenz; derivation and finite arithmetic audit by ChatGPT/Geeps.

**Status:** internal candidate structural theorem; hand reduction plus exact finite arithmetic. External mathematical review and novelty review remain open.

## 1. Scope

Use the canonical maximum-degree-root system. Assume

`t=0`,
`F=empty`.

The exact ledger `e(F)=r+t` then gives

`r=0`.

Thus every H-cross edge is selected and every B-source has residual degree zero.

Assume the graph is non-bipartite. Since A is independent and the root has no A-neighbours, non-bipartiteness in this boundary is equivalent to

`Q=e(G[B])>0`.

Let `A={a_1,...,a_a}` and encode every `u in B` by

`c(u) in {0,1}^a`,
`c_i(u)=1 iff u a_i in E(G)`.

## 2. Every B-edge changes exactly one coordinate

Take an edge `uw` of `G[B]`. In H this is a missing B-pair, so the canonical construction chooses exactly one selected representative. Because `r=0`, that representative is some H-cross edge, say

`u a_i -> w`.

In G this says

`u a_i` is a non-edge,
`u w` and `a_i w` are edges,

so

`c_i(u)=0`, `c_i(w)=1`.                                (2.1)

We claim all other coordinates agree. If for some `j!=i` one also had

`c_j(u)=0`, `c_j(w)=1`,

then the H-cross edge `u a_j` exists. Since `r=0`, it too is selected, and its unique B-exception must be w (equivalently in G, u and a_j have w as a common neighbour). It would therefore represent the same missing unordered B-pair `{u,w}`, impossible because the canonical system selects exactly one representative per missing unordered B-pair.

The opposite discrepancy

`c_j(u)=1`, `c_j(w)=0`

would make `w a_j` a selected H-cross edge representing the same pair in the opposite orientation, equally impossible.

Hence

> every edge of `G[B]` joins two codewords at Hamming distance exactly one.  (2.2)

Orient each such edge from the 0-endpoint to the 1-endpoint in its unique changed coordinate, and call that coordinate the edge colour.

## 3. Every zero coordinate has exactly one outgoing edge

Fix `u in B` and a coordinate i with `c_i(u)=0`. Then `u a_i` is an H-cross edge. Since `r=0`, it is selected, say

`u a_i -> w`.

By (2.2), `uw` is an i-coloured B-edge directed from u to w. Thus every zero coordinate supplies at least one outgoing edge.

It supplies at most one. If u had two i-coloured outgoing edges to w and w', then both missing B-pairs would have to be represented by the same selected cross edge `u a_i`, impossible.

Therefore:

> for every u and every zero coordinate i of c(u), there is exactly one outgoing i-edge.  (3.1)

There are no other B-edges by (2.2).

Consequences:

- the outdegree of u is exactly the number `z(u)` of zero coordinates of c(u);
- directed edges strictly increase Hamming weight;
- if a code occurs, every coordinatewise supercode occurs somewhere: repeatedly follow the unique outgoing edges for chosen zero coordinates.

So the occupied code set is an upset of the Boolean lattice, with possible multiplicities in each code fibre.

## 4. Indegree is the canonical incoming selected load

A directed edge `u->w` is exactly a selected missing B-pair whose exception is w. Hence its directed indegree is

`indeg(w)=p_w`.                                         (4.1)

Let

`lambda := b-a-1 = 2b-n`.

Since the root has maximum G-degree b, the canonical source inequality gives here

`p_w<=lambda`.                                         (4.2)

There is also a direct G-degree calculation. If c(w) has h ones, then w has

- one root neighbour;
- h neighbours in A;
- `a-h` outgoing B-edges;
- `p_w` incoming B-edges.

Thus

`d_G(w)=1+h+(a-h)+p_w=a+1+p_w<=b`,

which is (4.2).

Because `Q=sum p_w>0`, we necessarily have

`lambda>=1`.                                           (4.3)

## 5. Factorial path lemma

Let u have z zero coordinates. Choose any ordering of those z coordinates and follow, in that order, the unique outgoing edge of the chosen colour. At every step that coordinate changes from 0 to 1 and never changes again.

Every permutation therefore gives a directed path of length z from u to the all-ones fibre. Distinct permutations give distinct colour sequences, hence distinct directed paths. Thus u generates

`z!` directed paths of length z.                        (5.1)

Every vertex has total directed indegree at most lambda. Consequently, a fixed endpoint can be the endpoint of at most

`lambda^z`

directed paths of length z (reverse the paths one edge at a time, with at most lambda choices at each step).

There are at most b possible endpoints. Therefore

> `z! <= b lambda^z`.                                  (5.2)

This is the basic expansion obstruction.

## 6. Root criticality forces a vertex with at least a/2 zeros

Because `Q>0`, some vertex u has at least one zero coordinate, hence positive B-outdegree.

Consider the D2C-critical root edge `ru`.

After deleting `ru`, the pair `(r,u)` is still at distance 2 through any B-neighbour of u. A pair `(r,x)` with x in B is still adjacent. The only other way a length-at-most-2 path can use `ru` with r as an endpoint is a path

`r-u-a_i`.

But no A-vertex can have degree one in the present non-bipartite D2C graph: if some a_i had unique neighbour u, diameter 2 would force u to be universal, and a D2C graph with a universal vertex can have no edge away from u (deleting such an edge would leave diameter at most 2), so it would be a star, contrary to Q>0. Hence every `a_i` has another B-neighbour, and deleting `ru` cannot make `(r,a_i)` exceed distance 2.

Therefore criticality of `ru` supplies a B-vertex w such that, before deletion,

`N_G(u) intersect N_G(w)={r}`.                          (6.1)

In particular u and w have no common A-neighbour, so their code supports are disjoint.

If u has z zero coordinates, its support has size `a-z`. Disjointness implies the support of w has size at most z, so w has at least `a-z` zero coordinates. Hence

`max(z(u),z(w)) >= ceil(a/2)`.                         (6.2)

Combining (6.2) with (5.2), there exists an integer

`z in [ceil(a/2),a]`

such that

> `z! <= b lambda^z`.                                  (6.3)

## 7. Add second-extremal density

In this exact boundary,

`b=a+1+lambda`,
`n=a+b+1=2a+2+lambda`,
`m=b(a+1)`.

Assume

`m >= M(n):=floor((n-1)^2/4)+1`.                       (7.1)

The unfloored comparison is

`4m-(n-1)^2 = 4a-lambda^2+2lambda+3`.                 (7.2)

Since `M(n)>(n-1)^2/4`, (7.1) implies the right side of (7.2) is positive. Therefore

`(lambda-1)^2 < 4a+4`.

For `a>=4` this gives the convenient coarse bound

`lambda <= 3 sqrt(a)`.                                (7.3)

## 8. Hand cutoff at a=1296

Use the standard integral lower bound

`log(z!) >= integral_1^z log x dx = z log z-z+1`,

so in particular

`z! >= (z/e)^z`.                                       (8.1)

Using `e<3`, (6.2), and (7.3), when `a>=1296` we have

`z/(e lambda) > z/(3 lambda)`
`             >= (a/2)/(9 sqrt(a))`
`             = sqrt(a)/18`
`             >= 2`.

Thus (8.1) gives

`z!/lambda^z > 2^z >= 2^(a/2)`.                       (8.2)

On the other hand `b=a+1+lambda<=a+1+3sqrt(a)<=2a` for this range, while `2^(a/2)>2a`. This contradicts (6.3).

Therefore any graph in scope must have

`a<1296`.                                              (8.3)

## 9. Exact finite arithmetic and the order-294 cutoff

`check_zero_residual_cutoff.py` exhausts the finite integer range `1<=a<1296`.

For every integer lambda satisfying the exact density inequality (7.1), it asks whether any

`z in [ceil(a/2),a]`

can satisfy (6.3). This is pure integer arithmetic using exact factorials. The ratio

`f(z)=z!/lambda^z`

changes monotonically on either side of z approximately lambda, so it suffices to test the interval endpoints and the one/two integers around lambda; the checker retains that argument explicitly.

The largest a and the largest resulting n surviving these **necessary arithmetic conditions** are both attained at

`a=134`,
`lambda=24`,
`z=67`,
`b=159`,
`n=294`.

No graph realization at these parameters is asserted.

Therefore:

> **Zero-residual boundary theorem.** If a non-bipartite D2C graph in the canonical maximum-degree-root system satisfies `t=0`, `F=empty` (hence `r=0`) and `m>=floor((n-1)^2/4)+1`, then `n<=294`.

The theorem is hand-reduced to a finite exact arithmetic check; external review remains open.

## 10. Relation to the hypercube-face family

The k=3 graph `X_3` has

`a=3`, `b=8`, `lambda=4`, `n=12`,

and lies exactly in this boundary. Its cube codes realize every Boolean code once, with each directed coordinate edge present exactly once.

For `X_k`, k>=4, the same Boolean mechanism remains D2C, but the graph falls below M(n). The order-294 theorem is therefore a generalization of the observed self-dilution of that explicit family: **the entire exact residual-zero mechanism is finite at second-extremal density**, whether or not it is literally the hypercube family.

## 11. Next structural layer

The eventual problem now moves to perturbations:

- small positive `r`;
- nonempty F;
- `delta=r-e(F)` near the second-extremal threshold.

The natural target is a stability version of Sections 2–6: most cross nonedges should still define coordinate-like labels, while residual incidences and F-edges pay for collisions or broken coordinates. The existing Hall/endpoint machinery is designed to measure precisely those exceptional incidences.
