# Rigid one-code cuts with at least two matched-selected heads: full boundary exposure

Date: 2026-09-21

Status: raw realizability theorem inside the rigid complete one-code interface. It generalizes the residual-one population obstruction to arbitrary residual matched-coordinate dimension and uses only the post-audit boundary trichotomy, the global matched-leaf collapse, and the independently audited singleton-head witness location.

## 1. Setup

Let `Y=A_d` be the one-code outside block of a rigid complete cut. Suppose at least two X-heads are supplied by distinct tight matched coordinates. Write the selected matched-head coordinates as S, `|S|=m>=2`.

For each `i in S`, the corresponding matched-selected head has code

`d xor e_i`.

Let `I(d,X)` and `C(d,X)` be the exposed and universal coordinate sets of the boundary trichotomy.

## 2. Full exposure

### Theorem 2.1

If `m>=2`, then

> **`I(d,X)=[p]`.**                                      `(2.1)`

### Proof

Fix a tight coordinate j.

- If `j notin S`, every matched-selected head `d xor e_i` with `i in S` agrees with d at j.
- If `j in S`, choose another selected coordinate `i in S`, `i!=j` (possible because m>=2). The head `d xor e_i` agrees with d at j.

Thus every coordinate has some X-head agreeing with d. `square`

Moreover every selected coordinate is nonuniversal because its own head `d xor e_i` disagrees with d there. Therefore

> **`C(d,X) subseteq [p]\S`, so `|C|<=p-m`.**            `(2.2)`

## 3. Population consequence

The global matched-leaf theorem gives `|L(d,X)|<=2`.

Let `rho=max_c |X_c|` be the largest X-code-class multiplicity.

At a coordinate with no matched-forward support, at most rho Y-heads can reverse-certify because the forced reverse witnesses all lie in one X-code class and fixed-source injectivity makes distinct Y-heads require distinct physical witnesses.

Hence if

> **`y>rho`,**                                            `(3.1)`

then every one of the `p-|L|` nonmatched coordinates requires a U-forward witness. Different coordinates require different one-match U-code classes `bar d xor e_i`. Therefore

> **`p-|L|<=u`.**                                        `(3.2)`

Using `|L|<=2`:

### Corollary 3.1 — full-exposure population obstruction

For every rigid complete one-code cut with `m>=2` and `y>rho`,

> **`p<=u+2`.**                                          `(3.3)`

If `C=empty`, matched-forward support vanishes and this sharpens to

> **`p<=u`.**                                            `(3.4)`

## 4. Complementary witness-class refinement

The direct singleton-head audit gives more than the crude u-capacity. Fix a minimum outside source of code d and let k be its number of selected U-witnesses. Every one of those k witnesses has code `bar d`. Put

`e=u-k`,

the number of U-vertices outside this mandatory complementary code class.

A boundary U-forward witness has code `bar d xor e_i`, never `bar d`. Therefore none of the k mandatory complementary witnesses can populate a boundary one-match class. Consequently the number of coordinates with any U-forward support is at most e, not merely u.

### Theorem 4.1 — escape-reservoir boundary bound

For a rigid complete one-code cut with `m>=2`,

> **at most `e=u-k` exposed coordinates can use the U-forward arm.** `(4.1)`

Combining with the global matched-leaf bound and reverse-gamma multiplicity gives

> **`p <= e+2+floor(x/y) G(C0)`**                        `(4.2)`

for an above-M candidate whenever reverse-only coordinates occur; if `y>x`, the reverse-only arm is impossible and

> **`p<=e+2`.**                                          `(4.3)`

If additionally `y>rho`, every nonmatched coordinate must U-forward, so

> **`p<=e+2`;**                                           `(4.4)`

and if `C=empty`,

> **`p<=e=u-k`.**                                        `(4.5)`

The preserved one-code occupancy theorem gives the independent exact bound

> **`0<=e=u-k<=c`.**                                     `(4.6)`

Therefore `(4.2)` has the coarser but parameter-only consequence

> **`p<=c+2+floor(x/y)G(C0)`.**                          `(4.7)`

If `y>rho`, then

> **`p<=c+2`;**                                           `(4.8)`

and if also `C=empty`,

> **`p<=c`.**                                             `(4.9)`

Thus whenever the rooted gap c is substantially smaller than p, literal realizability forces a large reverse X-code class (`rho>=y`) and a correspondingly heavy reverse-gamma channel. The old scalar theory could not see this because it treated the selected `U_bar d` population as if it remained available for arbitrary boundary routing.

## 5. Reverse-gamma alternative

When large reverse classes exist, `(4.2)` makes the physical dichotomy explicit. Full exposure gives p boundary coordinates, but only

- e coordinates can be routed through one-match U-forward classes;
- at most two can use matched leaves;
- all remaining coordinates are reverse-only and must be absorbed by X gamma classes of size at least y.

Repeated use of those gamma classes incurs the gamma-collision A-slack bill. There is no fourth aggregate-capacity channel.

This is exactly the interface missing from the earlier scalar near-rigid escape analysis: the large selected class `U_bar d` consumes unmatched population but cannot help with boundary U-forward routing.

## 6. Relation to residual-one closure

Residual dimension one has `m=p-1>=2`, so full exposure is automatic. On the corrected intermediate half-ray the minimum outside source has the two selected complementary witnesses, hence `k=2` and `e=u-k=t-1`. Every X reverse class has size at most two while `y=t>=4`, and `C=empty`; `(4.5)` would require

`2t=p<=t-1`,

an immediate contradiction. Thus the pure half-ray closure is even stronger when the mandatory complementary witness class is retained explicitly.

## 7. Relation to the large-gap scalar escape family

For the preserved diagnostic family

`p=3t, u=4t, k=3t, y=t, x=5t`,

one has only

`e=u-k=t`

vertices available outside `U_bar d`. Since `m=2t>=2`, all p=3t boundary coordinates are exposed. Hence at least

> **`p-e-2=2t-2`**                                      `(7.1)`

coordinates must be reverse-only (up to the two matched-leaf exceptions).

Thus that scalar family remains only if X can supply linear reverse-gamma capacity to at least `2t-2` coordinates. With `floor(x/y)=5`, the reverse-gamma theorem forces a repeated gamma multiplicity at least

`ceil((2t-2)/5)`,

and therefore a corresponding collision bill. This does not by itself contradict the previously recorded scalar score ceiling, but it identifies a new literal physical requirement omitted from the old method diagnostic. Any future use of that family must carry this reverse-only load explicitly.

## 8. Scope

This is a necessary condition conditional on the rigid complete one-code interface. It does not assert that the interface itself is reachable from an arbitrary D2C graph. Bounded actual-D2C regression still has zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control.
