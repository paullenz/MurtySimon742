# Unit-column theorem: regression and scope challenge
22 September 2026. Internal finite evidence, not external proof verification.

The 1,396-fixture / 68,741-assignment suite passed:
- 71 all-unit-column cases, 60 with nonempty F.
- 514 two-column cases having a unit column.
- 469 residual-mass-at-most-three cases.
- 68,703 demand-at-most-three bound checks.
- All 26,439 residual-source partitions for directed cycles of lengths 3–9 fail the exact selected/witness contradiction kernel.

**Coverage limitation:** there were zero degree-two F cases inside the all-unit-column actual-graph branch. Its cycle-saturation exclusion is supported by the written proof and abstract repeated-source kernel, not by a realizable saturated-cycle fixture. No graph existence or universal nonexistence follows just from these finite counts.

A direct scope challenge found an actual D2C graph for which the conclusion would be false if “maximum-degree root” were omitted. It is the C5 blow-up with independent part sizes (1,1,2,2,1), on vertices [[0],[1],[2,3],[4,5],[6]], with graph edges
[(0,1),(0,6),(1,2),(1,3),(2,4),(2,5),(3,4),(3,5),(4,6),(5,6)].
Root 0 has degree 2 while the graph maximum is 3. Its A={2,3,4,5}, B={1,6}, F=K(2,2), all four R_i=1 and f=r=4. Every edge deletion was independently BFS-checked. This is a hypothesis control, not a counterexample to the stated theorem or to Murty–Simon. The nonmaximum root violates the x_i>=d_i-R_i premise (x_i=0, d_i-R_i=1).

Reproduce with the standard-library helper:
```python
import check_raw_profile as C
parts=[[0],[1],[2,3],[4,5],[6]]
G=C.from_edges(7,[(u,v) for k in range(5) for u in parts[k] for v in parts[(k+1)%5]])
C.certify_d2c_bfs(G)
print(C.legal_choices(G,0))
```

Unit checker SHA256: f6728a49120960540daaf24fb0610b56789b284ff2e758eb44b82db16b8cf4bd.
Measured graph replay duration: 57.11508049099939 seconds.
Complete compact output: UNIT_COLUMN_RESULTS.json. The source regenerates its full deterministic fixture ledger and preserves its hash before compacting the output. Sampling limits are unchanged from EQUALITY_REGRESSION.md.
