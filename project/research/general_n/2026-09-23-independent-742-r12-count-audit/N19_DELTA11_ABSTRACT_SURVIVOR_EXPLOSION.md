# n=19, Delta=11: v4 abstract-survivor explosion

24 September 2026, 08:00 scheduled session. Status: failed scalar-extension
route preserved; graph realizability is not established.

The first 200 stable indices were run through the exact-small-star v4 model
with `rho=3` and strict-counterexample allowance `Dmax=27`. Unlike the
adjacent `n=19, Delta=10` row, this prefix produced many abstract survivors.
The first three are:

| index | demand `d` | selected `x` | height `h` | exact deficit | gap |
|---:|---|---|---|---:|---:|
| 1 | `(9,6)` | `(9,6)` | `(9,6)` | 23 | -4 |
| 2 | `(9,6)` | `(9,7)` | `(9,8)` | 18 | -9 |
| 3 | `(9,6)` | `(9,8)` | `(9,10)` | 17 | -10 |

The output volume itself is the useful negative result: simply extending
scalar shards at this row cannot supply a graph theorem. The bounded pivot is
to retain actual source sets `C_i`, private-source incomparability, and edge
criticality, beginning with the extremal two-label profile at index 3. No
prefix-closure claim is made.

## Exact graph-level test of leading index 3

`realize_n19_delta11_index3_z3.py` fixes the profile

    d=(9,6), x=(9,8), h=(9,10), D<=27,

retains all 19 graph vertices, degree at most 11 with a degree-11 root,
distinct one-use physical source edges, diameter at most two, and deletion
criticality for every present edge. B-symmetry normalizes the forced disjoint
source sets to `C0={1,2}` and `C1={3}`. Z3 returns `unsat`.

This is internal exact computer-assisted evidence for one fixed profile. The
criticality encoding and normalization still require an independent replay
before the exclusion is promoted; no claim is made for the other prefix
survivors.

### Normalization and encoding checks

The source-set normalization does not discard a case. Here `|C0|=2`,
`|C1|=1`, `|T0|=9`, and `|T1|=8`. Since `T0=B\\C0`, the two endpoint sets
meet. At any common endpoint the private-source lemma makes `C0,C1`
incomparable. If their intersection were nonempty, singleton `C1` would be a
subset of `C0`; hence they are disjoint and B-symmetry permits
`C0={1,2}, C1={3}`.

The one-use constraints count both orientations of each physical B-edge, so
an edge cannot be reused with its former source as a later endpoint. Unique
common-neighbour constraints range over all graph vertices, not just B.

`validate_d2c_criticality_characterization.py` independently compared the
criticality formula with literal edge deletion on every diameter-two Graph
Atlas graph. It checked 5,553 edges in 457 graphs (22 D2C graphs), with zero
mismatches. This validates the generic criticality equivalence but is still
not an independent second encoding of the full fixed-profile UNSAT result.

### Independent direct-deletion replay

`realize_n19_delta11_index3_direct_z3.py` rebuilds the graph and source model
with separate variables and replaces the criticality characterization by its
literal definition: after deleting each present edge, some vertex pair has
neither a direct edge nor any two-step path. It also returns `unsat`.

Thus two distinct criticality encodings agree that stable index 3 is not
graph-realizable, and the generic characterization has an independent
5,553-edge regression. This promotes the fixed-profile exclusion to internal
computer-assisted status. It still excludes only index 3, not the many other
abstract survivors or the full row.

## Leading two-label family

`realize_n19_delta11_two_label_family_z3.py` generalizes the validated
criticality model to the first three `(9,6)` demand profiles and exhausts the
incomparable source-set intersection types (`|C0 intersect C1|=0,1`) up to B
symmetry.

| stable index | `(x0,x1)` | `(h0,h1)` | C-intersection | result |
|---:|---|---|---:|---|
| 1 | `(9,6)` | `(9,6)` | 0 | UNSAT |
| 1 | `(9,6)` | `(9,6)` | 1 | UNKNOWN (300s timeout) |
| 2 | `(9,7)` | `(9,8)` | 0 | UNSAT |
| 2 | `(9,7)` | `(9,8)` | 1 | UNKNOWN (300s timeout) |
| 3 | `(9,8)` | `(9,10)` | 0 | UNSAT |

The two UNKNOWN cases are not exclusions. They are the exact remaining
leading geometries and should be attacked by symmetry breaking or a direct
human degree/criticality argument; no additional scalar sharding is useful
until this graph-level fork is resolved.
