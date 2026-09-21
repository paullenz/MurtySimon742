# Clone-closed five-centre family and its exact internal extremum

21 September 2026.  Q3 antipodal-transversal scope.  This is a theorem about
an explicit family, not an optimality theorem over all five-centre graphs.

## Construction

Start from `G(1,1)` in `FIVE_CENTRE_TWO_PARAMETER_FAMILY_THEOREM.md` and allow
arbitrary positive multiplicities for

    C00,C01,C10,C11,C20,C21, P0,P1, S0,S1,S2,S7,

while keeping `S4` a singleton.  Every coordinate copy is joined to the
distinguished P1 hub; the P0--P1 and S0--S7 blocks are complete bipartite;
every S1 and S2 copy is joined to S4.  There are no other A-edges.

Let `C` be the total coordinate population and write the populations of
`P0,P1,S0,S7,S1,S2` as `r,q,a,b,c,d`.  All seven variables are positive and
`C>=6`.

## Uniform D2C theorem

Every graph in this clone-closed family is D2C.

For the 82 edges of the base graph, the certificate checker selects one lost
pair that avoids the neighbourhood of every permitted new clone type.  Adding
a clone can create a new length-two path between old vertices only when both
ends lie in that clone neighbourhood, so all selected witnesses survive.
Every new edge is the image of a base edge under a permutation of its false-
twin class; the same safe certificate transfers.  The first nonhub P1 copy is
the only new type not represented in the base.  Its odd spokes and P0 edges
have their own endpoints as deletion witnesses, and those pairs avoid every
future clone hazard set.  Diameter two follows because each clone has the same
neighbourhood as its represented type (or, for the first nonhub P1, reaches
all old types through its odd cube neighbourhood and the complete P0 block).
Induction in any order proves the claim.

The exact order and size are

    n = 10+C+r+q+a+b+c+d,
    m = 24+5C+4(r+q+a+b)+5(c+d)+rq+ab.

The companion checker records all 82 universal base certificates and directly
replays 200 seeded combined blowups.

## Exact maximum within the family

Put

    t=C+c+d >= 8,
    p=r+q+a+b >= 4,

so `n=10+t+p` and

    m=4n-16+t+rq+ab.

For fixed `p`, convexity of the two balanced-product functions gives

    rq+ab <= 1+floor((p-2)^2/4).

Equality puts one complementary pair at its minimum populations `(1,1)` and
balances the other pair.  Write `t=8+k` and `w=n-20`; then

    m <= 4n-7+k+floor((w-k)^2/4),   0<=k<=w-2.

Because

    floor(w^2/4)-floor((w-k)^2/4) >= k,

the exact maximum at every `n>=22` is

    m_max(n)=4n-7+floor((n-20)^2/4).

For `n>=24`, equality forces `t=8`: one copy of every coordinate, S1 and S2,
with either the parity pair or the antipodal star pair fixed at `(1,1)` and
the other pair balanced.  At `n=23` there is an additional tie with `t=9`.

The corresponding gap below `M(n)` is positive linear.  With `w=n-20`, it is

    11w/2+18       if w is even,
    (11w+37)/2     if w is odd.

Thus allowing every certificate-safe clone does not approach the eventual
boundary more closely than linearly.  It does expose a second extremal mode:
the quadratic block may live in the parity pair or in the S0--S7 star pair.

## Trust boundary

The theorem does not show that S4 is intrinsically uncloneable under every
possible A-graph, nor that all D2C graphs on this centre support belong to the
clone-closed family.  Those are separate classification problems.
