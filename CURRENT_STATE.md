# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_HIGH_COMPLEXITY_BETA_MULTIPLICITY_SPARSE_U_DENSE_AU_INTERNAL_CANDIDATES`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19` in the preserved theorem). The active branch is the unmatched/errorful antipode regime. Earlier work forced every above-`M(n)` linearly-unmatched candidate into high switching complexity, high unmatched-row cover, and small projective alpha classes. This checkpoint obtains the first genuinely aggregate Hall consequences in that regime: **multiplicity-level beta injectivity, small U-code classes, linear proliferation of complementary U-code types, asymptotic sparsity of `G[U]`, and a quadratically dense A--U layer whose beta witnesses have strong fibrewise exclusion geometry.**

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

## 3. Preserved A-side quadratic switching stability

The matched-target private-foot theorem gives, for a critical matched-core edge certified by `h in A`,

`epsilon_h>=epsilon_t'+1`.

If after switching there is a zero-signed induced subcore on `s_0>=3` tight fibres, clique criticality amplifies this to

> `L_A>=s_0(s_0-1)`.                                      `(ZS)`

Define the switching-deletion invariant

`kappa_sw=min_S tau_vc(L Delta delta(S))`

for the matched signing, and put

`sigma_0=p-kappa_sw`.

Then `sigma_0` is the largest zero-signed subcore obtainable after switching, so every above-threshold candidate must satisfy

> `sigma_0(sigma_0-1)<=S_req-2`.                          `(SD)`

In particular, for fixed `lambda` and `u=O(p)`,

> `kappa_sw=p-O(sqrt(p))`.

The exact `tau(Psi)<=2` unmatched-row classification is already absorbed by this theorem: every such row leaves a zero-signed subcore of size at least `p-2`, hence has quadratic `L_A` cost. Do not return to case-by-case cheap-row enumeration.

Files: `ZERO_SIGNING_SUBCORE_QUADRATIC_SLACK_AND_TAU2_ROWS.md`, `SWITCHING_DELETION_STABILITY_FROM_A_SLACK.md`.

## 4. High row cover and small alpha classes

Put

`C=S_req-2`,

`R=floor((1+sqrt(1+4C))/2)`,

`R_*=max(2,R)`.

The row-kernel theorem and `(ZS)` imply that every unmatched row of an above-threshold candidate satisfies

> `tau(Psi(K_y))>=ceil(p/(R_*+1))`.                       `(RC)`

The projective-twin theorem identifies

`mu_alpha=max_c |alpha^{-1}(c)|`

with the largest true-twin clique obtainable by switching the matched 2-lift. Hence

> `mu_alpha<=R_*`.                                         `(AC)`

For fixed `lambda` and `u=O(p)`, every unmatched row has cover `Omega(sqrt(p))`, while every projective alpha class has size `O(sqrt(p))`.

File: `ROW_COVER_AND_ALPHA_CAP_FROM_SLACK_STABILITY.md`.

## 5. Preserved antipode-fan payment

For a U--U antipode hub `z`, with partner set `Y` of size `d`,

`sum_{y in Y}eta(yz)>=binom(d,2)+bar e(G[Y])`.

Consequences retained:

- `lambda=-1`: `E_U>=ceil(u/4)`;
- `lambda>=0`: `E_U>=min(u,ceil(u/2)+lambda)`;
- equality forces odd clique fan sets, regular tournament charging and private complementary-code holes.

This checkpoint extends the same Boolean fan injection to **matched antipode hubs** whenever their unmatched partner set has one common partial code; matched antipode partners automatically do.

File: `BOOLEAN_ANTIPODE_FAN_PAYMENT.md` plus the new `BETA_MULTIPLICITY_CODE_PAIR_STABILITY.md`.

## 6. New multiplicity row-edge theorem

Group unmatched vertices by partial Boolean code:

`t_c=|{y in U:c(y)=c}|`,

and A-vertices by

`n_d=|{x in A:c(x)=d}|`.

For an occupied U-code `c` and coordinate `i`, all `t_c` physical P--U edges have the same two possible witness codes

`a_i(c)=alpha(q_i(c))`,

`b_i(c)=beta_i(c)`.

The old per-source rule gives alpha capacity `n_{a_i(c)}`. The new point is **beta-target injectivity**: for a fixed matched target `q`, one A-vertex cannot beta-certify two distinct edges incident with `q`, because beta criticality requires

`N(x) cap N(q)={y}`.

Therefore

> `t_c <= n_{a_i(c)}+n_{b_i(c)}` for every `c,i`.        `(MH)`

If `nu_c` is the matching number of the row-singleton graph `Psi(K_c)`, summing `(MH)` over a code-disjoint row matching gives

> `nu_c t_c<=a`,

so

> `t_c<=floor(a/nu_c)`
>
> `   <=floor(a/ceil(tau(Psi(K_c))/2))`.                  `(MC)`

Together with `(RC)`, every exact U-code class has size `O(sqrt(p))` when `u=O(p)`.

This is a genuine multiplicity theorem, not a support statement.

## 7. New complementary-pair mass cap

