# Residual-one k=2: all Y--U edges are triangular and the exact low-k ray is asymptotically closed

Date: 2026-09-20

Status: **same-session conditional theorem**, downstream of the rigid one-code residual-one interface, `k=2`, `J2=empty`, and the preceding same-session Y-independence / B0 source-collapse results. This theorem is not graph-level closure of the rigid interface. It closes only the exact low-k stress ray against an unbounded sequence. Independent hostile replay is required before promotion.

The bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.

## 1. Exact-ray parameters

Use

`u=x=p+1`, `y=|Y|=p-1`, `|H|=p-1`, `k=2`, `J2=empty`,

and

`C0=floor((3p^2+10p-4)/2)`.

Let

`B=B0={w in U_bar(d):d_H(w)=0}`,

`b=|B|`,

and `D=U\B`.

The predecessor chain gives:

- B is independent;
- B is Y-anticomplete;
- every U-source outside B has oriented U--U source capacity at most two;
- every H-positive escape has at most one Y-neighbour;
- `G[Y]` is independent.

## 2. Scope repair: every Y--U edge is actually triangular

The previous low-A-slack note correctly warned that the convenient two-orientation lemma is only automatic for triangle edges. In the present exact branch the missing triangle hypothesis can itself be proved.

> **THEOREM (YU-TRI). Every edge between Y and U lies in a triangle.**

Take `y in Y=A_d` and `t in U` with `yt in E`.

If `c(t) != bar d`, then there is a tight matched coordinate on which t and y choose the same matched endpoint. That endpoint is a common neighbour of y and t, so yt lies in a triangle.

If `c(t)=bar d`, there are two cases.

- If `d_H(t)=0`, then `t in B0`, but B0 is Y-anticomplete, contradicting `yt in E`.
- If `d_H(t)>0`, choose `h in H cap N(t)`. Since Y is complete to H, h is a common neighbour of y and t.

Thus every existing Y--U edge is triangular. `(YU-TRI)`

This resolves, rather than ignores, the triangle-scope blocker preserved in the preceding note.

## 3. High-Y vertices must use reverse B0 witnesses

Let `t in D` satisfy `d_Y(t)>=2`, and fix an edge `ty0`.

Because `yt` is triangular, raw triangle-edge criticality gives one of the two singleton orientations.

### Forward orientation from t is impossible

- a witness in the rooted B-layer shares the root with t;
- an X-witness is adjacent to every Y-vertex, hence to another Y-neighbour of t besides y0;
- a Y-witness cannot be adjacent to the singleton head y0 because `G[Y]` is independent.

So the forward orientation fails.

### Reverse orientation

The reverse witness w must have zero common matched endpoint with source y0 of code d, hence

`c(w)=bar d`.

The residual-one A-code repertoire contains no `bar d` class, so `w in U_bar(d)`. Since Y is complete to X, singleton common-neighbourhood forces

`N_X(w)=empty`.

In particular w is H-free, hence

> **`w in B0`.**                                           `(YU-B0W)`

For a fixed ordered pair `(y0,w)`, the singleton common-neighbour set is graph-fixed, so it can certify at most one head t.

Therefore, writing `D_2={t in D:d_Y(t)>=2}`,

> **`e(Y,D_2)<=|Y| |B|`.**                                `(YU-CAP)`

Vertices of `D\D_2` contribute at most `|D|` further Y--U edges.

## 4. Y-hole capacity bound

Since B is Y-anticomplete, its contribution to `Z_{Y,U}` is `b(p-1)`.

The potential Y--D pairs number `(p-1)|D|`. By `(YU-CAP)`,

`e(Y,D)<= (p-1)b+|D|`.

Thus the D-side Y-hole block satisfies

`Z_{Y,D} >= [(p-1)(|D|-b)-|D|]_+`.

Asymptotically, if

`eta=b/p`,

then

> **`Z_{Y,U}/p^2 >= eta+[1-2eta]_+-o(1)`**
>
> `=max{eta,1-eta}-o(1)`.                                 `(YU-HOLE1)`

Because `e(Y)=0`,

> **`L_Y/p^2 >= max{eta,1-eta}-o(1)`.**                  `(YU-L1)`

## 5. B0--D U-edge isolation creates a second Y-hole bound

Let

`C=e(B,D)`.

Choose one valid orientation of every U--U edge. Every D-source has total oriented U--U source capacity at most two. Hence all but `O(p)` of the B--D edges are sourced in B.

For `w in B`, let `o_w` be the number of its B-sourced cross edges. Each such edge `wt` uses a witness in `A_d=Y`, because the source code is `bar d`.

If y is the witness for `wt`, then

`N(w) cap N(y)={t}`.

Therefore y must be nonadjacent to every other D-neighbour of w. Distinct outgoing heads from the same w use distinct Y-witnesses.

If `q_w=d_D(w)`, the certificates sourced at w force at least

`o_w(q_w-1)>=o_w(o_w-1)`

Y--D nonedges.

A fixed Y--D nonedge `(y,t')` can be charged for at most b sources w, because a charge requires `wt' in E`. Hence

`b Z_{Y,D} >= sum_w o_w(o_w-1)`.

By Cauchy,

`sum_w o_w(o_w-1) >= O^2/b-O`,

where `O=sum_w o_w=C-O(p)`.

Normalize

`q=C/p^2`.

For `eta>0` this yields

