# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_SUBLINEAR_LAMBDA_RATIO_GAP_LINEAR_LAMBDA_ENVELOPE_CYLINDER_CRITICALITY`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The principal advances now are:

- exact finite-deficit source-tuple capacity;
- the ratio gap `u/p<27/14` has been extended from fixed `lambda` to the whole sublinear regime `lambda=o(p)` (for linear-unmatched `u=O(p)` sequences);
- alpha/beta diversion coercivity gives a first explicit semialgebraic envelope in the genuinely linear regime `lambda=Theta(p)`;
- beta-cylinder multiplicity has now been connected directly to D2C edge criticality through a unique-common-neighbour slack/hole identity and a complementary-code dual-clique mechanism.

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

Every vertex of `A union U` chooses exactly one endpoint from every tight pair, hence has a partial Boolean code in `{0,1}^p`; every two tight fibres are joined by a perfect matching.

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

> `m>M(n) ==> E_U+L_A<=S_req-2`.                         `(GS-A)`

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

> `sigma_0(sigma_0-1)<=S_req-2`.                          `(SD)`

Put `C=S_req-2` and

`R_*=max(2,floor((1+sqrt(1+4C))/2))`.

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
> `min(h,p)a>=pu-mu_alpha a`,                             `(BP)`

where `h` is the number of occupied complementary U-code pairs.

Selected orientation inside `U` gives

> `e(G[S])<=sum_{y in S}n_{bar c(y)}` for every `S subseteq U`, `(UE)`

hence

> `q <= a floor((mu_alpha+1)a/p)
>      <=(mu_alpha+1)a^2/p`.                              `(SU)`

For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x` beta deficit, `d_x=d_U(x)`, and `Y_x` the distinct designated beta sources. The beta/central decomposition gives

> `s=B_beta+C`,

and every U-neighbour except the designated source in a targeted fibre lies on the same central side as `x`.

## 5. Directional deficiency--Hamming and source-tuple capacity

For coordinate `i`, write

`d_i=u_i^0-u_i^1`, `H=sum_i d_i^2`.

Let `P_alpha` be the directional alpha payment and

`J=sum_x(p-ell_x)(u-d_x)>=0`.

The preserved directional budget is

> `J+H/2+P_alpha`
>
> `<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.           `(DHB)`

The finite-deficit source-tuple hierarchy is exact. For every integer `r>=3`,

> `sum_x binom(ell_x,r)/(p-ell_x+r)
>  <= (1/r)binom(u,r)`.                                   `(FDPr)`

Hence if `p-K>=r`,

> `|{x:k_x<=K}|`
>
> `<=((K+r)/r) binom(u,r)/binom(p-K,r)`.                 `(FDSr)`

The `r=3` member combined with `(DHB)` yields the preserved ratio-gap polynomial

`F(rho)=L_0(rho)-6D_0(rho)-12rho^3/125`,

which is positive on `[27/14,2]`.

File: `FINITE_DEFICIT_SOURCE_TUPLE_CAPACITY_AND_RATIO_GAP.md`.

## 6. Alpha--beta diversion coercivity and integrated product

For fibre `i`, let

`m_i=min(u_i^0,u_i^1)`,

`P_i` be alpha directional payment, and

`T_i=r_i^0 e_i^1+r_i^1 e_i^0`

be beta endpoint-slack payment, where `e_i^0+e_i^1=lambda+1`.

For `lambda>=0`, the new exact fibre coercivity theorem is

> `P_i+((m_i+1)/(lambda+1))T_i >= m_i(m_i+1)`.           `(ABF)`

Globally,

> `P_alpha+[p(floor(u/2)+1)/(lambda+1)]L_A`
> `>=sum_i m_i(m_i+1)`.                                  `(ABG)`

Writing `z=u-sqrt(H/p)>=0`,

> `sum_i m_i(m_i+1)>=(p/4)z(z+2)`.                       `(MIC)`

The source-tuple cutoff bounds have also been integrated over the entire deficit staircase. If

`C_hat_r(K)=floor(((K+r)/r)binom(u,r)/binom(p-K,r))`,

then every `N` A-vertices have total beta deficit at least

> `Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`.             `(IST)`

Combining side-occupancy thresholding with `(IST)` gives

