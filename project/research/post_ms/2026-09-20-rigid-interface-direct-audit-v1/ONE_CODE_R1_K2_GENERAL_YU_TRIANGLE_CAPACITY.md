# Residual-one k=2: general Y--U triangle/capacity theorem

Date: 2026-09-20

Status: **same-session conditional structural theorem**, valid throughout the rigid one-code residual-one branch with `k=2`, `J2=empty`, `p>=3`; it is not restricted to the exact stress ray. No finite scan is used.

This note extracts the parameter-free core of the exact-ray closure so that the next session can optimize it with variable `y`, `c`, `g0=p-y`, and `lambda`.

## 1. General residual-one k=2 setup

Residual dimension one gives

- `x=p+1` because `x-k=p-1` and `k=2`;
- `u=c+1` because `k=u-c+1`;
- `|H|=p-1`;
- `K` has two heads of code `C=d xor e_j`;
- `Y=A_d`, `|Y|=y`;
- `J2=empty`, so every matched head `h_i` has code `d xor e_i`.

The complete A-code repertoire is therefore

- d on Y;
- C on K;
- `d xor e_i` on the single head `h_i`, `i in I`.

In particular `A_bar(d)=empty` for `p>=3`.

Let

`B=B0={w in U_bar(d):d_H(w)=0}`,

`b=|B|`,

and `D=U\B`, `d_U=|D|=u-b`.

The predecessor private-spoke theorem gives

- B is Y-anticomplete;
- B is independent;
- every source outside B has oriented U--U source capacity at most two (H-positive `bar d` sources have capacity zero; all other complementary A-classes have size at most two).

The companion Y-independence theorem is also parameter-free here:

> **`e(Y)=0`.**                                            `(GYC-Y0)`

## 2. Every Y--U edge is triangular

> **THEOREM (GYC-TRI). Every edge between Y and U lies in a triangle.**

Take `y0 in Y` and `t in U` with `y0t in E`.

If `c(t)!=bar d`, then some tight matched coordinate agrees with d. Since `y0` has code d, y0 and t see the same endpoint of that tight matched pair. That endpoint is a common neighbour, so the edge lies in a triangle.

If `c(t)=bar d`, then:

- if `d_H(t)=0`, t lies in B and is Y-anticomplete, contradiction;
- if `d_H(t)>0`, any H-neighbour of t is also adjacent to y0 because Y is complete to X.

Thus the edge is triangular in every case. `(GYC-TRI)`

This is the exact structural fact that resolves the triangle-scope warning for Y--U edges inside the present branch. The warning remains valid outside this scope.

## 3. Every high-Y non-B vertex is reverse-certified through B

Let

`D_2={t in D:d_Y(t)>=2}`.

Fix `t in D_2` and an edge `ty0`, `y0 in Y`.

By `(GYC-TRI)`, the triangle-edge two-orientation lemma applies.

### Forward orientation from t is impossible

- any rooted-B witness shares the root with t;
- any X-witness is adjacent to every Y-vertex and therefore shares another Y-neighbour of t besides y0;
- a Y-witness cannot be adjacent to the singleton head y0 because `e(Y)=0`.

Hence the forward orientation fails.

### Reverse orientation

Let w be the reverse witness, so

`N(y0) cap N(w)={t}`.

The source y0 has code d. Any matched endpoint shared by y0 and w would be an extra common neighbour, so

`c(w)=bar d`.

Since `A_bar(d)=empty`, w lies in U. Because Y is complete to X, the singleton equation forces

`N_X(w)=empty`.

Therefore w is H-free and hence

> **`w in B0`.**                                           `(GYC-BW)`

For one fixed ordered pair `(y0,w)`, the graph-fixed singleton common-neighbour set identifies at most one head t. Consequently

> **`e(Y,D_2)<=y b`.**                                     `(GYC-CAP)`

The low-Y set `D\D_2` contributes at most `d_U` further Y--U edges. Therefore

> **`e(Y,D)<=yb+d_U`.**                                   `(GYC-EDGE)`

Because B itself is Y-anticomplete,

> **`Z_{Y,U}>=max{by, d_U(y-1)}`.**                       `(GYC-Z1)`

The second term follows from

`yu-e(Y,D) >= yu-yb-d_U=d_U(y-1)`.

## 4. B--D U-edges force additional Y--D isolation holes

Let

`C=e(B,D)`.

Orient every U--U edge by one valid raw certificate. Sources in D contribute at most two oriented U--U edges each, so at least

> `O=[C-2d_U]_+`                                          `(GYC-O)`

cross edges are sourced in B.

For `w in B`, let `o_w` be the number of those B-sourced cross edges from w. A B-source has code `bar d`, so its A-witness has complementary code d and therefore lies in Y.

If y is the witness for the edge wt, then

`N(w) cap N(y)={t}`.

Thus y must miss every other D-neighbour of w. Distinct outgoing heads from w require distinct Y-witnesses. If `q_w=d_D(w)`, the witness family forces at least

`o_w(q_w-1)>=o_w(o_w-1)`

Y--D nonedges.

A fixed Y--D nonedge `(y,t')` can be charged for at most b different sources w, because a charge requires `wt' in E`. Therefore

`b Z_{Y,D} >= sum_w o_w(o_w-1)`.

Cauchy gives

`sum_w o_w(o_w-1) >= O^2/b-O`.

Hence, for `b>0`,

> **`Z_{Y,D} >= [O(O-b)/b^2]_+`.**                       `(GYC-ISO)`

Combining the physically disjoint B--Y holes with the two D-side bounds gives the exact safe form

> **`Z_{Y,U} >= by + max{0, y(d_U-b)-d_U, O(O-b)/b^2}`.** `(GYC-Z2)`

Here the capacity and isolation terms both live in Y--D, so they are combined by a maximum, not added.

## 5. Why this is the right off-ray object

The exact low-k ray set `y=p-1`, `u=p+1`; inserting those values into `(GYC-Z2)` plus the exact U-degree identity produced the strict score coefficient

`2-2/(3sqrt(3))>3/2`

and hence finite-order closure of that ray.

Off the ray, the theorem itself remains valid with no asymptotic specialization. The next optimization should retain at least

- `p`;
- `y` or `theta=y/p`;
- `c` and `u=c+1`;
- `g0=p-y`;
- `b=|B0|`;
- `C=e(B0,U\B0)`;
- the exact score ceiling through `lambda=c+p-y-1`.

The two competing mechanisms are now explicit:

1. small B gives too little reverse-certificate capacity for Y--U density;
2. large B is itself Y-anticomplete and independent;
3. dense B--D U adjacency forces a quadratic isolation rectangle in Y--D.

This is a compact structural package suitable for the next variable-parameter score/rooted optimization.

Global caveat unchanged: all statements remain conditional downstream of the rigid complete Hall-cut interface, whose bounded actual-D2C regression still has zero positive fixtures with `x>=3`.