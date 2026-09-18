# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_BOOLEAN_SWITCHING_BRANCH_EVENTUALLY_CLOSED_INTERNAL_CANDIDATE_NEAR_FULL_STABILITY_NOW_ACTIVE`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit did not continue the fixed-defect ladder one integer at a time. It extracted a general open-neighbourhood twin package in a minimum-defect switched state, collapsed every nonlopsided minimum-defect geometry for `d_*>=7`, closed all lopsided states for `d_*>=9` by hand residual counting, certified the remaining `d_*=7,8` finite boundaries, and thereby internally exhausted the full tight-antipode Boolean switching branch for `k>=19`.

## 1. Preserved dense-root entry point

For a non-bipartite D2C graph above `M(n)`, the preserved maximum-root work forces a rooted triangle at a maximum-degree root. For `n>=14`, the all-private edge-witness theorem excludes the all-private branch and forces a disjoint-support antipode.

For an antipode `uw` at root `v`, with `B=N(v)`, `b=|B|`, `A=V\N[v]`, and `lambda=2b-n`, the exact slack identity is

`epsilon_u+epsilon_w=lambda+1+eta(uw)`,

where `eta` counts vertices adjacent to neither antipode endpoint. Tight antipodes are those with `eta=0`; they form a matching. For every antipode matching `M`,

`b lambda + r - Q >= |M|(lambda+1)+sum_{e in M} eta(e)`  `(AMC)`.

If tight antipodes cover all of `B`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then:

- `G[B]` is a 2-lift of `K_k`;
- every A-vertex is a Boolean transversal;
- `Q=e(G[B])=k(k-1)`;
- `r=k(a-k+1)`;
- `delta=r-e(F)`;
- the actual distinct A-code support is a vertex cover of the orientation-code graph `Omega_sigma`;
- an above-`M(n)` full-tight graph must have `a<=2k`.

For a Boolean code `c`, the switched graph `L_c` has

`phi(c)=k-#{leaf coordinates of L_c}`,

and

`d_Omega(c)=k-phi(c)`.

## 2. Mandatory 12-vertex negative control

The published Radosavljevic--Stanic--Zivkovic (2024) order-12, size-32 graph has been reconstructed directly from the authoritative Figure 1 and exactly checked. It is isomorphic to the project's `X_3`:

- 12 vertices;
- 32 edges, while `M(12)=31`;
- diameter 2;
- every edge critical;
- unique dominating edge;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

The eight inner vertices are `Q_3`, the three outer vertices are coordinate-zero faces, and the central root is universal on the cube.

Files:

- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`;
- `check_published_12_vertex_exception_figure.py`;
- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CHECK_SUMMARY.json`.

This is a direct figure reconstruction, not an author-supplied adjacency file. The `k=4` hostile control remains untouched by every eventual theorem below.

## 3. Preserved fixed-defect hierarchy through six

Before this unit the full-tight switching hierarchy was:

- defect `0`: residual-zero/perfect-matching mechanism leaves only finite `H5/X_3` boundaries; above threshold the perfect-matching state is excluded;
- defect `1`: complete one-defect regime eventually closed;
- defect `2`: complete regime closed from `k>=14`;
- defect `3`: complete regime closed from `k>=15`;
- defect `4`: complete regime internally closed from `k>=19`;
- defect `5`: support-impossible from `k>=8`;
- defect `6`: support-impossible from `k>=9`.

The general leaf package for `d>=3` exceptional/non-leaf coordinates, pendant sizes `p_i`, `t` isolated leaf-pairs, and `g` nonempty pendant groups is

`B_d = 2 sum_i (p_i-1)_+ + 2 sum_{i<j} min(p_i,p_j)`,

and for `t>=1`

`L_d = B_d + 4tg + 2t(t-1) + 1`.

Coordinatewise residual monotonicity reduces every fixed-`d`, fixed-core pendant problem to the status alphabet `0,1,>=2`.

The elementary large-minimum-defect degree bound gives, for

`d_* = min_c phi(c)`,

`tau(Omega)>=ceil(k(k-1)/(k-d_*))`.

Thus `2d_*>k+1` is already support-impossible. Before the present unit this left, for `k>=19`,

`7 <= d_* <= floor((k+1)/2)`.

