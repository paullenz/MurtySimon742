# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_THRESHOLD_FREE_MOMENT_CAPACITY_INTERNAL_CANDIDATE`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19` in the preserved theorem). The live branch is the unmatched/errorful antipode regime. Earlier work forced linearly-unmatched candidates into high switching complexity, small alpha capacity, sparse `G[U]`, and a quadratically dense `A--U` layer. The current checkpoint converts beta-witness reuse first into an exact Hamming-energy budget and then into a **threshold-free moment capacity inequality**. For fixed `lambda`, this sharpens the surviving linear-unmatched ratio from the old `u/p<=4+o(1)` endpoint through `31/8` to

> `u <= (2+sqrt(2))p+O(sqrt(p))`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory hostile control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. It has `u=0`, so every unmatched-layer theorem below leaves it untouched.

## 2. Near-full partial-Boolean framework

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

## 3. Preserved high-complexity stability

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

Files: `ZERO_SIGNING_SUBCORE_QUADRATIC_SLACK_AND_TAU2_ROWS.md`, `SWITCHING_DELETION_STABILITY_FROM_A_SLACK.md`, `ROW_COVER_AND_ALPHA_CAP_FROM_SLACK_STABILITY.md`.

## 4. Preserved multiplicity Hall and antipode structure

For an occupied U-code `c` and coordinate `i`, beta-target injectivity gives

> `t_c <= n_{a_i(c)}+n_{b_i(c)}`.                         `(MH)`

If `nu_c` is the matching number of the row-singleton graph,

> `nu_c t_c<=a`.                                          `(MC)`

For complementary U-codes,

> `p(t_c+t_bar c)<=(mu_alpha+1)a`.                        `(CP)`

If `h` is the number of occupied complementary U-code pairs, exact beta-pool incidence gives

> `min(h,p)a>=pu-mu_alpha a`.                             `(BP)`

Thus for fixed `lambda`, `u=Theta(p)`, each exact code class/complementary pair has only `O(sqrt(p))` mass while linearly many complementary code-pair types are occupied.

The Boolean antipode-fan payment remains preserved:

- `lambda=-1`: `E_U>=ceil(u/4)`;
- `lambda>=0`: `E_U>=min(u,ceil(u/2)+lambda)`;
- equality is rigid (odd clique fan, regular tournament charging, complementary private holes);
- matched antipode hubs satisfy the corresponding same-code fan inequality.

Files: `BOOLEAN_ANTIPODE_FAN_PAYMENT.md`, `BETA_MULTIPLICITY_CODE_PAIR_STABILITY.md`.

## 5. Sparse U, dense A--U

Selected orientation of edges inside `U` gives, for every `S subseteq U`,

> `e(G[S])<=sum_{y in S}n_{bar c(y)}`.                    `(UE)`

Using `(CP)`,

> `q <= a floor((mu_alpha+1)a/p)`
>
> `  <= (mu_alpha+1)a^2/p`.                               `(SU)`

Therefore, for fixed `lambda`, `u=O(p)`,

> `q=O(p^(3/2))`,

and for `u=Theta(p)`,

> `Q=p(p+u-1)+O(p^(3/2))`.

The exact unmatched-slack identity then forces

> `s=u(p+u-1)-2q-E_U`
>
> ` =Theta(p^2)`                                          `(AU)`

through the above-threshold linear-unmatched regime. More precisely, if `u=rho p+O(1)`, then

> `s=rho(1+rho)p^2+O(p^(3/2))`.

File: `UNMATCHED_INTERNAL_EDGE_CAPACITY.md`.

## 6. Beta-reuse geometry and exact beta/central partition

For `x in A`, let `ell_x` be its beta load and `I_x` its beta target fibres. For `i in I_x`, let `y_i` be the designated unmatched source.

The selected/Hall per-source injectivity implies that the `y_i` are pairwise distinct for fixed `x`: otherwise one physical cross edge `xy` would be selected for two distinct beta obligations from the same source.

Put

`Y_x={y_i:i in I_x}`,

`C_x=N_U(x)\Y_x`,

`c_x=|C_x|`.

Then

> `d_U(x)=ell_x+c_x`.

Writing

`B=sum_x ell_x=B_beta`,

`C=sum_x c_x`,

there is an exact partition

> `s=B+C`.                                                 `(BC)`

Criticality gives `ell_x<=p`. For every `i in I_x`, all U-neighbours of `x` except the single source `y_i` choose the same side of fibre `i` as `x`.

File: `BETA_WITNESS_REUSE_GEOMETRY.md`, with the explicit source-distinctness audit in `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`.

## 7. Central-triple Hamming theorem

For coordinate `i`, write

