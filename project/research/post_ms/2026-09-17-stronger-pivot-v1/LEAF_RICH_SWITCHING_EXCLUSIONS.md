# Leaf-rich switching exclusions in the full tight-antipode branch

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The live problem is the sufficiently-large/eventual second-extremal problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 Dailly--Foucaud--Hansberg Conjecture 3 is not assumed. The order-12, size-32 obstruction remains a mandatory hostile control.

This note critically changes emphasis from the immediately preceding handoff. The previous unit suggested attacking the algebraically first surviving layer `a=k+1,r=2k` through `F`-separation. For the eventual problem that layer is not the most informative object: above-`M(n)` density forces a full-tight root to have `a` close to `2k`, not close to `k`. The more useful next question is therefore whether the switching class itself can force `a` into a narrow near-balanced window before `F` is analysed.

Two leaf-rich switching types admit compact answers. A perfect-matching switched state is impossible in an above-`M(n)` full-tight graph once `k>=8`; and a full-star switched state is stronger still: its witness-code graph is exactly two disjoint copies of `K_k`, after which `F`-separation excludes the entire star branch above `M(n)` for `k>=8`.

---

## 1. Full-tight setup and a density window

Assume a maximum-degree root `v` has a full tight-antipode cover

\[
B=P_1\dot\cup\cdots\dot\cup P_k,\qquad |P_i|=2,
\]

so

\[
b=\Delta(G)=2k.
\]

Put

\[
A=V(G)\setminus N[v],\qquad a=|A|,
\]

and retain the full-tight identities

\[
Q=k(k-1),\qquad r=k(a-k+1),\qquad \delta=r-e(F).
\tag{1.1}
\]

Every `A`-vertex has exactly `k` neighbours in `B`, hence

\[
d_F(x)\le k. \tag{1.2}
\]

Choose endpoint bits on the antipode fibres. For a Boolean code `c`, let `L_c` be the switched graph on `[k]`, as in the preceding notes. Write

\[
\ell(c)=|\{j:d_{L_c}(j)=1\}|.
\]

The preserved Boolean witness-cover inequality is

\[
Q\le\sum_{c\in C}\ell(c), \tag{1.3}
\]

where `C` is the set of distinct A-codes.

Before using switching, note a simple but important density restriction.

> **Lemma 1.1 (above-M density window).** If `m>M(n)` in the full-tight branch, then
>
> \[
> \boxed{a\le2k}. \tag{1.4}
> \]

Indeed `m<=n\Delta/2=nk`. If `n=2s>=4k+2`, then `s>=2k+1` and

\[
M(n)=s^2-s+1>2sk=nk.
\]

If `n=2s+1>=4k+3`, then `s>=2k+1` and

\[
M(n)=s^2+1>(2s+1)k=nk.
\]

Thus an above-threshold graph must have `n<=4k+1`, equivalently `a<=2k`.

This is why the eventual full-tight problem lives near `a=2k`, even though the finite `X_3` boundary sits at `a=k-1`.

---

## 2. Perfect-matching switched states are too expensive

Suppose some code `c` has

\[
L_c\ \text{a perfect matching}. \tag{2.1}
\]

Then `k` is even. The preserved switching lemma says that for `k>=6`, every genuinely different switched state has at most two leaves. The only two codes giving the same switched graph are `c` and its complement.

Hence for any witness-code cover `C`,

\[
k(k-1)
\le \sum_{d\in C}\ell(d)
\le 2k+2(|C|-2).
\]

Therefore

> **Lemma 2.1 (perfect-matching cover cost).** For even `k>=6`, if the switching class contains a perfect matching, then
>
> \[
> \boxed{|C|\ge \frac{k^2-3k+4}{2}.} \tag{2.2}
> \]

For even `k>=8`, the right side is strictly greater than `2k`. By Lemma 1.1 an above-`M(n)` full-tight graph has only `a<=2k` labels. Consequently:

> **Corollary 2.2.** In an above-`M(n)` full-tight graph with even `k>=8`, **no switched state `L_c` can be a perfect matching**.

This does not touch the `k=4` residual-zero `X_3` mechanism; that finite hostile control remains outside the range of the corollary.

---

## 3. A full-star state normalises the orientation-code graph completely

Now suppose some code `c` has

\[
L_c=K_{1,k-1}. \tag{3.1}
\]

Switch first by `c`, so the signing itself is the star, and then switch at the star centre. This gauges the signing to the zero signing `sigma=0`. Gauge switching merely relabels the two endpoints in fibres, so it induces a bijection on Boolean codes and an isomorphism of the orientation-code graph. We may therefore work at `sigma=0` without loss.

