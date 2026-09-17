# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `COMPLETE_TWO_DEFECT_SWITCHING_EVENTUALLY_CLOSED_AND_TRIANGLE_STAR_THREE_DEFECT_CLOSED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This enlarged unit resumed from `7c3a83c393f3911642fa37c34ae42a0351bfce2d`. It completed the entire four-parameter two-defect switching problem, rather than stopping at the isolated-star subcase, and then carried the same structural method one layer further to the first low-cover three-defect normal form.

## Preserved full-tight entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces rooted triangles at a maximum-degree root. For `n>=14`, the all-private edge-witness theorem forces a disjoint-support antipode. Tight antipodes form a matching. If they cover `B=N(v)`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`; every A-vertex is a Boolean transversal; and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=r-e(F)`.

The orientation-code graph `Omega_sigma` has one Boolean-code vertex per possible witness code and one edge per physical rooted B-edge. The actual set of distinct A-codes is a vertex cover of `Omega_sigma`.

The above-threshold density window remains

> if `m>M(n)` in the full-tight branch, then `a<=2k`.

The mandatory order-12/32 hostile control is exactly the `k=4,r=0` Boolean/cube perfect-matching mechanism and remains untouched.

## Preserved barriers before this unit

- `r=0`: only `k=2` (`H5`) and `k=4` (`X_3`) survive the full-tight switching/factorization classification.
- `r=k`: impossible for `k>=5` by the Boolean witness-code cover theorem.
- `a=k+1,r=2k`: below `M(n)` for every `k>=17` by the Hamming-support defect theorem.
- perfect-matching switched state: excluded above `M(n)` for even `k>=8`.
- full-star one-defect state: exact `tau(Omega)=2k-2`, excluded above `M(n)` for `k>=8`.
- non-star one-defect state `K_{1,k-3} dotcup K_2`: exact `tau(Omega)=2k-2`, excluded above `M(n)` for `k>=16`.

Thus the complete one-defect regime was already eventually closed.

---

# New result I: complete two-defect switching classification

A switched graph with exactly `k-2` leaves has exactly two non-leaf coordinates `a,b`. Every leaf is attached to `a`, attached to `b`, or paired with another leaf in an isolated `K_2`; the edge `ab` may be present.

Write

- `p` = leaves attached to `a`;
- `q` = leaves attached to `b`;
- `t` = isolated leaf-leaf pairs;
- `epsilon in {0,1}` = indicator of `ab`.

Then

`p+q+2t=k-2`,

and `p+epsilon`, `q+epsilon` are both different from one.

Full hand note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/TWO_DEFECT_COMPLETE_SWITCHING_CLASSIFICATION.md`.

## Exact cover formulas

For `t=0, epsilon=0`:

- isolated-star (`min(p,q)=0`): `tau=2k-1`;
- otherwise `p,q>=2` and
  `tau=2k-3+2 min(p,q)>=2k+1`.

For `t=0, epsilon=1`:

`tau=2k-2+2 min(p,q)`.

Thus only `min(p,q)=1` can have `tau<=2k`, and then `tau=2k`.

For `t>=1` and `p+q>0`:

`tau = 2(p-1)_+ + 2(q-1)_+ + 2 min(p,q) + 2t^2+6t+6`.

For the special `p=q=0, epsilon=0` family:

`tau=2t^2+2t+3`.

Every valid `t>=1` tuple satisfies `tau>2k`.

These formulas come from direct quotient-pair/component accounting using the forced witness-code formula; they are hand mathematics, not an extrapolation from the finite scan.

## Density consequence

Since an above-`M(n)` full-tight graph has `a<=2k`, every two-defect parameter tuple is immediately impossible except two lopsided normal forms:

1. **isolated-star:** `(0,k-2,0,0)` or symmetric, `tau=2k-1`;
2. **adjacent-lopsided:** `(1,k-3,0,1)` or symmetric, `tau=2k`.

The isolated-star form was already closed for `k>=12`.

## Adjacent-lopsided closure

For the new survivor, direct orientation-code accounting gives

`Omega ~= 2 K_{k-3} + 2 K_{2,k-2} + 2 K_{1,k-3} + 2 K_2`,

so `tau=2k`. Therefore above threshold one must have exactly

`a=2k`, `lambda=-1`, `r=k(k+1)`.

The two clique layers again have clean Boolean codes

`x_d={b,d}`, `bar x_d=[k]\{b,d}`.

Same-layer clean labels are F-independent. A clean cross-layer F-edge forces residual degree at least `k-1` at both endpoints. The eight non-clique minimum-cover labels are treated conservatively as exceptional. Hence, if `h` is the number of high-residual clean labels,

`h(k-1)<=r`,

and

`e(F)<=floor(h^2/4)+8k`.

Since `h<=k+2`, this supplies the required defect `delta>=2k-1` for every `k>=14`.

Therefore:

> **COMPLETE TWO-DEFECT SWITCHING EXCLUSION — internal candidate.** If a full-tight switching class contains a state with exactly two non-leaf coordinates and `k>=14`, then `m<=M(n)`.

The complete two-defect regime is now eventually closed.

## Two-defect verification

Files:

- `check_two_defect_complete_switching_classification.py`
- `TWO_DEFECT_COMPLETE_SWITCHING_CHECK_SUMMARY.json`

Finite replay:

- exact graph/Tau replay for all 104 valid parameter tuples at `k=5,...,10`;
- formula-level density scan of 159,344 tuples through `k=100`;
- only the isolated-star and adjacent-lopsided normal forms ever satisfy `tau<=2k`;
- adjacent-lopsided defect arithmetic replayed through `k=5000`, reproducing threshold `k=14`.

Finite checks are evidence only; the universal formulas and F-separation arguments are the mathematical basis.

---

# New result II: first three-defect low-cover state

A switched graph with exactly `k-3` leaves has three exceptional coordinates. Every leaf is attached to one exceptional coordinate or paired with another leaf, and the induced graph on the three exceptional coordinates is arbitrary. This is again a finite-parameter structural family.

Exact exploratory scans at `k=6,...,9` identify a lowest-cover state (up to exceptional-coordinate relabelling):

- the three exceptional coordinates span `K_3`;
- all `k-3` leaves are attached to one triangle vertex.

Call this the **triangle-star three-defect state**.

Full hand note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/THREE_DEFECT_TRIANGLE_STAR_SWITCHING_EXCLUSION.md`.

