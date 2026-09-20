# Exact all-F outside-population score gate

Date: 2026-09-20

Status: internal conditional arithmetic corollary of `ALL_F_OUTSIDE_LAYER_COLLAPSE.md`. No bounded scan is used in the theorem.

## 1. Population gate

Put

`T=u-k-2>=0`, so `u_o=T+1`,

and use the exact first-strict identity

`lambda=2p+T-g-y+1`.

The outside-layer collapse gives

`E_{U_o} >= (T+1)(T+p-1)`.

Since total available excess is

`C0=(lambda+3)p+(lambda+2)u-2 floor((lambda+1)^2/4)-4`,

a necessary condition for any all-F one-witness survivor is

> `(T+1)(T+p-1) <= C0`.                                 `(F-POP)`

This deliberately ignores all pair-local, core, buffer, Y and a0 costs, so it is a safe necessary gate.

## 2. Exact completed-square form

Let

`L=lambda+1=2p+T-g-y+2`

and let `eta` be 1 when L is odd and 0 when L is even. Since

`2 floor(L^2/4)=(L^2-eta)/2`,

direct expansion gives

`2[C0-(T+1)(T+p-1)]`

`= R(p,k,g,y)+eta-(T-k-3)^2`,

where

`R(p,k,g,y)`

`= -g^2-2gk+2gp-2gy+k^2+4kp-2ky+12k+2py+6p-y^2+11`.

Hence the exact necessary condition is

> `(T-k-3)^2 <= R(p,k,g,y)+eta`.                        `(F-POP-SQUARE)`

In particular the parity-free consequence

> `T <= k+3+floor(sqrt(max(0,R+1)))`                    `(F-T-CAP)`

holds whenever the branch is nonempty. If `R+eta<0`, the shape is impossible for that parity.

This is an explicit analytic reservoir cap, not a finite-search cutoff.

## 3. Exact two-step concavity

Along one parity class of T,

`C0(T+2)-C0(T)=2p+2u+4`,

while

`E_{U_o}(T+2)-E_{U_o}(T)=4T+2p+4`.

Therefore

> `[C0-E_{U_o}](T+2)-[C0-E_{U_o}](T)=2(k+2-T)`.         `(F-POP-SLOPE)`

So the outside-population budget increases only until the neighbourhood of `T=k+2` and then decreases strictly, with second parity-step difference `-4`.

This removes the former unbounded-T obstruction of `ALL_F_RESIDUAL_GATE.md`: for every fixed shape `(p,k,g,y)` the all-F one-witness branch is now analytically confined to a finite T interval before any residual or pair-local inequality is applied.

## 4. Pair-local strengthening

The entire outside layer has code `bar C`, which lies outside the audited complementary pair `P={d,bar d}`. Hence its score is disjoint from the pair-local score `S_P`. If `Sigma_F` is the exact pair threshold already defined in `ALL_F_RESIDUAL_GATE.md`, and

`A_F=[p-y-x+2]_+`,

then every survivor actually satisfies the stronger local/global interface

> `Sigma_F+(T+1)(T+p-1)+A_F <= C0`.                    `(F-POP-PAIR)`

This preserves pair locality: `Sigma_F` is not replaced by total score, and the outside-population bill is charged only after the exact pair requirement has been met.

## 5. Consequence for forward work

The live y>=2 all-F arm has `g in {0,1}` by head saturation. Its former asymptotic problem was an outside reservoir T that could make the older rooted upper bound grow. The physical reverse-fan collapse instead makes the whole outside population self-price quadratically and bounds T explicitly by `(F-T-CAP)`. The remaining task is therefore a finite-parameter structural classification in ratios/scaling of `(p,k,y)`, not an uncontrolled T-tail.
