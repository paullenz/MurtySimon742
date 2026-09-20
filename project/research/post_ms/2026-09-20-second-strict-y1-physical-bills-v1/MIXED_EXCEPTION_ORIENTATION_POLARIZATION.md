# Mixed second-strict exceptional capacity — fixed-coordinate orientation polarization

Date: 2026-09-20

Status: **same-session internal structural strengthening/correction** of the mixed-hole exceptional-capacity analysis in `SECOND_STRICT_INITIAL_REDUCTION.md`. The earlier inequality `(H-1)(s-1)<=1` is valid as a coarse capacity bound but misses a stronger graph-fixed orientation constraint. Exploiting that constraint eliminates the apparent `H=s=2` corner.

## 1. Setup

In the exact mixed second-strict branch let

- `z_0` be the unique outside vertex nonadjacent to the buffer b;
- `H` be the number of outside-certified Type-R buffer heads;
- `S_0` be the difference support of the unique X-hole `a_0` from d;
- `s=|S_0|`.

For every outside-certified Type-R head x and every `j in S_0`, the preserved radius>=2 matched-edge exhaustion says the matched edge `xq_j` must use the one exceptional physical vertex `z_0` as its singleton witness.

The two possible orientations are:

- **reverse:** `q_j -> x`, requiring `z_0q_j notin E` and `z_0x in E`, with `N(q_j) cap N(z_0)={x}`;
- **forward:** `x -> q_j`, requiring `z_0x notin E` and `z_0q_j in E`, with `N(x) cap N(z_0)={q_j}`.

The predecessor counted at most s reverse obligations and at most H forward obligations, yielding `Hs<=H+s`.

## 2. Orientation is fixed by the coordinate

For a fixed coordinate j, the physical adjacency `z_0q_j` is graph-fixed.

Therefore:

- if `z_0q_j in E`, **reverse is impossible for every head** at coordinate j; all H obligations `(x,j)` must use forward routing;
- if `z_0q_j notin E`, **forward is impossible for every head** at coordinate j; all H obligations `(x,j)` must use reverse routing.

This polarization was not used in the coarse predecessor count.

## 3. Reverse coordinates are impossible when H>=2

Suppose `z_0q_j notin E`, so coordinate j is reverse-only.

Every one of the H heads requires

`N(q_j) cap N(z_0)={x}`.

But the left-hand common-neighbour set belongs to the **single fixed physical pair** `(q_j,z_0)`. It cannot simultaneously equal two different singleton heads.

Hence a reverse-only coordinate can exist only if

> **`H<=1`.**                                             `(MIX-REVCOORD-H1)`

Thus when `H>=2`, every coordinate in `S_0` must be forward-only:

> `z_0q_j in E` for all `j in S_0`.                       `(MIX-ALL-FWD)`

## 4. Forward capacity then forces s=1

Assume `H>=2`. By Section 3 all s coordinates are forward-only.

For one fixed head x, each coordinate j would require

`N(x) cap N(z_0)={q_j}`.

Again the common-neighbour set of the fixed physical pair `(x,z_0)` is graph-fixed, so it can be a singleton matched head for at most one coordinate.

Therefore every head can support at most one forward-only coordinate, and since all s coordinates must be supported,

> **`s<=1`.**                                             `(MIX-S1-H2)`

Because `S_0` is nonempty,

> **`H>=2  ==>  |S_0|=1`.**                              `(MIX-POLAR)`

This strictly strengthens the predecessor consequence, which required `H>=3` and left the apparent corner `H=2,s=2`.

## 5. Consequences for head counts

The mixed branch always has

`H>=x-2`.

Hence:

- if `x>=4`, then `H>=2`, and `(MIX-POLAR)` gives

  > **`|S_0|=1` for every mixed second-strict configuration with x>=4`.** `(MIX-X4-S1)`

- the previously listed exceptional x=4 corner `H=2,|S_0|=2` is **empty**;
- only x=3 can have `H=1` and `|S_0|>1`.

Combining this with `X4_SINGLETON_SUPPORT_CLOSURE.md` immediately gives:

> **every mixed y=1 x=4 survivor has `n<=19`.**           `(MIX-X4-N19)`

Thus the only mixed-y1 head count not yet structurally bounded is

> **`x=3`.**                                              `(MIX-Y1-LAST-X3)`

## 6. Audit significance

This is a strengthening rather than an invalidation of the old inequality: `Hs<=H+s` remains a necessary coarse count, but it is not sharp because it permits mixing forward and reverse obligations at one coordinate even though `z_0q_j` fixes the orientation globally for that coordinate.

Hostile replay should verify only the raw witness orientation convention above. If that convention is correct, the x=4 exceptional support corner disappears before any score or pair-capacity calculation.