## 4. New twin-package theorem

Choose a switched state attaining the minimum defect `d=d_*`, with `ell=k-d` leaves. In the only range not already closed by the degree bound,

`ell>=d-1`.

Decompose the leaves into ordinary pendant groups `P_j` of sizes `p_j` attached to `g` exceptional parents, plus `t` isolated leaf-pairs. Let `Q0` be the `q=d-g` exceptional coordinates carrying no ordinary pendant group. Partition `Q0` into equal-open-neighbourhood twin classes `T`.

For a twin class of size `m`, the forced orientation-code formula gives, vertex-disjointly from the old leaf-only package:

- `2 K_m` from pairs inside the twin class, cover `2(m-1)`;
- `2 K_{m,p_j}` against every pendant group, cover `2 min(m,p_j)`;
- two `K_{m,1}` copies against each isolated leaf, total `4t` cover per twin class.

Hence

`tau(Omega) >= L_d + 2 sum_T [(|T|-1)+sum_j min(|T|,p_j)+2t]`.

The disjointness is a hand code calculation. A collision between a twin-clique code and a pendant-star centre would force a zero-parent exceptional coordinate to have degree one, which is forbidden; the other potential collisions separate by leaf coordinate or collapse the neighbourhood classes.

Full note:

`MINIMUM_DEFECT_TWIN_PACKAGE_COLLAPSE.md`.

## 5. General consequence: every nonlopsided minimum-defect state closes for d>=7

Using `ell>=d-1`, the twin package gives strict support excess whenever:

- `g>=2` ordinary pendant groups;
- `g=1` and `t>=1`;
- `g=0` (all leaves lie in isolated pairs).

Therefore any surviving minimum-defect state with `d>=7` would have to be **pure lopsided**:

- `t=0`;
- `g=1`;
- all `z=k-d` leaves attach to one exceptional root;
- `z>=d-1`.

This is the main structural compression of the unit. The previous exponentially widening fixed-defect family has collapsed to one ray shape for arbitrary `d`.

## 6. Pure lopsided d>=10 closes uniformly

Put `q=d-1` for the nonroot exceptional coordinates. The leaf-leaf package and the exact nonroot-exception/leaf twin-star package already cost

`2(z-1)+2q = 2k-4`.

A directed `Q0-Q0` code is absorbed by one of those star-centre codes only when its source is root-adjacent and has exactly two neighbours in `Q0`. If `b_bad` is the number of unordered exceptional pairs with an absorbed endpoint, then for `q>=5`

`b_bad <= 2q-4`.

Hence at least

`(q^2-5q+8)/2`

exceptional pairs survive. Each gives two complementary residual orientation edges. A residual code has degree at most `q`, so

`tau(R_Q) >= ceil(q-5+8/q)`.

For `q>=9`, i.e. `d>=10`, this is at least five, exactly what is needed beyond `2k-4`.

Thus every minimum-defect state with `d_*>=10` is support-impossible: if `k-d_*<d_*-1` the elementary degree bound closes it; if `k-d_*>=d_*-1` the twin/lopsided theorem closes it.

## 7. d_*=9 closes by hand

For `d=9`, `q=8`. Retaining the twin-class core cliques gives lopsided package margin

`2(q-h-2)`

where `h` is the number of distinct open-neighbourhood classes among the eight nonroot exceptional coordinates.

- `h<=5`: package already strict;
- `h=6`: package equality, but a residual exceptional edge remains;
- `h=7`: at least 15 quotient residual edges remain after removing the unique twin-pair edge; degree at most eight gives quotient cover at least two and full complementary cover at least four;
- `h=8`: the worst absorbed-pair equality would force six identical root-adjacent neighbourhoods, contradicting `h=8`; at least 17 quotient edges remain, giving quotient cover at least three and full residual cover at least six.

Therefore `d_*=9` is excluded without a finite core scan.

## 8. d_*=7,8 finite boundary certificates

### Seven defects

For the pure lopsided seven-defect ray, audit at `z=3` over all rooted seven-vertex exceptional cores. The NetworkX graph atlas has 1044 unlabelled seven-vertex graphs; rooting and validity filtering leaves 4376 cores.

