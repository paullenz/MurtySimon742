# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_BOOLEAN_FAN_ROW_CAPACITY_FRONTIER_INTERNAL_CANDIDATES`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19` in the preserved theorem). The active work is the unmatched/errorful antipode branch. The current highest-value interface is now explicit: total maximum-degree slack is exactly the extremal defect, U-antipode branching is more expensive once the partial Boolean fibres are used, and saturation of that stronger error bound forces a rigid complementary-code/private-hole configuration that can be fed into row/Hall capacity.

## 1. Scope and mandatory negative control

The comparison threshold is

`M(n)=floor((n-1)^2/4)+1`.

No all-order theorem is assumed. The Radosavljevic--Stanic--Zivkovic (2024) order-12 graph has been reconstructed directly from Figure 1 and exactly checked:

- `n=12`, `m=32>M(12)=31`;
- diameter 2 and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

Files:

- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`;
- `check_published_12_vertex_exception_figure.py`;
- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CHECK_SUMMARY.json`.

Every eventual statement below leaves this control untouched.

## 2. Preserved root/stability entry point

For a maximum-degree root `v`, write

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

`Q=e(G[B])`, `F=G[A]`, and

`delta=b(n-b)-m=r-e(F)`.

For an antipode `uw` at `v`,

`uw notin E(G)`, `N(u) cap N(w)={v}`,

and

`epsilon_u+epsilon_w=lambda+1+eta(uw)`,                        `(AS)`

where `epsilon_x=b-d(x)` and `eta(uw)` counts vertices outside `{u,w,v}` adjacent to neither endpoint.

Tight antipodes have `eta=0` and form a matching. For every antipode matching `M`,

`b lambda+r-Q >= |M|(lambda+1)+sum_{e in M} eta(e)`.             `(AMC)`

For `n>=14`, the all-private edge-witness pricing theorem excludes the all-private branch above `M(n)` whenever a maximum-degree root lies in a triangle. The separate `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` remains the scope repair when a maximum root has `Q=0`; the resulting false-twin core branch is not yet closed.

## 3. Full-tight branch is preserved and closed internally

If tight antipodes cover all of `B`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`, every A-vertex is a Boolean transversal,

`Q=k(k-1)`, `r=k(a-k+1)`,

and the realised A-code support covers the full-tight orientation graph. The fixed switching-defect hierarchy has been internally exhausted for `k>=19`; see

`FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`.

Do not reopen the fixed-defect ladder as the main attack.

## 4. Near-full partial Boolean normal form

Let the complete tight-antipode matching have `p` pairs

`P_i={u_i,w_i}`,

put `P=union_i P_i`, and let `U=B\P`, `u=|U|`. Then

`b=2p+u`.

Write

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`.

Every vertex of `A union U` chooses exactly one endpoint from every tight pair, so it has a partial Boolean code in `{0,1}^p`. Exact identities are

`Q=p(p+u-1)+q`,                                               `(NF1)`

`r=(p+u)(a-p)+p-s-q`,                                        `(NF2)`

`delta=(p+u)(a-p)+p-s-q-f`,                                  `(NF3)`

`E_U:=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,                   `(NF4)`

`L_A:=sum_{x in A}epsilon_x=a(p+u)-s-2f`.                     `(NF5)`

If `p>=2`, every B-vertex is triangle-active and every A-vertex has at least two B-neighbours from the tight fibres, so the private-foot alternative disappears. Every unmatched `y in U` therefore has an errorful antipode.

Partial-code antipode restrictions:

- U--U antipodes have complementary codes;
- if `y in U` is antipodal to matched endpoint `q`, then `c(y)=alpha(q)`;
- if `q'` is the tight mate of `q`, then

  `eta(yq)=epsilon_y-epsilon_q'`.

Files: `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md` and predecessor notes.

## 5. Exact global slack criterion: the actual extremal target

For any graph rooted at a maximum-degree vertex, let

