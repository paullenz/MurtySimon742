# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_CONTINUUM_SOURCE_PROFILE_ENHANCED_COERCIVITY_CYLINDER_SCOPE_REPAIRED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. This checkpoint adds four material advances:

- alpha/beta coercivity now retains and prices **excess alpha diversion** rather than discarding it;
- the complete finite source-deficit staircase has an explicit continuum limit, giving a stronger linear-`lambda` variational master;
- once `lambda>2p-1`, root imbalance itself forces a nonzero beta-load floor, so the integrated source term cannot be erased by alpha diversion;
- the beta-cylinder criticality route has been **scope-corrected**: a pigeonholed cylinder class need not equal the centre's code. The correct near-code witness theorem leaves only at most `k_x` matched-B exceptional feet, all with rigid row-complement signatures.

A new same-code clique theorem also converts same-code clique size directly into the global scorecard.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory hostile control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. It has `u=0`, so every unmatched-layer theorem below leaves it untouched.

## 2. Near-full partial-Boolean framework and exact scorecard

For a maximum-degree root `v`, write

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

`Q=e(G[B])`, `F=G[A]`, `delta=b(n-b)-m=r-e(F)`.

Let the complete tight-antipode matching in `B` have `p` pairs and put

`U=B\P`, `u=|U|`, so `b=2p+u`.

Every vertex of `A union U` chooses exactly one endpoint from every tight pair and therefore has a Boolean code in `{0,1}^p`; every two tight fibres are joined by a perfect matching.

Write

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`.

Exact identities:

`a=2p+u-lambda-1`,

`Q=p(p+u-1)+q`,

`r=(p+u)(a-p)+p-s-q`,

`delta=(p+u)(a-p)+p-s-q-f`.

For `epsilon_z=b-d(z)`, put

`E_U=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,

`L_A=sum_{x in A}epsilon_x=a(p+u)-s-2f`.

If `p>=2`, every unmatched `y in U` has an errorful antipode; U--U antipodes have complementary Boolean codes.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`.

Then

> `m<=M(n)` iff `E_U+L_A>=S_req`,

and parity gives

> `m>M(n) ==> E_U+L_A<=C_0:=S_req-2`.                    `(GS-A)`

At `lambda=-1`, this is `E_U+L_A<=2p+u-4` above threshold.

Main files: `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`, `GLOBAL_SLACK_DEFECT_CRITERION.md`.

## 3. Preserved full-tight / switching stability

If tight antipodes cover all of `B`, the switching-defect hierarchy is internally closed for `k>=19`; see `FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`. Do not reopen the fixed-defect ladder as the main attack.

In the near-full branch, a switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

With switching-deletion invariant

`kappa_sw=min_S tau_vc(L Delta delta(S))`,

`sigma_0=p-kappa_sw`,

an above-threshold candidate satisfies

> `sigma_0(sigma_0-1)<=C_0`.                              `(SD)`

Put

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`.

Then every unmatched row satisfies

> `tau(Psi(K_y))>=ceil(p/(R_*+1))`,                       `(RC)`

and the largest projective alpha/true-twin class satisfies

> `mu_alpha<=R_*`.                                        `(AC)`

## 4. Preserved selected/Hall, sparse-U, and beta geometry

Key consequences remain:

> `t_c <= n_{a_i(c)}+n_{b_i(c)}`;                         `(MH)`
>
> `nu_c t_c<=a`;                                          `(MC)`
>
> `p(t_c+t_bar c)<=(mu_alpha+1)a`;                        `(CP)`
>
> `min(h,p)a>=pu-mu_alpha a`.                             `(BP)`

Selected orientation inside `U` gives

> `e(G[S])<=sum_{y in S}n_{bar c(y)}` for every `S subseteq U`, `(UE)`

hence

> `q<=a floor((mu_alpha+1)a/p)<=(mu_alpha+1)a^2/p`.       `(SU)`

