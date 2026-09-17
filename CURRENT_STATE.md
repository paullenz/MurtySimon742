# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `ISOLATED_STAR_TWO_DEFECT_SWITCHING_EVENTUALLY_EXCLUDED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit resumed from `b0fc10c604d3133c43ceb13d345d1e08b90379f0`. The complete leaf-rich one-defect regime was already closed. Rather than attempt a broad signing census, the unit classified the first genuinely two-defect switched states by the shape forced by their `k-2` leaves. Every such state is an explicit four-parameter object `(p,q,t,epsilon)`. The apparent minimum-cover member of that family, `K_1 dotcup K_{1,k-2}`, has now been solved exactly: its orientation-code graph is `2 K_{k-2} + 4 K_{1,k-2} + one doubled K2`, so `tau(Omega_sigma)=2k-1`; F-separation then excludes it above `M(n)` for every `k>=12`.

## Preserved full-tight entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces rooted triangles at a maximum-degree root. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover `B=N(v)`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`; every `A`-vertex is a Boolean transversal; and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=r-e(F)`.

The orientation-code graph `Omega_sigma` has one code vertex per Boolean code and one edge per physical rooted B-edge, joining its two possible orientation-witness codes. The actual distinct A-code support `C` is a vertex cover.

The mandatory order-12/32 hostile control is exactly the `k=4,r=0` Boolean/cube perfect-matching mechanism and remains untouched.

## Preserved structural barriers

### Small-residual barriers

- `r=0`: only `k=2` (`H5`) and `k=4` (`X_3`) survive the full-tight switching/factorization classification.
- `r=k`: impossible for `k>=5` by the Boolean witness-code cover theorem.
- `a=k+1,r=2k`: below `M(n)` for every `k>=17` by the Hamming-support defect theorem.

### Eventual-scale density window

Because `Delta=2k`, every graph satisfies `m<=nk`. Comparing directly with `M(n)` gives

> if `m>M(n)` in the full-tight branch, then `a<=2k`.

Thus the eventual problem is controlled by code-support lower bounds near size `2k`, not by continuing the small-residual staircase indefinitely.

### Closed leaf-rich switching classes

- perfect-matching switched state: excluded above `M(n)` for even `k>=8`;
- full-star one-defect state: `tau(Omega)=2k-2`, excluded above `M(n)` for `k>=8`;
- non-star one-defect state `K_{1,k-3} dotcup K_2`: exact decomposition into two `K_{k-3}` plus three balanced double-stars, `tau(Omega)=2k-2`, excluded above `M(n)` for `k>=16`.

The complete one-defect switching regime is therefore eventually closed.

## New reduction: every two-defect state is a four-parameter graph

Assume some switched graph `L` has exactly `k-2` leaves, so it has exactly two non-leaf coordinates `a,b`. Every other vertex has degree one. Hence every leaf is either

- attached to `a`;
- attached to `b`; or
- paired with another leaf in an isolated `K_2`.

The edge `ab` may also be present.

Thus, writing

- `p` = number of leaves attached to `a`;
- `q` = number of leaves attached to `b`;
- `t` = number of leaf-leaf `K_2` components;
- `epsilon in {0,1}` = indicator of `ab`,

we have

`p+q+2t=k-2`,

with exceptional degrees `p+epsilon` and `q+epsilon`, neither equal to one.

So the complete two-defect problem is an explicit finite parameter family `(p,q,t,epsilon)`. This is now the preferred structural target; do not revert to arbitrary signing enumeration.

## New exact normal form: isolated-star two-defect state

The apparent extremal member is

`(p,q,t,epsilon)=(0,k-2,0,0)`

or symmetrically `(k-2,0,0,0)`: one exceptional coordinate is isolated and the other is the centre of `K_{1,k-2}`.

Gauge with isolated coordinate `a`, star centre `b`, and `D=[k]\{a,b}`. The zero switched state has signing edges exactly `{bd:d in D}`.

Define clique codes

`x_d={b,d}` and `bar x_d=[k]\{b,d}`.

Direct forced-witness evaluation over every quotient pair gives the complete non-isolated orientation-code graph:

> **ISOLATED-STAR TWO-DEFECT ORIENTATION-CODE NORMAL FORM — internal candidate**
>
> `Omega_sigma ~= K_{k-2} dotcup K_{k-2} dotcup 4 K_{1,k-2} dotcup K_2`,
>
> where the final `K_2` edge has physical multiplicity two.

The quotient-pair accounting is exact:

- pairs inside `D` give the two clique layers;
- pairs `{b,d}` give two complementary stars;
- pairs `{a,d}` give two more complementary stars;
- pair `{a,b}` gives the doubled `K_2`.

