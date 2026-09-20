# Two-X-hole branch — complete analytic closure for x>=16

Date: 2026-09-20

Status: **same-session internal analytic closure** of the core-saturated exact second-strict two-X-hole branch for `y>=2`, `x>=16`. This combines the exact positive-combination obstruction, localization of both X- and U_o-density to the two physical hole-code witness classes, and the new forward-routing physical surcharge. No finite scan is used as proof.

## 1. Setup and inherited exact obstruction

Retain

- `M=M_H=m_{H_0}+m_{H_1}`;
- certificate load `L`;
- `omega=|U_o|`;
- `e_X<=M`, `e_o<=M`;
- the zero-resource score/rooted margins `A_0,B_0` of `TWO_X_HOLE_NO_HOLE_CODE_CLOSURE.md`.

That note proves

> `A_0+3B_0=-Phi`,                                       `(E-COMB0)`

where

`Phi=8L+P-2eps`
`    +3p^2+2p omega-3py-8p`
`    +omega^2-4omega x+omega y-8omega`
`    +5x^2-3xy-10x+2y^2+4y+20`,                         `(E-PHI)`

and

`P=[omega(p-x)+2L]_+`, `eps in {0,1}`.

The density resource M can improve the score margin by at most `2M` and the rooted margin by at most `3M`.

## 2. Forward routing cancels most of the M rebate

For each distinct represented physical hole code C, put

`F_C=s_C[m_C-2]_+`

as in `TWO_X_HOLE_HOLE_CLASS_FORWARD_SURCHARGE.md`, and

`F_H=sum_C F_C`.

That theorem gives at least `F_H` additional core--outside holes and `F_H` additional X--outside holes beyond the J-incidence ledger. Therefore

> `A<=A_0+2M-2F_H`.                                      `(E-A)`

For the rooted margin:

- `e_o<=M` adds at most M to q;
- `e_X<=M` can recover at most `2M` units of A-slack available to E_U;
- the additional core--outside holes remove `F_H` from q;
- the additional X--outside holes add `F_H` to L_A and therefore remove another `F_H` from the E_U allowance.

Hence

> `B<=B_0+3M-2F_H`.                                      `(E-B)`

The extra outside-witness slack from the forward theorem is deliberately ignored, so these are conservative.

A survivor requires `A,B>=0`, hence

> `0<=A+3B<=-Phi+11M-8F_H`.                              `(E-NEC0)`

Thus

> **`Phi<=11M-8F_H`.**                                   `(E-NEC)`

## 3. Universal net value of one represented hole class

Suppose first that the two physical hole codes are distinct. Their complementary outside classes are then disjoint and

`M<=omega`.

For one represented hole code with parameters `(m,s)`, the hole-class routing theorem gives

`ms<=m+2s`.

Its contribution to the right side of `(E-NEC)` is

`11m-8s[m-2]_+`.

We claim

> **`11m-8s[m-2]_+ <=3m+16`.**                           `(E-CLASS)`

Proof:

- `m=1`: left side 11, right side 19;
- `m=2`: both give 22;
- `m>=3`: if `s=1`, equality holds:
  `11m-8(m-2)=3m+16`;
- if `m>=3,s>=2`, then
  `11m-8s(m-2)<=11m-16(m-2)=32-5m<=3m+16`.

There are at most two distinct physical hole codes. Summing `(E-CLASS)` gives

> `11M-8F_H<=3M+32<=3omega+32`.                          `(E-NET)`

If instead `H_0=H_1=C`, the predecessor matched-routing theorem gives `m_C<=2`, while `M=2m_C<=4`. The bounded-resource closure already rules this out for `x>=14`. Therefore every possible survivor with `x>=16` lies in the distinct-hole-code situation above.

Consequently every `x>=16` survivor would have to satisfy

> **`Phi-3omega<=32`.**                                  `(E-REQ)`

## 4. Analytic lower bound Phi-3omega>32 for x>=16