At `z=3` the leaf package has cover four. Maximum matching reaches the required residual target in all but 15 rooted cases. Exact solution of those 15 gives minimum residual cover 19, hence minimum additive margin

`4+19-2(10)=3`.

Coordinatewise residual monotonicity propagates that strict margin to every larger `z`, in particular the minimum-defect range `z>=6`.

### Eight defects

Here `q=7`.

- `h<=4`: twin package already strict;
- `h=5`: package equality and a residual quotient edge remains;
- `h=6`: package is two short, while the quotient residual has cover at least two, hence at least four over complementary halves;
- `h=7`: the sole finite boundary.

Enumerating all 1044 seven-vertex graph-atlas cores for `Q0` and all `2^7` root-neighbour masks leaves exactly 66513 valid all-distinct rooted cores. Every quotient residual graph has vertex-cover number at least three; there are zero cover-`<=2` cases. Thus the complementary residual contributes at least six, exceeding the four-code shortfall.

Files:

- `check_minimum_defect_d7_d8_lopsided_boundary.py`;
- `MINIMUM_DEFECT_D7_D8_LOPSIDED_BOUNDARY_CHECK_SUMMARY.json`.

## 9. New milestone: full-tight Boolean switching branch internally closed

Combining the preserved defect `0,...,6` results with Sections 4--8 gives:

> **FULL-TIGHT BOOLEAN SWITCHING EXCLUSION — internal candidate.** If tight antipodes cover all of `B` and `k>=19`, then an above-`M(n)` counterexample cannot occur.

The minimum switching defect is exhausted as follows:

- `0<=d_*<=6`: preserved fixed-defect results;
- `d_*=7,8`: finite boundary certificates after the hand twin-package reduction;
- `d_*=9`: hand residual-count closure;
- `d_*>=10`: uniform hand twin/lopsided closure or the elementary large-defect degree bound.

Full synthesis:

`FULL_TIGHT_SWITCHING_BRANCH_EVENTUAL_CLOSURE.md`.

This is the point at which continuing to classify switching defects would be the wrong optimization target.

## 10. Active frontier: lift from full-tight to near-full/errorful antipodes

The clean Boolean switching problem is now internally exhausted. The main mathematical attack should return to the stability layer.

The relevant preserved facts are:

- all-private maximum-root triangle branch is impossible above `M(n)` for `n>=14` by edge-witness pricing;
- therefore a dense counterexample enters the antipode branch;
- tight antipodes form a matching;
- errorful antipodes pay exactly through `eta` in `(AS)` and `(AMC)`;
- a full tight matching is now eventually impossible by Section 9.

The next high-value theorem is therefore a **near-full tight-matching / antipode-error stability inequality**: show that if the tight matching does not cover all of `B`, then the unmatched vertices and/or positive `eta` force enough extra canonical defect `delta` to reach `m<=M(n)`. The full-tight closure should be used as the zero-error endpoint, not reopened.

A useful first quantitative identity for a tight antipode matching of size `p`, with `u=b-2p` unmatched B-vertices, follows from `(AMC)` and the general maximum-degree inequality `r<=Q+2delta`:

`(b-u)(lambda+1)/2 <= b lambda + 2delta`,

or

`u(lambda+1) >= b(1-lambda)-4delta`.

This alone is not yet sufficient, but it identifies the correct variables for the next stability step. Positive antipode errors add directly to the left side of `(AMC)` and should only strengthen the payment.

Do not return to the closed `{4,5}` ladder, first-proof optimization for Erdős #742, or another fixed switching-defect scan unless needed as a regression check.

## 11. Trust boundary

- The published 12/32 graph is directly reconstructed from the authoritative figure and exactly checked, but no author-supplied adjacency file has been located.
- The leaf-package, coordinatewise monotonicity, twin-package, lopsided residual count, and `d=9` reductions are hand structural arguments.
- The `d=7,8` terminal boundaries are finite rooted-core certificates; older four-/five-/six-defect steps also contain finite proof-producing certificates. These remain internal theorem candidates pending external mathematical review and journal-style compression.
- The new full-tight closure concerns only the full tight-antipode Boolean branch. Near-full, unmatched, and errorful antipode configurations remain open.
- Exact computations are audit/certificate support, not substitutes for the unbounded structural reductions.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
