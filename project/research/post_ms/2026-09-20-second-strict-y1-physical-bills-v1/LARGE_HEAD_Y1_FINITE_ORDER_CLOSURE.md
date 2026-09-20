# Exact second-strict mixed y=1 — complete finite-order bound for the large-head tail

Date: 2026-09-20

Status: **same-session internal analytic reduction** for the already-classified large-head mixed branch `p>=2`, `x>=5`. This corrects the apparent exceptional-Fz k=1 asymptotic tail and then shows that the same physical nonnegative-buffer gate bounds **all** R/Fz/Fx large-head cases. No finite scan is used as proof.

## 1. Physical gate omitted by the old diagnostic

The exact second-strict mixed layer has

> `epsilon_b=p-g+2`.

Because the root has maximum degree, every slack is nonnegative. Therefore

> **`g<=p+2`.**                                           `(Y1-GATE)`

This condition was absent from the original `check_y1_physical_bills.py` and is now restored there.

Write

`k=x-g>=1`, so `x=g+k`,

and `omega=|U_o|`.

The exact rooted margins used by the old diagnostic can be optimized analytically in omega. The parity remainder is `eps in {0,1}`.

## 2. R and no-exception Fz

For both cases the exact rooted margin has

`2B=`
` eps-g^2-2gk+2gp-2k^2+2k+6p-2p^2`
` +(2g+2k-2p+4)omega-omega^2-8`.

As a real quadratic in omega, its maximum is

> `2B_max=eps+4g-k^2-2kp+6k-p^2+2p-4`.                 `(Y1-RBMAX)`

Using `eps<=1` and `(Y1-GATE)`,

`2B_max`
` <= -(p+k)^2+6(p+k)+5`.

A survivor has `B>=0`, hence `B_max>=0`, so with `s=p+k`,

`s^2-6s-5<=0`.

Since `p>=2`, `k>=1`, s is a positive integer and therefore

> **`p+k<=6`.**                                           `(Y1-RS6)`

Then

> `p<=5`, `k<=4`, `x=g+k<=p+k+2<=8`.                    `(Y1-RX8)`

To bound omega, complete the same square:

`2B=2B_max-[omega-(x-p+2)]^2`.

Under `3<=s<=6`, the upper relaxation above gives `2B_max<=14`, while

`x-p+2<=k+4<=8`.

Thus

> **`omega<=11`.**                                        `(Y1-RW11)`

The rooted partition order in the mixed y=1 branch is

`n=1+(x+1)+(2p+k+1+omega)`
` =x+2p+k+omega+3`.

Since `2p+k=p+(p+k)<=11`,

> **`n<=8+11+11+3=33`.**                                 `(Y1-RN33)`

This covers both R and no-exception Fz.

## 3. Exceptional Fz

The exceptional-Fz rooted floor is one unit stronger (`r>=x+2`), and its exact margin is

`2B=`
` eps-g^2-2gk+2gp-2k^2+6p-2p^2`
` +(2g+2k-2p+4)omega-omega^2-10`.

Its real omega maximum is

> `2B_max=eps+4g-k^2-2kp+4k-p^2+2p-6`.                 `(Y1-FZBMAX)`

Using `g<=p+2`,

`2B_max<=-(p+k)^2+6(p+k)+3`.

Therefore `B>=0` again forces

> **`p+k<=6`.**                                           `(Y1-FZS6)`

and hence `p<=5`, `x<=8`.

The square centre is again `x-p+2<=k+4<=8`, while the relaxed maximum is at most 12 for `3<=p+k<=6`. Therefore

> **`omega<=11`**

and the same order estimate gives

> **`n<=33`.**                                            `(Y1-FZN33)`

The special k=1 correction `EXCEPTIONAL_FZ_K1_SCALING_CORRECTION.md` gives the sharper n<=34 by a direct route; the present all-k calculation improves and subsumes its asymptotic conclusion in the classified large-head regime.

