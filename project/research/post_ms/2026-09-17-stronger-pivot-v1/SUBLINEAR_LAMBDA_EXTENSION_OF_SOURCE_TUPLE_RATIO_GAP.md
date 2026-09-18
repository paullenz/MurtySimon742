# Extending the source-tuple ratio gap from fixed to sublinear `lambda`

**Status:** internal asymptotic reduction / candidate theorem, 18 September 2026. This note remains inside the near-full partial-Boolean branch and does **not** assert the eventual second-extremal theorem. The order-12, size-32 `X_3` hostile control has `u=0` and is untouched.

## 1. Purpose

The preserved triple-source ratio-gap theorem was stated for fixed `lambda`:

> every above-`M(n)` near-full sequence with `p->infinity`, fixed `lambda`, and `u/p` tending to a finite limit satisfies
>
> `limsup u/p < 27/14`.

The fixed-`lambda` hypothesis is stronger than the proof actually needs. The only place it entered was in making the projective-alpha, internal-U and scorecard error terms lower order than `p^3` in the directional deficiency--Hamming budget.

The switching/scorecard estimates already imply the same lower-order property whenever

> `lambda=o(p)`.

Thus the whole source-tuple ratio-gap argument extends to the sublinear-imbalance regime.

---

## 2. Scorecard size when `lambda=o(p)`

Assume an above-`M(n)` sequence with

`p->infinity`,

`u=O(p)`,

and

`lambda=o(p)`.

Recall

`a=2p+u-lambda-1=O(p)`

and

`C=S_req-2`

`=p lambda+3p+u lambda+2u-ceil(lambda(lambda+2)/2)-4`.

Because `u=O(p)` and `lambda=o(p)`, an above-threshold candidate has

> `0<=C=O(p(lambda+1))=o(p^2)`.                           `(SL1)`

The lower inequality follows because `E_U+L_A>=0` and above threshold requires `E_U+L_A<=C`.

---

## 3. High-complexity bounds become genuinely sublinear

The preserved zero-signed-subcore theorem gives

`mu_alpha<=R_*`,

where

`R_*=max(2,floor((1+sqrt(1+4C))/2))`.

By `(SL1)`,

> `R_*=O(sqrt(p(lambda+1)))=o(p)`.                        `(SL2)`

Hence

> `mu_alpha=o(p)`.                                        `(SL3)`

The preserved alpha-capacity bound gives

`h_alpha<=mu_alpha a`,

so, because `a=O(p)`,

> `h_alpha=o(p^2)`.                                       `(SL4)`

Likewise the preserved U-edge capacity theorem gives

`q <= (mu_alpha+1)a^2/p`,

and therefore

> `q=o(p^2)`.                                             `(SL5)`

Finally the scorecard itself gives

> `E_U<=C=o(p^2)`, and `L_A<=C=o(p^2)`.                  `(SL6)`

These are exactly the estimates formerly obtained from fixed `lambda`.

---

## 4. Directional Hamming budget has the same leading term

The directional deficiency--Hamming budget is

`J+H/2+P_alpha`

`<=p u(p+1-lambda-u/2)+u h_alpha+2p q+pE_U`.             `(DHB)`

Assume along a subsequence

`u/p -> rho`

for finite `rho>=0`.

By `(SL4)--(SL6)`,

`u h_alpha=o(p^3)`,

`2p q=o(p^3)`,

and

`pE_U=o(p^3)`.

Also `lambda=o(p)` gives

`p u lambda=o(p^3)`.

Since `P_alpha>=0`, `(DHB)` therefore yields exactly the same leading estimates as in the fixed-`lambda` proof:

> `J <= [rho(2-rho)/2+o(1)]p^3`,                         `(SLJ)`
>
> `H <= [rho(2-rho)+o(1)]p^3`.                           `(SLH)`

In particular a finite positive limit ratio cannot exceed `2`: if `rho>2`, the right side of `(DHB)` is negative at leading order while its left side is nonnegative.

---

## 5. The triple-source contradiction is unchanged

For `rho in (1,2]`, the preserved ratio-gap proof uses only `(SLJ)`, `(SLH)`, beta-load capacity, the side-occupancy lemma, and the exact `r=3` source-tuple capacity theorem. None of those later steps requires `lambda` to be fixed.

For completeness, the same quantities are

`gamma=rho(2-rho)`,

`L_0(rho)=[rho-(rho+2)gamma]/(1-gamma)`,

`D_0(rho)=rho(2-rho)/(rho-1)`.

The Hamming threshold argument gives at least

`[L_0(rho)-6D_0(rho)+o(1)]p`

witnesses with beta deficit at most `p/6`, while the exact triple-source capacity theorem gives at most

`(12rho^3/125+o(1))p`.

Thus feasibility still requires

`F(rho)=L_0(rho)-6D_0(rho)-12rho^3/125<=0`.

The already certified exact polynomial identity is

`F(rho)`

`=-rho(12rho^4-24rho^3-863rho^2+2250rho-1125)`

` /[125(rho-1)^2]`,

and the preserved derivative/sign check proves

`F(rho)>0`

for every

`rho in [27/14,2]`.

Therefore:

> **SUBLINEAR-LAMBDA TRIPLE-SOURCE RATIO GAP — internal candidate.**
>
> Let `p->infinity` along above-`M(n)` near-full candidates with `u=O(p)` and `lambda=o(p)`. Then every finite subsequential limit `rho=lim u/p` satisfies
>
> `rho < 27/14`.                                          `(SLRG)`

Equivalently, in the linear-unmatched near-full regime,

> `limsup u/p < 27/14`

whenever `lambda=o(p)`.

The same trust boundary as the fixed-`lambda` theorem applies; the constant `27/14` remains deliberately unoptimized.

---

## 6. Strategic consequence: a genuine scale dichotomy

The live unmatched branch can now be divided by the scale of the root imbalance, not by whether `lambda` is literally constant.

For any putative above-threshold near-full sequence with `u=O(p)` and

`limsup u/p >= 27/14`,

the new theorem forces

> `lambda` **not** to be `o(p)`.

Hence, after passing to a subsequence, there is a constant `theta>0` with

> `lambda >= theta p`.                                    `(LINLAM)`

So the only way to retain a large unmatched ratio is to enter a genuinely linearly imbalanced root regime. This is a much narrower target for the new alpha--beta coercivity inequality `(ABF)/(IPM)`: the next positive-`lambda` attack may assume that `lambda` itself carries linear scale rather than treating every slowly growing intermediate regime separately.

This is the main value of `(SLRG)`: it removes the entire mesoscopic window

`1 << lambda << p`

from the old fixed-`lambda` gap.

---

## 7. Trust boundary

- `(SL1)--(SL6)` use only preserved exact scorecard, switching-deletion, alpha-capacity and U-edge-capacity inequalities.
- The asymptotic passage requires `u=O(p)` and `lambda=o(p)` explicitly.
- The triple-source contradiction is exactly the previously audited `27/14` argument with the fixed-`lambda` error estimate replaced by `(SL4)--(SL6)`.
- No assertion is made here for `lambda=Theta(p)`; that is now the isolated positive-imbalance frontier.
- No all-order second-extremal theorem is claimed.
- The published `X_3` exception is full-tight (`u=0`) and unaffected.
