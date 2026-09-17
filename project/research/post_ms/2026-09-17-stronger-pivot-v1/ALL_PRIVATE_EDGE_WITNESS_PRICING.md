# All-private edge-witness pricing and the dense-root antipode theorem

17 September 2026. **Internal candidate hand theorem; external mathematical and novelty review open.**

This strengthens `ALL_PRIVATE_STABILITY.md`. The earlier gap inequality

` t(b-t) <= 2 delta `

uses only the cost of private feet and maximum-degree slack. The missing ingredient is that **every edge of `G[B]` is itself critical**. Pricing one criticality witness per `B`-edge gives a much stronger inequality and, in the second-extremal density regime, removes the entire all-private branch for sufficiently large order.

No claim about the eventual second-extremal problem is promoted here. The maximum-triangle-root scope issue and the antipode branch remain open.

## 1. Setup

Let `G` be diameter-2-critical and let `v` be a maximum-degree root. Put

`B=N(v)`, `A=V(G)\N[v]`, `b=|B|`, `a=|A|`, `F=G[A]`,

`Q=e(G[B])`, `f=e(F)`, `delta=b(n-b)-m=r-f`.

Let `T` be the set of triangle-active vertices of `B`, i.e. the endpoints of edges of `G[B]`, and write `t=|T|`. Assume `Q>0`, so `t>=2`.

Assume the **all-private branch**: for each `u in T`, choose a private foot `x_u in A` with

`N_G(x_u) intersect B={u}`.

The feet are automatically distinct. Let

`X={x_u : u in T}`, `Y=A\X`.

Since every `B`-edge has both ends in `T`, write

`C=binom(t,2)`, `s=C-Q >=0`.

Thus `s` is the number of missing edges from the complete graph on the active set `T`.

Let

`d=C-e(F[X]) >=0`

be the number of missing edges among the private feet. Let

`c=e_F(X,Y)`, `g=e_F(Y)`.

Finally let `E` be the number of missing `A-B` incidences whose `A`-endpoint lies in `Y`. The private feet themselves contribute exactly `t(b-1)` missing cross incidences, so

`Q+r=t(b-1)+E`.                                      (1.1)

## 2. A stronger defect payment already follows from maximum degree

Because

`Q=C-s`, `f=C-d+c+g`, `r=f+delta`,

substituting into (1.1) gives

`E = delta-s-t(b-t)-d+c+g`.                           (2.1)

For every `y in Y`, if `h_y` is the number of missing neighbours of `y` in `B`, then

`deg_B(y)=b-h_y`.

Since `v` has maximum degree `b`,

`deg_F(y)<=h_y`.

Summing over `Y` gives

`c+2g <= E`.                                          (2.2)

In particular `c+g<=E`. Combining with (2.1) yields

> `delta-s >= t(b-t)+d`.                              (2.3)

So the all-private branch already pays not only for the active/inactive gap but also for every missing private-foot edge.

## 3. Criticality of every B-edge gives an injective defect charge

Take an edge `uw in E(G[B])` and delete it. The endpoints `u,w` remain at distance two through the root `v`, so they cannot themselves witness criticality.

Any length-at-most-two path destroyed by deleting `uw` must use `uw`. Therefore, after orienting the edge if necessary, there is a vertex `z in N(u)\{w}` such that the pair `(z,w)` has distance greater than two in `G-uw`.

The witness cannot lie in `B` (a `B`-vertex still reaches `w` through `v`), and it cannot be `v`. Hence `z in A`. Necessarily

`z not~ w`,

and

`N_G(z) intersect N_G(w)={u}`.                        (3.1)

Now charge the edge `uw` as follows.

### Type I: the witness is the private foot

If `z=x_u`, then `x_w` is adjacent to `w`. Condition (3.1) forces

`x_u x_w notin E(F)`.

Charge `uw` to the missing foot-foot edge `x_u x_w`, counted by `d`.

### Type II: the witness is not the private foot

If `z!=x_u`, then `z` cannot be any other private foot, because every private foot has a unique neighbour in `B`. Hence `z in Y`. Since `z not~w`, charge `uw` to the missing cross incidence `(z,w)`, counted by `E`.

### Injectivity

Type-I charges are injective because the missing pair `x_u x_w` identifies the `B`-edge `uw`.

A Type-II charge `(z,w)` can also occur for at most one `B`-edge. Indeed, (3.1) says that the source `u` is the **unique** common neighbour of `z` and `w`; two distinct source edges charged to the same `(z,w)` would give two common neighbours.

The two charge types are disjoint. Therefore

> `Q <= d+E`.                                         (3.2)

This is the new criticality input.

## 4. Eliminate the internal variables

Let

`L=sum_{x in A} (b-deg_G(x)) >=0`

be the total maximum-degree slack on `A`. A direct degree sum gives

`L=Q+delta-f`.

Together with (1.1),

