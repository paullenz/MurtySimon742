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

## 5. Exact universal-coordinate refinement

Let `L=L(d,X)` be the set of heads with matched-forward support. The global matched-leaf theorem gives more than the coarse `|L|<=2`:

- if `|C|=0`, then `|L|=0`;
- if `|C|=1`, then `|L|<=1`;
- if `|C|=2`, then `|L|<=2`, and equality requires the two universal coordinates to form an isolated `K_2` in the matched-row graph;
- if `|C|>=3`, then `|L|=0`, because every universal coordinate already has at least two neighbours inside the clique `R_d[C]` and therefore cannot be a global leaf.

Since every one of the p exposed coordinates is U-forward or matched-forward,

> **`p <= c-r+|L|`.**                                    `(5.1)`

Hence the exact case split is

> **`|C|=0 or |C|>=3  =>  c>=p+r`;**                    `(5.2)`
>
> **`|C|=1             =>  c>=p+r-1`;**                  `(5.3)`
>
> **`|C|=2             =>  c>=p+r-2`,**                  `(5.4)`

and equality in `(5.4)` requires the universal pair to be an isolated matched-row `K_2`.

The previously stated coarse theorem

> **`c>=p+r-2`**                                         `(5.5)`

is therefore sharp only at this exceptional two-universal-coordinate geometry. Generically (`|C|=0` or at least 3), the stronger exact requirement is `c>=p+r`.

This is a pure graph-realizability condition. It does not use the score ceiling, rooted-Q inequality, pair-local Hall capacity, gamma-collision theorem, or the audit-sensitive source-tuple capacity theorem.

## 6. What happened to the reverse-gamma branch

Earlier same-session notes allowed coordinates with no forward support to be “reverse-only” provided X contained a large enough forced gamma class. That was too weak for repeated outside codes.

For `y>=2` the reverse arm is not expensive; it is **impossible**. The reason is physical and immediate: any X-witness and the matched source `q_i^{d_i}` share every vertex of the same-code class Y.

Therefore all reverse-gamma multiplicity calculations for a one-code block with `y>=2` are superseded as possible realization channels. They may remain relevant only for singleton outside code classes (`y_d=1`) in a multi-code setting.

## 7. Residual-one consequence

For residual dimension one, `r=1` and `m=p-1>=2`.

- If the residual K class is nonempty, the residual coordinate is nonuniversal and every private coordinate is also nonuniversal, so `C=empty` and `(5.2)` gives

  > **`c>=p+1`.**                                        `(7.1)`

- If the K class is absent, the residual coordinate is the only possible universal coordinate, so `|C|<=1` and `(5.3)` gives

  > **`c>=p`.**                                          `(7.2)`

The corrected intermediate half-ray has `p=2t`, `c=t`, `r=1`, `y=t>=4`, and a nonempty K class. It violates `(7.1)` for every t, so the entire half-ray is impossible without any score calculation.

## 8. Large-gap scalar escape family is also unrealizable

The preserved scalar diagnostic family had

`p=3t, c=2t, m=2t, r=t, y=t`.

For every `t>=2`, even the weakest exceptional bound `(5.4)` requires

`2t=c >= p+r-2=4t-2`,

which fails. Hence:

> **the large-gap scalar escape family is not a literal graph-realizability escape.**

Its survival of the old scalar score package reflected a missing boundary-criticality constraint, not a genuine candidate geometry.

This is strategically important: both of the principal explicit one-code scalar escape families preserved on 20 September are now killed by the same raw boundary mechanism.

## 9. Remaining one-code regimes

For a repeated one-code outside block (`y>=2`) with `m>=2`, there are no reverse-only coordinates. The live frontier is compressed to:

1. **very large rooted gap:** generically `c>=p+r`, with only the exceptional `|C|=1,2` relaxations above;
2. the small matched-head cases `m<=1`;
3. singleton outside blocks `y=1`, where the reverse arm may still exist.

The exceptional `|C|=2` equality geometry is especially rigid: the two universal coordinates must form an isolated matched-row edge. It should be kept subordinate unless the rooted residual ledger actually drives a survivor into that face.

These are the correct next branches to intersect with the residual defect `delta`, rooted triangle count Q, and exact pair-local Hall machinery.

## 10. Scope

This is a necessary condition conditional on the rigid complete one-code interface. It does not prove that the interface is reachable from an arbitrary D2C graph. Bounded actual-D2C regression still has zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control.
