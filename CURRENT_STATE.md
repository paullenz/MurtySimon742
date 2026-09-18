# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_MATCHED_FOOT_SELF_PRICING_CYLINDER_SPILL`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The two active engines are:

1. the source/Hamming/alpha-beta variational programme for the linear-`lambda` regime; and
2. the repaired beta-cylinder programme, whose exceptional matched-B witness channel is now not merely capped but **self-priced by `L_A`**, forced to polarize fibrewise, and controlled by complementary A-code mass.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. It has `u=0`, so every unmatched-layer theorem below leaves it untouched.

## 2. Near-full normal form and exact scorecard

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

Let the complete tight-antipode matching in `B` have `p` pairs and let `U` be the unmatched part, `u=|U|`, so `b=2p+u`. Every vertex of `A union U` chooses exactly one endpoint from every tight pair and therefore has a Boolean code in `{0,1}^p`; every two tight fibres are joined by a perfect matching.

Put `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Then

`a=2p+u-lambda-1`,

`Q=p(p+u-1)+q`,

`r=(p+u)(a-p)+p-s-q`,

`delta=b(n-b)-m=(p+u)(a-p)+p-s-q-f`.

For vertex slack `epsilon_z=b-d(z)`, define

`E_U=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,

`L_A=sum_{x in A}epsilon_x=a(p+u)-s-2f`.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`.

Then

> `m<=M(n)` iff `E_U+L_A>=S_req`,

and parity gives

> `m>M(n) ==> E_U+L_A<=C_0:=S_req-2`.                    `(GS-A)`

At `lambda=-1`, `C_0=2p+u-4`.

Main files: `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`, `GLOBAL_SLACK_DEFECT_CRITERION.md`.

## 3. Switching stability and row complexity

A switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

Let `sigma_0` be the largest zero-signed subcore obtainable after switching. Above threshold,

> `sigma_0(sigma_0-1)<=C_0`.                              `(SD)`

Put

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`.

Then

> `sigma_0<=R_*`,
>
> every unmatched row has `tau(Psi(K_y))>=ceil(p/(R_*+1))`,
>
> the largest projective alpha/true-twin class has `mu_alpha<=R_*`.

The full-tight switching hierarchy itself is internally closed for `k>=19`; do not reopen the fixed-defect ladder as the main attack.

## 4. Selected/Hall, sparse-U, and source-tuple facts

For Boolean U-code multiplicities and A-code counts, the preserved selected/Hall machinery gives, among other consequences,

> `nu_c t_c<=a`,
>
> `p(t_c+t_bar c)<=(mu_alpha+1)a`,
>
> `min(h,p)a>=pu-mu_alpha a`.

Selected orientation inside `U` gives

> `e(G[S])<=sum_{y in S}n_{bar c(y)}` for every `S subseteq U`,

hence

> `q<=a floor((mu_alpha+1)a/p)<=(mu_alpha+1)a^2/p`.       `(SU)`

For coordinate `i`, write `d_i=u_i^0-u_i^1` and `H=sum_i d_i^2`. For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x` beta deficit, and `d_x=d_U(x)`. Put

`J=sum_x(p-ell_x)(u-d_x)>=0`.

The directional budget is

> `J+H/2+P_alpha`
>
> `<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.           `(DHB)`

