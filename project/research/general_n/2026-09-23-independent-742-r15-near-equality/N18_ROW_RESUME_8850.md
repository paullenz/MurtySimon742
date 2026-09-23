# n=18, Delta=10 strengthened row prefix through scalar 8,850

The deterministic resumed replay extended the solved prefix from scalar 7,700 to 8,850, reaching full-pattern index 11,795. No abstract survivor was found. The resumed segment's local best gap was 5; the global prefix best remains 1 from the preceding session.

A solver-free traversal of the identical partition, symmetry and scalar filters gives exact totals after the four separately excluded tuples:

- full patterns: **70,959**;
- scalar-pass candidates requiring MILP: **54,816**.

Thus the saved zero-survivor prefix covers candidates 1-8,850. The remaining 45,966 candidates cannot be completed serially within this slot at the observed rate. The next bounded unit is deterministic disjoint sharding of the remaining scalar-index range.

No row closure or graph theorem is claimed.
