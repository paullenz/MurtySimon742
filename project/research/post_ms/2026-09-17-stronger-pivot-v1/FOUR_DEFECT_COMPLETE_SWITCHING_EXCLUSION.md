# Complete four-defect switching exclusion via a residual core matching lemma

18 September 2026. Research directed by Paul Lenz; derivation and finite certificates by ChatGPT/Geeps.

**Status: internal finite-certificate structural theorem; not promoted. External mathematical review and hand compression of the finite core lemma remain open.**

The active target is the eventual / sufficiently-large second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 strengthening is not assumed. The order-12, size-32 `X_3` obstruction is the separate `k=4,r=0` perfect-matching mechanism and remains a mandatory negative control.

This note completes the four-defect switching regime inside the already established full tight-antipode Boolean normal form. The lopsided no-pair ray and all isolated-pair four-defect states were already closed. The only remaining states were the finite-width no-pair strips with at least two nonempty pendant groups.

---

## 1. Setup

Let a switched graph `L` on the `k` antipode fibres have exactly four non-leaf coordinates. Call them

\[
E=\{e_1,e_2,e_3,e_4\}.
\]

With no isolated leaf-pairs, every leaf lies in a pendant group `D_i` attached to `e_i`. Write the sorted attachment sizes

\[
w\le x\le y\le z,
\qquad
k=4+w+x+y+z.
\]

The general leaf-package theorem gives

\[
B_4=2\sum_i(p_i-1)_+ +2\sum_{i<j}\min(p_i,p_j),
\]

and, after sorting,

\[
B_4=2S-2g+6w+4x+2y,
\]

where `S=w+x+y+z` and `g` is the number of nonempty groups.

An above-`M(n)` full-tight graph has `a<=2k`, so the leaf-package inequality leaves only:

- `g=1`: `(0,0,0,z)`;
- `g=2`: `(0,0,y,z)`, `1<=y<=6`;
- `g=3`: `(0,x,y,z)` with `(x,y)` in
  `{(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3)}`;
- `g=4`: `(w,x,y,z)` with `(w,x,y)` in
  `{(1,1,1),(1,1,2),(1,1,3)}`.

The `g=1` ray was already classified: only two exceptional cores have `tau(Omega)<=2k`, and F-separation closes those from `k>=19`. The goal here is to eliminate every nonlopsided strip by support alone.

---

## 2. Separate the leaf package from a residual core-witness graph

Let `V_leaf` be the set of orientation codes occurring on quotient pairs whose two coordinates are leaves. The subgraph induced by those physical edges has exact cover number `B_4` by the general leaf-package theorem.

Now delete all vertices in `V_leaf`. From the remaining orientation-code graph retain only physical edges of two kinds:

1. quotient pairs between two exceptional coordinates;
2. quotient pairs between an exceptional coordinate and one fixed representative leaf from each nonempty pendant group.

Call the resulting graph `Gamma`.

`Gamma` is vertex-disjoint from the leaf-package subgraph by construction. Therefore any vertex cover of the full orientation-code graph restricts independently to covers of those two subgraphs, and any matching in `Gamma` gives

\[
\boxed{\tau(\Omega)\ge B_4+\nu(\Gamma).} \tag{2.1}
\]

The forced code formula makes `Gamma` completely explicit. If `x_i` is the chosen representative of `D_i` and `q` is exceptional, then the orientation code of the leaf source is, modulo the complementary physical copy,

\[
\{e_i,q\},
\]

while the exceptional-source code is

\[
N_L(q)\triangle\{x_i\}.
\]

Exceptional-exception quotient pairs use the same formula

