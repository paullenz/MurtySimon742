# Boolean antipode-fan payment in the near-full branch

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal hand theorem. External mathematical and novelty review remain open. The finite atlas replay below is regression evidence only.

## 1. Purpose

The earlier antipode-branching inequality

`3 sum eta(yz) >= d(d-1)`

is valid for an arbitrary rooted antipode fan, but it does not use the partial Boolean structure supplied by even one tight antipode pair. In the near-full branch that omission costs a factor.

Once at least one tight pair is present, all unmatched antipode partners of a fixed unmatched centre have the same partial Boolean code. Hence they share a matched `B`-neighbour. That shared neighbour prevents a partner from serving as the private arm certifying criticality of an edge between two other partners. Repricing those partner-partner edges gives a stronger coefficient and an extra stability term.

The result materially improves the universal lower bound on unmatched maximum-degree slack.

## 2. Setup

Let `G` be diameter-2-critical, let `v` be a maximum-degree root, and put

`B=N(v)`.

Suppose the tight antipodes in `B` include `p>=1` disjoint pairs

`P_i={u_i,w_i}`.

Let `P` be their union and `U=B\P`. Tightness means

`N(u_i) intersect N(w_i)={v}`

and there is no vertex outside `{v,u_i,w_i}` adjacent to neither endpoint. Consequently every vertex outside `{v,u_i,w_i}` is adjacent to exactly one endpoint of `P_i`. Thus every vertex in `A union U` has a partial Boolean code in `{0,1}^p`.

For an antipode pair `xy` relative to `v`, write

`eta(xy)=# {z notin {v,x,y}: z not~x and z not~y}`.

Let `J_U` be the graph on `U` whose edges are the U-U antipode pairs.

Fix `z in U` and let

`Y=N_{J_U}(z)`, `d=|Y|`.

For each `y in Y`, put `eta_y=eta(yz)` and let

`H_y={x notin {v,y,z}: x not~y and x not~z}`.

Then `|H_y|=eta_y`.

Because `y` and `z` are antipodes, their partial Boolean codes are complementary. Therefore every member of `Y` has the same code `bar c(z)`. In particular, since `p>=1`, any two vertices of `Y` share at least one common matched neighbour in `P`.

## 3. Edge-criticality prices partner-partner edges to external holes

Let `yy'` be an edge of `G[Y]`. The endpoints share a matched neighbour in `P`, so after deleting `yy'` they remain at distance two. Hence `(y,y')` itself cannot certify criticality of the edge.

Since `G` is D2C, deleting `yy'` must destroy every length-at-most-two path for some pair using that edge. After orienting the edge if necessary, there is therefore a vertex

`x in N(y)\{y'}`

such that

`x not~ y'`

and

`N(x) intersect N(y')={y}`.                                      (3.1)

The vertex `x` is not adjacent to `z`: otherwise `x` would be a common neighbour of the antipodes `z,y` distinct from `v`. Thus

`x in H_{y'}`.                                                     (3.2)

Moreover `x` cannot belong to `Y`. Every member of `Y` has the same partial Boolean code as `y'`, hence shares at least one matched neighbour with `y'`, contradicting (3.1). Therefore

`x in H_{y'}\Y`.                                                   (3.3)

Charge the edge `yy'` to the ordered pair `(y',x)`.

For a fixed ordered pair `(y',x)`, condition (3.1) determines `y` uniquely: it is the unique common neighbour of `x` and `y'`. Hence the charge is injective.

Let

`r_y=|H_y intersect Y|`.

The available charges targeted at `y` number at most `eta_y-r_y`, so

`e(G[Y]) <= sum_{y in Y}(eta_y-r_y)`.                              (3.4)

But an unordered pair of vertices of `Y` is a nonedge exactly when each endpoint lies in the other endpoint's hole set. Therefore

`sum_y r_y = 2 bar e(G[Y])`.                                      (3.5)

Using

`e(G[Y])=binom(d,2)-bar e(G[Y])`

in (3.4) gives the main inequality.

> **BOOLEAN ANTIPODE-FAN PAYMENT THEOREM.**
>
> If `p>=1`, then for every unmatched centre `z in U`,
>
> `sum_{y in N_{J_U}(z)} eta(yz)`
>
> `    >= binom(d_{J_U}(z),2) + bar e(G[N_{J_U}(z)]).`             (BAF)
>
> In particular,
>
> `2 sum_y eta(yz) >= d(d-1)`.                                    (BAF0)

