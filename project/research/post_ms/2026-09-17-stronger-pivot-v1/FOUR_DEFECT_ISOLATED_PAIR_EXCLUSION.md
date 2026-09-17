# Four-defect isolated-pair switching exclusion

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical review open.**

`GENERAL_LEAF_PACKAGE_REDUCTION.md` shows that, for sufficiently large four-defect states, the presence of isolated leaf-pairs leaves only three finite-width possibilities:

1. `t=1`, one nonempty pendant group;
2. `t=1`, two nonempty pendant groups, with the smaller size `y in {1,2,3}`;
3. `t=2`, one nonempty pendant group.

This note adds the four-vertex exceptional-core contribution and eliminates all three possibilities by orientation-code support alone.  No F-density estimate is needed.

The order-12/32 `X_3` obstruction is a separate residual-zero perfect-matching mechanism and is unaffected.

---

## 1. Setup

Let the exceptional coordinates be `0,1,2,3`.  The unbounded pendant group is attached to coordinate `0`; write its size as `z`.  Any second pendant group is attached to coordinate `1` and has fixed size `y`.  The remaining leaves form `t` isolated `K_2` components.

The exceptional core is a graph `H` on `{0,1,2,3}`.  For a designated exceptional coordinate with no pendant leaves, validity requires its core degree not to equal one.  If a coordinate has exactly one attached leaf, its core degree must be nonzero; coordinates with at least two attached leaves are automatically non-leaves.

The exact physical orientation-code graph is reconstructed from the forced-code rule.  The calculation below is a finite rooted-core case split; the unbounded parameter `z` only enlarges the same clique/star packages, so the cover-number excess over `2k` is constant along each ray.

---

## 2. One isolated pair and one pendant group

Here

\[
t=1,\qquad(p_0,p_1,p_2,p_3)=(z,0,0,0),
\qquad k=6+z.
\]

For `z>=4`, the valid rooted exceptional cores are the same eight rooted types as in the no-pair lopsided classification.  Exact projective-code grouping gives:

| rooted core | `tau(Omega)-2k` |
|---|---:|
| empty | 8 |
| `K_3` through the attachment root + isolated | 16 |
| `C_4` | 14 |
| `K_4-e`, missing edge away from root | 12 |
| non-root `K_3` + isolated root | 19 |
| paw, root pendant | 17 |
| `K_4-e`, missing root edge | 16 |
| `K_4` | 16 |

Thus

\[
\boxed{\tau(\Omega_\sigma)\ge2k+8.} \tag{2.1}
\]

In particular this ray is impossible in an above-`M(n)` full-tight graph, because such a graph has `a<=2k` while its distinct A-code support must cover `Omega_sigma`.

---

## 3. Two isolated pairs and one pendant group

Now

\[
t=2,\qquad(p_0,p_1,p_2,p_3)=(z,0,0,0),
\qquad k=8+z.
\]

For `z>=4` the same rooted-core calculation gives:

| rooted core | `tau(Omega)-2k` |
|---|---:|
| empty | 16 |
| `K_3` through the attachment root + isolated | 32 |
| `C_4` | 26 |
| `K_4-e`, missing edge away from root | 24 |
| non-root `K_3` + isolated root | 35 |
| paw, root pendant | 33 |
| `K_4-e`, missing root edge | 32 |
| `K_4` | 32 |

Hence

\[
\boxed{\tau(\Omega_\sigma)\ge2k+16.} \tag{3.1}
\]

This ray is even farther outside the density window.

---

## 4. One isolated pair and two pendant groups

The general leaf-package theorem permits this case only when the smaller group satisfies

\[
y\in\{1,2,3\}.
\]

Write

\[
t=1,\qquad(p_0,p_1,p_2,p_3)=(z,y,0,0),
\qquad k=6+z+y,
\]

with `z>=max(4,y)`.

A complete labelled exceptional-core check from the forced-code formula gives the following **minimum** excesses over all valid core graphs:

\[
\begin{array}{c|c}
y&\min_H\bigl(\tau(\Omega_\sigma)-2k\bigr)\\
\hline
1&14\\
2&18\\
3&20.
\end{array} \tag{4.1}
\]

The minima are attained by explicit core types:

- `y=1`: the single exceptional edge joining the two attachment coordinates;
- `y=2,3`: `K_4` or `K_4` with the attachment-to-attachment edge deleted in the corresponding labelled position.

The precise minimizer is less important than the uniform consequence

\[
\boxed{\tau(\Omega_\sigma)>2k.} \tag{4.2}
\]

Thus every surviving two-group isolated-pair ray is support-impossible above threshold.

---

## 5. Complete isolated-pair conclusion

`GENERAL_LEAF_PACKAGE_REDUCTION.md` already shows that, once `k` is sufficiently large, no other four-defect pattern with `t>=1` can satisfy the necessary leaf-package condition `L_4<=2k`.

For `k>=13`:

- `t=1,g=1` has `z>=7`;
- `t=1,g=2` with `y<=3` has `z>=4`;
- `t=2,g=1` has `z>=5`;
- `t>=3` is excluded by the leaf package itself except for fixed smaller orders.

Combining Sections 2--4 therefore gives:

> **FOUR-DEFECT ISOLATED-PAIR EXCLUSION — internal candidate.**  
> In the full tight-antipode Boolean branch, if a switched state has exactly four non-leaf coordinates, contains at least one isolated leaf-leaf `K_2`, and
> \[
> \boxed{k>=13},
> \]
> then
> \[
> \boxed{\tau(\Omega_\sigma)>2k},
> \]
> so the state cannot occur in an above-`M(n)` graph.

Thus every eventual four-defect counterexample may be assumed to have

\[
\boxed{t=0}. \tag{5.1}
\]

---

## 6. Strategic consequence

Together with `FOUR_DEFECT_LOPSIDED_SWITCHING_CLASSIFICATION.md`, the remaining four-defect frontier is now entirely no-pair and has at least two nonempty pendant groups.  The general leaf-package reduction leaves only the bounded-width strips

- `(0,0,y,z)`, `1<=y<=6`;
- `(0,x,y,z)` with `(x,y)` in the seven listed pairs;
- `(w,x,y,z)` with `(w,x,y)` equal to `(1,1,1)`, `(1,1,2)`, or `(1,1,3)`.

Only `z` remains unbounded.  This is a much smaller target than the original arbitrary four-defect family.

---

## 7. Trust boundary

- The rooted-core excess tables are finite hand calculations from the exact forced-code formula, backed by exact regression over several consecutive values of the unbounded parameter.
- The theorem uses those tables only as support lower bounds; no D2C realizability is inferred from the switching states.
- The claim is eventual (`k>=13`), not all-order.
- The `k=4` order-12/32 `X_3` negative control lies outside this regime.
- External mathematical review remains open.