For every integer `r>=3`,

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`.   `(FDPr)`

The integrated finite-deficit staircase gives `J>=w_T Phi_r(N_T)` in the notation of the preserved source-tuple files.

A key consequence already proved is:

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`. `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

## 5. Enhanced alpha-beta coercivity and linear-`lambda` master

For fibre `i`, put `m_i=min(u_i^0,u_i^1)` and `h_i=h_i^0+h_i^1`. For `lambda>=0`,

> `P_i+((m_i+1)/(lambda+1))T_i`
>
> `>=(m_i+1)max(m_i,h_i)`
>
> `=m_i(m_i+1)+(m_i+1)(h_i-m_i)_+`.                     `(EABF)`

With

`X_alpha=sum_i(m_i+1)(h_i-m_i)_+`,

> `P_alpha+[p(floor(u/2)+1)/(lambda+1)]L_A`
>
> `>=sum_i m_i(m_i+1)+X_alpha`.                          `(EABG)`

For every integer `0<=t<u/2`,

> `X_alpha`
>
> `>=(t+1)[h_alpha-pu/2+H/(2u)-uH/(u-2t)^2]_+`.          `(AOH)`

Also

> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

For fixed `r>=3`, if `u/p->rho` and `N/p->nu`,

> `Phi_r(N)/p^2 -> phi_r(nu;rho)`,

where

> `phi_r(nu;rho)=int_0^1 [nu-(kappa/r)(rho/(1-kappa))^r]_+ d kappa`. `(CSP)`

In the linear regime `u/p->rho`, `lambda/p->theta`, `A=2+rho-theta>0`, `H/p^3->eta`, `h_alpha/p^2->alpha`, `q/p^2->xi`, the continuum enhanced IPM `(CEIPM)` is the live necessary condition. In the `theta>2` region the beta floor supplies the alpha-free source-profile lower bound

> `nu_0=[theta-2-Ax]_+/(1-x)`.                            `(HSP)`

The old coarse linear envelope is uniformly non-sharp on compact subsets of

> `theta>2+rho/5`.                                       `(STRICT)`

No optimized replacement for the old coarse `13/4` theta cap has yet been promoted.

File: `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`.

## 6. Same-code clique and common-foot payments

For nonadjacent vertices with exactly one common neighbour,

> `|holes|=epsilon_z+epsilon_w-(lambda+1)`.               `(UCH)`

If an actual same-code A-clique has order `r>=2`, then

> `E_U+L_A>=ceil(r(lambda+1)/2)`.                         `(SCC)`

Hence above threshold,

> `omega_same-code(A)<=max(1,floor(2C_0/(lambda+1)))`.   `(SCCAP)`

Reusing one A/U incoming foot on a same-code source block of size `t` forces the common-foot hole excess to grow at least quadratically once the clique cap is active. These facts are the current pricing tools for the A/U cylinder channel.

## 7. Repaired beta-cylinder localisation

For `x in A`, the beta-cylinder theorem supplies some full A-code class `R subseteq N_A(x)` with

> `|R|>=ceil((p-epsilon_x)_+/2^{k_x})`.                   `(CY3)`

The repeated code need not equal `c(x)`. If

`D={i:c_R(i)!=c(x)(i)}`,

then

> `D subseteq [p]\I_x`, so `|D|<=k_x`.                  `(CR1)`

For a critical edge `xz`, `z in R`:

- an A/U witness is complementary to the relevant source code;
- a matched-B witness can occur only in a coordinate `i in D`, with a forced row-complement signature;
- if `|R|>=2`, no outgoing orientation from `x` can use a matched-B witness;
- incoming matched-B witnesses are the only non-scorecard escape.

Never reinstate the discarded assumption `c_R=c(x)`.

File: `CYLINDER_REPEATED_CLASS_WITNESS_LOCALISATION.md`.

## 8. Matched-foot gamma collision framework

For a matched endpoint `w=q_i^s`, define its row-complement source code `gamma(w)`. If `w` is an incoming critical foot,

> `N(z) cap N(w)={x} ==> c(z)=gamma(w)`.                 `(MF1)`

For fixed `z,w`, the singleton common neighbour is unique, so

> `t_w<=n_{gamma(w)}`.                                    `(MF2)`

Gamma-collision classes are switchable zero-signed subcores. If

`mu_gamma=max_c |{w:gamma(w)=c}|`,

then

> `mu_gamma<=sigma_0`.                                    `(MF5)`

Opposite endpoints have complementary source codes:

> `gamma(q_i^1)=bar gamma(q_i^0)`.                        `(MF6)`

The old aggregate capacity and weighted payment are

> `M_P<=mu_gamma a<=sigma_0 a`,                           `(MFC)`
>
> `sum_i[t_i^0 epsilon_i^1+t_i^1 epsilon_i^0]<=mu_gamma L_A`. `(MFSP+)`

File: `MATCHED_FOOT_COLLISION_CAPACITY.md`.

## 9. New matched-foot self-pricing and polarization

The collision parameter can now be eliminated in favour of the **actual** A-side slack.

Define

> `R_A(L_A)=max(2,floor((1+sqrt(1+4L_A))/2))`.

Because a gamma-collision class of size at least three is a zero-signed subcore,

> `mu_gamma<=R_A(L_A)`.                                   `(MSP2)`

Therefore

> `M_P<=a R_A(L_A)`.                                      `(MSP3)`

More sharply, if `m=ceil(M_P/a)>=3`,

> `L_A>=m(m-1)`.                                          `(MSP1)`

Thus if `a=O(p)`, a quadratic matched-B escape forces `L_A=Omega(p^2)`; if `L_A=o(p^2)`, then `M_P=o(p^2)`.

The paired endpoint identity also yields, fibre by fibre,

> `t_i^0 epsilon_i^1+t_i^1 epsilon_i^0`
>
> `>=(lambda+1)min(t_i^0,t_i^1)`.

Hence

> `(lambda+1)sum_i min(t_i^0,t_i^1)<=mu_gamma L_A`.      `(PT2)`

For `lambda>=0`, with `D_t=sum_i|t_i^0-t_i^1|`,

> `M_P-D_t<=2mu_gamma L_A/(lambda+1)`.                   `(PT3)`

So cheap matched-foot traffic must be strongly one-sided within tight fibres.

## 10. New complement-majority capacity

Partition A-codes into unordered complementary pairs `Pi={c,bar c}` and define

> `Delta_A=sum_Pi |n_c-n_bar c|`,
>
> `a_pm=sum_Pi max(n_c,n_bar c)=(a+Delta_A)/2`.

Using `gamma(q_i^1)=bar gamma(q_i^0)`, source capacity `t_w<=n_gamma(w)`, and `(PT2)`, one obtains for `lambda>=0`

> `M_P<=mu_gamma[a_pm+L_A/(lambda+1)]`.                   `(CP5)`

Together with `(MFC)`,

> `M_P<=mu_gamma min(a,a_pm+L_A/(lambda+1))`.             `(CP6)`

Eliminating `mu_gamma` via `(MSP2)` gives the fully scorecard-aware form

> `M_P`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`.      `(CP7)`

