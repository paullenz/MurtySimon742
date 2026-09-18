# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_CONTINUUM_SOURCE_PROFILE_MATCHED_FOOT_CAPACITY`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The current near-full attack has two complementary engines:

1. a global source/Hamming/alpha-beta variational inequality, now strengthened by the continuum limit of the complete finite source-deficit staircase; and
2. a repaired local beta-cylinder criticality theory in which the only matched-B escape has a new global collision/capacity bound.

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

## 4. Selected/Hall and sparse-U facts still in force

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

## 5. Directional Hamming and finite source-tuple hierarchy

For coordinate `i`, write `d_i=u_i^0-u_i^1` and `H=sum_i d_i^2`. For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x` beta deficit, and `d_x=d_U(x)`. Put

`J=sum_x(p-ell_x)(u-d_x)>=0`.

The directional budget is

> `J+H/2+P_alpha`
>
> `<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.           `(DHB)`

For every integer `r>=3`,

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`.   `(FDPr)`

Define

`C_hat_r(K)=floor(((K+r)/r)binom(u,r)/binom(p-K,r))`,

`Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`.

If `j=min(p,floor(H/T^2))<p`, then

> `J>=w_T Phi_r(N_T)`,                                   `(IP)`

where

`w_T=(u-T)/2-1`,

`N_T=ceil((B_beta-aj)_+/(p-j))`,

`B_beta=pu-h_alpha`.

The preserved sublinear-imbalance consequence is:

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`. `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

## 6. Enhanced alpha-beta coercivity

For fibre `i`, put `m_i=min(u_i^0,u_i^1)` and `h_i=h_i^0+h_i^1`. For `lambda>=0`, preserving the old `P_i,T_i` notation,

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

Thus excess alpha diversion is itself priced once Hamming imbalance is known.

Also, since `h_alpha<=mu_alpha a<=pa`,

> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

So once `lambda>2p-1`, root imbalance forces a positive beta-load floor before any finer alpha-capacity argument.

## 7. Continuum source-deficit profile and the live linear-lambda master

Fix `r>=3`. If

`u/p->rho>0`, `N/p->nu>=0`,

then

> `Phi_r(N)/p^2 -> phi_r(nu;rho)`,

where

> `phi_r(nu;rho)=int_0^1 [nu-(kappa/r)(rho/(1-kappa))^r]_+ d kappa`. `(CSP)`

For `r=3`, if `kappa_*` solves

`nu=kappa_* rho^3/[3(1-kappa_*)^3]`,

then

`phi_3=nu kappa_*-(rho^3/3)[1/(2(1-kappa_*)^2)-1/(1-kappa_*)+1/2]`.

Now let

`u/p->rho`, `lambda/p->theta`, `A=2+rho-theta>0`,

`H/p^3->eta`, `h_alpha/p^2->alpha`, `q/p^2->xi`.

For `sqrt(eta)<tau<rho`, put

`x=eta/tau^2`,

`nu=[rho-alpha-Ax]_+/(1-x)`,

`c=theta(1+rho)-theta^2/2`,

`g=max(1,rho/(2theta))`.

Then every limiting above-threshold candidate satisfies

> `((rho-tau)/2)phi_r(nu;rho)`
>
> ` +eta/2+(rho-sqrt(eta))^2/4`
>
> ` +Omega(rho,eta,alpha)`
>
> `<=rho(1-theta-rho/2)+rho alpha+2xi+g c`,              `(CEIPM)`

where

`Omega=sup_{0<s<rho/2} s[alpha-rho/2+eta/(2rho)-rho eta/(rho-2s)^2]_+`.

If `theta>2`, `(RBF)` permits the alpha-free replacement

> `nu_0=[theta-2-Ax]_+/(1-x)`.                           `(HSP)`

The old coarse lower envelope

`eta/2+(rho-sqrt eta)^2/4`

has unique minimum `rho^2/6` at `eta=rho^2/9`. At that minimizer, choosing `tau=2rho/3` gives

`nu_0=(5theta-10-rho)/3`.

Hence the old coarse linear envelope is uniformly non-sharp on compact subsets of

> `theta>2+rho/5`.                                       `(STRICT)`

No optimized replacement for the old `13/4` coarse theta bound is promoted yet. Future global optimization should use `(CEIPM)`, not the discarded coarse envelope alone.

File: `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`.

## 8. Same-code clique scorecard payment

For nonadjacent vertices with exactly one common neighbour,

> `|holes|=epsilon_z+epsilon_w-(lambda+1)`.               `(UCH)`

If an actual same-code A-clique has order `r>=2`, D2C critical witnesses and multiplicity give

> `E_U+L_A>=ceil(r(lambda+1)/2)`.                         `(SCC)`

Therefore above threshold,

> `omega_same-code(A)<=max(1,floor(2C_0/(lambda+1)))`.   `(SCCAP)`

Reusing one A/U incoming foot on a same-code source block of size `t` forces the corresponding hole excess to be at least `t^2/R_C-t`, with `R_C=max(1,floor(2C_0/(lambda+1)))`.

## 9. Repaired beta-cylinder witness localisation

The beta-cylinder theorem gives, for `x in A`,

> some full A-code class `R subseteq N_A(x)` of size at least
>
> `ceil((p-epsilon_x)_+/2^{k_x})`.                       `(CY3)`

**Scope correction:** the repeated code `c_R` need not equal `c(x)`; it only agrees with `c(x)` on beta-target coordinates.

Let

`D={i:c_R(i)!=c(x)(i)}`.

Then

> `D subseteq [p]\I_x`, so `|D|<=k_x`.                  `(CR1)`

For each critical edge `xz`, `z in R`:

- an A/U witness is complementary to the source code;
- a matched-B witness can occur only in a coordinate `i in D`, with a forced row-complement signature;
- if `|R|>=2`, no outgoing orientation from `x` can use a matched-B witness;
- incoming matched-B witnesses are therefore the only non-scorecard escape, with at most `k_x` possible endpoint types locally.

This is the canonical cylinder formulation. Do **not** use the older implicit assumption `c_R=c(x)`.

File: `CYLINDER_REPEATED_CLASS_WITNESS_LOCALISATION.md`.

## 10. New global matched-foot collision/capacity theorem

For a matched endpoint `w=q_i^s`, define its row-complement source code `gamma(w)` as the Boolean code choosing the mate of `w` in fibre `i` and the endpoint opposite every matched-B neighbour of `w` in every other fibre.

If `w` is an incoming critical foot,

> `N(z) cap N(w)={x}`,

then necessarily

> `c(z)=gamma(w)`.                                        `(MF1)`

For fixed `z,w`, the singleton common neighbour is unique, so `w` can certify at most one centre for a given source. Thus

> `t_w<=n_{gamma(w)}`.                                    `(MF2)`

If endpoints `q_i^{s_i}` have the same `gamma` code, then for every pair

> `sigma_ij=s_i xor s_j`.

Switching fibre `i` by `s_i` makes every sign inside that collision class zero. Therefore gamma-collision classes are switchable zero-signed subcores, and

> `mu_gamma:=max_c |{w:gamma(w)=c}|<=sigma_0<=R_*`.      `(MF5)`

Hence the total number `M_P` of exceptional incoming cylinder certifications using matched-B feet satisfies

> `M_P<=sigma_0 a<=R_* a`.                               `(MFC)`

This is the first aggregate cylinder-capacity theorem that remains valid after the code-scope repair. In the common regime `C_0=O(p)`, it gives only `O(p^{3/2})` total matched-foot escape.

There is also a scorecard-weighted form. Since one use obeys

`epsilon_z+epsilon_w>=lambda+1`, and any A-source can be counted for at most `mu_gamma` colliding feet,

> `sum_w t_w(lambda+1-epsilon_w)_+<=sigma_0 L_A`.        `(MFS)`

For one tight fibre `P_i`, `epsilon_i^0+epsilon_i^1=lambda+1`, so equivalently

> `sum_i[t_i^0 epsilon_i^1+t_i^1 epsilon_i^0]<=sigma_0 L_A`. `(MFSP)`

Thus heavy matched-foot reuse can occur only on high-slack endpoints; their mates are correspondingly low-slack and expensive in the opposite direction.

Files: `MATCHED_FOOT_COLLISION_CAPACITY.md`, `check_matched_foot_collision_capacity.py`.

## 11. Verification at this checkpoint

New enhanced-coercivity/source-profile regression:

`check_enhanced_coercivity_continuum_and_clique_slack.py`

with frozen summary `ENHANCED_COERCIVITY_CONTINUUM_CLIQUE_CHECK_SUMMARY.json`:

- 496,388 checks, zero failures.

New matched-foot sign-algebra regression:

`check_matched_foot_collision_capacity.py`

with frozen summary `MATCHED_FOOT_COLLISION_CHECK_SUMMARY.json`:

- all 33,866 2-lift signings through `p=6`;
- 47,260 gamma-collision classes;
- 64,220 collision pairs;
- 202,012 opposite-endpoint complement checks;
- **347,358 checks, zero failures**.

These are audit support only; the promoted statements are the hand proofs.

## 12. Active next move

Two tightly specified targets remain.

### A. Linear-`lambda` global optimization

Optimize `(CEIPM)` with the explicit `phi_3` profile and alpha-overflow term. In the `theta>2` region, use the alpha-free beta floor `(HSP)`. Seek a hand-certifiable shrinking of the compact `(rho,theta)` survivor rather than another coarse numerical constant.

### B. Aggregate low-deficit cylinder closure

For any family of low-deficit centres, choose one repeated cylinder class per centre. The matched-B portion of all those classes has total mass at most `sigma_0 a` by `(MFC)`, and cheap matched feet satisfy the stronger weighted cap `(MFS)`. Therefore any repeated-class mass beyond this must enter A/U witness channels.

The next theorem should combine this with the cylinder multiplicity

`|R_x|>=ceil((p-epsilon_x)_+/2^{k_x})`

on the low-deficit population forced by the source-tuple staircase, and convert the excess A/U witness demand into `L_A` via distinct-witness or common-foot capacity.

The separate `Q=0` / false-twin-core branch remains open and has not been conflated with the triangle/partial-Boolean branch.

## 13. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form and scorecard: hand derivations.
- Source-tuple hierarchy, directional Hamming, enhanced alpha-beta coercivity, continuum profile, unique-common-neighbour, same-code clique payment, repaired cylinder localisation and matched-foot capacity: hand arguments with regression where stated.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not global.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- No arbitrary repeated cylinder class may be identified with the centre code unless `D=emptyset` is proved.
- `X_3` has `u=0` and is untouched by every new unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->