Use the same safe relaxations as the no-hole-code closure:

- `P>=0`;
- `eps<=1`;
- `L>=max(x-2,omega)`.

Let `Phi_0` be the resulting lower bound for Phi. Then

`Phi-3omega>=Phi_0-3omega`.

Completing the square in y gives

> `Phi_0-3omega=2(y-y_*)^2+N'/8`,                        `(E-SQ)`

with

`y_*=(3p-omega+3x-4)/4`

and

`N'=64 max(x-2,omega)`
`   +15p^2+22p omega-18px-40p`
`   +7omega^2-26omega x-96omega`
`   +31x^2-56x+128`.                                     `(E-N)`

As a real quadratic in p, the unconstrained minimizer is unchanged:

`p_*=(9x+20-11omega)/15`.

### 4.1 Case p_*<=1

The minimum over `p>=1` occurs at `p=1`.

If `omega>=x-2`, substitute the active maximum term and minimize the resulting quadratic in omega. Its real minimizer is

`omega_0=(13x+5)/7`,

and

> `N'>=24(2x^2-27x+29)/7`.                               `(E-N1)`

For `x>=16` this is increasing, and at `x=16` it is

`2616/7 >373`.

If `omega<=x-2`, the p=1 expression is decreasing throughout that interval, so its minimum is at `omega=x-2`, giving

> `N'>=12x^2-60x+151`.                                   `(E-N2)`

At `x=16` this is 2263 and increases thereafter.

### 4.2 Case p_*>1

If `omega>=x-2`, the condition `p_*>1` requires

`omega<(9x+5)/11<x-2`

for every `x>=14`, impossible.

Thus `omega<=x-2`. Minimize first in p. The real minimum is

`N'=(8/15)G'`,

where

`G'=120(x-2)-2omega^2-24omega x-125omega`
`   +48x^2-150x+190`.

This is strictly decreasing in omega. Under `p_*>1`,

`omega<(9x+5)/11`.

Using that real boundary gives

> `N'>=8(218x^2-1167x-865)/121`.                         `(E-N3)`

At `x=16` this exceeds 2398 and is increasing for all `x>=16`.

### 4.3 Conclusion

The weakest of `(E-N1)--(E-N3)` for `x>=16` is `(E-N1)`, already greater than 373 at x=16. Since the square in `(E-SQ)` is nonnegative,

> `Phi-3omega >373/8 >46 >32`.                            `(E-GAP)`

This contradicts `(E-REQ)`.

Therefore:

> **TWO-X-HOLE EVENTUAL CLOSURE.** In the core-saturated exact second-strict two-X-hole branch with `y>=2`,
>
> **no graph exists for `x>=16`.**                       `(2X-X16-CLOSED)`

The only unclosed two-X-hole configurations have

> **`4<=x<=15`.**                                         `(2X-FINITE-HEAD-TAIL)`

This is a finite **head-count tail**, not a bounded parameter-box proof: p, y and omega were not bounded in the argument.

## 5. Significance

The two-X-hole arm is no longer an asymptotic obstruction. Its entire sufficiently-large-head regime is analytically closed using physical witness routing and the exact rooted/score ledger.

The remaining `4<=x<=15` tail can be retained for later structural cleanup, but it should not dominate the eventual theorem programme. The next asymptotic priority should return to whichever second-strict or loaded-buffer branch can still support unbounded x, while keeping the zero-positive-rigid-cut interface caveat explicit.

## 6. Audit boundary

This is same-session candidate mathematics. Hostile replay should focus on:

1. the margin accounting `A<=A_0+2M-2F_H`, `B<=B_0+3M-2F_H`;
2. the treatment of repeated versus distinct hole codes in M;
3. the completed-square lower bound for `Phi-3omega`.

The proof intentionally ignores the stronger Hamming-slot and outside-slack surcharges, so any correction there cannot be needed to make the stated contradiction work.