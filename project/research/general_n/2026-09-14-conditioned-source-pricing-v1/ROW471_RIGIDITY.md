# Row 471 rigidity: two conditioned branches hand-closed

14 September 2026. **Exact hand consequence of the conditioned source-price branch bounds plus the existing receiver box and positive-label endpoint forcing. Internally integer-checked; external mathematical review OPEN.** This closes two `e_L` branches of one synthetic relaxed profile. It does **not** exclude row 471 as a whole, change the 707/713 sample count, change the canonical frontier, or prove graph realizability/nonrealizability beyond the stated projection.

## Setup

For original synthetic row 471,

```text
a=21, b=25, t=1, D0=0, Esel=47,
label demands = 1^5, 2^4, 3^12.
```

Take the conditioned low block `L={i:s_i<=2}`. Its base demand is

```text
S_L = 5*1+4*2 = 13.
```

Exactly nine sources have `rho_u=3`, namely

```text
u = 5,9,10,11,12,13,16,19,23,
```

and their row sums total 45. They are the **only** sources eligible for the twelve demand-three labels.

For a source pressure `d_u=(p_u-rho_u+1)_+`, every selected positive-demand label has excess at least `d_u`. All labels in this profile are positive-demand.

## Branch `e_L=39`

Here high-block excess is

```text
H = Esel-e_L = 8.
```

The twelve high labels therefore contain exactly `36+8=44` selected incidences. The nine high-eligible sources have 45 selections in total, so **exactly one** of their selections lies in the low block.

The conditioned receiver box has total free capacity 22, so at least

```text
96-22 = 74
```

pressure units are required. Grouping pressure capacity by its charge cost `q_u` gives

```text
cost q:       1   2   3   4   5   6   7
capacity:     8  20  20  14  12   2   6
```

The cheapest 74 units are exactly all units of costs 1 through 5 and cost

```text
224.
```

The source-priced selected-incidence bound for this SAME branch gives

```text
C=sum_u q_u d_u <=225.
```

Consequently several low-cost capacities are forced. If source 9 (`q=2`) had `d_9<=3`, the cheapest 74 units would cost at least 228. If source 23 (`q=3`) had `d_23<=3`, they would cost at least 227. If source 13 (`q=4`) had `d_13<=1`, they would cost at least 226. Therefore

```text
d_9>=4, d_23>=4, d_13>=2.
```

Their row sums are respectively 2,3,4. Across these three sources there can be at most the single low-block selection available to all nine high sources. Even allowing **maximal overlap** among their high-label choices, the least high excess occurs by using that low slot on source 23 or source 13:

```text
high counts 2,2,4 at pressures 4,4,2 -> 4+4+2+2 = 12,
or
high counts 2,3,3 at pressures 4,4,2 -> 4+4+4 = 12.
```

Every other allocation costs at least as much. Thus the branch requires at least 12 high-label excess units, but has only 8:

> **12 > 8. Contradiction.**

So `e_L=39` is excluded.

## Branch `e_L=40`

Now high-block excess is 7, so the high labels contain 43 selected incidences and the nine high-eligible sources have exactly **two** low-block selections in total.

The receiver free capacity is again 22, hence 74 pressure units are required. The pressure-capacity table becomes

```text
cost q:       1   2   3   4   5   6   7
capacity:     8  20  20  15  12   2   6
```

The cheapest 74 units cost 223. The conditioned source-price upper bound is again 225. If source 9 had `d_9<=3`, the minimum rises to 226. If source 23 had `d_23<=2`, it rises to 228. If source 13 had `d_13<=1`, it rises to 226. Hence

```text
d_9>=4, d_23>=3, d_13>=2.
```

Their row sums remain 2,3,4, and there are only two low slots available among all high-eligible sources. Giving those two slots to these three sources in the most favourable possible way and nesting their high-label sets as much as possible still requires at least 10 high excess units. Two minimizing patterns are

```text
low slots (0,1,1): high counts (2,2,3), pressures (4,3,2)
    -> 4+4+2 = 10;
low slots (1,0,1): high counts (1,3,3), pressures (4,3,2)
    -> 4+3+3 = 10.
```

But this branch has only 7 high excess units:

> **10 > 7. Contradiction.**

So `e_L=40` is excluded.

## Verification and scope

[`verify_row471_rigidity.py`](verify_row471_rigidity.py) independently rechecks the complete integer arithmetic: the receiver pressure requirement, exact minimum charge with the stated source pressure weakened, the number of high-source low slots, and the minimum excess possible under maximally overlapping high-label sets. It records contradictions `12>8` and `10>7`.

The conditioned source-price scan had left row 471 branches

```text
39,40,41,42,43,47.
```

This hand rigidity step reduces that list to

```text
41,42,43,47.
```

No claim is made about those four branches here. The next priority is to test them using the stronger destination-label / shared residual-neighbourhood coupling, while preserving complete branch coverage and the exact reasons each earlier branch was removed.
