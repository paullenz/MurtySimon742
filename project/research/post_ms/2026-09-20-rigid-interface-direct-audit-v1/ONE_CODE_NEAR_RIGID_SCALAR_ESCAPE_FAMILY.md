# One-code near-rigid cut — explicit scalar escape family

Date: 2026-09-20

Status: **same-session method-diagnostic / obstruction**, conditional on the exact rigid Hall interface and the one-code near-rigid formulas already preserved in this directory. This is not a graph construction. It shows that the current scalar combination of the W-class crowding price, distinct-head occupancy, gamma collision and Hamming-slot floor does **not** by itself close the large-gap branch. Exact pair-local `Ccap_P/(ONE-P)/(CROWD)` and/or rooted residual feedback are therefore genuinely necessary.

## 1. Family

For every integer `t>=2`, take

- `c=2t`,
- `p=3t`,
- `y=t`, hence `g0=p-y=2t`,
- `lambda=g0+c-1=4t-1`,
- `u=4t`,
- `x=p+u-c=5t`,
- choose minimum-source U-witness count `k=3t`,
- hence escape count `d=u-k=t`,
- and matched-covered head count `m=x-k=2t`.

Then

`0<=d<=c`, `k>=x-p=u-c`, `k<=u`, and `m=p-c+d`,

so the occupancy and distinct-head scalar constraints are all respected. The graph order would be

> `n=4p+2u-lambda=16t+1`,

and therefore

> `c=(n-1)/8`.

Thus this is fully compatible with the predecessor linear-gap necessity `n<=77c+46`: the rooted gap is macroscopic, but only at density about one eighth of the order.

## 2. Exact W-class price

The preserved two U-slack mechanisms are

`E_base=k(p-1)`

and

`E_same=k(g0+k-1)-2(y-1)(k-1)`.

On the family,

`E_base=9t^2-3t`,

`E_same=9t^2+5t-2`.

Hence for every `t>=1`,

> `E_class=E_same=9t^2+5t-2`.

So the same-code witness-class crowding theorem is being used in its stronger branch, not bypassed.

## 3. Exact A-slack price

The gamma collision price is

`phi(m)=m(m-1)=4t^2-2t`.

The near-rigid Hamming-slot quantity is

`Q=xg0-km-p/2=4t^2-3t/2`.

For `t>=2`, `k<=x-3`, so the preserved integral Hamming floor is

> `ell=floor(4t^2-3t/2)+1`.

Moreover `Q-phi=t/2>0`, hence `ell>phi`. Therefore the exact one-dimensional score floor `(WC-10)` on this family is

> `S_floor=9t^2+5t-2 + floor(4t^2-3t/2)+1`.

No weakening by averaging is involved here.

## 4. Exact above-M ceiling

For `lambda=4t-1` (odd),

`A_lambda=floor(lambda^2/2)+lambda+4+(lambda mod 2)=8t^2+4`.

Since `p+u=7t`,

`C0=(lambda+2)(p+u)+p-A_lambda`

becomes

> `C0=20t^2+10t-4`.

Using `floor(q)+1<=q+1`,

`C0-S_floor`

is at least

`20t^2+10t-4 -(9t^2+5t-2) -(4t^2-3t/2+1)`

`=7t^2+13t/2-3`,

which is strictly positive for every `t>=1`.

Therefore every member of this infinite parameter family survives the **full current scalar W-class + collision/Hamming score floor** with large positive margin.

## 5. Interpretation

This is not evidence that any such D2C graph exists. It is evidence about proof method:

> **the present one-dimensional scalar score package cannot close the large-gap one-code rigid branch.**

The family is especially informative because it is not hiding in a degenerate corner:

- `x=5t` and `y=t` both grow linearly;
- the minimum source uses `k=3t` U-witnesses;
- `d=t=c/2` U vertices escape that witness class;
- `m=2t` heads are matched-covered;
- the stronger W-class same-code price dominates the base incidence price;
- the Hamming-slot price dominates the gamma-collision price;
- yet the exact above-M ceiling still has quadratic room.

Thus adding another weak total-score inequality is unlikely to be decisive. The correct next test is to intersect this family with the quantities that have deliberately **not** been aggregated here:

1. exact pair-local `Ccap_P`;
2. `(ONE-P)` and `(CROWD)` on the same complementary pair;
3. distinct singleton-head support `rho` rather than only `m<=rho`;
4. the exact rooted residual/defect identity and located physical U-nonedges.

If the family violates one of those local constraints, that identifies the missing structural mechanism. If it survives them asymptotically, it should be treated as the canonical scaling family for the next structural classification rather than obscured by broader finite scans.

## 6. Trust boundary

No claim of graph realizability is made. Bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control outside this conditional interface.