> `J>=w_T Phi_r(N_T)`.                                    `(IP)`

Together `(ABG)`, `(DHB)`, `(IP)`, and the scorecard produce the exact integrated positive-`lambda` master `(IPM)` in

`ALPHA_BETA_COERCIVITY_INTEGRATED_PRODUCT_AND_CYLINDER.md`.

## 7. New scale result: `27/14` gap now holds for `lambda=o(p)`

The fixed-`lambda` hypothesis in the earlier ratio-gap theorem is not necessary.

Assume

`p->infinity`, `u=O(p)`, `lambda=o(p)`,

and an above-`M(n)` near-full sequence. Since

`C=S_req-2=O(p(lambda+1))=o(p^2)`,

we have

`R_*=O(sqrt(p(lambda+1)))=o(p)`,

hence

`mu_alpha=o(p)`,

`h_alpha<=mu_alpha a=o(p^2)`,

`q=o(p^2)`,

`E_U,L_A=o(p^2)`.

Therefore `(DHB)` has exactly the same normalized leading term as in the fixed-`lambda` proof. Along `u/p->rho`,

> `J <= [rho(2-rho)/2+o(1)]p^3`,
>
> `H <= [rho(2-rho)+o(1)]p^3`.

The preserved triple-source argument then applies unchanged. Thus:

> **SUBLINEAR-LAMBDA RATIO GAP — internal candidate.**
>
> If `u=O(p)` and `lambda=o(p)`, every finite subsequential limit satisfies
>
> `rho=lim u/p < 27/14`.                                  `(SLRG)`

Consequently any putative sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime: after a subsequence, `lambda>=theta p` for some constant `theta>0`.

File: `SUBLINEAR_LAMBDA_EXTENSION_OF_SOURCE_TUPLE_RATIO_GAP.md`.

## 8. New linear-`lambda` envelope from alpha--beta coercivity

Now assume

`u/p->rho>0`, `lambda/p->theta>0`,

and put

`A=2+rho-theta` (`a/p->A`).

From `(MIC)`, uniformly over the Hamming imbalance,

> `H/2+sum_i m_i(m_i+1) >= [rho^2/6+o(1)]p^3`.           `(LC2)`

Using only the coarse preserved bounds

`h_alpha<=p a`,

`q<=[A^2+o(1)]p^2`,

and the scorecard term in `(IPM)`, every limiting pair must satisfy

> `rho^2/6`
>
> `<=rho(1-theta-rho/2)+rho A+2A^2`
>
> `  +max(1,rho/(2theta))[theta(1+rho)-theta^2/2]`.       `(LCE)`

For `rho in [27/14,2]`, this yields the explicit upper envelope

> `theta <= theta_-(rho)`
>
> `=(5rho+7-sqrt(11rho^2+4rho+1))/3`,                    `(LTE)`

and in particular

> `theta<13/4`.                                           `(L13)`

Numerically `theta_-(27/14)=3.19939...` and `theta_-(2)=3.23996...`.

This is deliberately coarse: it drops the nonnegative integrated source-product term `w_T Phi_r(N_T)`. The next linear-`lambda` attack should use that term rather than merely optimize this envelope numerically.

File: `LINEAR_LAMBDA_COARSE_ENVELOPE_FROM_ALPHA_BETA_COERCIVITY.md`.

## 9. New beta-cylinder edge-criticality structure

The beta-cylinder theorem gives, for `x in A`, a central cylinder of codimension `ell_x=p-k_x` containing all A-neighbours and

> `d_A(x)>=(p-epsilon_x)_+`.

Hence some full A-code class inside the cylinder contains at least

> `ceil((p-epsilon_x)_+/2^{k_x})`                         `(CY3)`

A-neighbours of `x`.

The new D2C criticality analysis prices the edges into such a repeated class.

### Unique-common-neighbour slack identity

If `z,w in A union U` are nonadjacent with

`N(z) cap N(w)={t}`,

then the number of vertices adjacent to neither is exactly

> `epsilon_z+epsilon_w-(lambda+1)`.                       `(UCH)`

In particular

> `epsilon_z+epsilon_w>=lambda+1`.                        `(UCS)`

### Same-code edge localisation

