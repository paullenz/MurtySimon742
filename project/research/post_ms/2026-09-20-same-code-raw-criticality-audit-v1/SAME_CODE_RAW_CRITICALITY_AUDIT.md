# Raw-criticality audit of same-code certification and ordered source-witness injection

Date: 2026-09-20

Status: **independent hand re-derivation inside the current rooted near-full setup**. This note was created because the 20 September daily adversarial audit made the full coded-layer same-code criticality theorem and ordered `(source,witness)` injectivity a mandatory upstream gate before further all-R deductions. It does not assert realizability of the rigid complete-cut branch.

## 1. Audit reconciliation

The binding daily audit is `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

This audit keeps unchanged:

- `X_3` as the mandatory 12-vertex / 32-edge hostile control;
- the repaired meanings of P1 and P2;
- the zero-positive-fixture caveat for rigid complete Hall cuts with `x>=3`;
- exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)`;
- the rule that finite parameter scans are diagnostics, not graph counts.

The purpose here is narrower: re-prove, without importing the 18 September coded-layer theorem, exactly the raw D2C statement used by all-R Units VI, XIII and XIV.

## 2. Raw triangle-edge criticality

Let `G` be diameter-2-critical and let `xy` be an edge lying in a triangle. Then there is an orientation of `xy`, say source `s in {x,y}` and head `h` the other endpoint, and a vertex `w` such that

> `sw notin E` and `N(s) cap N(w)={h}`.                 `(RAW-SC)`

### Proof

Delete `xy`. Because `xy` lies in a triangle, `x` and `y` still have distance two, so they are not the pair whose distance exceeds two in `G-xy`. Since `G` has diameter two, choose a pair `{r,t}` which has a path of length at most two in `G` but no such path in `G-xy`. A direct edge other than `xy` survives deletion, so the lost path has length exactly two and uses `xy`. Hence one endpoint of the lost pair is `x` or `y`, the middle vertex is the other endpoint of `xy`, and every length-two path between the lost pair must use that middle vertex. Thus, after orienting the edge from the endpoint belonging to the lost pair toward the middle vertex, the other member `w` of the lost pair is nonadjacent to the source and has that head as its unique common neighbour with the source. `square`

No code language is used in this step.

## 3. Exhaustive witness-location audit for an equal-code edge

Use the rooted near-full notation. The root is `v`; its neighbourhood consists of the `2p` vertices in the `p` tight matched fibres together with the unmatched set `U`; `A=V\N[v]`. Every vertex of `A union U` has one selected endpoint in every tight fibre and hence a Boolean code.

Let `xy` be an edge with `x,y in A union U` and `c(x)=c(y)=c`, with `p>=1`.

Because equal codes share the same selected endpoint in every tight fibre, `xy` lies in a triangle. Apply `(RAW-SC)` and write `s` for its source, `h` for its head and `w` for its witness.

### 3.1 The root cannot be the witness

If `s in U`, then `sv in E`, contradicting the required nonadjacency `sw notin E`.

If `s in A` and `h in A`, the root is not adjacent to the head, so it cannot satisfy `N(s) cap N(v)={h}`.

If `s in A` and `h in U`, then the root is adjacent to the head, but every one of the `p>=1` matched endpoints selected by the code of `s` is also a common neighbour of `s` and the root. Those vertices are distinct from `h`. Hence the common neighbourhood cannot be the singleton `{h}`.

Thus `w!=v` in every A-A, A-U, U-A and U-U orientation.

### 3.2 No tight matched endpoint can be the witness

Equal-code vertices have identical adjacency to every matched endpoint. A witness for `(RAW-SC)` must be adjacent to `h` and nonadjacent to `s`. Therefore no matched endpoint can distinguish the two endpoints in the required way.

Since the root and all matched vertices have been excluded, necessarily

> `w in A union U`.                                      `(LOC)`

### 3.3 The witness code is exactly complementary

If `c(w)` agreed with `c(s)` in any coordinate `i`, then `s` and `w` would share the selected matched endpoint in fibre `i`. That matched vertex is distinct from the head `h in A union U`, contradicting the singleton common-neighbour relation.

Therefore `w` differs from the source in every coordinate:

> `c(w)=bar c`.                                          `(COMP)`

### 3.4 A U-source cannot use a U-witness

If `s,w in U`, both are adjacent to the root `v`, giving a common neighbour distinct from the head. Hence

> `s in U  =>  w in A_bar c`.                            `(U-SOURCE)`

This checks both possible orientations for A-U and U-U edges; no orientation is silently discarded.

## 4. Re-derived full coded-layer theorem

The raw argument proves the following independently of the 18 September package.

### Theorem 4.1 — full coded-layer same-code criticality

For every same-code edge `xy` in `G[A union U]`, one can choose an orientation with source `s` and head `h` and a witness `w` such that

- `sw notin E`;
- `N(s) cap N(w)={h}`;
- `w in A union U`;
- `c(w)=bar c(s)`;
- if `s in U`, then `w in A`.

This matches the statement used downstream.

## 5. Ordered `(source,witness)` injectivity

Choose one valid orientation and witness for each same-code edge in any selected family. Map the edge to the ordered pair `(s,w)`.

