# Cross-certificate grid-cover dichotomy

Date: 2026-09-20

Status: **internal conditional structural sharpening** inside the literal all-R equality pinch. This note uses only the raw X--Y certificate classification already preserved in `ALL_R_EXACT_LOCAL_OPTIMIZATION.md` and keeps the 20 September audit boundary unchanged.

## 1. Residual grid after maximal core credit

For `y>=2`, every edge of the complete X--Y cut must be U-certified. The k common-core witnesses have k distinct X-heads and together can certify at most the ky cells in those k X-rows.

To obtain the weakest outside-witness requirement, grant those k rows completely for free. There remain exactly

> `g=x-k`

residual X-rows and y Y-columns, hence a complete residual certificate grid of

> `R=gy`

cells which must be certified by outside witnesses among the d z-nonneighbours.

A `bar C` outside witness has one graph-fixed Y-head, so inside the residual grid it can cover cells in **one column only**, at most g cells.

A `bar d` outside witness has one graph-fixed X-head, so inside the residual grid it can cover cells in **one row only**, at most y cells.

Thus the relevant per-witness capacities for the residual problem are g and y, not x and y.

## 2. Row-or-column cover dichotomy

Let `s_C` be the number of used outside `bar C` witnesses and `s_D` the number of used outside `bar d` witnesses.

Suppose fewer than g residual rows have a `bar d` witness and fewer than y columns have a `bar C` witness. Then choose a residual row with no D-type witness and a column with no C-type witness. Their intersection cell has no possible outside certificate, contradiction.

Therefore every valid certificate cover satisfies the sharp head-coverage dichotomy

> `s_D >= g` **or** `s_C >= y`.                         `(GRID-DICH)`

In particular

> `s_C+s_D >= min{g,y}`.                                `(GRID-POP)`

Since the internal-X witness population is disjoint from the cross population,

> `d >= m+min{g,y}`                                     `(d-GRID)`

for `y>=2` whenever m internal-X witnesses are used.

This is stronger in physical meaning than the earlier scalar `d max{x,y}>=gy` bound: it identifies the necessary head coverage, not merely total load.

## 3. Residual typed load constraints

If `R_C,R_D` are the selected loads assigned to the two outside types, then the exact residual-grid capacities are

> `R_C+R_D=gy`,
>
> `s_C<=R_C<=s_C g`,
>
> `s_D<=R_D<=s_D y`.                                   `(GRID-LOAD)`

These should replace the relaxed `R_C<=s_C x` bound when the selected load is explicitly the residual `gy` grid.

The existing type-aware slack and physical-hole bills remain valid:

`P_cross >= [R_C-s_C[x-p+1]_+]_+ + R_D+s_D(p-y-1)`,

`Z_X >= Z_X^0+NJ+e+m+R_C+s_D(x-1)`,

`Z >= Z_0+NJ+e+m(y+1)+gy+s_C(y-1)+s_D(x-1)`.

## 4. Focused diagnostic effect

On the same daily-audited abstract parameter box, the focused typed `e(X)=0` replay with `(GRID-DICH)` and `(GRID-LOAD)` leaves

> **60,552** abstract rows admitting an `e(X)=0` tuple,

split as:

- **55,945** with `y>=2`;
- **4,607** with `y=1` (unchanged because the grid theorem is not asserted there).

The preceding typed-hole replay had 62,800 `e=0` rows, so the grid-cover structure removes a further **2,248** rows from that slice.

Again this is a slice diagnostic, not a total survivor count and not realizability evidence.

## 5. Next question

The residual grid now has a clean extremal form. Near cheapest coverage must choose one of two head-saturated regimes:

1. **row-saturated:** at least one D-type outside witness for every one of the g residual X-heads;
2. **column-saturated:** at least one C-type outside witness for every one of the y Y-heads.

The next structural attack should treat these two regimes separately and ask whether the required family of same-code U-witnesses can coexist with the z-nonneighbour set and with each other without forcing additional U--U nonedges or extra A--U holes. This is more targeted than another global scalar inequality.