`T=sum_{z in V} epsilon_z`.

Then

`T=nb-2m`

and

> `2 delta=T-b lambda`.                                        `(GS1)`

Moreover

> `m<=M(n)` iff `T>=floor(n(lambda+2)/2)-2`.                    `(GS2)`

Thus

> `m>M(n) ==> T<=floor(n(lambda+2)/2)-4`.                       `(GS3)`

In the near-full decomposition, each tight pair contributes `lambda+1`, so

`T=p(lambda+1)+E_U+L_A`,                                      `(GS4)`

and equivalently

> `2 delta=E_U+L_A+p-lambda(p+u)`.                             `(GS5)`

Important special cases:

- `lambda=-1`: threshold requires `E_U+L_A>=2p+u-2`; above threshold gives `E_U+L_A<=2p+u-4`.
- `lambda=0`: threshold requires `E_U+L_A>=3p+2u-2`; above threshold is two units below this.

This corrects the strategic focus: row/Hall support is useful only insofar as it ultimately forces **combined U- plus A-side slack**, or an equivalent defect payment.

File: `GLOBAL_SLACK_DEFECT_CRITERION.md`.

## 6. Row-singleton and capacity structure already preserved

For `y in U`, let `q_i` be the endpoint chosen from `P_i`, let `K_y` be the graph on `[p]` in which `ij` is an edge iff `q_iq_j` is an edge, and put `L_y=bar K_y`.

After translation by `bar c(y)`, the P--U witness constraints are

`{A_i,{i}}`, where `A_i=N_{L_y}(i)`.                            `(ROW)`

The preserved exact results include:

1. `tau(Psi(K))=1` iff `K=K_p` or `K=K_{p-1} dotcup K_1`.
2. `tau(Psi(K))<=2` iff `L=bar K` is complete bipartite, a star plus isolates, or a two-centre graph whose other vertices are leaves of exactly one centre (centre edge optional).
3. If a row cover has size at most `t`, deleting at most `t` exceptional coordinates leaves at most `t` true-twin cliques (finite row-kernel theorem).
4. Exact row translation:

   `alpha(q_i) Delta bar c(y)=N_{L_y}(i)`,

   `beta_i(y) Delta bar c(y)={i}`.

5. Matched-antipode eligibility:

   `c(y)=alpha(q_i') iff i is universal in K_y iff i is isolated in L_y`.

6. Per-source Hall capacity gives

   `B_beta>=pu-W_alpha`, `s>=pu-W_alpha`,

   where `W_alpha=sum_{q in P} n_{alpha(q)}`.

7. Alpha-code preimage multiplicity is exactly the largest true-twin clique appearing in a switching state of the matched 2-lift.
8. Beta pools are radius-one Hamming spheres; complementary row classes have disjoint beta pools for `p>=3`.

Main file: `UNMATCHED_ROW_KERNEL_CAPACITY_STABILITY.md` with independent finite regression.

## 7. Predecessor unmatched slack floor and why it was not enough

The general antipode branching theorem gave

`3 sum_{y in N_J(z)} eta(yz) >= d_J(z)(d_J(z)-1)`,               `(ABE)`

and led to the coarse unmatched floors

- `E_U>=ceil(u/5)` at `lambda=-1`;
- roughly `E_U>=ceil(u/3)` at `lambda>=0`.

The abstract unit-error `K_{1,4}` star saturates ABE, so ABE alone could not improve those constants. This was preserved as a genuine methodological obstruction.

The new work below removes that obstruction **inside the partial-Boolean near-full branch**.

## 8. NEW: Boolean antipode-fan payment

Assume `p>=1`. Fix an unmatched hub `z in U` and let

`Y=N_{J_U}(z)`, `d=|Y|`,

where `J_U` is the U--U antipode graph.

