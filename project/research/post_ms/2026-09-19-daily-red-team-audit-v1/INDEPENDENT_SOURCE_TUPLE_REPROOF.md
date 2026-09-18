# Independent source-tuple capacity re-proof — 19 September 2026

## Scope

This note deliberately re-derives the finite source-tuple capacity theorem used in the recent beta-support/Hall work without importing the existing proof text. It does **not** certify the whole graph-to-selected-system interface. The theorem below is proved conditional on two explicit structural premises inherited from that interface.

### Premise A — distinct physical sources

For every witness `x`, its source set `Y_x` contains pairwise distinct physical sources.

### Premise B — selected source-coordinate uniqueness

For a fixed physical source `y` and coordinate `i`, at most one selected witness uses `y` in the source-coordinate obligation `(y,i)`.

These are the exact shared premises that must still be independently traced back through the rooted criticality and selected-representative construction.

## Setup

Let witness `x` have source set `Y_x` of size `ell_x`. Relative to its centre code `c(x)`, the selected sources have `ell_x` designated target coordinates, one for each physical source, and `k_x` further non-target coordinates on which some selected source differs from the centre. Thus every coordinate nonconstant on a fixed subset of `r` sources from `Y_x` lies among at most `r+k_x` coordinates.

Fix an integer `r>=2` and an `r`-set `R` of physical sources. Let

`M_R = |{x : R subset Y_x}|`.

For `y in R`, let `a_y(R)` be the number of coordinates on which `y` is the unique bit among the sources of `R`. Let `T(R)` be the number of coordinates nonconstant on `R`.

## Lemma 1 — common-witness multiplicity

`M_R <= min_{y in R} a_y(R) <= T(R)/r`.

### Proof

For each common witness `x` and each `y in R`, the designated target coordinate `i_x(y)` makes `y` the unique bit among the selected sources and therefore among `R`. By Premise B, fixed physical source `y` cannot use the same coordinate for two distinct common witnesses. Hence the `M_R` common witnesses inject into the coordinates counted by `a_y(R)`, proving `M_R<=a_y(R)` for every `y`.

At a binary coordinate, at most one member of an `r`-set can be the unique bit. Therefore the sets of coordinates counted by the `a_y(R)` are pairwise disjoint subsets of the nonconstant coordinates, and

`sum_{y in R} a_y(R) <= T(R)`.

Thus `min_y a_y(R) <= T(R)/r`.

## Lemma 2 — fixed-tuple weighted capacity

For every fixed `r`-set `R`,

`sum_{x: R subset Y_x} 1/(k_x+r) <= 1/r`.

### Proof

If there is no common witness the assertion is immediate. Otherwise, for each common witness `x`, every coordinate nonconstant on `R` must be either one of the `r` designated target coordinates belonging to sources in `R` or one of the `k_x` non-target excess coordinates. Therefore

`T(R) <= k_x+r`.

If `T(R)>0`, this gives

`1/(k_x+r) <= 1/T(R)`.

Summing over the `M_R` common witnesses and applying Lemma 1,

`sum_{x: R subset Y_x} 1/(k_x+r) <= M_R/T(R) <= 1/r`.

The case `T(R)=0` cannot occur when a common witness exists, because each designated target coordinate makes one source unique.

## Corollary 3 — global r-tuple capacity

Summing Lemma 2 over all `r`-subsets of the ambient `a` physical sources gives

`sum_x binom(ell_x,r)/(k_x+r) <= binom(a,r)/r`.

Each witness appears once for each `r`-subset of its source set, so the left side is exactly the required double count.

## Corollary 4 — bounded-excess support capacity (`FDPr`)

For witnesses with `ell_x>=r` and `k_x<=K`,

`sum binom(ell_x,r) <= (K+r)/r * binom(a,r)`.

Indeed, `1/(k_x+r)>=1/(K+r)` on this subfamily, so Corollary 3 implies the claim.

If every witness in the subfamily has `ell_x>=u`, then

`N_{>=r}(K) <= floor(((K+r)/r) * binom(a,r)/binom(u,r))`.

The floor is legitimate because the count is integral.

## Corollary 5 — finite arbitrary-subset deficit

Let `L` be any chosen set of `N` witnesses with `ell_x>=u>=r`, and define

`C_hat_r(K)=floor(((K+r)/r) * binom(a,r)/binom(u,r))`.

For each integer `K>=0`, at most `C_hat_r(K)` witnesses in `L` can satisfy `k_x<=K`; hence

`#{x in L : k_x>K} >= [N-C_hat_r(K)]_+`.

Because the `k_x` are nonnegative integers,

`sum_{x in L} k_x = sum_{K>=0} #{x in L : k_x>K}`.

If the geometric setup bounds `k_x<=p-r`, truncating at `K=p-r` is exact; without that upper bound, truncating there is still a valid lower bound. Consequently

`sum_{x in L} k_x >= Phi_r(N) := sum_{K=0}^{p-r} [N-C_hat_r(K)]_+`.

This is the finite layer-cake deficit statement used downstream.

## Edge cases and audit observations

- The denominator `r` comes from the binary-coordinate fact that at most one member of an `r`-set is unique at a given coordinate; it is not an averaging heuristic.
- The proof is genuinely for an arbitrary chosen subset `L`; no ordering or extremal choice of witnesses is required.
- If `p-r<0`, the displayed truncated sum is empty and yields the harmless lower bound zero; downstream applications should state the intended range `r<=p`.
- The proof needs global uniqueness for the physical pair `(source,coordinate)`, not merely uniqueness inside one witness. Weakening Premise B to witness-local uniqueness would invalidate Lemma 1.
- The proof needs physical sources in `Y_x` to be distinct. Counting repeated source labels as different tuple elements would invalidate the fixed-`R` argument.

## Audit conclusion

The finite source-tuple capacity theorem, its bounded-excess support form, and the integrated arbitrary-subset deficit are mathematically re-derived at the abstract selected-system level. The principal unresolved issue is now more sharply located: independently certify Premises A and B from the rooted D2C criticality/selected-representative construction and then test the whole chain on realizable graphs. This note does not promote any global eventual D2C theorem.
