# A residual-defect gate for the complete four-centre branch

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Setup

The four-centre classification reduces the branch to one parity plane. For coordinate direction i, let x_i,y_i be the physical populations of its complementary halfcube codes and put

    t=sum_i(x_i+y_i),    C=sum_i x_i y_i.

Let r,q be the P0,P1 multiplicities, s the number of star vertices,

    M=rq-e(P0,P1),    I=e(P0)+e(P1),    a=t+r+q+s.

At the original Q3 root, b=8, Q=12 and

    delta=8(n-8)-m=4a-12-e(A).

## Theorem

Every graph in this branch satisfies

    e(A) <= 2C+rq+M+s-I,

and hence

    delta >= 4a-12-2C-rq-M-s+I,

    M(n)-m >= floor(a^2/4)-2C-rq-M-s+I-3.

In particular, any graph exceeding the candidate second-extremal value must satisfy

    2C+rq+M+s-I > floor(a^2/4)-3.

## Proof

The raw type classification permits coordinate A-edges only to P0. For an edge from coordinate vertex x to p in P0, criticality requires a physical vertex y of the complementary coordinate code with p as the unique common A-neighbour of x,y. Charge xp to xy. A fixed cross-code physical pair has at most one common P0 vertex if it receives a charge and can support at most the two incidences xp,yp. Summing the three complementary pairs gives

    e(coordinates,P0) <= 2C.

There are no other coordinate A-edges. `PARITY_STAR_MISSING_PAIR_LEDGER.md` bounds all edges induced by parity and star vertices by rq+M+s-I. Adding proves the A-edge bound.

The displayed defect and gap formulas follow from the exact Q3 skeleton count

    n=a+9,    m=20+4a+e(A),
    M(n)=floor(a^2/4)+4a+17.

No duration, finite-search or Hall-interface inference enters the proof.

## Interpretation

This is a sufficient density gate, not yet an unconditional M(n) theorem for the branch. The remaining obstruction is now explicit: control the combination 2C+M, preferably by showing that large complementary-coordinate capacity and many missing parity pairs compete for the same P0 physical certificates. The exact order-19 and order-20 classifications satisfy the gate sharply enough to give their proved bounds.
