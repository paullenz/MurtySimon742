# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_FINITE_DEFICIT_SOURCE_TUPLE_RATIO_GAP_27_14_INTERNAL_CANDIDATE`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the unmatched/errorful antipode regime. The directional beta-fibre argument first improved the fixed-`lambda` linear-unmatched frontier to `limsup u/p<=2`; endpoint stability then forced a bipolar Boolean geometry. The current checkpoint shows that this ratio-two endpoint is itself impossible by a new exact finite-deficit designated-source tuple-capacity theorem, and gives the quantitative internal bound

> `limsup u/p < 27/14 = 1.928571428...`

for every fixed `lambda` above-threshold near-full sequence with `p->infinity`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory hostile control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. It has `u=0`, so every unmatched-layer theorem below leaves it untouched.

## 2. Near-full partial-Boolean framework and scorecard

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

## 3. Preserved switching/high-complexity stability

A switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

With switching-deletion invariant

`kappa_sw=min_S tau_vc(L Delta delta(S))`,

`sigma_0=p-kappa_sw`,

an above-threshold candidate satisfies

> `sigma_0(sigma_0-1)<=S_req-2`.                          `(SD)`

Put

`C=S_req-2`,

`R=floor((1+sqrt(1+4C))/2)`,

`R_*=max(2,R)`.

Then every unmatched row satisfies

> `tau(Psi(K_y))>=ceil(p/(R_*+1))`,                       `(RC)`

and the largest projective alpha/true-twin class satisfies

> `mu_alpha<=R_*`.                                        `(AC)`

For fixed `lambda` and `u=O(p)`:

- `kappa_sw=p-O(sqrt(p))`;
- every unmatched row has cover `Omega(sqrt(p))`;
- `mu_alpha=O(sqrt(p))`.

Do not return to cheap-row case enumeration.

## 4. Multiplicity Hall, antipode payment, sparse U

Preserved selected/Hall consequences include

> `t_c <= n_{a_i(c)}+n_{b_i(c)}`;                         `(MH)`
>
> `nu_c t_c<=a`;                                          `(MC)`
>
> `p(t_c+t_bar c)<=(mu_alpha+1)a`;                        `(CP)`
>
> `min(h,p)a>=pu-mu_alpha a`,                             `(BP)`

where `h` is the number of occupied complementary U-code pairs.

The Boolean antipode-fan payment remains preserved:

- `lambda=-1`: `E_U>=ceil(u/4)`;
- `lambda>=0`: `E_U>=min(u,ceil(u/2)+lambda)`;
- equality is rigid (odd clique fan, regular tournament charging, complementary private holes);
- matched antipode hubs satisfy the corresponding same-code fan inequality.

Selected orientation of edges inside `U` gives, for every `S subseteq U`,

> `e(G[S])<=sum_{y in S}n_{bar c(y)}`.                    `(UE)`

Hence

> `q <= a floor((mu_alpha+1)a/p)
>      <=(mu_alpha+1)a^2/p`.                              `(SU)`

For fixed `lambda`, `u=O(p)`,

> `q=O(p^(3/2))`.

Thus for `u=rho p+O(1)`,

> `Q=p(p+u-1)+O(p^(3/2))`,
>
> `s=rho(1+rho)p^2+O(p^(3/2))`.

## 5. Beta-reuse geometry

For `x in A`, let `ell_x=|I_x|` be its beta load and

`Y_x={y_i:i in I_x}`

its designated unmatched beta sources. The sources in `Y_x` are pairwise distinct.

Put

`C_x=N_U(x)\Y_x`, `c_x=|C_x|`, `d_x=d_U(x)`.

Then

> `d_x=ell_x+c_x`.

Writing

`B=sum_x ell_x=B_beta`,

`C=sum_x c_x`,

there is an exact partition

> `s=B+C`.                                                 `(BC)`

For every `i in I_x`, all U-neighbours of `x` except the single source `y_i` choose the same side of fibre `i` as `x`.

## 6. Directional deficiency--Hamming budget

For coordinate `i`, write

`u_i^0=|{y in U:c(y)_i=0}|`,

`u_i^1=|{y in U:c(y)_i=1}|`,

`d_i=u_i^0-u_i^1`,

`H=sum_i d_i^2`.

Let `h_i^0,h_i^1` be alpha-oriented P--U source counts by side, and define

`P_alpha=sum_i[h_i^0(u_i^1+1)+h_i^1(u_i^0+1)]`.

Directional fibre capacity gives

> `W:=sum_x ell_x d_x
>     <=p(u^2/2+u)-H/2-P_alpha`.                           `(DFM)`

Define

`J=sum_x(p-ell_x)(u-d_x)>=0`,

and `h_alpha=pu-B`. Exact algebra gives

> `W=uB+ps-pua+J`,

hence

