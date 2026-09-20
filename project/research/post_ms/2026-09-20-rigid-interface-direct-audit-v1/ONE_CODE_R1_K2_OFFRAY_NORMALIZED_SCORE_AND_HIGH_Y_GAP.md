# Residual-one k=2: off-ray normalized score and a high-Y gap

Date: 2026-09-20

Status: **same-session conditional theorem / hostile replay synthesis**, downstream of the rigid one-code residual-one interface, `k=2`, `J2=empty`, the repaired raw same-code theorem, ordered `(source,witness)` injection, global H/Y polarization, and the general Y--U triangle/capacity theorem. This note does **not** establish graph-level reachability of the rigid interface. Bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.

## 1. Hostile replay of the load-bearing chain

Before using the off-ray theorem, the four steps requested by the live handoff were replayed directly.

1. **Y-independence.** A Y--Y edge has same code `d`, hence raw same-code criticality requires a complementary witness of code `bar d`. In residual dimension one, `A_bar(d)=empty`. A witness in `B0` is impossible because `B0` is Y-anticomplete. A witness in `U_bar(d)\B0` has an H-neighbour, and every Y vertex sees every H vertex, so that H-neighbour is an illicit second common neighbour. Thus `e(Y)=0` survives replay.

2. **All Y--U edges are triangular.** If `c(t)!=bar d`, then t and the d-coded Y endpoint agree on at least one tight matched coordinate and share that matched endpoint. If `c(t)=bar d`, an H-free t lies in B0 and is Y-anticomplete; an H-positive t shares an H-neighbour with the Y endpoint. Thus every existing Y--U edge is triangular in this exact scope.

3. **High-Y D vertices reverse through B0.** For `t in D=U\B0` with `d_Y(t)>=2`, the t-sourced orientation of a Y--t triangle edge is impossible: a U/B witness shares the root, an X witness sees another Y-neighbour of t, and a Y witness cannot see the Y head because `e(Y)=0`. In the reverse orientation, the singleton condition forces complementary code `bar d`, no A-location exists, and Y-completeness to X forces the witness X-anticomplete. Hence it lies in B0. The fixed ordered `(Y-source,B0-witness)` pair certifies at most one head.

4. **B0--D isolation charge.** For B-sourced B--D edges, distinct outgoing heads from one B source require distinct Y witnesses. Each such witness must miss every other D-neighbour of the same B source. A fixed Y--D nonedge can be charged by at most `b=|B|` B sources. Therefore the multiplicity divisor really is b, not one and not the B-degree of the witness.

No new scope defect was found in these four steps. The result remains conditional on the upstream rigid interface and the repaired same-code theorem.

## 2. Variable residual-one parameters

In residual dimension one with `k=2` and `J2=empty`, the exact identities are

`x=p+1`,

`u=c+1`,

`g0=p-y`,

`lambda=c+p-y-1`,

`|H|=p-1`.

Let

`B=B0={w in U_bar(d): d_H(w)=0}`,

`b=|B|`, `D=U\B`, `C=e(B,D)`.

Consider an unbounded sequence with `p->infinity` and bounded ratios, and write

`theta=y/p`, `kappa=c/p`, `eta=b/p`, `q=C/p^2`.

Then

`0<=theta<=1`, `0<=eta<=kappa`, `0<=q<=eta(kappa-eta)`.

The exact score ceiling

`C0=(lambda+2)(p+u)+p-A_lambda`

has leading coefficient

> **`S0(kappa,theta)=((1+kappa)^2-theta^2)/2`.**          `(OR-S0)`

## 3. General Y-hole coefficient

The exact general Y--U capacity theorem gives

`Z_YU >= b y + max{0, y(|D|-b)-|D|, O(O-b)/b^2}`,

where `O=[C-2|D|]_+`.

For fixed positive eta, division by `p^2` gives

> **`Y0 = eta theta + max{0, theta(kappa-2eta), (q/eta)^2}`** `(OR-Y)`

as an asymptotic lower coefficient for `Z_YU`. At `eta=0`, necessarily `q=0` and the capacity arm gives the limiting coefficient `theta kappa`.

Because `e(Y)=0`, the standard Y-side degree-slack identity remains

`L_Y=Z_YU-y`,

so asymptotically

> **`L_A/p^2 >= L_Y/p^2 >= Y0-o(1)`.**                  `(OR-LY)`

## 4. Total A--U hole coefficient

The global H/Y polarization says every escape vertex in D pays at least

`min{p-1,y-1}`

holes across H or Y. Every vertex of B is simultaneously H-anticomplete and Y-anticomplete. Since `theta<=1`, this yields

`Z/p^2 >= kappa theta + eta-o(1)`.

Independently, all B--H holes are disjoint from the Y-hole count `(OR-Y)`, so

`Z/p^2 >= eta+Y0-o(1)`.

Therefore put

> **`Z0=max{kappa theta+eta, eta+Y0}`.**                  `(OR-Z)`

Then

> **`Z/p^2 >= Z0-o(1)`.**                                `(OR-Z2)`

This is the first useful off-ray synthesis: the general reverse-certificate/isolation theorem and the global H/Y polarization live in compatible physical currencies and can be retained simultaneously.

## 5. U-edge localization and the normalized score obstruction

B is independent. Every U--U edge not across B--D lies inside D, and every D source has oriented U--U source capacity at most two. Hence

