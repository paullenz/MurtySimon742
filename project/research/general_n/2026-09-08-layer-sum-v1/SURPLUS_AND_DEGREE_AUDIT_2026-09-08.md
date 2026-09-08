# Adversarial audit of the cubic-to-surplus step and 13/22 assembly

8 September 2026. Internal assurance by ChatGPT/Geeps. **The full 13/22 result remains CANDIDATE; independent mathematical review remains OPEN.**

## Verdict

No blocking defect has been found in the passage

    3S^3 <= a^2 r(2r+1),   S>=r+2t

to

    t < 4a^2/81 + 1/8,

or in the exact conversion of that surplus estimate into the maximum-degree condition `Delta>=13n/22` for `n>=6`.

The audit also identifies an important limitation: the asymptotic coefficient `4/81` is **sharp if one uses only these two scalar inequalities**. Therefore a better all-order degree coefficient cannot come from polishing the final one-variable optimisation alone; it must use stronger demand/residual structure upstream.

## 1. Completing the square

From

    3S^3 <= a^2 r(2r+1)

we obtain

    r^2+r/2 >= (3/2)S^3/a^2,

hence

    (r+1/4)^2 >= (3/2)S^3/a^2 + 1/16.

For S>0 the right side is strictly larger than `(3/2)S^3/a^2`, so

    r > sqrt(3/2) S^(3/2)/a - 1/4.                 (A)

There is no loss of sign: r>=0, so r+1/4 is positive before taking square roots.

## 2. One-variable optimisation

Let `K=sqrt(3/2)` and `u=K sqrt(S)/a`. From `2t<=S-r` and (A),

    2t < S - K S^(3/2)/a + 1/4
       = (a^2/K^2) u^2(1-u) + 1/4.

For every real u>=0,

    4/27-u^2(1-u)
      = (u-2/3)^2(u+1/3) >= 0.

Since `K^2=3/2`,

    2t < 8a^2/81 + 1/4,

and therefore

    t < 4a^2/81 + 1/8.                              (B)

The factorisation is exact and covers u>1 as well; no implicit assumption that the maximiser lies in a preselected interval is needed.

## 3. Why 4/81 cannot be improved at this scalar stage

For every integer k>=1 set

    a=27k,
    S=216k^2,
    r=144k^2,
    t=36k^2.

Then

    S=r+2t,
    t/a^2=4/81.

Moreover the leading part of the cubic inequality is exact:

    3S^3 = 2a^2r^2,

so certainly

    3S^3 <= a^2r(2r+1).

Thus there is an infinite scalar family satisfying the two inputs and attaining `t/a^2=4/81` exactly. The family is **not asserted graph-realisable**. Its role is methodological: any improvement to the asymptotic coefficient must exploit information discarded before this scalar stage.

This directs future optimisation back to the threshold family, demand profile, truncated residual mass, equality rigidity, or graph structure.

## 4. Exact 13/22 conversion

Write `b=Delta` and `a=n-1-b`, so `n-b=a+1`. If

    b >= 13n/22,

then

    22b >= 13(a+b+1),
    9b >= 13(a+1),

and therefore

    b-n/2 = (b-a-1)/2 >= 2(a+1)/9.                 (C)

If `m>=floor(n^2/4)`, then

    t=m-b(n-b)
      >= floor(n^2/4)-b(n-b)
      = floor((b-a-1)^2/4).

Equivalently, accounting for parity,

    t >= (b-n/2)^2-1/4
      >= 4(a+1)^2/81-1/4.                           (D)

For a>=4, subtracting the upper bound (B) from the last expression in (D) leaves

    (4/81)(2a+1)-3/8,

which is at least `4/9-3/8>0`.

For a=2, the degree condition forces b>=5, so the exact floor identity gives t>=1, while (B) gives t<16/81+1/8<1. For a=3 it forces b>=6, again giving t>=1 while `t<36/81+1/8<1`.

For a=1 and n>=6, b=n-2>=4. Density at the balanced bound would give t>=1, whereas the one-vertex graph F has no edges and the ledger `e(F)=r+t` gives t=-r<=0.

The universal-vertex case a=0 is a star and is already strict for n>=4.

## 5. The n=5 boundary is real

The qualification n>=6 cannot simply be deleted. `K(2,3)` has

    n=5, Delta=3, e=6=floor(25/4),

and `3>=65/22`. In the scalar coordinates it has a=1 and the density-required surplus is t=0, so there is no contradiction with (B). This is a genuine boundary exception, not a weakness of the rounding argument.

## 6. Independent scalar enumeration

A new checker, `src/check_surplus_degree_adversarial.py`, independently searches the scalar consequences.

For every `1<=a<=200` and every integer `1<=S<=a(a-1)`, it finds the smallest integer r satisfying the cubic inequality and then the largest integer t satisfying `2t<=S-r`. This is the adversarial choice because smaller r and larger t are hardest for (B).

The complete domain contains 2,666,600 scalar `(a,S)` cases. Every case satisfies the strict scaled form

    648t < 32a^2+81.

The smallest observed scaled margin is 17, at `a=22, S=138, r=90, t=24`. The largest observed integer excess above `4a^2/81` is `8/81`; this finite-domain observation is not used to strengthen the theorem.

The same checker independently enumerates every integer pair `(n,b)` with `6<=n<=5000`, `b>=ceil(13n/22)` and `a=n-1-b>=1`. Across 5,107,274 cases it verifies that the density-required integer surplus is incompatible with (B). The smallest scaled contradiction margin in this domain is positive. `K(2,3)` is included as a mandatory n=5 negative control.

These finite searches test arithmetic and rounding; the universal proof is the algebra in Sections 1-5.

## 7. Research consequence

The assurance picture is now sharper. The final optimisation and degree assembly are not the place to seek a lower asymptotic threshold: `4/81` is scalar-sharp. The best next mathematical attack is therefore to retain information discarded by the cubic aggregation, especially:

* the full sequence `(W_h,z_h)` instead of collapsing it to one residual mass;
* the stronger truncated mass `r_H`;
* equality/near-equality rigidity in the threshold capacity lemma;
* simultaneous restrictions linking different demand levels to the same selected graph.

Those are the plausible routes to lowering `13/22` or eventually attacking the remaining middle-degree region.
