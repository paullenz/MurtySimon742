# False-twin two-exception second-extremal gate

Date: 2026-09-18

Status: internal structural corollary of `FALSE_TWIN_PRIVATE_SUPPORT_AND_BIPARTITE_STABILITY.md`.

This note extracts a clean second-extremal consequence of the private-support theorem. It is useful because the exact zero-surplus direct-fan model is a false-twin blow-up: the number of vertices outside the false-twin class and its common neighbourhood is now a genuine stability parameter.

No all-order second-extremal theorem is claimed.

## 1. Setup

Let `G` be diameter-2-critical. Let `D` be a false-twin class of order `d>=2`, with common open neighbourhood `W`, `w=|W|`. Put

> `Z=V(G)\(D union W)`, `z=|Z|=n-d-w`.                  `(TE0)`

Let

> `W^+={x in W:d_{G[W]}(x)>0}`, `t=|W^+|`.              `(TE1)`

The private-support theorem gives an injection `W^+ -> Z`, so

> `t<=z`,                                                  `(TE2)`

and the edge envelope

> `m<=w(n-w)+binom(z,2)-t(w-1)+binom(t,2)`.              `(TE3)`

Indeed `D` has no neighbours in `Z`, the private witnesses reduce `e(W,Z)` by at least `t(w-1)`, and all edges of `G[W]` lie on the `t` active vertices.

Define the balance deficit

> `B_w=floor(n^2/4)-w(n-w)>=0`.                           `(TE4)`

Since

> `floor(n^2/4)-M(n)=floor(n/2)-1`,                      `(TE5)`

we obtain the following exact criterion.

## 2. False-twin second-extremal criterion

### Theorem 2.1

If

> `B_w+t(w-1)-binom(t,2)-binom(z,2)`
> ` >= floor(n/2)-1`,                                    `(TE6)`

then

> `m<=M(n)=floor((n-1)^2/4)+1`.                          `(TE7)`

### Proof

Rewrite `(TE3)` as

`m<=floor(n^2/4)`
`   -B_w+binom(z,2)-t(w-1)+binom(t,2)`.

Condition `(TE6)` says that the total subtraction from `floor(n^2/4)` is at least the exact gap `(TE5)`. square

This is the first direct comparison with the live second-extremal threshold extracted from the false-twin private-support theorem.

## 3. Zero and one external exceptions

### Corollary 3.1 — `z=0`

If `z=0`, then `t=0` and the private-support theorem gives `G=K_{d,w}`.

Thus the zero-exception false-twin model is exactly the complete-bipartite extremal family.

### Corollary 3.2 — `z=1`

If `z=1`, then `G` is triangle-free.

### Proof

If `G[W]` had an edge, both of its endpoints would lie in `W^+`, so `t>=2`, contradicting `t<=z=1`. Thus `W` is independent.

Now `D` is independent, `D` has no edges to the single vertex of `Z`, and there is no edge inside the one-vertex set `Z`. Hence no triangle exists. square

So the triangle-containing branch cannot realize a false-twin class with exactly one external exception.

## 4. Two external exceptions

Let `z=2`.

If `G[W]` has an edge, then `t>=2`; by `(TE2)`, necessarily

> `t=2`.                                                   `(TE8)`

The edge criterion `(TE6)` then becomes

> `B_w+2w-4 >= floor(n/2)-1`.                             `(TE9)`

### Lemma 4.1

For every integer `n>=7` and every integer `w`, `(TE9)` holds.

### Proof

Write `h=floor(n/2)`.

If `n=2h`, then

`B_w=(w-h)^2`,

and `(TE9)` is equivalent to

`(w-h+1)^2+h-4>=0`,

which holds for `h>=4`; the only even `n>=7` begin at `n=8`.

If `n=2h+1`, write `w=h+a`. Then

`B_w=a^2-a`,

and `(TE9)` is equivalent to

`a^2+a+h-3>=0`.

Its minimum over integer `a` is `h-3`, so it holds for `h>=3`, i.e. `n>=7`. square

Hence:

### Corollary 4.2 — active two-exception case closes at `M(n)`

If `n>=7`, `z=2`, and `G[W]` contains an edge, then