For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x` beta deficit, `d_x=d_U(x)`, and `Y_x` the distinct designated beta sources. The beta/central decomposition and cylinder structure remain valid.

## 5. Directional Hamming and finite source-tuple capacity

For coordinate `i`, write

`d_i=u_i^0-u_i^1`, `H=sum_i d_i^2`.

Let `P_alpha` be the directional alpha payment and

`J=sum_x(p-ell_x)(u-d_x)>=0`.

The preserved directional budget is

> `J+H/2+P_alpha`
>
> `<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.           `(DHB)`

For every integer `r>=3`, the finite-deficit source-tuple hierarchy is exact:

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`.   `(FDPr)`

Hence

> `|{x:k_x<=K}|`
>
> `<=((K+r)/r)binom(u,r)/binom(p-K,r)`.                  `(FDSr)`

The complete cutoff staircase is

> `Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`,            `(IST)`

with

`C_hat_r(K)=floor(((K+r)/r)binom(u,r)/binom(p-K,r))`.

If `j=min(p,floor(H/T^2))<p`, the side-occupancy threshold theorem gives

> `J>=w_T Phi_r(N_T)`,                                   `(IP)`

where

`w_T=(u-T)/2-1`,

`N_T=ceil((B_beta-aj)_+/(p-j))`,

`B_beta=pu-h_alpha`.

## 6. Preserved ratio reductions

The triple-source member of the hierarchy and `(DHB)` give the preserved sublinear-imbalance gap:

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies
>
> `rho<27/14`.                                           `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

For

`u/p->rho>0`, `lambda/p->theta>0`, `A=2+rho-theta>0`,

the earlier coarse alpha--beta envelope gives

> `rho^2/6`
>
> `<=rho(1-theta-rho/2)+rho A+2A^2`
>
> ` +max(1,rho/(2theta))[theta(1+rho)-theta^2/2]`.        `(LCE)`

For `rho in [27/14,2]` this implied the coarse bound `theta<13/4`. That remains valid but is no longer the correct final optimization object.

## 7. New enhanced alpha--beta coercivity

For fibre `i`, put

`m_i=min(u_i^0,u_i^1)`,

`h_i=h_i^0+h_i^1`,

and retain the preserved `P_i,T_i` notation. For `lambda>=0`:

> `P_i+((m_i+1)/(lambda+1))T_i`
>
> `>=(m_i+1)max(m_i,h_i)`
>
> `=m_i(m_i+1)+(m_i+1)(h_i-m_i)_+`.                     `(EABF)`

Thus, with

`X_alpha=sum_i(m_i+1)(h_i-m_i)_+`,

> `P_alpha+[p(floor(u/2)+1)/(lambda+1)]L_A`
>
> `>=sum_i m_i(m_i+1)+X_alpha`.                          `(EABG)`

The overflow term itself obeys, for every integer `0<=t<u/2`,

> `X_alpha`
>
> `>=(t+1)[h_alpha-pu/2+H/(2u)-uH/(u-2t)^2]_+`.          `(AOH)`

This is an exact finite payment: excess alpha diversion cannot be treated as free once the Hamming imbalance is known.

File: `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`.

## 8. New root-imbalance beta floor

Because

`h_alpha<=mu_alpha a<=pa`,

we have the exact bound

> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

Consequently, if `j<p`,

> `N_T`
>
> `>=ceil((p(lambda+1-2p)-aj)_+/(p-j))`.                 `(RBN)`

Thus once `lambda>2p-1`, alpha diversion cannot erase beta-source scarcity.

## 9. New continuum source-deficit profile and enhanced linear master

Fix `r>=3`. If

`u/p->rho>0`, `N/p->nu>=0`,

then

> `Phi_r(N)/p^2 -> phi_r(nu;rho)`,                        `(CSP)`

where

> `phi_r(nu;rho)=int_0^1 [nu-(kappa/r)(rho/(1-kappa))^r]_+ d kappa`. `(CP)`

For `r=3`, if `kappa_*` solves

