# Hostile replay of the two nonparity affine-plane exclusions

21 September 2026. Audit complete internally; external review open.

The first opposite-edge proof draft omitted C21 from the codes avoiding vertices 2 and 3. This was a substantive local error. It did not survive the first independent truth-table replay. The proof was repaired rather than hidden: C21 is the unique remaining bridge type between mandatory complementary C10 and C11 populations, and its forced adjacency kills both orientations of cube edge 4--6.

The coordinate-face proof survives unchanged. There, after spokes 4 and 5, the codes avoiding 6 and 7 are exactly C10,S0,S1. Physical matching uniqueness prevents the two star types from meeting C11, while the restriction prevents a C10 intermediate.

`check_four_centre_orbit_exclusions.py` independently rebuilds the singleton and reverse channels from cube bitsets, checks the antipode membership used for each physical uniqueness exclusion, calculates the surviving neighbour-code sets, and verifies that the two eliminated orbits have six labelled supports each while the parity orbit has two. Together they partition all 14 affine planes.

The finite SAT result for the minimal multisets agrees but is not used as proof. The corrected opposite-edge argument adds the necessary cube-edge step and covers arbitrary multiplicities.
