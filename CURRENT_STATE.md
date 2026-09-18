# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_COMPLETE_CYLINDER_FEASIBILITY_LARGE_CODE_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The current near-full programme has two complementary engines:

1. the source/Hamming/alpha-beta variational route for the linear-`lambda` regime; and
2. the repaired beta-cylinder route, whose **entire critical-witness accounting is now globally closed**: matched-B feet and A/U witnesses both have exact aggregate capacities.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. It has `u=0`, so every unmatched-layer theorem below leaves it untouched.

## 2. Near-full normal form and scorecard

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

Let the complete tight-antipode matching in `B` have `p` pairs and let `U` be the unmatched part, `u=|U|`, so `b=2p+u`. Every vertex of `A union U` chooses exactly one endpoint from every tight pair and has a Boolean code in `{0,1}^p`.

Put `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Then

`a=2p+u-lambda-1`,

`Q=p(p+u-1)+q`,

`r=(p+u)(a-p)+p-s-q`,

`delta=b(n-b)-m=(p+u)(a-p)+p-s-q-f`.

For `epsilon_z=b-d(z)`, put

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

## 3. Switching stability and row complexity

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
> the largest projective alpha/true-twin class has `mu_alpha<=R_*`.

The full-tight switching hierarchy itself is internally closed for `k>=19`; do not reopen the fixed-defect ladder as the main attack.

## 4. Selected/Hall, sparse-U, source-tuple, and Hamming facts

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

## 5. Enhanced alpha-beta coercivity and linear-`lambda` master

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

The continuum enhanced IPM `(CEIPM)` is the live necessary condition in the linear regime. For `theta=lambda/p>2`, the beta floor supplies the alpha-free source-profile lower bound

> `nu_0=[theta-2-Ax]_+/(1-x)`.                            `(HSP)`

The old coarse linear envelope is uniformly non-sharp on compact subsets of

> `theta>2+rho/5`.                                       `(STRICT)`

No optimized replacement for the old coarse `13/4` theta cap is promoted yet.

File: `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`.

## 6. Unique-common-neighbour and same-code payments

For nonadjacent vertices with exactly one common neighbour,

> `|holes|=epsilon_z+epsilon_w-(lambda+1)`.               `(UCH)`

If an actual same-code A-clique has order `r>=2`, then

> `E_U+L_A>=ceil(r(lambda+1)/2)`.                         `(SCC)`

Hence above threshold,

> `omega_same-code(A)<=max(1,floor(2C_0/(lambda+1)))`.   `(SCCAP)`

Common A/U witness reuse on a same-code source block forces density and a quadratic hole/clique payment. These remain the local structural tools for large code classes.

## 7. Repaired beta-cylinder localisation

For `x in A`, the beta-cylinder theorem supplies some full A-code class `R subseteq N_A(x)` with

> `|R|>=ceil((p-epsilon_x)_+/2^{k_x})`.                   `(CY3)`

The repeated code need not equal `c(x)`. If

`D={i:c_R(i)!=c(x)(i)}`,

then

> `D subseteq [p]\I_x`, so `|D|<=k_x`.                  `(CR1)`

For a critical edge `xz`, `z in R`:

- A/U witnesses are complementary to the relevant source code;
- a matched-B witness can occur only in a differing coordinate `i in D`;
- if `|R|>=2`, no outgoing orientation from `x` can use a matched-B witness;
- incoming matched-B witnesses are the only exceptional channel.

Never use the discarded assumption `c_R=c(x)`.

## 8. Matched-foot gamma collisions and the old aggregate cap

For a matched endpoint `w=q_i^s`, define its row-complement source code `gamma(w)`. An incoming matched foot obeys

> `N(z) cap N(w)={x} ==> c(z)=gamma(w)`,                  `(MF1)`
>
> `t_w<=n_{gamma(w)}`.                                    `(MF2)`

Gamma-collision classes are switchable zero-signed subcores. With

`mu_gamma=max_c |{w:gamma(w)=c}|`,

> `mu_gamma<=sigma_0`.                                    `(MF5)`

Opposite endpoints satisfy

> `gamma(q_i^1)=bar gamma(q_i^0)`.                        `(MF6)`

The preserved aggregate and weighted caps are

> `M_P<=mu_gamma a`,                                      `(MFC)`
>
> `sum_i[t_i^0 epsilon_i^1+t_i^1 epsilon_i^0]<=mu_gamma L_A`. `(MFSP+)`

## 9. New matched-foot self-pricing and fibre polarization

Define

> `R_A(L_A)=max(2,floor((1+sqrt(1+4L_A))/2))`.

Because any gamma-collision class of size at least three is a zero-signed subcore,

> `mu_gamma<=R_A(L_A)`.                                   `(MSP2)`

Thus

> `M_P<=a R_A(L_A)`.                                      `(MSP3)`

More sharply, if `m=ceil(M_P/a)>=3`,

> `L_A>=m(m-1)`.                                          `(MSP1)`

So with `a=O(p)`, quadratic matched-foot escape forces `L_A=Omega(p^2)`; if `L_A=o(p^2)`, then `M_P=o(p^2)`.

Also, fibre by fibre,

> `t_i^0 epsilon_i^1+t_i^1 epsilon_i^0`
>
> `>=(lambda+1)min(t_i^0,t_i^1)`.

Hence

> `(lambda+1)sum_i min(t_i^0,t_i^1)<=mu_gamma L_A`.      `(PT2)`

For `lambda>=0`, cheap matched-foot traffic is therefore forced to be fibrewise one-sided.

## 10. New complement-majority matched-foot capacity

Partition A-codes into unordered complementary pairs and put

`Delta_A=sum_{ {c,bar c} }|n_c-n_bar c|`,

`a_pm=(a+Delta_A)/2`.

Then for `lambda>=0`,

> `M_P<=mu_gamma[a_pm+L_A/(lambda+1)]`.                   `(CP5)`

Together with `(MFC)` and `(MSP2)`,

> `M_P`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`.      `(CP7)`

