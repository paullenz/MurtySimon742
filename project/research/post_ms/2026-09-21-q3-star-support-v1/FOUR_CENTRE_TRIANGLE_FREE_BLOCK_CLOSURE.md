# Triangle-free parity/star blocks cannot exceed the candidate bound

21 September 2026. Internally proved at Q3-antipodal-transversal, exactly-four-centre parity-plane scope; external review open.

## Theorem

Let the four star centres be one parity plane. Write `t` for the total coordinate population, `r,q` for the two parity populations, `s` for the star population, `w=r+q`, and `W=w+s`. If the graph induced by the parity and star vertices is triangle-free, then

    m <= M(n)=floor((n-1)^2/4)+1.

Consequently every counterexample surviving in this four-centre branch contains a triangle entirely inside its parity/star block. This conclusion is independent of the invalidated matching-one and one-tree-component conjectures.

## Coordinate capacity

At least five of the six coordinate codes occur. Group the six populations into the three complementary pairs and let

    C=sum_i x_i y_i.

For fixed total `t`, positivity of at least five populations gives

    C <= floor((t-3)^2/4)+1.                 (1)

Indeed, if exactly five populations are positive, select the complementary pair receiving the largest movable mass. The other three mandatory vertices leave total `t-3` in that pair, whose product is at most `floor((t-3)^2/4)`; the other complete pair contributes at most one after moving all excess to the selected pair. If all six populations are positive, the analogous bound is `floor((t-4)^2/4)+2`, which is no larger than (1) for `t>=6`.

Raw edge criticality also gives two independent bounds on all coordinate-incident A-edges:

    E_coord <= rt,
    E_coord <= 2C <= 2 floor((t-3)^2/4)+2.   (2)

The first uses that coordinate vertices can meet only `P0`; the second is the complementary-pair charge from `FOUR_CENTRE_RESIDUAL_DEFECT_GATE.md`.

## Triangle-free closure

Let `B` be the number of edges induced by the `W` parity and star vertices. Mantel's theorem gives

    B <= floor(W^2/4).

The exact Q3 skeleton formula says it suffices to prove

    E_coord+B <= floor((t+W)^2/4)-3.          (3)

Put

    R=tW/2+t^2/4-4.

The floor inequality `floor X-floor Y >= floor(X-Y)` yields

    floor((t+W)^2/4)-floor(W^2/4)-3 >= R.    (4)

Both sides of the desired comparison are integral, so it is enough to bound `E_coord<=R`.

If `5<=t<=2W+6`, use the second bound in (2). Its real upper relaxation differs from `R` by

    R-((t-3)^2/2+2)
      = -t^2/4+t(W/2+3)-21/2.

This is concave in `t`, so its minimum on the interval is at an endpoint. At `t=5` it equals `(10W-7)/4`; at `t=2W+6` it equals `3W-3/2`. Both are positive.

If `t>2W+6`, use `E_coord<=rt` and `r<=w`. Then

    R-rt >= t(t-2w+2s)/4-4.

Since `t>2(w+s)+6`, the final expression is positive (indeed `t-2w+2s>4s+6`, and `s>=4`). Thus `E_coord<=R` in both cases. Combining (4) with Mantel proves (3), hence the theorem.

## Consequence and next target

The exact survivor wedge now has a structural, rather than merely scalar, extra condition: its parity/star block contains a triangle. Same-parity edges are allowed, so this does **not** yet force the triangle to use a star. The next raw-criticality task is to split parity-only triangles from star-containing triangles and charge the relevant substitution or bridge losses back into the budget `D(u,s)`.

## Trust boundary

The result concerns the already reduced Q3 parity-plane branch with exactly four centre codes, not arbitrary D2C graphs or supports with five or more centres. The five-coordinate premise and the coordinate charge are previously proved raw-criticality statements in this package. No selected/Hall source-tuple premise is used.
