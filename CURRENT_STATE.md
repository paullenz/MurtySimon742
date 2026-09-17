# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `ALL_ONE_DEFECT_FULL_TIGHT_SWITCHING_CLASSES_EVENTUALLY_EXCLUDED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit resumed from `5419f061681742fb29358598ba0468af07500e32`, critically kept the eventual-scale `a<=2k` density window as the main guide, and attacked the remaining non-star one-defect switching class rather than returning to the small-residual staircase. The class admits an exact orientation-code decomposition: two `K_{k-3}` components plus three balanced double-stars. Consequently `tau(Omega_sigma)=2k-2` exactly. Combining the resulting near-balanced support with F-separation excludes the whole non-star one-defect class above `M(n)` for `k>=16`.

## Preserved full-tight entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces rooted triangles at a maximum-degree root. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover `B=N(v)`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`; every A-vertex is a Boolean transversal; and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=r-e(F)`.

The order-12/32 hostile control is exactly the `k=4,r=0` Boolean/cube normal form and remains mandatory.

The orientation-code graph `Omega_sigma` has one code vertex per Boolean code and one edge per physical rooted B-edge, joining its two possible orientation-witness codes. The distinct A-code support `C` is a vertex cover. If `ell(c)` is the number of degree-one coordinates of the switched graph `L_c`, then

`deg_Omega(c)=ell(c)`

(counting physical multiplicity) and

`Q <= sum_{c in C} ell(c)`.

## Preserved structural barriers

### Residual-zero / small-residual staircase

- `r=0`: full-tight switching/factorization classification leaves only `k=2` (`H5`) and `k=4` (`X_3`).
- `r=k`: impossible for `k>=5` by the Boolean witness-code cover theorem.
- `a=k+1,r=2k`: below `M(n)` for every `k>=17` by the Hamming-support defect theorem.

These remain valid but are not the main eventual-scale strategy.

### Above-M density window

Because `Delta=2k`, every graph satisfies `m<=nk`. Comparing with `M(n)` gives:

> if `m>M(n)` in the full-tight branch, then `a<=2k`.

So genuinely large candidates live near the balanced scale `a=2k`.

### Previously closed leaf-rich switching classes

- If some switched state is a perfect matching, code-cover capacity excludes above-`M(n)` full-tight graphs for even `k>=8`.
- If some switched state is a full star, `Omega_sigma ~= K_k dotcup K_k`; hence `|C|>=2k-2`, and F-separation closes the whole full-star class above `M(n)` for `k>=8`.

Full note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/LEAF_RICH_SWITCHING_EXCLUSIONS.md`.

## New exact normal form: non-star one-defect switching class

Assume the switching class contains

`K_{1,k-3} dotcup K_2`.

Gauge so that the zero code gives this graph. Write

`[k]={a,b,c} dotcup D`, `|D|=k-3`,

with signing edges

`{ad:d in D} union {bc}`.

The three one-defect switched states have exceptional vertices `a,b,c`, with six complementary centre codes

`z_a=empty`, `bar z_a=[k]`,

`z_b=[k]\{a,b}`, `bar z_b={a,b}`,

`z_c=[k]\{a,c}`, `bar z_c={a,c}`.

For each `d in D`, put

`x_d={a,d}`, `bar x_d=[k]\{a,d}`.

Direct evaluation of the forced orientation-witness formula gives the complete orientation-code graph.

### Exact decomposition

After deleting isolated code vertices:

> **NON-STAR ONE-DEFECT ORIENTATION-CODE NORMAL FORM — internal candidate**
>
> `Omega_sigma ~= K_{k-3} dotcup K_{k-3} dotcup T_a dotcup T_b dotcup T_c`,
>
> where each `T_*` is a balanced double-star with two adjacent centres and `k-3` leaves on each centre.

In the physical-edge multigraph, each central double-star edge has multiplicity two. The two clique layers are the codes `{x_d}` and `{bar x_d}`.

The quotient-pair accounting is exact:

- pairs `de` inside `D` give clique edges `x_dx_e` and `bar x_d bar x_e`;
- pairs from `{a,b,c}` to `D` give the pendant double-star edges;
- the two physical edges over each pair inside `{a,b,c}` give the doubled central edge of the corresponding double-star.

Full note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/NONSTAR_ONE_DEFECT_SWITCHING_EXCLUSION.md`.

## Exact cover number tau=2k-2

Each `K_{k-3}` contributes cover number `k-4`; each balanced double-star contributes exactly `2`. Therefore

> `tau(Omega_sigma)=2(k-4)+6=2k-2`.

Thus every actual distinct code support satisfies

`|C|>=2k-2`.

Combining with `a<=2k`, any above-threshold graph in this class has only

`a in {2k-2,2k-1,2k}`,

or, with `lambda=2k-a-1`,

`lambda in {1,0,-1}`.

For `k>=7`, any vertex cover of size at most `2k` must contain all six double-star centre codes: replacing a centre pair by leaves costs at least `k-4>=3` extra vertices. Each clique contributes at least `k-4` of its `k-3` vertices, so at most one code from each clique can be omitted.

This proves the previously conjectured `tau>=2k-2` bound exactly for the complete non-star one-defect class.

## New F-separation closure

Let

`q=a-(2k-2)=1-lambda in {0,1,2}`.

