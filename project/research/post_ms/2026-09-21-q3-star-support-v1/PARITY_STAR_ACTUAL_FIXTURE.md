# An actual parity-star fixture and its replication cost

21 September 2026. Exact graph-level positive control; no minimum-order theorem claimed.

The parity-star obstruction is realizable. An exact SAT search produced and the independent raw graph checker verified a D2C graph with

    n=26, m=104, M(26)=157.

Its A-code multiset has one copy of each coordinate code, two copies of each even star code, two P0 vertices and one P1 vertex. The 16 A-edges are recorded exactly in `PARITY_STAR_MINIMUM_SEARCH.json`.

Structurally, one P0 is the hub for all six coordinates. The P1 vertex meets at least one star in every centre class, as raw P1-spoke criticality predicts. One copy in three classes forms a K_1,3 around an S6 copy; the other copies supply P1 bridges. Two P0--star edges form missing-pair V structures with P1. Direct deletion replay confirms the whole graph is D2C.

The graph is extremely sparse relative to the target: its deficit is 53. It therefore validates the live interface without threatening the density theorem.

## Bounded search scope

The exact grid used all six coordinate types, one or two copies of each of the four star centres, r=2..5 and q=1..3, forcing one P0--S0 edge. Within that grid the first satisfiable order is 26 and requires two copies of every centre. This is not a global minimum claim: larger star multiplicities, five-coordinate supports and other parity multiplicities were not exhausted.

Earlier tests with one star per centre, r,q through eight, and with up to four copies of S0 alone were UNSAT under a forced parity-star edge. These are diagnostics, not proofs. The positive fixture is now a mandatory control for any proposed parity-star nonexistence or density argument.

## Raw forced fan

If a P1 vertex t is adjacent to S_c, then for each of the three odd leaf spokes of t lying in S_c, the direct certificate is destroyed. The singleton replacement is an absent odd-centred star, so the reverse replacement forces t to meet a star in each of the other three even centre classes. Thus every P1 vertex incident to one star is incident to all four star-centre classes. The fixture realizes this forced fan.
