# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_FIXED_DEFECTS_THROUGH_SIX_CLOSED_AND_MINIMUM_DEFECT_WINDOW_ISOLATED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The current line is the triangle-containing full tight-antipode Boolean branch. Since the previous live-state checkpoint, the complete four-defect regime was closed, five defects were shown support-impossible, the published 12/32 exception was directly certified as the project's `X_3`, coordinatewise residual monotonicity was extracted, and the complete six-defect regime was shown support-impossible from `k>=9`. A universal orientation-code degree bound now reduces the remaining full-tight switching gap for `k>=19` to minimum switching defect between `7` and `floor((k+1)/2)`.

## 1. Preserved full-tight entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces rooted triangles at a maximum-degree root. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover

`B=N(v)=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`,

then:

- `G[B]` is a 2-lift of `K_k`;
- every A-vertex is a Boolean transversal;
- `Q=e(G[B])=k(k-1)`;
- `r=k(a-k+1)`;
- `delta=r-e(F)`;
- the actual distinct A-code support is a vertex cover of the orientation-code graph `Omega_sigma`;
- if `m>M(n)` in this full-tight branch, then `a<=2k`.

For a Boolean code `c`, its switched graph `L_c` has

`ell(c)=#{j:d_{L_c}(j)=1}`

leaf coordinates and switching defect

`phi(c)=k-ell(c)`.

The orientation-code degree is exactly

`d_Omega(c)=ell(c)`.

## 2. Mandatory 12-vertex negative control is now directly identified

The previous documentary gap has been materially closed.

Files:

- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`;
- `check_published_12_vertex_exception_figure.py`;
- `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CHECK_SUMMARY.json`.

Direct edge tracing from Figure 1 of Radosavljevic--Stanic--Zivkovic (2024), DOI `10.2298/PIM2429021R`, followed by an exact graph check, shows that the published order-12, size-32 graph is isomorphic to the project's independently reconstructed `X_3`.

The eight inner vertices are exactly `Q_3`; the three outer vertices are the three coordinate-zero faces; the central root is universal on the cube. The reconstructed graph has:

- 12 vertices;
- 32 edges, so `32>M(12)=31`;
- degree sequence `8,7,6,6,6,5,5,5,4,4,4,4`;
- diameter 2;
- every edge critical;
- a unique dominating edge.

In the full-tight notation it is precisely

`k=4, b=8, a=3, r=0, F=emptyset`.

Trust boundary: this is a direct reconstruction from the authoritative published vector figure, not an author-supplied machine-readable adjacency list. It is nevertheless now an explicit graph-level identification, not merely an invariant match.

## 3. Fixed-defect hierarchy now complete through six

The preserved switching hierarchy is:

- defect `0`: residual-zero classification leaves only `H5` and the finite `k=4` `X_3` mechanism; perfect-matching switched states are excluded above threshold for even `k>=8`;
- defect `1`: complete one-defect regime eventually closed;
- defect `2`: complete regime closed from `k>=14`;
- defect `3`: complete regime closed from `k>=15`;
- defect `4`: complete regime internally closed from `k>=19`;
- defect `5`: **support-impossible from `k>=8`**;
- defect `6`: **support-impossible from `k>=9`**.

The four-defect completion is in

`FOUR_DEFECT_COMPLETE_SWITCHING_EXCLUSION.md`.

Its nonlopsided finite-width strips are eliminated by an exact leaf-package plus a residual matching certificate; only the previously handled lopsided family needs F-separation. The finite four-core matching lemma remains internally certified rather than hand-compressed for publication.

The five-defect theorem is in

`FIVE_DEFECT_COMPLETE_SUPPORT_EXCLUSION.md`.

For `k>=8`, every five-defect switching state has `tau(Omega)>2k`. Five defects therefore require no F-separation cleanup. The infinite pendant rays are reduced by residual vertex-cover monotonicity to finite exceptional-core certificates; the only dangerous lopsided rooted cores have explicit all-ray component formulas, with worst exact cover `2k+1`.

## 4. General leaf package and coordinatewise residual monotonicity

For a switched state with `d>=3` non-leaf exceptional coordinates, pendant sizes `p_1,...,p_d`, `t` isolated leaf-leaf `K_2` components, and `g` nonempty pendant groups, the exact leaf-only package is

`B_d = 2 sum_i (p_i-1)_+ + 2 sum_{i<j} min(p_i,p_j)`

and, for `t>=1`,

`L_d = B_d + 4tg + 2t(t-1) + 1`.

If `p_(1)<=...<=p_(d)` then

`B_d = 2S-2g + 2 sum_i (d-i)p_(i)`.

The new note

`COORDINATEWISE_RESIDUAL_RAY_MONOTONICITY.md`

removes an unnecessary “largest pendant group” restriction from the earlier ray lemma. If **any** pendant group has size at least two, adding another leaf to that group:

- embeds the old residual orientation-code graph outside the leaf package into the new residual graph;
- cannot decrease its vertex-cover number;
- increases the exact leaf-package cover by at least two while `2k` increases by exactly two.

Hence the support margin

`L_d + tau(R) - 2k`

is coordinatewise nondecreasing once a pendant size has reached two.

Consequently every fixed-`d`, fixed-`t`, fixed-core attachment problem reduces to the finite status alphabet

`0, 1, >=2`,

with every `>=2` coordinate tested at its boundary value `2` (or the first value needed to enter a chosen order threshold). This is the current reusable finite-state reduction.

## 5. Complete six-defect support theorem

Files:

- `SIX_DEFECT_LOPSIDED_SUPPORT_EXCLUSION.md`;
- `check_six_defect_lopsided_support_exclusion.py`;
- `SIX_DEFECT_LOPSIDED_SUPPORT_CHECK_SUMMARY.json`;
- `SIX_DEFECT_COMPLETE_SUPPORT_EXCLUSION.md`;
- `check_six_defect_complete_support_exclusion.py`;
- `SIX_DEFECT_COMPLETE_SUPPORT_CHECK_SUMMARY.json`.

### Lopsided ray

For six defects with no isolated leaf-pairs and all leaves on one exceptional coordinate, the first eventual base is `z=3`, `k=9`. There are `15572` valid labelled six-vertex exceptional cores.

The disjoint leaf-package/residual lower bound is strict for every core except 15 labelled cores, all one rooted isomorphism class. The exceptional core is

`K_2 join 2K_2`,

with one joined `K_2` vertex the pendant root.

For this core the full orientation-code graph has the exact all-`z` decomposition

- four doubled `K_2` components;
- two `K_{z+1}` cliques;
- eight `K_{1,z+2}` stars;
- one balanced double-star with `z+1` leaves per centre and centre-edge multiplicity four.

Therefore

`tau(Omega)=2z+14=2k+2`.

Every other core is propagated by residual monotonicity. Thus the lopsided ray is support-impossible for `k>=9`.

There is a genuine lower-order switching obstruction: at `z=2`, `k=8`, the empty six-vertex exceptional core has `tau(Omega)=16=2k`. No D2C realization is claimed.

### Complete six-defect boundary

Coordinatewise monotonicity plus the leaf-package inequality reduces all six-defect states with `k>=9` to exactly **31** finite attachment-status boundaries:

- `t=0`: 14;
- `t=1`: 8;
- `t=2`: 5;
- `t=3`: 3;
- `t=4`: 1;
- `t>=5`: impossible from the leaf package alone.

The lopsided boundary is handled above. Of the remaining 30 patterns, 29 are certified for **every valid labelled six-vertex core** by an explicit deterministic residual matching, with minimum certified support margin `+1`.

The sole generic matching miss is the fixed state

`t=2`, `p=(0,0,0,0,0,0)`, `k=10`, empty exceptional core.

Its residual graph is exactly

`8 K_{1,6} + 2 K_6`,

so `tau(R)=18`. Its leaf package has cover `5`, hence

`tau(Omega)>=23>20=2k`.

Therefore:

> **COMPLETE SIX-DEFECT SUPPORT EXCLUSION — internal candidate.** If a full tight-antipode switching class contains a state with exactly six non-leaf coordinates and `k>=9`, then `tau(Omega)>2k`; hence it cannot occur in an above-`M(n)` full-tight graph.

No F-separation is needed for defects five or six.

## 6. Universal large minimum-defect exclusion

Let

`d_* = min_c phi(c)`

be the minimum switching defect across the entire signing.

Since `|E(Omega)|=k(k-1)` and every code vertex has degree at most `k-d_*`, every vertex cover satisfies

`tau(Omega) >= ceil(k(k-1)/(k-d_*))`.

Therefore if

`2d_*>k+1`,

then

`tau(Omega)>2k`,

which is impossible above threshold.

Full note:

`MINIMUM_SWITCHING_DEFECT_DEGREE_BOUND.md`.

Combining this elementary bound with the complete fixed-defect hierarchy gives the current sharp switching window:

> for `k>=19`, any above-`M(n)` full-tight signing would have to satisfy
>
> `7 <= d_* <= floor((k+1)/2)`.

This is now the main full-tight structural gap.

## 7. Strategic next move

Do **not** simply classify seven defects as another isolated integer unless it is needed diagnostically.

The highest-value target is a defect-count-dependent residual-core lower bound capable of bridging

`7 <= d_* <= floor((k+1)/2)`.

The preferred route is:

1. use the coordinatewise `{0,1,>=2}` reduction to identify what the worst residual exceptional-core configurations can look like for general `d`;
2. seek a lower bound on the residual exceptional-core witness cover/matching that grows with `d`;
3. use `d=7` exact work only to discover or falsify that proposed general inequality;
4. combine it with the elementary large-minimum-defect degree bound above.

The lopsided case is a natural first general test: after removing its leaf package, only a `d`-vertex rooted exceptional core remains, and defects five and six both already exhibit strict support excess.

Once the full-tight branch is structurally compressed, return to near-full/unmatched/errorful antipodes using `(AMC)`; do not prematurely mix that instability into the clean Boolean switching problem.

## 8. Trust boundary

- The 12/32 published graph is directly reconstructed from the authoritative figure and exactly checked, but no author-supplied adjacency file has been located.
- The leaf-package and coordinatewise monotonicity lemmas are hand structural arguments.
- The four-, five-, and six-defect core steps contain finite proof-producing certificates that have not yet been compressed into journal-style hand classifications; they remain internal theorem candidates pending external review.
- Exact computations are audit/certificate support, not substitutes for the unbounded structural reductions.
- No all-order second-extremal theorem is claimed.
- External novelty assessment and mathematical review remain open.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
