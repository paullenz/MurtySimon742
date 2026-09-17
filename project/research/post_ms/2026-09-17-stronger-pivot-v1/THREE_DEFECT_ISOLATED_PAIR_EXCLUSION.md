# Three-defect isolated-pair exclusion from leaf packages plus outside matchings

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical review open.**

This note continues `THREE_DEFECT_LEAF_PACKAGE_REDUCTION.md`. The leaf-package theorem reduces every three-defect state containing isolated leaf-leaf `K_2` components to three narrow rays. Small matchings in the orientation-code graph outside the leaf-leaf code support close all three rays.

The conclusion is strong:

> for `k>=10`, every three-defect switched state containing at least one isolated leaf-pair has `tau(Omega_sigma)>2k`.

Hence such a state is incompatible with the preserved above-`M(n)` density window `a<=2k`; no F-analysis is required.

The order-12/32 hostile control is residual-zero/perfect-matching and is unaffected.

---

## 1. Preserved leaf-package bound

Use the notation of `THREE_DEFECT_LEAF_PACKAGE_REDUCTION.md`:

- exceptional coordinates `a,b,c`;
- pendant attachment sizes `p_1,p_2,p_3`;
- `g` nonempty pendant groups;
- `t>=1` isolated leaf-pairs;
- sorted attachment counts `x<=y<=z`;
- `k=3+S+2t`, where `S=p_1+p_2+p_3`.

Let `V_LL` be the set of orientation-code vertices occurring in an edge whose quotient pair consists of two leaves. The exact minimum cover of the leaf-leaf subgraph is

\[
L=B+4tg+2t(t-1)+1, \tag{1.1}
\]

where

\[
B=2\sum_i(p_i-1)_+
 +2\sum_{i<j}\min(p_i,p_j).
\]

In particular

\[
L-2k=(4t-2)g+4x+2y+2t^2-6t-5. \tag{1.2}
\]

If `L>2k`, the state is already impossible above threshold. Thus only the finite-width survivors of the leaf-package test need attention.

---

## 2. Additivity with an outside matching

Let

\[
\Omega^\circ=\Omega_\sigma-V_{LL}. \tag{2.1}
\]

Every vertex cover of `Omega_sigma` must use at least `L` vertices from `V_LL`, because both endpoints of every leaf-leaf edge lie in `V_LL`. If `Omega^circ` contains a matching of size `mu`, at least `mu` further cover vertices are needed outside `V_LL`. Therefore

\[
\boxed{\tau(\Omega_\sigma)\ge L+\nu(\Omega^\circ).} \tag{2.2}
\]

This elementary separation is the only new covering principle needed below.

For each listed quotient pair, both physical rooted-B edges over that pair are used. Direct substitution in the forced witness-code formula shows that the displayed physical edges have pairwise distinct endpoints and that none of those endpoints belongs to `V_LL`. Thus `q` displayed quotient pairs give a matching of size `2q` in `Omega^circ`.

---

## 3. Leaf-package survivors for `k>=10`

The exact inequality (1.2) leaves only the following possibilities once fixed small orders are removed.

### Case A: `t=1`, `g=1`

The attachment pattern is

\[
(0,0,z).
\]

The two zero-attachment exceptional coordinates, call them `a,b`, must have exceptional-core degree different from one. Hence the exceptional core is either empty or a triangle. Let `c` be the attachment centre, let `d` be any pendant leaf at `c`, and let `{r,s}` be the isolated leaf-pair.

Here

\[
L-2k=-7. \tag{3.1}
\]

The four quotient pairs

\[
\boxed{
\{a,c\},\quad
\{a,d\},\quad
\{b,r\},\quad
\{b,s\}
} \tag{3.2}
\]

supply eight pairwise vertex-disjoint physical orientation-code edges in `Omega^circ`, for both possible exceptional cores. Therefore

\[
\nu(\Omega^\circ)\ge8,
\]

