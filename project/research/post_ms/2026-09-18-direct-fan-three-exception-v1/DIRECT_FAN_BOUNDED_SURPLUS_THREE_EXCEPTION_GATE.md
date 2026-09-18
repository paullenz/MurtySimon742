# Bounded-surplus direct fans: private support and the three-exception gate

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large second-extremal diameter-2-critical programme.

The active target remains

`M(n)=floor((n-1)^2/4)+1`.

The published 2024 order-12, size-32 graph `X_3` remains a mandatory negative control. Its canonical rooted analysis has no internal A-edge mass (`f=0`), hence no positive direct fan, so none of the hypotheses below is triggered there.

No all-order or eventual second-extremal theorem is claimed.

## 1. Rooted direct-fan setup

Work in the live rooted partial-Boolean branch. Fix an A-vertex `x` and let

`D=D_x={y in A: xy is direct}`,

where direct means

`N(x) intersect N(y)=empty`.

Put

`d=|D|>=2`.

The preserved direct-fan theorem gives:

- `D` is independent;
- all leaves have the complementary Boolean code;
- with

  `W=(V(G)\{v})\N(x)`,

  every leaf satisfies `N(y) subseteq W`;
- defining

  `H_y=W\N(y)`,

  one has

  `h_y:=|H_y|=epsilon_x+epsilon_y-(lambda+1)>=0`.

Write the total direct-fan hole surplus as

> `eta=sum_{y in D} h_y`.                                  `(BH0)`

Also put

`w=|W|`,

`Z=V(G)\(D union W)`,

`z=|Z|`.

The rooted identities give

> `w=a+epsilon_x`,                                         `(BH1)`
>
> `z=b+1-d-epsilon_x`.                                    `(BH2)`

Since `D subseteq A\{x}`, one has `d<=a-1`, hence

> `w>=d+1`.                                                `(BH3)`

Finally

> `e(D,W)=dw-eta`,                                        `(BH4)`

and there are no edges inside `D` or from `D` to `Z`.

The exact false-twin model from the previous checkpoint is precisely `eta=0`.

## 2. Low total surplus forces a universal leaf

If

> `eta<=d-2`,                                              `(BH5)`

then at least two leaves have `h_y=0`. In particular, choose one leaf `y_0` with

> `N(y_0)=W`.                                              `(BH6)`

This elementary observation is the key to extending the exact false-twin private-support theorem. We do not need all leaves to be twins; one universal leaf, together with the total-hole budget, is enough.

## 3. Bounded-surplus private-support injection

Let

`W^+={t in W:d_{G[W]}(t)>0}`,

`t=|W^+|`.

### Theorem 3.1 — direct-fan private support below one total hole per leaf

Assume `(BH5)`. Then there is an injection

> `phi:W^+ -> Z`                                           `(BH7)`

such that for every `t in W^+`,

> `N(phi(t)) intersect W={t}`.                            `(BH8)`

Consequently

> `t<=z`.                                                   `(BH9)`

### Proof

Choose `y_0` as in `(BH6)`. Fix `t in W^+` and choose `t' in W` with `tt' in E(G[W])`. Since `y_0` is adjacent to every vertex of `W`, the edge `y_0t` lies in the triangle `y_0-t-t'`.

The standard triangle-edge criticality certificate gives one of two orientations.

**Forward orientation.** There is a vertex `q` with

`N(y_0) intersect N(q)={t}`.

Since `N(y_0)=W`, this is exactly `(BH8)`.

**Reverse orientation.** There is a vertex `q` with

`N(t) intersect N(q)={y_0}`.

Because `q` is adjacent to `y_0`, `(BH6)` gives `q in W`. For every other leaf `y in D\{y_0}`, if both `t` and `q` were outside `H_y`, then `y` would be a second common neighbour of `t` and `q`, contradicting the singleton common neighbourhood. Hence for every one of the `d-1` other leaves, at least one of `t,q` belongs to `H_y`. This requires at least `d-1` hole incidences, contradicting `eta<=d-2`.

Thus the reverse orientation is impossible, and the forward orientation holds.

It remains to place `q`. It is not in `W`. If `q` were another leaf of `D`, then

`|N(y_0) intersect N(q)|=|W\H_q|=w-h_q`.

By `(BH3)` and `h_q<=eta<=d-2`,

`w-h_q>=w-d+2>=3`,

contradicting the singleton intersection. Thus `q in Z`.

Different `t` give different witnesses, since one vertex cannot have its intersection with `W` equal to two different singletons. Hence `phi` is injective. square

### Structural interpretation

The exact false-twin theorem required every leaf to see all of `W`. Theorem 3.1 shows that this is much more robust: as long as the **total** direct-fan hole mass is at most `d-2`, every internally active vertex of `W` still requires its own external private support vertex.

Equivalently, every direct fan satisfies the dichotomy

