# Opposite-edge plane: exact removal of parity multiplicities

21 September 2026. Internal structural reduction, conditional on existence of a graph with this support.

For star support {0,1,6,7}, the previous note forces both parity codes. In fact their physical populations induce a complete bipartite component of G[A], anticomplete to every coordinate and star vertex.

For a P0 vertex, spokes at 3 and 5 have neither singleton-star nor reverse-star alternatives. Every A-neighbour must avoid 3,5, leaving only C00,P1,S0,S6. C00 is A-isolated by the preceding theorem. P0--S0 and P0--S6 have no A-edge certificate: the relevant star antipode is odd and outside P0, their opposite-star target cannot neighbour P0, and the halfcube-side P1 target cannot neighbour either even star. The latter exclusion follows from the symmetric P1 spoke test, which requires every neighbour to avoid 2,4. Hence P0 can neighbour only P1, and conversely. Since these codes are disjoint, diameter two forces every cross-parity pair to be adjacent.

Consequently all but one vertex of each parity class may be deleted while retaining D2C, and conversely the two remaining vertices may be independently replaced by r,q>=1 false twins.

Diameter is preserved: all core/parity pairs have intersecting B-codes, missing parity/B pairs have cube paths, and opposite-parity pairs are adjacent. Each parity/B edge is direct-critical because the parity code is cube-independent and its A-neighbours avoid that B vertex. Each parity/parity edge is direct-critical. A remaining core A-edge cannot use an adjacent parity vertex as its third target, because parity is anticomplete to the core. A core spoke may use a parity singleton witness, but one physical copy suffices and has no A-neighbour in common with the core. Cube-edge witnesses are coordinate vertices, not parity vertices. Root-edge certificates persist. Thus neither collapse nor expansion loses a necessary certificate.

If the collapsed graph has order n0 and size m0, expansion gives exactly

    n=n0+r+q-2,
    m=m0+4(r+q-2)+(rq-1).

At fixed k=r+q the densest such expansion balances r,q. Its gap is

    M(n)-m = floor((k+n0-3)^2/4)-floor(k^2/4)-4k+10-m0.

For each fixed collapsed core this is (n0-11)k/2+O(1), with n0>=20. Thus parity expansion of any fixed realizable core lies below M(n) for all sufficiently large expansion sizes. This does not provide a uniform threshold over growing cores and does not establish that the core exists.

The next bounded task is therefore core realizability with exactly one P0 and one P1, retaining arbitrary star/coordinate multiplicities and the forced matching. Parity multiplicity need not be searched.

Exact arithmetic audit: if g(k) denotes the balanced-expansion gap above, then g(k+2)-g(k)=n0-11. Thus each parity subsequence increases by at least nine at every two-vertex expansion. Its initial values are g(2)=M(n0)-m0 and g(3)=M(n0+1)-m0-5. This gives a direct fixed-core eventual bound without relying on asymptotic notation.