`E+L=2(delta-s)-t(b-t)`.                              (4.1)

Hence

`E <= 2(delta-s)-t(b-t)`.                             (4.2)

From (2.3),

`d <= delta-s-t(b-t)`.                                (4.3)

Use (3.2), (4.2), (4.3), and `Q=C-s`:

`C-s <= d+E`

`     <= 3(delta-s)-2t(b-t)`.

Therefore:

> **ALL-PRIVATE EDGE-WITNESS PRICING THEOREM (APW).**
>
> `3 delta >= binom(t,2) + 2s + 2t(b-t)`.             (APW)

This is strictly stronger than the earlier coarse all-private gap estimate in the dense regimes relevant here.

Two useful endpoint cases are:

- if `t=b`, then `3delta >= binom(b,2)+2s`;
- if `t=2`, then `3delta >= 4b-7+2s`.

## 5. Uniform lower bound when b>=7

For fixed `b`, ignoring the nonnegative `2s` term gives

`3delta >= Phi_b(t)`,

where

`Phi_b(t)=binom(t,2)+2t(b-t)=t(4b-3t-1)/2`.

This is a concave quadratic in `t`, so on `2<=t<=b` its minimum is at an endpoint.

`Phi_b(2)=4b-7`,

`Phi_b(b)=binom(b,2)`.

For `b>=7`, `binom(b,2)>=4b-7`. Hence

> `3delta >= 4b-7` whenever `b>=7`, `Q>0`, and the root is all-private.   (5.1)

## 6. Dense second-extremal consequence

Let

`M(n)=floor((n-1)^2/4)+1`.

Assume

`n>=14`, `m>=M(n)+1`,

and a maximum-degree root `v` lies in a triangle (`Q>0`).

We show that the all-private branch is impossible.

### Even order

Let `n=2k`, so `k>=7`. Then

`M(n)+1=k^2-k+2`.

Since `b=Delta(G)>=ceil(2m/n)`, one has `b>=k`. Write `b=k+j`, `j>=0`. Then

`delta=b(n-b)-m`

`<= (k+j)(k-j)-(k^2-k+2)`

`= k-j^2-2`.

Thus

`3delta <= 3k-3j^2-6`.

But (5.1) requires

`3delta >=4b-7=4k+4j-7`.

The latter lower bound exceeds the former upper bound by

`k+3j^2+4j-1>0`,

a contradiction.

### Odd order

Let `n=2k+1`, so `k>=7`. Then

`M(n)+1=k^2+2`.

Again `b>=ceil(2m/n)>=k`; write `b=k+j`, `j>=0`. Now

`delta <= (k+j)(k+1-j)-(k^2+2)`

`=k+j-j^2-2`,

so

`3delta <=3k+3j-3j^2-6`.

But (5.1) gives

`3delta >=4k+4j-7`,

and the lower bound exceeds the upper bound by

`k+j+3j^2-1>0`.

Again contradiction.

Therefore:

> **DENSE ROOT ANTIPODE THEOREM (internal candidate).**
>
> Let `G` be D2C of order `n>=14` with `m>=M(n)+1`. If a maximum-degree root `v` lies in a triangle, then the all-private alternative of the root-edge dichotomy is impossible. Consequently there exist `u,w in N(v)` such that
>
> `uw notin E(G)` and `N_G(u) intersect N_G(w)={v}`.

Thus any sufficiently-large counterexample above the proposed second-extremal level, **provided a maximum-degree vertex lies in a triangle**, must enter the disjoint-support antipode branch.

This does not solve the maximum-triangle-root scope issue and does not yet contradict the antipode branch.

## 7. The 12-vertex hostile control remains intact

The published 2024 order-12, size-32 D2C exception has

`32>M(12)=31`

and remains a mandatory negative control.

The independent `X_3` reconstruction in `HYPERCUBE_FACE_EXCEPTION.md` has maximum-degree root data

`n=12`, `b=8`, `F=empty`, `delta=0`, `Q=12`.

It is **not** in the all-private branch: with `F=empty`, private feet cannot exist in a non-star D2C graph. It instead has the antipodal structure explicitly supplied by the cube. Hence APW and the dense-root antipode theorem do not exclude or misclassify the 12-vertex obstruction.

The threshold theorem above is stated only from `n>=14` so the eventual argument remains cleanly separated from the small hostile control.

## 8. Regression and trust boundary

The companion checker `check_all_private_edge_witness_pricing.py` does two independent finite regressions:

1. every all-private maximum-degree triangle root in the NetworkX graph atlas through order 7 satisfies APW (three such roots, zero violations);
2. the parity arithmetic proving the dense consequence is exhaustively checked for a wide finite range of `n,b,t,s`, with no failure.

The finite checks are evidence only. The proof above is the mathematical basis.

External review remains required, especially for the edge-criticality witness injection in Section 3. No eventual second-extremal theorem is claimed.