Choose a minimum canonical core: all six double-star centres and `k-4` codes from each clique. Mark all six centre labels exceptional; also mark duplicate clique-code classes and labels outside the canonical clique core. There are at most `2q` exceptional non-centre labels, hence

`|E|<=6+2q=8-2lambda`.

Every other label is a clean singleton clique code.

### Clean same-clique labels are F-independent

For `d!=e`, `Omega` contains the edge `x_dx_e`; because both labels are singleton classes, the represented rooted B-edge must be selected at one endpoint. The selected source coordinate is one of `d,e`, where the two codes disagree. F-separation therefore forbids an F-edge. The same holds in the complementary clique.

### Clean cross-clique F-edges require R>=k-1 at both ends

For `d!=e`, the codes `x_d` and `bar x_e` agree only at coordinates `d,e`. The switched graph at `x_d` has leaf set `D\{d}`; among the two agreement coordinates only `e` can be selected. Thus an F-edge forces selected cross-degree at most one and residual degree at least `k-1`. Symmetrically the other endpoint also has residual degree at least `k-1`. When `d=e`, the codes are complements and force residual degree `k`.

If `h` is the number of clean labels with residual degree at least `k-1`, then

`h(k-1)<=r`,

and the clean-clean F graph is bipartite between the two clique layers. Therefore

> `e(F) <= floor(h^2/4) + (8-2lambda)k`,
>
> `h <= floor(r/(k-1))`.

This deliberately overcharges every edge incident with the exceptional set at the maximum possible F-degree `k`.

## Eventual exclusion of the non-star one-defect class

For the three near-balanced values,

`r=k(k-lambda)`

and

- `lambda=1`: `h<=k`, `e(F)<=floor(k^2/4)+6k`;
- `lambda=0`: `h<=k+1`, `e(F)<=floor((k+1)^2/4)+8k`;
- `lambda=-1`: `h<=k+2`, `e(F)<=floor((k+2)^2/4)+10k`.

The exact defect needed for `m<=M(n)` is

- `2k-2` when `lambda=1`;
- `2k-1` when `lambda=0`;
- `2k-1` when `lambda=-1`.

The resulting closure thresholds are:

- `lambda=1`: every `k>=12`;
- `lambda=0`: every `k>=14`;
- `lambda=-1`: every `k>=16`.

Therefore:

> **NON-STAR ONE-DEFECT SWITCHING EXCLUSION — internal candidate.** In the full tight-antipode branch, if the Boolean switching class contains `K_{1,k-3} dotcup K_2` and `k>=16`, then `m<=M(n)`.

Together with the full-star theorem, this closes the entire one-defect switching regime for sufficiently large fibre count.

## Verification

Companion files:

- `project/research/post_ms/2026-09-17-stronger-pivot-v1/check_nonstar_one_defect_switching_exclusion.py`
- `project/research/post_ms/2026-09-17-stronger-pivot-v1/NONSTAR_ONE_DEFECT_SWITCHING_EXCLUSION_CHECK_SUMMARY.json`

Finite regression:

- exact orientation-code construction for every `k=5,...,100`;
- every case gives exactly two clique components of size `k-3` and three double-stars of size `2k-4`;
- exactly three simple central pairs have multiplicity two;
- `tau(Omega_sigma)=2k-2` throughout;
- defect arithmetic checked through `k=5000`, reproducing exact thresholds `12,14,16` for `lambda=1,0,-1`.

These are regression checks only. The universal claims are the hand proofs.

## Mandatory negative control and trust boundary

- `k=2,r=0`: classical `H5` remains allowed.
- `k=4,r=0`: independent twelve-vertex `X_3` Boolean/cube mechanism remains allowed with `n=12,m=32>M(12)=31`.
- The new theorem begins far above the hostile-control range and does not suppress it.
- Direct primary-source adjacency certification of the published 2024 Figure-1 graph against the project's `X_3` reconstruction remains open; no stronger identification is claimed.
- External mathematical review and novelty assessment remain open.
- No all-order second-extremal theorem is claimed.

## Strategic consequence

The full-tight branch now has the complete leaf-rich switching regime structurally compressed:

1. perfect-matching switched states: excluded above `M(n)` for even `k>=8`;
2. full-star one-defect states: excluded above `M(n)` for `k>=8`;
3. non-star one-defect `K_{1,k-3} dotcup K_2` states: excluded above `M(n)` for `k>=16`.

The conjectured orientation-code cover bound `tau(Omega_sigma)>=2k-2` is now proved with equality for both one-defect normal forms.

**NEXT ACTION:** move to the genuinely intermediate switching regime in which every switched state has at least two non-leaf coordinates and there is no perfect-matching state. The highest-value next theorem is a universal or stability version of

`tau(Omega_sigma)>=2k-2`.

Do not start with a broad signing enumeration. First derive a structural lower bound from the leaf sets themselves: every `Omega` edge is an oriented leaf incidence, and pairwise switching says the symmetric difference of two switched states is a complete cut. Seek a compact argument that either forces `tau>=2k-2` for sufficiently large `k` or isolates a new finite list of low-cover switching normal forms. If the bound fails, preserve the first explicit obstruction and classify it rather than hiding it behind scalar inequalities.

Use `(AMC)` only when returning to near-full/unmatched/errorful antipodes. Do not revisit Q0, the closed mixed `{4,5}` selected-excess ladder, or first-proof optimization for Erdős #742.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
