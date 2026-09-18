# False-twin private support and bipartite stability

Date: 2026-09-18

Status: internal structural theorem package for the direct-fan equality branch of the eventual / sufficiently-large second-extremal D2C programme.

## 1. Motivation

At the current rooted-transfer frontier, a large direct fan has an exact zero-surplus equality model: its leaves are false twins. The previous generic false-twin floor was

> `2e(overline{G[W]}) >= min(d,w-1)(d+2w-n)_+`.          `(old-FTF)`

The present note uses **edge criticality itself** to show that every internally active common neighbour requires its own external private witness. This strengthens `(old-FTF)` and identifies the equality model as a stability neighbourhood of a complete bipartite graph.

This is a graph-theoretic D2C lemma; it does not depend on the partial-Boolean setup.

## 2. Setup

Let `G` be diameter-2-critical. Let `D` be a false-twin class of order

`d=|D|>=2`,

so every vertex of `D` has the same open neighbourhood `W` and `D` is independent. Put

`w=|W|`,

`Z=V(G)\(D union W)`,

`z=|Z|=n-d-w`.

Let

> `W^+={x in W:d_{G[W]}(x)>0}`                            `(FT0)`

be the support of the internal edge set of `W`.

## 3. Private-support injection

### Theorem 3.1 — every internally active common neighbour has a private external witness

There exists an injection

> `phi:W^+ -> Z`                                          `(FT1)`

such that for every `x in W^+`,

> `N(phi(x)) intersect W={x}`.                            `(FT2)`

In particular,

> `|W^+|<=z`.                                              `(FT3)`

### Proof

Fix `x in W^+`. Choose `x' in W` with `xx' in E(G[W])`, and choose any `u in D`.

The edge `ux` lies in the triangle `u-x-x'`. Hence deleting `ux` does not make the endpoints `u,x` farther than two. Since `G` is diameter-2-critical, the standard triangle-edge criticality certificate gives one of the two orientations:

1. there is a vertex `y` with `N(u) intersect N(y)={x}`; or
2. there is a vertex `y` with `N(x) intersect N(y)={u}`.

The second orientation is impossible because `d>=2`. Choose `u' in D\{u}`. If `N(x) intersect N(y)={u}`, then `y` is adjacent to `u`, hence `y in N(u)=W`. But every vertex of `W` is also adjacent to `u'`, while `x` is adjacent to `u'`; therefore `u'` would be a second common neighbour of `x` and `y`.

Thus the first orientation holds. Since `N(u)=W`,

`N(y) intersect W={x}`.

The criticality witness is nonadjacent to the source `u`, so `y notin W`; it is not in `D` either, because every vertex of `D` has neighbourhood exactly `W` and `w>=2` here. Hence `y in Z`.

Set `phi(x)=y`. If `x!=x''`, then no one vertex can satisfy both

`N(y) intersect W={x}`

and

`N(y) intersect W={x''}`.

Therefore `phi` is injective. square

The theorem gives more than a cardinality bound: every internally active vertex of the common-neighbour side comes with a distinct external vertex whose entire adjacency into `W` is a single prescribed edge.

## 4. Strong missing-edge floor

All edges of `G[W]` are supported on `W^+`, so Theorem 3.1 implies

> `e(G[W]) <= binom(min(w,z),2)`.                          `(FT4)`

Equivalently:

### Corollary 4.1 — strengthened false-twin floor

> `2e(overline{G[W]})`
> ` >= (d+2w-n)_+(n-d-1)`.                               `(FT5)`

### Proof

If `z>=w`, the right side is zero. If `z<w`, then `(FT4)` gives

`e(overline{G[W]})`

`>=binom(w,2)-binom(z,2)`

`=(w-z)(w+z-1)/2`.

Now

`w-z=d+2w-n`

and

`w+z-1=n-d-1`.

square

This dominates the previous floor `(old-FTF)`, because whenever the positive part is nonzero,

`n-d-1=w+z-1>=w-1>=min(d,w-1)`.

Thus `(FT5)` should replace `(old-FTF)` at the live direct-fan frontier.

## 5. Bipartite stability interpretation

Theorem 3.1 says that at least

> `k=(d+2w-n)_+=w-z`                                      `(FT6)`

vertices of `W` are isolated in `G[W]`.

Equivalently, all internal edges on the common-neighbour side are confined to at most `z` exceptional vertices.

