# Whole-code fan capacity audit

Date: 2026-09-18

Target note:

`WHOLE_CODE_FAN_CAPACITY_AND_COMPACT_SCORECARD.md`

Checker:

`check_whole_code_fan_capacity.py`

## Result

The checker was replayed against the exact integer formulas before preservation.

- low-hole / beta hybrid profile cases: **1,494,045**;
- uniformly bounded-hole whole-code cap cases: **2,010**;
- compact quadratic lower/upper-hole implication cases: **10,949,820**;
- total exact arithmetic checks: **12,445,875**;
- failures: **0**.

The profile audit compares the new full-witness-set low-hole cap against the preceding split profile over `d<=35`, all `0<=K<=d-2`, same-code edge budgets through 80, and U-edge budgets through 30. No case made the new hybrid cap weaker than the preserved bound.

The compact audit does not assume the final quadratic inequality. It enumerates the primitive interval

`d(d-1)-2E <= G_x <= S+(d-1)(P-d)-d(lambda+1)`

and checks that every nonempty interval implies

`2d^2-(T+2)d+P <= S+2E`.

## Conservative parameter diagnostic

A separate deliberately pessimistic scan through `p<=60`, using the *maximum* above-threshold global scorecard, `q=0` in the rooted lower gate, the coarse root-imbalance beta floor, and the largest scorecard-compatible matched-foot allowance produced 19,814 parameter tuples with a positive rooted A/U fan gate. At that fully distribution-free worst case, neither the old nor the new fan scorecard excluded the minimally required fan.

This is recorded as a **negative diagnostic**, not as evidence against the theorem. It says that replacing the complementary-pair budget by the global envelope

`E_0=floor((a+u)S/(lambda+1))`

can wash out the gain. The next useful step is therefore to exploit the source-local pair inequality

`d(d+lambda-epsilon_x) <= S_bar(c(x))+2E_x`

and show that a forced fan cannot concentrate enough of the total slack in its one complementary code pair.

## Scope

This audit checks arithmetic consequences only. The graph-theoretic inputs are the already preserved fan normal form, same-code weighted edge capacity, root-hole fact for A-witnesses, and beta-sensitive U-edge bound. The scan is not a proof substitute.

The mandatory order-12, size-32 `X_3` graph is unaffected because its canonical root has `u=0` and no positive rooted A/U fan is forced.
