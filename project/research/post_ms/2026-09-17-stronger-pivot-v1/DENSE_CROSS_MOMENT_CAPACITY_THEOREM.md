# Threshold-free dense-cross moment capacity theorem

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural theorem; external review open. This note strengthens the threshold method in `DENSE_CROSS_THRESHOLD_CAPACITY_REFINEMENT.md`. The key point is that the loaded-witness side-occupancy inequality can be summed without choosing any imbalance threshold. A weighted Jensen argument then improves the fixed-`lambda` linear-unmatched ratio bound from `31/8` to

> `u <= (2+sqrt(2))p+O(sqrt(p))`.

No global eventual second-extremal theorem is claimed.

---

## 1. Exact moment inequality from side occupancy

Retain the near-full notation and, for `x in A`, write

- `ell_x=|I_x|` for beta load;
- `d_x=d_U(x)` for U-degree;
- `B=sum_x ell_x=B_beta`;
- `s=sum_x d_x=e(A,U)`.

For U-code coordinate `i`, write

`d_i=u_i^0-u_i^1`,

and

`H=sum_i d_i^2`.

The loaded-witness side-occupancy lemma says that for every `x` and every `i in I_x`,

> `d_x-1 <= (u+|d_i|)/2`.

Therefore

> `|d_i| >= (2d_x-u-2)_+`.                              (1.1)

Define the convex nondecreasing function

> `phi(t)=(2t-u-2)_+^2`.                                 (1.2)

Summing (1.1) over all target fibres used by `x` gives

> `ell_x phi(d_x) <= sum_{i in I_x} d_i^2`.             (1.3)

Now sum over `x in A`. For a fixed tight fibre `i`, the number

`r_i=|{x:i in I_x}|`

is exactly the number of beta-selected P--U obligations in that fibre. There is at most one such physical obligation per unmatched source, so

> `r_i<=u`.                                               (1.4)

Hence

> **MOMENT UPPER BOUND**
>
> `sum_x ell_x phi(d_x)`
>
> `<=sum_i r_i d_i^2`
>
> `<=u H`.                                                (1.5)

This is exact.

---

## 2. Beta-weighted U-degree has an exact lower bound

Put

> `W=sum_x ell_x d_x`.                                    (2.1)

For every A-vertex,

> `(p-ell_x)(u-d_x)>=0`.

Expanding gives

> `ell_x d_x >= u ell_x+p d_x-pu`.                       (2.2)

After summing over A,

> **BETA-WEIGHTED DEGREE LOWER BOUND**
>
> `W>=uB+p s-pua`.                                        (2.3)

This is the threshold-free analogue of the product ledger used in the central-triple argument.

Assume `B>0`. Since `phi` is convex, weighted Jensen with weights `ell_x/B` yields

> `sum_x ell_x phi(d_x) >= B phi(W/B)`.                  (2.4)

Because `phi` is also nondecreasing, use (2.3):

> `sum_x ell_x phi(d_x)`
>
> `>=B phi((uB+ps-pua)/B)`.                              (2.5)

Combine with (1.5):

> **THRESHOLD-FREE MOMENT CAPACITY THEOREM**
>
> `B * [ 2(uB+ps-pua)/B - u - 2 ]_+^2 <= u H`.          (2.6)

Equivalently,

> `B * [ u + 2p(s-ua)/B - 2 ]_+^2 <= uH`.               (2.7)

No asymptotics and no selected threshold are used in (2.6).

The inequality has a transparent extremal meaning. To make a quadratically dense A--U layer coexist with beta load close to `pu`, the beta-weighted A-vertices must have large U-degree. But large U-degree at every beta target coordinate forces large squared U-code imbalance, and the total available imbalance is exactly `H`.

---

## 3. Asymptotic consequence for fixed lambda

Assume an above-`M(n)` sequence with

> `p -> infinity`, `lambda` fixed, `u=rho p+O(1)`         (3.1)

(or more generally `u=rho p+o(p)` along a subsequence), with fixed positive `rho`.

