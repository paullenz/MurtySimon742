# Repeated one-code blocks force a much larger rooted gap

Date: 2026-09-21

Status: same-session synthesis inside the rigid complete one-code interface. This note combines the 21 September raw full-boundary theorem with the previously proved no-collision/distinct-head U-bound. It does **not** address reachability of the rigid interface from arbitrary D2C graphs; bounded actual-D2C regression still has no positive rigid complete fixture with `x>=3`, and `X_3` remains the mandatory negative control.

## Setup

Use the standard one-code notation. Let the outside block be `Y=A_d` with multiplicity `y>=2`. Write

- `p` for the matched-coordinate dimension;
- `u=|U|`;
- `c=lambda+1-g0`, with `g0=p-y`;
- `x=p+u-c`;
- `k` for the selected U-witness count of a minimum outside source;
- `m=x-k` for the selected matched-head count.

Assume the large-gap branch `c>=1` when invoking the previously proved global U-bound `u<4p+3c`.

## 1. Small matched-head cases are already near-maximal-gap

The identity `m=x-k` and the physical bound `k<=u` give

`m >= x-u = p-c`.

Hence

> **`c >= p-m`.**                                      `(1.1)`

In particular,

- `m=0 => c>=p`;
- `m=1 => c>=p-1`.

This uses neither the boundary-exposure theorem nor the score ceiling.

## 2. Repeated blocks with `m>=2`

For `y>=2,m>=2`, the full-boundary theorem gives

`c>=p+r-2`, where `r=p-m>=0`.

Therefore

> **`c>=p-2`.**                                         `(2.1)`

The stronger exact universal-coordinate split remains available:

- `|C|=0` or `|C|>=3`: `c>=p+r`;
- `|C|=1`: `c>=p+r-1`;
- `|C|=2`: `c>=p+r-2`, with equality requiring the universal pair to be an isolated matched-row `K_2`.

## 3. Unified repeated-code compression

Combining Sections 1 and 2 gives a simple statement valid for **every** selected matched-head count `m`:

> **If `y>=2`, then `p<=c+2`.**                         `(3.1)`

For `m<=1` the stronger `p<=c+1` holds. Thus the previously open small-matched-head regime does not evade a macroscopic rooted gap: it is actually at least as close to maximal gap as the `m>=2` regime.

This is important because it removes `m<=1` as a qualitatively separate scalar escape direction for the purpose of bounding order versus rooted gap. It remains a separate realizability geometry only for finer criticality analysis.

## 4. Improved order-versus-gap constant

The earlier one-code linear-gap theorem proved, without using the matched collision term,

> `u<4p+3c`.                                            `(4.1)`

Since `u,p,c` are integers, `(3.1)` and `(4.1)` imply

`u <= 4(c+2)+3c-1 = 7c+7`.

Also `lambda=g0+c-1>=c` because `g0>=1`. Using the exact order identity

`n=4p+2u-lambda`,

we obtain

`n <= 4(c+2)+2(7c+7)-c = 17c+22`.

Hence:

> **Repeated one-code linear-gap compression theorem.**  
> In the rigid one-code large-gap branch with `y>=2` and `c>=1`, every survivor satisfies
>
> **`n<=17c+22`, equivalently `c>=ceil((n-22)/17)`.**   `(4.2)`

The earlier general constant was `n<=77c+46`. Thus repeated outside-code multiplicity improves the coefficient of `c` from 77 to 17 by a purely structural argument.

## 5. Generic `m>=2` refinement

If the universal-coordinate geometry is generic (`|C|=0` or `|C|>=3`), the full-boundary theorem gives `c>=p+r`, so `p<=c-r`. Then `(4.1)` gives the integer bound

`u<=4(c-r)+3c-1 = 7c-4r-1`,

and therefore

> **`n<=17c-12r-2`.**                                  `(5.1)`

The one- and two-universal-coordinate exceptions interpolate between this and `(4.2)` with only additive losses. Thus positive residual matched dimension makes the order bound strictly tighter in the generic face.

## 6. Audit notes

The synthesis was replayed from the defining identities rather than inferred from the old `77c+46` theorem:

1. `m=x-k`, `x=p+u-c`, `k<=u` give `(1.1)` directly.
2. For `m>=2,y>=2`, `(2.1)` is exactly the weakest case of the independently preserved full-boundary theorem.
3. The U-bound `(4.1)` was proved in the older linear-gap note without any `m>=3` collision assumption, so it remains available in the small-matched-head cases.
4. No finite scan, source-tuple capacity theorem, pair-local Hall inequality, or reverse-gamma argument is used here.
5. The result remains conditional on the rigid complete one-code interface; it is not a graph-level eventual theorem.

## 7. Next use

The correct next move is not more scalar optimization of the dead half-ray. Feed the now-macroscopic rooted gap `c` into the exact rooted residual-defect identity and rooted triangle count `Q`, while keeping the `m<=1` and `y=1` geometries separated where certificate orientation genuinely differs.
