# Rigid Hall cuts — singleton-gamma resource sharpening

Date: 2026-09-20

Status: **same-session strengthening/correction of relaxation** in `RIGID_GAMMA_BUDGET.md`. The earlier `2p` gamma-fibre budget is valid but unnecessarily weak because a matched endpoint can help the rigid crossing system only when it is physically a singleton head on `A_X`. For `x>=3`, each tight fibre has at most one such endpoint. Retaining that fact improves the global matched relief from `2p` to `p`.

Nothing in the earlier note becomes false; every occurrence of `[hx-2p]_+` is superseded by the stronger `[hx-p]_+` once singleton matched resources are tracked.

## 1. Source-code-specific singleton matched resources

Assume the exact rigid Hall event `M_X=E_X=0`, with `x=|A_X|>=3`. Let D be the set of distinct codes represented in the outside source layer Y and put `h=|D|`.

For a source code d, define

> `mu_d := |{w : w is a tight matched endpoint, gamma(w)=d, and |N(w) cap A_X|=1}|`.

A d-coded source needs x distinct singleton-head witnesses. A matched witness must have gamma code d, so at most `mu_d` of those x witnesses can be matched. Therefore it needs at least

> `k_d:=[x-mu_d]_+`                                       `(SG-1)`

physical U-witnesses, all in `U_bar d`.

The complementary U-code classes are disjoint for distinct d, hence

> `u>=K:=sum_{d in D} k_d`.                               `(SG-2)`

## 2. The total singleton matched budget is p, not 2p

In one tight fibre the two matched endpoints partition `A_X`, so their A_X-degrees sum to x. Since `x>=3`, both endpoints cannot have A_X-degree one simultaneously.

Thus **each tight fibre contributes at most one singleton matched endpoint in total**, independently of its gamma code. Therefore

> `sum_{d in D} mu_d <= mu_X <= p`.                       `(SG-3)`

Now

`K=sum_d [x-mu_d]_+`
` >= [hx-sum_d mu_d]_+`
` >= [hx-p]_+`.

Hence the global population theorem sharpens to

> **`u >= [hx-p]_+`.**                                    `(SG-4)`

Equivalently, every rigid cut satisfies

> **`h x <= u+p`.**                                       `(SG-5)`

This simultaneously generalizes the old `x<=p+u` size obstruction (h=1) and strengthens the historical diversity bound `h(x-p)_+<=u` for every h>1.

## 3. Parameter form: a very strong code-collapse gate

Use

`a=2p+u-lambda-1=x+y`

and

`g0=x-T0=p-y`.

Then

`u+p = x+lambda+1-g0`.

So `(SG-5)` is exactly

> **`(h-1)x+g0 <= lambda+1`.**                            `(SG-COLL)`

Consequences:

1. existence of any proper rigid cut already requires `g0<=lambda+1` (the h=1 size obstruction);
2. if `h>=2`, then

   > **`x+g0<=lambda+1`;**                                `(SG-H2)`

3. more generally

   > `h <= 1+floor((lambda+1-g0)/x)`.                     `(SG-H)`

Thus whenever

> `lambda < x+g0-1`,

the outside source layer is automatically **one-code**.

This is substantially sharper than the preceding `2p` relaxation `(h-1)x<=y+lambda+1`.

## 4. Refined physical deficit with the sharper k_d

Let `y_d=|Y_d|`. Exactly as in the gamma-budget note, the physically disjoint U-witness populations give

> `Z_X >= (x-1)K`,                                        `(SG-ZX)`
> `Z_Y >= H_Y:=sum_d y_d k_d`,                            `(SG-ZY)`
> `Z >= (x-1)K+H_Y`.                                      `(SG-Z)`

Since `y_d>=1`, `H_Y>=K`; hence

> `Z>=xK>=x[hx-p]_+`.                                     `(SG-Z0)`

So the finite A--U nonedge reservoir itself imposes

> **`x[hx-p]_+<=au`.**                                    `(SG-AU)`

## 5. Refined U-slack and rooted residual

For `g0=p-y>=1`, the same per-witness degree count yields

> `E_U >= sum_d k_d(y_d+g0-1)`                            `(SG-EU-EXACT)`

and therefore, since `H_Y>=K`,

> **`E_U >= g0 K >= g0[hx-p]_+`.**                        `(SG-EU)`

For an above-M(n) graph with the standard ceiling `E_U<=C0`, every rigid cut must obey

> **`g0[hx-p]_+<=C0`.**                                   `(SG-C0)`

For `g0<=1`, the safe aggregate truncation remains

> `E_U >= [H_Y-(1-g0)u]_+`.

The exact rooted residual synthesis of `RIGID_GAMMA_RESIDUAL_CONSEQUENCES.md` remains valid after replacing its old k_d by the sharper `(SG-1)` and its relaxation `[hx-2p]_+` by `[hx-p]_+`.

## 6. Equality geometry worth attacking

The sharpening also exposes what equality in the population bound would mean. If `u=[hx-p]_+` and h>=2, then essentially every singleton matched endpoint across all p tight fibres must be allocated to one of the represented source codes and every remaining crossing-head obligation must be supplied by a distinct complementary U-code witness.

There is no longer a fictitious `2p` matched-relief reservoir created by counting both gamma orientations of one fibre: physical singleton-head geometry permits only one of them.

This makes `(SG-H2)` the correct next gate for the zero-positive-fixture problem. In particular, a multi-code rigid fixture can exist only in the strongly imbalanced regime `lambda>=x+g0-1`; all less-imbalanced rigid cuts are forced immediately into the already-developed one-code branch.