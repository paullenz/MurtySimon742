# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_BOOLEAN_FAN_ROW_AND_CLIQUE_CAPACITY_FRONTIER_INTERNAL_CANDIDATES`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19` in the preserved theorem). The active work is the unmatched/errorful antipode branch. The live objective is now to turn the strengthened U-antipode/row structure into A-side maximum-degree slack and hence into the exact second-extremal defect.

## 1. Scope and hostile control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an assumed all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) graph has been reconstructed from Figure 1 and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter 2 and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md` and its checker/summary. All eventual statements below leave this control untouched.

## 2. Preserved root and defect framework

For a maximum-degree root `v`, write

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

`Q=e(G[B])`, `F=G[A]`, `delta=b(n-b)-m=r-e(F)`.

For a rooted antipode `uw`,

`uw notin E(G)`, `N(u) cap N(w)={v}`,

and

`epsilon_u+epsilon_w=lambda+1+eta(uw)`,                         `(AS)`

where `epsilon_x=b-d(x)` and `eta(uw)` counts vertices outside `{u,w,v}` adjacent to neither endpoint. Tight antipodes have `eta=0` and form a matching.

For `n>=14`, the all-private edge-witness pricing theorem excludes the all-private branch above `M(n)` whenever a maximum-degree root lies in a triangle. `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` remains the scope repair for a maximum root with `Q=0`; the false-twin-core branch is still open.

## 3. Full-tight branch remains closed internally

If tight antipodes cover all of `B`, write `B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`. Then `G[B]` is a 2-lift of `K_k`, every A-vertex is a Boolean transversal, and the realised A-code support covers the full-tight orientation graph. The complete fixed switching-defect hierarchy is internally closed for `k>=19`; see `FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`.

Do not reopen the fixed-defect ladder as the main attack.

## 4. Near-full partial Boolean normal form

Let the complete tight matching have `p` pairs `P_i={u_i,w_i}`, let `P` be their union, and put `U=B\P`, `u=|U|`, so `b=2p+u`.

Write `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Every vertex of `A union U` chooses exactly one endpoint from every tight pair, giving a partial Boolean code in `{0,1}^p`.

Exact identities:

`Q=p(p+u-1)+q`,                                                `(NF1)`

`r=(p+u)(a-p)+p-s-q`,                                         `(NF2)`

`delta=(p+u)(a-p)+p-s-q-f`,                                   `(NF3)`

`E_U:=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,                    `(NF4)`

`L_A:=sum_{x in A}epsilon_x=a(p+u)-s-2f`.                      `(NF5)`

If `p>=2`, private A-feet for B-root edges are impossible, so every `y in U` has an errorful antipode. U--U antipodes have complementary partial codes. If `y in U` is antipodal to a matched endpoint `q` with tight mate `q'`, then `c(y)=alpha(q)` and

`eta(yq)=epsilon_y-epsilon_q'`.

Main file: `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`.

## 5. Exact global slack criterion

Let `T=sum_z epsilon_z`. Then for any graph at a maximum-degree root

`T=nb-2m`,

`2 delta=T-b lambda`.                                          `(GS1)`

Moreover

> `m<=M(n)` iff `T>=floor(n(lambda+2)/2)-2`.                     `(GS2)`

Hence

> `m>M(n) ==> T<=floor(n(lambda+2)/2)-4`.                        `(GS3)`

In near-full form,

`T=p(lambda+1)+E_U+L_A`,                                       `(GS4)`

`2 delta=E_U+L_A+p-lambda(p+u)`.                               `(GS5)`

At `lambda=-1`, the threshold is `E_U+L_A>=2p+u-2`; an above-threshold graph has `E_U+L_A<=2p+u-4`. At `lambda=0`, the threshold is `E_U+L_A>=3p+2u-2`.

This is the correct scorecard: support arguments matter only if they ultimately force `E_U+L_A` or equivalent defect payment.

File: `GLOBAL_SLACK_DEFECT_CRITERION.md`.

## 6. Preserved unmatched-row/Hall structure

For `y in U`, let `q_i` be its chosen endpoint in `P_i`, let `K_y` be the graph on `[p]` induced by adjacency among the `q_i`, and put `L_y=bar K_y`.

