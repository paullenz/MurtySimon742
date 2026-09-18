# Complementary-pair fan packing audit

Date: 2026-09-18

Target:

`COMPLEMENT_PAIR_FAN_PACKING.md`

## Exact arithmetic replay

The key implication was replayed exhaustively over the integer grid

- `1<=lambda+1<=20`;
- `1<=M_P<=50`;
- `0<=S_P<=100`;
- `-5<=T<=20`;
- `1<=d<=30`.

For each tuple the coarse pair edge budget

`E=floor(M_P S_P/(lambda+1))`

was formed. Whenever the primitive pair-local fan inequality

`d(2d-T-1)<=S_P+2E`

held, the checker verified the promoted concentration inequality

`(lambda+1)d(2d-T-1)`
` <= (lambda+1+2M_P)S_P`

for every case with positive left side.

- primitive feasible cases checked: **38,342,788**;
- failures: **0**.

This is an arithmetic audit only. The mathematical content remains the hand chain

`same-code edge capacity -> pair-local fan inequality -> pair slack floor -> disjoint-pair packing`.

## Interpretation

The audit supports the exact direction of the new reduction: a large A/U fan cannot be cheap unless its complementary code pair either has a large population coefficient `M_P` or captures a large share of the total slack.

The mandatory `X_3` order-12, size-32 control is not touched because its canonical rooted fan gate is zero.
