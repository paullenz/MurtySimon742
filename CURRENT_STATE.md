# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_QUADRATIC_A_SLACK_SWITCHING_STABILITY_AND_LARGE_ROW_COVER_INTERNAL_CANDIDATES`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19` in the preserved theorem). The active branch is the unmatched/errorful antipode regime. This checkpoint converts large zero-signed pieces of the tight-pair core into **quadratic A-side degree slack**, prices every exact `tau<=2` unmatched-row kernel, and forces any above-`M(n)` near-full candidate into a high switching-complexity / high row-cover regime.

## 1. Scope and mandatory hostile control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an assumed all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) graph has been reconstructed from Figure 1 and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter 2 and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md` and its checker/summary. Every eventual statement below leaves this control untouched.

## 2. Root / defect and near-full Boolean framework

For a maximum-degree root `v`, write

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

`Q=e(G[B])`, `F=G[A]`, `delta=b(n-b)-m=r-e(F)`.

Let the complete tight-antipode matching in `B` have `p` pairs

`P_i={q_i,q_i'}`, `i=1,...,p`,

and let `U=B\P`, `u=|U|`, so `b=2p+u`.

Every vertex of `A union U` chooses exactly one endpoint from every tight pair, hence has a partial Boolean code in `{0,1}^p`. Every two tight fibres are joined by a perfect matching.

Write `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Exact identities:

`Q=p(p+u-1)+q`,

`r=(p+u)(a-p)+p-s-q`,

`delta=(p+u)(a-p)+p-s-q-f`.

For `epsilon_z=b-d(z)`, put

`E_U=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,

`L_A=sum_{x in A}epsilon_x=a(p+u)-s-2f`.

If `p>=2`, private A-feet for root edges are impossible, so every unmatched `y in U` has an errorful antipode. U--U antipodes have complementary Boolean codes.

Main files: `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`, `GLOBAL_SLACK_DEFECT_CRITERION.md`.

## 3. Exact second-extremal scorecard

Let `T=sum_z epsilon_z`. Then

`T=nb-2m`,

`2 delta=T-b lambda`.

Moreover

> `m<=M(n)` iff `T>=floor(n(lambda+2)/2)-2`,

and parity gives

> `m>M(n) ==> T<=floor(n(lambda+2)/2)-4`.

In the near-full normal form,

`T=p(lambda+1)+E_U+L_A`.

Put

`c_lambda=ceil(lambda(lambda+2)/2)`

and

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`.

Then

> `m<=M(n)` iff `E_U+L_A>=S_req`,

while

> `m>M(n) ==> E_U+L_A<=S_req-2`.                         `(GS-A)`

At `lambda=-1`, `S_req=2p+u-2`, so above threshold forces

`E_U+L_A<=2p+u-4`.

This is the live numerical scorecard.

## 4. Preserved U-antipode/fan structure

For a U--U antipode hub `z`, let `Y=N_{J_U}(z)`, `d=|Y|`. All partners have code `bar c(z)`. The Boolean antipode-fan theorem gives

`sum_{y in Y} eta(yz)>=binom(d,2)+bar e(G[Y])`.

Globally,

`4 sum_{e in E(J_U)}eta(e)`

` >= sum_z d(z)(d(z)-1)+2 sum_z bar e(G[N_{J_U}(z)])`.

Consequences retained at this checkpoint:

- `lambda=-1`: `E_U>=ceil(u/4)`;
- `lambda>=0`: `E_U>=min(u,ceil(u/2)+lambda)`;
- saturated fans force odd clique partner sets, regular tournament charging, and distinct external private holes of the hub code;
- fan Hall capacity gives the true-twin / beta-sphere dichotomy recorded in `SATURATED_FAN_ROW_CAPACITY_DICHOTOMY.md`.

These results remain available but the current advance comes from pricing A-side private feet directly.

## 5. Matched-target private-foot slack transfer

Let `s,t in P` be an edge between matched-core endpoints in distinct fibres and let `t'` be the tight mate of `t`. If `h in A` certifies criticality of `st` from source `s` toward target `t`, so

`h~s`, `h not~t`, `N(h) cap N(t)={s}`,

then every A/U-neighbour of `h` must select `t'`. Comparing degrees of `h` and `t'` gives

> **PRIVATE-FOOT SLACK TRANSFER**
>
> `epsilon_h>=epsilon_t'+1`.                              `(PF)`

This is valid throughout the partial-Boolean near-full regime, not only under a special signing.

File: `MATCHED_PRIVATE_FOOT_SLACK_AND_COMPLETE_ROW_QUADRATIC_EXCLUSION.md`.