`nu=kappa_* rho^3/[3(1-kappa_*)^3]`,

then

> `phi_3`
>
> `=nu kappa_*-(rho^3/3)[1/(2(1-kappa_*)^2)-1/(1-kappa_*)+1/2]`. `(CP3)`

Now let

`H/p^3->eta`, `h_alpha/p^2->alpha`, `q/p^2->xi`,

and choose `sqrt(eta)<tau<rho`. Put

`x=eta/tau^2`,

`nu=[rho-alpha-Ax]_+/(1-x)`,

`c(rho,theta)=theta(1+rho)-theta^2/2`,

`g=max(1,rho/(2theta))`.

Then every limiting above-threshold candidate satisfies

> `((rho-tau)/2)phi_r(nu;rho)`
>
> ` +eta/2+(rho-sqrt(eta))^2/4`
>
> ` +Omega(rho,eta,alpha)`
>
> `<=rho(1-theta-rho/2)+rho alpha+2xi+g c(rho,theta)`,    `(CEIPM)`

where

> `Omega=sup_{0<s<rho/2}`
>
> `s[alpha-rho/2+eta/(2rho)-rho eta/(rho-2s)^2]_+`.      `(AOP)`

When `theta>2`, `(RBF)` allows the alpha-free replacement

> `nu_0=[theta-2-Ax]_+/(1-x)`.                           `(HSP)`

The old coarse `rho^2/6` Hamming/coercivity lower bound is therefore provably non-sharp on every compact subset of

> `theta>2+rho/5`,                                       `(STRICT)`

because its unique minimizer is `eta=rho^2/9`; at that point choosing `tau=2rho/3` gives

`nu_0=(5theta-10-rho)/3>0`,

hence a strictly positive continuum source-profile term.

No optimized numerical replacement for `13/4` is yet promoted. The correct next global calculation is the explicit variational inequality `(CEIPM)`.

## 10. Same-code clique scorecard payment

The exact unique-common-neighbour identity remains

> `|H(z,w)|=epsilon_z+epsilon_w-(lambda+1)`.              `(UCH)`

For an actual same-code A-clique `K` of order `r>=2`, orient every clique edge by one D2C critical witness. A complementary-code witness cannot serve edges with two different heads; both source and witness multiplicities are therefore at most `r-1`. Summing `(UCH)`/`(UCS)` over all clique edges gives

> `E_U+L_A>=ceil(r(lambda+1)/2)`.                         `(SCC)`

Hence an above-threshold candidate has

> `omega_same-code(A)`
>
> `<=max(1,floor(2C_0/(lambda+1)))`.                     `(SCCAP)`

If one A/U incoming critical foot is reused on a same-code source block `S_w` of size `t`, the preserved common-foot clique lower bound plus `(SCCAP)` yields the quadratic hole payment

> `sum_{z in S_w}[epsilon_z+epsilon_w-(lambda+1)]`
>
> `>=t^2/R_C-t`,                                         `(CFQ)`

where

`R_C=max(1,floor(2C_0/(lambda+1)))`.

Also the number of distinct A/U incoming feet in such a block is at most

> `floor(C_0/(lambda+1))`.                               `(CFGCAP)`

File: `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`.

## 11. Important cylinder scope correction and repaired near-code theorem

The beta-cylinder theorem gives, for `x in A`,

> `d_A(x)>=(p-epsilon_x)_+`,

and therefore some full A-code class `R subseteq N_A(x)` of size at least

> `ceil((p-epsilon_x)_+/2^{k_x})`.                       `(CY3)`

**Correction:** `CY3` does not imply that the repeated code of `R` equals `c(x)`. It only agrees with `c(x)` on the beta-target coordinates. The previous same-code criticality lemmas therefore apply directly only when the code difference set is empty.

The repaired theorem is as follows. Let

`D={i:c_R(i)!=c(x)(i)}`.

Then

> `D subseteq [p]\I_x`, so `|D|<=k_x`.                  `(CR1)`

