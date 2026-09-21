# Global substitution charge for coordinate-halfcube A-vertices

Date: 2026-09-21

## Scope

In the Q3-root antipodal-transversal branch, let `C` be the physical A-vertices whose B-codes are one of the six coordinate halfcubes `C_i^epsilon`. No restriction is imposed on multiplicities, and other star/parity A-vertices may also be present.

For each direction i, let

`C_i^0`, `C_i^1`

also denote the corresponding physical code classes, with sizes `a_i,b_i`.

Define

`P_coord = sum_i a_i b_i`

(the number of possible physical pairs between complementary coordinate codes),

`E_comp = sum_i e(C_i^0,C_i^1)`,

`M_comp=P_coord-E_comp`,

and let `E_noncomp` be all other edges of `G[C]` (same-code edges and edges between different coordinate directions).

## Coordinate-source A-edge classification

Fix a coordinate vertex x of code `H=C_i^epsilon` and an incident A-edge `xy`. If a critical pair involving x certifies deletion of xy, there are only two possible mechanisms.

### Direct endpoint

The endpoint pair `(x,y)` can become long only if `H_y∩H=∅`. Among all 16 antipodal transversals, the unique disjoint code is the complementary coordinate halfcube

`C_i^{1-epsilon}`.

Thus direct certification is available only on complementary-coordinate edges.

### Third-A target

A pair `(x,z)` with z adjacent to y can become long only if `H_z∩H=∅`, hence again z lies in the complementary coordinate code. Necessarily xz is a nonedge and y is the unique common A-neighbour of x,z.

### No B-target mechanism

There is no analogue of the star antipode bridge. A coordinate halfcube dominates every cube vertex outside itself through the unique crossing coordinate edge; vertices inside the halfcube are already adjacent to x. Hence no B-target can become longer than two after deleting an A-edge incident to x.

## Global injection

Every noncomplementary coordinate-coordinate edge must therefore be certified from one endpoint by a third-A mechanism. Choose one such endpoint and map the edge to the resulting missing complementary-code physical pair.

A fixed missing complementary pair `{x,z}` has at most one common A-neighbour y, by the certificate condition. That one y can support at most the two path edges `xy` and `yz`. Hence each missing complementary pair receives at most two oriented noncomplementary edges.

Therefore

`E_noncomp <= 2 M_comp`.

Equivalently,

`e(C)=E_comp+E_noncomp <= P_coord + M_comp = 2P_coord-E_comp`.

In the useful bookkeeping form,

`E_noncomp <= 2(P_coord-E_comp)`.

## Fixed-direction corollary

Restrict to one direction i. Inside `C_i^0∪C_i^1`, the noncomplementary edges are exactly same-code edges. A missing cross pair has a unique common A-neighbour lying on at most one side if it is to certify a same-code edge. Thus the factor improves from two to one:

`e(G[C_i^0∪C_i^1]) <= a_i b_i`.

So each opposite coordinate-code pair separately satisfies an exact Mantel-type product bound, even in the presence of the other four coordinate classes and star/parity vertices.

## Strategic consequence

This is the natural extension of the six-witness internal-edge argument to arbitrary coordinate multiplicity. Extra coordinate vertices do not create free density: every edge outside the three complementary bipartite channels must be paid for by deleting a complementary pair, with physical unique-common-neighbour multiplicity at most two globally and at most one within a fixed direction.

The remaining difficulty is to combine this internal coordinate charge with the star-leaf certificate requirement (at least one certifying coordinate nonneighbour per star per direction) and with cross-direction/star-coordinate edges. That is now the exact extra-multiplicity branch exposed by the minimal-face closure.
