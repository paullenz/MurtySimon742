# Enhanced alpha-beta coercivity, continuum source profile, and same-code clique slack

**Status:** internal structural lemmas / asymptotic necessary conditions, 18 September 2026. These results belong to the near-full partial-Boolean branch. They do **not** assert an eventual second-extremal theorem. The published order-12, size-32 `X_3` graph has `u=0` and is untouched.

## 1. Setup

Use the live notation from `CURRENT_STATE.md` and `ALPHA_BETA_COERCIVITY_INTEGRATED_PRODUCT_AND_CYLINDER.md`.

There are `p` tight fibres and `u` unmatched vertices. For fibre `i`, write

- `u_i^0+u_i^1=u`;
- `d_i=u_i^0-u_i^1`;
- `m_i=min(u_i^0,u_i^1)=(u-|d_i|)/2`;
- `h_i=h_i^0+h_i^1` for the number of alpha-oriented P--U sources in that fibre;
- `r_i^s=u_i^s-h_i^s`;
- `e_i^0+e_i^1=lambda+1` for the endpoint slacks;
- `P_i=h_i^0(u_i^1+1)+h_i^1(u_i^0+1)`;
- `T_i=r_i^0 e_i^1+r_i^1 e_i^0`.

Put

`H=sum_i d_i^2`,

`h_alpha=sum_i h_i`,

`P_alpha=sum_i P_i`.

For `lambda>=0`, the preserved endpoint-slack theorem gives

`sum_i T_i<=p L_A`.

The preserved directional budget is

`J+H/2+P_alpha`

