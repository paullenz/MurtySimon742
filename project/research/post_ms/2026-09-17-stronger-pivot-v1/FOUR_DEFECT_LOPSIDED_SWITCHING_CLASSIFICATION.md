# Lopsided no-pair four-defect switching classification

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical review open.**

This note takes the first infinite ray left by `GENERAL_LEAF_PACKAGE_REDUCTION.md`: a switched state with exactly four non-leaf coordinates, no isolated leaf-pairs, and all ordinary leaves attached to a single exceptional coordinate.  The rooted four-vertex exceptional core has only eight valid isomorphism types.  Exact projective-code grouping shows that only two of them have orientation-code cover number at most `2k`; both can then be excluded above `M(n)` for sufficiently large `k` by the existing F-separation mechanism.

The order-12/32 `X_3` obstruction remains a separate `k=4` residual-zero perfect-matching mechanism and is unaffected.

---

## 1. State and notation

Let the four exceptional coordinates be

\[
r,a,b,c,
\]

and let

\[
D=\{d_1,\ldots,d_{k-4}\}
\]

be all remaining coordinates.  Every `d in D` is a leaf adjacent to the root exceptional coordinate `r`; there are no isolated leaf-pairs.  Thus the attachment vector is

\[
(0,0,0,k-4).
\]

Let `H` be the graph induced by `{r,a,b,c}` in the chosen switched state.  For `k>=8`, coordinate `r` is automatically non-leaf.  The other three exceptional coordinates have no attached leaves, so validity requires

\[
d_H(a),d_H(b),d_H(c)\ne1. \tag{1.1}
\]

Up to permutations of `a,b,c`, there are exactly eight rooted core types satisfying (1.1).

For any source coordinate `i` and target `q`, work modulo complement and write the forced projective code class as

\[
\boxed{N(i)\triangle\{q\}.} \tag{1.2}
\]

This makes the rooted-core calculation finite.

---

## 2. Exact rooted-core cover table

A direct grouping of equal code classes in (1.2), followed by componentwise minimum-cover calculation, gives the following table for every `k>=8`.

| rooted exceptional core `H` | description | `tau(Omega_sigma)` |
|---|---|---:|
| empty | four isolated core vertices | `2k+4` |
| `K_3` through `r` + isolated | triangle containing `r` | `2k+3` |
| `C_4` | `K_{2,2}`, with `r` on one side | `2k+4` |
| `K_4-e`, `e` not incident with `r` | missing edge between two non-root exceptions | `2k` |
| `K_3` away from `r` + isolated `r` | non-root triangle | `2k+4` |
| paw | `r` is the pendant vertex of a triangle | `2k+1` |
| `K_4-e`, `e` incident with `r` | missing root-to-exception edge | `2k+4` |
| `K_4` | complete exceptional core | `2k-2` |

Thus the density window `a<=2k` immediately eliminates six of the eight rooted cores.

The two survivors have especially simple exact orientation-code decompositions.

---

## 3. Survivor A: `K_4-e` with the missing edge away from `r`

After relabelling, take

\[
E(H)=\{ra,rb,rc,ab,ac\},
\]

so the missing exceptional edge is `bc`.

Direct code grouping gives

\[
\boxed{
\Omega_\sigma\cong
2K_{k-3}
\dot\cup2K_{1,k-3}
\dot\cup2K_2
\dot\cup2K_{2,k-2}.
} \tag{3.1}
\]

Hence

\[
\boxed{\tau(\Omega_\sigma)=2k.} \tag{3.2}
\]

In an above-`M(n)` full-tight graph the A-code support has size at most `a<=2k`, so (3.2) forces

\[
\boxed{a=2k,\qquad\lambda=-1,\qquad r=k(k+1).} \tag{3.3}
\]

Since the cover number already equals the number of A-labels, all A-codes are distinct.

---

## 4. Survivor B: complete exceptional core

Now take

\[
H=K_4.
\]

The orientation-code graph decomposes as

\[
\boxed{
\Omega_\sigma\cong
2K_{k-3}\dot\cup3T_{k-3},
} \tag{4.1}
\]

where `T_m` is the balanced double-star consisting of two adjacent centres, each with `m` private leaves; the central physical edge has multiplicity two, which does not alter its cover number.  Thus

\[
\tau(T_m)=2
\]

and

\[
\boxed{\tau(\Omega_\sigma)=2(k-4)+6=2k-2.} \tag{4.2}
\]

Therefore any above-threshold realization has

\[
a\in\{2k-2,2k-1,2k\},
\]

or equivalently

\[
\boxed{\lambda\in\{1,0,-1\}.} \tag{4.3}
\]

---

## 5. Common clique-code geometry

In both survivors, the two large clique components have the same code classes.  One layer is

\[
\mathcal C^+
 =\{\varnothing\}\cup\{x_d=\{r,d\}:d\in D\}, \tag{5.1}
\]

and the other is the complementary layer

\[
\mathcal C^-=\{\overline x:x\in\mathcal C^+\}. \tag{5.2}
\]

Each layer is a `K_{k-3}` in `Omega_sigma`, so every code cover contains at least `k-4` distinct classes from each layer.

Call the indexed classes `x_d,bar x_d` **clean classes**; the two base classes `emptyset,[k]` are not called clean.

For `d!=e`, the switched graph at `x_d` has leaf coordinates

\[
\{r\}\cup(D\setminus\{d\}), \tag{5.3}
\]

and the same is true, up to complementation, at `bar x_d`.

