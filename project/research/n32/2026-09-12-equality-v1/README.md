# N32 equality evidence — t=1

12 September 2026.

This directory preserves the final `n=32, Delta=17, m=256` candidate equality analysis.

**Current conclusion inside the established bridge:** the `Delta=17` equality branch is excluded. Together with the balanced `Delta=16` hand argument, this gives the candidate equality statement `e(G)=256 iff G=K(16,16)`.

Start with:

- [`CERTIFICATION_LEDGER.md`](CERTIFICATION_LEDGER.md) — exact finite accounting and replay semantics;
- [`HAND_EXCEPTION.md`](HAND_EXCEPTION.md) — hand contradiction for the sole full-RX survivor;
- [`check_n32_t1_frontier.cpp`](check_n32_t1_frontier.cpp) — independent exhaustive demand-score frontier;
- [`n32_t1_lifted_potential_exact.py`](n32_t1_lifted_potential_exact.py) — exact 1,369-state first stage;
- [`n32_t1_full_rx_exact.py`](n32_t1_full_rx_exact.py) — exact sharded replay of the 615 survivors;
- [`n32_t1_zero_exact.py`](n32_t1_zero_exact.py) — exact strengthened zero-demand replay;
- [`aggregate_n32_t1_replay.py`](aggregate_n32_t1_replay.py) and [`run_replay.sh`](run_replay.sh) — aggregate assertions / one-command replay.

The fixed finite ledger is:

```text
frontier demand profiles       381
pre-model arithmetic impossible  1
positive-demand states        1984
  exact lifted-potential       1369
  full-RX stage                 615
    exact Farkas rejects        614
    hand survivor                 1
zero-demand states               61
  exact Farkas rejects           61
unresolved                         0
```

No floating-point infeasibility is accepted as proof evidence. Independent specialist review of the graph-to-model bridge remains open.