`<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.

The scorecard bound for an above-`M(n)` candidate is

`E_U+L_A<=C_0:=S_req-2`.

---

# Part I. Alpha overflow cannot hide inside the old coercivity bound

## 2. Exact strengthened fibre coercivity

The earlier proof used

`P_i >= (m_i+1)h_i`

and

`T_i >= (lambda+1)(m_i-h_i)_+`.

Keeping the excess alpha term instead of discarding it gives the following.

### Theorem 2.1 (enhanced fibre coercivity)

For every fibre and every `lambda>=0`,

> `P_i + ((m_i+1)/(lambda+1)) T_i`
>
> `>= (m_i+1) max(m_i,h_i)`
>
> `= m_i(m_i+1)+(m_i+1)(h_i-m_i)_+`.                    `(EABF)`

### Proof

If `h_i<=m_i`, the two preserved lower bounds give

`P_i+((m_i+1)/(lambda+1))T_i`

`>=(m_i+1)h_i+(m_i+1)(m_i-h_i)=m_i(m_i+1)`.

If `h_i>=m_i`, then `T_i>=0` and

`P_i>=(m_i+1)h_i`.

These are exactly the two branches of `(EABF)`.

### Corollary 2.2 (enhanced global coercivity)

Put

`X_alpha=sum_i (m_i+1)(h_i-m_i)_+`.

Then

> `P_alpha+[p(floor(u/2)+1)/(lambda+1)]L_A`
>
> `>=sum_i m_i(m_i+1)+X_alpha`.                           `(EABG)`

Thus the old `(ABG)` was sharp only when no fibre carries alpha mass beyond its minority-side population.

---

## 3. Exact Hamming-sensitive lower bound for the overflow term

The term `X_alpha` can itself be bounded from the global Hamming imbalance.

Put

`Y=sum_i(h_i-m_i)_+`.

Since `|d_i|<=u`,

`d_i^2<=u|d_i|`,

hence

`sum_i |d_i|>=H/u`.

Because

`sum_i m_i=(pu-sum_i|d_i|)/2`,

we get

> `Y >= [h_alpha-pu/2+H/(2u)]_+`.                         `(EO1)`

Now fix any integer `t` with

`0<=t<u/2`.

If `m_i<t`, then

`|d_i|=u-2m_i>u-2t`.

Therefore the number of such fibres is at most

`H/(u-2t)^2`.

Also `(h_i-m_i)_+<=h_i<=u`. Hence at most

`uH/(u-2t)^2`

units of the `Y`-mass can lie on fibres with `m_i<t`. Every remaining unit is multiplied in `X_alpha` by at least `t+1`. Therefore:

### Theorem 3.1 (alpha-overflow/Hamming payment)

For every integer `0<=t<u/2`,

> `X_alpha`
>
> `>=(t+1)[h_alpha-pu/2+H/(2u)-uH/(u-2t)^2]_+`.          `(AOH)`

This is exact and finite. It is useful precisely when an attempted linear-scale extremizer tries to erase beta load by pushing too much P--U traffic into alpha orientations.

Combining `(EABG)` with the directional budget gives the strengthened positive-`lambda` master obtained from the old `(IPM)` simply by adding `X_alpha` to its left side.

---

# Part II. High root imbalance forces a nonzero beta floor

## 4. Exact beta-load floor from the A-layer size

Let

`B_beta=sum_x ell_x=pu-h_alpha`.

The preserved alpha-capacity bound gives

`h_alpha<=mu_alpha a<=pa`.

Since

`a=2p+u-lambda-1`,

we obtain:

### Lemma 4.1 (root-imbalance beta floor)

> `B_beta >= p(lambda+1-2p)_+`.                           `(RBF)`

In particular, once `lambda>2p-1`, a positive linear fraction of all P--U obligations must be beta-oriented regardless of how favourable the alpha classes are.

The threshold count in the integrated product can therefore be made alpha-free in this regime. If

`j=min(p,floor(H/T^2))<p`,

then the old definition

`N_T=ceil((B_beta-aj)_+/(p-j))`

implies

> `N_T >= ceil((p(lambda+1-2p)-aj)_+/(p-j))`.             `(RBN)`

This is the key finite bridge into the genuinely linear `lambda` regime.

---

# Part III. Continuum limit of the complete source-deficit staircase

## 5. Asymptotic profile of `Phi_r`

Fix an integer `r>=3`. Recall

`C_hat_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`

and

`Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`.

Assume

`u/p -> rho>0`,

`N/p -> nu>=0`.

For `0<kappa<1`, define

> `c_{r,rho}(kappa)= [kappa/r] [rho/(1-kappa)]^r`.        `(CP1)`

Then ordinary Riemann-sum convergence gives:

### Theorem 5.1 (continuum source-deficit profile)

> `Phi_r(N)/p^2 -> phi_r(nu;rho)`,                        `(CSP)`

where

> `phi_r(nu;rho)=int_0^1 [nu-c_{r,rho}(kappa)]_+ d kappa`. `(CP2)`

### Proof sketch

For `K/p->kappa` in every compact subinterval of `(0,1)`,

`C_hat_r(K)/p -> c_{r,rho}(kappa)`.

The floor changes each summand by at most one. For finite `nu`, the positive part vanishes uniformly near `kappa=1` because `c_{r,rho}(kappa)->infinity`. The remaining compact interval is an ordinary Riemann sum. The total floor error is `O(p)`, negligible after division by `p^2`.

### Explicit triple-source form

For `r=3`,

`c_{3,rho}(kappa)=kappa rho^3/[3(1-kappa)^3]`.

For `nu>0`, let `kappa_*` be the unique solution of

`nu=kappa_* rho^3/[3(1-kappa_*)^3]`.

Then

> `phi_3(nu;rho)`
>
> `=nu kappa_* -(rho^3/3)`
>
> ` * [1/(2(1-kappa_*)^2)-1/(1-kappa_*)+1/2]`.           `(CP3)`

This turns the previously discrete source-tuple staircase into an explicit continuous penalty.

---

## 6. Strengthened linear-scale variational master

Assume now

`u/p->rho>0`,

`lambda/p->theta>0`,

`a/p->A=2+rho-theta>0`,

`H/p^3->eta`,

`h_alpha/p^2->alpha`,

`q/p^2->xi`.

Put

`c(rho,theta)=theta(1+rho)-theta^2/2`,

`g(rho,theta)=max(1,rho/(2theta))`.

The basic coercivity/Hamming term has the exact lower envelope

`eta/2+(rho-sqrt(eta))^2/4`.

For the alpha overflow, `(AOH)` gives the asymptotic lower bound

> `Omega(rho,eta,alpha)`
>
> `=sup_{0<s<rho/2}`
>
> ` s[alpha-rho/2+eta/(2rho)-rho eta/(rho-2s)^2]_+`.      `(AOP)`

Fix any real threshold `tau` with

`sqrt(eta)<tau<rho`.

Then

`j/p -> x=eta/tau^2<1`.

Using the actual beta density `beta=rho-alpha`,

`N_T/p -> nu=[beta-Ax]_+/(1-x)`.

Therefore `(IPM)` plus `(EABG)` and Theorem 5.1 gives the following necessary condition for every fixed `r>=3` and every admissible `tau`:

### Theorem 6.1 (continuum enhanced IPM)

> `((rho-tau)/2) phi_r(nu;rho)`
>
> ` + eta/2 + (rho-sqrt(eta))^2/4`
>
> ` + Omega(rho,eta,alpha)`
>
> `<= rho(1-theta-rho/2)+rho alpha+2xi`
>
> `   +g(rho,theta)c(rho,theta)`.                         `(CEIPM)`

The old coarse linear envelope `(LCE)` follows by dropping the nonnegative source-profile and alpha-overflow terms and using `alpha<=A`, `xi<=A^2`.

### Corollary 6.2 (alpha-free high-imbalance source profile)

If `theta>2`, Lemma 4.1 gives the asymptotic beta floor

`beta>=theta-2`.

Hence in `(CEIPM)` one may replace `nu` by the smaller alpha-free quantity

> `nu_0=[theta-2-Ax]_+/(1-x)`.                            `(HSP)`

Since `phi_r` is increasing in `nu`, this remains a valid lower bound.

Thus the integrated source term cannot be erased by taking `h_alpha` large once the root imbalance crosses `2p`.

---

## 7. The coarse `rho^2/6` envelope is strictly non-sharp in a broad high-`theta` region

The old Hamming/coercivity expression can be written exactly as

> `eta/2+(rho-sqrt(eta))^2/4`
>
> `=rho^2/6 +(3/4)(sqrt(eta)-rho/3)^2`.                  `(SQ)`

Its unique minimizer is therefore

`eta=rho^2/9`.

At that minimizer choose `tau=2rho/3`. Then `x=1/4`, and the alpha-free beta floor gives

> `nu_0=(5theta-10-rho)/3`.                               `(MINNU)`

Hence `nu_0>0` whenever

> `theta>2+rho/5`.                                        `(STRICT)`

At the unique point where the old lower bound equals `rho^2/6`, the integrated source-profile term is therefore strictly positive throughout `(STRICT)`.

By continuity and the strict quadratic growth in `(SQ)`, this yields:

### Corollary 7.1 (strict improvement over the coarse linear envelope)

Fix a compact parameter set with

`rho>=rho_0>0`,

`A=2+rho-theta>=A_0>0`,

`theta>=2+rho/5+delta`

for some `delta>0`.

Then there is an `epsilon=epsilon(rho_0,A_0,delta)>0` such that every limiting above-threshold candidate in that compact set satisfies the stronger left-side estimate

> `integrated/coercive LHS >= rho^2/6+epsilon`.

Thus `(LCE)` is uniformly non-sharp on every compact subset of this region. The next numerical envelope should optimize `(CEIPM)`, not `(LCE)`.

No explicit optimized replacement for `13/4` is claimed here.

---

# Part IV. Same-code cliques pay globally into the scorecard

## 8. Global same-code clique slack theorem

The earlier cylinder-criticality note showed that every same-code A-edge has a complementary-code critical witness and that the associated unique-common-neighbour pair satisfies

`epsilon_source+epsilon_witness>=lambda+1`.

For a clique, these local payments can be summed without losing all multiplicity information.

### Theorem 8.1 (same-code clique scorecard payment)

Assume `lambda>=0`. Let `K subseteq A` be a clique of order `r>=2` whose vertices all have the same Boolean code. Then

> `E_U+L_A >= ceil(r(lambda+1)/2)`.                        `(SCC)`

### Proof

Choose one critical orientation for every edge of `K`, as in the preserved same-code localisation lemma. This orients the complete graph on `K` as a tournament. For each oriented edge `x->z`, choose a complementary-code witness `w` with

`N(x) cap N(w)={z}`.

A fixed witness cannot certify two oriented edges with different heads. Indeed, if it certified both `x->z` and `x'->z'` with `z!=z'`, then `w` is adjacent to `z'`, while `x` is adjacent to `z'` because `K` is a clique. This would give a second member `z'` of `N(x) cap N(w)`, contradiction.

Hence every witness appears on at most `r-1` oriented edges. Every clique vertex appears as a source on at most `r-1` edges as well.

Summing `epsilon_x+epsilon_w>=lambda+1` over all `binom(r,2)` oriented clique edges gives

`binom(r,2)(lambda+1)`

`<=sum_x outdeg(x)epsilon_x + sum_w mult(w)epsilon_w`

`<=(r-1)(sum_{x in K}epsilon_x+sum_{w in W}epsilon_w)`

`<=(r-1)(E_U+L_A)`.

Divide by `r-1` and use integrality.

### Corollary 8.2 (scorecard clique cap)

In an above-`M(n)` candidate,

> `omega_same-code(A)`
>
> `<= max(1,floor(2C_0/(lambda+1)))`,                    `(SCCAP)`

where `C_0=S_req-2`.

This is a global cap on the clique side of every beta-cylinder repeated code class.

---

## 9. Common-foot concentration must create holes once the clique cap is active

Return to an incoming cylinder group `S_w` of size `t`, with one common complementary witness `w`. Put

`h_z=epsilon_z+epsilon_w-(lambda+1)`

and

`H_w=sum_{z in S_w}h_z`.

The preserved common-foot estimate gives

`omega(G[S_w])>=ceil(t^2/(t+H_w))`.

Let

`R_C=max(1,floor(2C_0/(lambda+1)))`.

By `(SCCAP)`, `omega(G[S_w])<=R_C`. Therefore:

### Corollary 9.1 (quadratic common-foot hole payment)

> `H_w >= t^2/R_C-t`.                                    `(CFQ)`

Thus one complementary witness cannot absorb an arbitrarily large incoming same-code cylinder block while remaining in the low-hole regime. Once its reuse exceeds the global same-code clique cap, the accumulated unique-common-neighbour hole excess must grow quadratically.

There is also a simple bound on the number of distinct incoming feet. If `g` different witnesses are used, choose one source from each group. The chosen sources have code `c`, the witnesses have code `bar c`, so all `2g` vertices are distinct. The `g` unique-common-neighbour inequalities are therefore disjoint in the scorecard and give

> `g(lambda+1)<=E_U+L_A<=C_0`.                            `(CFG)`

Hence

> `g<=floor(C_0/(lambda+1))`.                             `(CFGCAP)`

The cylinder star now has a genuine two-level capacity structure: only `O(C_0/(lambda+1))` incoming feet are available, and overloading any one of them creates the quadratic hole payment `(CFQ)`.

---

## 10. Strategic consequence

This checkpoint advances both live near-full routes.

1. **Linear root imbalance.** The discrete source-tuple staircase has an explicit continuum limit, and when `lambda>2p` a nonzero beta floor is forced before any optimization. The coarse `(rho,theta)` envelope is therefore provably non-sharp on the broad region `theta>2+rho/5`; future optimization should use `(CEIPM)` rather than merely adjusting `(LCE)`.

2. **Cylinder criticality.** Same-code cliques now pay directly into the global scorecard, not merely into another complementary near-clique. Concentrated incoming-foot reuse is consequently bounded by `(CFQ)/(CFGCAP)`.

3. **Alpha diversion.** Attempting to suppress beta load by excessive alpha orientation creates the new Hamming-sensitive payment `(AOH)`, which enters the same master inequality.

The next high-value step is to combine `(SCC)/(CFQ)` with the cylinder multiplicity `ceil((p-epsilon_x)_+/2^{k_x})` across many low-deficit centres, while separately optimizing the explicit continuum inequality `(CEIPM)` on the remaining linear-`lambda` parameter region.

## 11. Trust boundary

- `(EABF)--(AOH)` are finite hand inequalities.
- `(RBF)/(RBN)` are exact consequences of the preserved alpha-capacity theorem and `a=2p+u-lambda-1`.
- `(CSP)` is a standard Riemann-limit statement for the already proved finite staircase `(IST)`; it is not a computational extrapolation.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- Corollary 7.1 asserts a strict uniform improvement on compact subsets; it deliberately does not claim an optimized numerical replacement for the old `13/4` bound.
- `(SCC)` is a hand multiplicity count over D2C critical witnesses.
- The `X_3` negative control has `u=0` and is untouched.
