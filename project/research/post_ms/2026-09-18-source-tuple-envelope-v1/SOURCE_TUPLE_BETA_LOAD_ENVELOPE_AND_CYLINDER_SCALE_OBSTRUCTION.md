# Source-tuple beta-load envelope and cylinder-scale obstruction

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal structural theorem package / strategic correction. The finite statements below are hand consequences of the already-preserved selected source-tuple hierarchy, beta-load identity, switching/Hall alpha capacity, and repaired cylinder theorem. The asymptotic corollaries are necessary conditions only. No eventual second-extremal theorem is claimed.

The published 2024 order-12, size-32 `X_3` graph is untouched: it has `u=0` and does not enter the unmatched-layer arguments below.

---

## 1. Why this checkpoint changes the local strategy

The preceding live state proposed to lower-bound the left side of the distribution-free complete-cylinder inequality `(DCF)` from the beta-deficit/source-tuple distribution.

That is not the right main move.

The same source-tuple hierarchy that constrains low beta deficits also shows that, when `u=O(p)` and `a=O(p)`, the **entire cylinder lower-bound expression itself is only `O(p)`**. By contrast the distribution-free matched-foot term `a R_A(C_0)` is superlinear whenever `a=Theta(p)` and `C_0 -> infinity` (and is `Theta(p^2)` in the genuine linear-scorecard regime).

So `(FDPr)+(CY3)+(DCF)` alone cannot close the main asymptotic branch by a scale contradiction. A useful new local theorem would have to sharpen the right side of `(DCF)` to the same linear scale, or add genuinely new D2C structure. The higher-value use of `(FDPr)` is instead to constrain the **total beta load** directly.

The rest of this note makes both statements precise.

---

## 2. Exact threshold count and beta-load upper bound

Retain the live notation. For `x in A`,

`ell_x=|I_x|`, `k_x=p-ell_x`,

and put

`B_beta=sum_{x in A} ell_x = pu-h_alpha`.

For an integer `K` with `0<=K<=p-r`, define

`N_K=|{x in A:k_x<=K}|`.

The preserved source-tuple theorem says, for every fixed integer `r>=3`,

`sum_x binom(ell_x,r)/(p-ell_x+r) <= (1/r) binom(u,r)`.

Its threshold consequence is

> `N_K <= U_r(K)`,                                        `(ST1)`
>
> `U_r(K):=floor( ((K+r)/r) * binom(u,r)/binom(p-K,r) )`.

Now separate the vertices according to `k_x<=K`. A vertex in that set has `ell_x<=p`; a vertex outside has `ell_x<=p-K-1`. Hence

`B_beta <= N_K p+(a-N_K)(p-K-1)`

`       = a(p-K-1)+(K+1)N_K`.

Using `(ST1)` gives:

### Theorem 2.1 (finite source-tuple beta-load cap)

For every `r>=3` and every `0<=K<=p-r`,

> `B_beta`
> `<= a(p-K-1)+(K+1)U_r(K)`.                             `(STB)`

This is exact and finite. It is stronger than viewing `(FDPr)` only as a scarcity theorem for individual low-deficit witnesses: it caps the *total* beta traffic.

Equivalently, every attempted beta density must satisfy all of the inequalities `(STB)` simultaneously.

---

## 3. Switching/Hall lower bound and the beta-load sandwich

Above the comparison threshold, the preserved switching theorem gives

`mu_alpha<=R_*`,

