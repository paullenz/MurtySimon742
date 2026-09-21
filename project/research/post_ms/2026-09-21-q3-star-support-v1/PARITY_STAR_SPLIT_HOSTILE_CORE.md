# Smallest split-certificate hostile cores

21 September 2026. Exact finite obstructions; no arbitrary-multiplicity theorem claimed.

The cancellation reduction says a surviving counterexample needs a high-bridge star whose valid certificate graph has at least two tree components. The smallest possible shape has one star `x`, two `P0` neighbours `r0,r1`, two `P1` neighbours `t0,t1`, and component edges `r0t0,r1t1` represented by missing pairs uniquely bridged by `x`.

Exact SAT rejects both simplest ways to keep the cross pairs outside this certificate graph in the fixed eight-star, six-coordinate, `r=q=2` multiset:

1. making both cross pairs `r0t1,r1t0` present;
2. making all four parity pairs missing while a second physical star bridges both cross pairs.

Both formulas are UNSAT under full diameter-two and every-edge-critical constraints. The clauses and scopes are recorded in `PARITY_STAR_SPLIT_HOSTILE_CORE.json`.

This does not eliminate a split certificate graph in general: a cross pair could have a more complicated extra common-neighbour pattern, and larger multiplicities were not encoded. It does show that neither the complete-cross closure nor the single-second-star closure realizes the minimal obstruction. The next attack should classify the possible extra common neighbours of cross pairs under the four even star codes.

The present-cross pattern was then replayed with two copies of each star class and balanced parity populations `r=q=2,...,8`; every instance is UNSAT. This shows the obstruction persists after adding unrestricted extra parity vertices within that exact support, but remains a bounded multiplicity result.
