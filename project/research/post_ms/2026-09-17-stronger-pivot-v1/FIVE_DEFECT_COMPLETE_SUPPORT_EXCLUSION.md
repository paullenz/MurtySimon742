# Five-defect switching states are support-impossible from k >= 8

18 September 2026. Research directed by Paul Lenz; derivation and finite core audit by ChatGPT/Geeps.

**Status: internal structural/certificate theorem; not promoted. External mathematical review and compression of the finite five-vertex core table remain open.**

The active target remains the sufficiently-large/eventual second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 strengthening is not assumed, and the order-12/32 `X_3` obstruction remains the mandatory `k=4,r=0` negative control.

This note applies the general leaf-package theorem and residual ray monotonicity to the next switching layer after the complete four-defect closure. Unexpectedly, five defects are **easier**: no F-separation cleanup is required. For `k>=8`, support alone forces more than `2k` distinct witness codes.

---

## 1. Five-defect parameterisation

Let a switched state have exactly five non-leaf exceptional coordinates. Write the sorted pendant-group sizes

\[
a\le b\le c\le d\le z,
\]

and let `t` be the number of isolated leaf-leaf `K_2` components. Then

\[
k=5+a+b+c+d+z+2t.
\]

The general leaf-package theorem gives, with `g` nonempty pendant groups,

\[
B_5=2S-2g+2(4a+3b+2c+d)
\]

for `t=0`, and

\[
L_5=B_5+4tg+2t(t-1)+1
\]

for `t>=1`.

An above-`M(n)` full-tight graph requires `tau(Omega)<=a_A<=2k`, so the leaf package alone leaves only finitely many pendant rays.

---

## 2. Finite-width list

### No isolated leaf-pairs: t = 0

The necessary inequality is

\[
4a+3b+2c+d\le5+g.
\]

Hence the only unbounded rays are:

- `g=1`: `(0,0,0,0,z)`;
- `g=2`: `(0,0,0,y,z)`, `1<=y<=7`;
- `g=3`: `(0,0,x,y,z)` with
  \[
  (x,y)\in\{(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,2),(2,3),(2,4)\};
  \]
- `g=4`: `(0,w,x,y,z)` with
  \[
  (w,x,y)\in\{(1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,2,2)\};
  \]
- `g=5`: only `(1,1,1,1,z)`.

### One isolated leaf-pair: t = 1

The necessary inequality becomes

\[
4a+3b+2c+d+g\le6.
\]

The only rays are:

- `g=1`: `(0,0,0,0,z)`;
- `g=2`: `(0,0,0,y,z)`, `1<=y<=4`;
- `g=3`: only `(0,0,1,1,z)`.

### Two isolated leaf-pairs: t = 2

Only the lopsided `g=1` ray `(0,0,0,0,z)` survives the leaf-package inequality.

### No pendant groups

When `g=0`, the condition is

\[
2t^2-6t-9\le0,
\]

so only `t<=4` can survive the leaf package. These are fixed finite orders. For `k>=8`, only `t=2,3,4` need checking.

For `t>=3` with `g>=1`, or `t>=5` with `g=0`, the leaf package already exceeds `2k`.

---

## 3. Residual ray monotonicity makes every ray finite

Use the vertex-disjoint decomposition from `LEAF_PACKAGE_RESIDUAL_RAY_MONOTONICITY.md`:

\[
\tau(\Omega)\ge L_5+\tau(R),
\]

where `R` is the orientation-code graph induced outside the leaf-package code vertices.

Once the largest pendant group has size at least two, adding another leaf embeds the old residual graph in the new residual graph, so

\[
\tau(R_{z+1})\ge\tau(R_z).
\]

At the same time `L_5` and `2k` both increase by two. Therefore a strict support excess at one base point persists along the entire ray.

The infinite five-defect problem is consequently reduced to finitely many five-vertex exceptional cores at one base point per bounded attachment pattern.

---

## 4. Every nonlopsided ray has positive additive support excess

The exact forced-code construction was evaluated at the base point of each finite-width ray, over all valid labelled graphs on the five exceptional coordinates. The residual graph `R` was then solved exactly.

For **every no-pair nonlopsided ray**, the minimum value of

\[
L_5+\tau(R)-2k
\]

is already positive at the base point. The smallest such margin is `4`, on `(0,0,0,1,2)`; all other nonlopsided base patterns have larger margins.

For every `t=1` or `t=2` pendant ray left by Section 2, the same additive bound is positive. The smallest margin is `5`, on the `t=1,g=1` base `(0,0,0,0,2)`.

For the fixed `g=0` states with `t=2,3,4`, the additive margins are respectively

\[
3,\ 11,\ 23.
\]

