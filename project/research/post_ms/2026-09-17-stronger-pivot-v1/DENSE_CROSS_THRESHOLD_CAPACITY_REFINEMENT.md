# Dense-cross threshold capacity refinement

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate refinement; external review open. This note sharpens the ratio-gap argument in `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`. The earlier `63/16` bound remains valid but is superseded here by the cleaner stronger constant

> `u < (31/8)p`

for sufficiently large above-`M(n)` candidates with fixed `lambda` in the linear-unmatched near-full regime.

The improvement comes from keeping the exact capacity of the low-beta-load A-vertices instead of discarding their contribution.

---

## 1. Exact threshold capacity lemma

Retain

- beta load `ell_x=|I_x|` for `x in A`;
- U-degree `d_U(x)`;
- coordinate imbalance `d_i=u_i^0-u_i^1`;
- total beta load `B=sum_x ell_x`;
- cross-edge count `s=sum_x d_U(x)`;
- squared imbalance `H=sum_i d_i^2`.

The loaded-witness side-occupancy lemma gives, for every `i in I_x`,

> `d_U(x)-1 <= (u+|d_i|)/2`.                             (1.1)

Fix any real threshold `t>0` and put

> `J_t={i:|d_i|>=t}`, `j_t=|J_t|`.                       (1.2)

By the squared-imbalance ledger,

> `j_t <= H/t^2`.                                        (1.3)

Let

> `L_t={x in A:ell_x>j_t}`, `l_t=|L_t|`.                (1.4)

Every `x in L_t` uses at least one coordinate outside `J_t`, so (1.1) gives

> `d_U(x) <= (u+t)/2+1`.                                 (1.5)

For `x notin L_t`, only the trivial `ell_x<=j_t` is used. Since every A-vertex has `ell_x<=p`,

> `B <= l_t p+(a-l_t)j_t`
>
> `  =a j_t+l_t(p-j_t)`.                                (1.6)

Whenever `j_t<p`, this yields the exact lower bound

> `l_t >= (B-a j_t)/(p-j_t)`,                            (1.7)

with the right side replaced by zero if negative and by its ceiling when an integer bound is desired.

If also `u>t+2`, the bound (1.5) is strictly smaller than the trivial U-degree cap `u`. Therefore

> `s=sum_x d_U(x)`
>
> ` <=l_t[(u+t)/2+1]+(a-l_t)u`
>
> ` =au-l_t(u-t-2)/2`.                                  (1.8)

Combining (1.7)--(1.8) gives:

> **THRESHOLD CAPACITY LEMMA.** For every `t>0` with `j_t<p` and `u>t+2`,
>
> `s <= au - (u-t-2)/2`
>
> `       * max(0,(B-a j_t)/(p-j_t))`.                  (1.9)

Together with `j_t<=H/t^2`, this is a finite-parameter bridge from the Hamming-energy budget to an upper bound on the dense A--U layer. It is not asymptotic and does not require choosing `t` in advance.

---

## 2. Asymptotic specialization

Now assume an above-`M(n)` sequence with

> `p -> infinity`, `lambda` fixed, `u=rho p+o(p)`,       (2.1)

in the linearly-unmatched regime.

The preceding note gives

> `rho<=4+o(1)`,                                         (2.2)

and the exact dense-cross Hamming budget gives, for every subsequential limit `rho<=4`,

> `H <= rho(4-rho)p^3+O(p^(5/2))`.                       (2.3)

Also the preserved Hall/slack bounds give

> `a=(rho+2)p+o(p)`,                                     (2.4)
>
> `B>=rho p^2-o(p^2)`,                                   (2.5)
>
> `s=rho(1+rho)p^2+o(p^2)`.                              (2.6)

Choose

> `t=(7/5)p`.                                             (2.7)

Writing `j=j_t/p`, (1.3) and (2.3) give

> `j <= (25/49)rho(4-rho)+o(1)`.                        (2.8)

Put `l=l_t/p`. The **sharp** beta-capacity count (1.7), rather than the cruder bound used in the predecessor note, gives

> `l >= [rho-(rho+2)j]/(1-j)+o(1)`.                     (2.9)

For the ratios considered below the displayed numerator is positive and `j<1`.

Equation (1.8) becomes

> `s/p^2`
>
> `<=rho(rho+2)`
>
> ` -(rho-7/5)/2 * [rho-(rho+2)j]/(1-j)+o(1)`.          (2.10)

But (2.6) requires `s/p^2=rho(1+rho)+o(1)`. Hence a necessary asymptotic condition is

> `(rho-7/5)/2`
>
> ` * [rho-(rho+2)j]/(1-j) <= rho+o(1)`.                (2.11)

The left side decreases as `j` increases, so use the maximum permitted value from (2.8):

> `j=(25/49)rho(4-rho)`.                                (2.12)

After subtracting `rho`, (2.11) becomes the rational function

> `G(rho)`
>
> `= rho(125rho^3-675rho^2+595rho+567)`
>
> `  / [10(25rho^2-100rho+49)] <= o(1)`.                (2.13)

On the interval `[31/8,4]`, the denominator is positive because it is exactly `49[1-j]`.

At the clean endpoint

> `rho=31/8=3.875`,

one has

> `G(31/8)=54343/503680>0`.                             (2.14)

The cubic numerator

> `N(rho)=125rho^3-675rho^2+595rho+567`

is strictly increasing on `[31/8,4]`, since

> `N'(rho)=5(75rho^2-270rho+119)>0`                     (2.15)

there, and `N(31/8)=5259/512>0`. The denominator stays positive. Thus `G(rho)>0` throughout `[31/8,4]`.

This contradicts (2.13) by a fixed positive margin for all sufficiently large `p`.

Therefore:

> **SHARPENED EXPLICIT RATIO GAP — internal candidate.**
>
> For every fixed `lambda`, every sufficiently large above-`M(n)` near-full partial-Boolean candidate in the linear-unmatched regime satisfies
>
> `u < (31/8)p`.                                        (2.16)

This improves the predecessor `63/16` constant from a gap of `1/16` below four to a gap of `1/8` below four.

The constant `31/8` is still not numerically optimized. The point is that it follows from a short exact threshold argument with comfortable positive margin, rather than from a fitted computation.

---

## 3. Why the refinement is structurally useful

The threshold lemma (1.9), not merely the number `31/8`, is the reusable result. It says that the same squared coordinate imbalance `H` must simultaneously support:

1. enough highly imbalanced fibres to host the beta target sets of low-capacity witnesses; and
2. enough high-U-degree A-vertices to realise the cross density forced by unmatched degree slack.

The proof therefore turns the beta-reuse geometry into a direct **cross-edge capacity bound**. Future work should optimize (1.9) jointly with the exact budget

`Z+H/2 <= p u(2p-lambda-u/2)+(u-p)h_alpha+2pq+pE_U`

rather than optimize the scalar constant in isolation. A successful joint optimization may convert the present ratio exclusion into a direct lower bound on `E_U+L_A`, which is the actual second-extremal scorecard.

The order-12/32 `X_3` negative control remains untouched because it has `u=0`.