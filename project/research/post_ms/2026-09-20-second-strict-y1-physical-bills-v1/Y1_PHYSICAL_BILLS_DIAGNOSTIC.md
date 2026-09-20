# Mixed y=1 physical-bills diagnostic

Date: 2026-09-20

Evidence class: **abstract necessary-condition diagnostic only**. These rows are not graphs and the finite box is not a proof of closure or realizability.

The companion `check_y1_physical_bills.py` was independently replayed after construction over

- `2<=p<=20`;
- `5<=x<=30`;
- `2<=omega<=24`;
- `1<=g<x` (so `k=x-g>=1`);
- all `alpha,beta>=1`, `alpha+beta=omega-1` in exceptional Fz.

The replay returned:

| case | tested abstract parameter rows | necessary-condition survivors |
|---|---:|---:|
| R | 178,010 | 2,821 |
| Fz, no higher-radius head | 178,010 | 2,840 |
| Fx | 178,010 | 691 |
| Fz, one higher-radius head | 179,322 | 12,109 |

For exceptional Fz a parameter row is counted as surviving if **some** physical split `alpha+beta=omega-1` survives both the score and rooted inequalities.

Interpretation:

1. The new physical bills strongly compress Fx in this box.
2. R and no-exception Fz have similar scalar difficulty after their different Y/z_0/q contributions compensate.
3. Exceptional Fz remains the broadest scalar tail because cross-edges between its two ordinary-outside code classes can still buy rooted U-edge capacity. This confirms that preserving `alpha,beta` is structurally important; replacing the two classes by an undifferentiated outside-reservoir size would throw away the main remaining freedom.
4. The next proof step should therefore not be “scan a larger box”. It should attack the exceptional-Fz cross-class adjacency/certificate geometry, or derive an exact analytic optimization in `alpha,beta` and characterize any unbounded scaling family.

The counts above were reproduced independently from the formulas after the checker was committed.