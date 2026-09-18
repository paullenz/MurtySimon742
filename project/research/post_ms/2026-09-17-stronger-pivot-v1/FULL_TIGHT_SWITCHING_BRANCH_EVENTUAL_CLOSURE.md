# Full tight-antipode Boolean switching branch: eventual internal closure

18 September 2026. Research directed by Paul Lenz; synthesis by ChatGPT/Geeps.

**Status: internal theorem candidate. The unbounded structural reductions are hand mathematics; several small fixed-core steps (including the new d=7,8 boundary checks and older d=4--6 certificates) remain finite internal certificates pending external review.**

This note records the first point at which the entire **full tight-antipode Boolean switching branch** is internally closed above

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1
\]

for a uniform sufficiently-large threshold. It is not yet a theorem for all D2C graphs because unmatched/near-full/errorful antipodes remain outside this clean branch.

The published `12/32` graph remains the certified `k=4,r=0` `X_3` hostile control and is unaffected.

## 1. Preserved full-tight setup

If tight antipodes cover

\[
B=N(v)=P_1\dot\cup\cdots\dot\cup P_k,
\qquad |P_i|=2,
\]

then the preserved Boolean normal form gives

\[
b=2k,
\quad Q=k(k-1),
\quad r=k(a-k+1),
\quad \delta=r-e(F),
\]

and the actual distinct A-codes form a vertex cover of the orientation-code graph `Omega`. Any above-`M(n)` graph in this branch satisfies

\[
a\le2k.
\]

For a code `c`, let `phi(c)` be the number of non-leaf coordinates in the switched graph `L_c`, and put

\[
d_*:=\min_c\phi(c).
\]

## 2. Previously closed minimum-defect values

The preserved hierarchy before the present unit is:

- `d_*=0`: the residual-zero/perfect-matching mechanism leaves only finite `H5/X_3` boundaries; above threshold the perfect-matching state is excluded;
- `d_*=1`: complete one-defect regime eventually closed;
- `d_*=2`: complete regime closed from `k>=14`;
- `d_*=3`: complete regime closed from `k>=15`;
- `d_*=4`: complete regime internally closed from `k>=19`;
- `d_*=5`: support-impossible from `k>=8`;
- `d_*=6`: support-impossible from `k>=9`.

Thus `k>=19` reduces the remaining branch to `d_*>=7`.

The elementary orientation-degree bound gives

\[
\tau(\Omega)\ge
\left\lceil\frac{k(k-1)}{k-d_*}\right\rceil,
\]

so if `2d_*>k+1` there is already strict support excess. The only unresolved range therefore has

\[
k-d_*\ge d_*-1.
\]

## 3. New general collapse for d_* >= 7

The companion note

`MINIMUM_DEFECT_TWIN_PACKAGE_COLLAPSE.md`

introduces a vertex-disjoint twin package in a minimum-defect switched state.

If the `k-d` leaves consist of ordinary pendant groups of sizes `p_j` and `t` isolated leaf-pairs, partition the exceptional coordinates carrying no pendant group by equal open neighbourhood. For a twin class of size `m`, the orientation graph contains, disjointly from the old leaf package:

- `2K_m` from pairs inside the twin class;
- `2K_{m,p_j}` against each ordinary pendant group;
- `2K_{m,1}` against each isolated leaf, giving `4t` cover contribution per class.

This yields

\[
\tau(\Omega)\ge
L_d+2\sum_T\left[(|T|-1)+\sum_j\min(|T|,p_j)+2t\right].
\]

When the minimum-defect leaf count satisfies `k-d>=d-1`, the inequality closes **every** geometry with:

- at least two ordinary pendant groups;
- one ordinary pendant group plus at least one isolated pair;
- no ordinary pendant group.

Therefore any surviving minimum-defect state with `d>=7` would have to be **pure lopsided**:

- no isolated leaf-pairs;
- all `z=k-d` leaves attached to one exceptional root;
- `z>=d-1`.

This is the main structural compression of the present unit.

## 4. Pure lopsided d >= 10 is closed uniformly

Let `Q` be the `q=d-1` exceptional coordinates other than the pendant root. The leaf-leaf package plus the exact `Q`-against-leaf twin-star package costs

\[
2(z-1)+2q=2k-4.
\]

A `Q-Q` directed endpoint can fall into one of those star-centre codes only when its source coordinate is root-adjacent and has exactly two neighbours in `Q`. If `b` is the number of `Q` pairs with at least one such absorbed endpoint, then

\[
b\le2q-4.
\]

Consequently at least

\[
\frac{q^2-5q+8}{2}
\]

`Q` pairs survive. They give twice as many full orientation-code edges, and the residual maximum degree is at most `q`, so

\[
\tau(R_Q)\ge
\left\lceil q-5+\frac8q\right\rceil.
\]

For `q>=9`, i.e. `d>=10`, this is at least five. It supplies the five vertices needed beyond `2k-4` and gives strict support excess.