For complementary U-codes `c,bar c`, their row graphs are the same switching row, their selected matched endpoints are tight mates, and their beta pools are disjoint for `p>=3`.

Summing `(MH)` over both sides of one complementary pair `gamma={c,bar c}` gives

> `p(t_c+t_bar c)<=(mu_alpha+1)a`.                       `(CP)`

Hence

> `t_c+t_bar c<=floor((mu_alpha+1)a/p)`.

Using `(AC)`, every complementary U-code pair has total mass

> `O(sqrt(p))`

in the linearly-unmatched regime.

File: `BETA_MULTIPLICITY_CODE_PAIR_STABILITY.md`.

## 8. New global beta-pool proliferation theorem

Let `H` be the occupied complementary U-code pairs and `h=|H|`. For a pair `gamma={c,bar c}`, let

`S_gamma=B(c) union B(bar c)`

be its two disjoint beta spheres.

The global alpha-spill theorem gives

`B_beta>=pu-W_alpha>=pu-mu_alpha a`.

Beta-target injectivity gives, pairwise,

`B_beta(gamma)<=sum_{d in S_gamma}n_d`.

Hypercube incidence is exact: every Boolean A-code lies in exactly `p` complementary-pair beta unions over the whole cube. Hence over the `h` occupied pairs it is counted at most `min(h,p)` times. Therefore

> **BETA-POOL PROLIFERATION**
>
> `min(h,p)a>=pu-mu_alpha a`.                             `(BP)`

In particular

> `h>=max(0,ceil(pu/a-mu_alpha))`.

With `(AC)`, if `u=cp+O(1)` for fixed `c>0` and fixed `lambda`, then

> `h >= [c/(2+c)]p-O(sqrt(p))`.

Thus a linear unmatched layer forces **linearly many complementary Boolean code-pair types**. It cannot hide in a bounded or square-root family of reusable rows.

This is the first aggregate selected/Hall theorem in the high-complexity regime that scales linearly with `p`.

## 9. New antipode payment by code-pair type

### One-sided alpha-image classes

If `t_c=t>0` but `t_bar c=0`, then no U--U antipode is available, so every vertex of the class must use a matched antipode from

`R_c={q in P:alpha(q)=c}`.

Let `r_c=|R_c|`. If `r_c=0`, the one-sided class is impossible. Assign the `t` vertices to matched antipode hubs and let `d_q` be the load at hub `q`. The extended partial-Boolean fan theorem gives

`E_c>=max(t,sum_q binom(d_q,2))`.

If `t=r_c k+s`, `0<=s<r_c`, the convex minimum is

`Phi(t,r_c)=r_c binom(k,2)+s k`,

so

> `E_c>=max(t,Phi(t,r_c))`.                               `(OS)`

Since `r_c<=mu_alpha`, concentration beyond the available alpha hubs incurs quadratic branching slack.

### Generic non-alpha complementary pairs at lambda=-1

If

`|alpha^{-1}(c)|=|alpha^{-1}(bar c)|=0`,

then every vertex on either occupied side must use a U--U antipode in the opposite code class. Writing side sizes `t,s` and slack sums `E_c,E_bar`, zero-slack fan capacity gives

`t<=E_c+3E_bar`,

`s<=3E_c+E_bar`.

Therefore

> `E_c+E_bar>=ceil(max((t+s)/4,t/3,s/3))`.               `(GI)`

This recovers the old quarter-slack floor when the pair is balanced and is stronger for imbalanced generic pairs. Thus low slack forces generic complementary code pairs to be approximately balanced; heavily one-sided behaviour must pass through the exceptional alpha image and then pays `(OS)`.

## 10. New capacity theorem for edges inside U

For every U--U edge `yz`, the augmented orientation constraint is

`{bar c(y),bar c(z)}`.

Orient the edge according to its canonical selected B-source. Distinct obligations from a fixed source use distinct A-cross edges, so

> `d^+(y)<=n_{bar c(y)}`.

Hence for every `S subseteq U`,

> `e(G[S])<=sum_{y in S}n_{bar c(y)}`.                   `(UE)`

In particular

`q<=sum_c t_c n_bar c<=t_max a`.

Using `(CP)`,

> `q <= a floor((mu_alpha+1)a/p)`
>
> `  <= (mu_alpha+1)a^2/p`.                              `(SU)`

With `(AC)` and `u=O(p)`, fixed `lambda`,

> `q=O(p^(3/2))`.

Thus if `u=Theta(p)`, the unmatched induced graph is asymptotically sparse:

> `q/binom(u,2)=O(p^(-1/2))`.

The exact rooted-triangle count is correspondingly

`Q=p(p+u-1)+O(p^(3/2))`.

File: `UNMATCHED_INTERNAL_EDGE_CAPACITY.md`.

## 11. Sparse U forces a quadratically dense A--U layer

From the exact slack identity,

`s=u(p+u-1)-2q-E_U`.

Combining `(SU)` with `(GS-A)` gives the parameter-level necessary condition

> `s >= u(p+u-1)-2(R_*+1)a^2/p-(S_req-2)`.              `(AU)`

If `u=cp+O(1)`, fixed `c>0`, fixed `lambda`, then

