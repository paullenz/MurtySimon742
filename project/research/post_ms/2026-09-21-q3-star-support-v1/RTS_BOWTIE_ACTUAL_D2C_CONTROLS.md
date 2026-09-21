# Actual D2C controls for the RTS bow-tie

21 September 2026. Exact graph-level SAT plus independent D2C replay.

## Result

The locally saturated RTS bow-tie from `RTS_BOWTIE_LOCAL_SATURATION.md` is graph-realizable. Moreover, the status of its fourth parity cross pair is not forced.

Two explicit controls are saved in `RTS_BOWTIE_REALIZABILITY_RESULTS.json`:

1. an actual `n=33,m=143` D2C graph with all six coordinate codes, three copies of each even star code, `r=4,q=2`, and the fourth pair `r't'` **present**;
2. an actual `n=34,m=148` D2C graph with the same coordinate/star populations, `r=5,q=2`, and `r't'` **missing**.

Both contain the RTS triangle `r-t-x`, the crossed missing pairs `rt'` and `r't`, and singleton common-neighbour equations

    N_A(r) intersect N_A(t')={x},
    N_A(r') intersect N_A(t)={x}.

Every saved adjacency list passes direct diameter-two and every-edge-deletion replay. These fixtures are sparse (`M(33)-143=114`, `M(34)-148=125`) and are controls for realizability, not near-extremal examples.

## Uniform bounded regression

With all six coordinate codes, equal multiplicity `k` in each of the four even star classes, and `2<=r,q<=8`, exact SAT gives:

- `k=1`: no RTS-bow-tie fixture;
- `k=2`: no RTS-bow-tie fixture;
- `k=3`: satisfiable exactly for `r>=4` throughout the scanned rectangle, independently of `q` in `2,...,8`.

This finite threshold is diagnostic only. It suggests that the bow-tie's raw obstruction is paid on the `P0`/star side rather than by a large `P1` reservoir, but no arbitrary-multiplicity theorem is inferred from the grid.

## Consequences

Two tempting local closures are now ruled out:

1. the RTS bow-tie itself cannot be forbidden from raw graph realizability;
2. neither presence nor absence of the fourth pair `r't'` can be assumed universally.

The next structural target must therefore compare the bow-tie's forced physical populations with density. The bounded grid points to a replication cost: the first symmetric controls require three copies of every star class and at least four `P0` vertices. A valid proof must derive whatever part of that cost is genuinely forced, rather than extrapolating the finite threshold.

## Reproduction

Run `search_rts_bowtie_realizability.py`. It rebuilds the two controls, verifies their crossed singleton equations and direct D2C status, and replays the complete `k<=3`, `2<=r,q<=8` uniform grid.

The first replay's reporting loop failed after successfully writing the result file because it treated grid metadata as a fixture row. The loop was corrected; the mathematical output and direct graph checks had completed before that reporting-only failure.
