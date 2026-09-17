# Leaf-package / residual ray monotonicity

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal structural lemma; not promoted. External mathematical review open.**

This strengthens `ORIENTATION_CODE_RAY_EXTENSION_LEMMA.md`. A matching certificate is not the only object that persists when the unique unbounded pendant group is enlarged: once that group already has at least two leaves, the **entire old residual orientation-code subgraph** embeds in the new residual subgraph. Consequently its vertex-cover number cannot decrease.

---

## 1. Leaf package and residual graph

Fix a switched state with exceptional non-leaf set `E`, pendant groups `D_i`, and any fixed isolated leaf-pairs. Let `Omega` be the full orientation-code graph.

Let `Omega_leaf` be the subgraph contributed by quotient pairs whose two coordinates are leaves, and let `V_leaf` be the set of code vertices occurring in that subgraph. The general leaf-package theorem gives its exact cover number `L_d` (or `B_d` when there are no isolated leaf-pairs).

Define the residual induced graph

\[
R=\Omega[V(\Omega)\setminus V_{\rm leaf}].
\]

Because the two vertex sets are disjoint,

\[
\boxed{\tau(\Omega)\ge \tau(\Omega_{\rm leaf})+\tau(R).} \tag{1.1}
\]

---

## 2. Add one leaf to a pendant group of size at least two

Let `D_r` be the distinguished largest pendant group and assume initially

\[
|D_r|\ge2.
\]

Add a new leaf `u` adjacent only to its exceptional parent `r`.

The forced projective code formula is

\[
[c(q\to j)]=[N_L(q)\triangle\{j\}].
\]

As in the ray-extension lemma, old code classes embed injectively in the enlarged code space: old classes sourced at `r` toggle the new coordinate `u`, while old classes with other sources do not; complementary classes behave compatibly. No two distinct old classes merge.

Now inspect the leaf package. Quotient pairs of two **old** leaves reproduce exactly the embedded old leaf-package graph. Every genuinely new leaf-pair uses `u` as one coordinate. Its forced leaf-source code has the form

\[
\{p(x),u\}
\quad\text{or}\quad
\{r,x\}
\]

(up to complement), where `x` is an old leaf and `p(x)` its parent.

The second family `{r,x}` was already present in the old leaf package whenever `x in D_r`, because `|D_r|>=2`; for leaves in another group it was already present from old cross-group leaf pairs whenever that group is nonempty. The first family contains the genuinely new coordinate `u` and therefore cannot equal an embedded old residual code class.

Thus no embedded old residual vertex is newly swallowed by the leaf package. Equivalently,

\[
\boxed{R_k\hookrightarrow R_{k+1}} \tag{2.1}
\]

as a graph embedding on the old quotient-pair edges.

Hence

\[
\boxed{\tau(R_{k+1})\ge\tau(R_k).} \tag{2.2}
\]

---

## 3. Ray consequence

Increasing the largest pendant group by one raises the exact leaf-package cover by exactly two, while `2k` also rises by exactly two. Therefore, from (1.1) and (2.2):

> **RESIDUAL RAY MONOTONICITY PRINCIPLE.** If at one base point with largest pendant group at least two one has
>
> \[
> L_d+\tau(R)>2k,
> \]
>
> then the same strict support inequality holds at every larger point on that structural ray.

This permits a finite **vertex-cover** certificate at one base point, not merely a matching certificate, to close the whole unbounded ray.

---

## 4. Scope and caveats

- The base size-two condition is important: it ensures the old same-group leaf-package codes `{r,x}` already exist before extension.
- If the ray begins with a largest group of size one, move to the size-two point before applying the lemma; the omitted smaller order is a finite boundary case.
- The lemma concerns persistence of a lower-bound subgraph. It does not assert that the exact full cover number itself changes by exactly two.
- Isolated leaf-pairs may be present but are held fixed along the ray.
- The order-12/32 `X_3` residual-zero obstruction is outside this higher-defect pendant-ray setting and is unaffected.