`u_i^0=|{y in U:c(y)_i=0}|`,

`u_i^1=|{y in U:c(y)_i=1}|`,

`d_i=u_i^0-u_i^1`,

`H=sum_i d_i^2`.

The triples

`(x,z,i)` with `z in C_x`, `i in I_x`

inject into ordered U-code coordinate disagreements by

`(x,z,i) -> (y_i,z,i)`.

Hence, with

`T=sum_x ell_x c_x`,

> `T+H/2<=p u^2/2`.                                       `(CH)`

This is a hand injection.

Define

`Z=sum_x(p-ell_x)(u-c_x)>=0`,

and let

`h_alpha=pu-B`.

Exact algebra gives

> `T=p u(u-2p+lambda)`
>
> `  -(u-p)h_alpha-2pq-pE_U+Z`.

Therefore

> **DENSE-CROSS HAMMING BUDGET**
>
> `Z+H/2`
>
> `<=p u(2p-lambda-u/2)`
>
> `  +(u-p)h_alpha+2pq+pE_U`.                              `(HB)`

For `u>=p`, `h_alpha<=mu_alpha a`. The coarse consequence in the fixed-`lambda`, linear-unmatched regime is

> `u<=4p-2lambda+O(sqrt(p))`.

File: `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`.

## 8. Loaded-witness side occupancy and finite threshold capacity

For every beta-loaded `x` and every `i in I_x`, all U-neighbours except `y_i` lie on one side of coordinate `i`, so

> `d_U(x)-1<=(u+|d_i|)/2`.                                `(SO)`

For any `t>0`, let

`J_t={i:|d_i|>=t}`, `j_t=|J_t|`,

`L_t={x:ell_x>j_t}`, `l_t=|L_t|`.

Then

> `j_t<=H/t^2`,

and every `x in L_t` has

> `d_U(x)<=(u+t)/2+1`.

Beta-load capacity gives

> `l_t >= max(0,(B-a j_t)/(p-j_t))`                       `(TC1)`

when `j_t<p`, while cross-edge capacity gives

> `s<=au-l_t(u-t-2)/2`                                    `(TC2)`

when `u>t+2`.

Choosing `t=(7/5)p` and combining `(HB)`, `(TC1)`, `(TC2)` yields the exact asymptotic internal candidate

> `u < (31/8)p`

for all sufficiently large fixed-`lambda` linearly-unmatched above-threshold candidates.

This remains preserved as a finite-threshold tool, but is superseded asymptotically by the moment theorem below.

File: `DENSE_CROSS_THRESHOLD_CAPACITY_REFINEMENT.md`.

## 9. New threshold-free moment capacity theorem

The side-occupancy lemma can be summed without selecting `t`.

Let

`d_x=d_U(x)`,

`phi(t)=(2t-u-2)_+^2`.

For every `i in I_x`, `(SO)` gives

`|d_i| >= (2d_x-u-2)_+`.

If

`r_i=|{x:i in I_x}|`,

then `r_i<=u` because fibre `i` has at most one beta-selected P--U obligation per unmatched source. Hence

> `sum_x ell_x phi(d_x) <= sum_i r_i d_i^2 <= uH`.        `(MU)`

Now put

`W=sum_x ell_x d_x`.

Since `(p-ell_x)(u-d_x)>=0`,

> `W>=uB+ps-pua`.                                         `(MW)`

Weighted Jensen with weights `ell_x/B` and the convex nondecreasing `phi` therefore yields the exact finite inequality

> **THRESHOLD-FREE MOMENT CAPACITY THEOREM**
>
> `B * [2(uB+ps-pua)/B-u-2]_+^2 <= uH`.                  `(MCAP)`

Equivalently,

> `B * [u+2p(s-ua)/B-2]_+^2 <= uH`.

This is now the strongest compact dense-cross inequality in the project.

File: `DENSE_CROSS_MOMENT_CAPACITY_THEOREM.md`.

## 10. New strongest linear-unmatched ratio bound

Assume `lambda` fixed and

`u=rho p+o(p)`

along an above-`M(n)` sequence.

The preserved alpha-spill and sparse-U bounds give

> `B=rho p^2+O(p^(3/2))`,
>
> `s=rho(1+rho)p^2+O(p^(3/2))`,
>
> `a=(rho+2)p+O(1)`.

Thus `(MW)` gives

> `(uB+ps-pua)/B=(rho-1)p+O(sqrt(p))`.

The Hamming budget `(HB)` gives

> `H<=rho(4-rho)p^3+O(p^(5/2))`.

Substitute both into `(MCAP)`. For `rho>2`,

