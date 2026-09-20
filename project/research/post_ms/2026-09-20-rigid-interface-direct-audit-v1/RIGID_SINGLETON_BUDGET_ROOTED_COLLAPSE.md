# Rigid Hall cuts — sharpened singleton budget and rooted code-collapse

Date: 2026-09-20

Status: **same-session structural synthesis**, conditional on the exact rigid Hall event `M_X=E_X=0`, `x=|A_X|>=3`, and the standard rooted size identity. This note feeds the physical singleton-head budget from `RIGID_SINGLETON_GAMMA_BUDGET_SHARPENING.md` into the rooted parameters. It supersedes the weaker `u+2p` diversity relaxation in `RIGID_GAMMA_RESIDUAL_CONSEQUENCES.md`; it does not remove the zero-positive-fixture caveat.

## 1. Inputs

Let `D` be the distinct source codes represented in `Y`, `h=|D|`. The sharpened physical singleton budget gives

> `h x <= u+p`.                                            `(SRC-1)`

The exact rooted size identity is

> `x+y=2p+u-lambda-1`.                                    `(SRC-2)`

Write, as in the rigid/Hall packages,

> `g0:=p-y`.                                               `(SRC-3)`

Then `(SRC-2)` is equivalently

`u=x-p-g0+lambda+1`.                                      `(SRC-4)`

## 2. Rooted collapse inequality

Substitute `(SRC-4)` into `(SRC-1)`:

`h x <= x-g0+lambda+1`.

Therefore every exact rigid Hall cut satisfies

> **`(h-1)x <= lambda+1-g0`.**                             `(SRC-COLL)`

This is substantially stronger than the predecessor inequality

`(h-1)x <= y+lambda+1`,

which came from the coarse `u+2p` gamma budget. The entire `y` term has disappeared because only physically singleton matched endpoints can relieve U demand, and there are globally at most `p` of them.

## 3. Immediate consequences

Because `h>=1`, the left side of `(SRC-COLL)` is nonnegative. Hence a necessary condition for the rigid event itself is

> **`g0 <= lambda+1`.**                                    `(SRC-FEAS)`

Thus if `p-y>lambda+1`, the exact rigid Hall event `M_X=E_X=0` is impossible, regardless of one-code purification or pair-local capacity.

More generally,

> **`h <= 1+floor((lambda+1-g0)/x)`.**                     `(SRC-H)`

In particular:

- if `lambda+1-g0 < x`, then **`h=1`**;
- if `h>=2`, then necessarily
  > `lambda+1-g0 >= x >=3`, hence **`lambda>=g0+2`**;
- if `lambda<=g0+1`, then the rigid event is automatically one-code whenever it is feasible at all (at equality `lambda=g0-1` or smaller it is impossible by `(SRC-FEAS)`).

This is a score-free collapse coming solely from physical witness population plus the rooted size identity.

## 4. One-code form of the U demand

When `h=1`, the sharpened singleton budget gives

`K >= [x-p]_+`.

Using `(SRC-4)`,

`x-p=u+g0-lambda-1`,

so under `(SRC-FEAS)`

> **`K >= [u-(lambda+1-g0)]_+`.**                          `(SRC-U1)`

Thus in a one-code rigid cut, all but at most

`lambda+1-g0`

vertices of U are forced into the complementary witness population whenever `x>p`. This gives a useful physical interpretation of the narrow feasibility strip `g0<=lambda+1`: the same strip measures how many U vertices can escape the mandatory source-code witness population.

The located-hole theorem then yields

> `Z_X >= (x-1)[u-(lambda+1-g0)]_+`,                       `(SRC-ZX1)`

before any pair-local `Ccap_P`, `(ONE-P)` or `(CROWD)` price is added.

## 5. Strategic effect on the zero-fixture problem

The bounded graph regression has zero positive rigid complete Hall-cut fixtures with `x>=3`. The direct audit already reduced the concern that the singleton-head implication itself was misstated. `(SRC-COLL)` now shows that any actual fixture must lie in a very thin rooted strip:

> `p-y=g0 <= lambda+1`,

and any genuinely multi-code outside layer must lie in the still thinner regime

> `lambda+1-g0 >= x`.

Therefore the next reachability search/audit should be stratified by the integer gap

`c:=lambda+1-g0 >=0`.

- `0<=c<x`: only the one-code branch can occur;
- `c>=x`: multi-code remains possible, but `h<=1+floor(c/x)`;
- in the one-code case with `x>p`, at most `c` U vertices lie outside the mandatory complementary witness population.

This is the correct rooted front end for the near-rigid `Theta` / private-coordinate tradeoff. It should replace the older `y+lambda+1` diversity criterion in future live reasoning while the older theorem remains preserved historically.