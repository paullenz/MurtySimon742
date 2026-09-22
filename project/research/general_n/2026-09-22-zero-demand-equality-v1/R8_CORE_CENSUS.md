# Residual-mass-eight strict core census: labelled first pass

22 September 2026. Exact enumeration of the optimistic necessary core relaxation. This is a census, not a graph-realizability result and not yet an orbit/source screen.

screen_r8_core_counts.py enumerates every labelled positive-support core for every partition of r=8, applying edge charge, selected-source capacity, the exact P/N core ledger and optimistic N-slack. The all-unit case is excluded by the proved unit-column theorem.

Five partitions retain strict-surplus cores:
- (3,2,1,1,1): 2 labelled survivors;
- (3,1,1,1,1,1): 157;
- (2,2,2,1,1): 1;
- (2,2,1,1,1,1): 685;
- (2,1,1,1,1,1,1): 10,505.

The other 16 partitions have zero survivors. Total labelled survivors: 11,350.

To keep the seven-label case tractable and avoid a costly or error-prone isomorphism implementation mid-session, this first pass records exact degree/P signature counts and eight example edge sets per partition. Those signatures are explicitly not graph-isomorphism orbits. The saved JSON is enough for a later symmetry quotient and physical source screen.

This shows a sharp growth in the optimistic relaxation at r=8; unlike r=6 and r=7, a direct hand-enumerated orbit list is no longer the most efficient next interface. The next step should exploit source-state infeasibility by signature or canonical graph hashing, with an independent replay before any theorem claim. No extension beyond the proved S<=9 bound is asserted here.