## 6. Zero-signing subcore quadratic A-slack theorem

Suppose that after switching there is a coordinate set `R`, `|R|=s_0>=3`, on which every fibre pair is parallel. The selected endpoints on `R` form a clique `K_{s_0}`, and their mates form another `K_{s_0}`.

Rooted clique criticality supplies at least `s_0-1` restricted co-singleton A-code classes from the first clique and at least `s_0-1` restricted singleton classes from the second. These classes give the halfspace separators needed to amplify `(PF)` edge-by-edge: if one A-foot is reused on `t` critical clique edges, its degree slack is at least `t`.

Summing over all physical edges of the two cliques gives the hand theorem

> **ZERO-SIGNING SUBCORE QUADRATIC SLACK**
>
> `L_A>=s_0(s_0-1)`.                                      `(ZS)`

This is the central new A-side pricing result.

Finite support bookkeeping was independently replayed on 705,356 restricted-sphere configurations for subcore sizes `3,...,9`, with zero failures and minimum margin 0. The exact arithmetic reductions were replayed on 1,230,639 integer configurations, also with zero failures. These are audit checks only.

Files:

- `ZERO_SIGNING_SUBCORE_QUADRATIC_SLACK_AND_TAU2_ROWS.md`;
- `check_zero_signing_subcore_quadratic_slack_and_tau2_rows.py`;
- `ZERO_SIGNING_SUBCORE_QUADRATIC_SLACK_AND_TAU2_ROWS_CHECK_SUMMARY.json`.

The earlier full-zero-signing special case gives

`L_A>=p(p-1)`.

Its independent support/arithmetic regression covered 1,941,976 + 414,442 configurations with zero failures; see `MATCHED_PRIVATE_FOOT_SLACK_AND_COMPLETE_ROW_QUADRATIC_EXCLUSION*`.

## 7. Complete-row and one-code global collapse

If one unmatched row has `K_y=K_p`, the entire matched 2-lift switches to

`K_p dotcup K_p`.

The other exact one-code row `K_y=K_{p-1} dotcup K_1` does the same after switching the isolated fibre. Hence

> any row with `tau(Psi(K_y))=1` forces the full matched core to the zero-signing switching class.

Therefore every one-code row forces

`L_A>=p(p-1)`.

More generally, if the row sign graph `L_y=bar K_y` is complete bipartite, it is a cut, so switching one side again kills every sign and yields the same quadratic slack bound.

Files:

- `COMPLETE_ROW_GLOBAL_NORMAL_FORM.md`;
- `ONE_CODE_ROW_GLOBAL_COLLAPSE_AND_QUADRATIC_PRICING.md`;
- `TWO_CODE_CUT_ROW_QUADRATIC_PRICING.md`.

For a full zero-signing core, `(GS-A)` is impossible whenever

`(lambda+2)u <= p^2-(lambda+4)p+c_lambda+3`.                    `(QER)`

At `lambda=-1`, an above-threshold zero-core/one-code configuration therefore requires

`u>=p^2-3p+4`.

Thus one-code rows are pushed out of every linearly-unmatched near-full regime.

## 8. Every exact tau<=2 unmatched-row kernel is quadratically priced

The preserved exact classification says `tau(Psi(K_y))<=2` iff the row sign graph `L_y` is one of:

1. complete bipartite;
2. a star plus isolates;
3. a two-centre graph in which every other vertex is a leaf of exactly one centre, with the centre edge optional.

The new subcore theorem prices all three:

- complete bipartite: after switching, zero subcore size `p`, so `L_A>=p(p-1)`;
- star plus isolates: delete the star centre, zero subcore size `p-1`, so `L_A>=(p-1)(p-2)`;
- two-centre: delete the two centres, zero subcore size `p-2`, so `L_A>=(p-2)(p-3)`.

Hence for `p>=5`, every `tau<=2` row gives the uniform floor

> `L_A>=(p-2)(p-3)`.                                      `(LOW2)`

In particular, throughout

> `(lambda+2)u <= p^2-(lambda+8)p+c_lambda+9`,              `(LOW2-region)`

an above-`M(n)` candidate must satisfy

> `tau(Psi(K_y))>=3` for every `y in U`.

This replaces the previous case-by-case cheap-row frontier.

## 9. Global switching-deletion stability

All unmatched row sign graphs lie in one switching class. If `L` is any fixed sign graph of the matched 2-lift, define

`kappa_sw(L)=min_S tau_vc(L Delta delta(S))`.

Equivalently, `kappa_sw` is the least number of coordinates that must be deleted so that the remaining signing becomes zero after switching. Put

