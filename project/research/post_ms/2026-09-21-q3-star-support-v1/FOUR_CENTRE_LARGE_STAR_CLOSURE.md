# Unconditional large-star closure in the four-centre branch

21 September 2026. Internally proved; external review open.

Retain the notation of `FOUR_CENTRE_BUDGETED_CANCELLATION_GATE.md`. Let

    w=r+q,  u=t+w,
    U=M-I.

The unconditional missing-pair ledger gives

    B <= rq+s+U.

Hence the budgeted gate immediately proves `m<=M(n)` whenever

    U <= D(u,s)

with

    D(u,s)=floor((u+s)^2/4)-floor(u^2/4)-s-3.

This is an exact graph-level sufficient condition. Therefore every surviving counterexample in the exactly-four-centre branch must satisfy

    M-I > D(u,s).

## Simple population corollary

Since `U<=rq<=floor(w^2/4)`, the whole branch closes whenever

    s >= ceil(w/2).

Indeed `t>=5`, so `u>=w+5`. Using `floor A-floor B>=floor(A-B)` gives

    D(u,s) >= floor(s(2w+s+6)/4)-3.

For `w>=4` and `s>=w/2`, the right side is at least `floor(w^2/4)` because the continuous surplus is

    w^2/16+3w/4-3 >= 0.

The cases `w=1,2,3` follow directly from `s>=4`.

Thus any counterexample must lie in the sharply asymmetric regime

    s < (r+q)/2

and simultaneously have more than `D(u,s)` unoccupied missing parity pairs. This is a substantive unconditional reduction, not a consequence of the invalid matching-one lemma.