> **`Z_{Y,D}/p^2 >= (q/eta)^2-o(1)`.**                   `(YU-HOLE2)`

Together with B's own Y-antichain,

> **`L_Y/p^2 >= eta+max{[1-2eta]_+,(q/eta)^2}-o(1)`.**   `(YU-L2)`

For `eta=0`, necessarily `q=0` and `(YU-L1)` gives the limiting value one.

## 6. Exact U-edge/source geometry

B is independent. All U--U edges not lying across B--D must be sourced in D, and D has only O(p) total source capacity. Therefore

> **`e(U)=C+O(p)`**,                                      `(YU-EUEDGE)`

so

`e(U)/p^2=q+o(1)`.

Physical cross capacity gives

> **`0<=q<=eta(1-eta)`.**                                 `(YU-QDOM)`

The global H/Y polarization plus the double H/Y anticompleteness of B gives

> **`(Z_X+Z_Y)/p^2 >= 1+eta-o(1)`.**                     `(YU-Z)`

On the exact ray the degree identity simplifies to

`E_U=Z_X+Z_Y-2e(U)`.

Hence

> **`E_U/p^2 >= 1+eta-2q-o(1)`.**                        `(YU-E)`

## 7. Score optimization

Since `L_A>=L_Y`, `(YU-E)` and `(YU-L2)` imply

`(E_U+L_A)/p^2`
` >= 1+2eta-2q+max{[1-2eta]_+,(q/eta)^2}-o(1)`.          `(YU-SCORE)`

For `eta>0`, set

`t=q/eta`,

so `0<=t<=1-eta`. Define

`F(eta,t)=1+2eta-2eta t+max{[1-2eta]_+,t^2}`.

We minimize F exactly.

### Case 1: `0<eta<=1/2`

Put `A=1-2eta`.

For `t<=sqrt(A)`,

`F=2-2eta t`,

so the minimum on that interval is at `t=sqrt(A)`.

For `t>=sqrt(A)`,

`F=1+2eta-2eta t+t^2`,

whose unconstrained minimizer is `t=eta`.

The transition `eta=sqrt(1-2eta)` occurs at

`eta=sqrt(2)-1`.

For `eta<=sqrt(2)-1`, the minimum is

`2-2eta sqrt(1-2eta)`.

The product `eta sqrt(1-2eta)` is maximized at

`eta=1/3`,

with value `1/(3sqrt(3))`. Hence this range gives

> **`F>=2-2/(3sqrt(3))`.**                                `(YU-MIN1)`

For `sqrt(2)-1<=eta<=1/2`, the minimum is

`1+2eta-eta^2`,

which is larger than `(YU-MIN1)`.

### Case 2: `eta>=1/2`

Now `[1-2eta]_+=0`. The unconstrained quadratic minimizer `t=eta` lies beyond the allowed upper bound `1-eta`, so the minimum occurs at `t=1-eta`:

`F=2-2eta+3eta^2`,

whose minimum on this range occurs at `eta=1/2` and equals `7/4`.

Therefore the global minimum is

> **`min F = 2-2/(3sqrt(3))`**
>
> **`=1.6150998205...`.**                                 `(YU-MAIN)`

The minimizing relaxed geometry has

`eta=1/3`,

`t=1/sqrt(3)`,

and hence

`q=1/(3sqrt(3))`.

## 8. Asymptotic closure of the exact low-k ray

The exact score ceiling is

`E_U+L_A<=C0`,

with

`C0/p^2 -> 3/2`.

But `(YU-MAIN)` gives

`liminf (E_U+L_A)/p^2 >= 2-2/(3sqrt(3))`

and

`2-2/(3sqrt(3)) - 3/2 = 1/2-2/(3sqrt(3))`

`=0.1150998205... >0`.

Therefore:

> **EXACT-RAY FINITE-ORDER THEOREM.** Under the current rigid one-code residual-one hypotheses, `k=2`, `J2=empty`, and the exact low-k ray parameters, there is no unbounded sequence of survivors. Equivalently, there exists a finite `p0` beyond which this exact ray is impossible. `(YU-CLOSE)`

No explicit p0 is claimed by the proof here; the theorem is asymptotic and structural.

## 9. Diagnostic finite replay

A separate conservative integer diagnostic using the exact pre-limit inequalities (real Cauchy relaxation, not a graph scan) finds the relaxed score lower bound first exceeds the exact C0 at `p=114` and remains above it through `p=10000`; at `p=114` the relaxed margin is 4.

This is **diagnostic only**. It is not promoted as a proved finite threshold because the present theorem deliberately avoids depending on finite enumeration or on a completeness claim for the candidate minimizer list.

## 10. Audit significance and next move

This session therefore does three things:

1. removes the Y-dense compensator arm exactly (`e(Y)=0`);
2. resolves the triangle-scope blocker by proving every Y--U edge is triangular;
3. converts reverse-certificate capacity plus B0--D isolation into a strict asymptotic score contradiction on the exact low-k ray.

The result is still conditional downstream of the unresolved rigid complete Hall-cut interface, and it closes only the exact low-k stress ray, not the whole residual-one branch.

The next high-value task is to hostile-replay `(YU-TRI)`, `(YU-B0W)`, and the isolation charge independently. If they survive, extend the same `eta/q` score mechanism off the exact ray, retaining `g0=p-y`, rather than returning to the now-closed exact stress family.