# Residual-one k=2 F0 H/Y polarization

Date: 2026-09-20

Status: **same-session conditional structural theorem**, downstream of the audited rigid one-code residual-one interface, `k=2`, `J2=empty`, the preserved `W_s--U_{bar d}` anticompleteness, and the F0 private-spoke theorem. No finite scan is used.

This is the direct follow-on to `ONE_CODE_R1_K2_F0_Y_FORWARD_BRANCH_CORRECTION.md`. It closes the specific pure-F0 high-Y endpoint much more strongly than the corrected population-capacity bound: an F0 escape cannot simultaneously have a genuine H-neighbourhood and more than one Y-neighbour.

## 1. Statement

Let `t in U\W_s` be fully free with respect to the selected rigid pair:

`N_K(t)=empty`,

`N_{W_s}(t)=empty`.

Assume `p>=3` and `J2=empty` in the residual-one `k=2` branch.

Then

> **`d_H(t)>0  =>  d_Y(t)<=1`.**                         `(HY-POL)`

Equivalently every F0 vertex belongs to one of two located-defect arms:

- H-anticomplete; or
- Y-sparse, with at most one Y-neighbour.

Consequently, for any F0 set F,

> **`Z_{H,F}+Z_{Y,F} >= |F| min{|H|,y-1}`.**            `(HY-BILL)`

On the exact q=1 low-k ray, `|H|=p-1` and `y=p-1`, so

> **`Z_{H,F}+Z_{Y,F} >= |F|(p-2)`.**                    `(HY-RAY)`

This is a located A--U defect bill, disjoint from missing U--U pairs inside the compressed proper-support reservoir.

## 2. Proof: take an F0 vertex with an H-neighbour

Suppose `h_i in N_H(t)`. We show that `t` cannot have two Y-neighbours.

Assume for contradiction that `y0,y1 in N_Y(t)` are distinct. Consider the edge `t y0`.

Because Y is complete to H, the path

`t--h_i--y0`

shows that `t y0` lies in a triangle. Therefore raw triangle-edge criticality yields one of the two singleton orientations.

## 3. Orientation sourced at t is impossible

Suppose first that there is a witness r with

`r in N(y0)\N[t]`,

`N(t) cap N(r)={y0}`.                                    `(HY-F)`

Since `t in U`, every witness in the rooted B-neighbourhood shares the root v with t. The head `y0` lies in A, so v would be an extra common neighbour. Thus r must lie in A.

If `r in X`, then X is complete to Y. Both `y0` and the second Y-neighbour `y1` are common neighbours of t and r, contradicting `(HY-F)`.

If `r in Y`, then r is adjacent to every H-vertex. The chosen `h_i` is therefore a common neighbour of t and r distinct from `y0`, again contradicting `(HY-F)`.

Hence the t-sourced orientation is impossible.

## 4. Orientation sourced at y0 forces a full-support `bar d` witness

The remaining orientation has a witness w with

`w in N(t)\N[y0]`,

`N(y0) cap N(w)={t}`.                                    `(HY-R)`

The root and all matched endpoints are excluded as witnesses:

- the root has the p matched endpoints selected by y0 as extra common neighbours;
- a private endpoint `q_l` has its matched head `h_l`, which is adjacent to every Y-vertex;
- the residual hub `q_j` has K-neighbours, again adjacent to every Y-vertex.

Thus w lies in `A union U`.

Because the head t lies in U, y0 and w may share no matched endpoint. Since `c(y0)=d`, this forces

> `c(w)=bar d`.                                          `(HY-CODE)`

At `J2=empty`, the A-code repertoire consists only of

- d on Y;
- `d xor e_j` on K;
- `d xor e_l` on `h_l`, `l in I`.

For `p>=3`, none equals `bar d`. Therefore

> `w in U_{bar d}`.                                      `(HY-U)`

The selected witnesses W_s cannot serve as w because their K-head would be an extra common neighbour of y0 and w. Hence `w in U_{bar d}\W_s`.

Also Y is complete to X, so `(HY-R)` forces

> **`N_X(w)=empty`.**                                    `(HY-X0)`

By the preserved `W_s--U_{bar d}` anticompleteness, w is itself an F0 vertex.

## 5. Full private support plus X-anticompleteness makes the reverse orientation impossible

The code `bar d` differs from d on every private coordinate `i in I`. Hence w is adjacent to every private endpoint `q_i`.

Apply the already-proved F0 private-spoke theorem to each edge `wq_i`.

Its reverse private-spoke orientation would require an H-witness adjacent to w. That is impossible by `(HY-X0)`. Therefore every private spoke of w is forced into the forward orientation:

> **`N(w) cap N(h_i)={q_i}` for every `i in I`.**        `(HY-PRIVATE)`

Return now to the original chosen H-neighbour `h_i of t`. The reverse F0--Y certificate `(HY-R)` has `wt in E`. By assumption `th_i in E`. Thus t is a common neighbour of w and h_i.

But `(HY-PRIVATE)` says their unique common neighbour is `q_i`. Since `t!=q_i`, contradiction.

Therefore the y0-sourced orientation is also impossible.

The assumed edge `ty0` cannot be critical, contradicting diameter-2-criticality. Hence an F0 t with any H-neighbour has at most one Y-neighbour, proving `(HY-POL)`.

## 6. Located-defect corollary

For each `t in F`:

- if `d_H(t)=0`, t contributes all `|H|` missing H--t pairs;
- if `d_H(t)>0`, `(HY-POL)` gives at least `y-1` missing Y--t pairs.

These are distinct physical A--U pairs for different t, so summing yields `(HY-BILL)`.

On the exact low-k ray `|H|=y=p-1`, the smaller arm is `p-2`, giving `(HY-RAY)`.

## 7. Consequence for the predecessor pure-F0 equality normal form

The predecessor compressed half-barrier equality required almost every F0 escape to be simultaneously

- H-near-complete;
- Y-near-complete;
- K-free and W_s-free.

`(HY-POL)` rules this out **exactly**, not merely at leading coefficient. An H-near-complete F0 vertex has an H-neighbour, hence has at most one Y-neighbour; it cannot be Y-near-complete when `y` grows.

Thus the coefficient-1/2 pure-F0 endpoint is no longer merely redirected to a positive-density certificate reservoir. It is structurally impossible in the `J2=empty`, high-y residual-one branch.

This also supersedes the need to optimize the golden witness split: the earlier forward branch was invalid, and the surviving reverse branch collides with the private-coordinate fan before any golden-ratio endpoint can arise.

## 8. What remains open

This theorem does **not** close the whole residual-one k=2 branch. The global minimizer can migrate away from pure F0 toward D1, mixed, K-heavy, hub-neighbour, full-support, or low-y geometry and pay the associated departure costs.

The next useful synthesis should insert `(HY-BILL)` into the compressed class optimization while keeping

- proper-support missing-U cost;
- K-heavy Y-capacity;
- D1 complement capacity;
- mixed slack;
- hub/support departure penalties;
- exact weighted rooted currencies

separate. For `y=o(p)`, the correct next route remains the large-gap / rooted residual ledger rather than the high-y F0 argument.

Global audit caveat unchanged: no positive actual-D2C rigid complete Hall-cut fixture with `x>=3` is known in the bounded graph-level regression.