# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_SOURCE_TUPLE_BETA_ENVELOPE_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The former active idea — force the parameter-only complete-cylinder inequality `(DCF)` from the beta-deficit distribution — has been critically reassessed and retired as the **generic** main line: `(FDPr)` itself implies that the whole repaired-cylinder expression is only `O(p)` when `u,a=O(p)`, whereas the current distribution-free cylinder upper bound is usually superlinear. The higher-value route is now the new **source-tuple total beta-load envelope / switching sandwich**, coupled to `(CEIPM)` and complementary-pair scorecard payment.

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

## 3. Preserved switching / Hall / source-tuple stack

A switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

If `sigma_0` is the largest zero-signed subcore obtainable after switching, then above threshold

> `sigma_0(sigma_0-1)<=C_0`.                              `(SD)`

With

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`,

one has

> `sigma_0<=R_*`,
>
> every unmatched row has `tau(Psi(K_y))>=ceil(p/(R_*+1))`,
>
> `mu_alpha<=R_*` for the largest projective alpha / switching true-twin class.

Selected/Hall consequences include

> `nu_c t_c<=a`,
>
> `p(t_c+t_bar c)<=(mu_alpha+1)a`,
>
> `min(h,p)a>=pu-mu_alpha a`.

Selected orientation inside `U` gives

> `e(G[S])<=sum_{y in S}n_{bar c(y)}` for every `S subseteq U`,

hence

> `q<=a floor((mu_alpha+1)a/p)<=(mu_alpha+1)a^2/p`.       `(SU)`

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x` beta deficit. The source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`    `(FDPr)`

for every `r>=3`.

The directional Hamming/product budget and enhanced alpha-beta coercivity remain preserved. In particular:

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`. `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

Core preserved files include:

- `FINITE_DEFICIT_SOURCE_TUPLE_CAPACITY_AND_RATIO_GAP.md`;
- `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`;
- `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`.

## 4. Preserved repaired-cylinder and complementary-pair machinery

For `x in A`, the beta-cylinder theorem supplies a full A-code class `R subseteq N_A(x)` with

> `|R|>=ceil((p-epsilon_x)_+/2^{k_x})`.                   `(CY3)`

The repeated code need not equal `c(x)`. If

`D={i:c_R(i)!=c(x)(i)}`,

then

> `D subseteq [p]\I_x`, so `|D|<=k_x`.                  `(CR1)`

Never use the discarded assumption `c_R=c(x)`.

All critical-witness channels are now accounted for:

- A/U witnesses are complementary to the relevant source code;
- matched-B witnesses can occur only in differing fibres;
- repeated outgoing classes cannot use matched-B witnesses;
- incoming matched-B traffic is controlled by gamma-collision / switching structure;
- A/U overlap is controlled by unique-common-neighbour injections.

Same-code crowding and complementary-pair localization give the distribution-free complete-cylinder inequality

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

`R_A(C_0)=max(2,floor((1+sqrt(1+4C_0))/2))`,

`V_0=a+u`,

`D_0=5p+5u-3lambda-2`,

`R_code=floor((D_0+sqrt(D_0^2+12C_0))/3)`.

Core file:
`project/research/post_ms/2026-09-18-large-code-pair-v1/SAME_CODE_CROWDING_COMPLEMENT_PAIR_LOCALIZATION.md`.

`(DCF)` remains valid, but Section 5 explains why it is no longer the preferred generic closure route.

## 5. New cylinder-scale obstruction

Let

`N_K=|{x in A:k_x<=K}|`.

From `(FDPr)` with `r=3`, if `u<=Cp` and `0<=K<=p/2-3`, then for sufficiently large `p`,

> `N_K<= (8C^3/3)(K+3)`.                                 `(CS1)`

The exact dyadic layer-cake identity is

> `sum_x 2^{-k_x}=sum_{K>=0}N_K/2^{K+1}`.                `(CS2)`

Therefore, if `u=O(p)` and `a=O(p)`,

> `sum_x 2^{-k_x}=O(1)`,

and hence even the **entire** repaired-cylinder expression satisfies

> `Gamma:=sum_x ceil((p-epsilon_x)_+/2^{k_x})=O(p)`.     `(CSO)`

This is a strategic obstruction, not a D2C exclusion theorem. It shows that `(FDPr)` cannot generically force the `(DCF)` left side to quadratic scale; in fact it prevents that. If `a=Theta(p)` and `C_0->infinity`, the matched-foot term `aR_A(C_0)` on the current right side is already `omega(p)` and is `Theta(p^2)` in the genuine linear-scorecard regime.

Therefore the previous active plan “lower-bound `(DCF)` from `(FDPr)`” is retired as the generic main line. Revisit the cylinder route only if new D2C structure reduces its upper capacity to the same `O(p)` scale, or in a finite/equality subcase.

Core file:
`project/research/post_ms/2026-09-18-source-tuple-envelope-v1/SOURCE_TUPLE_BETA_LOAD_ENVELOPE_AND_CYLINDER_SCALE_OBSTRUCTION.md`.

## 6. New exact total beta-load envelope

Put

`B_beta=sum_x ell_x=pu-h_alpha`.

For `r>=3` and `0<=K<=p-r`, define

> `U_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

The threshold form of `(FDPr)` gives `N_K<=U_r(K)`. Splitting total beta load at threshold `K` yields the exact finite cap

> `B_beta`
> `<= a(p-K-1)+(K+1)U_r(K)`.                             `(STB)`

Above threshold put

`R_hat=min(p,R_*)`.

Since `h_alpha<=mu_alpha a<=R_hat a`,

