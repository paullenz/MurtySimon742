# Counterexample: consecutive target neighborhoods do not make contiguous source-band cuts sufficient

14 September 2026. **Preserved red-team failure.** This note prevents a false strengthening of [`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md).

## Tempting but false claim

The staircase-band relaxation has ordered source bands and every target type is compatible with an interval of band indices. It is tempting to infer:

> If the band flow is infeasible, then some **contiguous interval of source bands** violates its Hall cut.

That statement is false, even with a band system arising from a valid sharp-hardness up-set of `(q,c,P)` types.

## Type table

Take six type classes, all of multiplicity one:

| type | `(q,c,P)` | selected? |
|---:|---|:---:|
| 0 | `(0,2,4)` | no |
| 1 | `(3,3,1)` | yes |
| 2 | `(3,3,4)` | yes |
| 3 | `(3,5,3)` | yes |
| 4 | `(4,6,2)` | yes |
| 5 | `(4,7,3)` | no |

The selected set `{1,2,3,4}` is an up-set under the sharp order

```text
x >=_* y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
```

Its minimal generators, ordered by cross degree, are

```text
g_1=(3,3,1),
g_2=(3,5,3),
g_3=(4,6,2).
```

The staircase bands are therefore

```text
B_1={types 1,2}: M_1=2, D_1=6,
B_2={type 3}:    M_2=1, D_2=3,
B_3={type 4}:    M_3=1, D_3=4.
```

## Target band intervals

Using generator compatibility, the target-band neighborhoods are:

| target type | compatible bands |
|---:|---|
| 0 `(0,2,4)` | `{1,2}` |
| 1 `(3,3,1)` | `{1,2,3}` |
| 2 `(3,3,4)` | `{1,2,3}` |
| 3 `(3,5,3)` | `{1,2,3}` |
| 4 `(4,6,2)` | `{2,3}` |
| 5 `(4,7,3)` | `{2,3}` |

Every target neighborhood is a contiguous interval, exactly as the band theorem requires.

## All seven nonempty source-band cuts

Let `F_B(J)` be the band Hall margin: target capacity available to bands `J` minus their exact band demand. Direct integer evaluation gives

| selected bands `J` | demand | capacity | `F_B(J)` |
|---|---:|---:|---:|
| `{1}` | 6 | 6 | 0 |
| `{2}` | 3 | 5 | +2 |
| `{1,2}` | 9 | 10 | +1 |
| `{3}` | 4 | 4 | 0 |
| `{1,3}` | 10 | 9 | **-1** |
| `{2,3}` | 7 | 8 | +1 |
| `{1,2,3}` | 13 | 13 | 0 |

Thus every contiguous interval of bands has nonnegative Hall margin:

```text
{1}, {2}, {3}, {1,2}, {2,3}, {1,2,3}.
```

But the disconnected set

```text
J={1,3}
```

is deficient by one.

For that cut the target contributions are

```text
type 0: 2
type 1: 1
type 2: 2
type 3: 3
type 4: 0
type 5: 1
----------------
total:  9 < demand 10.
```

## Consequence

The band relaxation has a genuine consecutive-ones incidence structure on the target side, but **band-flow feasibility cannot in general be reduced to checking only contiguous source-band intervals**.

Any further simplification must use additional Murty-Simon-specific information—such as the earlier pair-capacity, selected-incidence, demand or excess constraints—not interval convexity alone.

The valid statement from [`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md) remains unchanged: exact target-flow feasibility implies feasibility of the complete staircase-band flow, with arbitrary source-band cuts handled by max-flow/min-cut.