For `sigma=0`,

\[
ij\in E(L_c)\iff c_i\ne c_j.
\]

Thus `L_c` is the complete cut determined by the support of `c`. For `k>=5`, this graph has a degree-one vertex **only** when the support has size `1` or `k-1`. Therefore the only leaf-bearing codes are

\[
e_1,\ldots,e_k,
\qquad
\bar e_1,\ldots,\bar e_k. \tag{3.2}
\]

Each has `k-1` leaves; every other code has zero leaves.

A direct orientation calculation now gives the whole witness-code graph:

- one physical B-edge over `{i,j}` joins the witness codes `e_i,e_j`;
- the complementary physical B-edge joins `\bar e_i,\bar e_j`.

Hence

> **Lemma 3.1 (star orientation-code normal form).** If the switching class contains a full star and `k>=5`, then, after deleting isolated code vertices,
>
> \[
> \boxed{\Omega_\sigma\cong K_k\ \dot\cup\ K_k.} \tag{3.3}
> \]

In particular every actual code support covering all rooted B-edges contains at least `k-1` codes from each layer:

\[
\boxed{|C|\ge2k-2.} \tag{3.4}
\]

Combining (3.4) with Lemma 1.1 gives

\[
2k-2\le a\le2k. \tag{3.5}
\]

It is useful to write

\[
\lambda=2k-a-1.
\]

Then (3.5) says that an above-`M(n)` star-class graph has only the three imbalance values

\[
\boxed{\lambda\in\{1,0,-1\}.} \tag{3.6}
\]

Equivalently

\[
a\in\{2k-2,2k-1,2k\}. \tag{3.7}
\]

This already collapses the star switching branch to three near-balanced residual layers.

---

## 4. F-separation makes almost all star codes mutually nonadjacent

Remain in the zero-signing gauge. Call the codes `e_i` the **low layer** and `\bar e_i` the **high layer**.

The selected-incidence separation rule from the predecessor says:

> if coordinate `j` is selected at label `x`, every `F`-neighbour of `x` agrees with `x` in coordinate `j`. \tag{4.1}

A label will be called **clean** if its code is one of the `2k` star codes in (3.2) and that code occurs exactly once among the A-labels. Let `E` be the set of non-clean labels.

Because at least `2k-2` distinct star codes must occur and `a<=2k`, there are only

\[
q=a-(2k-2)=1-\lambda\in\{0,1,2\}
\]

labels beyond a minimum star-code cover. A duplicated code class consumes at least one such surplus occurrence; all members of a duplicated class may be marked non-clean. Therefore

\[
\boxed{|E|\le2q=2(1-\lambda).} \tag{4.2}
\]

### 4.1 No same-layer F-edge between clean labels

Take clean low-layer labels of codes `e_i,e_j`, `i!=j`. Their codes differ exactly in coordinates `{i,j}`. The orientation-code graph contains the physical edge `e_ie_j`. Because each code occurs only once, the selected representative of that B-edge must be carried by one of these two labels. If it is carried by `e_i`, its selected source coordinate is `j`; if carried by `e_j`, its selected source coordinate is `i`. In either case the two labels disagree at a selected coordinate, contradicting (4.1) if they were F-adjacent.

Thus clean low-layer labels form an independent set in `F`. The same argument applies to the high layer.

### 4.2 Cross-layer F-edges require almost total residuality

Consider clean labels of codes `e_i` and `\bar e_j`.

- If `i=j`, the two codes disagree in all `k` coordinates. An F-edge therefore forces every coordinate to be residual at both endpoints.
- If `i!=j`, the codes agree only in coordinates `i,j`. The code `e_i` has star centre `i`, so `i` is not a leaf and cannot be selected; among the agreement coordinates it can select only `j`. Hence an F-edge forces its selected degree to be at most one, i.e. its residual degree is at least `k-1`. Symmetrically the `\bar e_j` endpoint also has residual degree at least `k-1`.

Therefore every clean-clean F-edge is a cross-layer edge whose endpoints both have residual degree at least `k-1`.

Let `h` be the number of clean labels with residual degree at least `k-1`. Since the total label-residual degree is `r`,

\[
h(k-1)\le r. \tag{4.3}
\]

The clean-clean part of `F` is bipartite between the two star layers, so

\[
e_F(A\setminus E)\le\left\lfloor\frac{h^2}{4}\right\rfloor. \tag{4.4}
\]

