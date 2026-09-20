# Exact maximizer locations for the grid-compressed residual gate

Date: 2026-09-20

Status: internal conditional algebraic corollary of `GRID_RESIDUAL_GATE.md`.

Let

`T=u-k-2`, `h=min(g,y)`,

and fix m. The admissible interval is

`d in [m+h,T]`.

Write

`A=L_Y+p+u-y+m+h-1`,

so the score switch in `(R-GRID)` is

`max{phi(g),A-d}`.

The physical q term is

`Q_grid(d)=const-d-binom(T-d,2)`.

Its first difference is exact:

> `Q_grid(d+1)-Q_grid(d)=T-d-2`.                         `(DQ)`

On the branch `A-d>=phi(g)`, the `-max` term contributes `+d`, so

> `R_grid(d+1,m)-R_grid(d,m)=T-d-1`.                    `(DR-LIN)`

On the branch `A-d<=phi(g)`, the max term is constant, so

> `R_grid(d+1,m)-R_grid(d,m)=T-d-2`.                    `(DR-CONST)`

Consequences:

1. before the score switch, `R_grid` is increasing throughout the admissible range except possibly the final step into d=T;
2. after the switch, it is maximized at `d=T-2` or `d=T-1` whenever those values lie in the branch/domain;
3. therefore the global integer maximum can occur only at a constant-size candidate set consisting of the clipped switch neighbours and the final q-peak:

> `{ floor(A-phi(g)), floor(A-phi(g))+1, T-2, T-1 }`

intersected with `[m+h,T]`, together with an interval endpoint only when clipping removes its adjacent candidate.

Thus the existential d-search in the rooted residual gate is not genuinely long-range. It reduces analytically to at most a handful of explicit d-values, independent of the size of u.

This is useful for a future sufficiently-large argument: any unbounded survivor family of `(R-GRID)` must already survive one of these explicit endpoint/switch geometries. The next run should substitute these candidates into `(R-GRID)` and classify their asymptotic parameter balances rather than scan d numerically.