## 4. Fx

The exact Fx rooted floor is

`r_low=x+p-2+ceil((x+p-2)/x)`.

Since the ceiling is at least one,

> `r_low>=x+p-1`.

Using this weaker lower bound makes the rooted margin only larger, so any survivor must satisfy the upper-relaxed quadratic

`2B<=`
` eps-g^2-2gk+2gp-2k^2+2k-2p^2+4p`
` +(2g+2k-2p+2)omega-omega^2`.

Its real omega maximum is

> `2B_max<=eps+2g-k^2-2kp+4k-p^2+2p+1`.                `(Y1-FXBMAX)`

Applying `g<=p+2` and `eps<=1` gives

`2B_max<=-(p+k)^2+4(p+k)+6`.

Thus `B>=0` implies

`s^2-4s-6<=0`, `s=p+k`,

and therefore

> **`p+k<=5`.**                                           `(Y1-FXS5)`

So `p<=4`, `k<=3`, and

> **`x<=p+k+2<=7`.**                                      `(Y1-FXX7)`

The square centre is `x-p+1<=k+3<=6`; the relaxed maximum is at most 9, hence

> **`omega<=9`.**                                         `(Y1-FXW9)`

Also `2p+k=p+(p+k)<=9`, so

> **`n<=7+9+9+3=28`.**                                   `(Y1-FXN28)`

## 5. Large-head y=1 conclusion

Combining the three classified geometries:

> **LARGE-HEAD MIXED-y=1 FINITE-ORDER CLOSURE.**
>
> In the exact second-strict mixed-hole branch with `p>=2`, `x>=5`, every R/Fz/Fx survivor satisfies
>
> **`n<=33`.**                                            `(Y1-N33)`

Hence this entire classified large-head y=1 arm is impossible for

> **`n>=34`.**                                            `(Y1-N34-CLOSED)`

This is analytic. It does not depend on the finite survivor counts of the diagnostic checker.

## 6. Diagnostic confirmation after repairing the physical gate

The repaired diagnostic now rejects `epsilon_b<0`. On its original box

`2<=p<=20`, `5<=x<=30`, `2<=omega<=24`, `1<=g<x`,

survivors fall from the superseded counts

- R: 2,821;
- Fz0: 2,840;
- Fx: 691;
- Fz1: 2,276;

to

- **R: 86**;
- **Fz0: 86**;
- **Fx: 17**;
- **Fz1: 38**.

Expanding independently to

`p<=30`, `x<=60`, `omega<=50`

produces exactly the same survivor counts and maxima:

- R/Fz0: `p<=5`, `x<=8`, `omega<=10` in the scanned rows;
- Fx: `p<=3`, `x<=7`, `omega<=7`;
- Fz1: `p<=5`, `x<=8`, `omega<=8`.

These finite replays are audit support only; `(Y1-N33)` is the proof-level conclusion.

## 7. Strategic correction

The previously advertised “unbounded exceptional-Fz k=1 scalar family” was a checker/feasibility artefact caused by allowing negative exact buffer slack. It is no longer a reason to prioritize pair-local optimization in that family.

After this correction, the exact second-strict programme has much less asymptotic residue:

- mixed `(1,1)`, `y>=2`: internally closed;
- mixed `(1,1)`, `y=1`, `p>=2,x>=5`: finite order `n<=33`;
- two-X-hole `(2,0)`, `y>=2,x>=4`: finite order `n<=816` by the companion closure;
- `(0,2)`: internally closed.

The remaining second-strict work is therefore concentrated in explicit small-head/small-p tails (notably `x=3,4` and any `p=1` cases outside the large-head classification), plus independent adversarial replay of the same-session closures.

If those tails can also be bounded in order, the exact unloaded second-strict layer will cease to be an asymptotic branch entirely, and the eventual programme should move to higher buffer defect / loaded-buffer structure.