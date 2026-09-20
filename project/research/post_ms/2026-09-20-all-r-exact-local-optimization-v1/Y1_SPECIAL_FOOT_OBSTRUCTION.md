# The y=1 special-foot slice still forces one outside witness

Date: 2026-09-20

Status: **internal conditional lemma** inside the literal all-R equality pinch. This handles the slice deliberately excluded from the `y>=2` residual-grid theorem.

## 1. Why y=1 is exceptional

Let `Y={y}`. For an edge `xy` with `x in X`, the matched endpoint in the unique fibre where `C` differs from d is adjacent to y and nonadjacent to x. Unlike the `y>=2` case, there is no second Y-vertex automatically preventing this matched endpoint from serving as the raw criticality witness for the orientation `x -> y`.

Hence the full cross-reservoir theorem cannot simply be copied to `y=1`.

## 2. The edge `a_0 y` cannot use the special matched foot

The distinguished outside witness z has code `bar C` and `a_0 z in E`. In the special fibre where `C` differs from d`, the code `bar C` agrees with d. Therefore z is adjacent to the d-selected matched endpoint q in that fibre.

If q were the raw witness for `a_0 -> y`, the required singleton relation would be

`N(a_0) cap N(q)={y}`.

But z is adjacent to both `a_0` and q, so z is a second common neighbour. Contradiction.

Thus the special matched foot cannot certify the edge `a_0y`.

## 3. The reverse orientation is impossible

An orientation `y -> a_0` with a U-witness would require a complementary `bar d` witness adjacent to `a_0`. The previously proved `A0-CODE` localization allows only codes d or C among U-neighbours of `a_0`; for `p>=3`, `bar d` is neither. Root/A alternatives fail as in the general cross-edge location audit.

Therefore `a_0y` must be certified in orientation `a_0 -> y` by an outside U-witness of code `bar C`.

The witness cannot be z because a witness must be nonadjacent to its source and `a_0z in E`. It cannot lie in the purified J-set because those vertices are A-anticomplete and hence are not adjacent to the head y.

Consequently it lies among the d z-nonneighbours.

Hence the y=1 slice satisfies the physical requirements

> `d>=1`,                                               `(Y1-d)`
>
> at least one outside C-type cross witness is used.   `(Y1-C)`

That witness is nonadjacent to `a_0`, so the a0 degree/slack floor gains one unit relative to a hypothetical free matched-foot cover. The selected source-witness pair also contributes one located X--U hole.

## 4. Focused diagnostic effect

Applying only this mandatory outside-witness obligation, its a0 score cost, one selected X--U hole, and the existing exact pair/q/residual gates to the focused `e(X)=0,y=1` slice leaves

> **4,523** abstract rows,

compared with 4,607 before this lemma.

This is a slice diagnostic only.

## 5. Next target in y=1

The other `x-1` edges from `X'` to y may still use the special matched foot in principle. Any further closure must therefore inspect the common-neighbour set of that fixed matched endpoint simultaneously across `X'`, rather than assuming a general outside-witness requirement.
