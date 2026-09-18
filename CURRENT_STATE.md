# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_DISTRIBUTION_FREE_CYLINDER_BOUND_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The repaired beta-cylinder route now has global capacities for every witness channel, and the former residual obstruction — an unspecified macroscopic Boolean code class — has itself been priced into the scorecard. The current highest-value bridge is from the source-tuple / beta-deficit distribution to the new **parameter-only complete-cylinder upper bound**.

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

The integrated finite-deficit staircase gives the preserved lower bound `J>=w_T Phi_r(N_T)`.

A key consequence is

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`. `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

## 4. Enhanced alpha-beta coercivity and the linear-`lambda` master

For fibre `i`, with `m_i=min(u_i^0,u_i^1)` and alpha load `h_i`,

> `P_i+((m_i+1)/(lambda+1))T_i`
>
> `>=(m_i+1)max(m_i,h_i)`                                `(EABF)`

for `lambda>=0`.

The alpha-overflow term

`X_alpha=sum_i(m_i+1)(h_i-m_i)_+`

has an explicit Hamming-sensitive lower bound, and

> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

For fixed `r>=3`, if `u/p->rho` and `N/p->nu`,

> `Phi_r(N)/p^2 -> phi_r(nu;rho)`
>
> `=int_0^1 [nu-(kappa/r)(rho/(1-kappa))^r]_+ d kappa`. `(CSP)`

The continuum enhanced IPM `(CEIPM)` is the independent global necessary condition in the linear regime. For `theta=lambda/p>2`, the beta floor supplies the alpha-free source-profile lower bound

> `nu_0=[theta-2-Ax]_+/(1-x)`.                            `(HSP)`

The old coarse linear envelope is uniformly non-sharp on compact subsets of

> `theta>2+rho/5`.                                       `(STRICT)`

No optimized replacement for the old coarse `13/4` theta cap is promoted.

Core file:
`project/research/post_ms/2026-09-17-stronger-pivot-v1/ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`.

## 5. Repaired cylinder localization and matched-B channel

For `x in A`, the beta-cylinder theorem supplies a full A-code class `R subseteq N_A(x)` with

> `|R|>=ceil((p-epsilon_x)_+/2^{k_x})`.                   `(CY3)`

The repeated code need not equal `c(x)`. If

`D={i:c_R(i)!=c(x)(i)}`,

then

> `D subseteq [p]\I_x`, so `|D|<=k_x`.                  `(CR1)`

For a critical edge `xz`, `z in R`:

- A/U witnesses are complementary to the relevant **source** code;
- a matched-B witness can occur only in a differing coordinate `i in D`;
- if `|R|>=2`, no outgoing orientation from `x` can use a matched-B witness;
- incoming matched-B witnesses are the only exceptional channel.

Never use the discarded assumption `c_R=c(x)`.

For a matched endpoint `w=q_i^s`, define its row-complement source code `gamma(w)`. Gamma collision classes are switchable zero-signed subcores. Put

`mu_gamma=max_c |{w:gamma(w)=c}|`.

Then

> `mu_gamma<=sigma_0`,
>
> `gamma(q_i^1)=bar gamma(q_i^0)`.

Define

`R_A(L_A)=max(2,floor((1+sqrt(1+4L_A))/2))`.

Matched-foot self-pricing gives

> `mu_gamma<=R_A(L_A)`,                                   `(MSP2)`
>
> `M_P<=aR_A(L_A)`.                                      `(MSP3)`

More sharply, if `m=ceil(M_P/a)>=3`,

> `L_A>=m(m-1)`.                                          `(MSP1)`

Fibre polarization gives

> `(lambda+1)sum_i min(t_i^0,t_i^1)<=mu_gamma L_A`.      `(PT2-old)`

and the complement-majority refinement is

> `M_P<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`.  `(CP7)`

Core files:
`CYLINDER_REPEATED_CLASS_WITNESS_LOCALISATION.md`,
`MATCHED_FOOT_COLLISION_CAPACITY.md`, and
`project/research/post_ms/2026-09-18-matched-foot-polarization-v1/MATCHED_FOOT_POLARIZATION_SELF_PRICING_AND_CYLINDER_SPILL.md`.

## 6. Preserved A/U witness-overlap theorem

For each Boolean code `c`, define

`n_c=|A_c|`, `t_c=|U_c|`, `N_c=n_c+t_c`,

`L_c=sum_{x in A_c}epsilon_x`,

`E_c=sum_{y in U_c}epsilon_y`,

`S_c=L_c+E_c`.

Every A/U cylinder certificate has a source `z in A`, a witness `w in A union U` with `c(w)=bar c(z)`, and a singleton common neighbourhood. A fixed ordered pair `(z,w)` can occur at most once.

If `C_c` is the number of A/U certifications whose source has code `c`, then

