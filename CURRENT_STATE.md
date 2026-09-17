# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FIRST_POSITIVE_RESIDUAL_FULL_TIGHT_LAYER_EXCLUDED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. The residual-zero full-tight Boolean boundary had already been classified at predecessor `5951cbb99378524492dd7afdb09e7a4984d25f11`: only `k=2` (`H5`) and `k=4` (`X_3`) survive. This unit did not duplicate that work. It attacked the first positive-residual layer and extracted a stronger Boolean witness-code cover theorem.

## Preserved entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces every maximum-degree root `v` to have rooted triangles `Q=e(G[N(v)])>0`. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover `B=N(v)`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`; every `A`-vertex is a Boolean transversal; and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=k(a-k+1)-e(F)`.

The order-12/32 hostile control is exactly the `k=4,r=0` Boolean/cube normal form.

## Boolean witness-code cover

Choose endpoint bits on the antipode fibres and let `sigma_ij` encode the 2-lift. For a Boolean code `c in {0,1}^k`, define its switched graph `L_c` on `[k]` by

`ij in E(L_c)` iff `sigma_ij xor c_i xor c_j = 1`.

Let

`ell(c)=#{j:deg_{L_c}(j)=1}`,

`phi(c)=k-ell(c)`.

A selected H-cross incidence at source fibre `j` can occur only when `j` is a leaf of `L_c`; the unique leaf neighbour determines the rooted B-edge represented by that incidence. Multiple A-labels with the same code cannot reuse that rooted B-edge. Therefore, if `C` is the set of **distinct** A-codes,

> `Q <= sum_{c in C} ell(c)`.

Equivalently,

> `sum_{c in C} phi(c) <= k|C|-k(k-1)`.

The same structure can be packaged as an orientation-code graph `Omega_sigma`: one vertex per Boolean code and one edge per physical B-edge, joining its two possible orientation-witness codes. The actual code support `C` must be a vertex cover of `Omega_sigma`.

Full proof:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/FIRST_POSITIVE_RESIDUAL_TIGHT_COVER_GAP.md`.

## New switching theorem — at least k+1 witness codes for k>=5

Two local facts drive the proof.

1. If `k>=6`, switching a perfect matching by a genuinely nontrivial complete cut leaves at most two degree-one vertices. Thus any different switched state has `phi>=k-2`.
2. If two distinct switched graphs each have exactly one non-leaf vertex, with exceptional coordinates `a,b`, then their switching cut is `{a,b}` (up to complement). The first graph is either:
   - the full star centred at `a`; or
   - `K_{1,k-3} dotcup K_2`, with the isolated edge containing `b`.

Assume a code cover has at most `k` distinct codes.

- Fewer than `k-1` codes do not have enough leaf capacity.
- `k-1` codes would force every switched graph to be a perfect matching, impossible for `k>=5` by the residual-zero switching obstruction.
- With exactly `k` codes, total leaf deficiency is at most `k`. Perfect-matching states are impossible for even `k>=6` because every genuinely different switch costs at least `k-2`; odd `k` has no perfect matching. Hence all `k` codes must be one-defect states.
- Distinct one-defect states are then either a family of stars or, in the only non-star possibility, a three-state `K_{1,k-3}+K_2` triad. Neither can cover both physical B-edges over every quotient edge: the star family fails by a binary complement-sign obstruction, and the triad leaves every pair inside the common set `D` uncovered when `k>=5`.

Therefore:

> **BOOLEAN WITNESS-COVER THEOREM — internal candidate.** For every full tight-antipode Boolean system with `k>=5`, the set of distinct A-codes covering all rooted B-edges satisfies
>
> `|C| >= k+1`.

Since `a>=|C|`, the exact full-cover residual formula gives

> `a>=k+1`,
>
> `r=k(a-k+1)>=2k`.

Thus the entire algebraically first positive residual layer

`a=k`, `r=k`

is impossible. Together with the residual-zero classification, there is a genuine two-layer gap away from the `H5/X_3` boundary.

## Verification

Files:

- `FIRST_POSITIVE_RESIDUAL_TIGHT_COVER_GAP.md`
- `check_first_positive_residual_tight_cover_gap.py`
- `FIRST_POSITIVE_RESIDUAL_TIGHT_COVER_CHECK_SUMMARY.json`

Executed finite regression:

- all canonical switching gauges through `k=6` (1,098 signings);
- exact minimum orientation-code vertex-cover distributions:
  - `k=5`: minimum `8` (the theorem only requires `6`);
  - `k=6`: minimum `10` (the theorem only requires `7`);
- 80 one-defect switching-pair records at `k=5` and 150 at `k=6`, with no classification failure.

These are regression evidence only. The universal theorem is the hand proof.

## Negative controls and trust boundary

- `k=2,r=0`: classical six-vertex `H5` mechanism remains allowed.
- `k=4,r=0`: independent twelve-vertex `X_3` cube/Boolean mechanism remains allowed, with `n=12,m=32>M(12)=31`.
- No all-order second-extremal statement is claimed.
- External mathematical review and novelty assessment remain open.

The 2024 published drawing has still not been directly certified against an authoritative adjacency list; the project does not overstate that identification.

## Strategic consequence

The exact Boolean exception cannot scale through either `r=0` or the first positive layer `r=k` once `k>=5`. The next full-tight layer is

`a>=k+1`, `r>=2k`.

Residual mass alone is not enough: the eventual theorem needs a lower bound on

`delta=r-e(F)`.

The natural next structural input is the already-proved F-separation rule: if coordinate `j` is selected at label `x`, every F-neighbour of `x` agrees with `x` in coordinate `j`. Hence an F-edge can differ only in coordinates residual at **both** endpoints. The next unit should use this Hamming/residual support restriction to upper-bound `e(F)` in the `a=k+1,r=2k` layer, rather than running a broad scalar census.

Use `(AMC)` only when returning to unmatched/errorful antipodes. Do not revisit Q0, the closed mixed `{4,5}` ladder, or first-proof optimization for Erdős #742.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
