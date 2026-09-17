# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `LEAF_RICH_FULL_TIGHT_SWITCHING_BRANCHES_EXCLUDED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. Two independent continuations from predecessor `0a311bae71ee15045926dbbe4fa3e70737c88998` have now been reconciled rather than overwritten. One closed the first surviving small-residual layer `a=k+1,r=2k` below `M(n)` for `k>=17` by a Hamming-support defect bound. The present unit critically reassessed the eventual scale and found a stronger large-order direction: in any above-`M(n)` full-tight graph with `b=2k`, the handshake bound forces `a<=2k`, so genuinely large candidates live near `a=2k`, not near `a=k+1`. Exploiting that, two leaf-rich switching subbranches are now excluded for `k>=8`.

## Preserved full-tight entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces rooted triangles at a maximum-degree root. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover `B=N(v)`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`; every `A`-vertex is a Boolean transversal; and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=r-e(F)`.

The residual-zero classification preserves only `k=2` (`H5`) and `k=4` (`X_3`). For `k>=5`, the Boolean witness-cover theorem gives at least `k+1` distinct A-codes and excludes `a=k,r=k`.

The orientation-code graph `Omega_sigma` has one vertex per Boolean code and one edge per physical rooted B-edge; the actual distinct code support `C` is a vertex cover. If `ell(c)` is the number of degree-one coordinates of the switched graph `L_c`, then

`Q <= sum_{c in C} ell(c)`.

## Preserved second-positive Hamming closure

At the first surviving layer

`a=k+1`, `r=2k`,

the Boolean witness-cover theorem forces all `k+1` A-codes to be distinct. If `D_x` is the residual-coordinate set of label `x`, with `R_x=|D_x|`, F-separation gives

`d_F(x) <= min(k,2^{R_x}-1)`,

and

`sum_x R_x=2k`.

This yields `e(F)<=k^2/5` for `k>=19`, with sharper boundary arithmetic at `k=17,18`, and therefore

> **SECOND POSITIVE-RESIDUAL FULL-TIGHT DEFECT THEOREM — internal candidate:** the layer `a=k+1,r=2k` lies strictly below `M(n)` for every `k>=17`.

Full note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/SECOND_POSITIVE_RESIDUAL_HAMMING_DEFECT.md`.

This result remains valid and preserved, but the present unit shows that it should not define the main eventual strategy.

## New density window: eventual full-tight candidates lie near a=2k

Because `Delta=2k`, every graph satisfies `m<=n Delta/2=nk`. If `n>=4k+2`, the exact parity formulas for `M(n)` give `M(n)>nk`. Hence any above-`M(n)` full-tight graph must satisfy

> `n<=4k+1`, hence `a<=2k`.

This is the correct large-order scale for the full-tight branch.

## New perfect-matching switching exclusion

Suppose some switched state `L_c` is a perfect matching. For even `k>=6`, the preserved switching lemma says every genuinely different switched state has at most two leaves; only the complementary code pair gives the same matching. Thus any witness-code cover satisfies

`k(k-1) <= 2k + 2(|C|-2)`,

and therefore

> `|C| >= (k^2-3k+4)/2`.

For even `k>=8`, this exceeds `2k`, contradicting `|C|<=a<=2k` in an above-threshold graph.

> **PERFECT-MATCHING SWITCHING EXCLUSION — internal candidate:** an above-`M(n)` full-tight graph with even `k>=8` has no perfect-matching switched state.

The `k=4` `X_3` hostile control remains outside the range.

## New full-star orientation-code normal form

Suppose some `L_c` is a full star `K_{1,k-1}`. Gauge switching by `c` and then at the star centre reduces to `sigma=0`. For `k>=5`, the only leaf-bearing codes are

`e_1,...,e_k` and their complements.

The orientation-code graph is exactly

> `Omega_sigma ~= K_k dotcup K_k`

plus isolated code vertices. Hence every actual witness-code support has

> `|C|>=2k-2`.

Combined with `a<=2k`, an above-threshold star-class graph has only

`a in {2k-2,2k-1,2k}`,

or, with `lambda=2k-a-1`,

> `lambda in {1,0,-1}`.

So this switching class collapses to three near-balanced residual layers before any detailed F analysis.

## New F-separation closure of the full-star class

Stay in the zero-signing gauge and call `e_i` the low layer and `bar(e_i)` the high layer. A selected coordinate at label `x` forces every F-neighbour of `x` to agree with `x` in that coordinate.

Call a star-code label clean when its code occurs exactly once. If

`q=a-(2k-2)=1-lambda in {0,1,2}`,

then at most `2q` labels are non-clean.

For clean labels:

1. two distinct labels in the same star layer cannot be F-adjacent: the corresponding `Omega` edge must be selected at one of the two singleton labels, and the labels disagree in that selected coordinate;
2. a low/high clean F-edge forces both endpoints to have residual degree at least `k-1` (or `k` for complementary indices).

If `h` is the number of clean labels with residual degree at least `k-1`, then

`h(k-1)<=r`,

and the clean-clean F graph is bipartite. With `d_F<=k` on the at most `2q` exceptional labels,

> `e(F) <= floor(h^2/4)+2(1-lambda)k`,
>
> `h <= floor(r/(k-1))`.

For the three possible imbalance values this gives:

- `lambda=1`: closure to `m<=M(n)` for every `k>=5`;
- `lambda=0`: closure for every `k>=6`;
- `lambda=-1`: closure for every `k>=8`.

Therefore:

> **FULL-STAR SWITCHING EXCLUSION — internal candidate.** In the full tight-antipode branch, if the Boolean switching class contains a full star and `k>=8`, then `m<=M(n)`.

Full note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/LEAF_RICH_SWITCHING_EXCLUSIONS.md`.

