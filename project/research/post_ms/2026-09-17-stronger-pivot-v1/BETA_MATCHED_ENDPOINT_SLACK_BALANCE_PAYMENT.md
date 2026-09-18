# Balanced beta fibres charge matched-endpoint slack into `L_A`

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** exact internal candidate inequality in the near-full partial-Boolean branch; external review open.

This note combines the exact beta-side hole identity with the directional alpha/beta bookkeeping. It gives a direct global payment into `L_A` whenever beta obligations occupy both sides of many tight fibres. Unlike the current ratio theorems, the inequality retains the matched-endpoint slack `lambda+1` explicitly and is therefore a plausible bridge toward weakening the fixed-`lambda` restriction.

---

## 1. Fibre notation

For tight fibre `i`, write its two matched endpoints as `q_i^0,q_i^1`, and put

`e_i^s = epsilon_{q_i^s}=b-d(q_i^s)`.

The tight-pair degree identity gives

> `e_i^0+e_i^1=lambda+1`.                                (1.1)

Let

`u_i^s=|{y in U:c(y)_i=s}|`.

As in the directional beta-fibre note, let `h_i^s` be the number of alpha-oriented P--U obligations whose unmatched source lies on side `s`. Then the beta-oriented source counts are

`r_i^s=u_i^s-h_i^s`.                                     (1.2)

Write

`h_i=h_i^0+h_i^1`,

`h_alpha=sum_i h_i`,

and `d_i=u_i^0-u_i^1`, `H=sum_i d_i^2`.

---

## 2. Exact beta-side slack charge

Consider a beta obligation in fibre `i` whose source lies on side `0`. Its matched target is `q_i^0`, while the selected A-witness chooses the tight mate `q_i^1`. The beta-side hole identity gives

`epsilon_x>=e_i^1`.

Similarly, a beta obligation sourced on side `1` forces

`epsilon_x>=e_i^0`.

Summing over all beta targets of each A-vertex and then over `A`, exactly as in the preserved beta-side charge inequality,

> `p L_A >= sum_i (r_i^0 e_i^1+r_i^1 e_i^0)`.            `(BES1)`

This is already useful because it retains the directional endpoint slack rather than discarding it.

---

## 3. Balanced-fibre lower bound

For nonnegative `e_i^0,e_i^1`,

`r_i^0 e_i^1+r_i^1 e_i^0`

`>= (e_i^0+e_i^1) min(r_i^0,r_i^1)`

`= (lambda+1) min(r_i^0,r_i^1)`.                         (3.1)

Also

`min(r_i^0,r_i^1)
 >= min(u_i^0,u_i^1)-h_i`.                               (3.2)

Since

`min(u_i^0,u_i^1)=(u-|d_i|)/2`,

summing (3.1)--(3.2) and using `(BES1)` gives the exact coarse payment

> **BALANCED BETA ENDPOINT-SLACK PAYMENT**
>
> `p L_A`
>
> `>= (lambda+1)[(pu-sum_i |d_i|)/2-h_alpha]`.           `(BES2)`

Equivalently,

> `L_A >= (lambda+1)
>          [u/2-(sum_i|d_i|)/(2p)-h_alpha/p]`.           `(BES3)`

The right side may be replaced by its positive part.

By Cauchy--Schwarz,

`sum_i|d_i|<=sqrt(pH)`,

so

> `L_A >= (lambda+1)
>          [u/2-(1/2)sqrt(H/p)-h_alpha/p]`.              `(BES4)`

Again the positive part may be taken.

---

## 4. Interpretation

The inequality has the correct limiting behaviour in the hardest layer:

- at `lambda=-1`, every tight endpoint has zero slack and `(BES2)` becomes vacuous;
- for `lambda>=0`, balanced beta traffic across a fibre cannot avoid paying A-side degree slack, irrespective of how the `lambda+1` endpoint slack is split inside the tight pair.

At any regime where

`sum_i|d_i|=o(pu)` and `h_alpha=o(pu)`,

one gets

> `L_A >= (lambda+1)(u/2-o(u))`.                         (4.1)

Thus the nearly balanced Hamming regimes produced by the directional moment machinery automatically convert positive `lambda` into scorecard payment.

In particular, along the now-excluded fixed-`lambda` ratio-two endpoint one would have

`L_A >= (lambda+1)(p-o(p))`.

The point of `(BES2)` is not that endpoint itself, but that the same term survives when `lambda` is allowed to vary.

---

## 5. Strategic use

The next global attack can retain `(BES2)` alongside

- the scorecard `E_U+L_A`;
- the directional deficiency--Hamming budget `(DHB)`;
- the source-tuple capacity hierarchy `(FDPr)`.

The three inequalities price different escape mechanisms:

1. large Hamming imbalance is visible in `H` and `sum|d_i|`;
2. alpha diversion is visible in `h_alpha`;
3. balanced beta traffic with positive matched slack is paid directly into `L_A`.

This gives a plausible trichotomy for removing or weakening the fixed-`lambda` assumption, rather than treating growing `lambda` by a new case enumeration.

---

## 6. Trust boundary

- `(BES1)` is the preserved beta-side hole charge with the source side retained.
- `(BES2)`--`(BES4)` are elementary exact inequalities from `(BES1)` and the tight-pair slack identity.
- No new global eventual theorem is claimed.
- The order-12/32 `X_3` graph has `u=0` and is untouched.
- The separate `Q=0` / false-twin-core branch remains open.