For every critical edge `xz`, `z in R`:

- an A/U witness is complementary to the **source** code;
- a matched-B witness can occur only in a coordinate `i in D`, and its B-row is forced to be complementary to the source on every other tight fibre;
- if `|R|>=2`, **no outgoing orientation from `x` can use a matched-B witness**, because that endpoint is adjacent to every member of the repeated class and would create multiple common neighbours;
- incoming matched-B witnesses are therefore the only non-scorecard escape, and there are at most `|D|<=k_x` possible endpoint types.

Thus the repeated class decomposes as

> `R=O dotcup I_AU dotcup I_P`,                           `(CR2)`

where `O` and `I_AU` are controlled by the existing A/U complementary-witness machinery, while `I_P` uses at most `k_x` rigid matched-row feet.

If one matched endpoint `w` is reused on a source set `S_w subseteq I_P`, the unique-common-neighbour hole estimate still gives

> `d_overline{G[S_w]}(z)`
> `<=epsilon_z+epsilon_w-(lambda+1)`,                    `(CR4)`

so heavy reuse forces a dense source block. However `epsilon_w` is a matched-endpoint slack and is **not** automatically part of `E_U+L_A`; it must be converted through endpoint-slack machinery or a new row-overlap argument.

File: `CYLINDER_REPEATED_CLASS_WITNESS_LOCALISATION.md`.

This correction narrows an implicit scope leap in the previous checkpoint and must be respected in all future cylinder arguments.

## 12. Verification at this checkpoint

New regression support:

`check_enhanced_coercivity_continuum_and_clique_slack.py`

with frozen summary

`ENHANCED_COERCIVITY_CONTINUUM_CLIQUE_CHECK_SUMMARY.json`.

It replayed:

- 35,000 exhaustive small enhanced-fibre configurations;
- 200,000 deterministic exact-rational alpha-overflow stress cases;
- 127,378 exact beta-floor cases;
- 144 exact triple-profile antiderivative identities;
- all 33,866 tournament orientations through order six for the clique multiplicity bookkeeping;
- 100,000 exact-rational common-foot rearrangement cases.

Total: **496,388 checks, zero failures**. These are audit support only; the promoted statements are the hand proofs.

The earlier UCN/cylinder and alpha--beta/integrated-product regression suites remain preserved.

## 13. Active next move

There are now two tightly specified live targets.

### A. Linear-`lambda` global optimization

Do not optimize the old coarse `(LCE)` further. Use `(CEIPM)` with the explicit continuum profile `phi_3` (and, where useful, larger fixed `r`) plus the alpha-overflow term `(AOP)`. In the `theta>2` region, use the alpha-free beta floor `(HSP)`.

The immediate objective is a hand-certifiable reduction of the compact `(rho,theta)` survivor, ideally one that can then be combined with the sublinear-`lambda` `27/14` gap.

### B. Low-deficit cylinder overlap

Do not assume the CY3 repeated class has code `c(x)`. Instead exploit the repaired trichotomy: a low-deficit centre has at most `k_x` matched-B exceptional incoming feet, each with a rigid row-complement signature. The next theorem should bound **reuse of those matched feet across many low-deficit centres**, converting it into endpoint-slack payment `T_i` or a rigid signed-row obstruction.

This is more precise than the previous informal complementary-near-clique overlap target.

The separate `Q=0` / false-twin-core branch from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` remains open and has not been conflated with the triangle/partial-Boolean branch.

Do not return to the closed mixed `{4,5}` selected-excess ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742.

## 14. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form and scorecard: hand derivations.
- Source-tuple capacity, directional Hamming, enhanced alpha--beta coercivity, continuum profile, unique-common-neighbour and same-code clique payment: hand arguments with independent regression where stated.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not a global theorem.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- The earlier cylinder pigeonhole remains valid, but its repeated class need not equal the centre code; the repaired witness-localisation theorem is the current canonical formulation.
- The `X_3` negative control has `u=0` and is untouched by every new unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->