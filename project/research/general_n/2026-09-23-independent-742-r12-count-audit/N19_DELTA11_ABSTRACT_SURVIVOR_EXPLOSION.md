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

### Strengthened intersection-one replay

The two timeout cases were replayed after adding only consequences of the
encoded graph model: degree ordering among the five inactive A-vertices,
pair-deficit lower bounds for assigned incidences, and the audited exact-star
inequalities (73 for the nine-set label; 45 and 58 for the six- and seven-set
labels).  Both cases again returned `UNKNOWN` at 300 seconds:

| stable index | `(x0,x1)` | `(h0,h1)` | C-intersection | strengthened result |
|---:|---|---|---:|---|
| 1 | `(9,6)` | `(9,6)` | 1 | UNKNOWN (300s timeout) |
| 2 | `(9,7)` | `(9,8)` | 1 | UNKNOWN (300s timeout) |

This is a useful negative solver result, not an exclusion.  The redundant
star constraints did not resolve the hard branch, so the next bounded step is
to split an intersection-one case by the shared source edge's endpoint
degrees or rebuild it with the independent literal-deletion encoding.

Splitting index 1 by the deficit of the common source vertex reduces that
UNKNOWN branch sharply.  With 80-second exact checks, deficit ranges `3--5`,
`6--8`, and `9--10` are UNSAT; only `0--2` remains UNKNOWN.  These four
ranges exhaust the possible deficit `0--10`, so no omitted range is being
treated as excluded.  The surviving low-deficit shard still requires exact
resolution.

Exact follow-up shards at common-source deficits `0`, `1`, and `2` each
remained UNKNOWN after 180 seconds.  Thus the reduction to `0--2` is durable,
but none of its three leaves is an exclusion.  Increasing the same encoding's
timeout again is not a justified proof step; an independent literal-deletion
model or a new structural consequence is required.

The generalized literal edge-deletion encoding was then run on the whole
remaining index-1 deficit range `0--2`.  It also returned UNKNOWN at 300
seconds.  The timeout output landed fractionally after the research cutoff;
that post-cutoff fraction is not credited.  Agreement of two encodings on a
timeout is not mathematical evidence of infeasibility, so index 1 remains
open precisely in this low-deficit intersection-one branch.

## 09:00 recovery: root-edge witness obstruction closes index 1 / intersection 1

A direct graph argument removes the timeout branch without using additional
solver time.  In stable index 1 with `|C0 intersect C1|=1`, normalize
`C0={1,2}` and `C1={1,3,4,5,6}`.  Since `x=(9,6)`, every element of
`T0={3,...,11}` and `T1={2,7,...,11}` is assigned.

One-use of physical source edges now forces the B-geometry.  For each
`t=7,...,11`, an edge `1t` would be the source for both assigned pairs
`(L0,t)` and `(L1,t)`, so `1t` is absent; the L0 assignment then forces
`2t`, and the L1 assignment forces exactly one edge from `t` to
`{3,4,5,6}`.  For the assigned pair `(L1,2)`, using any source
`j in {3,4,5,6}` would reuse the same physical edge `2j` for `(L0,j)`.
Hence its source is 1.  Therefore `12` is present, every `2j` with
`j=3,...,6` is absent, and the L0 assignments force every `1j` with
`j=3,...,6` to be present.

Criticality of the root edge `01` then forces an A-vertex `r` with
`N_B(r)={1}`.  Indeed, `0` and `1` retain two-step paths through
`2,3,4,5,6`; and if deletion of `01` were witnessed on the 1-side by a
B-vertex `t`, then `t` must be one of `7,...,11`, but `1` and `t` already
share the B-neighbour 2.  Thus the only possible lost two-step path is
`0-r` with 1 its unique common neighbour, exactly `N_B(r)={1}`.
The same argument for root edge `02` gives a distinct A-vertex `s` with
`N_B(s)={2}`: the only B non-neighbours of 2 forced here are `3,...,6`,
and each shares B-neighbour 1 with 2.

Neither `r` nor `s` is adjacent to the root, and each has only one B-neighbour,
so each has degree at most `1+6=7` and deficit at least 4.  Thus these two
root-edge witnesses contribute at least 8 to the global deficit.

It remains to combine this with the already-audited exact-star inequalities.
Write `p=def(L0)`, `q=def(L1)`, and
`U=def(2)+sum_{t=3}^{11} def(t)`.  The two star inequalities give

    U >= 73 - 9p,
    U >= 45 - 6q.

Also `0<=p<=9` because `L0` has its two forced B-neighbours, and `0<=q<=6`
because `L1` has its five forced B-neighbours.  Therefore

    p + q + U >= 23.

For completeness: if `p<=6`, the first inequality gives at least 25; if
`p>=7` and `q<=5`, the second gives at least 27; and if `p>=7,q=6`, the
three possibilities `p=7,8,9` give lower bounds 23,23,24 respectively.

The total degree deficit is therefore at least `23+8=31`, even before adding
the nonnegative deficit of vertex 1 and the other inactive A-vertices.  A
strict counterexample at `n=19, Delta=11` has
`D=19*11-2e <= 209-2*91 = 27`.  Contradiction.

Hence stable index 1 with source-set intersection one is excluded at graph
level.  This argument is conditional on the audited source assignment,
one-use, root-edge criticality, and exact-star premises; it is an internal
proof step, not external acceptance.  The next bounded target is stable index
2 with source-set intersection one.
