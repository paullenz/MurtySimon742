# Complete three-defect switching classification and eventual exclusion

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

This note completes the three-defect switching layer in the full tight-antipode Boolean branch. It combines:

1. the exact leaf-package reduction;
2. the isolated-pair exclusion;
3. an exact finite exceptional-core increment table for the remaining no-pair states;
4. the previously proved F-separation closures of the two lopsided low-cover normal forms.

The result is eventual, not all-order:

> **for `k>=15`, a full-tight switching class containing any state with exactly three non-leaf coordinates cannot occur above `M(n)`.**

The false all-order 2019 Dailly--Foucaud--Hansberg strengthening is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control and is outside this three-defect layer.

---

## 1. Setup

Let a chosen switched graph have exactly three non-leaf exceptional coordinates `1,2,3`. Every other coordinate is a leaf. Write

- `p_i` for the number of leaves attached directly to exceptional coordinate `i`;
- `t` for the number of isolated leaf-leaf `K_2` components;
- `S=p_1+p_2+p_3`;
- `g=|{i:p_i>0}|`;
- `x<=y<=z` for the sorted attachment counts.

Then

\[
k=3+S+2t. \tag{1.1}
\]

The actual A-code support is a vertex cover of `Omega_sigma`, and every above-`M(n)` full-tight graph satisfies

\[
\boxed{a\le2k}. \tag{1.2}
\]

Thus any switched state with

\[
\tau(\Omega_\sigma)>2k \tag{1.3}
\]

is impossible above threshold before any F-analysis.

---

## 2. Isolated leaf-pairs are already gone eventually

`THREE_DEFECT_ISOLATED_PAIR_EXCLUSION.md` proves from the exact leaf-package formula plus small outside matchings that

\[
\boxed{
t>=1,\ k>=10
\quad\Longrightarrow\quad
\tau(\Omega_\sigma)>2k.
} \tag{2.1}
\]

Hence the eventual three-defect problem may assume

\[
\boxed{t=0}. \tag{2.2}
\]

All ordinary leaves are therefore attached directly to one of the three exceptional coordinates.

---

## 3. Leaf-leaf cover for `t=0`

The exact leaf-package theorem gives

\[
B(p_1,p_2,p_3)
=2\sum_i(p_i-1)_+
 +2\sum_{i<j}\min(p_i,p_j). \tag{3.1}
\]

Equivalently,

\[
B=2S-2g+4x+2y. \tag{3.2}
\]

This is the minimum cover of the subgraph of `Omega_sigma` contributed by quotient pairs whose two coordinates are leaves.

The remaining issue is the finite exceptional core on the three non-leaf coordinates.

---

## 4. Exceptional-source code classes

Work modulo complement. For a leaf `d` with parent `p(d)`, the forced witness-code class for the orientation `d -> q` is

\[
\{p(d),q\}. \tag{4.1}
\]

For an exceptional source `i`, let `N(i)` be its neighbourhood in the chosen zero switched graph. The corresponding projective code class for `i -> q` is

\[
\boxed{N(i)\triangle\{q\}.} \tag{4.2}
\]

Equations (4.1)--(4.2) reduce all code equalities to set equality. Once the pendant-pendant packages contributing (3.1) are removed, only the graph induced on the three exceptional coordinates and whether each `p_i` is `0`, `1`, or at least `2` can affect collisions with those packages.

There are only four exceptional-core isomorphism types: empty, one edge, `P_3`, and `K_3`.

A direct case split in (4.2) gives the exact increment table below. The proof is finite: in each row, grouping equal classes gives an explicit cover of size `B+C`, while the disjoint clique/matching packages in the same grouping give the matching lower bound. The accompanying checker independently replays the table on the exact orientation-code graph across the stated finite range.

---

## 5. Exact no-pair core-increment table

For `k>=7`,

\[
\boxed{\tau(\Omega_\sigma)=B+C_H.} \tag{5.1}
\]

The increment `C_H` is as follows.

### 5.1 Empty exceptional core

Validity requires every positive `p_i` to differ from `1`.

\[
C_H=
\begin{cases}
8,&g=1,\\
14,&g>=2.
\end{cases} \tag{5.2}
\]

The `g=1` row is exactly the empty-core star state, whose full decomposition is

\[
2K_{k-3}\dot\cup2K_{1,k-3}\dot\cup2K_{2,k-2}\dot\cup2K_2
\]

and hence has `tau=2k`.

### 5.2 One exceptional-core edge

Let `u,v` be the edge endpoints and `w` the isolated exceptional coordinate. Validity requires `p_u,p_v>=1` and `p_w!=1`.

\[
C_H=
\begin{cases}
10,&p_w=0\text{ and }\min(p_u,p_v)=1,\\
14,&\text{otherwise}.
\end{cases} \tag{5.3}
\]

### 5.3 Exceptional core `P_3`