Thus all these states are support-impossible, and residual ray monotonicity extends the base certificates along every unbounded ray.

The only place where the vertex-disjoint additive split is not by itself strong enough is the no-pair lopsided ray `(0,0,0,0,z)`.

---

## 5. The lopsided no-pair ray

Assume `z>=3`, so `k=5+z`.

At the base `z=3`, the residual additive bound fails only for three rooted exceptional-core isomorphism classes. Root the five-vertex core at the unique exceptional coordinate carrying the pendant leaves. Up to permutation of the other four coordinates, the three dangerous cores are represented by masks

`861`, `894`, `895`

in lexicographic pair-bit order

`01,02,03,04,12,13,14,23,24,34`,

with root `4`.

They have transparent graph descriptions:

1. `861`: root `4` is universal and the other four vertices induce `P_4`;
2. `894`: root `4` is universal and the other four vertices induce `C_4`;
3. `895`: root `4` is universal and the other four vertices induce `K_4-e`.

Every other valid rooted core already has

\[
B_5+\tau(R)>2k
\]

at `z=3`, and is therefore closed along the whole ray by residual monotonicity.

The three exceptional cores admit direct component decompositions of the **full** orientation-code graph for every `z>=3`.

### 5.1 Universal root + P4

The components occur in complementary pairs and have cover contributions

- two pairs of fixed-cover tree components, contribution `2+2` per complementary pair family;
- two cliques `K_{z+1}`, contribution `2z`;
- two `P_3` components, contribution `2`;
- two `K_2` components, contribution `2`.

Thus

\[
\boxed{\tau(\Omega)=2z+12=2k+2.}
\]

### 5.2 Universal root + C4

The orientation graph decomposes into

- two large components of cover number `4` each;
- two cliques `K_{z+1}`, contribution `2z`;
- four `K_2` components, contribution `4`.

Hence again

\[
\boxed{\tau(\Omega)=2z+12=2k+2.}
\]

### 5.3 Universal root + K4-e

The decomposition is especially simple:

- four stars `K_{1,z+3}`, total cover `4`;
- two `K_{2,z+1}`, total cover `4`;
- two cliques `K_{z+1}`, total cover `2z`;
- three two-vertex components (one physical edge may be doubled), total cover `3`.

Therefore

\[
\boxed{\tau(\Omega)=2z+11=2k+1.}
\]

So even the unique worst rooted core lies one code above the full-tight density window.

At the finite boundary `z=2`, there are five labelled switching cores with `tau=2k`; this is why the theorem begins at `k=8` rather than `k=7`. No D2C realization is claimed for those switching states.

---

## 6. Complete five-defect support theorem

Combining Sections 2--5 gives:

> **FIVE-DEFECT SUPPORT EXCLUSION — internal candidate.** If a full tight-antipode switching class contains a state with exactly five non-leaf coordinates and
>
> \[
> \boxed{k\ge8},
> \]
>
> then
>
> \[
> \boxed{\tau(\Omega)>2k.}
> \]
>
> Since an above-`M(n)` full-tight graph requires `a<=2k` and its distinct A-code support is a vertex cover of `Omega`, such a state cannot occur in an above-threshold graph.

Thus five defects are excluded by witness-code support alone; the residual/F-separation machinery is not needed.

---

## 7. Significance

The complete fixed-defect hierarchy now reads:

- one defect: eventually closed;
- two defects: eventually closed from `k>=14`;
- three defects: eventually closed from `k>=15`;
- four defects: internally closed from `k>=19`;
- **five defects: support-impossible already from `k>=8`.**

The qualitative change at five defects is important. It suggests that the difficult switching regime may be confined to very small defect count: once the exceptional set is large enough, the exceptional-core witness demand itself overwhelms the `2k` code-support budget.

The next high-value question is therefore not to classify six defects one case at a time, but to seek a defect-count lower bound on the residual exceptional-core contribution. The lopsided five-defect worst case has residual support exactly large enough to give `tau=2k+1`, and preliminary six-defect data suggest an even larger excess. A bound growing with the defect count could collapse **all `d>=5` layers at once**.

---

## 8. Verification and trust boundary

The companion checker reconstructs the full orientation-code graph from the forced-code formula, verifies the finite-width ray list, solves the residual base graphs exactly over all valid labelled five-vertex exceptional cores, canonicalises the only lopsided dangerous cores, and checks the three explicit component formulas across multiple `z` values.

This finite core calculation is used only after the hand leaf-package and ray-monotonicity reductions have removed every unbounded parameter. It remains an internal certificate rather than an externally reviewed hand classification of all rooted five-vertex cores.

The `k=4`, order-12/32 `X_3` residual-zero negative control is outside the five-defect theorem and is untouched. No all-order second-extremal theorem is claimed.
