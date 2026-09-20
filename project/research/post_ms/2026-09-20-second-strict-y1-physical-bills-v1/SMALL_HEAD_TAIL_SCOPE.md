# Exact second-strict mixed y=1 — scope of the remaining small-head tail

Date: 2026-09-20

Status: **same-session scope reduction**, conditional on the rigid one-code setup.

After `LARGE_HEAD_Y1_FINITE_ORDER_CLOSURE.md`, every mixed y=1 configuration with `p>=2,x>=5` has order at most 33. The only potentially asymptotic y=1 work therefore lies outside that classification.

## 1. p=1 is impossible at the rigid one-code interface

The rigid one-code setup requires every X-code to be different from both

`d` and `bar d`.

When `p=1`, the Boolean code cube `{0,1}^p` has exactly the two codes `d` and `bar d`. There is no third code available for an X-vertex.

Since the branch has `x>=3`, it follows immediately that

> **the rigid one-code second-strict branch has no `p=1` configuration.** `(Y1-P1-EMPTY)`

Thus the remaining mixed y=1 tail automatically has `p>=2`.

## 2. Remaining head sizes

The large-head classification assumed `x>=5`. Therefore the only y=1 head counts not covered by the new finite-order theorem are

> **`x=3` or `x=4`.**                                     `(Y1-SMALL-X)`

The earlier exceptional-capacity inequality gives

`(H-1)(|S_0|-1)<=1`,

with at least `H>=x-2` outside-certified heads.

Consequently:

- for `x=4`, `H>=2`; if `|S_0|>=2`, the only non-singleton-support possibility is the exact corner `H=2`, `|S_0|=2`; otherwise `|S_0|=1` and much of the large-head code geometry should transfer;
- for `x=3`, `H>=1` and the capacity inequality alone does not force `|S_0|`.

Thus the remaining mixed-y1 problem is an explicit **two-head-size structural tail**, not an unclassified large-x family.

## 3. Next move

Treat the two sizes separately rather than weakening the large-head theorem:

1. `x=4`: split `|S_0|=1` from the single exceptional support corner `H=2,|S_0|=2`; reuse R/Fx/Fz criticality where its proofs do not use x>=5.
2. `x=3`: enumerate the raw certificate roles symbolically (not graph-isomorphism brute force) and derive direct score/rooted bounds on p and omega.

If both fixed-head tails admit finite order bounds, then—subject to adversarial replay—the entire exact unloaded second-strict layer will be finite-order and the eventual programme can move to the next buffer-defect/loaded branch.