Every exceptional label has `F`-degree at most `k` by (1.2). Hence

> **Lemma 4.1 (star-class F bound).** In the full-star switching class,
>
> \[
> \boxed{
> e(F)\le
> \left\lfloor\frac{h^2}{4}\right\rfloor
> +2(1-\lambda)k,
> \qquad
> h\le\left\lfloor\frac{r}{k-1}\right\rfloor.
> } \tag{4.5}

This is deliberately conservative: all edges incident with exceptional labels are simply charged at the maximum-degree bound.

---

## 5. The full-star switching branch is finite

For the three possible imbalance values in (3.6), the exact residual and the bound on `h` are

\[
\begin{array}{c|c|c|c}
\lambda & a & r=k(k-\lambda) & h\le \\
\hline
1 & 2k-2 & k(k-1) & k\\
0 & 2k-1 & k^2 & k+1\\
-1 & 2k & k(k+1) & k+2
\end{array}
\tag{5.1}
\]

So Lemma 4.1 gives

\[
\delta=r-e(F)
\ge
\begin{cases}
 k(k-1)-\lfloor k^2/4\rfloor, & \lambda=1,\\[2mm]
 k^2-\lfloor (k+1)^2/4\rfloor-2k, & \lambda=0,\\[2mm]
 k(k+1)-\lfloor (k+2)^2/4\rfloor-4k, & \lambda=-1.
\end{cases}
\tag{5.2}
\]

The defect required for `m<=M(n)` is, respectively,

\[
D=b(n-b)-M(n)=
\begin{cases}
2k-2, & \lambda=1,\\
2k-1, & \lambda=0,\\
2k-1, & \lambda=-1.
\end{cases}
\tag{5.3}
\]

A direct parity check of (5.2) gives:

- `lambda=1`: the lower bound reaches `D` for every `k>=5`;
- `lambda=0`: it reaches `D` for every `k>=6`;
- `lambda=-1`: it reaches `D` for every `k>=8`.

Therefore:

> **FULL-STAR SWITCHING EXCLUSION — internal candidate.**  
> Let a D2C graph admit a maximum-degree root with a full tight-antipode cover of `B`, with `b=2k`. If the associated Boolean switching class contains a full star and `k>=8`, then
>
> \[
> \boxed{m\le M(n).}
> \]
>
> Hence no above-`M(n)` counterexample in the full-tight branch can have a full-star switched state once `k>=8`.

The theorem is substantially stronger than the preceding `r>=2k` gap in the star subbranch: it uses the exact orientation-code graph plus F-separation to close the branch outright for all sufficiently large fibre counts.

---

## 6. Verification and negative control

Companion checker:

`check_leaf_rich_switching_exclusions.py`

Recorded summary:

`LEAF_RICH_SWITCHING_EXCLUSIONS_CHECK_SUMMARY.json`

The checker verifies:

- the zero-signing switching class through `k=12`: exactly `2k` leaf-bearing codes, all full stars;
- the orientation-code graph is exactly two `K_k` components;
- the perfect-matching cover lower bound through `k=20`;
- the exact star-class defect arithmetic through `k=30`, including the thresholds `k=5,6,8` for `lambda=1,0,-1`.

These are finite regression checks of the algebra and normal forms. The universal statements above are hand proofs.

The order-12/32 hostile control remains untouched. It has `k=4`, lies on the residual-zero perfect-matching/factorization boundary, and is outside every sufficiently-large exclusion proved here.

---

## 7. Strategic consequence

The full-tight branch now has two leaf-rich switching mechanisms removed at large `k`:

1. a perfect-matching state is impossible above `M(n)` for even `k>=8` by code-cover capacity;
2. a full-star state is impossible above `M(n)` for every `k>=8` by the stronger `K_k dotcup K_k` orientation-code normal form and F-separation.

This makes a broad attack on the artificial `a=k+1,r=2k` layer less attractive. The next high-value question is the **intermediate switching regime** in which every switched graph has at least two non-leaf vertices and no perfect-matching or full-star state. The finite orientation-code data (`tau=8` at `k=5`, `tau=10` at `k=6`) continue to suggest the universal cover bound `tau(Omega_sigma)>=2k-2`; proving that bound, or proving it for the remaining one-defect `K_{1,k-3}+K_2` triad and then bootstrapping, would collapse every full-tight above-threshold graph to the same near-balanced three-layer window before the final `F` analysis.

No eventual theorem is claimed beyond the stated full-star and perfect-matching subbranches.