Thus near-maximal matched-B escape requires either large `L_A` or strong polarization of the A-layer between complementary Boolean code classes.

File: `project/research/post_ms/2026-09-18-matched-foot-polarization-v1/MATCHED_FOOT_POLARIZATION_SELF_PRICING_AND_CYLINDER_SPILL.md`.

## 11. New global A/U witness-overlap theorem

For each Boolean code `c`, define

`n_c=|A_c|`, `t_c=|U_c|`, `N_c=n_c+t_c`,

`L_c=sum_{x in A_c}epsilon_x`,

`E_c=sum_{y in U_c}epsilon_y`,

`S_c=L_c+E_c`.

Every A/U cylinder certificate consists of a source `z in A` and witness `w in A union U` with

> `c(w)=bar c(z)`,
>
> `N(z) cap N(w)={head}`.

A fixed ordered pair `(z,w)` can occur in at most one certification because its singleton common neighbour uniquely determines the head.

If `C_c` is the number of A/U certifications whose source has code `c`, then

> `C_c<=n_c N_{bar c}`,                                   `(AUC1)`

and the unique-common-neighbour slack inequality gives

> `(lambda+1)C_c`
>
> `<=N_{bar c}L_c+n_cS_{bar c}`.                         `(AUC3)`

Therefore for `lambda>=0`,

> `M_AU`
>
> `<=sum_c min(`
>
> `    n_cN_{bar c},`
>
> `    [N_{bar c}L_c+n_cS_{bar c}]/(lambda+1))`.         `(AUC4)`

With

`mu_A=max_c n_c`, `mu_V=max_c N_c`,

one also has the coarse but useful bound

> `(lambda+1)M_AU`
>
> `<=mu_V L_A+mu_A(E_U+L_A)`
>
> `<=(mu_V+mu_A)(E_U+L_A)`.                              `(AUC5)`

Above threshold,

> `M_AU<=((mu_V+mu_A)C_0)/(lambda+1)`.                   `(AUC6)`

Arbitrary cross-centre witness reuse is already included in these bounds; this closes the aggregate overlap bookkeeping gap.

File: `project/research/post_ms/2026-09-18-matched-foot-polarization-v1/AU_WITNESS_OVERLAP_CAPACITY_AND_COMPLETE_CYLINDER_FEASIBILITY.md`.

