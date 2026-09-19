# Zero-buffer local pair feasibility after the criticality repair

Date: 2026-09-19

Status: internal structural follow-on to `COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md`. This note stays inside the corrected `r=0`, zero-buffer-slack common-buffer subbranch and retains pair-local slack rather than collapsing immediately to total `C0`.

## 1. Setup

Assume the corrected common-buffer equality geometry and additionally

`epsilon_b=0`.

The buffer floor then gives

`g=p`, `k=x-p>0`.

The repair theorem shows that all k buffer--X edges which cannot use the reverse orientation must use **outside unmatched** witnesses; matched Orientation-A feet are impossible because every matched gamma code is `d` or `bar d`, while every X-code is different from both.

Let `m` be the number of distinct outside witnesses used by a chosen set of k forced edges. For an above-`M(n)` candidate put

`R_A=floor(R_code(C0)/2)`.

Then

> `m>=m0:=ceil(k/R_A)`                                    `(1.1)`

(with `R_A=0` making the branch impossible).

The repaired geometry gives

> `L_Y>=A:=y(1+m0)`,                                      `(1.2)`
>
> `E_bar>=B:=E_core=k(p+k-2)`,                            `(1.3)`

where `E_bar` is the slack on `U_bar d=U_-=W0 dotcup {b}`; the buffer contributes zero.

Hence already

> `S_P>=s_geom:=A+B`.                                     `(1.4)`

## 2. Exact pair traffic in the zero-buffer model

Because `g=p`, every Y-source uses all p gamma-d matched endpoints on p crossing edges. The remaining k crossing edges use the common core W0. Since `e(Y)=0`, the pair-P traffic is therefore exact:

> `P_P=yp`,                                               `(2.1)`
>
> `C_P=yk`,                                               `(2.2)`
>
> `t_P=xy=y(p+k)`.                                        `(2.3)`

Thus the generic lower bounds can be sharpened here to equal traffic identities.

In particular the exact pair capacity requires

> `2xy<=Ccap_P`
> `=R_code(S_P)[p+2S_P/(lambda+1)]`.                      `(2.4)`

## 3. Directed A/U capacity gives an exact local score floor

The preserved directed A/U capacity for the one-sided pair is

> `(lambda+1) C_P <= u_bar L_Y+yE_bar`,                  `(3.1)`

with

`u_bar=|U_bar d|=k+1`.

Using `(2.2)`, put `L=lambda+1` and

`T=L y k`.

We want the least possible useful pair slack

`L_Y+E_bar`

subject to

`L_Y>=A`, `E_bar>=B`,

`(k+1)L_Y+yE_bar>=T`.

Starting from `(A,B)`, one extra unit of `L_Y` buys `k+1` units of capacity and one extra unit of `E_bar` buys y units. Therefore the exact integer minimum is

> `s_AU=A+B`
> ` +ceil([T-(k+1)A-yB]_+/max(k+1,y))`.                  `(3.2)`

Since any `U_d` slack in the pair increases `S_P` but does not help `(3.1)`, every survivor satisfies

> `S_P>=s_AU`.                                            `(3.3)`

This is the exact local optimization; no total-score substitution is used in its derivation.

### Equality direction

If `y>k+1`, any extra useful slack beyond `(A,B)` is cheapest in `E_bar`; if `k+1>y`, it is cheapest in `L_Y`; if the coefficients tie, either direction is equally cheap. Thus near equality already identifies which half of the pair must absorb the remaining capacity burden.

## 4. Exact Ccap and CROWD floors

Define `s_cap` to be the least nonnegative integer s satisfying

> `R_code(s)[p(lambda+1)+2s]`
> ` >=2xy(lambda+1)`.                                     `(4.1)`

Monotonicity of `R_code` gives

> `S_P>=s_cap`.                                           `(4.2)`

The preserved crowding inequality gives

> `S_P>=s_crowd:= [y(3y-D0)]_+`,                         `(4.3)`

where

`D0=5p+5u-3lambda-2`.

Therefore the zero-buffer equality branch has the compact local necessary condition

> `S_P>=s_*:=max{s_geom,s_AU,s_cap,s_crowd}`.            `(4.4)`

An above-threshold survivor must in particular have

> `s_*<=C0`.                                              `(4.5)`

The point of `(4.4)` is not the total ceiling `(4.5)`; it is that all four constraints are now expressed on the same physical complementary pair P and can be subjected to equality/stability analysis.

## 5. Residual coupling is simultaneous, not separate

The criticality repair also gives, with `ell=k`,

> `Z>=ka+y(1+m)`.                                         `(5.1)`

At the minimal distinct-witness count `m0`, this is

> `Z>=ka+y(1+m0)`.                                        `(5.2)`

The core U-slack floor is

> `E_U>=E_core`.                                          `(5.3)`

Hence, with

`D_zero=ka+y(1+m0)-u(p-lambda)`,

one has

> `q+E_U>=E_core+ceil([D_zero-E_core]_+/2)`.              `(5.4)`

This must hold simultaneously with `(4.4)`. Thus any near-sharp local pair configuration also has a compulsory rooted residual cost; local pair saturation cannot be optimized independently of `q+E_U`.

## 6. Diagnostic outcome

The companion checker scans the same bounded abstract box used by the z=1 diagnostics (`3<=p<=18`, `1<=u<=18`, `lambda>=0`). Among the 17,174 zero-buffer `(p,u,lambda,x)` branches passing the predecessor scalar score floor:

- the repaired outside-witness geometry alone rejects 113;
- 17,061 remain;
- the exact directed A/U floor `(3.2)` is **strictly stronger than `s_geom` in 5,280** of the remaining/considered branches;
- nevertheless it creates no additional rejection against total `C0` in this coarse box;
- exact `s_cap` and `s_crowd` create no strict improvement over `s_geom` on this bounded box.

This is useful negative information. The local pair tools are not producing a new scalar contradiction merely by being stacked. The next gain must come from their **near-equality structure** or from coupling `(4.4)` to the residual lower bound `(5.4)`, not from another coarse numerical minimum.

These are abstract parameter-branch counts, not graph counts.

## 7. Next structural target

The zero-buffer branch is now normalized enough for a compact stability theorem.

The next move should classify simultaneous near equality in:

1. outside-witness reuse `m=m0`;
2. Y-hole identity `L_Y=y(1+m)`;
3. core slack `E_bar=E_core` or the exact extra amount prescribed by `(3.2)`;
4. directed A/U capacity `(3.1)`;
5. exact crossing capacity `(2.4)`;
6. the rooted residual inequality `(5.4)`.

In particular, if `s_AU>s_geom`, near equality forces the extra pair slack onto the coefficient-maximizing side identified above. That should be converted back into exact degree structure of W0 or exact Y-hole geometry before any move to `z=2`.

`X_3` remains outside this branch because `u=0`.