The extra nonedge term is useful stability information, not merely an artefact of the proof.

## 4. Global error inequality

Sum (BAF) over all centres of `J_U`. Each antipode error `eta(e)` is counted at both ends. Hence

> `2 sum_{e in E(J_U)} eta(e)`
>
> ` >= sum_{z in U} binom(d_{J_U}(z),2)`
>
> `    + sum_{z in U} bar e(G[N_{J_U}(z)]).`                       (4.1)

Equivalently,

> `4 sum_{e in E(J_U)} eta(e)`
>
> ` >= sum_z d_{J_U}(z)(d_{J_U}(z)-1)`
>
> `    + 2 sum_z bar e(G[N_{J_U}(z)]).`                            (4.2)

The predecessor general antipode-branching theorem had coefficient `6` in front of the total error and no neighbourhood-nonedge term. Thus the partial Boolean fibre structure improves the branching price by a factor `3/2` on the U-U antipode graph.

## 5. Zero-slack unmatched vertices: improved hub capacity

Retain the near-full notation

`b=2p+u`, `lambda=2b-n`, `epsilon_x=b-d_G(x)`,

and let

`Z={y in U: epsilon_y=0}`.

A zero-slack unmatched vertex cannot have a matched antipode. Indeed the preserved matched-antipode identity is

`eta(yq)=epsilon_y-epsilon_{q'}`,

where `q'` is the tight mate of the matched endpoint `q`. With `epsilon_y=0`, the right side is nonpositive; equality zero would make `yq` tight, contrary to `y in U`, while an errorful antipode needs positive eta. Therefore every `y in Z` has a U-U antipode.

Assign each `y in Z` to one such hub `z in U`. If a fixed hub receives `d_z` assigned zero-slack partners, then all corresponding errors equal

`eta(yz)=epsilon_z-lambda-1=:η_z`.

They are errorful, so `η_z>=1`. Applying (BAF0) to this subset of partners gives

`d_z η_z >= binom(d_z,2)`,

hence

> `d_z <= 2η_z+1 = 2(epsilon_z-lambda-1)+1.`                     (5.1)

This replaces the earlier ABE capacity

`d_z <= 3(epsilon_z-lambda-1)+1`.

### Saturation normal form

If equality holds in (5.1), so `d_z=2η_z+1`, then equality must hold at every step of the proof of (BAF):

1. `G[Y]` is complete; there are no internal holes among the assigned partners.
2. Every hole incidence is external to `Y` and is used by exactly one critical partner-partner edge.
3. Orient each edge `yy'` toward the endpoint whose hole certifies its criticality. Every vertex has indegree exactly `η_z`; hence the orientation is a regular tournament on `2η_z+1` vertices.
4. Every used hole has partial Boolean code `c(z)`. Indeed it must avoid all matched neighbours of its target, whose code is `bar c(z)`.

Thus extremal fan capacity is highly rigid. In the first case `η_z=1`, a saturated hub has exactly three zero-slack partners; they form a triangle, and their three external hole incidences support a directed 3-cycle of criticality witnesses. The abstract `K_{1,4}` obstruction left open by the old ABE inequality is impossible once a tight Boolean fibre is present.

## 6. Improved universal unmatched-slack floors

Let

`E_U=sum_{y in U} epsilon_y`.

Assume the dense comparison regime `m>M(n)`, for which the preserved degree arithmetic gives `lambda>=-1`.

### 6.1 Odd half-balance: `lambda=-1`

Let `H` be the set of positive-slack hubs used by the zero vertices and put

`S_H=sum_{z in H} epsilon_z`.

From (5.1),

`|Z| <= 2S_H+|H|`.

Every used hub has positive integer slack, so `|H|<=S_H`. Every remaining positive-slack unmatched vertex costs at least one further unit of `E_U`. Therefore

`u <= 4 E_U`.

Hence

> **if `lambda=-1`, then `E_U >= ceil(u/4)`.**                    (6.1)

The predecessor coefficient was `ceil(u/5)`.

### 6.2 `lambda>=0`

