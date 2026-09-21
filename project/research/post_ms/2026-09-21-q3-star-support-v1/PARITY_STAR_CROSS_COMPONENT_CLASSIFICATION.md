# Cross-component classification for the remaining parity-star obstruction

21 September 2026. Raw structural reduction; external review open.

Let `x` be a high-bridge star and let `H_x` be its valid missing-pair certificate graph from `PARITY_STAR_CANCELLATION_REDUCTION.md`. Suppose `H_x` has distinct components. For `r in R` from one component and `t in T` from another, both vertices are adjacent to `x`, but `rt` is not an edge of `H_x`. Exactly one of the following must happen:

1. `rt` is an actual parity edge; or
2. `rt` is missing and has an additional common A-neighbour besides `x`.

The additional common neighbour cannot be a coordinate vertex: in the four-centre parity-plane classification every coordinate A-edge runs to `P0`, so no coordinate can meet both `r in P0` and `t in P1`. Hence every extra bridge lies in `R union T union S`.

More explicitly, an extra parity bridge in `R` uses a same-`P0` edge plus a cross-parity edge; an extra bridge in `T` uses a cross-parity edge plus a same-`P1` edge. Every such same-parity edge is already charged injectively to an occupied missing pair by `PARITY_BLOCK_SUBSTITUTION_BOUND.md`. An extra star bridge makes the cross pair share at least two star neighbours.

If the two components have bipartition sizes `(a,b)` and `(c,d)`, this demand applies to exactly `ad+bc` cross-component parity pairs. Thus a two-tree-component counterexample cannot hide in coordinate capacity. Every cross-component pair is paid for by one of three visible resources:

- a present `R--T` edge;
- a same-parity edge, hence an occupied missing-pair token;
- overlap of two physical star neighbourhoods.

The first two smallest closures were exact UNSAT in `PARITY_STAR_SPLIT_HOSTILE_CORE.md`. The remaining proof task is to show that the required complete cross-component matrix exhausts more of these three resources than a second tree component can save, or to build an actual larger fixture showing otherwise. This is the next local route into the rooted residual ledger: present cross edges lower `M`, same-parity bridges raise `I`, and repeated star overlap reduces unique-certificate capacity.
