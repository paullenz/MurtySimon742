# Boundary witnesses versus extra U-vertices

Date: 2026-09-21

Status: raw structural theorem inside the repeated rigid one-code `y>=2,m>=2` interface. The final theorem below controls the entire extra-U population, including complementary-code vertices, by combining service multiplicity with the singleton-coordinate witness rows.

## 1. Setup

Let `Y=A_d`, `y>=2`, and use the corrected full-boundary theorem. Let `L` be the matched-forward head set, `ell=|L|`, and write

`q=p-ell`.

Choose one U-forward certificate for every boundary edge `y q_i^{d_i}` with `i notin L`. Let `W_i` be the used U-witnesses in coordinate i and `W=union W_i`. Every `w in W_i` has

`c(w)=bar d xor e_i`, `N_X(w)=empty`,

and the previously proved theorem gives `G[W]` independent.

For `w in W`, let `t_w` be the number of chosen boundary edges served by w. Then

`sum_{w in W} t_w = yq`, `1<=t_w<=y`.

Write

`|W|=q+a`,

so `a>=0` measures extra physical boundary-witness multiplicity. Since W is disjoint from the k selected complementary witnesses and `e=u-k=q+d`, one has

> **`0<=a<=d`.** `(1.1)`

## 2. One noncomplementary U-neighbour forces full Y-anticompleteness

If `w in W_i`, z is unmatched with `c(z)!=bar d`, and wz is an edge, raw criticality of the triangular B-edge can only orient from w to z. Its witness lies in `X_{d xor e_i}`, and singleton-head criticality forces

> **`N_Y(w)=empty`.** `(2.1)`

The reverse orientation would require an A-witness of code `bar c(z)` adjacent to w; because w is X-anticomplete this would have to lie in Y, forcing `c(z)=bar d`, contradiction.

## 3. Local service / extra-U tradeoff

For the extra noncomplementary population R, with `h=|R|`, `q_w=d_R(w)`, the exact degree-deficit identity gives

> **`epsilon_w >= g0+t_w+|W|-1 +(h-q_w)+(y-t_w)1_{q_w>0}`.** `(3.1)`

This records both missing extra-U edges and the fact that touching one noncomplementary extra vertex makes w Y-anticomplete.

## 4. Fixed-coordinate witness capacity

For fixed `w in W_i`, every distinct noncomplementary extra-U neighbour requires a distinct physical witness in `X_{d xor e_i}`. Hence

> **`d_R(w)<=x_i:=|X_{d xor e_i}|`.** `(4.1)`

The classes `X_{d xor e_i}` are pairwise distinct and `sum_i x_i<=x`.

## 5. Minimal-W face

If `a=0`, then there is exactly one used boundary witness per U-forward coordinate. Total service forces `t_w=y` for every such w, hence W is Y-anticomplete. The reverse orientation is then impossible even for complementary-code extra vertices. For `R_all=U\W`, every W--R_all edge must orient from w through `X_{d xor e_i}`. Therefore

`e(W,R_all)<=x`.

Since `|R_all|=d+k`,

> **`E_W >= q(2p-ell-1)+q(d+k)-x`.** `(5.1)`

Together with the disjoint selected-complementary bill `E_K>=k(p-1)`, this gives

> **`E_U >= q(2p-ell-1)+q(d+k)-x+k(p-1)`.** `(5.2)`

## 6. General singleton-coordinate barrier

The preceding mechanism does not require *all* coordinate witness sets to be singletons. Let

`S0={i notin L: |W_i|=1}`

and `q0=|S0|`.

Every nonsingleton coordinate consumes at least one of the a extra physical witnesses, so

> **`q0>=q-a`.** `(6.1)`

(When `a>q`, use the trivial `q0>=0`.)

For each `i in S0`, the unique w_i must serve all y boundary sources at coordinate i, so

> **`t_{w_i}=y` and `N_Y(w_i)=empty`.** `(6.2)`

Now put

`R_all=U\W`, `h_all=|R_all|`.

Using `u=e+k=q+d+k` and `|W|=q+a`,

> **`h_all=d+k-a`.** `(6.3)`

For every singleton-coordinate witness w_i and every z in R_all, an edge w_i z cannot orient from z to w_i:

- if `c(z)=bar d`, the required reverse witness has code d and lies in Y, but w_i is Y-anticomplete;
- otherwise the reverse orientation is already excluded by Section 2.

Hence every such edge must orient from w_i to z through a witness in the fixed class `X_{d xor e_i}`. For fixed w_i, distinct heads z require distinct physical X-witnesses. Summing over the pairwise-distinct singleton coordinate classes gives

> **`e(W_0,R_all)<=sum_{i in S0} x_i<=x`,** `(6.4)`

where `W_0={w_i:i in S0}`.

Therefore at least

> **`q0 h_all-x >= (q-a)(d+k-a)-x`** `(6.5)`

W_0--R_all edges are missing whenever the right side is positive. These missing U-edges are not included in the earlier service-counted floor.

The service-counted theorem gives

`E_W >= |W|(g0+|W|-1)+yq`

before this extra term. Thus the whole repeated-code branch satisfies the new finite bound

> **`E_W >= (q+a)(g0+q+a-1)+yq + max{0,(q-a)(d+k-a)-x}`.** `(6.6)`

Finally W and the selected complementary witness union K are disjoint code layers, so adding the preserved `E_K>=k(p-1)` bill is legitimate:

> **`E_U >= (q+a)(g0+q+a-1)+yq`**
>
> **`      + max{0,(q-a)(d+k-a)-x}+k(p-1)`,**             `(6.7)`
>
> for some integer **`0<=a<=d`**.

This is a substantially sharper normal form than the previous scalar d parameter. It shows exactly how d can escape: it must choose between

1. **witness multiplicity** `a`, which enlarges the independent W-layer and therefore the quadratic service floor; and
2. **unconsumed extra U-population** `d-a`, which creates a rectangular singleton-W versus extra-U hole block unless X contains enough coordinate-specific witnesses to certify the corresponding physical edges.

The complementary-code reservoir is included: it cannot bypass the singleton rows.

## 7. Next optimization target

Equation `(6.7)` should now replace the coarser boundary bill in the exact score ceiling. The next question is whether minimizing over `a in [0,d]` upgrades the 6.09% macroscopic wedge, or closes a full neighborhood of the old small-`r`, small-`g0` escape. Any asymptotic optimization must retain the `x` term explicitly until an independently justified relation between x and the one-code parameters is inserted.
