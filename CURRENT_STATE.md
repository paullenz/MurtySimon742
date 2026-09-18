# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_BRANCH_CLOSED_NEAR_FULL_AUGMENTED_HALL_ROW_SINGLETON_FRONTIER_INTERNAL_CANDIDATES`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The full tight-antipode Boolean branch remains internally closed for `k>=19`. The main attack has moved to unmatched/errorful antipodes. This unit extracted an exact partial-Boolean normal form for an arbitrary tight matching, eliminated the private-foot escape once two tight pairs exist, built the augmented selected-witness graph created by unmatched B-vertices, proved quadratic error curvature for branching antipodes, and then reduced each unmatched vertex's P--U witness obligations to a small row-singleton cover problem with a complete classification of its one-code extremals.

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

This remains untouched by all eventual thresholds below.

## 2. Preserved root/stability entry point

For a maximum-degree root `v`, write

`B=N(v)`, `b=|B|`, `A=V\N[v]`, `a=|A|`, `lambda=2b-n=b-a-1`,

`Q=e(G[B])`, `F=G[A]`, and

`delta=b(n-b)-m=r-e(F)`.

For an antipode `uw` at `v`,

`uw notin E(G)`, `N(u) cap N(w)={v}`,

and the exact slack identity is

`epsilon_u+epsilon_w=lambda+1+eta(uw)`,                 `(AS)`

where `eta(uw)` counts vertices outside `{u,w,v}` adjacent to neither endpoint.

Tight antipodes have `eta=0` and form a matching. For every antipode matching `M`,

`b lambda+r-Q >= |M|(lambda+1)+sum_{e in M} eta(e)`.    `(AMC)`

For `n>=14`, the preserved all-private edge-witness pricing theorem excludes the all-private branch above `M(n)` whenever a maximum-degree root lies in a triangle, so that branch enters the antipode regime.

The separate `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` remains the scope repair when a maximum root has `Q=0`: above threshold either a maximum-degree triangle root exists or a peelable maximum-degree false-twin class occurs. The latter Q=0/twin-core branch is not claimed closed here.

## 3. Preserved milestone: full-tight Boolean branch closed internally

If tight antipodes cover all of `B`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`, every A-vertex is a Boolean transversal,

`Q=k(k-1)`,

`r=k(a-k+1)`,

and the realised A-code support covers the orientation-code graph `Omega`.

The complete switching hierarchy has been internally exhausted for `k>=19`. The unbounded reductions are structural; several low fixed-defect terminal cases use finite proof-producing certificates. See

`FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`.

Do not reopen the fixed switching-defect ladder as the main attack.

## 4. New near-full partial Boolean normal form

Let the complete tight-antipode matching have `p` pairs

`P_i={u_i,w_i}`, `1<=i<=p`,

and put

`P=union_i P_i`, `U=B\P`, `u=|U|`, so `b=2p+u`.

Write

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`.

Every vertex outside a tight pair chooses exactly one of its endpoints. Therefore:

- between any two tight pairs there is a perfect matching;
- every `y in U` chooses one endpoint from every pair;
- every `x in A` chooses one endpoint from every pair.

Thus every vertex of `A union U` has a partial Boolean code in `{0,1}^p`.

Exact identities:

`Q=p(p-1)+pu+q = p(p+u-1)+q`,                          `(NF1)`

`r=a(p+u)-s-Q = (p+u)(a-p)+p-s-q`,                     `(NF2)`

`delta=(p+u)(a-p)+p-s-q-f`,                            `(NF3)`

`sum_{y in U} epsilon_y=u(p+u-1)-2q-s`,                `(NF4)`

`sum_{x in A} epsilon_x=a(p+u)-s-2f`.                  `(NF5)`

Full note:

`NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`.

## 5. Two tight pairs force antipode coverage

If `p>=2`, every B-vertex is triangle-active, while every A-vertex has at least the `p` matched B-neighbours supplied by the tight pairs. Therefore no A-vertex can be a private foot with `N_B(x)={y}`.

Hence the root-edge dichotomy gives:

> **NO-PRIVATE / ANTIPODE-COVER REDUCTION — internal candidate.** If `p>=2`, every vertex of `B` has an antipode partner. Every unmatched `y in U` is incident only with errorful antipodes.

