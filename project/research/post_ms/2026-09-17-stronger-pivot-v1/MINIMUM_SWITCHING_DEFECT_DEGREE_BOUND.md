# Universal large minimum-switching-defect support bound

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal structural lemma; elementary and hand-checkable, not promoted. External review open.**

The fixed-defect program has now closed switching states with five and six non-leaf coordinates by support alone. Before pushing to seven defects one case at a time, it is useful to record the opposite-end bound: if **every** switched state has many non-leaf coordinates, the orientation-code graph cannot be covered by `2k` codes for the simplest possible reason — no code has enough witness degree.

## 1. Orientation-code degree

In the full tight-antipode Boolean normal form, the orientation-code graph `Omega_sigma` has one edge for each physical rooted `B`-edge. Hence

\[
|E(\Omega_\sigma)|=Q=k(k-1). \tag{1}
\]

For a Boolean code `c`, let `L_c` be its switched graph on the `k` antipode fibres, let

\[
\ell(c)=|\{j:d_{L_c}(j)=1\}|,
\]

and let

\[
\phi(c)=k-\ell(c)
\]

be its number of non-leaf coordinates.

The leaf-incidence calculation used throughout the project gives

\[
\boxed{d_{\Omega}(c)=\ell(c)=k-\phi(c)} \tag{2}
\]

(counting physical edge multiplicity where relevant).

Define the minimum switching defect of the signing by

\[
d_*:=\min_c\phi(c). \tag{3}
\]

Then every orientation-code vertex has degree at most

\[
\Delta(\Omega)\le k-d_*. \tag{4}
\]

## 2. Edge-count lower bound on the witness-code cover

Every vertex cover `C` of a multigraph covers at most the sum of the degrees of its vertices. Thus from (1) and (4),

\[
k(k-1)
\le\sum_{c\in C}d_\Omega(c)
\le |C|(k-d_*).
\]

Therefore

\[
\boxed{
\tau(\Omega_\sigma)\ge
\left\lceil\frac{k(k-1)}{k-d_*}\right\rceil.
} \tag{5}
\]

This is just the global form of the witness-leaf capacity inequality.

If

\[
2d_*>k+1, \tag{6}
\]

then

\[
\frac{k(k-1)}{k-d_*}>2k,
\]

so

\[
\boxed{\tau(\Omega_\sigma)>2k.} \tag{7}
\]

Since an above-`M(n)` full-tight graph requires `a<=2k` and its distinct A-code support is a vertex cover of `Omega_sigma`, condition (6) is impossible above threshold.

Thus:

> **LARGE MINIMUM-DEFECT SUPPORT EXCLUSION.** In an above-`M(n)` full tight-antipode counterexample one must have
>
> \[
> \boxed{d_*\le\left\lfloor\frac{k+1}{2}\right\rfloor.} \tag{8}
> \]

No finite computation is involved.

## 3. Combined current window

The existing fixed-defect theorems give, for sufficiently large `k` in the full-tight branch:

- defect `0`: perfect-matching state excluded (apart from the finite `X_3` mechanism);
- defect `1`: complete one-defect regime eventually excluded;
- defect `2`: excluded from `k>=14`;
- defect `3`: excluded from `k>=15`;
- defect `4`: excluded from `k>=19`;
- defect `5`: support-impossible from `k>=8`;
- defect `6`: support-impossible from `k>=9`.

Consequently, for

\[
\boxed{k\ge19},
\]

any above-threshold full-tight signing would have to satisfy the sharply narrowed minimum-defect window

\[
\boxed{
7\le d_*\le\left\lfloor\frac{k+1}{2}\right\rfloor.
} \tag{9}
\]

This is the remaining switching-theoretic gap after the present work.

## 4. Strategic meaning

The next useful theorem should bridge (9), not merely add one fixed integer at a time. Two routes now look natural:

1. strengthen (5) using the switching structure to show that a `2k`-vertex cover cannot consist entirely of near-maximum-degree code vertices; or
2. use the coordinatewise leaf-package reduction to prove a residual exceptional-core contribution growing with `d_*`, which would subsume the five-/six-defect certificates.

The second route is especially consistent with the observed five- and six-defect behaviour: once `d` reaches five, support rather than F-separation has been sufficient.

## 5. Negative control and scope

The published 12-vertex `X_3` graph has `k=4` and lies at the residual-zero/perfect-matching boundary. It is outside the large-`k` conclusion (9) and remains untouched.

This note concerns only the full tight-antipode Boolean normal form. It does not close unmatched/errorful antipodes and does not claim an all-order second-extremal theorem.
