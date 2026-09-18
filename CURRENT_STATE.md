# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_BRANCH_CLOSED_NEAR_FULL_PARTIAL_BOOLEAN_NORMAL_FORM_AND_ANTIPODE_ERROR_CURVATURE_ESTABLISHED_INTERNAL_CANDIDATES`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full tight-antipode Boolean switching branch remains internally closed for `k>=19`. The main attack has now moved into the genuinely near-full regime. This unit extracted the exact partial Boolean normal form for an arbitrary tight matching, proved that two tight pairs eliminate the private-foot branch entirely, imported the full-tight orientation graph as a necessary support subsystem, built the exact augmented orientation constraints created by unmatched B-vertices, and proved a quadratic error payment for branching in the antipode graph.

## 1. Preserved dense-root entry point

For a non-bipartite D2C graph above `M(n)`, the preserved root work reduces the triangle-containing maximum-root branch as follows.

For `n>=14`, the all-private edge-witness theorem rules out the branch in which every triangle-active root neighbour has a private A-foot. Hence a dense maximum-triangle root has a disjoint-support antipode.

For an antipode `uw` at root `v`, with

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

the exact slack identity is

`epsilon_u+epsilon_w=lambda+1+eta(uw)`,                 `(AS)`

where `eta` counts vertices outside `{u,w,v}` adjacent to neither endpoint.

Tight antipodes are those with `eta=0`; they form a matching. For every antipode matching `M`,

`b lambda + r - Q >= |M|(lambda+1)+sum_{e in M} eta(e)`.   `(AMC)`

The canonical defect is

`delta=b(n-b)-m=r-e(F)`.

The rooted triangle count is

`Q=e(G[B])`.

## 2. Mandatory 12-vertex negative control

The published Radosavljevic--Stanic--Zivkovic (2024) order-12, size-32 graph has been reconstructed directly from the authoritative Figure 1 and exactly checked. It is isomorphic to the project's `X_3`:

- `n=12`;
- `m=32>M(12)=31`;
- diameter 2;
- every edge critical;
- unique dominating edge;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

The eight inner vertices are `Q_3`, the three outer vertices are coordinate-zero faces, and the central root is universal on the cube.

Files:

- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`;
- `check_published_12_vertex_exception_figure.py`;
- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CHECK_SUMMARY.json`.

This hostile control is outside every eventual threshold proved below and must remain so.

## 3. Preserved milestone: full-tight Boolean branch closed internally

If tight antipodes cover all of `B`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then:

- `G[B]` is a 2-lift of `K_k`;
- every A-vertex is a Boolean transversal;
- `Q=k(k-1)`;
- `r=k(a-k+1)`;
- actual A-codes cover the orientation-code graph `Omega`;
- an above-`M(n)` candidate has `a<=2k`.

The complete switching hierarchy has been internally exhausted for `k>=19`:

- defects `0,...,4`: structural classifications plus F-separation/defect closure;
- defects `5,6`: support-impossible from their stated thresholds;
- defects `7,8`: general twin-package reduction plus finite rooted-core certificates;
- defect `9`: hand residual-count closure;
- defects `>=10`: uniform twin/lopsided support closure or the elementary orientation-degree bound.

Full synthesis:

`FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`.

Therefore the fixed-defect ladder is no longer the main target.

## 4. New near-full partial Boolean normal form

Let the complete tight-antipode matching have `p` pairs

`P_i={u_i,w_i}`, `1<=i<=p`.

Put

`P=union_i P_i`, `U=B\P`, `u=|U|`,

so

`b=2p+u`.