## Exact orientation-code normal form

Direct forced-code evaluation gives

`Omega ~= 2 K_{k-2} + 4 K_{1,k-2} + one doubled K_2`,

hence

`tau(Omega)=2k-1`.

This is the same simple component signature as the isolated-star two-defect state, although the clique codes are slightly different.

Therefore above threshold

`a in {2k-1,2k}`,

`lambda in {0,-1}`.

## Triangle-star F-separation closure

One clique layer consists of

`emptyset` and `x_d={c,d}` for `d in D`,

and the other is its complement. Mark the at-most-two selected special clique codes, the four star centres, and the doubled-edge endpoint exceptional. After accounting for a possible one-label surplus,

`|E|<=7-2lambda`.

Clean same-layer labels are F-independent. For distinct `d,e`, the clean cross-layer codes `x_d` and `bar x_e` agree only at `d,e`, while the leaf set at `x_d` is `{c} union (D\{d})`; only `e` can be selected. Thus every clean cross-layer F-edge forces residual degree at least `k-1` at both endpoints.

Consequently

`e(F)<=floor(h^2/4)+(7-2lambda)k`,

`h<=floor(r/(k-1))`.

This closes

- `lambda=0` from `k>=13`;
- `lambda=-1` from `k>=15`.

Therefore:

> **TRIANGLE-STAR THREE-DEFECT SWITCHING EXCLUSION — internal candidate.** If a full-tight switching class contains the triangle-star state and `k>=15`, then `m<=M(n)`.

## Three-defect verification

Files:

- `check_three_defect_triangle_star_switching_exclusion.py`
- `THREE_DEFECT_TRIANGLE_STAR_CHECK_SUMMARY.json`

Finite replay:

- exact orientation-code component decomposition checked for every `k=5,...,100`;
- exact `tau=2k-1` reproduced throughout;
- defect arithmetic replayed through `k=5000`, reproducing closure thresholds `13` and `15`.

---

## Strategic consequence and next move

The full-tight branch now has a clean leaf-defect hierarchy:

- perfect-matching / zero-defect switching mechanism: finite `H5/X_3` boundary;
- one-defect regime: eventually closed;
- **entire two-defect regime: eventually closed from `k>=14`;**
- first identified low-cover three-defect normal form: eventually closed from `k>=15`.

The next highest-value theorem is the **complete three-defect orientation-code cover classification**. Parameterise by attachment counts `(p1,p2,p3)`, the number `t` of isolated leaf-pairs, and the 3-vertex exceptional graph. Exact finite exploration suggests

`tau(Omega_sigma)>=2k-1`,

with equality only for the triangle-star state and relabellings. This remains unproved and must not be promoted.

If that cover theorem succeeds, every other three-defect state either becomes impossible directly from `a<=2k` or is pushed into a very small list of near-balanced normal forms amenable to the same F-separation closure.

Do not revert to arbitrary signing enumeration, Q0, the closed mixed `{4,5}` ladder, or first-proof optimization for Erdős #742. Use finite scans only to identify extremal parameter normal forms and audit hand component formulas.

## Mandatory negative control and trust boundary

- `k=2,r=0`: classical `H5` remains allowed.
- `k=4,r=0`: independent twelve-vertex `X_3` Boolean/cube mechanism remains allowed with `n=12,m=32>M(12)=31`.
- Nothing in the two-/three-defect theorems suppresses the `k=4` hostile control.
- Direct primary-source adjacency certification of the published 2024 Figure-1 graph against the project's `X_3` reconstruction remains open; no stronger identification is claimed.
- External mathematical review and novelty assessment remain open.
- No all-order second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.
<!-- CURRENT-STATUS:END -->
