# N34 state 60 — whole-state exclusion

13 September 2026. Candidate whole-state exclusion inside the frozen N34 experiment; external mathematical review remains open.

Frozen state: `n2=8, n3=7, rho=1^7,2^5,3^6, S=37, r=35, a=15, b=18`.

The earlier full `E=0..34` low-demand scan had nonpositive layers only at `E={0,1,2,3,4,5,6,7}`. The joint-Hall class-packing replay at commit `9a7a67a930c5cda80b12b7695b31d897aa9ba2d9` made `E={1,2,3,4,5,6,7}` strict, leaving only `E=0`.

`ORIENTATION_TARGET_CAPACITY.md` proves that an oriented missing B-edge `u -> w` must satisfy `c_w >= q_u-1`. Hence for every threshold k, incoming mass to targets with `c_w<=k` can come only from sources with `q_u<=k+1`. On `E=0`, exact demand also gives the recorded active-source bound `p_u<=rho_u-1`.

The exact enumerator `verify_e0_orientation_capacity.py` checks the full frozen q-partition domain. GitHub Actions run `34785891328` succeeded with:

`state=60 profiles=253001 passing=0 Q=37 max_min_cut=31 minimum_deficit=6`

Thus every one of the 253,001 E=0 q-profiles violates a necessary orientation-capacity cut; even the closest profile is six incoming incidences short.

The replay output is committed as `E0_ORIENTATION_CAPACITY_REPLAY.txt` and also preserved as Actions artifact `e0-orientation-capacity-replay`, artifact id `10326950324`, ZIP SHA-256 `304dfd030f0deb7947e31b17110fa42e234924edfa4936b7b34c03b481885904`.

Therefore state 60 is excluded as a whole scalar state in the frozen N34 experiment. This inherits the trust boundary of the canonical selected/residual bridge and the frozen N34 catalogue.