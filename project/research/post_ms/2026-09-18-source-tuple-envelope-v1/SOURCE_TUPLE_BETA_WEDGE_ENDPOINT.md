# Source-tuple beta wedge and endpoint exclusion

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal asymptotic structural corollary. This is a short consequence of the exact beta-load cap `(STB)`, the root-imbalance beta floor `(RBF)`, and finite-deficit source-tuple scarcity. It does not use the second-extremal scorecard and does not claim an eventual D2C theorem.

The 12/32 `X_3` negative control has `u=0` and is untouched.

---

## 1. Linear scaling

Assume a partial-Boolean sequence with

`p -> infinity`,

`u/p -> rho>0`,

`lambda/p -> theta>2`,

and hence

`a/p -> A=2+rho-theta>0`.

Write

`B_beta=sum_x ell_x`,

`D_beta=sum_x k_x=ap-B_beta`.

The root-imbalance floor gives

`B_beta/p^2 >= theta-2+o(1)`.                            `(1.1)`

On the other hand, apply the exact source-tuple beta cap `(STB)` with any fixed deficit threshold `K` and `r=3`. Since `u=Theta(p)`, the source-tuple threshold count `U_3(K)=O_K(1)`. Therefore

`B_beta <= a(p-K-1)+O_K(1)`,

and after dividing by `p^2`,

`limsup B_beta/p^2 <= A`.                               `(1.2)`

Combining `(1.1)--(1.2)` gives

`theta-2 <= A=2+rho-theta`,

so

> `theta <= 2+rho/2`.                                    `(BW)`

Equivalently,

> `rho >= 2(theta-2)` whenever `theta>2`.

This is the simplest source-tuple beta wedge. It already cuts the admissible root-imbalance slope in half relative to the trivial positivity condition `theta<2+rho`.

---

## 2. Equality in the wedge is impossible

The boundary in `(BW)` cannot actually occur.

Suppose

`theta=2+rho/2`.

Then

`A=rho/2=theta-2`.

The lower and upper beta-density bounds therefore force

`B_beta=ap-o(p^2)`,

or equivalently

> `D_beta=sum_x k_x=o(p^2)`.                              `(2.1)`

Choose an integer sequence `K_p` with

`K_p -> infinity`,

`K_p=o(p)`,

`D_beta/K_p=o(p)`.

For example, when `D_beta>0`, take a harmless integer adjustment of `sqrt(D_beta)`; if necessary enlarge it slowly so that it tends to infinity.

By Markov,

`|{x:k_x>K_p}| <= D_beta/K_p=o(p)`.

Since `a=(A+o(1))p` with `A=rho/2>0`, this gives

> `N_{K_p}=|{x:k_x<=K_p}|=(A-o(1))p`.                    `(2.2)`

But the exact triple-source threshold bound gives, for `K_p=o(p)`,

`N_{K_p}`

`<=((K_p+3)/3) binom(u,3)/binom(p-K_p,3)`

`=((rho^3/3)+o(1))K_p`

`=o(p)`,                                                  `(2.3)`

contradicting `(2.2)`.

Hence:

### Theorem 2.1 (strict beta wedge)

Every convergent partial-Boolean sequence with `rho>0` and `theta>2` satisfies

> `theta < 2+rho/2`.                                     `(SBW)`

This endpoint exclusion uses no scorecard asymptotics. It is the same finite-deficit scarcity mechanism that previously killed the ratio-two polarization, now applied to the total beta-load boundary.

---

## 3. Relationship with the stronger rational cap

On the slice `rho<=2`, `(SBW)` gives `theta<3`.

The proportional-threshold beta envelope from the companion note is stronger there: choosing `r=3`, `kappa=1/9` yields

`theta<=3227/1088=2.965992647...`.

The point of `(SBW)` is different: it is a simple structural wedge valid for **every** finite positive `rho`, and it shows that the first beta-load boundary is not attainable.

---

## 4. Strategic consequence

A high-imbalance survivor cannot simultaneously have too little unmatched mass. In the linear regime, every increase of `theta` above two forces at least twice as much unmatched density:

`rho>2(theta-2)`.

This relation should be imposed before optimizing `(CEIPM)`. It removes an entire wedge of parameter space using only source-tuple scarcity and the root-imbalance beta floor, with no Hamming or alpha-distribution optimization.

The next useful coupling is therefore `(SBW)+(CSTS)+(CEIPM)`, not a return to the distribution-free cylinder bound.

---

## 5. Trust boundary

- `(BW)` follows from the exact source-tuple beta cap with fixed `K` and the preserved root-imbalance beta floor.
- The strict endpoint exclusion uses only `D_beta=ap-B_beta`, Markov, and the exact `r=3` threshold form of `(FDPr)`.
- No finite uniform gap below `2+rho/2` is claimed by `(SBW)`.
- The separate `Q=0` / false-twin-core branch remains open.
- `X_3` has `u=0` and is untouched.
- No all-order or eventual second-extremal theorem is claimed.