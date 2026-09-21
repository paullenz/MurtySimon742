# Opposite-parallel-edge support forces both parity codes

21 September 2026. Internally proved at Q3-transversal scope; external review open.

Suppose the star centres are exactly T={0,1,6,7}. Then:

- C10,C11,C20,C21 and both P0,P1 occur;
- exactly one of C00,C01 occurs;
- the missing direction-0 coordinate code forces a perfect matching of physical stars between the two centres on the opposite side;
- consequently n>=20.

Realizability and sharp density remain open.

## 1. Both direction-0 coordinate types are A-isolated

For C00, at spokes 2 and 4 the outside targets are respectively 3 and 5. Both singleton-star and reverse-star replacements have absent centres. Any A-neighbour code must avoid 3 and 5. The available codes satisfying this are C00,P1,S0,S6. A P1 neighbour is itself impossible: its spoke at 2 has its direct certificate destroyed by C00, while its singleton star S2 and reverse star S5 are absent. Thus the symmetric spoke tests leave only C00,S0,S6.

A same-C00 edge has no certificate: the complementary C01 cannot neighbour its endpoint. A C00--S0 edge has no certificate: S0's antipode 7 is outside C00; C00--S7 is forbidden; and the halfcube-side third target C01 cannot neighbour S0 (the corresponding C01 list is C01,S1,S7). The C00--S6 edge fails symmetrically. Hence C00 is A-isolated. Translation by cube vector 1 gives the same result for C01.

Both codes cannot coexist, because they have disjoint B-neighbourhoods and an isolated endpoint cannot reach its complement in two steps. Cube-edge criticality in direction 0 requires at least one. Exactly one occurs.

## 2. The missing code forces a physical matching

If C01 is absent, the direction-0 leaf spokes at stars S0 and S6 force adjacent reverse-star witnesses in the other class. Each witness requires its partner to be its unique antipode bridge; the symmetric requirement forces mutual uniqueness. Thus the physical S0,S6 classes are perfectly matched, with no additional antipode bridges.

If C00 is absent, the identical argument perfectly matches S1,S7. This is the same physical matching mechanism already proved in the parity-plane case; no code multiplicity restriction is imposed.

## 3. Neither parity code can be absent

Suppose P0 were absent. The centre spoke of every even-centred star (S0 or S6) would require an adjacent opposite-centred odd star. Such opposite-star endpoints are antipode bridges for one another.

But either the even pair S0,S6 is already uniquely matched, in which case the even endpoint cannot acquire that extra bridge, or the odd pair S1,S7 is already uniquely matched, in which case the odd endpoint cannot acquire it. Both alternatives contradict the required centre-spoke certificate. Thus P0 occurs. The same argument with the parity roles reversed forces P1.

## 4. Remaining mandatory coordinates and order

Direction-1 and direction-2 star leaf spokes have their reverse centres outside T. They force C10,C11,C20,C21. Together with four star classes, both parity codes, and one direction-0 coordinate class, this yields at least eleven A vertices, hence n>=20.

## Next issue

The surviving support has an isolated direction-0 coordinate population and a mandatory matching in one parity pair of star classes, while both parity populations occur. Determining whether all remaining cube-edge and spoke certificates can coexist is the next coherent bounded problem. Necessary type-pair survival is not an existence proof.