Write

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`.

Tightness of every `P_i` says that each vertex outside the pair chooses exactly one endpoint. Hence:

- between two tight pairs there is a perfect matching;
- every `y in U` chooses one endpoint of every `P_i`;
- every `x in A` chooses one endpoint of every `P_i`.

Thus every vertex of `A union U` carries a partial Boolean code in `{0,1}^p`.

The exact rooted counts are

`Q = p(p-1)+pu+q = p(p+u-1)+q`,                        `(NF1)`

`r = a(p+u)-s-Q`

`  = (p+u)(a-p)+p-s-q`,                                `(NF2)`

and

`delta=(p+u)(a-p)+p-s-q-f`.                            `(NF3)`

For unmatched B-slack,

`E_U=sum_{y in U} epsilon_y = u(p+u-1)-2q-s`.          `(NF4)`

For A-slack,

`L_A=sum_{x in A} epsilon_x = a(p+u)-s-2f`.            `(NF5)`

Each tight pair still satisfies

`epsilon_{u_i}+epsilon_{w_i}=lambda+1`.

Full note:

`NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`.

## 5. Two tight pairs eliminate the private-foot alternative

Assume `p>=2`.

Every B-vertex is triangle-active:

- a matched endpoint meets every other tight pair;
- an unmatched vertex meets every tight pair.

But every A-vertex has exactly `p>=2` neighbours in the matched set `P`. Therefore no A-vertex can be a private foot with `N_B(x)={y}`.

Hence the root-edge dichotomy collapses to the antipode alternative:

> **NO-PRIVATE / ANTIPODE-COVER REDUCTION — internal candidate.** If `p>=2`, every vertex of `B` has an antipode partner. Every unmatched `y in U` is incident only with **errorful** antipodes, because all tight antipodes have already been placed in the matching.

This is a significant stability reduction: unmatched vertices cannot escape through the previously troublesome private-foot branch.

## 6. Errorful antipodes obey partial-code constraints

Let `c(z)` be the partial Boolean code of `z in A union U`.

If `y,z in U` are antipodes, they can share no matched neighbour, so

`c(z)=bar(c(y))`.                                      `(PC1)`

If `y in U` is antipodal to a matched endpoint `q in P_i`, let `q'` be the tight mate of `q`. Define `alpha(q)` by choosing

- `q'` in fibre `P_i`;
- in every other fibre, the endpoint not adjacent to `q`.

Then

`c(y)=alpha(q)`.                                       `(PC2)`

The slack identities also give the exact local error formula

`eta(yq)=epsilon_y-epsilon_q'`.                        `(PC3)`

Since this antipode is errorful,

`epsilon_y>=epsilon_q'+1`.                             `(PC4)`

Thus every unmatched vertex is forced either into a complementary U-code relation or into one of the special matched-endpoint antipode codes, with an explicit slack payment.

## 7. Full-tight support survives inside the near-full branch

The physical B-edges between distinct tight pairs form exactly the ordinary full-tight 2-lift on `p` fibres. Their selected A-witnesses have exactly the same forced partial codes as in the full-tight orientation graph `Omega_P`.

Therefore the realised A-code support `C_A` satisfies

`tau(Omega_P) <= |C_A| <= a`.                          `(SUP)`

Since

`a=2p+u-lambda-1`,

we have

`a<=2p  iff  u<=lambda+1`.

The preserved support-only full-tight results say that, for `p>=19`, every minimum switching defect `d_*>=5` has `tau(Omega_P)>2p`.

Hence:

> **LOW-DEFECT NEAR-FULL REDUCTION — internal candidate.** If `p>=19` and `u<=lambda+1`, then the inherited matched-pair switching problem must satisfy `d_*<=4`.

Equivalently, if `d_*>=5`, then

`u>=lambda+2`.

The old full-tight F-separation conclusions for `d_*=0,...,4` are **not** silently imported; those low-defect cases must be re-priced with the unmatched vertices present.

## 8. New augmented orientation graph Omega+

The unmatched vertices generate further exact selected-witness constraints beyond the ordinary P--P graph `Omega_P`.

For `y in U`, let `q_i in P_i` be its chosen endpoint.

For the physical B-edge `y q_i`, the two possible orientations force the A-witness code to be one of

`alpha(q_i)`

or

`beta_i(y)`,

where `beta_i(y)` chooses `q_i` in fibre `i` and the endpoint nonadjacent to `y` in every other fibre.

Thus every P--U edge contributes the two-code constraint

`{alpha(q_i), beta_i(y)}`.                              `(AUG1)`

For an edge `yz in G[U]`, the two orientations force

`{bar(c(y)), bar(c(z))}`.                               `(AUG2)`