After translation by `bar c(y)`, the P--U witness constraints are

`{A_i,{i}}`, with `A_i=N_{L_y}(i)`.                             `(ROW)`

Preserved exact results from `UNMATCHED_ROW_KERNEL_CAPACITY_STABILITY.md`:

- `tau(Psi(K))=1` iff `K=K_p` or `K=K_{p-1} dotcup K_1`;
- complete classification of all `tau<=2` rows;
- fixed row cover implies a finite true-twin kernel;
- `alpha(q_i) Delta bar c(y)=N_{L_y}(i)` and `beta_i(y) Delta bar c(y)={i}`;
- matched-antipode eligibility is exactly isolation in `L_y`;
- per-source Hall capacity gives `B_beta>=pu-W_alpha` and `s>=pu-W_alpha`;
- alpha-code preimage multiplicity is the switching true-twin multiplicity of the matched 2-lift;
- complementary beta pools are disjoint for `p>=3`.

## 7. New Boolean antipode-fan payment

Let `J_U` be the U--U antipode graph. Fix `z in U`, let `Y=N_{J_U}(z)`, `d=|Y|`. All partners in `Y` have code `bar c(z)` and therefore share matched P-neighbours.

Pricing every edge of `G[Y]` through D2C criticality gives

> `sum_{y in Y} eta(yz) >= binom(d,2)+bar e(G[Y])`.               `(BAF)`

In particular

`2 sum_y eta(yz)>=d(d-1)`.                                     `(BAF0)`

Globally,

`4 sum_{e in E(J_U)}eta(e)`

` >= sum_z d(z)(d(z)-1)+2 sum_z bar e(G[N_{J_U}(z)])`.           `(BAF-global)`

This improves the old general branching coefficient from 6 to 4 on the U--U antipode graph and removes the abstract unit-error `K_{1,4}` obstruction from the partial-Boolean branch.

File: `BOOLEAN_ANTIPODE_FAN_PAYMENT.md`.

Independent graph-atlas regression through order seven: 21 D2C classes, 50 maximum-degree roots, 9 roots with a tight pair, 3 U-antipode fan centres, one branching fan, zero fibre or BAF violations, minimum margin 0. See `check_boolean_antipode_fan_payment.py` and `BOOLEAN_ANTIPODE_FAN_PAYMENT_CHECK_SUMMARY.json`.

## 8. Improved unmatched slack floors

Let `Z={y in U:epsilon_y=0}`. A zero-slack unmatched vertex cannot have a matched antipode, so assign it to a U-hub `z`. If `d_z` zero-slack partners are assigned to `z`, then

`eta_z=epsilon_z-lambda-1>=1`

and BAF gives

> `d_z<=2eta_z+1=2(epsilon_z-lambda-1)+1`.                       `(HC)`

Consequently:

- `lambda=-1`: `E_U>=ceil(u/4)`;
- `lambda>=0`, zeros present: `E_U>=ceil(u/2)+lambda`;
- universally for `lambda>=0`: `E_U>=min(u,ceil(u/2)+lambda)`.

In particular at `lambda=0`, `E_U>=ceil(u/2)` rather than the previous `ceil(u/3)`.

At `lambda=-1`, any above-`M(n)` candidate must therefore have at least

`4+ceil(u/4)`

maximum-degree vertices in `A`.

## 9. Saturation is rigid: clique partners and private holes

If one fan saturates `(HC)`, with `d=2eta+1`, equality in BAF forces:

- `G[Y]=K_d`;
- the partner-edge charges form a regular tournament;
- used holes are external and have hub code `c(z)`.

A hole certifying an edge from source `x in Y` satisfies

`N(h) cap Y={x}`.

Different sources therefore need distinct holes. Hence at least `d` distinct external hub-code vertices are forced, one private to each source. The two complementary code classes contain at least `2d+1` vertices in `A union U`, and

> `n_{c(z)}>=max(0,2d+1-u)`                                      `(PH-A)`

when U is too small to host all holes.

The cheapest saturated fan (`eta=1,d=3`) is therefore a triangle of three partners plus three distinct hub-code private holes, not an abstract `K_{1,4}` error star.

File: `SATURATED_BOOLEAN_FAN_PRIVATE_HOLES.md`.