> `rho(rho-2)^2 p^4`
>
> `<=rho^2(4-rho)p^4+O(p^(7/2))`.

Therefore

> `(rho-2)^2<=rho(4-rho)+O(p^(-1/2))`.

The upper root of the limiting quadratic

`rho^2-4rho+2=0`

is exactly

> `rho=2+sqrt(2)`.

Since the derivative of the difference at that root is positive,

> **MOMENT RATIO THEOREM — internal candidate.**
>
> For every fixed `lambda`, every sufficiently large above-`M(n)` near-full candidate in the linear-unmatched regime satisfies
>
> `u <= (2+sqrt(2))p+O(sqrt(p))`.                         `(MR)`

Hence

> `limsup u/p <= 2+sqrt(2)=3.41421356...`.

This substantially supersedes the earlier `4+o(1)` and `31/8` boundaries. It is not asserted for arbitrary growing `lambda`.

## 11. Equality/stability shape at the new frontier

Near equality in `(MR)` requires near equality simultaneously in several independent hand inequalities:

1. `(p-ell_x)(u-d_x)` is small for most beta weight;
2. weighted Jensen is nearly saturated, so beta-weighted U-degrees concentrate near `(rho-1)p`;
3. side occupancy nearly saturates in many target fibres;
4. the global Hamming budget `(HB)` nearly saturates.

This is now a more valuable target than another code-row classification. A successful **stability-of-moment-capacity** theorem should price failure of these simultaneous equality conditions into `E_U+L_A`, which would attack `(GS-A)` directly.

## 12. Verification at this checkpoint

Audit support preserved:

### Dense-cross Hamming suite

`check_dense_cross_hamming_energy_and_ratio_gap.py`

- 5,050 exact U-code multisets for the Hamming-energy identity;
- 1,890 product-identity cases;
- 182,720 exact dense-cross algebra cases;
- zero failures.

Frozen summary: `DENSE_CROSS_HAMMING_ENERGY_CHECK_SUMMARY.json`.

### Threshold-capacity suite

`check_dense_cross_threshold_capacity_refinement.py`

- 121,170 finite beta-load capacity cases;
- exact `31/8` endpoint arithmetic;
- zero failures.

Frozen summary: `DENSE_CROSS_THRESHOLD_CAPACITY_CHECK_SUMMARY.json`.

### Moment-capacity suite

`check_dense_cross_moment_capacity_theorem.py`

- 201,238 finite weighted-degree/Jensen cases;
- exact limiting polynomial/root arithmetic;
- zero failures.

Frozen summary: `DENSE_CROSS_MOMENT_CAPACITY_CHECK_SUMMARY.json`.

Earlier multiplicity/fan graph-atlas and Boolean-incidence regressions remain preserved in `check_beta_multiplicity_code_pair_stability.py`.

These checks are evidence only; the promoted internal candidate statements are hand arguments.

## 13. Full-tight branch remains closed internally

If tight antipodes cover all of `B`, the fixed switching-defect hierarchy remains internally closed for `k>=19`; see `FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`. The order-12/32 `X_3` graph is a small full-tight `k=4,r=0` exception and remains explicitly allowed.

Do not reopen the fixed-defect ladder as the main attack.

## 14. Active next move

The threshold-free moment inequality is the first compact analytic bridge from dense A--U structure to the Hamming budget. The next move should **not** optimize the decimal ratio constant and should not return to row normal forms.

Priority:

1. prove a quantitative **stability version of `(MCAP)`**: if the moment inequality is close to equality, force the beta-weighted A-vertices into the near-equality configurations described above;
2. show those configurations necessarily create additional A-side degree slack `L_A`, antipode error `E_U`, or forbidden reuse in the selected system;
3. feed that payment directly into `(GS-A)`.

A secondary route is to remove or weaken the fixed-`lambda` assumption by retaining the exact `lambda` terms in `(HB)` and `(MCAP)`.

The separate `Q=0` / false-twin-core branch from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` remains open and has not been conflated with this triangle/partial-Boolean branch.

Do not return to the closed mixed `{4,5}` selected-excess ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742.

## 15. Trust boundary

- Published 12/32 graph: reconstructed directly from the authoritative figure; no author-supplied adjacency file located.
- Full-tight eventual closure: internal candidate pending external review.
- Near-full normal form, scorecard, switching stability, multiplicity Hall, fan payment, U-edge capacity, beta-reuse geometry, Hamming budget, threshold capacity, and moment capacity are hand arguments.
- `(MR)` is conditional on fixed `lambda` and the linearly-unmatched `u=Theta(p)` regime; it is not a global eventual theorem.
- Finite computations/checkers are audit/regression support only.
<!-- CURRENT-STATUS:END -->
