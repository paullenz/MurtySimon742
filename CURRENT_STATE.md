# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_SOURCE_TUPLE_BETA_ENVELOPE_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The previous proposed next move — force the parameter-only complete-cylinder inequality `(DCF)` from the beta-deficit distribution — has been critically reassessed and is **not** the best main route: the source-tuple hierarchy itself shows that the whole cylinder expression is only `O(p)` when `u,a=O(p)`, while the present distribution-free cylinder upper bound is generically superlinear. The higher-value use of the source-tuple hierarchy is now the new **total beta-load envelope / switching sandwich**, to be coupled with `(CEIPM)` and scorecard payment.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. It has `u=0`, so every unmatched-layer theorem below leaves it untouched.

## 2. Near-full normal form, rooted triangles, residual defect, and scorecard

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

Let the complete tight-antipode matching in `B` have `p` pairs and let `U` be the unmatched part, `u=|U|`, so `b=2p+u`. Every vertex of `A union U` chooses exactly one endpoint from every tight pair and has a Boolean code in `{0,1}^p`.

Put `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Then

> `a=2p+u-lambda-1`,
>
> `Q=e(G[B])=p(p+u-1)+q`,
>
> `r=(p+u)(a-p)+p-s-q`,
>
> `delta=b(n-b)-m=(p+u)(a-p)+p-s-q-f`.

For `epsilon_z=b-d(z)`, put

> `E_U=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,
>
> `L_A=sum_{x in A}epsilon_x=a(p+u)-s-2f`.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`.

Then

> `m<=M(n)` iff `E_U+L_A>=S_req`,

and parity gives

> `m>M(n) ==> E_U+L_A<=C_0:=S_req-2`.                    `(GS-A)`

At `lambda=-1`, `C_0=2p+u-4`.

The live branch is triangle-containing / partial-Boolean. The separate `Q=0` / false-twin-core branch remains open and must not be conflated with this one.

## 3. Preserved switching, Hall, sparse-U, and source-tuple machinery

A switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

Let `sigma_0` be the largest zero-signed subcore obtainable after switching. Above threshold,

> `sigma_0(sigma_0-1)<=C_0`.                              `(SD)`

With

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`,

one has

> `sigma_0<=R_*`,
>
> every unmatched row has `tau(Psi(K_y))>=ceil(p/(R_*+1))`,
>
> the largest projective alpha / switching true-twin class has `mu_alpha<=R_*`.

Preserved selected/Hall consequences include

> `nu_c t_c<=a`,
>
> `p(t_c+t_bar c)<=(mu_alpha+1)a`,
>
> `min(h,p)a>=pu-mu_alpha a`.

Selected orientation inside `U` gives

> `e(G[S])<=sum_{y in S}n_{bar c(y)}` for every `S subseteq U`,

hence

> `q<=a floor((mu_alpha+1)a/p)<=(mu_alpha+1)a^2/p`.       `(SU)`

For coordinate imbalance `d_i=u_i^0-u_i^1`, let `H=sum_i d_i^2`. For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x` beta deficit, and `d_x=d_U(x)`. Put

`J=sum_x(p-ell_x)(u-d_x)>=0`.

The directional budget is

> `J+H/2+P_alpha`
>
> `<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.           `(DHB)`

For every `r>=3`,

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`.   `(FDPr)`

The integrated finite-deficit staircase and continuum profile remain preserved. A key consequence is

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`. `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

Core files include:

- `FINITE_DEFICIT_SOURCE_TUPLE_CAPACITY_AND_RATIO_GAP.md`;
- `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`;
- `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`.

## 4. Preserved enhanced alpha-beta / continuum master

For fibre `i`, with `m_i=min(u_i^0,u_i^1)` and alpha load `h_i`,

> `P_i+((m_i+1)/(lambda+1))T_i`
>
> `>=(m_i+1)max(m_i,h_i)`                                `(EABF)`

for `lambda>=0`.

The alpha-overflow term

`X_alpha=sum_i(m_i+1)(h_i-m_i)_+`

has an explicit Hamming-sensitive lower bound.

The root-imbalance floor

> `B_beta>=p(lambda+1-2p)_+`                              `(RBF)`

remains valid, but is now subsumed above threshold by the stronger scorecard-aware beta floor in Section 7.

For fixed `r>=3`, if `u/p->rho` and a threshold count `N/p->nu`,

> `Phi_r(N)/p^2 -> phi_r(nu;rho)`
>
> `=int_0^1 [nu-(kappa/r)(rho/(1-kappa))^r]_+ d kappa`. `(CSP)`

The continuum enhanced IPM `(CEIPM)` remains the main independent global necessary condition in the linear-`lambda` regime. The old coarse linear envelope is known to be non-sharp; do not optimize or quote the old `13/4` cap as current best information.

## 5. Repaired cylinder witness accounting remains valid

For `x in A`, the beta-cylinder theorem supplies a full A-code class `R subseteq N_A(x)` with

> `|R|>=ceil((p-epsilon_x)_+/2^{k_x})`.                   `(CY3)`

The repeated code need not equal `c(x)`. If

`D={i:c_R(i)!=c(x)(i)}`,

then

> `D subseteq [p]\I_x`, so `|D|<=k_x`.                  `(CR1)`

For critical edges from the repeated class:

- A/U witnesses are complementary to the relevant **source** code;
- a matched-B witness can occur only in a differing coordinate `i in D`;
- if `|R|>=2`, no outgoing orientation from the centre can use a matched-B witness;
- incoming matched-B witnesses are the only exceptional channel.

Never use the discarded assumption `c_R=c(x)`.

Matched-foot gamma collision classes are switchable zero-signed subcores. With

`R_A(L_A)=max(2,floor((1+sqrt(1+4L_A))/2))`,

preserved matched-foot self-pricing gives

> `M_P<=aR_A(L_A)`,                                      `(MSP3)`

and the A/U channel has the exact codewise unique-common-neighbour capacity from `(AUC1)--(AUC4)`.

Same-code crowding and complementary-pair localization further give the distribution-free complete-cylinder inequality

> `sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `<= aR_A(C_0)`
>
> ` + min(`
>
> `     R_code C_0/(lambda+1),`
>
> `     V_0 sqrt(2aC_0/(lambda+1))`
>
> `   )`                                                  `(DCF)`