## 10. Fan-to-row Hall dichotomy

For the common partner row put `A_i=N_L(i)`,

`m(C)=|{i:A_i=C}|`, `D=max_C m(C)`.

Because

`alpha(q_i)=c(z) Delta A_i`,                                    `(FR1)`

`D` is both the largest repeated alpha code among the selected matched sources and a true-twin clique size in the row graph; the matched-core projective-twin parameter satisfies `mu_alpha>=D`.

For a fan with `d` partners, per-source capacity gives

> `B_beta(Y)>=max(0,dp-Da)`.                                     `(FAS)`

If `J` is the set of coordinates with `n_{alpha(q_i)}<d`, then each `i in J` forces a distinct beta code `c(z) Delta {i}` and

> `|J|>=max(0,p-D floor(a/d))`.                                  `(FBS)`

Thus every saturated low-error fan produces either

1. a large true-twin/alpha class in the matched core, or
2. a large explicit radius-one beta-code set adjacent to the fan and nonadjacent to its hub.

File: `SATURATED_FAN_ROW_CAPACITY_DICHOTOMY.md`.

## 11. New pricing of the cheap complete row

The one-code row `K_y=K_p` was previously cheap only from the support viewpoint. It actually creates the B-clique

`C_y={y,q_1,...,q_p}`

of size `p+1`.

A general D2C clique-criticality lemma now shows: every clique of size `s>=3` has private feet for all but at most one clique source. If the clique lies in `B=N(v)`, every such foot must lie in A, because a B-foot would share the root `v` with every target.

Therefore a complete unmatched row forces at least `p` distinct A-side private feet. Their codes are explicit:

- a foot private to `q_i` has code `beta_i(y)=bar c(y) Delta {i}` and is nonadjacent to `y`;
- a foot private to `y` has code `bar c(y)` and is adjacent to `y`.

Hence A realises at least `p-1` of the `p` radius-one beta codes, regardless of how the selected witness row itself is covered.

Moreover, a private foot of code `beta_i(y)` cannot also be a selected beta witness for `yq_i`, because the former is nonadjacent to `y` while the latter must be adjacent. If that coordinate beta-spills, then

> `n_{beta_i(y)}>=2`.                                            `(CR-MULT)`

File: `COMPLETE_ROW_CLIQUE_PRIVATE_FEET.md`.

This means neither one-code row remains an unstructured escape:

- `K_p` forces a large rooted B-clique and almost a full beta sphere of A-private feet;
- `K_{p-1} dotcup K_1` forces a complementary U--U antipode and enters BAF.

## 12. Active next move

The next compact theorem target is **A-side pricing** of the explicit structures now forced.

Two inputs are ready:

1. saturated/generic fan beta support: many distinct A vertices in codes `c(z) Delta {i}`, adjacent to fan partners and nonadjacent to the hub;
2. complete-row private feet: at least `p-1` beta-sphere code classes already occupied by A vertices that are deliberately nonadjacent to the row vertex, with beta-selected witnesses requiring additional multiplicity.

The next goal is to show that these A-side populations force either

- a linear lower bound on `L_A`, via maximum-degree slack and criticality of their A--U/F edges; or
- enough repeated alpha/true-twin structure to collapse the matched core into the already-classified low switching-defect normal forms.

A theorem of the schematic form

`L_A + controlled U-error >= linear payment from beta/private-foot support`

would plug directly into `(GS4)`--`(GS5)` and is now the highest-value route toward an externally reviewable eventual theorem.

Do not return to the closed mixed `{4,5}` ladder, arbitrary fixed-defect enumeration, or first-proof optimization for Erdős #742. The Q=0/false-twin-core branch remains separate and open.

## 13. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure; no author-supplied adjacency file has been located.
- Full-tight eventual closure is an internal candidate pending external review.
- The near-full normal form, row identities, BAF theorem, improved unmatched floors, private-hole theorem, fan row-capacity inequalities and clique-private-foot theorem are hand arguments.
- Atlas and exact finite computations are audit/regression support only.
- No theorem yet converts all unmatched/errorful configurations into enough `E_U+L_A` to finish the eventual second-extremal result.
- The Q=0/twin-core branch remains separate and not closed.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