\[
N_L(q)\triangle\{q'\}.
\]

Thus after the attachment-status pattern is fixed, the only finite freedom in `Gamma` is the graph induced by `L` on the four exceptional coordinates.

---

## 3. Ray-extension lemma

The diagnostic scan from the previous unit suggested that the exceptional-core increment is constant as the largest group grows. This is not merely empirical.

> **RAY-EXTENSION LEMMA.** Fix the exceptional four-vertex core and all pendant groups except the largest group `D_r`. Choose the representative of `D_r` once. If one new leaf `u` is added to `D_r`, every matching in the old residual core-witness graph `Gamma` remains a matching in the new one.

### Proof

The old coordinate set embeds naturally in the new one. The only old orientation codes whose bit pattern changes are codes sourced at the parent `r`: each such code gains the new coordinate `u`, because `u` is added to `N_L(r)`. Codes sourced anywhere else, and the small leaf-source codes `{e_i,q}`, do not contain `u`.

Hence two previously distinct old code vertices cannot merge:

- if both are sourced at `r`, both gain the same new coordinate, preserving inequality;
- if neither is sourced at `r`, neither changes;
- if exactly one is sourced at `r`, the new code contains `u` and the other does not.

The same argument applies to the complementary physical copy. Every old residual edge therefore survives with distinct endpoints, and every old vertex-disjoint matching remains vertex-disjoint. ∎

Meanwhile increasing the largest attachment by one increases `B_4` by exactly two and also increases `2k` by exactly two. Therefore any positive support excess proved at one base value of `z` persists along the entire ray.

This is the structural explanation of the previously observed `+2` ray behaviour.

---

## 4. Finite exceptional-core matching lemma

The only remaining finite object is the four-vertex exceptional core. There are `2^6=64` labelled core graphs, with invalid ones discarded when an allegedly exceptional coordinate would actually have degree one in the whole switched graph.

Direct use of the forced-code formula above gives the following matching bounds for `Gamma`.

> **FOUR-DEFECT CORE MATCHING LEMMA — finite certificate.**
>
> For every valid exceptional core:
>
> - `g=2`, smaller pendant size `y=1`: `nu(Gamma)>=12`;
> - `g=2`, `2<=y<=6`, once `z>=3`: `nu(Gamma)>=14`;
> - every surviving `g=3` strip: `nu(Gamma)>=20`;
> - every surviving `g=4` strip: `nu(Gamma)>=18`.

This is a genuinely finite lemma, not an extrapolation in `z`. The accompanying proof-producing checker reconstructs `Gamma` from the forced-code formula, deletes the exact leaf-package vertex set, and constructs an explicit vertex-disjoint matching by the deterministic rule “match a minimum-degree live vertex to a minimum-degree neighbour.” It verifies 556 valid labelled core/base-pattern instances. The smallest matching produced in each row is exactly the claimed bound.

Files:

- `check_four_defect_no_pair_core_matching.py`;
- `FOUR_DEFECT_NO_PAIR_CORE_MATCHING_CHECK_SUMMARY.json`.

The unbounded `z` direction is **not** checked numerically: it is supplied by the Ray-Extension Lemma.

For external presentation, the 64-core finite lemma can still be compressed by hand into rooted four-vertex isomorphism types; this is a presentation cleanup, not an unresolved infinite case.

---

## 5. Support exclusion of every nonlopsided no-pair strip

### 5.1 Two nonempty groups

Write the attachment sizes as `(0,0,y,z)`.

The exact leaf contribution is

\[
B_4=2z+4y-4.
\]

Since

\[
2k=2z+2y+8,
\]

for `y=1`, the matching lemma gives

\[
\tau(\Omega)\ge B_4+12=2k+2.
\]

For `2<=y<=6`, using the bound `14`,

\[
\tau(\Omega)\ge B_4+14=2k+(2y+2)>2k.
\]

Thus every `g=2` strip is support-impossible above threshold.

### 5.2 Three nonempty groups

Write `(0,x,y,z)`. Then

\[
B_4=2z+6x+4y-6.
\]

Adding the core matching bound `20` gives

\[
\tau(\Omega)-2k
\ge 4x+2y+6>0.
\]

Hence every surviving `g=3` strip is support-impossible.

### 5.3 Four nonempty groups

Write `(w,x,y,z)`. Then

\[
B_4=2z+8w+6x+4y-8.
\]

Adding the core matching bound `18` gives

\[
\tau(\Omega)-2k
\ge 6w+4x+2y+2>0.
\]

Hence every surviving `g=4` strip is support-impossible.

So every no-pair four-defect state with at least two nonempty pendant groups has `tau(Omega)>2k` throughout its eventual ray.

---

## 6. Complete four-defect conclusion

The previous units established:

1. every four-defect state with an isolated leaf-pair is support-impossible from `k>=13`;
2. the no-pair lopsided ray `g=1` is below `M(n)` from `k>=19` by exact core classification plus F-separation.

Section 5 eliminates every remaining no-pair nonlopsided strip by support alone.

Therefore:

> **COMPLETE FOUR-DEFECT SWITCHING EXCLUSION — internal candidate.** If a full tight-antipode switching class contains a state with exactly four non-leaf coordinates and `k>=19`, then
>
> \[
> \boxed{m\le M(n).}
> \]

Equivalently, an above-`M(n)` full-tight counterexample with `k>=19` cannot have a switched state with zero, one, two, three, or four non-leaf coordinates, apart from the already isolated finite lower-order mechanisms outside the stated ranges.

The threshold `19` comes from the previously closed lopsided `K_4` exceptional-core state; the new nonlopsided strips are eliminated by support before F-separation is needed.

---

## 7. Strategic consequence

The leaf-defect hierarchy now extends one complete layer farther:

- one defect: eventually closed;
- two defects: eventually closed from `k>=14`;
- three defects: eventually closed from `k>=15`;
- **four defects: internally closed from `k>=19`.**

The important reusable idea is not the number `19`; it is the decomposition

\[
\text{leaf package} + \text{finite residual core witness}
\]

together with ray extension. For fixed defect count `d`, the general leaf-package theorem bounds every attachment except the largest, while the Ray-Extension Lemma shows that a matching certificate at one base point persists along the unbounded ray.

This reduces every fixed-`d` switching problem to finitely many exceptional-core matching problems.

The natural next test is `d=5`. If the residual core matching already forces `tau(Omega)>2k` in every five-defect ray, then five defects will be easier than four: support alone will close the whole layer and no F-separation cleanup will be needed.

---

## 8. Trust boundary

- The leaf-package and ray-extension lemmas are hand structural arguments.
- The four-coordinate residual matching lemma is finite and proof-producing, but presently certified by an explicit exact checker rather than compressed into a short isomorphism-class proof. It is therefore retained as an internal theorem candidate, not promoted as externally reviewed mathematics.
- The `k=4`, order-12/32 `X_3` residual-zero obstruction is outside the theorem scope and remains untouched.
- No all-order second-extremal statement is claimed.