for every family `X` of beta-loaded centres, where

`V_0=a+u`,

`D_0=5p+5u-3lambda-2`,

`R_code=floor((D_0+sqrt(D_0^2+12C_0))/3)`.

Core file:
`project/research/post_ms/2026-09-18-large-code-pair-v1/SAME_CODE_CROWDING_COMPLEMENT_PAIR_LOCALIZATION.md`.

`(DCF)` is correct but is no longer the preferred generic closure route for the reason in Section 6.

## 6. New cylinder-scale obstruction: why the old active bridge is not enough

Let

`N_K=|{x in A:k_x<=K}|`.

From `(FDPr)` with `r=3`, if `u<=Cp` and `0<=K<=p/2-3`, then for sufficiently large `p`,

> `N_K<= (8C^3/3)(K+3)`.                                 `(CS1)`

The exact dyadic layer-cake identity is

> `sum_x 2^{-k_x}=sum_{K>=0}N_K/2^{K+1}`.                `(CS2)`

Therefore, if `u=O(p)` and `a=O(p)`,

> `sum_x 2^{-k_x}=O(1)`,

and hence the complete repaired-cylinder expression itself satisfies

> `Gamma:=sum_x ceil((p-epsilon_x)_+/2^{k_x})=O(p)`.     `(CSO)`

This is a **strategic obstruction**, not a D2C exclusion theorem. It says the proposed programme “force the `(DCF)` left side above its parameter-only right side using only `(FDPr)`” cannot close the generic linear-size coded layer on scale: the source-tuple hierarchy itself keeps the entire cylinder expression linear.

When `a=Theta(p)` and `C_0->infinity`, the current matched-foot term `aR_A(C_0)` is already `omega(p)`; in the genuine linear-scorecard regime it is `Theta(p^2)`.

Thus `(DCF)` should be treated as an equality/stability or finite-subcase tool unless a new D2C argument reduces its right side to linear scale.

Core file:
`project/research/post_ms/2026-09-18-source-tuple-envelope-v1/SOURCE_TUPLE_BETA_LOAD_ENVELOPE_AND_CYLINDER_SCALE_OBSTRUCTION.md`.

## 7. New exact source-tuple beta-load envelope

Put

`B_beta=sum_x ell_x=pu-h_alpha`.

For `r>=3` and `0<=K<=p-r`, define

