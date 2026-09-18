# Bounded-hole A/U fan capacity

Date: 2026-09-18

Status: internal structural theorem package for the live eventual / sufficiently-large D2C second-extremal programme. This extends the exact one-hole type split to every uniformly bounded-hole fan.

No global eventual theorem is claimed.

## 1. Setup

Fix an A/U certificate fan with A-source `x`, heads `h_i`, witnesses `w_i in A union U`, and order `d`.

Let

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|=epsilon_x+epsilon_{w_i}-(lambda+1)`.

Assume a uniform hole bound

> `g_i<=K` for every `i`,                               `(BH)`

where `K>=1` is an integer.

All witnesses have Boolean code `bar(c(x))`.

Split

`W_A=W_x intersect A`, `d_A=|W_A|`,

`W_U=W_x intersect U`, `d_U=|W_U|`,

so `d=d_A+d_U`.

The exact witness-neighbourhood normal form says that a witness `w_i` is nonadjacent, among the vertices in `Y_x`, only to the vertices of its hole set `Z_i`.

## 2. A-witness side: the root consumes one hole

If `w_i in A`, then the maximum-degree root `v` lies in `Z_i`. Since `v` is not another witness,

> `d_{overline{G[W_A]}}(w_i)<=K-1`.                     `(BAdeg)`

Hence

> `e(G[W_A])`
> ` >= binom(d_A,2)-(K-1)d_A/2`
> ` = d_A(d_A-K)/2`.                                     `(BAedge)`

The right side may be negative for `d_A<K`; in that range the statement is understood with the trivial lower bound zero.

All edges of `G[W_A]` are same-code A-edges. Let `c=bar(c(x))`, `V_0=a+u`, and `S=E_U+L_A`. The preserved same-code weighted edge capacity gives

`(lambda+1)e(G[V_c])`
` <= N_bar(c)S_c+N_cS_bar(c)`
` <= V_0S`.

Since `G[W_A] subseteq G[V_c]`, we obtain:

### Theorem 2.1 — bounded-hole A-witness capacity

> `(lambda+1)d_A(d_A-K)/2 <= V_0S`.                     `(BAC)`

Therefore

> `d_A <= R_A(K)`,                                       `(BAC2)`

where

> `R_A(K)=`
> ` floor((K+sqrt(K^2+8V_0S/(lambda+1)))/2)`.            `(RAK)`

For `K=1` this recovers the one-hole A-witness cap.

## 3. U-witness side: q pays for the near-clique

For a U-witness the hole set has size at most `K`, so inside `W_U`

> `d_{overline{G[W_U]}}(w_i)<=K`.                       `(BUdeg)`

Hence

> `e(G[W_U])`
> ` >= binom(d_U,2)-K d_U/2`
> ` = d_U(d_U-K-1)/2`.                                   `(BUedge)`

Again take the positive part when the quadratic expression is negative.

Since `G[W_U] subseteq G[U]`,

> `q>=d_U(d_U-K-1)/2`.                                  `(BUQ)`

The beta-sensitive U-edge cap is

`q<=Q_beta:=au-B_beta+N_1`.

Therefore:

### Theorem 3.1 — bounded-hole U-witness capacity

> `d_U<=R_U(K)`,                                         `(BUC)`

where

> `R_U(K)=`
> ` floor(((K+1)+sqrt((K+1)^2+8Q_beta))/2)`.             `(RUK)`

For `K=1` this is exactly the one-hole U-witness bound.

## 4. Global bounded-hole fan cap

Adding the two witness types gives the main finite theorem.

### Theorem 4.1 — bounded-hole fan capacity

Every A/U fan satisfying `(BH)` obeys

> `d <= R_A(K)+R_U(K)`.                                  `(BHFC)`

There are only two reservoirs for a uniformly low-hole fan:

- same-code A-edge/slack capacity;
- U-edge capacity, itself reduced by beta traffic.

No third witness type exists.

This is a direct finite reduction from local fan geometry to the two global budgets `S=E_U+L_A` and `Q_beta`.

## 5. Quadratic internal-edge floor

The two lower bounds also give a compact type-free consequence.

From `(BAedge)` and `(BUedge)`,

`e(G[A_bar(c(x))])+q`

` >= [d_A(d_A-K)+d_U(d_U-K-1)]/2`.

Since

`d_A^2+d_U^2>=d^2/2`

and

`K d_A+(K+1)d_U <= (K+1)d`,

we obtain:

> `e(G[A_bar(c(x))])+q`
> ` >= d^2/4-(K+1)d/2`.                                 `(BHED)`

Use the positive part if the right side is negative.

Thus for fixed `K`, every linear bounded-hole fan creates `Omega(p^2)` internal edge mass either in one same-code A-class or in U.

## 6. Bounded-hole Hamming localization

The general fan stability theorem can be specialized without any Markov loss, because every `g_i<=K`.

Put

`G_x=sum_i g_i<=Kd`.

Take `tau=K` in `(BST)/(EXC)`. There are no high-hole indices, so all but at most

> `R_K(d):=floor((1+sqrt(1+12Kd))/2)`                    `(BHEX)`

heads satisfy

> `t_i<=K`,
>
> `dist_H(c(h_i),c(x))<=K`.                              `(BHLOC)`

For fixed `K` and linear `d`, only `O(sqrt(p))` heads escape a fixed-radius Hamming ball about the source code.

This is substantially stronger than the earlier `o(p)`-radius localization for a merely subquadratic total hole mass.

## 7. Asymptotic corollary

Suppose `d=Theta(p)` and `K=O(1)`.

If simultaneously

> `S=o(p^2)`

and

> `Q_beta=o(p^2)`,

then `(RAK)` and `(RUK)` give

`R_A(K)=o(p)`, `R_U(K)=o(p)`,

contradicting `(BHFC)`.

Therefore:

### Corollary 7.1 — bounded-hole linear fans need a quadratic budget

A linear fixed-`K` A/U fan forces at least one of

> `S=Omega(p^2)`,
>
> `Q_beta=Omega(p^2)`.                                   `(BHDICH)`

Equivalently, in a slice where both budgets are subquadratic, every rooted-transfer linear A/U fan must contain witnesses with unbounded hole count.

This is the first general reduction beyond the one-hole model.

## 8. Rooted-transfer use

If the rooted-transfer dichotomy forces an A/U fan of order

`d>=H/(2a)`, `H=(F_min-sigma_0a)_+`,

and the global parameters make

`R_A(K)+R_U(K)<H/(2a)`,

then that fan cannot satisfy `g_i<=K` for all witnesses. Hence some witness has

> `g_i>=K+1`.                                             `(BHGROW)`

Allowing `K` to grow slowly with `p` converts global budget information into a lower bound on the maximum local hole surplus.

The next step is to combine such forced large-hole witnesses with the exact identity

`g_i=epsilon_x+epsilon_{w_i}-(lambda+1)`

and the scorecard. A large hole can only come from large source slack, large witness slack, or both; repeated large-hole fans should therefore become directly expensive in `E_U+L_A`.

## 9. Scope

The mandatory `X_3` order-12, size-32 graph remains untouched because its canonical root has `u=0` and `F_min=0`.

The theorem is conditional on the live partial-Boolean near-full setup and a chosen A/U fan. It does not assert the false all-order 2019 conjecture or a complete eventual theorem.