If `x,z in A` have the same Boolean code and `xz` is an edge, edge criticality supplies `w in A union U` of the complementary Boolean code such that either

`N(x) cap N(w)={z}`

or

`N(z) cap N(w)={x}`.

Thus every same-code A-edge is certified across the complementary code class.

For a same-code star around `x`, outgoing witnesses are distinct and pay

> `sum epsilon_w >= |O|(lambda+1-epsilon_x)`.            `(OUT)`

If many incoming edges share one foot `w`, their source set `S_w` is forced dense:

> `d_overline{G[S_w]}(z)
>  <=epsilon_z+epsilon_w-(lambda+1)`.                     `(CFH)`

Hence

> `omega(G[S_w])`
> `>=ceil(|S_w|^2/(|S_w|+sum_{z in S_w}[epsilon_z+epsilon_w-(lambda+1)]))`. `(CFC)`

### Dual-clique transfer

If one source `x` has distinct critical feet `w_i` with zero hole count, the `w_i` form a clique, are joined to the corresponding heads by exactly a perfect matching, and are anticomplete to the other heads.

More generally, if `W` is such a witness set,

> `2e(overline{G[W]})`
> `<=sum_i[epsilon_x+epsilon_{w_i}-(lambda+1)]`.          `(ADC)`

A same-code A-clique of order `r` therefore transfers at least `floor(r/2)` vertices into a complementary-code near-clique unless the relevant source/foot slacks already pay into `E_U+L_A`.

File: `UNIQUE_COMMON_NEIGHBOR_SLACK_AND_CYLINDER_CRITICALITY.md`.

## 10. Verification added at this checkpoint

New regression support:

`check_ucn_cylinder_and_linear_lambda_envelope.py`

replayed

- all 1,249 graph-atlas graphs of orders 3--7;
- 4,424 unique-common-neighbour pairs for `(UCH)`;
- all 21 D2C graph-atlas classes and 29 critical triangle edges for the generic edge-witness lemma;
- 10,001 exact-rational ratio-grid points on `[27/14,2]` for the `theta=13/4` envelope sign and the `theta_-` / high-regime ordering.

Zero failures. Frozen summary: `UCN_CYLINDER_LINEAR_LAMBDA_CHECK_SUMMARY.json`.

The earlier alpha--beta/integrated-product regression also remains preserved (`632,299` algebraic checks, zero failures). Computation is audit support only; the promoted statements are the hand counting arguments.

## 11. Active next move

The research now has two genuinely different surviving scales.

### A. Large unmatched ratio

If `u/p>=27/14` asymptotically, the sublinear-`lambda` window is gone. The survivor must have `lambda=Theta(p)` and obey the explicit `(rho,theta)` envelope `(LCE)/(LTE)`.

Highest-value next step: **put the discarded integrated product `w_T Phi_r(N_T)` back into the linear-scale optimization.** This is the intended place where source-tuple scarcity and alpha--beta coercivity should interact; merely shaving the coarse `13/4` bound is not the objective.

### B. Low-deficit/low-slack beta witnesses

The beta-cylinder theorem now produces a repeated A-code neighbourhood, and D2C criticality converts its edges into complementary-code unique-common-neighbour witnesses. The next structural target is an **overlap-capacity theorem for many such cylinders**: show that many low-deficit/low-slack centres cannot all reuse the same complementary near-cliques without forcing additional `E_U+L_A`, or else collapse into a rigid dual-clique/matching normal form which can be attacked directly.

These two attacks are complementary: the integrated-product route targets the global linear-`lambda` scale, while the cylinder-criticality route targets local equality/low-slack structure.

The separate `Q=0` / false-twin-core branch from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` remains open and has not been conflated with the triangle/partial-Boolean branch.

Do not return to the closed mixed `{4,5}` selected-excess ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742.

## 12. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form and scorecard: hand derivations.
- Source-tuple capacity, directional Hamming, alpha--beta coercivity, integrated product, unique-common-neighbour and cylinder-criticality results: hand arguments with independent regression where stated.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not a global theorem.
- `(LCE)/(LTE)` are asymptotic necessary conditions in the linear-`lambda` regime, not a closure theorem.
- The `X_3` negative control has `u=0` and is untouched by every new unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->