> `eta>=d-1`,
>
> or the private-support injection `(BH7)-(BH8)` holds.     `(BH10)`

## 4. Edge envelope with bounded surplus

Under `(BH5)`, let `t=|W^+|`. The private witnesses force

> `e(W,Z)<=zw-t(w-1)`.                                    `(BH11)`

Also

> `e(G[W])<=binom(t,2)`.                                  `(BH12)`

Using `(BH4)` and `e(G[Z])<=binom(z,2)` gives

> `m<=w(n-w)+binom(z,2)-t(w-1)+binom(t,2)-eta`.           `(BH13)`

This is exactly the previous false-twin envelope, strengthened by the explicit loss `eta` from the missing D-W edges.

Let

`B_w=floor(n^2/4)-w(n-w)`.

Since

`floor(n^2/4)-M(n)=floor(n/2)-1`,

we obtain the bounded-surplus second-extremal criterion

> `B_w+eta+t(w-1)-binom(t,2)-binom(z,2)`
> ` >= floor(n/2)-1`
>
> ` ==> m<=M(n)`.                                         `(BH14)`

## 5. Zero, one, and active two/three external exceptions

Assume `(BH5)`.

### `z=0` or `z=1`

By `(BH9)`, `t<=1`, so `G[W]` is independent. Since `D` is independent, `D` has no neighbours in `Z`, and `|Z|<=1`, the graph is triangle-free.

### `z=2` and `G[W]` nonempty

Then `t=2`. The criterion `(BH14)` is weaker than the already verified exact-false-twin criterion only by the favourable additional term `eta`. For every `n>=7`,

> `B_w+2w-4>=floor(n/2)-1`,                               `(BH15)`

so

> `m<=M(n)`.                                               `(BH16)`

### `z=3` and `G[W]` nonempty

Now `2<=t<=3`. The weakest case is `t=2`, because for `t=3` one necessarily has `w>=3` and the correction is no smaller. Thus it suffices to check

`B_w+2w-6>=floor(n/2)-1`.

If `n=2h`, the difference between the left and right sides is

`(w-h+1)^2+h-6`,

which is nonnegative for `h>=6`.

If `n=2h+1`, writing `w=h+a`, the difference is

`a^2+a+h-5`,

which is nonnegative for `h>=5`.

Therefore

> `n>=11`, `z=3`, `G[W]` nonempty ==> `m<=M(n)`.          `(BH17)`

The only genuinely new case is therefore `z<=3` with `W` independent.

## 6. Independent `W`, two external vertices

Let `z=2`, `W` independent, and suppose the graph contains a triangle. Write `Z={r,s}`. Since `D` has no edges to `Z`, the triangle must be

`r-s-x-r`

for some `x in W`.

Choose the universal leaf `y_0` from `(BH6)`.

Consider the triangle edge `rx`. The reverse criticality orientation would require a vertex `q` with

`N(x) intersect N(q)={r}`.

It cannot lie in `D`, since `D` has no neighbours in `Z`; it cannot be `s`, because `s` is adjacent to `x`; and if `q in W`, then `x` and `q` have the common neighbour `y_0` in addition to `r`. Thus the reverse orientation is impossible.

Hence the forward orientation holds: some leaf `y_r in D` satisfies

`N(r) intersect N(y_r)={x}`.

Therefore every W-neighbour of `r` other than `x` is a hole of `y_r`, so

> `d_W(r)<=eta+1`.                                        `(BH18)`

Similarly

> `d_W(s)<=eta+1`.                                        `(BH19)`

Thus

`e(W,Z)<=2eta+2`,

and

> `m<=dw-eta+(2eta+2)+1=dw+eta+3`.                       `(BH20)`

Since `eta<=d-2` and `w>=d`,

`m<=dw+d+1`.

But

`floor((d+w+1)^2/4)>=d(w+1)=dw+d`,

because

`(d+w+1)^2-4d(w+1)=(w+1-d)^2>=0`.

As `n=d+w+2`, this proves

> `z=2`, `W` independent, triangle-containing ==> `m<=M(n)`. `(BH21)`

So the two-exception closure survives the whole bounded-surplus range `(BH5)`.

## 7. Independent `W`, three external vertices

Now let `z=3`, `W` independent, and put

`J=G[Z]`.

Every vertex of `W` must have a Z-neighbourhood that dominates `J`: if `w in W` is nonadjacent to `z in Z`, a common neighbour of `w,z` cannot lie in `D` or `W`, so it must lie in `Z`. Also every vertex of `Z` has at least one W-neighbour, because it must be within distance two of the universal leaf `y_0`.

We split according to `e(J)`.

### 7.1 `e(J)=0`

The graph is triangle-free.

### 7.2 `e(J)=1`

