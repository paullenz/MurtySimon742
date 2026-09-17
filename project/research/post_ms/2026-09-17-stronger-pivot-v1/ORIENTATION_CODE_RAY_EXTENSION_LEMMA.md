# Orientation-code ray extension: finite core certificates persist along pendant rays

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal structural lemma; not promoted. External mathematical review open.**

This note isolates the mechanism behind the repeated empirical observation that, once every bounded attachment parameter is fixed, increasing the one unbounded pendant group raises the orientation-code cover lower bound in lockstep with `2k`. The phenomenon is structural, not numerical.

---

## 1. Setup

Let `L` be one switched graph on the `k` antipode fibres. Fix a set `E` of `d>=3` non-leaf exceptional coordinates. Every other coordinate is a leaf, lying either in a pendant group `D_i` attached to an exceptional parent `e_i` or in an isolated leaf-leaf pair.

Fix:

- the exceptional graph `L[E]`;
- every isolated leaf-pair;
- every pendant group except one distinguished group `D_r`;
- one representative leaf from every nonempty pendant group.

Suppose `D_r` is enlarged by one new leaf `u`, adjacent only to its parent `r`.

For an oriented quotient pair with source coordinate `q` and target coordinate `j`, the projective orientation-code class is

\[
\boxed{[c(q\to j)] = [N_L(q)\triangle\{j\}]}, \tag{1.1}
\]

where `[S]` identifies a code with its complement.

---

## 2. Injectivity under one-leaf extension

Adding `u` changes only one old neighbourhood:

\[
N_{L'}(r)=N_L(r)\cup\{u\};
\]

all other old neighbourhoods are unchanged.

Therefore every old projective code class transforms in one of two ways:

- if its source is not `r`, its representative set is unchanged;
- if its source is `r`, its representative gains the new coordinate `u`.

This transformation is injective on old projective code classes.

Indeed, two classes transformed in the same way remain distinct because deleting `u` recovers the old classes. If exactly one gains `u`, equality as ordinary sets is impossible. Equality up to complement would imply that the old representatives were already complementary, hence belonged to the same old projective class.

Thus:

> **PROJECTIVE RAY INJECTIVITY.** Distinct old orientation-code classes never merge when a new pendant leaf is added to one fixed parent.

The same statement holds in the full Boolean code graph before quotienting by complement. Each old full code either keeps the new bit equal to zero or acquires it equal to one, depending on its source and physical orientation. Codes with different new-bit behaviour cannot merge; codes with the same behaviour preserve their old distinction.

---

## 3. Matching persistence

Let `Gamma_k` be any subgraph of the orientation-code graph formed entirely from old quotient pairs and old code vertices—for example the residual core-witness graph obtained after deleting the leaf-package vertices and retaining exceptional-exception pairs plus one representative leaf from each active group.

Under one-leaf extension every edge of `Gamma_k` maps to the corresponding edge of `Gamma_{k+1}`, and Section 2 shows that distinct old vertices remain distinct. Hence every vertex-disjoint matching persists.

Therefore

\[
\boxed{\nu(\Gamma_{k+1})\ge\nu(\Gamma_k).} \tag{3.1}
\]

Iterating gives monotonicity along the entire pendant ray.

This is stronger than the empirical statement that a few consecutive exact scans agree: one finite matching certificate at a base point remains a certificate for all larger values of the unbounded attachment.

---

## 4. Interaction with the leaf package

For fixed defect count `d`, fixed isolated-pair count `t`, and fixed bounded pendant groups, increasing the **largest** pendant group by one increases the exact leaf-package cover number by exactly two.

In the sorted leaf-package formula

\[
B_d=2S-2g+2\sum_{i=1}^d(d-i)p_{(i)},
\]

the largest attachment has coefficient zero in the weighted sum, while `S` increases by one. Hence

\[
B_d(k+1)=B_d(k)+2. \tag{4.1}
\]

At the same time

\[
2(k+1)=2k+2. \tag{4.2}
\]

Combining (3.1), (4.1), and a vertex-disjoint leaf-package/core-witness decomposition gives:

> **RAY-EXTENSION PRINCIPLE.** If at one base point on a fixed structural ray one has
>
> \[
> B_d+\nu(\Gamma)>2k,
> \]
>
> then the same strict inequality holds at every larger value of the distinguished largest pendant group.

No further scan in the unbounded parameter is needed.

---

## 5. Why this matters

The general leaf-package theorem already proves that for every fixed defect count `d`, all attachment counts except the largest are bounded in any possible above-`M(n)` state. The present lemma removes the remaining infinite direction:

1. enumerate the finitely many bounded attachment patterns allowed by the leaf package;
2. for each, inspect only one finite exceptional core together with one base value of the largest group;
3. produce a residual matching certificate;
4. extend that certificate along the whole ray by the lemma above.

Thus every fixed-defect switching problem is reduced to a genuinely finite exceptional-core problem.

The four-defect completion uses this principle explicitly. The next application is the five-defect layer, where preliminary exact core data suggest support alone may already rule out every sufficiently-large state.

---

## 6. Trust boundary

- The ray-extension statement is a hand injectivity argument, not a fitted pattern from computation.
- It guarantees persistence of a **given finite certificate**; it does not claim that the exact minimum cover number itself must increase by exactly two.
- The fixed-core base certificate must still be proved or independently certified.
- The `k=4`, order-12/32 `X_3` residual-zero obstruction lies in a different switching regime and is unaffected.