The unmatched set can no longer hide in the private-foot branch.

Partial-code restrictions are exact:

- if `y,z in U` are antipodes, then `c(z)=bar(c(y))`;
- if `y in U` is antipodal to a matched endpoint `q in P_i`, then `c(y)=alpha(q)`, where `alpha(q)` chooses the mate of `q` in fibre `i` and the endpoint nonadjacent to `q` in every other fibre;
- if `q'` is the tight mate of `q`, then

`eta(yq)=epsilon_y-epsilon_q'`,

so an errorful matched-endpoint antipode forces `epsilon_y>=epsilon_q'+1`.

## 6. Full-tight support survives as a necessary subsystem

The P--P rooted B-edges among the tight pairs form the ordinary full-tight orientation graph `Omega_P`. Their selected A-witnesses obey exactly the old forced-code rule, so the realised A-code support `C_A` satisfies

`tau(Omega_P)<=|C_A|<=a`.                               `(SUP)`

Because

`a=2p+u-lambda-1`,

we have `a<=2p` iff `u<=lambda+1`.

The preserved support-only full-tight theorems imply that for `p>=19`, minimum switching defect `d_*>=5` gives `tau(Omega_P)>2p`. Hence:

> if `p>=19` and `u<=lambda+1`, the inherited matched-pair switching problem must have `d_*<=4`.

The old full-tight F-separation conclusions for `d_*=0,...,4` are not imported automatically; unmatched vertices alter the residual ledger.

## 7. Augmented orientation graph from unmatched vertices

For `y in U`, let `q_i in P_i` be the endpoint chosen by `y`.

Each physical P--U edge `y q_i` yields the two possible forced A-witness codes

`{alpha(q_i), beta_i(y)}`,                              `(AUG1)`

where `beta_i(y)` chooses `q_i` in fibre `i` and the endpoint nonadjacent to `y` in every other fibre.

Each U--U edge `yz` yields

`{bar(c(y)),bar(c(z))}`.                                `(AUG2)`

Together with the P--P constraints these form an augmented orientation multigraph `Omega+`. The realised A-code support must cover it.

There is also a per-source capacity rule: if `n_c` A-vertices realise code `c`, then at a fixed B-source at most `n_c` selected obligations can be assigned to endpoint code `c`.

This capacitated `Omega+` object is the correct place to reuse selected/Hall machinery in the near-full branch.

## 8. Branching antipodes pay quadratic error

Let `J_v` be the antipode graph. For `w in B`, put

`S=N_J(w)`, `d=|S|`,

`E_w=sum_{y in S} eta(yw)`.

A nonedge inside `S` consumes two antipode-error incidences, while every edge inside `S` injects by D2C edge-criticality into an error incidence. Consequently

> `3E_w >= d(d-1)`.                                    `(ABE)`

Globally,

`sum_{e in E(J_v)} eta(e) >= (1/6)sum_w d_J(w)(d_J(w)-1)`.   `(ABE-global)`

In the near-full `p>=2` branch, errorful antipode edges cover all unmatched vertices, so also

`sum_{e errorful} eta(e)>=ceil(u/2)`.

Files:

- `ANTIPODE_BRANCHING_ERROR_PAYMENT.md`;
- `check_antipode_branching_error_payment.py`;
- `ANTIPODE_BRANCHING_ERROR_CHECK_SUMMARY.json`.

The atlas regression covers all 21 D2C isomorphism classes through order seven, every root, 125 positive-degree antipode centres and 50 branching centres, with zero violations. This is regression evidence only.

## 9. New row-singleton reduction for one unmatched vertex

Fix `y in U`. Let `q_i in P_i` be the endpoints selected by `y`, and define a graph `K_y` on `[p]` by

`ij in E(K_y) iff q_i q_j in E(G)`.

For each `i`, let

`A_i={j!=i: ij notin E(K_y)}`.

Translate the Boolean cube by the common vector `bar(c(y))`. Then the P--U selected constraints at `y` become exactly

`{A_i,{i}}`, `i=1,...,p`.                               `(ROW)`

Call this `p`-edge graph on subset-codes `Psi(K_y)`.

