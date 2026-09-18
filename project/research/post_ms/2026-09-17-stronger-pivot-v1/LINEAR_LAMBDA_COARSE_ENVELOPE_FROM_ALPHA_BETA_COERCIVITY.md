# A coarse linear-`lambda` envelope from alpha-beta coercivity

**Status:** internal asymptotic necessary condition / candidate checkpoint, 18 September 2026. This note attacks the linearly imbalanced root regime left after the sublinear-`lambda` extension. It does **not** close that regime and does not assert an eventual second-extremal theorem.

## 1. Scaling regime

Consider above-`M(n)` near-full candidates with

`p->infinity`,

`u/p -> rho>0`,

`lambda/p -> theta>0`.

Write

`A=2+rho-theta`,

so

`a/p -> A`.

Necessarily `A>=0`; in the nondegenerate A-layer regime below we take `A>0`, hence

`theta<2+rho`.

The scorecard allowance has leading coefficient

`C=S_req-2=[c(rho,theta)+o(1)]p^2`,

where

> `c(rho,theta)=theta(1+rho)-theta^2/2`.                  `(LC1)`

The integrated positive-`lambda` master inequality `(IPM)` is

`w_T Phi_r(N_T)+H/2+sum_i m_i(m_i+1)`

`<=p u(p+1-lambda-u/2)+u h_alpha+2p q`

`  +max(p,C_beta)C`,

with

`C_beta=p(floor(u/2)+1)/(lambda+1)`.

We deliberately discard the nonnegative integrated-product term `w_T Phi_r(N_T)` here. The resulting envelope is therefore coarse but robust.

---

## 2. A universal lower bound for the Hamming/coercivity side

Put

`eta=H/p^3`.

Since `H<=p u^2`, asymptotically `0<=eta<=rho^2`. The coercivity lower bound `(MIC)` gives

`sum_i m_i(m_i+1)`

`>= [((rho-sqrt(eta))^2)/4+o(1)]p^3`.

Therefore

`H/2+sum_i m_i(m_i+1)`

`>= [ eta/2+(rho-sqrt(eta))^2/4+o(1)]p^3`.

The quadratic in `sqrt(eta)` is minimized at `sqrt(eta)=rho/3`, giving

> `H/2+sum_i m_i(m_i+1)`
> `>= [rho^2/6+o(1)]p^3`.                                `(LC2)`

This lower bound is independent of the detailed U-code imbalance.

---

## 3. Coarse upper bounds on alpha diversion and internal U edges

The preserved alpha-capacity theorem gives

`h_alpha<=mu_alpha a`.

Trivially `mu_alpha<=p`, hence

> `h_alpha <= p a=[A+o(1)]p^2`.                          `(LC3)`

The preserved U-edge capacity theorem gives

`q <= a floor((mu_alpha+1)a/p)`.

Again using `mu_alpha<=p`,

> `q <= [A^2+o(1)]p^2`.                                  `(LC4)`

These estimates are intentionally crude; they do not use the stronger high-complexity information available when the scorecard is smaller.

Also

`max(p,C_beta)/p -> g(rho,theta)`,

where

> `g(rho,theta)=max(1,rho/(2theta))`.                     `(LC5)`

---

## 4. Linear-imbalance master envelope

Divide `(IPM)` by `p^3`, use `(LC1)--(LC5)`, and drop `w_T Phi_r(N_T)>=0`. Every such limiting pair `(rho,theta)` must satisfy

> **LINEAR-LAMBDA ENVELOPE**
>
> `rho^2/6`
>
> `<= rho(1-theta-rho/2)`
>
> `   +rho A+2A^2`
>
> `   +g(rho,theta)c(rho,theta)`,                         `(LCE)`

where `A=2+rho-theta`.

This is the first explicit asymptotic semialgebraic restriction obtained from the new alpha--beta coercivity theorem in the genuinely linear-`lambda` regime.

---

## 5. Explicit upper envelope when the A-layer is small

Suppose

`rho in [27/14,2]`.

If

`theta >= 2+rho(1-1/sqrt(2))`,                            `(HR)`

then

`A<=rho/sqrt(2)`,

so `2A^2<=rho^2`. Also `(HR)` implies `theta>rho/2`, hence `g=1`.

In this range `(LCE)` reduces exactly to

> `14rho^2-30rho theta+66rho+9theta^2-42theta+48 >= 0`.   `(LCP)`

As a quadratic in `theta`, its roots are

> `theta_-(rho)=(5rho+7-sqrt(11rho^2+4rho+1))/3`,
>
> `theta_+(rho)=(5rho+7+sqrt(11rho^2+4rho+1))/3`.

The upper root satisfies `theta_+(rho)>2+rho`, outside the admissible A-layer range. Moreover, on `rho in [27/14,2]`, the lower root lies above the threshold `(HR)`. Hence every candidate in this ratio window must obey

> `theta <= theta_-(rho)`.                                `(LTE)`

Numerically,

- at `rho=27/14`, `theta_-(rho)=3.19939...`;
- at `rho=2`, `theta_-(rho)=(17-sqrt(53))/3=3.23996...`.

A simple rational corollary is

> `theta < 13/4`                                          `(L13)`

throughout `rho in [27/14,2]`.

Indeed at `theta=13/4`, the left-minus-right margin of `(LCE)` in the high-imbalance regime is

`7(32rho^2-72rho+15)/96`,

which is negative throughout `[27/14,2]`; the same quadratic remains decreasing in `theta` all the way to the admissible endpoint `2+rho`.

---

## 6. Combined scale reduction

Together with `SUBLINEAR_LAMBDA_EXTENSION_OF_SOURCE_TUPLE_RATIO_GAP.md`, this produces a useful two-sided reduction for any putative sequence with

`u/p -> rho in [27/14,2]`.

Such a sequence cannot have `lambda=o(p)`. After passing to a subsequence it must therefore have

`lambda/p -> theta>0`,

and the new coercivity envelope then requires

> `0 < theta <= theta_-(rho) < 13/4`.                    `(SCALE)`

Thus the large-unmatched-ratio survivor has been moved from an unrestricted positive-imbalance problem into an explicit compact `(rho,theta)` region.

This is not yet a contradiction. The deliberately discarded integrated-product term `w_T Phi_r(N_T)` is the most obvious source of further shrinkage: `(LCE)` uses the alpha--beta coercivity but none of the finite-deficit source-tuple scarcity which was built into `(IPM)` precisely for this purpose.

---

## 7. Trust boundary

- `(LC2)` is the exact minimization of the preserved Hamming/coercivity lower bound.
- `(LC3)` uses only `h_alpha<=mu_alpha a` and the trivial `mu_alpha<=p`.
- `(LC4)` uses the preserved U-edge capacity theorem and `mu_alpha<=p`.
- `(LCE)` is an asymptotic necessary condition obtained by dropping a nonnegative term from `(IPM)`; it cannot overstate an exclusion.
- `(LTE)` is only asserted for `rho in [27/14,2]` and the stated high-imbalance reduction; the threshold comparison has been separately regression-checked.
- No claim is made that all remaining `(rho,theta)` are realizable.
- The full-tight `X_3` graph has `u=0` and is unaffected.
