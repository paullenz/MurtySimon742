# Directional beta-fibre moment capacity and the ratio-two barrier

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural theorem; external mathematical review open. This note strengthens `DENSE_CROSS_MOMENT_CAPACITY_THEOREM.md`. The previous threshold-free argument used only the absolute coordinate imbalance seen by a beta-loaded witness. Here the source side of each selected P--U obligation is retained. That directional information gives a first-moment inequality stronger than the Jensen bound and moves the fixed-`lambda` linear-unmatched frontier from `2+sqrt(2)` to `2`.

The published order-12/32 `X_3` graph has `u=0` and is untouched.

---

## 1. Setup

Retain the near-full partial-Boolean notation:

- `p` tight antipode fibres;
- `U`, `|U|=u`, the unmatched part of `B=N(v)`;
- `A`, `|A|=a=2p+u-lambda-1`;
- `q=e(U)`, `s=e(A,U)`;
- `epsilon_z=b-d(z)`, `E_U=sum_{y in U}epsilon_y`;
- `ell_x=|I_x|` the beta load of `x in A`;
- `d_x=d_U(x)`;
- `B=sum_x ell_x=pu-h_alpha`;
- `H=sum_i d_i^2`, where `d_i=u_i^0-u_i^1` is the U-code imbalance in tight fibre `i`.

The exact unmatched-slack identity is

` s=u(p+u-1)-2q-E_U`.                                    (1.1)

For each coordinate `i`, let

`h_i^0`, `h_i^1`

be the numbers of alpha-oriented P--U obligations whose unmatched source lies on sides `0` and `1` of that fibre. Thus the beta-oriented source counts are

`r_i^0=u_i^0-h_i^0`, `r_i^1=u_i^1-h_i^1`.               (1.2)

---

## 2. Directional side capacity inside one fibre

Fix coordinate `i`.

If a beta-oriented obligation has unmatched source `y` on side `0`, its selected A-witness `x` chooses side `1`. By beta-reuse criticality, every U-neighbour of `x` other than the designated source `y` also lies on side `1`. Therefore

`d_U(x)<=u_i^1+1`.                                       (2.1)

Similarly, a beta obligation sourced on side `1` has witness degree

`d_U(x)<=u_i^0+1`.                                       (2.2)

The witnesses selected by distinct beta obligations in one fibre are pairwise distinct. For the same matched target this is beta-target injectivity; a single A-vertex cannot certify obligations to both tight mates because it chooses exactly one endpoint of the fibre.

Hence

`sum_{x: i in I_x} d_x`

` <= (u_i^0-h_i^0)(u_i^1+1)`

`    +(u_i^1-h_i^1)(u_i^0+1)`.                          (2.3)

Define the nonnegative directional alpha penalty

`P_alpha`

`=sum_i [h_i^0(u_i^1+1)+h_i^1(u_i^0+1)]`.               (2.4)

Since

`2u_i^0u_i^1=(u^2-d_i^2)/2`,

summing (2.3) over the `p` fibres gives the exact coarse directional bound

> **DIRECTIONAL BETA-FIBRE MOMENT BOUND**
>
> `W:=sum_x ell_x d_x`
>
> `<=p(u^2/2+u)-H/2-P_alpha`.                            (DFM)

In particular,

`W<=p(u^2/2+u)-H/2`.                                     (2.5)

This is strictly stronger than applying the absolute-value side-occupancy inequality through Jensen.

---

## 3. The missing product appears exactly

Put

`J=sum_x (p-ell_x)(u-d_x)>=0`.                           (3.1)

For each `x`,

`ell_x d_x = u ell_x+p d_x-pu+(p-ell_x)(u-d_x)`.

After summing,

> `W=uB+ps-pua+J`.                                       (3.2)

Thus `J` is not an auxiliary relaxation: it is the exact defect in the earlier lower bound `(MW)`.

Combine (3.2) with `(DFM)`:

`J+H/2+P_alpha`

`<=p(u^2/2+u)-uB-ps+pua`.                                (3.3)

Now substitute

`B=pu-h_alpha`,

`a=2p+u-lambda-1`,

and (1.1). Direct simplification gives the main finite budget:

> **DIRECTIONAL DEFICIENCY--HAMMING BUDGET**
>
> `J+H/2+P_alpha`
>
> `<= p u(p+1-lambda-u/2)`
>
> `   +u h_alpha+2p q+pE_U`.                             (DHB)

Every term on the left is nonnegative.

Dropping the left side therefore gives the necessary inequality

> `u(u/2-p-1+lambda)`
>
> `<= (u/p)h_alpha+2q+E_U`.                              (3.4)

This is the new ratio driver.

---

## 4. Fixed-lambda consequence: limsup u/p <= 2

Assume an above-`M(n)` sequence with fixed `lambda` and `u=Theta(p)`.

The preserved switching/slack machinery gives

`mu_alpha=O(sqrt(p))`,

`h_alpha<=mu_alpha a=O(p^(3/2))`,

`q<= (mu_alpha+1)a^2/p=O(p^(3/2))`,

and by `(GS-A)`

`E_U=O(p)`.

Equation (3.4) then gives

`u(u/2-p-1+lambda)=O(p^(3/2))`.                          (4.1)

The previous moment theorem already places `u=O(p)`, so (4.1) yields

> **DIRECTIONAL RATIO-TWO THEOREM — internal candidate.**
>
> For every fixed `lambda`, every sufficiently large above-`M(n)` near-full candidate in the linearly-unmatched regime satisfies
>
> `u <= 2p+2(1-lambda)+O(sqrt(p))`.                       (4.2)

In particular,

> `limsup u/p <= 2`.                                      (4.3)

This supersedes the old `2+sqrt(2)` asymptotic endpoint.

No claim is made here for arbitrary growing `lambda`.

---

## 5. Stability at the ratio-two frontier

The finite budget is more useful than the ratio alone.

Suppose `lambda` is fixed and `u=2p+O(sqrt(p))` along an above-threshold sequence. The same preserved bounds imply that the right side of `(DHB)` is `O(p^(5/2))`. Therefore

> `H=O(p^(5/2))`,                                        (5.1)
>
> `J=O(p^(5/2))`,                                        (5.2)
>
> `P_alpha=O(p^(5/2))`.                                  (5.3)

Thus the endpoint forces two simultaneous stability statements:

1. the U-code columns are balanced in squared energy;
2. the beta deficit `p-ell_x` and U-degree deficit `u-d_x` have only `O(p^(5/2))` total product.

The latter is the precise algebraic origin of the two-population phenomenon developed in the companion note `RATIO_TWO_POLARIZATION_AND_SOURCE_PAIR_STABILITY.md`.

---

## 6. Trust boundary

- `(DFM)` is a hand count using the source side of each selected beta obligation and fibrewise witness injectivity.
- `(DHB)` is exact algebra after `(DFM)`.
- The `O(sqrt(p))` error in (4.2) uses the already-preserved fixed-`lambda` high-complexity estimates; no new finite scan is substituted for proof.
- The result concerns the unmatched/errorful antipode branch only.
- The order-12/32 `X_3` control has `u=0` and remains explicitly allowed.
- No all-order or global eventual second-extremal theorem is claimed.
