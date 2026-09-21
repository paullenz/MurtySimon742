# Maximum-root ledger for the five-centre two-parameter family

21 September 2026.  Graph-level hand derivation with independent replay.

Let `G(r,q)` be the family in
`FIVE_CENTRE_TWO_PARAMETER_FAMILY_THEOREM.md`.  Its maximum-degree roots and
rooted residual quantities admit a complete closed form.

## Maximum-degree classification

For the original cube vertices, the five star codes cover vertex 0 four
times, vertices 3,5,6 three times, vertices 1,2,4 twice, and vertex 7 once.
Consequently

    deg(0)=11+r,
    deg(1)=deg(2)=deg(4)=9+q,
    deg(3)=deg(5)=deg(6)=10+r,
    deg(7)=8+q.

Every noncube vertex has smaller degree than the larger of the first two
displayed values: in particular the P1 hub has degree `10+r`, every P0 has
degree `4+q`, and every nonhub P1 has degree `4+r`.  Hence

    Delta=max(11+r,9+q).

The maximum roots are `{0}` when `q<r+2`, `{1,2,4}` when `q>r+2`, and all
four vertices when `q=r+2`.

## Exact rooted ledger

At root 0,

    b=11+r,  a=8+q,  lambda=b-a-1=2+r-q,  Q=17.

At any of roots 1,2,4,

    b=9+q,  a=10+r,  lambda=b-a-1=q-r-2,  Q=16.

Thus every maximum root has nonnegative lambda.  In either regime the exact
root defect is

    delta=b(n-b)-m=5r+7q+26.

This is positive linear throughout the family, consistently with its linear
gap below `M(n)`.

## No tight pairs at a maximum root

Every maximum root has `p=0`.  This is not merely a finite-grid observation.

For root 0, check the finite seed `G(1,1)`: no pair in its neighbourhood is a
tight pair.  Adding a P1 vertex leaves the root neighbourhood fixed and can
only add a common neighbour or an additional adjacency-pattern test; it
cannot turn a nontight old pair into a tight one.  Adding a P0 vertex adds a
new root neighbour with exactly the same open neighbourhood as the existing
P0 vertex.  Permuting P0 twins reduces every new candidate pair to an old
candidate type, while additions again cannot create tightness.

For roots 1,2,4 use `G(1,2)`, which contains both the distinguished P1 hub and
one nonhub P1 root-neighbour.  It has no tight pair at any of the three roots.
Every further P1 root-neighbour is an open-neighbourhood twin of that nonhub
vertex; extra P0 vertices are non-neighbours of the root and only add
incidences to the P1 neighbours.  The same monotonicity and twin argument
applies.  Since an odd cube vertex is maximum only when `q>=r+2>=3`, the seed
covers all neighbour types before the maximum-root regime begins.

Therefore the Boolean pair count is identically `p=0` at every maximum root.
The family is an actual dense D2C positive control, but it cannot exercise the
positive rigid complete Hall-cut interface highlighted by the daily audit.
This preserves, rather than repairs, the zero-positive-fixture gap.

## Independent replay

`check_five_centre_rooted_interface.py` checks all 400 pairs
`1<=r,q<=20`, comprising 760 maximum roots, against the formulas above.  It
also runs the prior graph-level root verifier under all three certificate
policies on representative boundary and unbalanced cases.  The mandatory
`X3` negative control is replayed in the same run with `n=12,m=32>M(12)=31`.
