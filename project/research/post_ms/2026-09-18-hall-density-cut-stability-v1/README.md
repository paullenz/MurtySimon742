# Hall density / cut stability package

This checkpoint develops the complementary-pair Hall-cut theorem into an exact density and stability framework.

Files:

- `HALL_DENSITY_STABILITY.md` — exact cut decomposition, capacity lift, Hall-density threshold theorem, two-sided cut sandwich, near-equality rigidity, complementary capacity forcing, and A--U cross-deficit localization.
- `HALL_RESERVE_POLARIZATION.md` — exact reserve expansion and disjoint-block polarization.
- `check_hall_cut_stability.py` — independent abstract algebra checker.
- `AUDIT_SUMMARY.md` — frozen audit scope and results.

Main new structural message:

> low pair-capacity density cannot occupy much A-mass; if it comes close to the allowed mass ceiling, the corresponding A-cut becomes complete, selected-source traffic becomes one-way, and the complement is forced to supply nearly all crossing-edge certificate capacity.

This is a majorization/stability strengthening of the previous Hall-cut theorem, not an eventual second-extremal proof.

The mandatory published 12-vertex, 32-edge `X_3` control remains valid and untouched: at its canonical root `u=0` and `A` is independent, so the new A--U cross-deficit/beta localization mechanism is inactive.
