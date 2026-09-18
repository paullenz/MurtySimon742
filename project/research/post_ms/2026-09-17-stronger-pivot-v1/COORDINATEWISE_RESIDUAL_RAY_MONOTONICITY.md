# Coordinatewise residual ray monotonicity and ternary reduction

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal structural lemma; not promoted. External mathematical review open.**

This strengthens `LEAF_PACKAGE_RESIDUAL_RAY_MONOTONICITY.md`. The earlier statement singled out the largest pendant group. The proof does not use maximality: it works for **any** pendant group once that group already contains at least two leaves. This removes an unnecessary asymmetry and gives a useful finite-state reduction for every fixed defect count.

The setting is the full tight-antipode Boolean normal form. Let a switched state have `d>=3` non-leaf exceptional coordinates, pendant groups `D_1,...,D_d`, and any fixed number of isolated leaf-pairs. Let `Omega` be its orientation-code graph. Let `V_leaf` be the code vertices used by quotient pairs whose two coordinates are leaves, and put

\[
R=\Omega[V(\Omega)\setminus V_{leaf}].
\]

The general leaf-package theorem gives the exact leaf-package cover `L_d`, and vertex-disjointness gives

\[
\tau(\Omega)\ge L_d+\tau(R). \tag{1}
\]

## 1. Enlarge an arbitrary established pendant group

Fix an exceptional coordinate `r` and assume

\[
|D_r|\ge2.
\]

Add a new leaf `u` adjacent only to `r`, keeping the exceptional core, all other pendant groups, and all isolated leaf-pairs fixed.

For a switched graph `L`, the projective forced witness code is

\[
[c(q\to j)]=[N_L(q)\triangle\{j\}]. \tag{2}
\]

Embed every old coordinate set in the enlarged coordinate set. Then:

- an old code sourced at `r` gains the new coordinate `u`;
- every old code sourced elsewhere is unchanged;
- complementary code classes transform compatibly.

Therefore two distinct old code classes cannot merge. If both are sourced at `r`, they both toggle `u`; if neither is, neither changes; if exactly one is, the new `u` bit separates them.

It remains to check that an embedded old residual vertex is not newly absorbed into the enlarged leaf package. Every genuinely new leaf-leaf quotient pair uses `u`. Its leaf-source codes have the projective forms

\[
\{p(x),u\}\quad\text{or}\quad\{r,x\}, \tag{3}
\]

where `x` is an old leaf and `p(x)` is its parent.

The first family contains the genuinely new coordinate `u`, so it cannot equal an embedded old residual class. For the second family:

- if `x\in D_r`, the code `{r,x}` was already present in the old same-group leaf package because `|D_r|>=2`;
- if `x` lies in another nonempty pendant group, `{r,x}` was already present from old cross-group leaf pairs;
- if `x` belongs to an isolated leaf-pair, the corresponding parent/target leaf-package code was likewise already present in the old leaf package.

Thus no old residual code vertex is newly swallowed by `V_leaf`. Every old residual physical edge survives, so

\[
\boxed{R(\mathbf p)\hookrightarrow R(\mathbf p+e_r)} \tag{4}
\]

and hence

\[
\boxed{\tau(R(\mathbf p+e_r))\ge\tau(R(\mathbf p)).} \tag{5}
\]

No assumption that `D_r` is largest was used.

## 2. The support margin is coordinatewise nondecreasing beyond size two

The exact leaf-package formula is

\[
B_d=2\sum_i(p_i-1)_++2\sum_{i<j}\min(p_i,p_j),
\]

with the fixed isolated-pair term added when `t>0`.

If `p_r>=2` is increased by one, the first sum increases by exactly `2`, while the pairwise-minimum sum can only increase. Therefore

\[
L_d(\mathbf p+e_r)-L_d(\mathbf p)\ge2. \tag{6}
\]

At the same time `k` increases by one, so `2k` increases by exactly two. Combining (5) and (6), the additive support margin

\[
\mu(\mathbf p):=L_d(\mathbf p)+\tau(R(\mathbf p))-2k
\]

satisfies

\[
\boxed{\mu(\mathbf p+e_r)\ge\mu(\mathbf p)\qquad(p_r\ge2).} \tag{7}
\]

This is the coordinatewise residual monotonicity principle.

## 3. Ternary finite-state reduction

For fixed `d`, fixed isolated-pair count `t`, and fixed exceptional core, every pendant size belongs to one of three structural statuses:

\[
0,\qquad1,\qquad\ge2.
\]

Once a coordinate has reached `2`, increasing it cannot decrease the support margin. Consequently, to prove a strict support inequality throughout an orthant of attachment vectors it is enough to prove it at the coordinatewise minimal vector obtained by replacing every entry `>=2` by `2`, apart from any finite adjustment needed to enter a stated lower bound on `k`.

Equivalently:

> **TERNARY REDUCTION.** For a fixed exceptional core and fixed `t`, the worst support margin on each attachment-status class occurs at its finite boundary with pendant sizes in `{0,1,2}` (or at the first point on that class satisfying the chosen order threshold).

This is stronger than the earlier one-ray statement. It says that after the leaf-package reduction there is no need to regard several pendant groups as simultaneously unbounded: all established groups may be pushed back independently to size two.

## 4. Why this matters

The fixed-defect switching problem can now be organized as follows.

1. The exact leaf-package inequality discards most attachment-status patterns immediately.
2. Every surviving large attachment vector reduces coordinatewise to a finite `{0,1,2}` boundary pattern.
3. Only the finite exceptional core and those finitely many status patterns require certification.

At defect count `d`, the exceptional core has only `2^{d choose 2}` labelled possibilities. The growth with `d` is still real, but the unbounded pendant geometry has been removed completely.

This gives a cleaner route to testing whether the five-defect support phenomenon extends to all `d>=5`: search for a defect-count lower bound on the residual exceptional-core witness contribution, rather than re-running unbounded pendant scans.

## 5. Trust boundary

- The lemma is a hand consequence of the forced projective code formula and the exact leaf-package decomposition.
- The `p_r>=2` hypothesis is essential for the same-group code `{r,x}` to have already appeared before extension.
- The statement concerns a lower-bound decomposition `L_d+tau(R)`, not equality with the full orientation-code cover number.
- The order-12/32 `X_3` graph is the separate `k=4,r=0` zero-defect mechanism and lies outside this higher-defect monotonicity argument.
- No all-order second-extremal theorem is claimed.
