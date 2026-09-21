# Boundary witnesses versus extra noncomplementary U-vertices

Date: 2026-09-21

Status: raw structural theorem inside the repeated rigid one-code `y>=2,m>=2` interface. This note is deliberately narrower than the scalar `d=e-(p-ell)` arm: it controls extra **noncomplementary-code** U-vertices. Extra vertices of code `bar d` require a separate treatment and are not silently charged here.

## 1. Setup

Let `Y=A_d`, `y>=2`, and use the corrected full-boundary theorem. Let `L` be the matched-forward head set, `ell=|L|`, and choose one U-forward certificate for every boundary edge `y q_i^{d_i}` with `i notin L`. Let `W_i` be the used U-witnesses in coordinate i and `W=union W_i`. Every `w in W_i` has

`c(w)=bar d xor e_i`, `N_X(w)=empty`,

and the previously proved theorem gives `G[W]` independent.

Put

`T={z in U : c(z) != bar d}`

and `R=T\W`, `h=|R|`. For `w in W`, let `t_w` be the number of chosen boundary edges served by w, and `q_w=d_R(w)`.

## 2. One noncomplementary U-neighbour forces full Y-anticompleteness

### Theorem 2.1

If `w in W_i`, `z in R`, and `wz` is an edge, then raw criticality of the triangular B-edge `wz` can only orient from w to z. Its witness lies in

`X_{d xor e_i}`,

and in particular

> **`N_Y(w)=empty`.**

### Proof

Both w and z lie in `B=N(v)`, so a B-witness in either orientation would share the root with the B-source; the witness must lie in A.

For an orientation from z to w, tight matched transversality forces an A-witness of code `bar c(z)` adjacent to w. Because w is X-anticomplete, such a witness would have to lie in Y. But Y has the unique code d, which would force `bar c(z)=d`, i.e. `c(z)=bar d`, contrary to `z in R`.

Hence the orientation is from w to z. Avoiding a tight matched common neighbour forces the A-witness code to be `bar c(w)=d xor e_i`, which is not d and therefore lies in X. Since the rigid cut is complete, this X-witness is adjacent to every vertex of Y. Singleton-head criticality `N(w) cap N(x)={z}` therefore forces w to have no Y-neighbour. `square`

This is a useful dichotomy: a used boundary witness that touches even one extra noncomplementary U-vertex must pay all y outside-code A-holes.

## 3. Exact local tradeoff

The existing service-counted proof gave

`epsilon_w >= g0+t_w+W-1`

from X-anticompleteness, the `t_w` served source holes and W-independence. Theorem 2.1 sharpens this. Missing R-edges contribute `h-q_w` further U-holes, and if `q_w>0` then all Y is missing rather than merely the `t_w` served sources. Thus

> **`epsilon_w >= g0+t_w+W-1 +(h-q_w)+(y-t_w) 1_{q_w>0}`.** `(3.1)`

Summing over W gives

> **`E_W >= W(g0+W-1)+y(p-ell)+Wh-Q + sum_{q_w>0}(y-t_w)`,** `(3.2)`

where `Q=e(W,R)=sum q_w`.

This strictly refines the earlier boundary-service floor unless the extra R-population is almost completely joined to W in a way that also makes every participating boundary witness already serve essentially all y outside sources.

## 4. Fixed-coordinate witness capacity

### Theorem 4.1

For fixed `w in W_i`, distinct neighbours `z in R` require distinct physical witnesses in `X_{d xor e_i}`. Consequently

> **`q_w <= x_i:=|X_{d xor e_i}|`.** `(4.1)`

### Proof

Theorem 2.1 forces every edge wz to be certified in the orientation from w with an X-witness x of the fixed code `d xor e_i`, satisfying `N(w) cap N(x)={z}`. A fixed ordered physical pair `(w,x)` cannot have two different singleton heads z and z'. Therefore distinct R-neighbours require distinct x. `square`

Hence

> **`Q <= sum_i |W_i| x_i`.** `(4.2)`

The code classes `X_{d xor e_i}` are pairwise distinct, so `sum_i x_i<=x`.

In the cheapest used-witness face `|W_i|=1` for every U-forward coordinate (therefore `W=p-ell` and each unique witness serves all y boundary edges at its coordinate), `(4.2)` simplifies to

> **`Q<=x`.** `(4.3)`

Equation `(3.2)` then becomes the clean additional defect bill

> **`E_W >= (p-ell)(2p-ell-1) +(p-ell)h-x`.** `(4.4)`

Thus if the forward-population excess is realized by h extra noncomplementary U-vertices while the boundary witness set remains minimal, those extra vertices are not a free repair reservoir: making them adjacent to the boundary witnesses requires at least one distinct X witness per physical W--R edge, and at most x such edges can be supported in the minimal-W face.

## 5. What this does and does not resolve

This attacks a real portion of the `d` escape arm exposed by the global score wedge. It does **not** yet charge extra U-vertices of complementary code `bar d`; those can potentially use the reverse orientation with a Y-witness on W--U edges and must be separated. Nor does `(4.2)` by itself control large multiplicities `|W_i|`; there the same X-code class may be reused across different physical sources w, although each fixed `(w,x)` has only one singleton head.

The next useful split is therefore:

1. minimal/near-minimal boundary-witness multiplicity, where `(4.4)` converts noncomplementary forward excess directly into quadratic/linear-X slack;
2. large `|W|- (p-ell)`, where service splitting already creates source deficits and should be combined with `(3.2)`;
3. complementary-code excess, which needs its own raw B-edge/diameter audit rather than being folded into d by scalar bookkeeping.