> `C_c<=n_cN_bar c`,                                     `(AUC1)`
>
> `(lambda+1)C_c<=N_bar c L_c+n_cS_bar c`.               `(AUC3)`

Hence, for `lambda>=0`,

> `M_AU`
>
> `<=sum_c min(n_cN_bar c,`
>
> `             [N_bar c L_c+n_cS_bar c]/(lambda+1))`.  `(AUC4)`

The old coarse consequence was

> `(lambda+1)M_AU<=(mu_V+mu_A)(E_U+L_A)`.                `(AUC5)`

Combining `(CY3)`, `(CP7)` and `(AUC4)` gave the exact codewise complete-cylinder feasibility inequality `(LDCF)`.

Core file:
`project/research/post_ms/2026-09-18-matched-foot-polarization-v1/AU_WITNESS_OVERLAP_CAPACITY_AND_COMPLETE_CYLINDER_FEASIBILITY.md`.

## 7. New same-code edge capacity on the whole coded layer

The same-code criticality theorem now applies to **all** edges inside a Boolean class `V_c=A_c union U_c`, not only A-edges.

For `p>=1`, every same-code edge has an A/U critical witness of complementary code. If the source lies in `U`, the witness must in fact lie in `A`, because two U-vertices also share the root.

Let

`e_c=e(G[V_c])`, `e_A(c)=e(G[A_c])`, `e_U(c)=e(G[U_c])`.

Then

> `e_c<=N_cN_bar c`,                                      `(SC1)`
>
> `e_A(c)<=n_cN_bar c`,                                   `(SC1A)`
>
> `e_U(c)<=t_cn_bar c`.                                   `(SC1U)`

For `lambda>=0`,

> `(lambda+1)e_c<=N_bar c S_c+N_cS_bar c`,               `(SC2)`
>
> `(lambda+1)e_A(c)<=N_bar c L_c+n_cS_bar c`,            `(SC2A)`
>
> `(lambda+1)e_U(c)<=n_bar c E_c+t_cL_bar c`.            `(SC2U)`

The same tournament argument also extends the clique payment to every same-code clique `K subseteq V_c`:

> `E_U+L_A>=ceil(|K|(lambda+1)/2)`.                       `(SCC+)`

This strictly extends the earlier A-only statement.

## 8. New degree-crowding and complementary-pair payment

Put

> `T=a-p=p+u-lambda-1`.

Exact degree crowding gives

> `2e_A(c)>=n_c(n_c-T)-L_c`,                              `(CR-A)`
>
> `2e_U(c)>=t_c(t_c-T-1)-E_c`,                            `(CR-U)`
>
> `2e_c>=N_c(N_c-T)-t_c-S_c`.                             `(CR-V)`

Combining these with the same-code edge capacities gives the one-sided complement-forcing inequalities

> `L_c>=[n_c(n_c-T-2N_bar c)]_+`,                         `(CF-A)`
>
> `E_c>=[t_c(t_c-T-1-2n_bar c)]_+`,                       `(CF-U)`
>
> `S_c>=[N_c(N_c-T-2N_bar c)-t_c]_+`.                     `(CF-V)`

Thus a large code class is no longer a free survivor: either it pays slack directly or its complementary class must also be large. The U-only version specifically requires complementary **A**-mass.

For `P={c,bar c}`, put `S_P=S_c+S_bar c`, `L_P=max(N_c,N_bar c)`. Then

> `S_P >= (lambda+1)[N_c(N_c-T)-t_c]_+/(2L_P+lambda+1)`, `(CPP-V)`

and the symmetric pair form is

> `S_P >= (lambda+1)[`
>
> ` N_c(N_c-T)+N_bar c(N_bar c-T)-(t_c+t_bar c)`
>
> `]_+/(4L_P+lambda+1)`.                                 `(CPP-P)`

These turn complement congestion itself into scorecard payment.

## 9. New complementary-pair localization of A/U cylinder traffic

For an unordered complement pair `P={c,bar c}`, put

`C_P=C_c+C_bar c`,

`A_P=n_c+n_bar c`,

`V_P=N_c+N_bar c`.

Then

> `C_P<=A_PV_P`.                                          `(PT1)`

Writing `V_0=a+u`, Cauchy gives

> `max_P C_P>=M_AU^2/(aV_0)`.                             `(PT2)`

Thus quadratic A/U cylinder traffic in a linear-size coded layer must concentrate quadratically in **one actual complementary pair**, rather than merely producing unrelated large maxima. In that pair,

> `max(n_cN_bar c,n_bar cN_c)>=M_AU^2/(2aV_0)`.          `(PT3)`

Define the aligned code mass

> `w_c=N_c+n_c=2n_c+t_c`,
>
> `mu_*=max_c w_c`.

Then the old `(mu_V+mu_A)` factor improves to

> `(lambda+1)M_AU<=mu_*(E_U+L_A)`.                        `(AUC5+)`

Locally,

> `(lambda+1)C_P<=max(w_c,w_bar c)S_P`.                  `(PT4)`

