# Raw criticality calculus: sound pruning with physical witnesses

21 September 2026. Scope: the Q3 root with antipodal-transversal outside codes.

Let H_x=N(x) intersect B and A_x=N(x) intersect A. All H_x have size four. An edge can destroy a path of length at most two only when one endpoint of the affected pair is an endpoint of the edge. This elementary observation gives the exhaustive cases below. These statements remain valid as descriptions of pairs that lose distance at most two even when the entire graph does not have diameter two.

For a spoke xs, x in A and s in H_x, the possible affected pairs are:

1. (x,s): H_x intersect N_Q(s) is empty and no A-neighbour of x contains s.
2. (x,t), t adjacent to s in Q and outside H_x: N_Q(t) intersect H_x={s}, and no A-neighbour of x contains t.
3. (x,z), z in A nonadjacent to x: H_x intersect H_z={s} and A_x intersect A_z is empty.
4. (s,z), z in A adjacent to x: H_z avoids the closed cube neighbourhood of s, and x is the unique A-neighbour of z whose code contains s.

For an A-edge xy, possible affected pairs are:

1. (x,y): both their B-code intersection and A-neighbour intersection are empty.
2. (x,t), t in H_y minus H_x: N_Q(t) intersect H_x is empty and y is the unique A-neighbour of x whose code contains t; or the reverse endpoint orientation.
3. (x,z), z in A nonadjacent to x: H_x intersect H_z is empty and A_x intersect A_z={y}; or the reverse endpoint orientation.

No pair involving the original root supplies an omitted certificate: an A vertex has four cube neighbours, so removal of one spoke leaves other length-two routes to the root; an A-edge lies on no length-two A-to-root route.

## Soundness of the type-relation fixed point

Start with every ordered pair of available code types. At each pruning round retain a pair only if each endpoint's spokes can have at least one of the above certificate types, and their connecting A-edge can have an endpoint certificate. Drop physical uniqueness requirements when making this necessary test; permit distinct copies of any available code. For a given forced neighbour K, only exclude the direct or standard B-target spoke witness when K itself destroys that witness.

Inductively every actual A-edge survives every pruning round. This holds at the initial complete relation. If it holds before a round, every actual witness edge needed by an actual certificate is still in the relation; dropping other physical restrictions only admits more possibilities. Therefore an actual edge cannot be removed. The finite relation decreases and terminates. Its final lists are overapproximations, never existence assertions.

This induction justifies using the resulting lists to prove forced absence, diameter incompatibility and clean-entry obstructions for arbitrary physical multiplicities. It does not justify constructing a graph merely because a type pair survives.

## Independent hostile replay

`check_exact_local_certificates.py` compares the complete predicted certificate sets above with literal distance-at-most-two reachability before and after each edge deletion. The code independently builds actual graphs; it does not invoke the pruning relation.

The corpus exhausts all 256 labelled pairs of A-code choices, both with and without their A-edge (512 populations). It adds 400 reproducible larger populations with repeated codes, third targets, competing neighbours, and densities from empty to complete, plus X3 and three actual five-coordinate D2C family members. The arbitrary populations are not asserted to be D2C.

All 28,934 A-B/A-A edge deletions agree exactly, comprising 11,720 lost distance-two pairs. Both endpoint orientations and physical uniqueness are tested. The result supports the local calculus and the soundness argument; it does not close the global selected-source premises or produce a positive rigid Hall cut.

Full counts: `EXACT_LOCAL_CERTIFICATE_RESULTS.json`. The finite replay is an audit of the preceding exhaustive proof, not a replacement for it.
