# The matching-one target for parity-star cancellation

21 September 2026. Precise proof target; finite evidence is exact but no general theorem is claimed.

The local certificate graph `H_x` of a high-bridge star has no isolated vertices. If its matching number is at most one, then every edge shares one endpoint: `H_x` is a single nontrivial star component. Consequently it has exactly one tree component, so the matching-deficiency reduction gives

    e(R union T union S) <= rq+s.

Combined with coordinate substitution this would sharpen the four-centre bound to

    e(A) <= 2C+rq+s,

removing the dangerous `+M-I` term from the residual-defect gate.

The exact SAT encoding in `PARITY_STAR_TRUE_SPLIT_CORE_RESULTS.json` forces a physical star to be the unique common A-neighbour of two vertex-disjoint missing `P0--P1` pairs, with every cross pair and all other A-edges left free. It is UNSAT on the six-coordinate support with `r=q=2` and each even star multiplicity `2,...,8`. This is precisely the smallest matching-number-two obstruction, not merely a chosen closure of it.

A proof must now start from two unique pairs `r0t0,r1t1` at the same star and use raw spoke criticality to contradict D2C, without relying on finite multiplicity. That lemma would close the missing-pair cancellation step in one stroke. Until proved, the improved density inequality remains conditional.

The same matching-two core remains UNSAT when every coordinate-code multiplicity is increased uniformly from one through eight (two copies per star class, `r=q=2`). Coordinate witness capacity therefore does not repair the hostile core in this exact range.
The matching-two core is also UNSAT for balanced parity multiplicities `r=q=2,...,8` on the fixed eight-star, six-coordinate support. Thus none of the three natural multiplicity axes repairs it in the tested range.
