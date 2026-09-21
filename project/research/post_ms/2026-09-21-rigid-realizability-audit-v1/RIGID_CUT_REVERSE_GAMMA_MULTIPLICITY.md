# Reverse-gamma multiplicity obstruction — corrected scope

Date: 2026-09-21

Status: **scope-corrected / partially superseded.** The same-session theorem `RIGID_CUT_BOUNDARY_CODE_EDGE_TRICHOTOMY.md` has now been strengthened: if an outside code class `Y_d` has multiplicity at least two, the X-reverse arm is impossible outright. Therefore the reverse-gamma multiplicity machinery below is relevant only to **singleton outside code classes `y_d=1`**. Earlier wording that treated reverse-only coordinates with `y_d>=2` as a live realization channel is superseded.

## 1. Why repeated outside codes have no reverse-only coordinates

Fix `y in Y_d` and an exposed coordinate i. An X-reverse witness w would have to satisfy

`N(q_i^{d_i}) cap N(w)={y}`.

But w lies in X and the rigid cut is complete, so w sees every vertex of `Y_d`. The matched source `q_i^{d_i}` also sees every vertex of `Y_d`, because they all have bit `d_i` at coordinate i. Thus

`Y_d subseteq N(q_i^{d_i}) cap N(w)`.

Hence if `y_d>=2` the required singleton is impossible.

Therefore

> **`y_d>=2 => R_d^rev=empty`.**                         `(1.1)`

All exposed coordinates for a repeated outside code must be U-forward or matched-forward.

## 2. Singleton outside code: reverse-gamma multiplicity remains valid

Now assume `y_d=1`. Reverse-only coordinates may exist. Let

`R_d^rev=I(d,X)\(U_0(d,X) union L(d,X))`, `r=|R_d^rev|`.

For each reverse-only coordinate i, the witness lies in the forced class `X_{gamma_i}`. Since `y_d=1`, nonemptiness is the only class-size requirement.

Let s be the number of distinct occupied forced gamma classes among these r coordinates. Certainly `s<=x`. Pigeonhole gives a gamma class repeated on at least

`g>=ceil(r/s)>=ceil(r/x)`

coordinates. The preserved gamma-collision theorem then yields `L_A>=g(g-1)` for `g>=3`.

Thus the former score-based multiplicity bound remains a legitimate, though weak, tool for singleton outside code classes.

## 3. Global support split after correction

For every represented outside code d:

- if `y_d>=2`, **only the two forward mechanisms exist**;
- if `y_d=1`, U-forward, matched-forward and X-reverse are all potentially available.

The global matched-leaf theorem still gives at most two matched-forward heads. Distinct U-forward coordinates still require distinct one-match U-code classes.

Therefore, for repeated outside code classes,

> **`|I(d,X)| <= |U_0(d,X)|+2 <= u+2`.**                `(3.1)`

In the one-code branch, retaining the minimum-source complementary witness class improves u to the escape reservoir `e=u-k=c-r`.

## 4. Superseded statements

The earlier same-session formulas

`r <= floor(x/y_d)G(C0)`

for general `y_d`, and the corresponding “large reverse class versus U-forward” alternative for a repeated one-code block, are no longer the right live statements. For `y_d>=2`, reverse-only coordinates do not exist, so those inequalities are merely vacuous weakenings and must not be used to preserve a parameter family that fails the forward population test.

In particular:

- the corrected intermediate half-ray is killed outright by forward population;
- the preserved large-gap scalar escape family is also killed outright once full exposure and the escape-reservoir count are applied.

## 5. Live use

Keep gamma multiplicity only for singleton outside code classes. For repeated one-code blocks, use `ONE_CODE_FULL_BOUNDARY_EXPOSURE_THEOREM.md`, whose live condition is

`p<=c-r+2`

when `m>=2,y>=2`, sharpened to `p<=c-r` when there is no matched-forward support.

This correction is a material strengthening of the raw realizability audit and should supersede the earlier reverse-gamma branch in CURRENT_STATE and README summaries.
