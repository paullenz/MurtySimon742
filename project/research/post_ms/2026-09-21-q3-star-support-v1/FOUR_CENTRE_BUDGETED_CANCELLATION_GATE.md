# Budgeted cancellation gate for the four-centre branch

21 September 2026. Rigorous conditional density theorem; external review open.

The failed exact-cancellation targets were stronger than the eventual density argument needs. Let

    t = number of coordinate vertices,
    r = |P0|,
    q = |P1|,
    s = number of star vertices,
    u = t+r+q,
    a = u+s.

Write `B=e(G[P0 union P1 union S])` for the parity/star block and define its excess over the desired exact cancellation by

    epsilon = max(0, B-(rq+s)).

## Theorem

Every exactly-four-centre parity-plane graph satisfies `m<=M(n)` whenever

    epsilon <= D(u,s),

where

    D(u,s) = floor((u+s)^2/4)-floor(u^2/4)-s-3.

At this scope `t>=5`, `r>=1` and `s>=4`, so `u>=6` and

    D(u,s)>=D(6,4)=9.

Thus even nine edges of failed parity-star cancellation are harmless uniformly; the admissible error grows with the graph.

## Proof

All coordinate A-edges run to `P0`, so their number is at most `rt`. If `B<=rq+s+epsilon`, then

    e(A) <= rt+rq+s+epsilon
         = r(t+q)+s+epsilon
         <= floor(u^2/4)+s+epsilon,

because `r+(t+q)=u`. The exact Q3 skeleton identity gives

    M(n)-m = floor(a^2/4)-e(A)-3
           >= D(u,s)-epsilon.

This is nonnegative under the displayed hypothesis. Monotonicity of `D` for `u>=6,s>=4` gives the uniform value nine.

## Corrected matching form

With hard-obligation matching deficiency `h`, bucket count `L`, and unused missing-pair capacity

    g=(M-I)-nu,

the block excess is bounded by

    epsilon <= max(0,h+L-s-g).

Therefore the actual target needed for the density theorem is only

    h+L-s-g <= D(u,s),

not matching-one, one-tree-component, or exact `h+L<=s+g`. The actual split-tree counterexample has `h+L-s-g=-2`, so it lies safely inside the gate despite falsifying both stronger conjectures.

This repair materially reduces the proof burden while keeping the graph-level trust boundary explicit. It does not itself bound the corrected excess in arbitrary multiplicity.