Thus the ambient 2-lift signing disappears from the local unmatched-vertex problem: every unmatched row is controlled solely by the ordinary graph `K_y`.

### Exact one-code classification

For `p>=3`,

> `tau(Psi(K))=1` iff `K=K_p` or `K=K_{p-1} dotcup K_1`.

The proof is elementary. If one code `C` covers every edge `{A_i,{i}}`, then for every `i`, `C=A_i` or `C={i}`. Distinct singleton endpoints mean at most one index can use the second option. If none does, the common `A_i` must be empty and `K=K_p`. If `C={j}`, every `i!=j` has `A_i={j}`, giving a clique on the other `p-1` vertices and an isolated `j`.

This cheap-cover classification has direct antipode meaning:

- if `K_y=K_p`, all selected coordinates are universal and every tight mate is partial-code eligible as an antipode partner of `y`; moreover `{y,q_1,...,q_p}` is a large B-clique;
- if `K_y=K_{p-1} dotcup K_1`, no matched endpoint is partial-code eligible. Since `y` must have an antipode, it must have a partner `z in U`, necessarily with `c(z)=bar(c(y))`.

Files:

- `UNMATCHED_ROW_SINGLETON_COVER.md`;
- `check_unmatched_row_singleton_cover.py`;
- `UNMATCHED_ROW_SINGLETON_COVER_CHECK_SUMMARY.json`.

Exact atlas replay for every unlabelled graph of order `p=3,...,7` finds exactly two one-code cases at every order and zero violations. At `p=7`, for example, among 1044 graphs the exact cover-number distribution is

`tau=1,2,3,4,5,6,7 : 2,11,44,107,210,323,347`.

## 10. Important obstruction: ABE alone is not enough

Do not try to finish the near-full branch by an abstract weighted-matching extraction from `(ABE)` alone.

The abstract weighted antipode graph `K_{1,4}` with `eta(e)=1` on every edge satisfies every local ABE inequality exactly at its centre:

`3*4=4*3`,

but every matching contains only one edge. Thus ABE alone does not force a near-perfect matching or a matching capturing a large fraction of the total error.

No such degree-four/unit-error centre occurs in the D2C atlas through order seven; this is a methodological obstruction, not a realised D2C counterexample.

Full note:

`ANTIPODE_WEIGHTED_MATCHING_OBSTRUCTION.md`.

## 11. Active next move

The near-full branch is now compressed to a much more specific augmented-Hall problem.

For each unmatched `y`, price its row graph `Psi(K_y)`.

- **Generic rows:** `tau(Psi(K_y))>=2`. The next theorem should turn many such rows into A-code multiplicity pressure using the per-source Hall capacities, not merely distinct-support counting.
- **Cheap complete rows:** `K_y=K_p`. These produce a large B-clique and many matched-endpoint antipode-eligible codes; price them through D2C edge-criticality plus `(AS)/(ABE)`.
- **Cheap clique-plus-isolate rows:** `K_y=K_{p-1} dotcup K_1`. These force a complementary U--U antipode, so they feed directly into the errorful antipode graph and `(AMC)`.

When `p>=19` and `u<=lambda+1`, `(SUP)` has already reduced the underlying matched 2-lift to `d_*<=4`; this should be used as a low-complexity endpoint rather than reopening arbitrary switching defects.

The next compact theorem target is therefore an **unmatched-row capacity lemma**: bound how many P--U obligations can be routed through a small multiset of A-codes unless the unmatched vertices fall into the two explicitly classified cheap row types. That would directly couple `u` to A-code multiplicity and residual defect.

Do not return to the closed mixed `{4,5}` ladder, another fixed-defect enumeration, or first-proof optimization for Erdős #742 except for audit/regression support.

## 12. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure; no author-supplied adjacency file has been located.
- Full-tight eventual closure is an internal candidate pending external review; several finite terminal certificates remain to be journal-compressed.
- The near-full Boolean normal form, no-private reduction, augmented orientation constraints, ABE theorem and row-singleton classification are hand arguments.
- Atlas computations are audit/regression support only.
- The Q=0/twin-core branch remains separate and is not closed by the near-full work.
- No theorem yet converts all unmatched/errorful antipode configurations into enough `delta` to prove the eventual second-extremal result.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
