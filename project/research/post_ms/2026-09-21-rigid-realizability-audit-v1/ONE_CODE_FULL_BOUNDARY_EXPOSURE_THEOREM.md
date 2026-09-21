# Rigid one-code cuts with at least two matched-selected heads: full boundary exposure and forward-only routing

Date: 2026-09-21

Status: raw realizability theorem inside the rigid complete one-code interface. **21 September strengthened correction:** for a one-code outside block of multiplicity `y>=2`, the X-reverse boundary arm is impossible altogether. The resulting theorem is substantially stronger than the earlier reverse-gamma alternative and supersedes any downstream treatment that allowed reverse-only coordinates for such a block.

## 1. Setup

Let `Y=A_d` be the one-code outside block of a rigid complete cut, with `y=|Y|`. Suppose at least two X-heads are supplied by distinct tight matched coordinates. Write the selected matched-head coordinates as S, `|S|=m>=2`.

For each `i in S`, the corresponding matched-selected head has code

`d xor e_i`.

## 2. Full exposure

### Theorem 2.1

If `m>=2`, then

> **`I(d,X)=[p]`.**                                      `(2.1)`

For a coordinate outside S, every matched-selected head agrees with d there. For a coordinate `j in S`, any other selected head agrees with d at j. Hence every tight coordinate is exposed.

Moreover every selected coordinate is nonuniversal because its own head disagrees with d there, so

> `C(d,X) subseteq [p]\S`, hence `|C|<=p-m`.             `(2.2)`

## 3. If y>=2, reverse is impossible everywhere

The corrected boundary theorem proves that when the outside code class contains at least two vertices, no X-reverse certificate can exist on any exposed boundary edge. Indeed, source `q_i^{d_i}` and every witness in X share all of Y as common neighbours, not a singleton.

Therefore for `y>=2` every one of the p exposed coordinates must be covered by either

1. U-forward support, or
2. matched-forward support.

The global matched-leaf theorem gives at most two coordinates of the second type.

## 4. Complementary witness-class refinement

Fix a minimum outside source and let k be its number of selected U-witnesses. All k have code `bar d`. Put

`e=u-k`.

A boundary U-forward witness has code `bar d xor e_i`, never `bar d`, so none of the mandatory k complementary witnesses can populate a boundary one-match class. Distinct boundary coordinates require distinct one-match U-code classes. Therefore at most e coordinates can be U-forward.

The preserved one-code occupancy identity is

`m=p-c+e`.

Writing

`r=p-m`

for the residual matched-coordinate dimension gives

> **`e=c-r`.**                                            `(4.1)`

### Theorem 4.1 — repeated one-code boundary obstruction

For every rigid complete one-code cut with

- `m>=2`, and
- `y>=2`,

one necessarily has

> **`p <= c-r+2`.**                                      `(4.2)`

Equivalently,

> **`c >= p+r-2`.**                                      `(4.3)`

This is a pure graph-realizability condition. It does not use the score ceiling, rooted-Q inequality, pair-local Hall capacity, gamma-collision theorem, or the audit-sensitive source-tuple capacity theorem.

If `C(d,X)=empty`, matched-forward support vanishes and the bound sharpens to

> **`p<=c-r`, equivalently `c>=p+r`.**                   `(4.4)`

Thus the rooted gap c must be essentially as large as the tight dimension plus the residual dimension before a repeated one-code rigid cut can even realize its B--A boundary edges.

## 5. What happened to the reverse-gamma branch

Earlier same-session notes allowed coordinates with no forward support to be “reverse-only” provided X contained a large enough forced gamma class. That was too weak for repeated outside codes.

For `y>=2` the reverse arm is not expensive; it is **impossible**. The reason is physical and immediate: any X-witness and the matched source `q_i^{d_i}` share every vertex of the same-code class Y.

Therefore all reverse-gamma multiplicity calculations for a one-code block with `y>=2` are now superseded as possible realization channels. They may remain relevant only for singleton outside code classes (`y_d=1`) in a multi-code setting.

## 6. Residual-one consequence

For residual dimension one, `r=1` and `m=p-1>=2`. Hence every repeated one-code residual-one realization satisfies

> **`c>=p-1`.**                                          `(6.1)`

If the residual coordinate is nonuniversal (`C=empty`, as happens whenever at least one residual-code K-head is present), then

> **`c>=p+1`.**                                          `(6.2)`

The corrected intermediate half-ray has `p=2t`, `c=t`, `r=1`, `y=t>=4`, and `C=empty`. It violates `(6.2)` for every t, so the entire half-ray is impossible without any score calculation.

## 7. Large-gap scalar escape family is also unrealizable

The preserved scalar diagnostic family had

`p=3t, c=2t, m=2t, r=t, y=t`.

For every `t>=2`, Theorem 4.1 would require

`3t <= 2t-t+2=t+2`,

which fails for `t>=2`.

Hence:

> **the large-gap scalar escape family is not a literal graph-realizability escape.**

Its survival of the old scalar score package reflected a missing boundary-criticality constraint, not a genuine candidate geometry.

This is strategically important: both of the principal explicit one-code scalar escape families preserved on 20 September are now killed by the same raw boundary mechanism.

## 8. Remaining one-code regimes

For a repeated one-code outside block (`y>=2`) with `m>=2`, there are no reverse-only coordinates. The only way to survive is to have a boundary U-forward reservoir of size at least `p-2`, i.e.

`e=c-r>=p-2`,

with at most two coordinates delegated to matched leaves.

Therefore the live one-code frontier is compressed to:

1. **very large rooted gap:** `c>=p+r-2`;
2. the small matched-head cases `m<=1`;
3. singleton outside blocks `y=1`, where the reverse arm may still exist.

These are the correct next branches to intersect with the rooted residual defect `delta`, triangle count Q, and exact pair-local Hall machinery.

## 9. Scope

This is a necessary condition conditional on the rigid complete one-code interface. It does not prove that the interface is reachable from an arbitrary D2C graph. Bounded actual-D2C regression still has zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control.
