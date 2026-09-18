# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_DENSE_CROSS_HAMMING_RATIO_GAP_INTERNAL_CANDIDATES`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19` in the preserved theorem). The active branch is the unmatched/errorful antipode regime. Earlier work forced a linearly-unmatched above-`M(n)` candidate into high switching complexity, high unmatched-row cover, small alpha classes, sparse `G[U]`, and a quadratically dense `A--U` layer. The latest checkpoint converts beta-witness reuse into an exact Hamming-energy ledger and then into a cross-edge capacity bound. For fixed `lambda`, the old asymptotic endpoint `u/p=4` is now separated from the surviving region by an explicit constant gap:

> `u < (31/8)p`

for all sufficiently large candidates in the linear-unmatched regime.

No global eventual second-extremal theorem is claimed.

## 1. Scope and mandatory hostile control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an assumed all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) graph has been reconstructed from Figure 1 and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter 2 and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. Every eventual statement below leaves this `u=0` control untouched.

## 2. Near-full partial-Boolean framework and exact scorecard

For a maximum-degree root `v`, write

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

`Q=e(G[B])`, `F=G[A]`, `delta=b(n-b)-m=r-e(F)`.

Let the complete tight-antipode matching in `B` have `p` pairs `P_i`, and let

`U=B\P`, `u=|U|`, so `b=2p+u`.

Every vertex of `A union U` chooses exactly one endpoint from every tight pair and therefore has a partial Boolean code in `{0,1}^p`. Every two tight fibres are joined by a perfect matching.

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

