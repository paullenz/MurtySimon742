# Boundary witnesses versus extra U-vertices

Date: 2026-09-21

Status: raw structural theorem inside the repeated rigid one-code `y>=2,m>=2` interface. Sections 2--4 first control extra noncomplementary-code U-vertices. Section 5 shows that on the cheapest/minimal used-boundary-witness face the same capacity bound automatically extends to **all** extra U-vertices, including complementary-code vertices.

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

## 3. Exact local tradeoff

The existing service-counted proof gave

`epsilon_w >= g0+t_w+W-1`

from X-anticompleteness, the `t_w` served source holes and W-independence. Theorem 2.1 sharpens this. Missing R-edges contribute `h-q_w` further U-holes, and if `q_w>0` then all Y is missing rather than merely the `t_w` served sources. Thus

> **`epsilon_w >= g0+t_w+W-1 +(h-q_w)+(y-t_w) 1_{q_w>0}`.** `(3.1)`

Summing over W gives

> **`E_W >= W(g0+W-1)+y(p-ell)+Wh-Q + sum_{q_w>0}(y-t_w)`,** `(3.2)`

where `Q=e(W,R)=sum q_w`.

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

For extra noncomplementary vertices alone, `(3.2)` then gives

> **`E_W >= (p-ell)(2p-ell-1) +(p-ell)h-x`.** `(4.4)`

## 5. Minimal-W face: complementary excess is not an escape

Assume now the minimal used-witness face

> **`W=p-ell`, equivalently `|W_i|=1` for every U-forward coordinate.**

Because the total service count is `y(p-ell)` and every unique witness can serve at most y boundary sources, equality forces

> **`t_w=y` for every `w in W`.** `(5.1)`

Hence every w is already Y-anticomplete, without using Theorem 2.1.

Let

`R_all=U\W`, `h_all=|R_all|`.

This now includes vertices of code `bar d`. Consider any edge wz with `w in W_i`, `z in R_all`.

- If it oriented from z to w, the A-witness would have to be adjacent to w. For `c(z)=bar d` its forced complementary witness code is d, hence the witness would lie in Y; but `(5.1)` makes w Y-anticomplete. For `c(z)!=bar d`, Section 2 already excludes this orientation.
- Therefore **every** W--R_all edge orients from w to z through a witness in `X_{d xor e_i}`.

The same fixed-pair singleton-head injection gives

> **`d_{R_all}(w)<=x_i`** and therefore, because there is one w per coordinate,
>
> **`e(W,R_all)<=sum_i x_i<=x`.** `(5.2)`

Since every missing W--R_all edge contributes to the U-hole term of the corresponding w,

> **`E_W >= (p-ell)(2p-ell-1)+(p-ell)h_all-x`.** `(5.3)`

Using `u=e+k=(p-ell+d)+k` on this face,

`h_all=u-(p-ell)=d+k`,

so the raw minimal-W bill is

> **`E_W >= (p-ell)(2p-ell-1)+(p-ell)(d+k)-x`.** `(5.4)`

The disjoint complementary selected-witness bill from the previous theorem remains

`E_K>=k(p-1)`

for the actual selected witness union. Thus, without identifying K with all complementary-code U-vertices,

> **`E_U >= (p-ell)(2p-ell-1)+(p-ell)(d+k)-x+k(p-1)`.** `(5.5)`

Any overlap in the underlying missing W--K physical edges is legitimate here: `E_U` is a sum of vertex degree deficits, so a missing U--U edge contributes to each endpoint's deficit.

Equation `(5.5)` is the first direct charge on the entire scalar d-arm in the minimal-W geometry. Large d can avoid that charge only by leaving the minimal-W face, i.e. by splitting boundary service among multiple witnesses per coordinate.

## 6. Remaining multiplicity escape

The d-arm is therefore compressed to a clear dichotomy:

1. **minimal W:** all extra U-population, regardless of code, incurs `(5.5)`;
2. **nonminimal W:** `W-(p-ell)>0`, so the fixed total `y(p-ell)` service is split among more physical witnesses. The exact tradeoff `(3.2)` already records the resulting service deficits, but a sharp global lower bound as a function of `W-(p-ell)` remains to be extracted.

This is now the highest-value continuation. A successful lower bound on the service-splitting term would turn the global d escape into a genuine second quadratic cost rather than a scalar reservoir.
