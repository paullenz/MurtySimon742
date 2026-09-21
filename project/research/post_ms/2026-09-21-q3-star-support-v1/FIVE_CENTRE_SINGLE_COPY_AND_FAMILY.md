# Five-centre orbit triage, exact single-copy classification, and an infinite family

21 September 2026. Q3 antipodal-transversal scope.

## Support orbits

The 48 cube automorphisms have exactly three orbits on five-element star-centre supports. Representatives and the distance multisets of their three-vertex complements are

| support representative | complement | complement distances |
|---|---|---|
| `{0,1,2,3,4}` | `{5,6,7}` | `{1,1,2}` |
| `{0,1,2,4,7}` | `{3,5,6}` | `{2,2,2}` |
| `{0,1,2,5,6}` | `{3,4,7}` | `{1,2,3}` |

Thus five-centre work has three support shapes, not 56 labelled cases.

## Exact single-copy classification

Fix one physical vertex at each of the five star centres and permit an arbitrary subset of the six coordinate and two parity codes, again with one physical vertex per chosen code. Exact SAT over all 256 halfcode subsets in each orbit gives:

- complement type `{1,1,2}`: no D2C graph;
- complement type `{2,2,2}`: exactly one minimum halfcode subset, with seven types;
- complement type `{1,2,3}`: no D2C graph.

The unique minimum model up to cube symmetry has

    C00,C01,C10,C11,C20,C21,P1,
    S0,S1,S2,S4,S7,

so its centre support is the closed cube neighbourhood of `0` together with the antipode `7`. Its A-edges are the six-coordinate `P1` hub plus

    S0--S7, S1--S4, S2--S4.

It is an actual `n=21,m=77` D2C graph, with `M(21)-m=24`. The two negative orbit results are only for the stated one-copy slice; arbitrary multiplicities remain open.

## Infinite family

For every `q>=1`, take the same six coordinate vertices and five star vertices, together with `q` copies of `P1`. Designate one `P1` vertex `h`; join `h` to all six coordinate vertices and retain the three star-forest edges above. Give the other `P1` copies no A-neighbours. Then

    n=20+q,
    m=73+4q=4n-7.

This graph is D2C for every `q>=1`.

### Uniform proof

The `q=1` base graph is directly replayed. Add an A-isolated `P1` twin `z`.

- Diameter two is preserved: `z` meets every odd cube vertex, reaches each even cube vertex through Q3, reaches the root through an odd cube vertex, meets every coordinate/star code on an odd cube vertex, and shares its B-code with the other `P1` vertices.
- Every new spoke `zb`, with `b` odd, is critical: after deletion, `z` has no length-two route to `b`, since the odd parity class is independent in Q3 and `z` has no A-neighbours.
- For every edge of the base graph, direct replay supplies a lost-distance witness whose two endpoints are not both odd cube vertices. An added isolated `P1` twin creates new length-two paths only between pairs of odd cube vertices, so these witnesses remain valid.

Induction adds arbitrary many isolated `P1` twins. The direct checker verifies the base-witness property for all 77 base edges and replays the first twenty family members.

## Significance

The five-centre frontier is nonempty already at order 21, but this family has only linear edge count and a quadratic gap below `M(n)`. It is therefore a structural positive control, not a density threat. The next useful question is whether any five-centre orbit supports quadratic-density parity blowups or whether a raw support obstruction forces a linear regime.

## Simultaneous-parity blowup diagnostic

The most direct quadratic candidate is in fact viable throughout the tested
rectangle.  Add `r>=1` copies of `P0` and `q>=1` copies of `P1`, make the
`P0--P1` block complete, keep one designated `P1` hub adjacent to all six
coordinates, and retain the three star edges above.  Direct graph-level replay
passes all 400 pairs `1<=r,q<=20`, with

    n = 20+r+q,
    m = rq+4(r+q)+73.

Thus five-centre support does admit quadratic-density parity blowups.  The
uniform twin-extension proof is now given in
`FIVE_CENTRE_TWO_PARAMETER_FAMILY_THEOREM.md`.  Writing `u=r+q` and
`d=|r-q|`, the exact gap from `M(n)` is

    11u/2+18+d^2/4                 if u is even,
    (11u+37)/2+(d^2-1)/4           if u is odd.

This corrects the earlier same-session odd-`u` shorthand `6u+18`, which was
arithmetically false.  The family theorem itself and its edge formula are
unchanged.