## 12. Complete aggregate cylinder feasibility inequality

For any family `X` of beta-loaded centres, choose one repeated class `R_x` per centre and one criticality certificate per edge into that class. All certificates lie either in the A/U channel or the matched-B channel.

Combining `(CY3)`, `(CP7)` and `(AUC4)` gives the exact finite necessary condition, for `lambda>=0`,

> `sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`
>
> `  +sum_c min(`
>
> `      n_cN_{bar c},`
>
> `      [N_{bar c}L_c+n_cS_{bar c}]/(lambda+1))`.       `(LDCF)`

This is the first aggregate cylinder inequality after the scope repair in which **every critical-witness type is globally priced**.

A shorter consequence is

> `sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`
>
> `  +((mu_V+mu_A)(E_U+L_A))/(lambda+1)`.                `(LDCF2)`

In the genuine linear-imbalance scale

`a=O(p)`, `lambda+1=Theta(p)`, `C_0=O(p^2)`,

a family with repeated-cylinder mass `Omega(p^2)` therefore forces at least one of

> `L_A=Omega(p^2)`,
>
> `mu_A=Omega(p)`,
>
> `mu_V=Omega(p)`.                                        `(LCT)`

So the cylinder attack has now been reduced to a specific structural survivor: **macroscopic Boolean code concentration**.

## 13. Verification at this checkpoint

Preserved matched-foot sign-algebra audit:

- all 33,866 signed 2-lifts through `p=6`;
- 347,358 checks, zero failures.

New matched-foot polarization algebra audit:

`check_matched_foot_polarization.py`

- 26,996 checks, zero failures.

New A/U overlap algebra audit:

`check_au_witness_overlap_capacity.py`

- 9,050 exhaustive small code-class slack tables, zero failures.

Frozen summaries are stored beside the scripts. These checks are audit support only; the promoted results are the hand proofs.

## 14. Active next move

The aggregate witness-overlap problem is now algebraically closed. The coherent local frontier is a **large-code-class structure theorem**.

In the linear-`lambda` regime, `(LCT)` says that a quadratic low-deficit cylinder population can survive only by spending quadratic A-slack or by creating a Boolean code class of linear order. The next structural target is therefore:

> show that `mu_A=Omega(p)` or `mu_V=Omega(p)` itself forces enough `E_U+L_A`, same-code edge/clique structure, or complementary-code congestion to violate the second-extremal scorecard.

Useful preserved inputs are:

1. same-code edges have complementary unique-common-neighbour witnesses;
2. same-code cliques pay `(SCC)` directly;
3. common-foot concentration forces density/hole payment;
4. U-code multiplicities already satisfy selected/Hall and complementary-pair caps.

A promising split is to distinguish a macroscopic code class with many internal A-edges from one that is sparse/independent. The dense case should feed `(SCC)`/common-foot criticality; the sparse case must still carry the beta/source-tuple/cylinder obligations and may force complementary-code congestion.

The independent global target remains optimization of `(CEIPM)` on the linear-`lambda` survivor region. Prefer a hand-certifiable exclusion over numerical envelope shaving.

The separate `Q=0` / false-twin-core branch remains open and has not been conflated with the triangle/partial-Boolean branch.

## 15. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form and scorecard: hand derivations.
- Source-tuple hierarchy, enhanced coercivity, continuum profile, repaired cylinder localisation, matched-foot self-pricing/polarization, A/U overlap capacity and complete cylinder feasibility: hand arguments with regression where stated.
- `(SLRG)` assumes `u=O(p)` and `lambda=o(p)`; it is not global.
- `(CEIPM)` is an asymptotic necessary condition, not a closure theorem.
- `(CP5)--(LDCF)` are promoted for `lambda>=0`; the raw paired identity at `lambda=-1` has no positive `(lambda+1)` payment.
- No arbitrary repeated cylinder class may be identified with the centre code unless `D=emptyset` is proved.
- The new cylinder reduction does **not** itself bound `mu_A` or `mu_V`; macroscopic code concentration is the surviving obstruction.
- `X_3` has `u=0` and is untouched by every new unmatched-layer result.
- No all-order or eventual second-extremal theorem is claimed.
<!-- CURRENT-STATUS:END -->