All members of `Y` have the same partial Boolean code `bar c(z)`, so any two share a matched P-neighbour. For each `y in Y`, let `H_y` be the `eta(yz)` vertices adjacent to neither `y` nor `z`.

If `yy'` is an edge of `G[Y]`, it cannot certify its own criticality because `y,y'` already share a P-neighbour. D2C criticality therefore supplies an external arm in `H_{y'}\Y` (or symmetrically), and the target/hole charge is injective. Counting internal holes and edge charges gives

> **BOOLEAN ANTIPODE-FAN PAYMENT**
>
> `sum_{y in Y} eta(yz)`
>
> ` >= binom(d,2)+bar e(G[Y])`.                                  `(BAF)`

In particular

`2 sum_y eta(yz) >= d(d-1)`.                                   `(BAF0)`

Globally over `J_U`,

> `4 sum_{e in E(J_U)}eta(e)`
>
> ` >= sum_z d(z)(d(z)-1)+2 sum_z bar e(G[N_{J_U}(z)])`.         `(BAF-global)`

This improves the old ABE coefficient from 6 to 4 on U--U antipodes and adds an explicit neighbourhood-nonedge penalty.

File: `BOOLEAN_ANTIPODE_FAN_PAYMENT.md`.

Independent atlas regression:

- all 21 D2C classes through order 7;
- 50 maximum-degree roots;
- 9 roots with at least one tight pair;
- 3 unmatched antipode fan centres, including one branching fan;
- zero fibre/complement violations;
- zero BAF violations;
- minimum integer margin 0.

Files:

- `check_boolean_antipode_fan_payment.py`;
- `BOOLEAN_ANTIPODE_FAN_PAYMENT_CHECK_SUMMARY.json`.

Finite replay is support only; the hand charge proof is the theorem basis.

## 9. NEW: improved unmatched slack floors

Let

`Z={y in U:epsilon_y=0}`.

A zero-slack unmatched vertex cannot have a matched antipode, so assign each `y in Z` to a U-antipode hub `z`. If a hub receives `d_z` zero-slack partners, then all their errors equal

`eta_z=epsilon_z-lambda-1>=1`.

BAF gives

> `d_z<=2 eta_z+1=2(epsilon_z-lambda-1)+1`.                       `(HC)`

This replaces the old coefficient 3.

Consequences in the dense comparison regime (`lambda>=-1`):

- if `lambda=-1`,

  > `E_U>=ceil(u/4)`;                                             `(UF-1)`

- if `lambda>=0` and no unmatched vertex has zero slack, `E_U>=u`;
- if `lambda>=0` and zero-slack unmatched vertices exist,

  > `E_U>=ceil(u/2)+lambda`;                                      `(UF0+)`

hence universally for `lambda>=0`,

> `E_U>=min(u,ceil(u/2)+lambda)`.                                 `(UF)`

In particular at `lambda=0`, `E_U>=ceil(u/2)`, improving the old `ceil(u/3)` floor.

At `lambda=-1`, combining `(UF-1)` with the exact above-threshold slack budget forces at least

> `4+ceil(u/4)`

maximum-degree vertices in `A` in any putative above-`M(n)` graph. This is a new interface with A-side/maximum-triangle-root structure.

## 10. NEW: saturation is rigid — regular tournament plus private holes

If one hub saturates `(HC)`, say

`d=2 eta+1`,

then equality in BAF forces:

1. the partner set `Y` is a clique;
2. the criticality charges orient `K_d` as a regular tournament;
3. all holes used by those charges are external to `Y` and have hub code `c(z)`.

A further edge-criticality argument shows that a hole witnessing an oriented edge from source `x` has

`N(h) cap Y={x}`.

Different sources therefore require distinct private holes. Hence a saturated fan forces at least `d` distinct vertices outside `Y union {z}` of code `c(z)`, one private to each source in `Y`.

Thus the two complementary code classes already contain at least `2d+1` vertices in `A union U`. If U is too small to host the private holes, then