### Corollary 5.1 — exact bipartite collapse at `z=0`

If `Z` is empty, then `G[W]` is empty and

> `G=K_{d,w}`.                                            `(FT7)`

### Proof

`D` is independent, `N(D)=W`, and `(FT3)` gives `W^+=emptyset`; hence `W` is independent. Since `D union W=V(G)`, the only edges are all edges between `D` and `W`. square

Thus the exact false-twin equality model sits on a transparent stability axis:

- `z=0`: complete bipartite;
- small `z`: all triangles through `D` are concentrated on at most `z` exceptional vertices of `W`;
- large internal activity in `W`: necessarily many external private witnesses in `Z`.

This is the right structural interpretation for the direct branch of the eventual second-extremal problem.

## 6. Edge-count refinement using private witnesses

Let `t=|W^+|`. The injection in Theorem 3.1 chooses `t` distinct vertices of `Z`, each having exactly one neighbour in `W`. Consequently

> `e(W,Z) <= t+(z-t)w = zw-t(w-1)`.                      `(FT8)`

Also

> `e(W)<=binom(t,2)`.                                     `(FT9)`

Hence

> `m`
> `=dw+e(W)+e(W,Z)+e(Z)`
> `<=dw+binom(t,2)+zw-t(w-1)+binom(z,2)`.                `(FT10)`

This is an exact structural upper envelope conditional only on the false-twin class and the number `t` of internally active common neighbours. It is stronger than the naive complete-graph allowance on `W` and records the cost of every active common-neighbour vertex twice: it consumes one external private witness and forces that witness to have only one edge back into `W`.

No second-extremal conclusion is promoted from `(FT10)` in this note; it is intended as the next quantitative interface with the rooted residual identities.

## 7. Specialization to a zero-surplus direct fan

Return to the live rooted setup. Let `x in A` have a direct fan `D_x` of order `d>=2`, and assume the direct-fan hole surplus is zero on every leaf:

> `epsilon_x+epsilon_y=lambda+1` for every `y in D_x`.   `(ZF0)`

Then the preserved direct-fan theorem gives one common neighbourhood

> `W=N(y)` for all `y in D_x`,                            `(ZF1)`

so the leaves form a false-twin class `D=D_x`.

Since

`n=2b-lambda`,

`w=b-epsilon_y=b-lambda-1+epsilon_x`,

we have

> `z=b+1-d-epsilon_x`,                                    `(ZF2)`

and

> `d+2w-n=d-lambda-2+2epsilon_x`.                        `(ZF3)`

Therefore `(FT5)` becomes the rooted zero-surplus floor

> `2e(overline{G[W]})`
> ` >= (d-lambda-2+2epsilon_x)_+(n-d-1)`.                `(ZF4)`

This is strictly sharper than the previous false-twin floor whenever the positive part is nonzero and `z>0`.

## 8. Relation to primitive / duplicated-vertex structure

False-twin classes are precisely duplicated-vertex classes. The recent primitive-D2C literature treats deletion/duplication of such vertices as the natural reduction from general D2C graphs to primitive cores. The theorem above gives a local reason that this reduction is especially relevant here: once rooted transfer forces the direct equality model, any deviation from a pure bipartite blow-up must be supported by distinct private external vertices.

The project should therefore treat the direct branch as a **blow-up stability problem**, not as another generic Boolean-code optimization.

## 9. Scope and negative control

- Theorem 3.1 uses only the standard triangle-edge criticality certificate and the definition of a false-twin class.
- The result is valid for every D2C graph, not only the near-full branch.
- The specialization `(ZF4)` applies only to the exact zero-surplus direct-fan equality model. Bounded-surplus direct fans still require a stability extension.
- The order-12, size-32 `X_3` control is not excluded: its canonical rooted transfer does not force a positive direct fan.
- No all-order or eventual second-extremal theorem is asserted.

## 10. Next structural step

There are now two coherent continuations.

1. Extend Theorem 3.1 from exact false twins to a bounded-hole direct fan by showing that all but a controlled exceptional set of internally active common-neighbour vertices still require distinct private witnesses.
2. Feed `(FT10)` into the rooted identities `Q=p(p+u-1)+q`, `delta+Q=L_A+f`, and `delta=r-f` to quantify how close a large direct fan can remain to the complete-bipartite extremal family while the graph is still triangle-containing.

Both continuations preserve the desired separation between the direct blow-up branch and the A/U complementary-pair branch.
