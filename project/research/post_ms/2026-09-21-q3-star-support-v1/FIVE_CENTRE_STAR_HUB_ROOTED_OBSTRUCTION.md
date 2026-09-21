# Maximum-root obstruction in the improved five-centre family

21 September 2026.  Raw rooted-criticality consequence.

Every maximum-degree root in the arbitrary-multiplicity star-hub family of
`FIVE_CENTRE_STAR_HUB_FAMILY_THEOREM.md` has Boolean tight-pair count `p=0`.

## Proof

Use the finite type seed with one copy of every outside type and a second,
nonhub P1 vertex.  Direct rooted inspection shows that every vertex other
than the original Q3 root has no tight pair in its neighbourhood.  The
original root has the four antipodal cube pairs, hence `p=4`, but its degree is
8.  The distinguished P1 hub always has degree

    4+r+C >= 11,

so the original root is never maximum degree.

All permitted family expansions add false twins of types already represented
in this seed.  For a fixed old root, adding vertices and incident edges cannot
turn a nontight old neighbour pair into a tight pair: adjacency of the pair is
unchanged, an existing second common neighbour is not removed, and an old
failure of the exact-one adjacency condition persists.  Any pair involving a
new root-neighbour is carried by a twin permutation to a represented seed
type.  If the chosen root itself is a new clone, it has the same open
neighbourhood as its represented type.  Therefore no expansion creates a
tight pair at any possible maximum-root type.

It follows that `p=0` at every maximum root for all multiplicities.  The
construction is an actual dense family with a positive linear residual gap,
but it cannot instantiate the positive rigid-Hall interface.  The daily
audit's zero-positive-fixture gap therefore remains genuine and cannot be
repaired merely by enlarging this family.

## Replay

The checker verifies the complete finite seed, then samples 1,000 combined
blowups (1,078 maximum roots), all with `p=0`.  It also retains X3 as the
mandatory order-12 negative control.  The finite seed plus monotonicity is the
proof; the random scan is only regression evidence.
