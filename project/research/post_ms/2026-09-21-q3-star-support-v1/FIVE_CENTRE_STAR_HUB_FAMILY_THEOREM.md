# Improved five-centre star-hub family

21 September 2026.  Q3 antipodal-transversal scope.  Internally proved and
machine-replayed; external review remains open.

## Construction and theorem

Use the six coordinate codes, P0, P1 and the five star centres
`{0,1,2,4,7}`.  Keep S7 a singleton.  Give arbitrary positive multiplicity
to every coordinate code and to `S0,S1,S2,S4,P0,P1`.  Make P0--P1 complete,
join every coordinate vertex to one distinguished P1 hub, and join every
`S0,S1,S2,S4` vertex to the S7 hub.  There are no other A-edges.

Every graph in this family is D2C.

The one-copy base has `n=22,m=83`.  All 83 base edges have deletion witnesses
which avoid the neighbourhood of every permitted clone type.  The false-twin
induction from `FIVE_CENTRE_CLONE_CLOSED_FAMILY_THEOREM.md` therefore applies
verbatim.  A first nonhub P1 has its own endpoints as witnesses for all new
odd spokes and P0 edges.  Direct replay of 200 combined blowups independently
checks the construction.

This family is strictly better than the earlier three-star-edge family at the
same populations: its star A-graph is the full `K1,4` centred at S7.  Exact
MaxSAT on the one-copy 13-code multiset proves that 11 A-edges is maximal,
attained by the six coordinate-hub edges, the P0--P1 edge and the four star-
hub edges.  This fixed-multiset statement does not classify all maximizing
A-graphs up to isomorphism.

## Exact formulas and internal extremum

Let `C>=6` be the total coordinate population, let `A>=4` be the total leaf-
star population, and let `r,q>=1` be the parity populations.  Then

    n = 10+C+A+r+q,
    m = 24+5(C+A)+4(r+q)+rq.

Put `t=C+A>=10`, `w=n-20` and `t=10+k`.  Balancing the parity block gives

    m <= 4n-6+k+floor((w-k)^2/4),  0<=k<=w-2.

The same discrete convexity calculation as before yields the exact maximum
inside this family:

    m_max(n)=4n-6+floor((n-20)^2/4),   n>=22.

For `n>=24`, equality forces `C=6`, `A=4` and balanced parity populations.
At `n=23` a one-unit linear-population expansion also ties.  The exact gap is

    M(n)-m_max(n) = 11w/2+17       if w is even,
                    (11w+35)/2     if w is odd.

Thus the improved family remains a positive linear distance below `M(n)`.
It improves the earlier clone-closed extremum by exactly one edge at every
order, but remains structurally far from an eventual counterexample.

## Trust boundary

This is an exact family theorem and a fixed-multiset MaxSAT result.  It is not
an upper bound for all five-centre D2C graphs.  In particular, it does not
exclude other A-graphs with larger multiplicities or settle the two remaining
five-centre support orbits.