Consequently,

> `E_U+L_A>=`
>
> `(lambda+1)M_AU^2/(2aV_0^2)`,                           `(PT6)`

or

> `M_AU<=V_0 sqrt(2a(E_U+L_A)/(lambda+1))`.              `(PT7)`

## 10. New aligned-code self-pricing and distribution-free cylinder cap

The aligned concentration `mu_*` itself is explicitly bounded.

Put

> `D_0=T+2V_0+1=5p+5u-3lambda-2`.

For every code,

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`.                      `(AC1)`

Therefore, in an above-`M(n)` candidate, define

> `R_code=floor((D_0+sqrt(D_0^2+12C_0))/3)`.             `(AC2)`

Then

> `mu_*<=R_code`.                                         `(AC3)`

This closes the previous checkpoint's unspecified “macroscopic code concentration” parameter at the finite scorecard level.

Combining `(AUC5+)`, `(PT7)`, and `(GS-A)` gives the **distribution-free A/U witness cap**

> `M_AU <= min(`
>
> ` R_code C_0/(lambda+1),`
>
> ` V_0 sqrt(2aC_0/(lambda+1))`
>
> `)`.                                                    `(DAU3)`

Finally, matched-foot self-pricing gives `M_P<=aR_A(C_0)`. Hence for every family `X` of beta-loaded A-centres,

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
> `   )`.                                                 `(DCF)`

`(DCF)` is the first **fully parameter-only** complete-cylinder feasibility inequality after the repeated-code scope repair: every witness channel is included and no `mu_A`, `mu_V`, `mu_*`, code-distribution, or complement-polarization variable remains on the right.

Core file:
`project/research/post_ms/2026-09-18-large-code-pair-v1/SAME_CODE_CROWDING_COMPLEMENT_PAIR_LOCALIZATION.md`.

## 11. Verification at this checkpoint

Preserved audits include:

- published 12/32 `X_3` exact reconstruction;
- all 33,866 signed 2-lifts through `p=6` for matched-foot sign algebra: 347,358 checks, zero failures;
- matched-foot polarization: 26,996 checks, zero failures;
- A/U overlap algebra: 9,050 checks, zero failures.

New finite algebra audit:

`project/research/post_ms/2026-09-18-large-code-pair-v1/check_same_code_crowding_pair_localization.py`

- crowding / complement forcing: 182,696 checks;
- weighted complementary-pair payment: 1,322,928 checks;
- aligned A/U capacity `(AUC5+)`: 1,562,500 checks;
- complementary-pair traffic localization: 20,000 deterministic seeded tables;
- global aligned-code cap `(AC1)--(AC3)`: 100,806 checks;
- **3,188,930 total checks, zero failures**.

Frozen summary:
`SAME_CODE_CROWDING_PAIR_CHECK_SUMMARY.json`.

These are audit support only; the promoted statements rest on the hand injections and degree counts.

## 12. Active next move

The generic “large code class” split is no longer the right frontier. The new local route is:

> **lower-bound the left side of `(DCF)` from the beta-deficit/source-tuple distribution.**

The source-tuple hierarchy and integrated finite-deficit staircase already constrain how beta mass can be distributed over deficits `k_x`; `(DCF)` prices the repeated-cylinder mass produced by low-deficit, low-slack centres. The missing compact bridge is to retain enough mass through the factor `2^{-k_x}` to contradict the parameter-only right side on a nontrivial part of the linear-`lambda` region.

Highest-value subtargets:

1. derive an exact layer-cake / convex lower bound for
   `sum_x (p-epsilon_x)_+ 2^{-k_x}`
   from beta load, the source-tuple hierarchy, and `L_A`;
2. combine that lower bound with `(DCF)` before doing any numerical envelope optimization;
3. if near equality survives, use `(CPP-P)` and `(PT4)` to classify the few heavy complementary code pairs forced to carry the A/U traffic.

The independent global route remains optimization of `(CEIPM)` in the linear-`lambda` region. Prefer a hand-certifiable exclusion over decimal envelope shaving.

The separate `Q=0` / false-twin-core branch remains open.

## 13. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form, `Q`, residual defect `delta`, and scorecard: hand derivations.
- Source-tuple hierarchy, enhanced coercivity, continuum profile, repaired cylinder localization, matched-foot self-pricing/polarization, and A/U overlap capacity: preserved hand arguments with regression where stated.
- `(SC1)--(SC2U)` are new hand critical-witness injections; `(CR-A)--(CR-V)` are exact degree counts.
- `(CF-A)--(DCF)` are finite algebraic consequences of those structural inputs.
- Positive `(lambda+1)` capacity conclusions in the new package are promoted for `lambda>=0`.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not global.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- No arbitrary repeated cylinder class may be identified with the centre code unless `D=emptyset` is proved.
- `X_3` has `u=0` and is untouched by every unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->