`C <= e(U) <= C+2|D|`.

For bounded kappa this implies

`e(U)/p^2=q+o(1)`.

The exact rooted identity

`Z=u(p-lambda)+2e(U)+E_U`

therefore gives

> **`E_U/p^2 >= Z0+kappa(kappa-theta)-2q-o(1)`.**         `(OR-E)`

Combining `(OR-E)` with `(OR-LY)` gives the off-ray normalized score floor

> **`(E_U+L_A)/p^2 >= F(kappa,theta,eta,q)-o(1)`,**
>
> **`F=Z0+Y0+kappa(kappa-theta)-2q`.**                   `(OR-F)`

Every bounded-ratio asymptotic survivor must therefore satisfy

> **`F(kappa,theta,eta,q) <= S0(kappa,theta)`**           `(OR-SCORE)`

for some `eta,q` in the physical domain above.

The exact low-k stress ray is the specialization `kappa=theta=1`; `(OR-F)` reduces to the previously closed eta/q optimization.

## 6. Independent rooted-Q ratio restriction

The predecessor rooted-Q feedback inequality in residual dimension one is

`2(x+y-1)+phi(p-1)`
` <= u(p-lambda)+2(c-1)u-(c-1)c+C0`.

After division by `p^2`, every bounded-ratio asymptotic survivor must satisfy

> **`1 <= kappa theta + S0(kappa,theta)`.**               `(OR-ROOT)`

Equivalently

> **`kappa^2+2(1+theta)kappa-theta^2-1 >= 0`.**          `(OR-ROOT2)`

Thus

> **`kappa >= sqrt(2(theta^2+theta+1))-(1+theta)`.**      `(OR-KMIN)`

At the high-Y endpoint `theta=1`, this gives

> **`kappa >= sqrt(6)-2 = 0.4494897427...`.**             `(OR-K1)`

This is much stronger there than the generic large-gap lower ratio `kappa>=1/6+o(1)`.

## 7. The theta=1 score is strictly impossible for every kappa>0

The off-ray score itself has a useful exact endpoint theorem. Put `theta=1`. For `eta>0`, write

`t=q/eta`, so `0<=t<=kappa-eta`.

Using only the baseline part `Z0>=kappa+eta`, `(OR-F)` gives

`F-S0 >= D`, where

> **`D = kappa^2/2-kappa+2eta(1-t)+max{kappa-2eta,t^2}`.** `(OR-D)`

We show `D>0` for every `kappa>0` in the physical domain.

### Case A: `kappa-2eta >= t^2`

Then

`D=kappa^2/2-2eta t`.

Since `t<=kappa-eta`,

`eta t<=eta(kappa-eta)<=kappa^2/4`.

Equality in the last inequality requires `eta=t=kappa/2`, but the case condition would then require `0>=kappa^2/4`, impossible for `kappa>0`. Hence

> **`D>0`.**

### Case B: `t^2 >= kappa-2eta`, `0<=t<=1`

Here the coefficient of eta in `(OR-D)` is nonnegative. The smallest permitted eta is `max{0,(kappa-t^2)/2}`.

If `kappa<=t^2`, then `D>=kappa^2/2>0`.

If `kappa>t^2`, feasibility `t<=kappa-eta` forces

`kappa>=2t-t^2`.

At the smallest eta,

`D=kappa^2/2-kappa t+t^3`.

For `0<=t<=1` this is increasing in kappa throughout the feasible range, and at `kappa=2t-t^2` it equals

> **`t^4/2`.**

Thus it is strictly positive except at the excluded zero endpoint.

### Case C: `t>1`

Now `(OR-D)` decreases with eta, so use the largest feasible `eta=kappa-t`. The resulting quadratic in kappa is minimized at `kappa=2t-1`, where

> **`D=(2t^2-1)/2>0`.**

Therefore:

> **HIGH-Y ENDPOINT THEOREM.** In the bounded-ratio residual-one `k=2,J2=empty` normal form, the normalized score obstruction is strict at `theta=1` for every `kappa>0`. `(OR-HY)`

Combined with `(OR-K1)`, there is a uniform positive gap on every compact bounded-kappa high-Y limit set allowed by the rooted-Q inequality. In particular, no bounded-ratio unbounded survivor can have `y/p -> 1`.

This strictly generalizes the previous exact stress-ray closure: the obstruction is not special to `c/p=1`.

## 8. What remains

The current mechanism does **not** yet close the whole variable residual-one branch. When theta is separated from one, `(OR-SCORE)` has feasible relaxed points. The correct next split is therefore:

1. use `(OR-KMIN)` and `(OR-SCORE)` to quantify an explicit high-Y exclusion wedge;
2. retain `g0/p=1-theta` in the middle regime rather than specializing it away;
3. keep `y=o(p)` on the existing large-gap/rooted-residual route;
4. do not return to the exact `kappa=theta=1` stress family.

A finite grid over `(kappa,theta,eta,q)` may be useful as a diagnostic to locate the next hostile scaling direction, but it is not proof.

## 9. Audit boundary

No claim here promotes the rigid cut to an actual D2C configuration. The latest daily audit remains binding: P1/P2 repairs, raw same-code criticality and ordered injection are load-bearing; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain mandatory when invoked; `X_3` remains the negative control; bounded graph-level regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`.