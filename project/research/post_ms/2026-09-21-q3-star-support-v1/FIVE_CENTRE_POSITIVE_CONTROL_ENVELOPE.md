# Five-centre positive-control envelope

21 September 2026.  Synthesis of proved explicit families; not a global upper
bound for five-centre graphs.

Two internally proved mechanisms currently supply the strongest explicit
controls on centre support `{0,1,2,4,7}`:

1. the repeated-S7 family, with `m_L(n)=6n-49` for every `n>=21`;
2. the improved star-hub/parity family, with
   `m_Q(n)=4n-6+floor((n-20)^2/4)` for every `n>=22`.

Their difference is

    m_L(n)-m_Q(n)=2(n-20)-3-floor((n-20)^2/4).

Hence they tie at orders 22 and 26; the repeated-S7 family is one edge denser
at orders 23,24,25; and the quadratic parity family is denser for every
`n>=27`.  At order 21 only the repeated-S7 mechanism exists and gives 77
edges.

This explains the two exact order-22 near-minimal mechanisms and identifies
the right hostile controls for future five-centre density claims: small-order
tests must include the repeated-star route, while eventual tests must include
balanced parity blowups.  Both remain a positive linear distance below
`M(n)`, so neither threatens the conjectured sufficiently-large boundary.

The envelope is only over these proved construction classes.  Other A-graphs,
larger code multiplicities and the other two five-centre support orbits remain
outside its scope.
