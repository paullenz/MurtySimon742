# Many tree components: finite hostile ladder

21 September 2026. Exact SAT diagnostic; no infinite family claimed.

The split-tree obstruction is not confined to two components. For each `d=2,...,6`, a full graph-level D2C SAT instance is satisfiable with joint multiplicity `k=2d`, one physical star adjacent to exactly `d` selected vertices on each parity side, `d` diagonal missing pairs uniquely bridged by that star, and every selected off-diagonal cross pair present. Consequently `H_x` has `d` disjoint one-edge tree components.

The exact rows are recorded in `PARITY_STAR_TREE_COMPONENT_LADDER_RESULTS.json`. The `d=2` graph is preserved and independently replayed in `PARITY_STAR_SPLIT_TREE_COUNTEREXAMPLE.json`; a separate `d=3` model also passed direct D2C replay during discovery. The larger rows use the same exact full-D2C encoding but are not promoted to a parametric construction.

This eliminates any repair that bounds the number of tree components per star by an absolute constant. The density attack must exploit the population and missing-pair cost of creating those components. In the `d=3,k=6` replay, the corrected block excess is `-7` while the global density budget `D(u,s)` is 333: the hostile local geometry is extremely sparse.