> `n_{c(z)} >= max(0,2d+1-u)`                                   `(PH-A)`

for A-code multiplicity.

For the cheapest `eta=1,d=3` fan, the three partners form a triangle and at least three distinct hub-code private holes are forced. If `u=4`, all three holes lie in A and `n_{c(z)}>=3`.

File: `SATURATED_BOOLEAN_FAN_PRIVATE_HOLES.md`.

This replaces the old abstract `K_{1,4}` obstruction by a much more rigid possible equality object: at `lambda=-1`, the cheapest local obstruction is a slack-one hub with three zero-slack partners forming a triangle, together with a private-hole system in the complementary code class.

## 11. NEW: exact fan-to-row Hall dichotomy

For a fan partner row with common code `c=bar c(z)`, put

`A_i=N_L(i)` and

`m(C)=|{i:A_i=C}|`, `D=max_C m(C)`.

The exact row identity gives

`alpha(q_i)=c(z) Delta A_i`.                                   `(FR1)`

Therefore `D` is simultaneously the largest repeated alpha code among the selected matched sources and a true-twin clique size in the row graph `K`. In particular the matched-core projective-twin parameter satisfies

`mu_alpha>=D`.                                                   `(FR2)`

If the fan has `d` partners, per-source capacity at coordinate `i` gives

`B_i>=(d-n_{alpha(q_i)})_+`.

Summing by neighbourhood classes yields

> **FAN ALPHA-SPILL**
>
> `B_beta(Y)>=max(0,dp-Da)`.                                     `(FAS)`

Let `J` be the coordinates for which `n_{alpha(q_i)}<d`. Every `i in J` forces a beta witness of the distinct code `c(z) Delta {i}`. Since a sufficient alpha class consumes at least `d` A-vertices and contains at most `D` coordinates,

> **FAN BETA-SUPPORT**
>
> `|J|>=max(0,p-D floor(a/d))`.                                  `(FBS)`

Thus a saturated low-error fan forces one of two explicit structures:

1. **large D:** a large repeated alpha/true-twin class in the matched core;
2. **small D:** many distinct radius-one beta codes adjacent to the fan and, by antipodality, nonadjacent to its hub.

File: `SATURATED_FAN_ROW_CAPACITY_DICHOTOMY.md`.

This is the cleanest current bridge between the stronger antipode-error theorem and selected/Hall capacity.

## 12. Active next move

Do **not** return to another fixed switching-defect enumeration. The next compact theorem target is the beta side of `(FBS)`.

A beta witness `x in A` for a partner `y in Y` satisfies

- `x~y`;
- `x not~z` because `y,z` are antipodes;
- its code is one of the explicit radius-one vertices `c(z) Delta {i}`.

The next goal is to price a large collection of such distinct beta-code A-neighbours against either

1. A-side maximum-degree slack `L_A`, using criticality of the A--U edges / F-edges they create; or
2. additional antipode error / matched-core switching defect.

The complementary large-`D` branch should be attacked by the projective-twin/switching normal form already available for the matched core.

A successful theorem of the schematic form

`L_A + (controlled U-error) >= linear function of beta-support or D`

would plug directly into `(GS4)`--`(GS5)` and is now more valuable than further support-only enumeration.

The Q=0/false-twin-core branch remains separate and open. Preserve it; do not silently assume a maximum-degree triangle root.

## 13. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure; no author-supplied adjacency file has been located.
- Full-tight eventual closure is an internal candidate pending external review; several finite terminal certificates remain to be journal-compressed.
- The near-full normal form, row identities, BAF theorem, improved unmatched floors, private-hole saturation theorem and fan row-capacity inequalities are hand arguments.
- Atlas and exact finite computations are audit/regression support only.
- The saturation/private-hole and row-capacity results sharply constrain equality but do not yet prove the eventual second-extremal theorem.
- The Q=0/twin-core branch remains separate and not closed.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