Hence every pure lopsided minimum-defect state with

\[
d_*\ge10
\]

is impossible above `M(n)`.

## 5. d_*=9 is also hand-closed

For `d=9`, `q=8`. Retain the full twin-class core cliques. If `h` is the number of distinct open-neighbourhood classes in `Q`, the lopsided package margin relative to `2k` is

\[
2(q-h-2).
\]

Thus `h<=5` is immediately strict.

- `h=6`: the package reaches `2k`; the general good-pair count leaves a residual edge after removing the at-most-three within-class quotient edges.
- `h=7`: the package is two short; at least 15 residual quotient edges remain after removing the unique twin-pair edge. Quotient maximum degree eight gives cover at least two, hence at least four across the complementary halves.
- `h=8`: equality in the worst absorbed-pair count would force six root-adjacent degree-two `Q` vertices to have the same two `Q` neighbours, contradicting the assumption that all eight neighbourhoods are distinct. Thus at least 17 quotient edges survive; degree at most eight gives quotient cover at least three and full residual cover at least six.

Therefore `d_*=9` is excluded without a finite core scan.

## 6. d_*=8 boundary certificate

Now `q=7`.

Again the package margin is `2(q-h-2)`.

- `h<=4`: strict already.
- `h=5`: package equality; the general absorbed-pair bound leaves at least eight quotient edges after deleting all within-class edges, so a residual edge exists.
- `h=6`: the package is two short; at least ten quotient residual edges remain after deleting the unique twin-pair edge. Maximum degree seven gives quotient cover at least two, hence full residual cover at least four.
- `h=7`: this is the sole genuinely finite boundary. The seven zero-parent exceptional coordinates have pairwise distinct neighbourhoods.

The companion checker enumerates every rooted core of this last type by taking all `1044` NetworkX graph-atlas graphs on seven vertices and all `2^7` root-neighbour masks. After validity and all-distinct filtering, exactly

\[
66513
\]

rooted cases remain. In every case the quotient residual `Q-Q` graph has vertex-cover number at least three; equivalently the two complementary halves contribute at least six residual cover vertices. There are **zero** cover-`<=2` cases.

Thus `d_*=8` is internally closed.

## 7. d_*=7 boundary certificate

For seven defects the pure lopsided ray is checked one layer lower, at `z=3`, so that coordinatewise residual ray monotonicity propagates the result to every larger pendant group.

The NetworkX graph atlas contains `1044` unlabelled graphs on seven vertices. Rooting them in every possible way and imposing the exceptional-coordinate validity condition leaves

\[
4376
\]

rooted cores.

At `z=3` the exact leaf package has cover four. A maximum-matching certificate already gives the required residual cover in all but 15 rooted cases. Those 15 are solved exactly; their minimum residual vertex-cover number is

\[
19.
\]

Thus even the worst rooted core satisfies

\[
4+19-2(7+3)=3>0.
\]

Coordinatewise residual monotonicity preserves this strict margin for every `z>3`. In particular it covers the minimum-defect range `z>=6`.

Thus `d_*=7` is internally closed.

Files:

- `check_minimum_defect_d7_d8_lopsided_boundary.py`;
- `MINIMUM_DEFECT_D7_D8_LOPSIDED_BOUNDARY_CHECK_SUMMARY.json`.

## 8. Full-tight eventual closure

Combining Sections 2--7 gives:

> **FULL-TIGHT BOOLEAN SWITCHING EXCLUSION — internal candidate.** In the full tight-antipode Boolean branch, if
>
> \[
> \boxed{k\ge19},
> \]
>
> then an above-`M(n)` counterexample cannot occur.

The proof is exhaustive by the minimum switching defect `d_*`:

- `0<=d_*<=6`: preserved fixed-defect theorems;
- `d_*=7,8`: the two finite boundary certificates above, after the general twin-package reduction;
- `d_*=9`: hand residual-count closure;
- `d_*>=10`: hand uniform twin/lopsided closure or, when `2d_*>k+1`, the elementary orientation-degree bound.

This is a materially stronger milestone than another fixed-defect exclusion: the **whole clean Boolean switching problem is now internally exhausted for sufficiently large `k`**.

## 9. What this does and does not prove

This does **not** yet prove the eventual second-extremal theorem for all D2C graphs. The remaining work has moved outside the full-tight branch: near-full tight support, unmatched antipodes, and errorful/private-witness configurations must now be controlled by the preserved stability/AMC machinery.

It also does not restore the false 2019 all-order conjecture. The published order-12/32 `X_3` graph is explicitly outside the eventual `k>=19` statement and remains mandatory regression data.

Several finite core certificates in the chain remain internal rather than journal-style hand classifications. The appropriate next step is therefore twofold:

1. audit/compress the new twin-package and `d=7,8` boundary certificates;
2. **move the main mathematical attack to the near-full/unmatched/errorful antipode stability problem**, rather than continuing the now-closed fixed-defect switching ladder.