where

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`.

Trivially `mu_alpha<=p`; put

`R_hat=min(p,R_*)`.

The alpha capacity is

`h_alpha<=mu_alpha a<=R_hat a`.

Since `B_beta=pu-h_alpha`, we obtain:

> `B_beta >= [pu-R_hat a]_+`.                             `(STL)`

When `R_hat=p`, this is exactly the earlier root-imbalance beta floor

`B_beta>=p(lambda+1-2p)_+`.

Combining `(STL)` and `(STB)` gives the compact parameter-only theorem:

### Theorem 3.1 (source-tuple / switching beta sandwich)

Every above-`M(n)` partial-Boolean candidate with `lambda>=0` satisfies, for every `r>=3` and `0<=K<=p-r`,

> `[pu-R_hat a]_+`
> `<= a(p-K-1)+(K+1)U_r(K)`.                             `(STS)`

No Hamming-energy variable, alpha distribution, code distribution, or cylinder witness variable appears in `(STS)`.

This is a useful independent necessary condition alongside `(CEIPM)`: switching limits how much P--U traffic can hide in alpha classes, while the source-tuple hierarchy limits how much of the remainder can be beta traffic.

---

## 4. Continuum beta envelope

Assume a sequence with

`u/p -> rho>0`,

`lambda/p -> theta>=0`,

`a/p -> A=2+rho-theta>0`.

Fix `r>=3` and choose `K/p->kappa` with `0<kappa<1`. From `(STB)`,

> `beta:=limsup B_beta/p^2`
> `<= F_r(kappa;rho,theta)`,                              `(CBE)`
>
> `F_r(kappa;rho,theta)`
> `= A(1-kappa)+(kappa^2/r)(rho/(1-kappa))^r`.

Thus

> `beta <= inf_{0<kappa<1} F_r(kappa;rho,theta)`          `(CBE*)`

for every fixed `r>=3`.

If additionally `C_0/p^2 -> c>=0`, then

`R_hat/p -> min(1,sqrt(c))`

(up to the irrelevant vanishing integer error), and `(STL)` gives

> `beta >= [rho-A min(1,sqrt(c))]_+`.                    `(CBL)`

Hence the source-tuple/switching sandwich has the asymptotic parameter-only form

> `[rho-A min(1,sqrt(c))]_+`
> `<= inf_kappa F_r(kappa;rho,theta)`.                    `(CSTS)`

For an above-threshold linear-scale sequence,

`c=theta(1+rho)-theta^2/2`.

The earlier root-imbalance floor is the branch where the `min` equals one:

`beta >= (theta-2)_+`.

---

## 5. A clean finite high-imbalance exclusion

The total-load form of the source-tuple theorem already improves the old coarse linear-`lambda` envelope without any continuum optimization.

### Theorem 5.1

Assume the partial-Boolean selected framework, `p>=10`, and

`u<=2p`.

Then

> `lambda <= 3p-1`.                                      `(3P)`

This statement does not require `m>M(n)`; it is a structural consequence of the selected source-tuple system itself.

### Proof

Suppose `lambda>=3p`. The root-imbalance floor gives

`B_beta>=p(lambda+1-2p)>=p(p+1)`.                        `(5.1)`

Use `(STB)` with `r=3`, `K=1`. Then

`N_1<=U_3(1)`

with

`U_3(1)=floor((4/3) binom(u,3)/binom(p-1,3))`.

Since `u<=2p`,

`U_3(1)<=floor((4/3) binom(2p,3)/binom(p-1,3))`.

For `p>=10`,

`(4/3) binom(2p,3)/binom(p-1,3) < 2p-1`,                `(5.2)`

because the difference is

`(2p-1)(3p^2-31p+18)/(3(p-3)(p-2))>0`.

Thus `U_3(1)<=2p-2`.

Also

`a=2p+u-lambda-1<=p-1`.

Therefore `(STB)` gives

`B_beta<=a(p-2)+2U_3(1)`

`      <=(p-1)(p-2)+4p-4`

`      =p^2+p-2`,

contradicting `(5.1)`.

So `(3P)` follows.

This is a finite, externally checkable replacement for the much weaker old coarse `theta<13/4` discussion on the `u<=2p` slice.

---

## 6. A hand-certifiable asymptotic improvement below `3`

The continuum envelope gives a little more while keeping the proof elementary.

Assume

`0<rho<=2`,

`theta>2`.

Take `r=3` and `kappa=1/9`. Since `A=2+rho-theta<=4-theta`, `(CBE)` and the root-imbalance lower bound give

`theta-2`

`<= (8/9)(4-theta)+(1/243)(2/(8/9))^3`

`= (8/9)(4-theta)+3/64`.

Solving gives

> `theta <= 3227/1088 = 2.965992647...`.                 `(RTH)`

Therefore:

### Corollary 6.1

For every above-threshold partial-Boolean sequence with

`u/p -> rho in (0,2]`,

`lambda/p -> theta>2`,

one has

> `theta <= 3227/1088`.

This is deliberately a short rational bound rather than a numerically optimized decimal. Optimizing `kappa` in `(CBE*)` for `r=3` improves the endpoint only slightly (to about `2.96597` at `rho=2`), so the rational form is preferable for review.

---

## 7. The cylinder-scale obstruction

We now return to the proposed `(DCF)` bridge and show why it cannot be the main asymptotic closure using only the existing source-tuple information.

Assume

`u<=C p`, `a<=D p`

for fixed constants `C,D`, and let

`N_K=|{x:k_x<=K}|`.

For `0<=K<=p/2-3`, `(ST1)` with `r=3` gives

`N_K`

`<=((K+3)/3) binom(u,3)/binom(p-K,3)`

`<= (8C^3/3)(K+3)`                                      `(7.1)`

for all sufficiently large `p`.

Put

`Z=sum_x 2^{-k_x}`.

The exact layer-cake identity is

> `Z=sum_{K>=0} N_K/2^{K+1}`.                            `(7.2)`

Using `(7.1)` through `p/2-3` and `N_K<=a` thereafter,

`Z <= (8C^3/3) sum_{K>=0}(K+3)/2^{K+1}+o(1)`

`  <= 32C^3/3+o(1)`.                                     `(7.3)`

Now the repaired cylinder expression for any family of centres is at most its value on all A-vertices with zero slack:

`Gamma=sum_x ceil((p-epsilon_x)_+/2^{k_x})`

`     <=sum_x ceil(p/2^{k_x})`

`     <=pZ+a`.

Hence:

### Theorem 7.1 (source-tuple cylinder-scale obstruction)

If `u=O(p)` and `a=O(p)`, then

> `Gamma=O(p)`.                                          `(CSO)`

In particular, the source-tuple hierarchy itself prevents the cylinder lower-bound expression from becoming quadratic.

But the distribution-free right side of `(DCF)` contains

`a R_A(C_0)`.

If `a=Theta(p)` and `C_0 -> infinity`, this term is already `omega(p)`; if `C_0=Theta(p^2)`, it is `Theta(p^2)`.

Therefore:

> **Strategic obstruction.** The programme “use `(FDPr)` to force the `(DCF)` left side above its current parameter-only right side” cannot close the generic `u=O(p)` branch on scale alone. Existing `(FDPr)` actually shows the opposite scale separation.

This does **not** invalidate `(DCF)`. It identifies its correct role: an equality/stability or finite-subcase tool unless the matched-foot/AU upper bound is sharpened to linear scale using additional D2C structure.

---

## 8. Strategic consequence

The highest-value next move is no longer a generic layer-cake lower bound for `(DCF)`.

The source-tuple hierarchy should instead be used through the new total-load sandwich `(STS)/(CSTS)` and then coupled to the stronger global constraints:

1. `(CEIPM)` / alpha-beta coercivity and Hamming energy;
2. complementary-pair payment `(CPP-P)` when traffic localizes;
3. a future **linear-scale** matched-foot/AU capacity theorem if one can be proved.

The clean immediate frontier is the linear-`lambda` parameter region left after `(CSTS)` and `(CEIPM)`. A particularly useful question is whether their equality conditions are compatible: `(CSTS)` wants beta traffic spread away from very small deficits, while `(CEIPM)` penalizes the resulting deficit/U-degree product and alpha overflow.

That coupling has a plausible route to a compact externally reviewable theorem. By contrast, further optimization of the current distribution-free cylinder cap is not the best use of effort until its scale mismatch is repaired.

The separate `Q=0` / false-twin-core branch remains open.

---

## 9. Trust boundary

- `(STB)` is an exact algebraic consequence of the preserved source-tuple count `(FDPr)`.
- `(STL)` uses only `B_beta=pu-h_alpha`, `h_alpha<=mu_alpha a`, and the preserved switching/Hall cap `mu_alpha<=R_*` above threshold.
- `(3P)` is a finite hand corollary; no asymptotics or computation are needed.
- `(CBE)--(RTH)` are asymptotic necessary conditions obtained from the exact finite theorem.
- `(CSO)` is a scale theorem about the *cylinder expression itself*, not a D2C exclusion theorem.
- The audit script associated with this note checks arithmetic consequences only; it does not replace the source-tuple or selected-witness proofs.
- The 12/32 `X_3` graph has `u=0` and is untouched.
- No all-order or eventual second-extremal claim is made.