Full hand note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/TWO_DEFECT_ISOLATED_STAR_SWITCHING_EXCLUSION.md`.

## Exact cover number tau=2k-1

Each `K_{k-2}` contributes `k-3`, the four stars contribute four, and the doubled `K_2` contributes one. Therefore

> `tau(Omega_sigma)=2k-1`.

This is one unit stronger than the one-defect normal forms.

Combining with the above-`M(n)` density window `a<=2k`, an above-threshold graph in this class can only have

`a in {2k-1,2k}`,

or

`lambda=2k-a-1 in {0,-1}`.

For `k>=5`, any code cover of size at most `2k` must contain all four star centres. Each clique contributes at least `k-3` codes and the doubled edge contributes one endpoint.

## New F-separation closure

Choose a minimum canonical core of size `2k-1`: four star centres, `k-3` codes from each clique, and one doubled-edge endpoint.

Put

`q0=a-(2k-1)=-lambda in {0,1}`.

Mark the four star-centre labels and the chosen doubled-edge label exceptional; also mark every label in a duplicated core class and every label outside the canonical core. Then

`|E|<=5+2q0=5-2lambda`.

Every other label is a clean singleton clique code.

### Clean same-clique labels are F-independent

For distinct `d,e`, the physical rooted B-edge represented by the Omega clique edge `x_dx_e` must be selected at one endpoint. Its source coordinate is one of `d,e`, where the codes disagree. F-separation therefore forbids an F-edge. The complementary clique is identical.

### Clean cross-clique F-edges force R>=k-1 at both endpoints

For `d!=e`, `x_d` and `bar x_e` agree only at coordinates `d,e`. The switched graph at `x_d` has leaf set `D\{d}`; only `e` among the agreement coordinates can be selected. Thus an F-edge permits at most one selected coordinate and forces residual degree at least `k-1`. The complementary endpoint obeys the same bound. When `d=e`, the codes are complements and force residual degree `k`.

If `h` is the number of high-residual clean labels, then

`h(k-1)<=r`,

and the clean-clean F graph is bipartite. Therefore

> `e(F) <= floor(h^2/4) + (5-2lambda)k`,
>
> `h <= floor(r/(k-1))`.

## Eventual exclusion of the isolated-star two-defect class

For `lambda=0` (`a=2k-1`):

`r=k^2`, `h<=k+1`,

`e(F)<=floor((k+1)^2/4)+5k`,

which supplies the required defect `delta>=2k-1` for every `k>=10`.

For `lambda=-1` (`a=2k`):

`r=k(k+1)`, `h<=k+2`,

`e(F)<=floor((k+2)^2/4)+7k`,

which supplies `delta>=2k-1` for every `k>=12`.

Therefore:

> **ISOLATED-STAR TWO-DEFECT SWITCHING EXCLUSION — internal candidate.** In the full tight-antipode branch, if the switching class contains `K_1 dotcup K_{1,k-2}` and `k>=12`, then `m<=M(n)`.

This is the first genuinely two-defect switching mechanism to be structurally closed.

## Verification

Companion files:

- `project/research/post_ms/2026-09-17-stronger-pivot-v1/check_two_defect_isolated_star_switching_exclusion.py`
- `project/research/post_ms/2026-09-17-stronger-pivot-v1/TWO_DEFECT_ISOLATED_STAR_CHECK_SUMMARY.json`

Finite replay:

- exact orientation-code component structure checked for every `k=5,...,100`;
- each case gives exactly two `K_{k-2}`, four `K_{1,k-2}`, and one doubled `K_2`;
- exact cover formula `tau=2k-1` reproduced throughout;
- defect arithmetic checked through `k=5000`, reproducing closure thresholds `10` for `lambda=0` and `12` for `lambda=-1`.

These are regression checks only. The universal statements are the hand proofs.

## Broader two-defect obstruction and next target

Exploratory exact calculations on the four-parameter two-defect family consistently indicate the stronger statement

`tau(Omega_sigma)>=2k-1`,

with equality only for the isolated-star state and its symmetric copy. This is **not yet proved and is not promoted**.

The highest-value next bounded theorem is now sharply defined:

> prove `tau(Omega_sigma)>=2k-1` for every two-defect parameter tuple `(p,q,t,epsilon)`, ideally with equality classification.

Do this by quotient-pair/component accounting in the four-parameter normal form, not by broad signing enumeration. If the universal bound fails, preserve the first explicit parameter obstruction and classify it. If it succeeds, the entire two-defect switching regime is forced into `a>=2k-1`, reducing it to the same two near-balanced `lambda` layers already controlled by F-separation.

Use `(AMC)` only when returning to near-full/unmatched/errorful antipodes. Do not revisit Q0, the closed mixed `{4,5}` selected-excess ladder, or first-proof optimization for Erdős #742.

## Mandatory negative control and trust boundary

- `k=2,r=0`: classical `H5` remains allowed.
- `k=4,r=0`: independent twelve-vertex `X_3` Boolean/cube mechanism remains allowed with `n=12,m=32>M(12)=31`.
- The new theorem begins above the hostile-control range and does not suppress it.
- Direct primary-source adjacency certification of the published 2024 Figure-1 graph against the project's `X_3` reconstruction remains open; no stronger identification is claimed.
- External mathematical review and novelty assessment remain open.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
