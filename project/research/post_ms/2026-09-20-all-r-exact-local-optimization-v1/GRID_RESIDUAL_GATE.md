# Grid-compressed rooted residual gate

Date: 2026-09-20

Status: internal conditional synthesis inside the literal all-R equality pinch. It compresses the residual-grid witness population into a one-dimensional d-gate and does not use finite survivor counts as proof.

## 1. Parameter-only bills from the residual grid

Assume `y>=2` and put

`h=min(g,y)`.

The residual-grid cover theorem and full cross-witness independence give, for m actually used internal-X witnesses,

`d>=m+h`,

`epsilon_{a_0}>=p+u-y-d+m+h-1`,

and, writing `J=u-k-2-d`,

`q<=Q_grid(d):=binom(u,2)-binom(k+1,2)-k-d-binom(J,2)-binom(h,2)`.

The Y-source floor remains

`L_Y=y(p-g+2)`.

Therefore the total U-score budget gives

> `E_U <= C0-max{phi(g), L_Y+p+u-y-d+m+h-1}`.          `(EU-GRID)`

## 2. Exact rooted residual compression

The rooted identity is

`r=(p-lambda)(p+u)+q+E_U`.

Every literal all-R equality-pinch survivor requires `r>=a`. Combining the two preceding physical upper bounds yields the necessary one-dimensional gate

> `a <= R_grid(d,m)`,                                    `(R-GRID)`
>
> `R_grid(d,m)=(p-lambda)(p+u)+Q_grid(d)`
> ` + C0-max{phi(g), L_Y+p+u-y-d+m+h-1}`,

for at least one integer

> `m+h<=d<=u-k-2`.                                      `(d-RANGE)`

No witness-type variables remain in `(R-GRID)`. For the dominant `e(X)=0` slice, `m=0`, so the whole grid/q/a0/residual interaction reduces to testing a single integer d in

> `h<=d<=u-k-2`.

This is a structural compression, not an asymptotic conclusion.

## 3. Immediate impossibility criteria

The all-R pinch is impossible whenever any one of the following holds:

1. `u-k-2<h` (there are too few z-nonneighbours even to host a residual-grid cover);
2. `max_{h<=d<=u-k-2} R_grid(d,0)<a` in the `e(X)=0` slice;
3. more generally, for a fixed internal witness population m, `max_{m+h<=d<=u-k-2}R_grid(d,m)<a`.

Because increasing m both raises the minimum admissible d and raises the a0 score bill, the m=0 gate is the weakest member of this family. Thus any parameter row failing the m=0 gate is excluded for every m.

## 4. Why this helps the next proof step

The previous typed witness system has several local variables. `(R-GRID)` shows that, after the purely structural head-cover and independence theorems are applied, their unavoidable effect on the rooted residual ledger is already visible through the single physical parameter d. This is the right interface for an eventual proof: one can now seek a closed analytic upper bound on `max_d R_grid(d,0)` rather than treating the bounded typed scan as evidence.

The next algebraic target is to maximize this piecewise-quadratic integer function exactly, with the switch coming only from the `max{phi(g),...}` term. If that maximum remains above a on an unbounded family, the family should be classified rather than hidden by further scalar relaxations.