Together with the ordinary P--P orientation edges, these constraints define an augmented orientation multigraph `Omega+` on `{0,1}^p`.

The realised A-code support must cover **every** edge/loop of `Omega+`.

Moreover the selected system retains per-source capacity: if `n_c` A-vertices realise code `c`, then at a fixed B-source at most `n_c` selected obligations can be assigned to orientation endpoint `c`.

This is the correct near-full reuse of the selected/Hall machinery: a capacitated orientation-cover problem rather than another raw switching-defect scan.

## 9. New theorem: branching antipodes pay quadratic error

Let `J_v` be the antipode graph on `B`. Fix `w in B`, put

`S=N_{J_v}(w)`, `d=|S|`,

and

`E_w=sum_{y in S} eta(yw)`.

Two observations give a sharp local payment.

1. A nonedge `yz` inside `S` is an error vertex for both antipodes `yw` and `zw`, so

`binom(d,2)-e(G[S]) <= E_w/2`.

2. For an edge `yz` inside `S`, D2C criticality supplies (after orientation) a witness `x` with `N(x) cap N(z)={y}`. Because `y` is antipodal to `w`, this `x` is also nonadjacent to `w`; hence `(x,z)` is an error incidence for `zw`. The charge is injective because `y` is the unique common neighbour of `x,z`. Therefore

`e(G[S]) <= E_w`.

Combining gives

> **ANTIPODE BRANCHING ERROR THEOREM — internal candidate.**
>
> `3 E_w >= d(d-1)`.                                  `(ABE)`

Globally,

`sum_{e in E(J_v)} eta(e)
 >= (1/6) sum_{w in B} d_J(w)(d_J(w)-1)`.              `(ABE-global)`

Thus concentrating many root-edge witnesses through an antipode hub has a quadratic error cost.

In the near-full `p>=2` branch, errorful antipode edges cover all `u` unmatched vertices, so additionally

`sum_{e errorful} eta(e) >= ceil(u/2)`.

Files:

- `ANTIPODE_BRANCHING_ERROR_PAYMENT.md`;
- `check_antipode_branching_error_payment.py`;
- `ANTIPODE_BRANCHING_ERROR_CHECK_SUMMARY.json`.

The atlas regression scans all 21 D2C isomorphism classes through order seven, all 126 roots, 125 positive-degree antipode centres and 50 branching centres. There are zero local/global violations; maximum observed antipode degree is 5 and the local inequality is attained in some cases.

## 10. Active next move

The clean full-tight endpoint is solved internally. The near-full state is now compressed to three interacting objects:

1. a genuine `p`-fibre Boolean 2-lift core;
2. an unmatched transversal set `U` whose vertices are all forced into errorful antipodes;
3. the capacitated augmented selected-witness graph `Omega+`.

The highest-value next theorem is a **weighted antipode-matching / augmented-Hall stability inequality**.

Two possible routes are now precise rather than speculative:

- convert `(ABE)` into a large-weight antipode matching, with edge weight `lambda+1+eta(e)=epsilon_x+epsilon_y`, so that `(AMC)` prices branching as well as matching-like error;
- use the P--U constraints `(AUG1)` and per-source capacities to show that many unmatched transversals force extra A-code multiplicity/support unless the matched 2-lift lies in one of the low-defect `d_*<=4` normal forms.

The second route is especially attractive when `u<=lambda+1`, because `(SUP)` has already reduced that entire range to `d_*<=4`.

Do **not** return to the closed mixed `{4,5}` ladder, fixed switching-defect enumeration, or first-proof optimization for Erdős #742 except for regression/audit support.

## 11. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure and exactly checked, but no author-supplied adjacency file has been located.
- The full-tight eventual closure remains an internal candidate pending external review; several terminal steps use finite proof-producing certificates after unbounded structural reductions.
- The near-full partial Boolean normal form, no-private reduction, code restrictions, augmented orientation constraints and antipode branching-error inequality are hand arguments.
- The atlas scan for `(ABE)` is regression evidence only, not the proof.
- No theorem yet converts the total branching error into enough canonical defect `delta` to close the whole near-full branch.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