Let `c` be the degree-2 centre and `u,v` the endpoints. Validity requires `p_u,p_v>=1`.

\[
C_H=
\begin{cases}
10,&p_c=1,\\
12,&p_c=0\text{ and }\min(p_u,p_v)=1,\\
14,&\text{otherwise}.
\end{cases} \tag{5.4}
\]

The only accidental smaller-order collision occurs below the uniform `k>=7` scope and is not used.

### 5.4 Exceptional core `K_3`

\[
C_H=
\begin{cases}
7,&g=1,\\
10,&g>=2\text{ and some }p_i=1,\\
14,&g>=2\text{ and no }p_i=1.
\end{cases} \tag{5.5}
\]

The `g=1` row is exactly the triangle-star state, with `tau=2k-1`.

---

## 6. Only the two lopsided states can have `tau<=2k`

Assume first `g>=2`.

If `g=2`, then `x=0` and `y>=1`, so (3.2) gives

\[
B-2k=2y-10\ge-8. \tag{6.1}
\]

If `g=3`, then `x,y>=1`, so

\[
B-2k=4x+2y-12\ge-6. \tag{6.2}
\]

For every exceptional core with `g>=2`, the table gives

\[
C_H\ge10, \tag{6.3}
\]

except that the empty core actually gives the stronger `C_H=14`. Combining (6.1)--(6.3),

\[
\boxed{g>=2\quad\Longrightarrow\quad\tau(\Omega_\sigma)>2k.} \tag{6.4}
\]

Thus an above-threshold graph can only have `g=1`.

For `g=1`, two exceptional coordinates have zero attachments. Their exceptional-core degrees must differ from one. On three vertices this leaves only

- the empty core; or
- the triangle core.

These are exactly the two already identified low-cover normal forms:

\[
\begin{array}{c|c}
\text{state}&\tau(\Omega_\sigma)\\
\hline
\text{empty-core star}&2k\\
\text{triangle-star}&2k-1.
\end{array} \tag{6.5}
\]

There are no other no-pair three-defect states with `tau<=2k` once `k>=7`.

---

## 7. F-separation closes the two survivors

The two low-cover states have already been treated independently.

### Empty-core star

`THREE_DEFECT_EMPTY_STAR_SWITCHING_EXCLUSION.md` proves

\[
\boxed{k>=14\quad\Longrightarrow\quad m\le M(n).} \tag{7.1}
\]

### Triangle-star

`THREE_DEFECT_TRIANGLE_STAR_SWITCHING_EXCLUSION.md` proves

\[
\boxed{k>=15\quad\Longrightarrow\quad m\le M(n).} \tag{7.2}
\]

Both arguments use clean complementary clique layers, F-separation, the residual identity

\[
\delta=r-e(F),
\]

and a conservative bound on the small exceptional cover core.

---

## 8. Complete three-defect conclusion

Combining (2.1), (6.4), (6.5), (7.1), and (7.2) gives:

> **COMPLETE THREE-DEFECT SWITCHING EXCLUSION — internal candidate.**  
> In the full tight-antipode Boolean branch, if the switching class contains a state with exactly three non-leaf coordinates and
> \[
> \boxed{k>=15},
> \]
> then
> \[
> \boxed{m\le M(n).}
> \]

More explicitly:

- every three-defect state with an isolated leaf-pair has `tau>2k` from `k>=10`;
- every no-pair state with at least two nonempty pendant groups has `tau>2k` from `k>=7`;
- the only two low-cover lopsided no-pair states are the empty-core star and triangle-star;
- those are excluded by F-separation from `k>=14` and `k>=15` respectively.

Thus the **entire three-defect switching regime is eventually closed**.

---

## 9. Strategic consequence

The full-tight leaf-defect hierarchy now reads:

- residual-zero/perfect-matching boundary: finite `H5/X_3` mechanism;
- one-defect regime: eventually closed;
- two-defect regime: eventually closed from `k>=14`;
- **three-defect regime: eventually closed from `k>=15`.**

Therefore any above-`M(n)` full-tight graph with sufficiently large `k` must have **every switched state containing at least four non-leaf coordinates**.

The next structural target should not be a raw four-defect census. The useful lesson from the three-defect proof is that the leaf-only orientation-code subgraph gives a large parameter-free support bound before the exceptional core is analysed. The next move should generalise the parent-map/leaf-package formula to `d` exceptional coordinates, or at least to four defects, and ask whether it produces a bounded-width reduction analogous to Sections 3--6.

---

## 10. Negative control and trust boundary

- The order-12/32 `X_3` hostile control is the `k=4,r=0` residual-zero perfect-matching Boolean/cube mechanism. Nothing here suppresses it.
- The exact core-increment table is an internal hand case analysis from the forced-code formula, backed by finite exact replay; it still requires external mathematical review.
- External novelty assessment remains open.
- No all-order second-extremal theorem is claimed.
- No claim is made here about the complete four-defect regime.