## Verification

New companion files:

- `check_leaf_rich_switching_exclusions.py`
- `LEAF_RICH_SWITCHING_EXCLUSIONS_CHECK_SUMMARY.json`

Finite replay verifies:

- zero-signing switching classes through `k=12`: exactly `2k` leaf-bearing codes, all stars;
- `Omega_sigma` is exactly two `K_k` components in that gauge;
- perfect-matching cover arithmetic through `k=20`;
- full-star defect arithmetic through `k=30`, with exact closure thresholds `k=5,6,8` for `lambda=1,0,-1`.

The preceding Hamming-defect checker independently replayed the `a=k+1,r=2k` theorem through `k=5000`.

Finite checks are regression evidence only. The universal statements are the hand proofs.

## Mandatory negative control and trust boundary

- `k=2,r=0`: classical `H5` remains allowed.
- `k=4,r=0`: the independent twelve-vertex `X_3` Boolean/cube mechanism remains allowed with `n=12,m=32>M(12)=31`.
- None of the new sufficiently-large exclusions suppresses the finite hostile control or revives the false all-order Conjecture 3.
- Direct adjacency-list certification of the published 2024 Figure-1 graph against the project's `X_3` reconstruction remains open; no stronger identification is claimed.
- External mathematical review and novelty assessment remain open.

## Strategic consequence

The full-tight branch now has both a **small-residual staircase** and a more relevant **large-order switching reduction**:

- `r=0`: only finite `H5/X_3` mechanisms;
- `r=k`: impossible for `k>=5`;
- `r=2k`: below `M(n)` for `k>=17`;
- for any above-threshold full-tight graph, density forces `a<=2k`;
- perfect-matching switched states are impossible above `M(n)` for even `k>=8`;
- full-star switched states are impossible above `M(n)` for every `k>=8`.

The highest-value next target is therefore **not** simply the next algebraic residual layer `r=3k`. It is the remaining intermediate switching regime at the eventual scale:

- no perfect-matching state;
- no full-star state;
- possible non-star one-defect states, especially the previously classified `K_{1,k-3} dotcup K_2` triad;
- otherwise every useful switched state has at least two non-leaf coordinates.

Finite orientation-code data still suggest the universal bound

`tau(Omega_sigma)>=2k-2` for `k>=5`.

A realistic next bounded unit is to prove this first for the non-star one-defect switching class (especially the `K_{1,k-3} dotcup K_2` triad). If successful, every above-threshold full-tight graph in that class is forced into `a>=2k-2`, after which the same near-balanced F-separation strategy can be applied. A universal `tau>=2k-2` theorem would be a major structural compression of the whole full-tight branch.

Use `(AMC)` only when returning to near-full/unmatched/errorful antipodes. Do not revisit Q0, the closed mixed `{4,5}` selected-excess ladder, or first-proof optimization for Erdős #742.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