> `s >= c(1+c)p^2-O(p^(3/2))`.

Therefore the surviving high-complexity linear-unmatched regime has a sharp two-layer shape:

- `G[U]` is sparse: `q=O(p^(3/2))`;
- the A--U cross graph is dense: `s=Theta(p^2)`.

The unmatched vertices must replace almost all missing U-neighbours by A-neighbours.

## 12. New beta-witness reuse geometry

For `x in A`, let `ell_x` be the number of beta-oriented P--U obligations whose selected cross edge uses `x`. Then

`sum_x ell_x=B_beta>=pu-mu_alpha a`.

Criticality of a beta-certified edge `yq` gives

`x~y`, `x not~q`, `N(x) cap N(q)={y}`.

Consequences:

1. one `x` can beta-certify at most one target in each tight fibre, so `ell_x<=p`;
2. if `I_x` is the set of its beta target fibres, then for each `i in I_x`, every other A/U-neighbour of `x` avoids the target endpoint `q_i` and therefore chooses its tight mate;
3. the designated beta source in fibre `i` is the unique neighbour allowed to choose `q_i`.

Thus outside its `ell_x` designated beta sources, every A/U-neighbour of `x` lies in one codimension-`ell_x` tight-fibre transversal class; the designated sources are the one-coordinate deviations from that class.

The load bounds are

> `|{x:ell_x>0}|>=ceil(u-mu_alpha a/p)`,                  `(BL1)`

and

> `max_x ell_x>=ceil(pu/a-mu_alpha)`.                     `(BL2)`

Using `(AC)`, when `u=cp+O(1)` these become

> linearly many beta-loaded A-vertices, and
>
> `max_x ell_x >= [c/(2+c)]p-O(sqrt(p))`.

Indeed the **average** beta load over A is already linear in `p`.

File: `BETA_WITNESS_REUSE_GEOMETRY.md`.

## 13. Verification added at this checkpoint

`check_beta_multiplicity_code_pair_stability.py` independently checks the nontrivial finite/algebraic interfaces used above:

- all 21 D2C graph-atlas classes through order seven and all 126 rooted vertices were inspected;
- 17 rooted instances contained a tight pair;
- the genuinely new matched-hub Boolean fan case occurred once, with two unmatched partners, zero code failures and zero BAF violations (minimum margin `2`);
- complementary beta-pool disjointness and exact `p`-fold complement-pair incidence were checked on 1,020 complement pairs and 2,040 code incidences for `p=3,...,10`, with zero failures;
- the rounded generic-pair imbalance lower bound was replayed on 1,681 integer cases, with zero failures.

Frozen summary: `BETA_MULTIPLICITY_CODE_PAIR_CHECK_SUMMARY.json`.

These checks are regression evidence only; the promoted internal candidate statements are based on the hand injections and counts in the notes.

## 14. Full-tight branch remains closed internally

If tight antipodes cover all of `B`, the fixed switching-defect hierarchy remains internally closed for `k>=19`; see `FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`. The full-tight order-12/32 `X_3` hostile control is a small `k=4,r=0` exception and remains explicitly allowed.

Do not reopen the fixed-defect ladder as the main attack.

## 15. Active next move

The aggregate Hall target from the previous checkpoint has now partly succeeded. In the linear-unmatched high-complexity regime, a survivor must simultaneously have

- high switching-deletion distance `p-O(sqrt(p))`;
- row cover `Omega(sqrt(p))` at every unmatched vertex;
- alpha classes `O(sqrt(p))`;
- linearly many complementary U-code-pair types;
- only `O(sqrt(p))` vertices per complementary pair;
- `q=O(p^(3/2))` internal U-edges;
- `s=Theta(p^2)` A--U edges;
- linearly many A-vertices carrying beta witness loads on linearly many distinct tight fibres, with codimension-Theta(p) exclusion patterns on their other neighbours.

The next compact theorem should aggregate those **beta-reuse exclusion patterns across the dense A--U layer**. A natural double count is over triples `(x,z,i)` with `xz in E(A,U)` and `i` one of the beta target fibres used by `x`: except for the unique designated source at coordinate `i`, every such `z` is forced onto the mate side of that fibre. The goal is to show that the quadratic cross density `(AU)` is incompatible with the linear complementary-code proliferation `(BP)` unless the forced fibre choices create enough `E_U` or `L_A` to violate `(GS-A)`.

A secondary open branch remains `Q=0` / false-twin core from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md`; it has not been conflated with the partial-Boolean triangle branch.

Do not return to the closed mixed `{4,5}` ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742.

## 16. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure; no author-supplied adjacency file has been located.
- Full-tight eventual closure is an internal candidate pending external review.
- The near-full normal form, exact slack criterion, Boolean fan theorem, A-side quadratic switching theorem, multiplicity Hall inequalities, beta-pool proliferation, U-edge capacity and beta-reuse geometry are hand arguments.
- Finite computations/checkers are audit and regression support only.
- The new results do **not** yet close all unmatched/errorful configurations; the dense A--U exclusion double count remains open.
- The `Q=0` / false-twin-core branch remains separate and open.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->