Let `ab` be the unique Z-edge and let `c` be isolated in `J`. Domination forces every vertex of `W` to be adjacent to `c`, so `d_W(c)=w`.

If there is a triangle, some `x in W` is adjacent to both `a` and `b`. Apply triangle-edge criticality to `xa`.

The reverse orientation cannot use a W-vertex because the universal leaf `y_0` would be a second common neighbour, cannot use `D`, and cannot use `b` because `b` is adjacent to `x`. The forward witness is either a D-leaf, in which case all other W-neighbours of `a` are holes of that leaf, or `c`, in which case `N(a) intersect N(c)=N_W(a)` must itself be `{x}`. In either case

> `d_W(a)<=eta+1`.                                        `(BH22)`

Similarly

> `d_W(b)<=eta+1`.                                        `(BH23)`

Hence

`e(W,Z)<=w+2eta+2`,

and therefore

> `m<=dw+w+eta+3<=dw+w+d+1`.                             `(BH24)`

As `n=d+w+3`,

`floor((d+w+2)^2/4)>=dw+w+d`,

because

`(d+w+2)^2-4(dw+w+d)=(d-w)^2+4>0`.

Thus

> `e(J)=1`, triangle-containing ==> `m<=M(n)`.             `(BH25)`

### 7.3 `e(J)=2`: the path case

Write the path as `1-0-2`, with centre `0`. For a vertex `w in W`, its Z-neighbourhood must be one of

`{0}`, `{1,2}`, `{0,1}`, `{0,2}`, `{0,1,2}`.

Let

- `A` be the number of W-vertices adjacent to both `0` and `1`;
- `B` be the number adjacent to both `0` and `2`;
- `C` be the number adjacent to both leaves `1,2` but not necessarily to the centre in the bookkeeping below, so that

  `d_W(1)=A+C`,

  `d_W(2)=B+C`;

more concretely, if the five type counts are `s,a,b,c,e` for the sets listed above, then

`A=a+e`, `B=b+e`, `C=c`,

and the number of W-Z incidences beyond the mandatory one per W-vertex is

> `E=A+B+C`.                                               `(BH26)`

If a W-vertex contributes to `A`, the edge from it to leaf `1` lies in a triangle with centre `0`. The third Z-vertex cannot certify that edge: it is nonadjacent to leaf `1`, and in the all-three type its common neighbourhood with leaf `1` also contains the centre. A W-witness is excluded by the universal leaf `y_0`. Hence the forward witness lies in `D` and its hole set contains every other W-neighbour of leaf `1`.

Different triangle W-vertices require different D-witnesses. Therefore

> `eta>=A(A+C-1)`.                                        `(BH27)`

Similarly

> `eta>=B(B+C-1)`.                                        `(BH28)`

If the graph is triangle-containing then `A+B>0`. Also every leaf has a W-neighbour, so `A+C>=1` and `B+C>=1`.

Assume without loss of generality `A>=B`.

- If `B=0`, then `C>=1` and `(BH27)` gives

  `E=A+C<=eta+1`.

- If `B>=1`, then

  `E-2=A+B+C-2<=2A+C-2`,

  while

  `A(A+C-1)-(2A+C-2)=(A-1)(A+C-2)>=0`.

  Hence `E<=eta+2`.

Thus in every triangle-containing path case

> `e(W,Z)<=w+eta+2`.                                      `(BH29)`

Since `e(J)=2`,

> `m<=dw-eta+(w+eta+2)+2=dw+w+4`.                        `(BH30)`

Finally

`floor((d+w+2)^2/4)>=dw+w+3`,

because

`(d+w+2)^2-4(dw+w+3)=(d-w)^2+4d-8>=0`

for `d>=2`. Hence

> `e(J)=2`, triangle-containing ==> `m<=M(n)`.             `(BH31)`

### 7.4 `e(J)=3`: the triangle case

Now `J=K_3`.

First, criticality of every Z-edge forces a singleton W-type at at least one endpoint. Indeed, for an edge `ij` of `J`, a triangle-edge witness must lie in `W` (the third Z-vertex is adjacent to both endpoints and D has no Z-neighbours), and the singleton common-neighbour condition forces that witness to have Z-neighbourhood exactly `{i}` or exactly `{j}`. Therefore the coordinates admitting singleton W-types form a vertex cover of `K_3`; at least two coordinates have singleton W-vertices.

Call them coordinates `1,2`.

For `i=1,2`, let `X_i` be the number of W-vertices of Z-degree at least two that are adjacent to `i`. Every edge from such a high-Z-degree W-vertex to `i` lies in a triangle. The reverse orientation is impossible: a W-witness shares the universal leaf `y_0`, while the third Z-vertex sees at least two vertices of the high W-vertex's Z-neighbourhood. Thus the forward witness lies in `D` and its hole set contains all other W-neighbours of `i`.