The preserved high-complexity bounds give

> `mu_alpha=O(sqrt(p))`,
>
> `q=O(p^(3/2))`,
>
> `E_U=O(p)`.

Therefore alpha spill and the exact unmatched-slack identity give

> `B=pu-O(p^(3/2))`
>
> ` =rho p^2+O(p^(3/2))`,                                (3.2)

and

> `s=u(p+u-1)-2q-E_U`
>
> ` =rho(1+rho)p^2+O(p^(3/2))`.                         (3.3)

Also

> `a=(rho+2)p+O(1)`.                                     (3.4)

Substitute into the beta-weighted degree bound (2.3):

> `uB+ps-pua`
>
> `=rho(rho-1)p^3+O(p^(5/2))`.                          (3.5)

Hence

> `(uB+ps-pua)/B`
>
> `=(rho-1)p+O(sqrt(p))`.                                (3.6)

For `rho>2`, the positive part in (2.6) is therefore

> `(rho-2)p+O(sqrt(p))`.                                 (3.7)

The exact dense-cross Hamming budget from the predecessor note gives

> `H <= rho(4-rho)p^3+O(p^(5/2))`                        (3.8)

through the already-established bounded-ratio window.

Now (2.6) gives

> `rho(rho-2)^2 p^4`
>
> `<=rho^2(4-rho)p^4+O(p^(7/2))`.                       (3.9)

Divide by `rho p^4`:

> `(rho-2)^2 <= rho(4-rho)+O(p^(-1/2))`.                (3.10)

Ignoring the vanishing error, the upper root is exact:

> `rho=2+sqrt(2)`.                                       (3.11)

Since the derivative of

`(rho-2)^2-rho(4-rho)=2rho^2-8rho+4`

at `rho=2+sqrt(2)` is `4sqrt(2)>0`, the error term in (3.10) yields the quantitative form

> **MOMENT RATIO THEOREM — internal candidate.**
>
> For every fixed `lambda`, every sufficiently large above-`M(n)` near-full candidate in the linear-unmatched regime satisfies
>
> `u <= (2+sqrt(2))p+O(sqrt(p))`.                        (3.12)

In particular,

> `limsup u/p <= 2+sqrt(2) = 3.41421356...`.             (3.13)

This supersedes the explicit `31/8=3.875` ratio bound as the strongest current asymptotic statement. The `31/8` theorem remains useful because its finite threshold-capacity lemma does not rely on Jensen and may be better suited to a finite explicit-order argument.

---

## 4. Equality shape suggested by the proof

The value `2+sqrt(2)` is not a numerical fit. It comes from equating two structural costs:

- the minimum beta-weighted high-U-degree moment, asymptotically `rho(rho-2)^2`;
- the maximum squared coordinate-imbalance budget, asymptotically `rho^2(4-rho)`.

Near equality requires simultaneous near-equality in several independent steps:

1. `(p-ell_x)(u-d_x)` must be small for most beta weight, so beta-relevant A-vertices tend toward either nearly full beta load or nearly full U-degree;
2. weighted Jensen must nearly saturate, so the U-degrees seen by beta weight concentrate near `(rho-1)p`;
3. the side-occupancy sum must nearly saturate, so beta target coordinates repeatedly meet near-extremal U-code imbalances;
4. the global Hamming budget must itself nearly saturate.

This gives a concrete stability target for the next attack. Rather than classify unmatched rows, one should price the **failure of equality** in (2.2), Jensen, and (1.5) into `E_U+L_A`. If those three defects can be shown not to vanish simultaneously in a D2C graph, the ratio endpoint can be pushed further or the near-full branch can close directly.

---

## 5. Trust boundary

- (1.5), (2.3) and (2.6) are hand inequalities.
- The asymptotic step uses the already-preserved fixed-`lambda`, `u=O(p)` alpha, U-edge and slack bounds.
- The result is not asserted for arbitrary growing `lambda`.
- The published order-12/32 `X_3` graph has `u=0` and is untouched.
- No all-order second-extremal theorem is claimed.