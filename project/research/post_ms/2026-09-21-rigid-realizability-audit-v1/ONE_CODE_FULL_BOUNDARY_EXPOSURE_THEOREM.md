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

Fix a minimum outside source of code d and let k be its number of selected U-witnesses. Every one of those k witnesses has code `bar d`. Put

`e=u-k`,

the number of U-vertices outside this mandatory complementary code class.

A boundary U-forward witness has code `bar d xor e_i`, never `bar d`. Therefore none of the k mandatory complementary witnesses can populate a boundary one-match class. Consequently the number of coordinates with any U-forward support is at most e, not merely u.

The preserved one-code occupancy identity is

`m=p-c+e`.

Writing

`r=p-m`

for the residual matched-coordinate dimension gives the exact relation

> **`e=c-r`.**                                            `(4.1)`

This is stronger than the coarse `e<=c`: every residual matched coordinate removes one unit from the boundary U-forward reservoir.

### Theorem 4.1 — residual-sensitive escape-reservoir bound

For a rigid complete one-code cut with `m>=2`,

> **at most `e=c-r` exposed coordinates can use the U-forward arm.** `(4.2)`

Combining with the global matched-leaf bound and reverse-gamma multiplicity gives

> **`p <= c-r+2+floor(x/y) G(C0)`**                      `(4.3)`

for an above-M candidate whenever reverse-only coordinates occur; if `y>x`, the reverse-only arm is impossible and

> **`p<=c-r+2`.**                                        `(4.4)`

If additionally `y>rho`, every nonmatched coordinate must U-forward, so

> **`p<=c-r+2`;**                                         `(4.5)`

and if `C=empty`,

> **`p<=c-r`.**                                           `(4.6)`

Thus when c is substantially smaller than `p+r`, literal realizability forces a large reverse X-code class (`rho>=y`) and a correspondingly heavy reverse-gamma channel.

Equivalently, irrespective of score, at least

> **`p-c+r-2`**                                           `(4.7)`

coordinates are reverse-only whenever this quantity is positive, except that the exact count may be larger if fewer than `c-r` one-match U classes are actually occupied.

This ties the raw boundary obstruction directly to the residual dimension r that appears in the eventual defect programme.

## 5. Reverse-gamma alternative

When large reverse classes exist, `(4.3)` makes the physical dichotomy explicit. Full exposure gives p boundary coordinates, but only

- `c-r` coordinates can be routed through one-match U-forward classes;
- at most two can use matched leaves;
- all remaining coordinates are reverse-only and must be absorbed by X gamma classes of size at least y.

Repeated use of those gamma classes incurs the gamma-collision A-slack bill. There is no fourth aggregate-capacity channel.

This is exactly the interface missing from the earlier scalar near-rigid escape analysis: the large selected `U_bar d` population consumes unmatched population but cannot help with boundary U-forward routing.

## 6. Relation to residual-one closure

Residual dimension one has `r=1`, so the exact boundary-forward reservoir is

`e=c-1`.

On the corrected intermediate half-ray `c=t`, hence `e=t-1`. Every X reverse class has size at most two while `y=t>=4`, and `C=empty`; `(4.6)` would require

`2t=p<=t-1`,

an immediate contradiction. Thus the pure half-ray closure is an instance of the general residual-sensitive theorem.

## 7. Relation to the large-gap scalar escape family

For the preserved diagnostic family

`p=3t, c=2t, m=2t`,

one has residual dimension `r=t` and therefore

`e=c-r=t`,

agreeing with the explicit `u-k` count. Since all p=3t boundary coordinates are exposed, at least

> **`p-e-2=2t-2`**                                      `(7.1)`

coordinates must be reverse-only.

With `x=5t,y=t`, `floor(x/y)=5`, so the reverse-gamma theorem forces a repeated gamma multiplicity at least

`ceil((2t-2)/5)`,

and therefore a corresponding collision bill. This does not by itself contradict the previously recorded scalar score ceiling, but it identifies a linear physical reverse-only load omitted from the old method diagnostic.

## 8. Scope

This is a necessary condition conditional on the rigid complete one-code interface. It does not assert that the interface itself is reachable from an arbitrary D2C graph. Bounded actual-D2C regression still has zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control.