If `Z` is empty then trivially `E_U>=u`.

If `Z` is nonempty, let `H` again be the used hubs and let `R_0` be the positive-slack unmatched vertices not used as hubs. Equation (5.1) gives

`|Z| <= 2S_H-(2lambda+1)|H|`.

Using `|R_0|<=sum_{R_0} epsilon`,

`u=|Z|+|H|+|R_0|`

` <= 2E_U-2lambda|H|`

` <= 2E_U-2lambda`.

Thus

> **if `lambda>=0` and `Z` is nonempty,**
>
> `E_U >= ceil(u/2)+lambda`.                                      (6.2)

Combining the zero-free and zero-present cases gives the universal form

> `E_U >= min(u, ceil(u/2)+lambda)` for `lambda>=0`.               (6.3)

At exact half degree (`lambda=0`) this improves the previous coarse floor from `ceil(u/3)` to

> `E_U >= ceil(u/2)`.                                              (6.4)

## 7. Equality/stability information for the new floors

The proof records the configurations that can make the new constants sharp.

- At `lambda=-1`, equality in the coarse ratio `u=4E_U` can occur only if every positive-slack unmatched vertex is a used hub of slack one, each hub receives exactly three zero-slack partners, and each such three-partner fan has the saturated triangle/regular-tournament normal form from Section 5.
- At `lambda=0`, equality `u=2E_U` with zero-slack unmatched vertices requires every positive-slack unmatched vertex to be a used hub, and each hub with slack `e` to receive exactly `2e-1` zero-slack partners. Each partner set is a clique carrying the corresponding regular tournament witness design.

These are not asserted to be realizable D2C graphs. They identify the only local structures that can defeat a stronger purely fan-counting inequality and therefore give a concrete next target for the row/Hall machinery.

## 8. Consequence for an above-threshold `lambda=-1` candidate

The exact global slack criterion gives, above `M(n)`,

`E_U+L_A <= 2p+u-4`

when `lambda=-1`, where

`L_A=sum_{x in A} epsilon_x`

and `a=2p+u`.

By (6.1),

`L_A <= a-4-ceil(u/4)`.

Since every positive-slack A-vertex contributes at least one unit to `L_A`, any such candidate must contain at least

> `4+ceil(u/4)` maximum-degree vertices in `A`.                    (8.1)

This does not close the `lambda=-1` branch, but it converts low total slack into a growing population of maximum-degree A-vertices. That is a useful interface with the maximum-triangle-root and A-edge criticality machinery.

## 9. Finite regression

`check_boolean_antipode_fan_payment.py` independently scans every D2C isomorphism class in the NetworkX graph atlas through order seven and every maximum-degree root. It constructs all tight B-antipodes, removes their endpoints to obtain `U`, and checks (BAF) at every U-antipode fan whenever at least one tight pair is present.

Recorded counts:

- 50 maximum-degree root instances;
- 9 root instances with at least one tight pair;
- 3 unmatched antipode fan centres;
- 1 branching fan centre;
- 4 fan-partner incidences in total;
- minimum integer margin in (BAF): `0`;
- zero violations of the complementary-code fibre property;
- zero violations of (BAF).

The one branching atlas instance has `d=2`, total error `2`, and one nonedge among its two partners, so it attains

`2 = binom(2,2)+1`.

This is a small regression only. The proof in Sections 2–6 is the mathematical basis.

## 10. Strategic consequence

The old abstract `K_{1,4}` error star is no longer the correct obstruction in the near-full Boolean branch. The cheapest remaining zero-slack fan is the much more rigid saturated `K_{1,3}` pattern at `lambda=-1`, and at `lambda=0` every saturated fan carries an odd clique plus a regular-tournament system of external complementary-code holes.

The next high-value move is therefore not another generic antipode-degree inequality. It is to combine these saturation normal forms with the row-singleton/beta-pool machinery. In particular, the external holes forced at equality all lie in the hub's partial-code class, while the zero-slack partners occupy the complementary class; this is exactly the two-class geometry in which the preserved disjoint beta-pool and per-source Hall capacities are strongest.

No eventual second-extremal theorem is claimed here. The published 12-vertex/32-edge control remains untouched: it lies in the full-tight `k=4,r=0` mechanism, not this unmatched branch.