# Mixed y=1 physical-bills diagnostic

Date: 2026-09-20

Evidence class: **abstract necessary-condition diagnostic only**. These rows are not graphs and the finite box is not a proof of closure or realizability.

The companion `check_y1_physical_bills.py` was independently replayed over

- `2<=p<=20`;
- `5<=x<=30`;
- `2<=omega<=24`;
- `1<=g<x` (so `k=x-g>=1`).

The exceptional-Fz formulas now include `EXCEPTIONAL_FZ_CROSS_CLASS_CLOSURE.md`, which proves the two ordinary outside code classes have **no cross edges**. The previous 12,109-row exceptional-Fz result allowing an `alpha*beta` U-edge term is superseded.

Current replay:

| case | tested abstract parameter rows | necessary-condition survivors |
|---|---:|---:|
| R | 178,010 | 2,821 |
| Fz, no higher-radius head | 178,010 | 2,840 |
| Fx | 178,010 | 691 |
| Fz, one higher-radius head | 171,237 | 2,276 |

The exceptional-Fz test count is smaller because that geometry requires both ordinary outside code classes and hence `omega>=3`.

Interpretation:

1. Fx remains the most compressed large-head scalar tail in this box.
2. R and no-exception Fz remain close in scalar difficulty.
3. The new cross-class theorem removes the dominant apparent exceptional-Fz freedom: its survivor count falls from the superseded 12,109 to **2,276** in the same parameter ranges.
4. All four tails are now governed by independent or nearly independent physical outside layers. The next step should solve the resulting score/rooted inequalities analytically and identify the scaling form of the remaining rows, rather than enlarging the box.

The counts above were reproduced independently from the formulas after the checker update. They remain diagnostics only.