> `U_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

The threshold form of `(FDPr)` gives `N_K<=U_r(K)`. Splitting beta load at threshold `K` therefore yields the exact finite cap

> `B_beta`
> `<= a(p-K-1)+(K+1)U_r(K)`.                             `(STB)`

Above threshold put

`R_hat=min(p,R_*)`.

Since `h_alpha<=mu_alpha a<=R_hat a`, one also has

> `B_beta >= [pu-R_hat a]_+`.                             `(STL)`

Thus every above-`M(n)` partial-Boolean candidate satisfies the parameter-only **source-tuple / switching sandwich**

> `[pu-R_hat a]_+`
> `<=a(p-K-1)+(K+1)U_r(K)`                               `(STS)`

for every `r>=3` and `0<=K<=p-r`.

This is now the preferred compact bridge from switching/Hall structure to the source-tuple hierarchy. It contains no Hamming variable, code-distribution variable, or cylinder witness variable.

### Continuum beta envelope

If

`u/p->rho`, `lambda/p->theta`, `A=2+rho-theta>0`,

and `K/p->kappa in (0,1)`, then `(STB)` gives, for every fixed `r>=3`,

> `beta:=limsup B_beta/p^2`
> `<=F_r(kappa;rho,theta)`                                `(CBE)`
>
> `=A(1-kappa)+(kappa^2/r)(rho/(1-kappa))^r`.

If `C_0/p^2->c>=0`, then `(STL)` gives

> `beta >= [rho-A min(1,sqrt(c))]_+`.                    `(CBL)`

For the live above-threshold linear scaling,

`c=theta(1+rho)-theta^2/2`.

The branch `min(1,sqrt(c))=1` recovers `beta>=(theta-2)_+`.

## 8. New finite and asymptotic root-imbalance restrictions

### Exact finite `3p` exclusion

Using `(STB)` with `r=3`, `K=1` gives a very short finite theorem:

> if `p>=10` and `u<=2p`, then `lambda<=3p-1`.            `(3P)`

This does **not** require `m>M(n)`; it is a structural consequence of the selected partial-Boolean system.

The hand proof is in the source-tuple envelope note. The key estimate is

> `U_3(1)<=2p-2` for `p>=10`, `u<=2p`,

while `lambda>=3p` would force

> `B_beta>=p(p+1)`

but `(STB)` gives at most `p^2+p-2`.

### Rational asymptotic improvement

If

`u/p->rho in (0,2]`,

`lambda/p->theta>2`,

then taking `r=3`, `kappa=1/9` in `(CBE)` gives

> `theta<=3227/1088=2.965992647...`.                     `(RTH)`

This supersedes the old coarse `13/4` discussion on this slice. It is intentionally a short rational bound rather than a decimal optimization; optimizing `kappa` only improves the endpoint slightly.

## 9. Verification at this checkpoint

Preserved audits include:

- exact published 12/32 `X_3` reconstruction;
- 347,358 signed-2-lift matched-foot sign checks, zero failures;
- 26,996 matched-foot polarization checks, zero failures;
- 9,050 A/U overlap checks, zero failures;
- 3,188,930 same-code crowding / complementary-pair / aligned-code checks, zero failures.

New audit package:

`project/research/post_ms/2026-09-18-source-tuple-envelope-v1/check_source_tuple_beta_envelope.py`

with frozen summary

`SOURCE_TUPLE_BETA_ENVELOPE_CHECK_SUMMARY.json`:

- finite `3p` arithmetic: 80,155 checks;
- exact dyadic layer-cake identity: 10,000 checks;
- rational-cap arithmetic: 1,035 checks;
- **91,190 total checks, zero failures**.

These are audit support only; the promoted statements rest on the hand arguments.

## 10. Active next move

The old active target “lower-bound the `(DCF)` left side from `(FDPr)`” is retired as the generic main line because of `(CSO)`.

The highest-value coherent attack is now:

1. combine the exact beta sandwich `(STS)` / continuum envelope `(CBE)--(CBL)` with `(CEIPM)` rather than treating beta load as a loose free variable;
2. seek a hand-certifiable incompatibility between the equality regimes of these two constraints in the genuinely linear-`lambda` region;
3. use `(CPP-P)` / complementary-pair payment only when the surviving parameter region forces concentration;
4. return to cylinder machinery only if a new D2C argument can reduce matched-foot/AU capacity to the same `O(p)` scale as `(CSO)`.

A useful immediate mathematical question is whether the beta-load envelope forces enough **alpha** traffic that enhanced alpha-overflow coercivity makes `(CEIPM)` impossible in part of the remaining linear region. This would connect two already-proved structural systems without another large case split.

The separate `Q=0` / false-twin-core branch remains open.

Do not reopen the closed mixed `{4,5}` selected-excess ladder or optimize for first-proof priority on Erdős #742.

## 11. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure (`k>=19`): internal candidate pending external review.
- Near-full normal form, `Q`, residual defect `delta`, and scorecard: hand derivations.
- Source-tuple hierarchy, enhanced coercivity, continuum profile, repaired cylinder localization, matched-foot self-pricing/polarization, A/U overlap capacity, same-code crowding and complementary-pair localization: preserved hand arguments with regression where stated.
- `(STB)` is an exact algebraic consequence of `(FDPr)`; `(STL)` uses only the beta identity and switching/Hall alpha capacity.
- `(3P)` is finite and hand-proved; `(RTH)` is an asymptotic necessary condition.
- `(CSO)` is a scale theorem about the cylinder expression itself; it does not refute `(DCF)` and is not an eventual D2C theorem.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not global.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- Positive `(lambda+1)` witness-capacity statements are promoted for `lambda>=0`.
- No arbitrary repeated cylinder class may be identified with the centre code unless `D=emptyset` is proved.
- `X_3` has `u=0` and is untouched by every unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->