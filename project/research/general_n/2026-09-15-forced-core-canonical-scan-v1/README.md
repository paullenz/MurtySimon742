# Canonical forced-core scan v1

15 September 2026. Research-branch discovery scan only; **not promoted to the canonical frontier**.

This package extends the exact post-pair relational enumeration over the 952 currently promoted-frontier survivors. It does not test only the stored witness: for any state whose stored relational witness is killed by the new theorem, it resumes the complete admissible `q` enumeration and accepts the state if any later profile survives both the old relational screens and the new forced-core test.

For residual level `r`, put `A_r={i:s_i<=r}`, `h=|A_r|`, and `U_r={u:rho_u=r,q_u=h}`. Eligibility forces `S_u=A_r` for each `u in U_r`. The fixed-neighbourhood routing criterion implies that a receiver `v` of one of these obligations must satisfy

```
v not in U_r,
q_v <= h+r-1,
q_v+rho_v >= h-1,
```

with incoming capacity `c_v=rho_v+b-a-1`; each receiver is dedicated to at most one core label. The scanner gives each candidate receiver the favourable effective capacity `min(c_v,|U_r|)` and exactly tests whether those capacities can be partitioned into `h` label bins each of demand `|U_r|`. Failure excludes that `q` profile.

If the partition is feasible, for every threshold `tau>r` it computes the minimum unavoidable loss of high selected slots among all feasible receiver-bin assignments. A used receiver satisfies `S_v subset A_r union R_u`, hence contributes at most `r` labels with demand at least `tau`. If even the minimum loss leaves fewer high slots than `sum_{s_i>=tau}s_i`, that `q` profile is excluded.

`prepare_scan.py` pins the previously promoted relational discovery result hash, reconstructs all 952 source states from its frozen `EXPECTED_ACTIVE.txt`, and separates stored witnesses that already survive this new theorem from those requiring resumed enumeration. `scan_forced_core.cpp` then performs exact integer enumeration. `aggregate.py` requires complete key coverage before reporting any candidate whole-state exclusions.

The scan is a discovery step. Any new whole-state exclusion remains unpromoted until separately audited/reproduced and reconciled with the canonical ledger. External mathematical review of the graph-to-selected/residual bridge and fixed-neighbourhood routing theorem remains open.