and

\[
\tau(\Omega_\sigma)\ge L+8\ge2k+1. \tag{3.3}
\]

So this ray is impossible above threshold.

### Case B: `t=1`, `g=2`

The leaf-package inequality allows only a smaller positive attachment size

\[
y\in\{1,2\}.
\]

Let `a` be the unique exceptional coordinate with no pendant group, and let `{r,s}` be the isolated leaf-pair. The two quotient pairs

\[
\boxed{\{a,r\},\quad\{a,s\}} \tag{3.4}
\]

supply four pairwise vertex-disjoint physical edges in `Omega^circ`, independently of the valid exceptional-core graph.

From (1.2),

\[
L-2k=2y-5,
\]

so

\[
\tau(\Omega_\sigma)
\ge L+4
=2k+(2y-1)
>2k. \tag{3.5}
\]

Thus both `y=1` and `y=2` are impossible above threshold.

### Case C: `t=2`, `g=1`

Again the attachment pattern is `(0,0,z)`, so the exceptional core is empty or a triangle. Let `a,b` be the zero-attachment exceptional coordinates, `c` the attachment centre, and `r` one endpoint of either isolated leaf-pair.

Equation (1.2) gives

\[
L-2k=-3. \tag{3.6}
\]

The two quotient pairs

\[
\boxed{\{a,c\},\quad\{b,r\}} \tag{3.7}
\]

supply four pairwise vertex-disjoint physical orientation-code edges in `Omega^circ`, for both possible exceptional cores. Hence

\[
\tau(\Omega_\sigma)\ge L+4\ge2k+1. \tag{3.8}
\]

So this ray is impossible above threshold.

---

## 4. Why these are all eventual isolated-pair cases

The leaf-package reduction gives:

- `t=1`: only `g=0`, `g=1`, or `g=2` with smaller positive attachment at most `2`;
- `t=2`: only `g=0` or `g=1`;
- `t=3`: only `g=0`;
- `t>=4`: already `L>2k`.

But `g=0` fixes

\[
k=3+2t,
\]

so the surviving `g=0` cases have `k=5,7,9` for `t=1,2,3`. Therefore none occurs once `k>=10`.

Cases A--C exhaust every remaining `k>=10` possibility.

We obtain:

> **THREE-DEFECT ISOLATED-PAIR EXCLUSION — internal candidate.**  
> In the full tight-antipode Boolean branch, if a switched state has exactly three non-leaf coordinates, contains at least one isolated leaf-leaf `K_2`, and `k>=10`, then
> \[
> \boxed{\tau(\Omega_\sigma)>2k.}
> \]
> Consequently it cannot occur in an above-`M(n)` graph, because such a graph has `a<=2k`.

This removes **all isolated-pair parameters** from the eventual three-defect classification.

---

## 5. Strategic consequence

For the eventual problem, a three-defect state may now be assumed to have

\[
\boxed{t=0.}
\]

Thus every ordinary leaf is attached directly to one of the three exceptional coordinates. The complete three-defect theorem is reduced to the no-pair finite-width rays

- `(0,0,z)` — already closed by the empty-core-star and triangle-star exclusions;
- `(0,y,z)` with `1<=y<=5`;
- `(1,y,z)` with `1<=y<=4`;
- `(2,2,z)`.

The first ray is closed for `k>=15`. The next highest-value task is therefore a finite exceptional-core cover certificate for the remaining bounded minor attachments. No isolated-pair analysis needs to be revisited.

---

## 6. Trust boundary

- The matching certificates (3.2), (3.4), and (3.7) are direct forced-code calculations and are independently replayable in the accompanying checker.
- The theorem is intentionally eventual (`k>=10`); the fixed small `g=0` states are not absorbed into it.
- No claim is made yet that the remaining `t=0` rays are completely classified.
- The published order-12/32 negative control remains outside this branch and remains mandatory.