> **DIRECTIONAL DEFICIENCY--HAMMING BUDGET**
>
> `J+H/2+P_alpha`
>
> `<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.           `(DHB)`

For fixed `lambda`, the preserved `h_alpha,q=O(p^(3/2))`, `E_U=O(p)` bounds imply

> `limsup u/p<=2`.                                        `(DR2)`

File: `DIRECTIONAL_BETA_FIBRE_MOMENT_AND_RATIO_TWO.md`.

The earlier central-Hamming and threshold-free moment inequalities remain preserved but are superseded asymptotically by `(DHB)`.

## 7. Ratio-two polarization and bipolar geometry

If a fixed-`lambda` above-threshold sequence were to satisfy `u/p->2`, `(DHB)` forces

`H=o(p^3)`, `J=o(p^3)`.

The A-layer then polarizes into two populations:

- `X`: `|X|=(2+o(1))p`, beta load `p-o(p)` on average and U-degree `p+o(p)` on average;
- `Z=A\X`: `|Z|=(2+o(1))p`, beta load `o(p)` on average and U-degree `2p-o(p)` on average.

The beta-source-pair Hamming injection is asymptotically saturated, and `U` splits into two complementary Boolean clusters of size `p+o(p)`.

The exact beta-side hole identity is stronger. If `x` beta-targets fibre `i` and chooses matched endpoint `q_i'`, the number of same-side vertices of `A union U` which are neither `x` nor adjacent to `x` is

> `epsilon_x-epsilon_{q_i'}`.                             `(BH)`

Thus neighbours of a beta-heavy `x` lie close to `c(x)` and non-neighbours close to `bar c(x)`, with total error paid directly by degree slack. At the ratio-two endpoint the whole `A union U` layer becomes asymptotically bipolar.

Files: `RATIO_TWO_POLARIZATION_AND_SOURCE_PAIR_STABILITY.md`, `BETA_SIDE_HOLE_IDENTITY_AND_BIPOLAR_CODE_GEOMETRY.md`.

## 8. Full beta-load scarcity

If `ell_x=p`, then every radius-one Hamming neighbour of `c(x)` occurs as a U-code. Hypercube incidence gives only `O(1)` possible full-load centre codes when `u=O(p)`, and at `u/p->2` at most four full-load A-witnesses in total.

File: `FULL_BETA_LOAD_HAMMING_SPHERE_SCARCITY.md`.

This exact endpoint is now subsumed by the finite-deficit theorem below.

## 9. New finite-deficit pair capacity

Put

`k_x=p-ell_x`.

For `y_i,y_j in Y_x`, their codes differ in exactly the two assigned coordinates on `I_x`, hence

> `dist_H(c(y_i),c(y_j))<=k_x+2`.

Combined with the source-pair multiplicity theorem

`M(y,z)<=dist_H(c(y),c(z))`,

this yields the exact weighted double count

> **FINITE-DEFICIT PAIR CAPACITY**
>
> `sum_x binom(ell_x,2)/(p-ell_x+2) <= binom(u,2)`.       `(FDP2)`

Therefore, if

`N_K=|{x:k_x<=K}|`,

then

> `N_K <= binom(u,2)(K+2)/binom(p-K,2)`.                 `(FDS2)`

For `u=rho p+o(p)`, `K=o(p)`,

> `N_K<=(rho^2+o(1))K`.

This immediately contradicts the ratio-two polarization, which would require `(2-o(1))p` witnesses with sublinear deficit. Thus **the ratio-two endpoint is impossible**, not merely unstable.

## 10. New source-tuple capacity hierarchy

For every integer `r>=3`, fix an `r`-set `R` of designated sources. In a common witness, each source must be assigned to a coordinate where it is the unique bit minority within `R`; every other nonconstant coordinate of `R` must lie outside the witness target set. Source-coordinate selected-witness uniqueness then gives the exact weighted hierarchy

> **SOURCE-TUPLE CAPACITY**
>
> `sum_x binom(ell_x,r)/(p-ell_x+r)
>  <= (1/r)binom(u,r)`.                                   `(FDPr)`

Hence if `p-K>=r`,

> `|{x:k_x<=K}|`
>
> `<=((K+r)/r) binom(u,r)/binom(p-K,r)`.                 `(FDSr)`

The `r=3` member is stronger than the pair bound near the former ratio-two endpoint.

File: `FINITE_DEFICIT_SOURCE_TUPLE_CAPACITY_AND_RATIO_GAP.md`.

## 11. New quantitative ratio gap: below 27/14

Assume fixed `lambda`, `p->infinity`, and along a subsequence

`u/p->rho<=2`.

From `(DHB)`,

> `J <= [rho(2-rho)/2+o(1)]p^3`,
>
> `H <= [rho(2-rho)+o(1)]p^3`.

Let `j` be the number of fibres with `|d_i|>=p`. Then

`j/p<=gamma+o(1)`, `gamma=rho(2-rho)`.

Let `L={x:ell_x>j}`. Beta-load capacity gives

> `|L|/p >= L_0(rho)+o(1)`,
>
> `L_0(rho)=[rho-(rho+2)gamma]/(1-gamma)`.