> `B_beta >= [pu-R_hat a]_+`.                             `(STL)`

Hence every above-`M(n)` partial-Boolean candidate satisfies the parameter-only **source-tuple / switching sandwich**

> `[pu-R_hat a]_+`
> `<=a(p-K-1)+(K+1)U_r(K)`                               `(STS)`

for every `r>=3` and `0<=K<=p-r`.

This is now the preferred compact bridge between switching/Hall structure and the source-tuple hierarchy. It contains no Hamming variable, code-distribution variable, or cylinder witness variable.

### Continuum form

If

`u/p->rho`, `lambda/p->theta`, `A=2+rho-theta>0`,

and `K/p->kappa in (0,1)`, then for every fixed `r>=3`,

> `beta:=limsup B_beta/p^2`
> `<=F_r(kappa;rho,theta)`                                `(CBE)`
>
> `=A(1-kappa)+(kappa^2/r)(rho/(1-kappa))^r`.

If `C_0/p^2->c>=0`, then `(STL)` gives

> `beta >= [rho-A min(1,sqrt(c))]_+`.                    `(CBL)`

For the live above-threshold linear scaling,

`c=theta(1+rho)-theta^2/2`.

The branch `min(1,sqrt(c))=1` recovers the root-imbalance floor `beta>=(theta-2)_+`.

## 7. New beta wedge and root-imbalance restrictions

The total-load theorem has three clean consequences.

### Strict beta wedge

Assume

`u/p->rho>0`, `lambda/p->theta>2`.

Using `(STB)` with any fixed `K` gives asymptotically

`beta<=A=2+rho-theta`,

while the root-imbalance floor gives

`beta>=theta-2`.

Hence

> `theta<=2+rho/2`.                                       `(BW)`

Moreover equality is impossible. On the boundary, total beta deficit

`D_beta=sum_x k_x=ap-B_beta`

would be `o(p^2)`. Markov would then force a linear number of `o(p)`-deficit centres, while the exact `r=3` source-tuple count allows only `o(p)` of them. Therefore every convergent partial-Boolean sequence with `rho>0`, `theta>2` satisfies the strict wedge

> `theta<2+rho/2`.                                        `(SBW)`

Core file:
`project/research/post_ms/2026-09-18-source-tuple-envelope-v1/SOURCE_TUPLE_BETA_WEDGE_ENDPOINT.md`.

### Exact finite `3p` exclusion

A short finite specialization of `(STB)` gives

> if `p>=10` and `u<=2p`, then `lambda<=3p-1`.            `(3P)`

This does **not** require `m>M(n)`.

### Rational asymptotic improvement on `rho<=2`

If

`u/p->rho in (0,2]`, `lambda/p->theta>2`,

then taking `r=3`, `kappa=1/9` in `(CBE)` gives

> `theta<=3227/1088=2.965992647...`.                     `(RTH)`

This supersedes the old coarse `13/4` discussion on this slice. The rational form is deliberately preferred to a tiny decimal optimization improvement.

## 8. Preserved continuum global route

The continuum enhanced IPM `(CEIPM)` remains the main independent global necessary condition in the genuinely linear-`lambda` regime. It incorporates:

- directional Hamming energy;
- beta-deficit/U-degree product;
- enhanced alpha-beta fibre coercivity;
- alpha overflow;
- source-deficit continuum profile;
- sparse-U and scorecard control.

The new constraints `(STS)/(CBE)/(CBL)/(SBW)` should now be imposed **before** optimizing `(CEIPM)`. In particular, beta load is no longer a loose free parameter.

The most promising next compact theorem is an incompatibility between the equality/near-equality regimes of the beta envelope and `(CEIPM)`, rather than further decimal envelope shaving.

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

These are audit support only; promoted statements rest on the hand arguments.

## 10. Active next move

Priorities, in order:

1. **Couple `(STS)/(CBE)/(CBL)/(SBW)` to `(CEIPM)`** and eliminate beta load as an independent optimization variable.
2. Seek a hand-certifiable excluded region, especially where source-tuple beta scarcity forces alpha traffic and `(CEIPM)` simultaneously penalizes alpha overflow / Hamming imbalance.
3. Use complementary-pair payment `(CPP-P)` if the surviving equality regime forces actual code-pair concentration.
4. Return to the cylinder machinery only if a new argument can reduce matched-foot/AU capacity to linear scale, matching `(CSO)`.

The separate `Q=0` / false-twin-core branch remains open.

Do not reopen the closed mixed `{4,5}` selected-excess ladder or optimize for first-proof priority on Erdős #742.

## 11. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure (`k>=19`): internal candidate pending external review.
- Near-full normal form, rooted triangle count `Q`, residual defect `delta`, and scorecard: hand derivations.
- Source-tuple hierarchy, enhanced coercivity, continuum profile, repaired cylinder localization, matched-foot self-pricing/polarization, A/U overlap, same-code crowding and complementary-pair localization: preserved hand arguments with regression where stated.
- `(STB)` is an exact algebraic consequence of `(FDPr)`; `(STL)` uses only the beta identity and switching/Hall alpha capacity.
- `(SBW)` is asymptotic but does not use the second-extremal scorecard; `(3P)` is finite; `(RTH)` is an asymptotic necessary condition.
- `(CSO)` is a scale theorem about the cylinder expression itself; it does not refute `(DCF)` and is not an eventual D2C theorem.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not global.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- Positive `(lambda+1)` witness-capacity statements are promoted for `lambda>=0`.
- No arbitrary repeated cylinder class may be identified with the centre code unless `D=emptyset` is proved.
- `X_3` has `u=0` and is untouched by every unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->