> `m<=M(n)`.                                               `(TE10)`

It remains to understand `z=2` with `W` independent. In fact the triangle-containing case is impossible.

### Theorem 4.3 — independent two-exception case is triangle-free

If `z=2` and `W` is independent, then `G` is triangle-free.

### Proof

Write `Z={r,s}`. Since `D` and `W` are both independent and `D` has no neighbours in `Z`, any triangle would have to be

`r-s-x-r`

for some `x in W`. Thus suppose for contradiction that

`rs in E(G)` and `x in N_W(r) intersect N_W(s)`.

Consider the triangle edge `rx`. Its endpoints remain at distance two after deleting `rx`, so D2C criticality gives the usual triangle-edge unique-common-neighbour certificate in one of two orientations.

**Orientation A.** There is `y` with

`N(r) intersect N(y)={x}`.

The witness is adjacent to `x` and nonadjacent to `r`. It cannot lie in `W`, because `W` is independent; it cannot be `s`, because `s` is adjacent to `r`. Hence it lies in `D`. But every vertex of `D` has neighbourhood exactly `W`, so

`N(r) intersect N(y)=N_W(r)`.

Therefore this orientation forces

> `N_W(r)={x}`.                                           `(TE11)`

**Orientation B.** There is `y` with

`N(x) intersect N(y)={r}`.

The witness is adjacent to `r` and nonadjacent to `x`. It cannot lie in `D`, since every vertex of `D` is adjacent to `x`; it cannot be `s`, since `s` is adjacent to `x`. Thus `y in W`. But both `x` and `y` are adjacent to every vertex of `D`, so their common neighbourhood contains the whole false-twin class `D`, of order at least two. This contradicts the singleton common neighbourhood.

Thus only Orientation A is possible, and `(TE11)` follows. By symmetry, applying the same argument to the triangle edge `sx` gives

> `N_W(s)={x}`.                                           `(TE12)`

Now consider the triangle edge `rs`. A criticality witness oriented from `r` would have to be adjacent to `s` and nonadjacent to `r`. No vertex of `D` is adjacent to `s`; the only W-neighbour of `s` is `x`, but `x` is also adjacent to `r`; and there is no third vertex in `Z`. So no such witness exists. The reverse orientation is identical. This contradicts edge criticality of `rs`.

Hence no triangle exists. square

## 5. Two-exception closure theorem

Combining the preceding cases gives a compact stability statement.

### Theorem 5.1

Let `G` be a diameter-2-critical graph of order `n>=7` containing a false-twin class `D` of order at least two. Put

`z=|V(G)\(D union N(D))|`.

If `z<=2`, then at least one of the following holds:

1. `z=0` and `G` is complete bipartite;
2. `G` is triangle-free;
3. `m<=M(n)`.

Consequently, in the live **triangle-containing above-`M(n)` branch**, every false-twin class must satisfy

> `z>=3`.                                                  `(TE13)`

This is a genuine local second-extremal obstruction rather than only a missing-edge estimate.

## 6. Rooted zero-surplus direct-fan consequence

For an exact zero-surplus direct fan of order `d` around source `x`, the false-twin specialization gives

> `z=b+1-d-epsilon_x`.                                    `(ZF-z)`

Therefore every triangle-containing above-`M(n)` candidate of order at least seven with such an exact direct fan must satisfy

> `b+1-d-epsilon_x>=3`,

or equivalently

> `d+epsilon_x<=b-2`.                                     `(ZF-gate)`

Thus a direct equality fan cannot occupy all but zero, one, or two vertices outside its bipartite blow-up core in the live branch.

## 7. Audit and scope

The theorem package is hand-proved. As a regression check, all 21 D2C graph-atlas classes through order seven were scanned. They contain 21 false-twin classes with `z<=2`: 17 with `z=0`, none with `z=1`, and four with `z=2`; no `z=2` class is triangle-containing. No failure of the statements above was found.

This scan is audit support only.

The order-12, size-32 `X_3` negative control is not excluded by this theorem: its live rooted-transfer analysis has `F_min=0`, so it does not force the exact direct-fan equality model.

No all-order second-extremal statement is asserted.