A fixed ordered pair `(s,w)` has one graph-fixed common-neighbour set. If it certifies an edge, that set is the singleton `{h}`; therefore the head `h` is uniquely determined. The certified edge is then exactly `sh`.

Hence:

> **one fixed ordered `(source,witness)` pair certifies at most one selected same-code edge.** `(PAIR-INJ)`

This is graph-level injectivity. It is not a claim that a raw witness vertex is globally unique across different sources.

Consequently, for a code `c`,

- `e(G[V_c]) <= |V_c||V_bar c|`;
- `e(G[A_c]) <= |A_c||V_bar c|`;
- `e(G[U_c]) <= |U_c||A_bar c|`.

The last restriction uses `(U-SOURCE)`.

## 6. Independent slack identity behind the weighted form

For any certificate `(RAW-SC)`, the nonadjacent vertices `s,w` have exactly one common neighbour. Therefore

`d(s)+d(w)-1 <= n-2`,

so

`d(s)+d(w)<=n-1`.

In the rooted near-full notation every coded vertex has `d(q)=b-epsilon_q` and `n=2b-lambda`. Hence

> `epsilon_s+epsilon_w >= lambda+1`.                    `(SC-SLACK)`

Summing `(SC-SLACK)` over the injective ordered pairs re-derives the weighted same-code capacity inequalities. Thus the weighted theorem also rests on raw degree counting rather than a separate code assumption.

## 7. Application to the literal all-R equality pinch

In the all-R pinch, all of `X` has code `C`, `a_0` is isolated in `G[X]`, `X'=X\{a_0}` has `N=x-1` vertices, `A_bar C=empty`, and the distinguished `z in U_bar C` cannot certify an internal X-edge because `N(s) cap N(z)={b}` for every `s in X'`.

By Theorem 4.1 and `(PAIR-INJ)`, every internal X-edge therefore uses a witness in `U_bar C\{z}` and distinct internal edges mapped to a fixed source-witness pair cannot collide. The 20 September audit's use of this theorem in all-R Units VI/XIII/XIV is therefore **verified at raw-criticality level**.

The purified z-neighbours are A-anticomplete, so they cannot be witnesses for internal X-edges. Every used internal-X witness lies among the at most `d` z-nonneighbours in `U_o\{z}`. This validates the location premise of `X-d-CAP` and `X-WIT-PAY`.

## 8. New corollary I — a witness must reserve a physical head

Let a fixed used witness `w` certify `r_w` internal edges of `G[X']`. Its selected sources are distinct by `(PAIR-INJ)`. The witness is nonadjacent to every selected source but adjacent to the head of every certified edge. Since at least one head lies in `X'`, at least one vertex of `X'` cannot be one of those sources.

Therefore

> `r_w <= N-1=x-2`.                                     `(HEAD-RESERVE)`

If at most `d` physical z-nonneighbours can be used, then

> `e(X) <= d(N-1)=d(x-2)`.                              `(X-d-CAP+)`

This strictly improves the previous `e(X)<=dN` whenever `e(X)>0`.

## 9. New corollary II — used witnesses pay the a_0 and z holes as well

Let `w` be a used internal-X witness of selected load `r_w`.

It is forced to be nonadjacent to:

1. all `y` vertices of `Y`, because every Y-vertex is adjacent to every X-source and would otherwise be an extra common neighbour;
2. the `r_w` distinct selected X-sources;
3. `a_0`, because `c(w)=bar C` while every U-neighbour of `a_0` has code `d` or `C` in the equality pinch;
4. `z`, because Unit XIII already localizes all usable witnesses to z-nonneighbours.

For a U-vertex,

`d_{A union U}(w)=p+u-1-epsilon_w`.

The four located groups above give `y+r_w+2` distinct nonneighbours in `A union U`, and `a=x+y`. Hence

> `epsilon_w >= [p-x+r_w+2]_+`.                         `(X-WIT-PAY+)`

This strengthens the inherited `[p-x+r_w]_+` floor by two units before truncation.

## 10. Exact aggregate load price

Put `h=N-1=x-2` and let `e=e(X)`. If `e>0`, let `m` be the number of actually used physical internal-X witnesses. Then

> `ceil(e/h) <= m <= min(d,e)`.

For fixed `m`, minimizing the sum of `(X-WIT-PAY+)` over loads `1<=r_i<=h`, `sum r_i=e`, gives exactly

> `E_D >= P_J=0(e,m):=[e-m(x-p-2)]_+`.                  `(LOAD-PRICE-0)`

The formula is valid on both sides of `x=p+2`: if `x-p-2>=0`, each witness has that much free load; if it is negative, every used witness pays the corresponding positive baseline.

The previous aggregate bound `[e-d(x-p)_+]_+` is therefore safe but not exact in the literal equality-pinch geometry.

## 11. Audit verdict

**Passed.** The same-code witness-location theorem and ordered `(source,witness)` injectivity used by the all-R package have been independently re-derived directly from raw D2C criticality, including A-A, A-U, U-A and U-U orientations.

The re-derivation also exposes two strictly stronger consequences, `(X-d-CAP+)` and `(X-WIT-PAY+)`, which should replace the weaker `Nd` capacity and old witness-slack floor in the next local optimization.

This does **not** repair the separate zero-positive-fixture rigid-cut coverage gap. The entire all-R branch remains conditional on reaching the rigid complete-cut hypotheses.