Two clean classes in the same layer are joined by the physical orientation-code edge over their leaf pair.  If each class occurs only once among the A-labels, F-separation therefore forbids an F-edge between those two labels: whichever endpoint represents that physical B-edge is selected at a coordinate where the two codes disagree.

For a cross-layer pair `x_d,bar x_e`:

- if `d!=e`, their codes agree only at coordinates `d,e`;
- among those two, only `e` is a leaf coordinate at `x_d`, and only `d` is a leaf coordinate at `bar x_e`.

Hence an F-edge between unique clean representatives forces

\[
R_{x_d}\ge k-1,
\qquad
R_{\bar x_e}\ge k-1. \tag{5.4}
\]

The case `d=e` is stronger: the two codes are complementary and any F-edge forces all coordinates residual.  Thus (5.4) remains valid uniformly.

---

## 6. Safe treatment of multiplicities

The previous paragraph is stated only for code classes represented by a **unique** A-label.  This avoids silently assuming that a selected incidence attached to a code class must use a particular duplicate label.

### Complete-core survivor

The global cover number is `2k-2`.  Let `D_A` be the number of distinct A-codes.  Since

\[
D_A\ge2k-2,
\]

the total multiplicity surplus is at most

\[
a-D_A\le1-\lambda. \tag{6.1}
\]

The two clique layers force at least `2k-10` distinct indexed clean classes: each `K_{k-3}` needs `k-4` code classes, and at most one of those can be its unindexed base class.  At most `1-lambda` of those clean classes can be duplicated.  Therefore at least

\[
2k-11+\lambda
\]

A-vertices are unique clean representatives.

All remaining vertices are declared exceptional, giving the safe bound

\[
\boxed{|E_A|\le10-2\lambda.} \tag{6.2}
\]

### `K_4-e` survivor

Here `tau=2k` and `a=2k`, so every A-code is distinct.  The two clique layers still provide at least `2k-10` indexed clean labels, hence

\[
\boxed{|E_A|\le10.} \tag{6.3}
\]

No uniqueness assumption is hidden in either estimate.

---

## 7. F-separation defect bound

Let `h` be the number of unique clean A-vertices with residual coordinate degree at least `k-1`.  Since

\[
\sum_{x\in A}R_x=r,
\]

we have

\[
\boxed{h(k-1)\le r.} \tag{7.1}
\]

The clean part of `F` is bipartite between the two clique layers, and every clean-clean F-edge has both endpoints among those `h` high-residual vertices.  Therefore

\[
e(F[\text{clean}])\le\left\lfloor\frac{h^2}{4}\right\rfloor. \tag{7.2}
\]

Every A-vertex has `d_F<=k` because it already has exactly `k` neighbours in `B`.  Edges incident with exceptional vertices therefore contribute at most `|E_A|k`.  Hence

\[
\boxed{
e(F)
\le
\left\lfloor\frac{h^2}{4}\right\rfloor+|E_A|k.
} \tag{7.3}
\]

Together with

\[
r=k(k-\lambda),
\qquad
\delta=r-e(F), \tag{7.4}
\]

this gives an explicit eventual comparison with `M(n)`.

The arithmetic thresholds are:

### Complete exceptional core

Using `|E_A|<=10-2lambda`:

- `lambda=1`: closed for every `k>=15`;
- `lambda=0`: closed for every `k>=17`;
- `lambda=-1`: closed for every `k>=19`.

Thus the complete-core lopsided state is below `M(n)` for all

\[
\boxed{k>=19.} \tag{7.5}
\]

### `K_4-e` survivor

Here `lambda=-1`, `|E_A|<=10`, and the same calculation closes from

\[
\boxed{k>=16.} \tag{7.6}
\]

---

## 8. Lopsided four-defect conclusion

Combining the exact rooted-core cover table with Sections 3--7 gives:

> **LOPSIDED NO-PAIR FOUR-DEFECT EXCLUSION — internal candidate.**  
> In the full tight-antipode Boolean branch, suppose a switching class contains a four-defect state with no isolated leaf-pairs and all `k-4` ordinary leaves attached to one exceptional coordinate.  If
> \[
> \boxed{k>=19},
> \]
> then
> \[
> \boxed{m\le M(n).}
> \]

Six rooted cores are impossible immediately because `tau(Omega)>2k`; the only two low-cover cores are `K_4` and `K_4-e` with the missing edge away from the attachment root, and both are eventually closed by residual/F-separation pricing.

---

## 9. Strategic consequence

The complete four-defect problem still contains the bounded-width attachment rays from `GENERAL_LEAF_PACKAGE_REDUCTION.md`, but its most dangerous unbounded lopsided no-pair ray is now closed.

The next coherent target is the remaining `t=0,g=2` strip

\[
(0,0,y,z),\qquad1\le y\le6,
\]

because `z` is the only unbounded parameter.  The same rooted-core/projective-code method can be applied separately for each of the six fixed values of `y` before moving to `g=3,4` or isolated-pair rays.

---

## 10. Trust boundary

- The eight-row rooted-core table is a finite hand calculation from (1.2), backed by an exact finite regression checker; external mathematical review remains open.
- The F-separation closure deliberately treats duplicate code classes conservatively and does not assume a selected representative is unique unless uniqueness is proved.
- The theorem concerns only the lopsided no-pair four-defect ray, not the complete four-defect family.
- `X_3` at `k=4` remains outside theorem scope and is not suppressed.
- No all-order second-extremal theorem is claimed.