`sigma_0=p-kappa_sw`.

Then `sigma_0` is the largest zero-signing induced subcore obtainable in any switching state. By `(ZS)`,

`L_A>=sigma_0(sigma_0-1)` whenever `sigma_0>=3`.

Combining with `(GS-A)`, every above-threshold candidate must satisfy

> `sigma_0(sigma_0-1)<=S_req-2`.                          `(SD)`

Thus

> `kappa_sw >= p-floor((1+sqrt(1+4(S_req-2)))/2)`

(up to the harmless size-one/two boundary).

At `lambda=-1`,

> `kappa_sw >= p-floor((1+sqrt(8p+4u-15))/2)`.

Therefore, for fixed `lambda` and `u=O(p)`,

> `m>M(n) ==> kappa_sw=p-O(sqrt(p))`.

A surviving near-full candidate must be highly switching-complex; it cannot be a bounded perturbation of the zero-signing core.

File: `SWITCHING_DELETION_STABILITY_FROM_A_SLACK.md`.

## 10. Large row cover and alpha-capacity cap in every above-threshold candidate

Let

`C=S_req-2`,

`R=floor((1+sqrt(1+4C))/2)`,

`R_*=max(2,R)`.

The row-kernel theorem says that if

`t=tau(Psi(K_y))`,

then outside at most `t` exceptional coordinates the row sign graph partitions into at most `t` equal-open-neighbourhood independent classes. The largest such class has size at least

`ceil((p-t)/t)`

and is itself a zero-signing subcore. Therefore an above-threshold candidate must have

> **ROW-COVER FLOOR**
>
> `tau(Psi(K_y))>=ceil(p/(R_*+1))`                         `(RC)`

for **every** unmatched vertex `y`.

At `lambda=-1`, `C=2p+u-4`; if `u=O(p)`, then

> every unmatched row has `tau(Psi(K_y))=Omega(sqrt(p))`.

The projective-twin theorem says

`mu_alpha=max_c |alpha^{-1}(c)|`

is the largest true-twin clique obtainable by switching the matched core. Such a class is also a zero-signing subcore, so

> **ALPHA TWIN CAP**
>
> `mu_alpha<=R_*`.                                         `(AC)`

The preserved Hall inequality therefore refines to

`s=e(A,U)>=pu-R_* a`.

For `u=O(p)` and fixed `lambda`, a hypothetical above-threshold candidate simultaneously has

- `kappa_sw=p-O(sqrt(p))`;
- every unmatched row cover `Omega(sqrt(p))`;
- every projective alpha/true-twin class `O(sqrt(p))`.

File: `ROW_COVER_AND_ALPHA_CAP_FROM_SLACK_STABILITY.md`.

## 11. Full-tight branch remains closed internally

If tight antipodes cover all of `B`, the fixed switching-defect hierarchy remains internally closed for `k>=19`; see `FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`. The full-tight order-12/32 `X_3` hostile control is a small `k=4,r=0` exception and remains explicitly allowed.

Do not reopen the fixed-defect ladder as the main attack.

## 12. Active next move

The structural frontier has changed materially. In the linearly-unmatched near-full regime, bounded/cheap row kernels are now gone **all at once**. The surviving candidate must have high row cover and no large repeated alpha class.

The next compact target is an **aggregate selected/Hall capacity theorem** in this high-complexity regime. The intended bridge is:

1. every U-row needs at least `Omega(sqrt(p))` witness-code support;
2. no alpha class can absorb more than `O(sqrt(p))` source coordinates;
3. remaining obligations must beta-spill into radius-one code spheres and actual A--U edges;
4. heavy reuse of beta spheres should either force A-code multiplicity/positive `L_A`, or complementary U-antipode/fan structure already priced by BAF.

A theorem converting these facts into a lower bound on `E_U+L_A` would plug directly into `(GS-A)` and attack the second-extremal threshold itself.

A secondary open branch remains `Q=0` / false-twin core from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md`; it has not been conflated with the partial-Boolean triangle branch.

Do not return to the closed mixed `{4,5}` ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742.

## 13. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure; no author-supplied adjacency file has been located.
- Full-tight eventual closure is an internal candidate pending external review.
- The near-full normal form, exact slack criterion, BAF theorem, private-foot slack transfer, zero-signing subcore quadratic theorem, switching-deletion stability, row-cover floor and alpha cap are hand arguments.
- Finite computations/checkers are audit and regression support only.
- The new results do **not** yet close all unmatched/errorful configurations: the high-row-cover aggregate Hall/beta-capacity step remains open.
- The `Q=0` / false-twin-core branch remains separate and open.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
