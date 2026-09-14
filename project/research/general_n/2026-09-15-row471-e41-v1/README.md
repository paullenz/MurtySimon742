# Row 471, conditioned branch `e_L=41`: high-block pressure closure

15 September 2026. **Exact finite consequence inside the existing selected-incidence / common-pressure relaxation; externally unreviewed.** This closes only the conditioned `eta=2, e_L=41` branch of original synthetic row 471. It does not exclude row 471 as a whole, change the 708/713 original-sample count, change the promoted canonical frontier, or prove an unrestricted Murty–Simon statement.

## Setup

For row 471,

```text
a=21, b=25, t=1, D0=0, Esel=47,
label demands = 1^5, 2^4, 3^12.
```

Take `L={i:s_i<=2}` and the remaining conditioned branch `e_L=41`. The twelve demand-three labels therefore have total excess

```text
H = 47-41 = 6.
```

Exactly nine sources can select a demand-three label:

```text
u = 5,9,10,11,12,13,16,19,23,
q = 6,2,6,7,7,4,5,5,3.
```

Their row sums total 45. The high block has `12*3+6=42` selected incidences, so these nine sources have exactly **three** selections in the low block.

The branch-specific conditioned caps give high-source pressure ceilings

```text
D = 2,4,2,1,1,4,3,3,4.
```

As in the earlier row-471 rigidity argument, the receiver box has free capacity 22. Since total incoming mass is 96, every actual pressure vector satisfies

```text
sum_u d_u >= 96-22 = 74.
```

The sixteen sources not eligible for demand-three labels have total pressure ceiling 64, hence the nine high-eligible sources must satisfy

```text
sum_high d_u >= 10.                                      (1)
```

## Shared high-excess lemma

Let `k_u` be the number of low-block selections made by one of the nine high-eligible sources, and `h_u=q_u-k_u` its number of high-block selections. We have

```text
sum_high k_u = 3.
```

If `d_u>0`, each of its `h_u` distinct demand-three labels has excess at least `d_u`. For a fixed `(h_u,d_u)` vector, even under maximally favourable nesting of the selected high-label sets, the high block therefore needs at least

```text
B(h,d) = sum_{j>=1} max{ d_u : h_u>=j }                  (2)
```

excess units. Necessarily `B(h,d)<=6`.

The exact verifier [`verify_row471_e41.py`](verify_row471_e41.py) enumerates only the nine small integer pressure ranges above. It first applies the per-source necessary consequence

```text
k_u >= (q_u-floor(6/d_u))_+   for d_u>0,
```

then exhausts the 164 allocations of the three actual low slots. Of 55,992 cap-respecting pressure vectors with `sum d>=10`, 1,311 survive the per-source shared-slack check. Only 25 pressure/low-slot pairs satisfy the stronger common nested-excess condition (2), representing 18 distinct pressure vectors.

Across all 25 surviving pairs, the number of high-block selections made by **positive-pressure** sources is at least

```text
R = sum_{u:d_u>0} h_u >= 28.                             (3)
```

This is a tiny exact integer exhaustion, not a numerical optimiser or tolerance-based infeasibility result.

## Final hand contradiction

A positive-pressure source may select a demand-three label only if that label has positive excess. Let `m` be the number of high labels with positive excess. Their total excess is six, so `m<=6`. Their total selected degree is therefore

```text
sum_{i:e_i>0}(3+e_i) = 3m+6 <= 24.                       (4)
```

Every one of the `R` high selections counted in (3) must land in those positive-excess labels. But (3) and (4) require

```text
28 <= R <= 24,
```

a contradiction.

> **Therefore the conditioned row-471 branch `eta=2, e_L=41` is impossible in the stated selected-incidence/common-pressure relaxation.**

Together with the earlier exact closures of `e_L=39,40`, the remaining conditioned row-471 branches are now

```text
42,43,47.
```

## Scope and preservation

This argument strengthens the selected-incidence/common-pressure route before destination compatibility or the one-common-residual-neighbourhood constraint is invoked. Those stronger constraints remain the next route for `42,43,47`.

The earlier non-closures and the fact that `39,40` required a different near-equality argument remain preserved. No failed result is reclassified. Internal exact replay is not external specialist review, and this synthetic profile is not a canonical scalar state or realized graph.