Distinct high W-vertices require distinct D-witnesses. Since coordinate `i` also has a singleton W-neighbour,

> `eta>=X_i^2` for `i=1,2`.                               `(BH32)`

Let `E=e(W,Z)-w` be the total number of Z-incidences beyond one per W-vertex. If the high type counts are `a_12,a_13,a_23,a_123`, then

`E=a_12+a_13+a_23+2a_123`,

while

`X_1=a_12+a_13+a_123`,

`X_2=a_12+a_23+a_123`.

Hence

`E=X_1+X_2-a_12<=X_1+X_2`.

Let `X=max(X_1,X_2)`. If `X=0`, then `E=0`. If `X=1`, then `E<=2<=eta+1`. If `X>=2`, then

`E<=2X<=X^2<=eta`.

Therefore

> `e(W,Z)<=w+eta+1`.                                      `(BH33)`

Since `e(J)=3`, again

> `m<=dw+w+4<=M(n)`.                                      `(BH34)`

## 8. Three-exception closure theorem

Combining Sections 5--7 gives the main result.

### Theorem 8.1 — bounded-surplus three-exception gate

Let `x in A` support a direct fan `D_x` of order `d>=2` in a D2C graph, and let `eta` be its total direct-fan hole surplus `(BH0)`. If

> `eta<=d-2`,                                              `(BH35)`

then for `n>=11` and

> `z=b+1-d-epsilon_x<=3`,                                 `(BH36)`

at least one of the following holds:

1. `G` is triangle-free;
2. `m<=M(n)`.

Therefore, in the live triangle-containing above-`M(n)` branch with `n>=11`, every direct fan satisfies the compact dichotomy

> `eta>=d-1`,
>
> **or**
>
> `z>=4`.                                                   `(BH37)`

Using `(BH2)`, this is equivalently

> `eta>=d-1`,
>
> **or**
>
> `d+epsilon_x<=b-3`.                                     `(BH38)`

This is the direct-branch stability statement that the previous checkpoint was aiming for: a large fan can approach the complete-bipartite boundary only by accumulating at least one unit of total hole surplus per leaf on average, up to the unavoidable integer endpoint.

### Corollary 8.2 — exact zero-surplus strengthening

If `eta=0` (the exact false-twin equality model), then every live triangle-containing above-`M(n)` candidate of order `n>=11` satisfies

> `z>=4`,                                                  `(BH39)`
>
> `d+epsilon_x<=b-3`.                                     `(BH40)`

This improves the previous exact false-twin gate `z>=3` / `d+epsilon_x<=b-2`.

### Corollary 8.3 — source-local slack alternative

If a live candidate has `d+epsilon_x>=b-2`, then `(BH38)` forces `eta>=d-1`. Since

`eta=d epsilon_x+sum_{y in D}epsilon_y-d(lambda+1)`,

we obtain

> `sum_{y in D}epsilon_y`
> ` >= d(lambda+2-epsilon_x)-1`.                          `(BH41)`

Together with the preserved direct-fan degree floor

`sum_{y in D}epsilon_y>=d(d-T)_+`,

this gives the source-local slack requirement

> `L_A>=epsilon_x`
> `    +max{d(d-T)_+, d(lambda+2-epsilon_x)-1}`           `(BH42)`

whenever `d+epsilon_x>=b-2`.

Thus the remaining near-boundary direct fan is not a free stability object: if it has too few external exceptions, it must pay an additional explicit local slack bill.

## 9. Scope and relation to the negative control

- The proof uses only the preserved direct-fan hole representation, the standard triangle-edge criticality certificate, diameter two, and elementary edge counting.
- The new theorem applies to the **total-hole** regime `eta<=d-2`; individual leaves may have holes and need not be twins.
- It strictly extends the earlier exact false-twin private-support theorem.
- The threshold `n>=11` enters only in the internally active `z=3` arithmetic. The `z<=2` bounded-surplus closure already holds from `n>=7`.
- `X_3` is untouched: at its canonical maximum-degree root, `A` is independent (`f=0`), so there is no positive direct fan and `(BH35)` is never invoked.
- No all-order or eventual second-extremal theorem is asserted.

## 10. Next structural step

The direct branch now has a compact stability normal form:

> **either** the direct fan has `eta>=d-1`,
>
> **or** it needs at least four vertices outside its near-bipartite core.

The next useful move is to feed `(BH38)/(BH42)` back into the rooted fan gate. In particular:

1. split direct sources according to whether `d+epsilon_x<=b-3` or the stronger local slack bill `(BH42)` applies;
2. combine that with the A/U self-priced complementary-pair cost rather than using the old global `R_D(T,L_A)` cap;
3. retain the exact residual target `delta>=D_M` and the rooted transfer lower bound on `f`.

That is more promising than another distribution-free fan-radius optimization because both surviving fan channels now have explicit local self-pricing mechanisms.