Equivalently, traffic above pure complement-majority capacity pays directly:

> `L_A>=((lambda+1)/mu_gamma)[M_P-mu_gamma a_pm]_+`.     `(CP9)`

Near-maximal matched-foot escape therefore has a rigid dichotomy: either `L_A` is already large, or the A-code distribution itself is strongly polarized between complementary code classes.

## 11. New aggregate cylinder-spill bridge

For any family `X` of beta-loaded centres, choose one repeated cylinder class `R_x` per centre and one criticality certificate per edge `xz`, `z in R_x`. Let `M_AU(X)` count certifications using A/U witnesses.

Since the remaining certifications are matched-B feet,

> `M_AU(X)+M_P(X)=sum_{x in X}|R_x|`,
>
> `M_P(X)<=M_P`.

Combining the cylinder lower bound `(CY3)` with `(CP7)` gives, for `lambda>=0`,

> `M_AU(X)`
>
> `>= [sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `    -R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))]_+`. `(CS4)`

Consequently, if `a=O(p)` and a low-deficit family has total repeated-class mass `Omega(p^2)`, then either

> `M_AU(X)=Omega(p^2)`

or

> `L_A=Omega(p^2)`.                                       `(CS5)`

This is the current high-value bridge from the source-deficit staircase into D2C critical-witness pricing. The matched-B exception is no longer an unpriced aggregate escape.

File: `project/research/post_ms/2026-09-18-matched-foot-polarization-v1/MATCHED_FOOT_POLARIZATION_SELF_PRICING_AND_CYLINDER_SPILL.md`.

## 12. Verification at this checkpoint

Preserved matched-foot sign-algebra audit:

`check_matched_foot_collision_capacity.py`

- all 33,866 signed 2-lifts through `p=6`;
- 47,260 gamma-collision classes;
- 64,220 collision pairs;
- 202,012 opposite-endpoint complement checks;
- 347,358 checks, zero failures.

New finite algebra audit:

`project/research/post_ms/2026-09-18-matched-foot-polarization-v1/check_matched_foot_polarization.py`

with frozen summary `MATCHED_FOOT_POLARIZATION_CHECK_SUMMARY.json`:

- 3,564 paired cross-slack cases;
- 11,000 complementary-pair capacity cases;
- 11,750 self-pricing counting cases;
- 682 inverse live-cap cases;
- **26,996 checks, zero failures**.

These are audit support only; all promoted statements above are hand arguments.

## 13. Active next move

The coherent local frontier is now the **A/U overlap theorem**.

The source-tuple hierarchy forces a population of low-deficit centres. Their repeated-cylinder mass is quantified by `(CY3)`. The new `(CS4)` says that, unless `L_A` is already large, a definite excess of that mass must enter A/U critical witnesses. The next theorem should price that forced A/U mass globally, combining:

1. outgoing A/U witnesses, which are distinct within each repeated class;
2. incoming A/U witnesses, whose reuse produces same-code source blocks;
3. the same-code clique scorecard theorem `(SCC)`; and
4. the common-foot hole/clique capacity bound.

The desired outcome is an inequality of the form

`forced A/U cylinder mass <= explicit function of E_U+L_A and code-overlap parameters`,

which can be composed directly with `(CS4)` and the finite source-deficit staircase.

In parallel, the separate global target remains optimization of `(CEIPM)` on the linear-`lambda` survivor region. Do not replace the local structural attack by numerical envelope shaving unless it produces a hand-certifiable exclusion.

The separate `Q=0` / false-twin-core branch remains open and has not been conflated with the triangle/partial-Boolean branch.

## 14. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form and exact scorecard: hand derivations.
- Source-tuple hierarchy, directional Hamming, enhanced alpha-beta coercivity, continuum profile, unique-common-neighbour, same-code clique payment, repaired cylinder localisation, matched-foot collision capacity, self-pricing, fibre polarization, complement-majority capacity and cylinder spill: hand arguments with regression where stated.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not global.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- `(CP5)--(CS4)` use division by `lambda+1` and are promoted only for `lambda>=0`; the raw paired inequality `(PT2)` remains meaningful at `lambda=-1` but gives no positive payment there.
- No arbitrary repeated cylinder class may be identified with the centre code unless `D=emptyset` is proved.
- `X_3` has `u=0` and is untouched by every new unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->