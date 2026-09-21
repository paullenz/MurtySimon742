# Residual-one rigid one-code branch: asymptotic boundary-feasible wedge

Date: 2026-09-21

Status: asymptotic analytic consequence of `RESIDUAL_ONE_BOUNDARY_POPULATION_OBSTRUCTION.md` plus the exact above-M score ceiling. This is a necessary condition within the rigid complete one-code residual-one interface; it is not a graph construction and does not remove the upstream zero-positive-fixture caveat.

## 1. Normalized variables

Consider an unbounded residual-one sequence with

`alpha=u/p`, `beta=y/p`, `gamma=c/p`,

and suppose the small-U branch

`0<alpha<1`

persists. The raw population theorem forces

`y<=k=u-c+1`,

so asymptotically

> **`beta+gamma<=alpha`.**                                `(1.1)`

In particular `beta<=alpha`.

The exact gap parameter is

`lambda=p-y+c-1`,

hence

`ell:=lambda/p -> 1-beta+gamma`.                         `(1.2)`

From `(1.1)`,

> `ell<=1+alpha-2beta`.                                  `(1.3)`

## 2. Boundary score floor as a function of alpha

The residual-gamma/U tradeoff gives, with g the multiplicity of the sole large residual X-code as a forced reverse gamma,

`E_U+L_A >= p(p-1)-g(p-g)`,

and the nonempty U-class count gives

`g>=p-u`.

Optimizing over g and dividing by p^2 yields the asymptotic floor

> `liminf (E_U+L_A)/p^2 >= Phi(alpha)`,                  `(2.1)`

where

`Phi(alpha)=1-alpha+alpha^2` for `0<=alpha<=1/2`,

and

`Phi(alpha)=3/4` for `1/2<=alpha<1`.                    `(2.2)`

The first branch comes from the active constraint `g/p>=1-alpha`; the second from the unconstrained minimum at `g/p=1/2`.

## 3. Exact score ceiling

The preserved score ceiling is

`E_U+L_A<=C0`,

`C0=(lambda+2)(p+u)+p-A_lambda`,

with `A_lambda=lambda^2/2+o(p^2)`.

Therefore

`limsup C0/p^2`
` <= ell(1+alpha)-ell^2/2`.                              `(3.1)`

For fixed alpha this concave expression is increasing for `ell<1+alpha`. By `(1.3)`, its largest value compatible with the population theorem is attained at the boundary `ell=1+alpha-2beta`. Hence

> `limsup C0/p^2`
> ` <= (1+alpha)^2/2-2beta^2`.                           `(3.2)`

Combining `(2.1)` and `(3.2)` gives the necessary wedge inequality

> **`Phi(alpha)+2beta^2 <= (1+alpha)^2/2`.**             `(3.3)`

## 4. Explicit consequences

### 4.1 No very-small-U residual-one survivor

For `alpha<=1/2`, `(3.3)` becomes

`1-alpha+alpha^2+2beta^2 <= (1+alpha)^2/2`,

or

> **`4beta^2 <= -1+4alpha-alpha^2`.**                    `(4.1)`

The right side must be nonnegative. Therefore

> **`alpha>=2-sqrt(3)=0.267949...`.**                    `(4.2)`

Thus the rigid residual-one branch cannot support an unbounded small-U sequence with

`u/p < 2-sqrt(3)-o(1)`.

Moreover, throughout `2-sqrt(3)<=alpha<=1/2`,

> **`beta <= (1/2)sqrt(-1+4alpha-alpha^2)`.**            `(4.3)`

### 4.2 Moderate-U branch

For `1/2<=alpha<1`, `(3.3)` gives

> **`beta^2 <= alpha/2+alpha^2/4-1/8`.**                 `(4.4)`

Together with the raw population condition `beta+gamma<=alpha`, this leaves a compact two-dimensional feasible wedge for `(alpha,beta,gamma)` rather than the previous unrestricted residual-one region.

## 5. Interpretation

The boundary obstruction now separates the residual-one asymptotic problem into three sharply different regimes:

1. `alpha<2-sqrt(3)`: impossible from boundary criticality plus the score ceiling;
2. `2-sqrt(3)<=alpha<1`: only the explicit wedge `(1.1),(4.3)/(4.4)` survives;
3. `alpha>=1`: the large-U regime, which must be treated through the rooted residual/defect ledger rather than the low-U witness scarcity argument.

The corrected intermediate half-ray lies outside the wedge much earlier: it violates the exact population theorem (`y>k` while `u<p`) and is therefore completely unrealizable.

## 6. Next use

The high-value next step is to intersect this wedge with the exact rooted-Q and residual defect inequalities, keeping `gamma=c/p` rather than eliminating it. If the intersection is empty, residual dimension one is asymptotically closed within the rigid interface. If not, the optimizer gives the literal ratio profile for the next raw-criticality attack.