Every `x in L` targets a fibre with `|d_i|<p`, so side occupancy gives

`u-d_U(x)>=[(rho-1)/2+o(1)]p`.

Therefore

> `sum_{x in L}k_x <= [D_0(rho)+o(1)]p^2`,
>
> `D_0(rho)=rho(2-rho)/(rho-1)`.

At least

`[L_0(rho)-6D_0(rho)+o(1)]p`

of these witnesses have `k_x<=p/6`. The triple-source capacity gives the opposite upper bound

`(12rho^3/125+o(1))p`.

Thus every feasible limit ratio must satisfy

> `F(rho)=L_0(rho)-6D_0(rho)-12rho^3/125<=0`.

But

`F(rho)`

`=-rho(12rho^4-24rho^3-863rho^2+2250rho-1125)`

` /[125(rho-1)^2]`,

and an elementary derivative check shows

> `F(rho)>0` for every `rho in [27/14,2]`.

At the left endpoint exactly,

`F(27/14)=219672/7245875>0`.

Therefore:

> **TRIPLE-SOURCE RATIO GAP — internal candidate.**
>
> For every fixed `lambda`, every above-`M(n)` near-full sequence with `p->infinity` satisfies
>
> `limsup u/p < 27/14 = 1.928571428...`.                  `(RG3)`

The constant is deliberately non-optimized. Do not spend the next unit merely shaving it numerically.

## 12. New matched-endpoint slack payment

For tight fibre `i`, let endpoint slacks be

`e_i^0,e_i^1`, with

`e_i^0+e_i^1=lambda+1`.

Let beta source counts by side be

`r_i^s=u_i^s-h_i^s`.

The beta-side hole identity gives

> `pL_A>=sum_i(r_i^0e_i^1+r_i^1e_i^0)`.                 `(BES1)`

Hence

> `pL_A`
>
> `>=(lambda+1)[(pu-sum_i|d_i|)/2-h_alpha]`.             `(BES2)`

By Cauchy,

> `L_A >= (lambda+1)
>          [u/2-(1/2)sqrt(H/p)-h_alpha/p]`,              `(BES3)`

with the positive part understood.

This is exact and retains `lambda`; it is now the preferred bridge toward weakening the fixed-`lambda` restriction.

File: `BETA_MATCHED_ENDPOINT_SLACK_BALANCE_PAYMENT.md`.

## 13. Verification at this checkpoint

New audit support:

`check_finite_deficit_source_tuple_capacity.py`

- 304,264 exact local triple-source geometry cases (`p<=6`, beta deficit `<=2`);
- 2,001 exact rational ratio-grid points on `[27/14,2]`;
- exact cutoff arithmetic and polynomial signs;
- zero failures.

Frozen summary: `FINITE_DEFICIT_SOURCE_TUPLE_CHECK_SUMMARY.json`.

Earlier dense-cross Hamming, threshold-capacity, moment-capacity, multiplicity/fan, and Boolean-incidence regression suites remain preserved. Computation is audit support only; the promoted internal statements are hand arguments.

## 14. Full-tight branch remains closed internally

If tight antipodes cover all of `B`, the fixed switching-defect hierarchy remains internally closed for `k>=19`; see `FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`. The order-12/32 `X_3` graph is a small full-tight `k=4,r=0` exception and remains explicitly allowed.

Do not reopen the fixed-defect ladder as the main attack.

## 15. Active next move

The ratio-two equality model has now been destroyed, and the source-tuple hierarchy gives a quantitative fixed-`lambda` gap. The next move should **not** optimize `27/14` as a decimal constant.

Highest-value structural target:

1. combine `(FDPr)`, `(BH)/(BES2)`, `(DHB)`, and the scorecard `(GS-A)` into a joint inequality for the distribution of `(k_x,epsilon_x,d_U(x))`;
2. use it to force direct payment in `E_U+L_A`, rather than another ratio-only restriction;
3. in parallel, use `(BES2)` to test whether positive/growing `lambda` can be absorbed, weakening the current fixed-`lambda` assumption.

A natural approach is a finite dyadic decomposition by beta deficit `k_x`: tuple capacity controls the number of low-deficit witnesses, `(DHB)` controls the product of beta and U-degree deficits, and `(BH)` prices low-slack witnesses which try to exhaust many fibre sides.

The separate `Q=0` / false-twin-core branch from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` remains open and has not been conflated with this triangle/partial-Boolean branch.

Do not return to the closed mixed `{4,5}` selected-excess ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742.

## 16. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form, scorecard, switching stability, multiplicity Hall, fan payment, U-edge capacity, beta-reuse geometry, directional Hamming budget, beta-side hole identity, finite-deficit pair/tuple capacity, and endpoint-slack payment are hand arguments.
- `(RG3)` is conditional on fixed `lambda`; it is not a global eventual theorem.
- No all-order second-extremal theorem is claimed.
- Finite computations/checkers are audit/regression support only.
<!-- CURRENT-STATUS:END -->