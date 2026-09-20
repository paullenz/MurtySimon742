# Residual-one k=2: explicit intermediate half-ray after the high-Y endpoint closure

Date: 2026-09-20

Status: **same-session method diagnostic / exact parameter ray**, conditional on the residual-one `k=2,J2=empty` interface and the hostile-replayed off-ray capacity package. This is **not a graph construction**. Its purpose is to identify the first simple scaling direction that survives the newly strengthened score/rooted package after the `y/p -> 1` endpoint has been closed.

## 1. Exact ray

For every integer `t>=2`, set

- `p=2t`,
- `c=t`,
- `y=t`, hence `g0=p-y=t`,
- `lambda=c+p-y-1=2t-1`,
- `u=c+1=t+1`,
- `x=p+1=2t+1`,
- `k=2`,
- `m=p-1=2t-1`,
- residual dimension `r=1`,
- `b=|B0|=0`, hence `C=e(B0,D)=0`.

The normalized parameters are therefore

`theta=y/p=1/2`, `kappa=c/p=1/2`, `eta=0`, `q=0`.

This is the simplest exact point well inside the intermediate-theta relaxed survivor wedge exposed by the new off-ray normalized theorem.

## 2. New off-ray score theorem leaves a large margin

The exact score ceiling is

`C0=(lambda+2)(p+u)+p-A_lambda`.

Here `lambda=2t-1` is odd and

`A_lambda=floor(lambda^2/2)+lambda+5=2t^2+4`.

Therefore

> **`C0=4t^2+7t-3`.**                                   `(HR-C0)`

Because `B0=empty`, the general Y--U capacity theorem gives

`Z_YU >= |D|(y-1)=(t+1)(t-1)=t^2-1`.

The global H/Y polarization gives the same leading baseline for total A--U holes:

`Z >= t^2-1`.

Also every U--U edge must be sourced from D and every D source has oriented U--U source capacity at most two, hence

`e(U)<=2|D|=2t+2`.

Since `p-lambda=1`, the exact rooted identity gives

`E_U=Z-u(p-lambda)-2e(U)`

and therefore

> `E_U >= t^2-5t-6`.                                    `(HR-E)`

Because `e(Y)=0`, the exact Y-side slack identity gives

> `L_Y=Z_YU-y >= t^2-t-1`.                              `(HR-LY)`

Thus the new package certifies only

> **`E_U+L_A >= 2t^2-6t-7`,**                            `(HR-SCORE-LB)`

which is far below `(HR-C0)` asymptotically. In normalized language the floor coefficient is `1/2`, while the ceiling coefficient is `1`.

So the intermediate half-ray is not a numerical boundary artefact; it has a genuine quadratic score margin.

## 3. Rooted-Q feedback also remains open

The residual-one rooted-Q necessary inequality is

`2(x+y-1)+phi(p-1)`
` <= u(p-lambda)+2(c-1)u-(c-1)c+C0`.

On the present ray,

left side
`=6t+(2t-1)(2t-2)`
`=4t^2+2`,

while the right side is

`(t+1)+(t^2+t-2)+C0`
`=5t^2+9t-4`.

Hence the rooted margin is

> **`t^2+9t-6>0` for every `t>=1`.**                     `(HR-ROOT)`

The new ratio restriction is correspondingly satisfied with large margin:

`1 < kappa theta+S0 = 1/4+1 = 5/4`.

## 4. Audit-mandated exact pair-local scalar gates

Take the natural minimum pair count

`g_P=m=2t-1`,

so

`k_P=x-g_P=2`.

The selected complementary used-witness pair contributes the safe pair-located slack floor

`S_P >= k(p+k-2)=2p=4t`.

For a hostile lower-capacity test, set `S_P=4t`.

The exact pair parameter is

`D0=5p+5u-3lambda-2`
`  =9t+6`.

The exact capacity is

`Ccap_P=R_code(S_P)[g_P+2S_P/(lambda+1)]`,

with

`R_code(s)=floor((D0+sqrt(D0^2+12s))/3)`.

Since the square root is at least D0,

`R_code(4t) >= floor(2(9t+6)/3)=6t+4`.

Also

`g_P+2S_P/(lambda+1)`
`=(2t-1)+8t/(2t)`
`=2t+3`.

Therefore

> **`Ccap_P >= (6t+4)(2t+3)=12t^2+26t+12`.**             `(HR-CCAP)`

The crossing demand is only

`2xy=2(2t+1)t=4t^2+2t`.

Thus exact `Ccap_P` has a large positive margin.

For purified `(ONE-P)`, the right side is

`y(p+x+k_P)=t(2t+2t+1+2)=4t^2+3t`,

again far below `(HR-CCAP)` even with `L_Y=0`.

Finally

`3y-D0=3t-(9t+6)=-6t-6<0`,

so the scalar `(CROWD)` floor is identically zero.

Hence:

> **all three audit-mandated aggregate pair-local scalar gates remain open on the half-ray.** `(HR-PAIR)`

This says only that those scalar inequalities do not eliminate the parameter ray; it is not realizability evidence.

## 5. Literal geometry forced by b=0

The ray is much more rigid physically than the margins above suggest.

Because `B0=empty`:

1. every U vertex lies in D;
2. every U vertex has at most one Y-neighbour (otherwise the reverse-certificate theorem would require a B0 witness);
3. `e(Y)=0`;
4. every existing Y--U edge is triangular;
5. every U--U edge must be sourced at a D endpoint, and each D source has capacity at most two, so `e(U)<=2u`;
6. global H/Y polarization forces every U vertex either H-anticomplete or Y-sparse; here Y-sparsity is already universal.

Thus a hypothetical realization of the half-ray has an asymptotically independent Y layer, an asymptotically sparse U layer, and only O(p) Y--U edges, while the score ceiling still permits it because `c` and `g0` balance at half scale.

This is now a much cleaner physical target than the old exact `c=p,y=p-1` stress family.

## 6. Next raw-criticality target

Do **not** spend another session optimizing the aggregate pair scalars on this ray; they have quadratic positive margin.

The next useful question is literal:

> with `B0=empty`, can a residual-one `k=2,J2=empty` D2C configuration have every U vertex of Y-degree at most one while Y is independent and U has only O(p) internal edges, yet still meet the maximum-degree/criticality requirements of all H--U and H--H edges?

The most promising attack is the H-side compensator. Since Y and U are both sparse on this ray, the exact degree-slack identities force a large fraction of H vertices to obtain their missing degree internally in H or through H--U incidence. Retain private matched-foot witness identities for H--H edges rather than replacing them by an edge count.

The upstream caveat remains unchanged: zero positive actual-D2C rigid complete Hall-cut fixtures with `x>=3` in bounded regression; `X_3` remains mandatory.