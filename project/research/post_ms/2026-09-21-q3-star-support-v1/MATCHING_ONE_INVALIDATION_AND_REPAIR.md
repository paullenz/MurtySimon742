# Matching-one invalidation and exact repair

21 September 2026. Actual graph-level counterexamples; prior finite inference withdrawn.

## What failed

The proposed lemma that every high-bridge star certificate graph `H_x` has matching number at most one is false. The earlier scans varied star, coordinate and parity multiplicities one axis at a time while holding the other populations at their smallest values. Joint scaling exposes actual D2C counterexamples.

With all six coordinate codes, three copies of each even star code and `r=q=3`, `search_matching_two_joint_scale.py` constructs an `n=33,m=142` D2C graph in which one `S0` vertex is the unique common A-neighbour of two vertex-disjoint missing `P0--P1` pairs. In that first model `H_x=K_{2,2}`, so matching-one fails although `H_x` is cyclic and causes no matching deficiency.

The stronger proposed condition that every `H_x` has at most one tree component is also false. With four copies of each star class and `r=q=4`, `search_split_tree_counterexample.py` constructs an `n=39,m=176` D2C graph whose chosen `S0` has `H_x` equal to two disjoint edges. Direct graph replay checks diameter two and deletion-criticality of every edge.

For this graph:

    h=3, L=14, s=16, so h+L=17>s.

Thus the sufficient shortcut `h+L<=s` is false. The graph is very sparse (`M(39)-m=186`) and does not refute the desired density bound; indeed its parity/star block has 30 edges while `rq+s=32`.

## Exact surviving condition

Let `O` be the number of hard parity-star obligations, `nu` the maximum matching size into unoccupied missing parity pairs, and

    h=O-nu,
    g=(M-I)-nu.

Here `g` is the unused missing-pair capacity omitted by the failed shortcut. The desired sharp block inequality is equivalent to

    O+L <= (M-I)+s,

or, identically,

    h+L <= s+g.

The split-tree counterexample has `nu=4`, `M-I=7`, hence `g=3`; its corrected inequality is `17<=19`. The finite model therefore invalidates both stronger local conjectures while demonstrating the exact slack that repairs the accounting.

## Dependency correction

- `PARITY_STAR_CANCELLATION_REDUCTION.md` remains valid through the definitions of `O,nu,h,L` and the conditional implication, but its proposed target `h+L<=s` is false.
- `PARITY_STAR_MATCHING_ONE_TARGET.md` is superseded as a theorem target.
- No proved order-19/order-20 classification, four-centre support theorem, star-forest theorem, parity substitution bound, or general `rq+M+s-I` ledger is affected.
- The improved arbitrary-multiplicity bound `e(R union T union S)<=rq+s` remains open. Its correct target is the capacity-aware inequality `h+L<=s+g`, not matching-one.

This is aligned with the daily audit: actual graph realizability has overruled a pattern inferred from a narrow finite grid, and the repair is stated at physical-incidence level rather than hidden in scalar evidence.