If `p>=2`, private A-feet for root edges are impossible, so every unmatched `y in U` has an errorful antipode. U--U antipodes have complementary Boolean codes.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`.

Then the exact second-extremal scorecard is

> `m<=M(n)` iff `E_U+L_A>=S_req`,

while parity gives

> `m>M(n) ==> E_U+L_A<=S_req-2`.                         `(GS-A)`

At `lambda=-1`, `S_req=2p+u-2`, so above threshold forces

`E_U+L_A<=2p+u-4`.

Main files: `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`, `GLOBAL_SLACK_DEFECT_CRITERION.md`.

## 3. Preserved A-side switching stability and row complexity

A zero-signed induced matched subcore on `s_0>=3` tight fibres forces

> `L_A>=s_0(s_0-1)`.                                      `(ZS)`

Define

`kappa_sw=min_S tau_vc(L Delta delta(S))`,

`sigma_0=p-kappa_sw`.

Then every above-threshold candidate satisfies

> `sigma_0(sigma_0-1)<=S_req-2`.                          `(SD)`

Put

`C=S_req-2`,

`R=floor((1+sqrt(1+4C))/2)`,

`R_*=max(2,R)`.

Every unmatched row satisfies

> `tau(Psi(K_y))>=ceil(p/(R_*+1))`,                       `(RC)`

and the largest projective alpha/true-twin class satisfies

> `mu_alpha<=R_*`.                                         `(AC)`

For fixed `lambda` and `u=O(p)`, this means

- `kappa_sw=p-O(sqrt(p))`;
- every unmatched row has cover `Omega(sqrt(p))`;
- every alpha class has size `O(sqrt(p))`.

Files: `ZERO_SIGNING_SUBCORE_QUADRATIC_SLACK_AND_TAU2_ROWS.md`, `SWITCHING_DELETION_STABILITY_FROM_A_SLACK.md`, `ROW_COVER_AND_ALPHA_CAP_FROM_SLACK_STABILITY.md`.

## 4. Preserved multiplicity Hall / code-pair structure

Group unmatched vertices by partial Boolean code:

`t_c=|{y in U:c(y)=c}|`,

and A-vertices by

`n_d=|{x in A:c(x)=d}|`.

For each occupied U-code `c` and coordinate `i`, beta-target injectivity gives

> `t_c <= n_{a_i(c)}+n_{b_i(c)}`.                         `(MH)`

If `nu_c` is the matching number of `Psi(K_c)`, then

> `nu_c t_c<=a`.                                           `(MC)`

For complementary U-codes,

> `p(t_c+t_bar c)<=(mu_alpha+1)a`.                        `(CP)`

Hence every exact U-code class and every complementary code pair has only `O(sqrt(p))` unmatched vertices when `u=O(p)` and `lambda` is fixed.

Let `h` be the number of occupied complementary U-code pairs. Exact beta-pool incidence gives

> `min(h,p)a>=pu-mu_alpha a`,                              `(BP)`

so if `u=cp+O(1)`, then

> `h >= [c/(2+c)]p-O(sqrt(p))`.

Thus a linear unmatched layer must proliferate over linearly many complementary Boolean types.

File: `BETA_MULTIPLICITY_CODE_PAIR_STABILITY.md`.

## 5. Preserved antipode payment

For a U--U antipode hub `z`, with partner set `Y` of size `d`,

`sum_{y in Y}eta(yz)>=binom(d,2)+bar e(G[Y])`.

Consequences retained:

- `lambda=-1`: `E_U>=ceil(u/4)`;
- `lambda>=0`: `E_U>=min(u,ceil(u/2)+lambda)`;
- equality forces odd clique fan sets, regular tournament charging and private complementary-code holes.

The same Boolean fan injection extends to matched antipode hubs whose unmatched partners share one code. One-sided code classes therefore pay either linear unmatched slack or quadratic hub-branching slack; generic non-alpha complementary pairs at `lambda=-1` satisfy the preserved imbalance floor

`E_c+E_bar>=ceil(max((t+s)/4,t/3,s/3))`.

Files: `BOOLEAN_ANTIPODE_FAN_PAYMENT.md`, `BETA_MULTIPLICITY_CODE_PAIR_STABILITY.md`.

## 6. Sparse U and dense A--U

For every `S subseteq U`, selected orientation of U--U edges gives

> `e(G[S])<=sum_{y in S}n_{bar c(y)}`.                    `(UE)`

Using `(CP)`,

> `q <= a floor((mu_alpha+1)a/p)`
>
> `  <= (mu_alpha+1)a^2/p`.                               `(SU)`

For fixed `lambda` and `u=O(p)`,

> `q=O(p^(3/2))`.

Thus for `u=Theta(p)`, `G[U]` is asymptotically sparse and

`Q=p(p+u-1)+O(p^(3/2))`.

The exact unmatched-slack identity then forces

> `s >= u(p+u-1)-2(R_*+1)a^2/p-(S_req-2)`.               `(AU)`

Hence if `u=cp+O(1)`,

> `s >= c(1+c)p^2-O(p^(3/2))`.

So the surviving layer has sparse `U` but quadratically dense `A--U`.

File: `UNMATCHED_INTERNAL_EDGE_CAPACITY.md`.

## 7. Beta-witness reuse geometry, now with source-distinctness explicit

For `x in A`, let `ell_x` be the number of beta-oriented P--U obligations whose selected cross edge uses `x`, and let `I_x` be the corresponding target fibres.

For each `i in I_x`, let `y_i in U` be the designated beta source. The predecessor selected/Hall theorem says distinct beta obligations from one fixed unmatched source use distinct selected cross edges. Therefore, for fixed `x`, the sources

> `y_i`, `i in I_x`, are pairwise distinct.

This closes an implicit injectivity point in the earlier reuse note.

Put

`Y_x={y_i:i in I_x}`,

`C_x=N_U(x)\Y_x`,

`c_x=|C_x|`.

Then

> `d_U(x)=ell_x+c_x`,

and, writing

`B=sum_x ell_x=B_beta`,

`C=sum_x c_x`,

there is an **exact beta/central partition**

> `s=B+C`.                                                 `(BC)`

Criticality still gives `ell_x<=p`; for every `i in I_x`, all U-neighbours of `x` except the single designated source `y_i` choose the same side of fibre `i` as `x`.

File: `BETA_WITNESS_REUSE_GEOMETRY.md`, with the explicit source-distinctness audit recorded in `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`.

## 8. New central-triple Hamming theorem

Fix 0/1 labels on the tight fibres. For coordinate `i`, let

`u_i^0=|{y in U:c(y)_i=0}|`,

`u_i^1=|{y in U:c(y)_i=1}|`,

`d_i=u_i^0-u_i^1`,

`H=sum_i d_i^2`.

Consider triples

`(x,z,i)` with `z in C_x` and `i in I_x`.

Their number is

> `T=sum_x ell_x c_x`.

Map `(x,z,i)` to `(y_i,z,i)`. The selected beta representative makes this map injective, and beta criticality forces `y_i,z` to disagree in coordinate `i`.

The total number of ordered coordinate disagreements among U-codes is exactly

> `D_U=2 sum_i u_i^0u_i^1`
>
> `   =p u^2/2-H/2`.

Therefore

> **CENTRAL-TRIPLE HAMMING THEOREM**
>
> `T+H/2<=p u^2/2`.                                       `(CH)`

This is a hand injection, not a scan-derived statement.

File: `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`.

## 9. New exact dense-cross Hamming stability budget

Define

> `Z=sum_x(p-ell_x)(u-c_x)>=0`,

and let

> `h_alpha=pu-B`.

The exact identities

`ell_x c_x=u ell_x+p c_x-pu+(p-ell_x)(u-c_x)`

and `s=B+C` give

> `T=(u-p)B+ps-pua+Z`.

Since `B=pu-h_alpha` and `s=u(p+u-1)-2q-E_U`, this simplifies exactly to

> `T=p u(u-2p+lambda)`
>
> `  -(u-p)h_alpha-2pq-pE_U+Z`.

Combining with `(CH)` gives

> **DENSE-CROSS HAMMING BUDGET**
>
> `Z+H/2`
>
> `<=p u(2p-lambda-u/2)`
>
> `  +(u-p)h_alpha+2pq+pE_U`.                              `(HB)`

When `u>=p`, use

`h_alpha<=W_alpha<=mu_alpha a`

to obtain the parameter-level version. Dropping `Z,H>=0` gives

> `u(u/2-2p+lambda)`
>
> `<=((u-p)/p)mu_alpha a+2q+E_U`.                         `(HN)`

For fixed `lambda`, `u=O(p)`, the right side is `O(p^(3/2))`, so first

> `u<=4p-2lambda+O(sqrt(p))`.

The important object for the next work is the full budget `(HB)`, not this coarse first ratio bound.

## 10. New loaded-witness side-occupancy lemma

The reuse geometry yields a stronger statement than merely putting `C_x` on one fibre side.

For `x` with `ell_x>0` and every `i in I_x`, **all** U-neighbours of `x` except `y_i` choose the same side of fibre `i` as `x`. Thus

> `d_U(x)-1<=max(u_i^0,u_i^1)`
>
> `         =(u+|d_i|)/2`.                                `(SO)`

Equivalently,

> `|d_i| >= (2d_U(x)-u-2)_+` for every `i in I_x`.

For any real threshold `t>0`, put

`J_t={i:|d_i|>=t}`, `j_t=|J_t|`.

Then

> `j_t<=H/t^2`.

If `ell_x>j_t`, some target fibre lies outside `J_t`, so

> `d_U(x)<=(u+t)/2+1`.                                    `(SO-t)`

This is the bridge from Hamming balance to cross-edge capacity.

## 11. New exact threshold capacity lemma

Let

`L_t={x in A:ell_x>j_t}`, `l_t=|L_t|`.

Since vertices outside `L_t` carry at most `j_t` beta obligations and every A-vertex carries at most `p`,

> `B<=l_t p+(a-l_t)j_t`.

Hence, when `j_t<p`,

> `l_t >= max(0,(B-a j_t)/(p-j_t))`.                     `(TC1)`

If also `u>t+2`, side occupancy gives

> `s<=au-l_t(u-t-2)/2`.                                   `(TC2)`

Together `(TC1)`--`(TC2)` form the **THRESHOLD CAPACITY LEMMA**. This is a finite-parameter inequality; it does not depend on taking a limit.

File: `DENSE_CROSS_THRESHOLD_CAPACITY_REFINEMENT.md`.

## 12. New explicit unmatched-ratio gap: 31/8

Now assume `lambda` fixed and an above-`M(n)` linear-unmatched sequence with

`u=rho p+o(p)`.

From `(HB)` plus the preserved alpha, `q` and slack bounds,

> `H<=rho(4-rho)p^3+O(p^(5/2))`                           `(HI)`

through the remaining `rho<=4+o(1)` window.

Choose

> `t=(7/5)p`.

Then

> `j_t/p <= (25/49)rho(4-rho)+o(1)`.

Use the **sharp** denominator in `(TC1)` rather than the earlier crude count. Writing `j=j_t/p`, one gets

> `l_t/p >= [rho-(rho+2)j]/(1-j)+o(1)`.

The required cross density is

> `s/p^2=rho(1+rho)+o(1)`,

whereas `(TC2)` gives

> `s/p^2`
>
> `<=rho(rho+2)`
>
> ` -(rho-7/5)/2 * [rho-(rho+2)j]/(1-j)+o(1)`.

Using the largest allowed

`j=(25/49)rho(4-rho)`

reduces feasibility to a rational inequality whose left-minus-right margin is

> `G(rho)`
>
> `=rho(125rho^3-675rho^2+595rho+567)`
>
> ` / [10(25rho^2-100rho+49)]`.

At

> `rho=31/8`,

one has exactly

> `G(31/8)=54343/503680>0`.

The cubic numerator is strictly increasing and positive on `[31/8,4]`, while the denominator is positive there. Hence the whole interval is impossible for sufficiently large `p`.

Therefore:

> **EXPLICIT LINEAR-UNMATCHED RATIO GAP — internal candidate.**
>
> For every fixed `lambda`, every sufficiently large above-`M(n)` near-full partial-Boolean candidate in the linear-unmatched regime satisfies
>
> `u < (31/8)p`.                                          `(RG)`

The constant is deliberately not numerically optimized. The reusable result is the threshold-capacity lemma, not the decimal boundary.

Files:

- `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`;
- `DENSE_CROSS_THRESHOLD_CAPACITY_REFINEMENT.md`.

## 13. Verification at this checkpoint

`check_dense_cross_hamming_energy_and_ratio_gap.py` audits:

- 5,050 exact U-code multisets for the Hamming-energy identity;
- 1,890 product-identity cases;
- 182,720 exact algebra cases for the dense-cross simplification;
- the exact predecessor endpoint polynomial arithmetic.

Frozen summary: `DENSE_CROSS_HAMMING_ENERGY_CHECK_SUMMARY.json`.

`check_dense_cross_threshold_capacity_refinement.py` audits:

- 121,170 finite beta-load capacity cases;
- `G(31/8)=54343/503680`;
- positivity/monotonicity endpoint arithmetic for the cubic numerator.

Frozen summary: `DENSE_CROSS_THRESHOLD_CAPACITY_CHECK_SUMMARY.json`.

Both suites report zero failures. These are regression/audit evidence only; the structural claims rest on the hand injections and inequalities.

The earlier `check_beta_multiplicity_code_pair_stability.py` remains preserved, including its graph-atlas and Boolean incidence audits.

## 14. Full-tight branch remains closed internally

If tight antipodes cover all of `B`, the fixed switching-defect hierarchy remains internally closed for `k>=19`; see `FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`. The full-tight order-12/32 `X_3` hostile control is a small `k=4,r=0` exception and remains explicitly allowed.

Do not reopen the fixed-defect ladder as the main attack.

## 15. Active next move

The dense-cross double count has now paid off. The next move should **not** be another unmatched-row classification and should not merely optimize `31/8` numerically.

The highest-value target is to optimize the joint finite-parameter system

- exact scorecard `(GS-A)`;
- Hamming budget `(HB)`;
- threshold capacity `(TC1)`--`(TC2)`;
- antipode lower bounds on `E_U`;
- alpha cap `(AC)` and U-edge cap `(SU)`;

with the aim of forcing a **direct lower bound on `E_U+L_A`**, rather than only a ratio bound on `u/p`.

Two coherent routes are now visible:

1. derive an analytic load/U-degree/imbalance inequality that absorbs `H` and `Z` without choosing one threshold `t`;
2. feed the threshold-capacity deficit back into degree slack on the A-side, thereby converting failed cross-edge capacity into explicit `L_A` payment.

A secondary open branch remains `Q=0` / false-twin core from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md`; it has not been conflated with the partial-Boolean triangle branch.

Do not return to the closed mixed `{4,5}` ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742.

## 16. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure; no author-supplied adjacency file has been located.
- Full-tight eventual closure is an internal candidate pending external review.
- The near-full normal form, exact slack criterion, Boolean fan theorem, A-side switching theorem, multiplicity Hall inequalities, beta-pool proliferation, U-edge capacity, beta-reuse geometry, central-triple Hamming theorem and threshold-capacity theorem are hand arguments.
- The `31/8` ratio gap is conditional on the fixed-`lambda`, linearly-unmatched regime and is not a global eventual theorem.
- Finite computations/checkers are audit and regression support only.
<!-- CURRENT-STATUS:END -->
