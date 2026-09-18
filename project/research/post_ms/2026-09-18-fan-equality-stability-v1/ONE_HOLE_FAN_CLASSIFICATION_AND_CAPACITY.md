# One-hole A/U fan classification and capacity

Date: 2026-09-18

Status: internal follow-on theorem package for the eventual / sufficiently-large D2C second-extremal programme. This treats the cheapest surviving perturbation after the zero-hole equality model was excluded in beta-saturated sparse-U slices.

No global eventual theorem is claimed.

## 1. Motivation

The beta-sensitive fan-hole theorem shows that when the global U-edge allowance

`Q_beta=au-B_beta+N_1`

is subquadratic, a linear A/U fan cannot contain linearly many zero-hole witnesses. The next cheapest local model is therefore

`g_i=1`

for most or all witnesses.

That case is much more rigid than a generic bounded-hole fan. The single hole identifies the witness type, and the witness graph becomes a clique with only a matching-sized defect.

## 2. Setup

Fix an A/U certificate fan with A-source `x`, distinct A-heads `h_i`, distinct witnesses `w_i in A union U`, and

`N(x) intersect N(w_i)={h_i}`.

As before, put

`Y_x=V(G)\({x} union N(x))`,

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|`.

Assume throughout this note that

> `g_i=1` for every `i`.                                  `(OH)`

Write the unique hole as

`Z_i={z_i}`.

All witnesses have Boolean code `bar(c(x))`, and the head-witness cut is the exact matching `h_iw_i`.

## 3. Witness graph is clique minus a matching

The exact fan-neighbourhood theorem gives

`N(w_i)={h_i} union (Y_x\{w_i,z_i})`.

### Lemma 3.1 — one-hole complement matching

Inside the witness set `W_x`, every vertex has at most one nonneighbour. Therefore

> `Delta(overline{G[W_x]})<=1`.                           `(OHM)`

Equivalently, the missing witness edges form a matching.

More precisely, if `w_iw_j` is absent, then

> `z_i=w_j` and `z_j=w_i`.                                `(OHP)`

Proof. Since `w_j in Y_x\{w_i}`, nonadjacency to `w_i` forces the unique hole `z_i` to equal `w_j`; symmetry gives the other identity. square

Thus a one-hole fan has a witness side which is exactly a clique minus disjoint pairs.

## 4. The single hole identifies A-witnesses

### Lemma 4.1 — root-hole identification

If `w_i in A`, then

> `z_i=v`.                                                `(RHI)`

Proof. Both `x` and `w_i` are nonadjacent to the root `v`, so `v` is an external hole of `(x,w_i)`. There is only one. square

Consequently any two A-witnesses are adjacent, because neither can be the other's hole.

### Corollary 4.2 — A-witness side is a clique

Let

`W_A=W_x intersect A`, `d_A=|W_A|`.

Then

> `G[W_A]=K_{d_A}`.                                       `(AWC)`

All vertices of `W_A` have the same Boolean code `bar(c(x))`.

## 5. A-witness heads are almost all exactly clean

Assume `p>=1`, so every witness-witness edge is non-direct because same-code witnesses share the selected tight-core endpoints.

For an A-witness index define, as before,

`t_i=|N(h_i) intersect (Y_x\{w_i})|`.

### Lemma 5.1 — the root hole cannot certify an A-witness pair

Let `i,j` be distinct A-witness indices. The edge `w_iw_j` cannot use `v` as the external certificate in either orientation, because `v` is nonadjacent to both A-witnesses.

Hence any criticality certificate for `w_iw_j` is a matching head: either `h_j` certifies the orientation from `w_i`, or `h_i` certifies the reverse orientation.

If `h_j` certifies from `w_i`, then

> `t_j=0`.                                                `(AHC)`

Proof. The general head-or-hole theorem says every extra `Y_x`-neighbour of `h_j` must lie in `Z_i={v}`. But `h_j in A` is nonadjacent to `v`, so there are none. square

### Theorem 5.2 — A-witness clean-head theorem

Among the `d_A` heads matched to A-witnesses, at most one has `t_i>0`.

For every other A-witness index,

> `N(h_i) intersect Y_x={w_i}`,                           `(ACLEAN)`
>
> `N(h_i) intersect N(w_i)=empty`,                        `(ADIR)`
>
> `c(h_i)=c(x)`.                                          `(ACODE)`

Proof. Every pair of A-witness indices has at least one endpoint whose head is clean by Lemma 5.1. Thus the dirty indices form an independent set in a complete graph and have size at most one. The directness and code conclusion are the same as in the zero-hole theorem. square

So a large one-hole A-witness population already contains, up to one exception, the exact dual structure from the zero-hole model: source-code heads directly matched to an antipodal same-code A-clique.

## 6. U-witness side is near-clique and directly raises q

Let

`W_U=W_x intersect U`, `d_U=|W_U|`.

By `(OHM)`, the missing graph on `W_U` also has maximum degree at most one. Therefore

> `e(G[W_U])>=binom(d_U,2)-floor(d_U/2)`.                 `(UWC)`

Since `G[W_U]` is a subgraph of `G[U]`,

> `q>=binom(d_U,2)-floor(d_U/2)`.                         `(OHQ)`

Combining with the beta-sensitive q-cap

`q<=Q_beta`

gives

> `d_U <= floor(1+sqrt(2Q_beta+1))`.                      `(DUC)`

Indeed `(OHQ)` implies `d_U(d_U-2)/2<=Q_beta`.

Thus beta saturation directly limits the U-part of any one-hole fan.

## 7. Same-code payment caps the A-witness side

All A-witnesses lie in one Boolean code class `c=bar(c(x))` and form a clique.

The preserved same-code weighted edge capacity says

`(lambda+1)e(G[V_c])`
` <= N_bar(c) S_c + N_c S_bar(c)`.

Since `e(G[V_c])>=binom(d_A,2)` and `N_c,N_bar(c)<=V_0:=a+u`,

> `(lambda+1)binom(d_A,2)<=V_0(E_U+L_A)`.                `(AWP)`

Consequently

> `d_A`
> ` <= floor((1+sqrt(1+8V_0(E_U+L_A)/(lambda+1)))/2)`.   `(DAC)`

This is intentionally distribution-free; the code-resolved version is stronger when `S_c,S_bar(c)` are known.

## 8. Finite one-hole fan capacity

Since `d=d_A+d_U`, `(DUC)` and `(DAC)` give:

### Theorem 8.1 — one-hole fan capacity

Every all-one-hole A/U fan satisfies

> `d <= R_A^(1)+R_U^(1)`,                                `(OHFC)`

where

> `R_A^(1)=floor((1+sqrt(1+8V_0(E_U+L_A)/(lambda+1)))/2)`,
>
> `R_U^(1)=floor(1+sqrt(2Q_beta+1))`.

Thus the two witness types are paid by different global resources:

- A-witnesses consume same-code slack capacity;
- U-witnesses consume internal-U edge capacity, already beta-sensitive.

There is no third cheap reservoir.

### Corollary 8.2 — quadratic edge dichotomy

For every all-one-hole fan,

> `e(G[A_bar(c(x))])+q >= d^2/4-d`.                       `(OHED)`

Proof. The A-witness clique contributes `binom(d_A,2)` A-edges. The U-witness near-clique contributes at least `binom(d_U,2)-floor(d_U/2)` U-edges. Since `d_A^2+d_U^2>=d^2/2`, the sum is at least `d^2/4-d`. square

So a linear one-hole fan always creates quadratic internal edge mass on one or both sides of the rooted decomposition.

## 9. Head localization in the one-hole model

The general threshold stability theorem with `G_x=d` and `tau=1` gives

> all but at most `floor((1+sqrt(1+12d))/2)` heads satisfy `t_i<=1`.

Hence all but `O(sqrt(d))` heads satisfy

> `dist_H(c(h_i),c(x))<=1`.                               `(OHHL)`

This can be sharpened on the A-witness indices by Theorem 5.2: all but at most one of those heads have **exactly** the source code.

Thus the one-hole model is a finite-radius Hamming object:

- witness code: exactly `bar(c(x))`;
- almost every A-witness head: exactly `c(x)`;
- all but `O(sqrt(d))` remaining heads: in the radius-one Hamming ball about `c(x)`.

This is a much smaller code-capacity target than the generic `o(p)` Hamming ball from the low-hole theorem.

## 10. Strategic consequence

The cheapest surviving fan after zero-hole exclusion is now fully split into two explicit mechanisms.

1. **A-hole mechanism:** the unique hole is the root, the witnesses form a same-code A-clique, and almost every matched head is exactly direct/source-code. This is priced by `(AWP)`.
2. **U-hole mechanism:** the witnesses lie in `U`, their induced graph is clique-minus-matching, and they directly force q through `(OHQ)`, which is priced by the beta-sensitive cap `(BQ)`.

Therefore an all-one-hole linear fan can survive only if at least one of the global budgets `E_U+L_A` or `Q_beta` is itself quadratic at the required scale.

The next useful extension is not another generic fan inequality. It is to show that any bounded-hole fan reduces, after deleting a controlled exceptional set, to a bounded union of these one-hole mechanisms; alternatively, insert `(OHFC)` directly into the rooted-transfer fan gate and test parameter closure.

## 11. Scope

The mandatory order-12, size-32 `X_3` control remains untouched: its canonical root has `u=0` and the rooted-transfer floor does not force this fan branch.

The triangle-free second-extremal case remains separate and known. The statements here concern only the triangle-containing near-full partial-Boolean branch.
