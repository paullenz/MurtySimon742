# At least three distinct star centres are necessary

Date: 21 September 2026. Status: internally derived and finite-type replayed; external review open.

## Theorem

In a diameter-two-critical graph with root neighbourhood Q3 and every outside B-code an antipodal transversal, the star-code support is either empty or contains at least three distinct cube centres. Multiplicities of stars, coordinate faces and parity codes are arbitrary.

The distinction is between distinct codes, not physical vertices. In particular, duplicating two star codes arbitrarily cannot escape the obstruction.

## Certificate facts

Use the raw A-B and A-A certificate classifications proved in `TWO_ANTIPODAL_CENTRES_IMPOSSIBLE.md`. For coordinate H=C_i^epsilon and spoke s in H, set t=s xor e_i. If neither star S_t nor star S_(bar s) is present, the spoke must use its standard B-target t; consequently every A-neighbour of a vertex of code H avoids t. For parity P and spoke s in P, if neither S_s nor S_(bar s) occurs, every A-neighbour avoids s.

An A-edge can only be certified from an endpoint by a direct disjoint code, an undominated B target in the other endpoint's code, or a third A target of disjoint code adjacent to the other endpoint. Coordinate and parity codes dominate Q3; the unique disjoint transversal of a code is its complement.

## Two-centre exclusion: choose a separating coordinate

Suppose exactly two distinct star centres c,d occur. Translate c to 000 and choose i with d_i=1. Put H=C_i^0 and H'=C_i^1. Write bar d=d xor 111 and e_i for the i-th unit vector.

### Step 1. Only two outside targets may avoid the standard coordinate certificate

For a source of code H, the four outside targets range over H'. A star singleton-intersection replacement is possible only for t=d. A reverse B-end replacement is possible only for s=bar d, hence t=bar d xor e_i. The centre 0 supplies neither: 0 lies inside H and bar 0 lies outside H.

Thus every A-neighbour code K avoids

    F = H' minus {d, bar d xor e_i}.

The two retained vertices have the same parity, while the two vertices of F have the other parity. They form the two diagonals of the square H'. Inspection of the six coordinate codes gives: only H avoids both vertices of F. Among parity codes only P_(parity d) does so. Star S_d meets three vertices of H', so it cannot avoid F. The only other possible star is S_0. Therefore

    N_A(H) has types in {H, P_(parity d), S_0}.

This is an upper bound; S_0 need not actually be allowed. The symmetric argument through d gives

    N_A(H') has types in {H', P_(parity c), S_d}.

### Step 2. The parity possibility is impossible by symmetry of adjacency

Let P=P_(parity d). Every s in P except possibly c,d,bar c,bar d must use its direct parity certificate, so no neighbour of a P vertex can have a code containing such s.

There exists s in P intersect H outside those exceptions:

- if d has odd parity, the only exceptions in P are d and bar c=111; both lie outside H. Both vertices of P intersect H are therefore nonexceptional;
- if d has even parity, the only exceptions in P are c=000 and d; d lies outside H, so the other vertex of P intersect H is nonexceptional.

An H-coded neighbour contains that s and destroys its only certificate. Hence H--P edges are forbidden. Symmetrically the parity possibility for H' is forbidden. Consequently

    N_A(H) has types in {H,S_c},
    N_A(H') has types in {H',S_d}.

### Step 3. Neither remaining edge type is critical

A same-H edge has intersecting endpoint codes and no B-target certificate. Its third-A certificate would require an H--H' edge, forbidden by Step 2. Thus same-H edges are impossible.

For an H--S_c edge:

- the H endpoint's third-A target must have code H', but H'--S_c is forbidden;
- the S_c endpoint has no direct certificate, because H meets S_c;
- the only undominated B target of S_c is bar c, which lies outside H;
- a third-A target from S_c must have code S_(bar c). If absent, impossible; if present, then d=bar c and the required H--S_d edge is forbidden.

Thus H--S_c is impossible. H vertices are A-isolated. The symmetric argument makes H' vertices A-isolated.

### Step 4. Both opposite coordinate types are forced

For a physical star of centre c, its leaf spoke in direction i needs either a nonadjacent H' vertex or an adjacent star of centre bar c xor e_i. The latter centre has i-th bit c_i, so it is not d, and it is not c. It is absent. Hence H' occurs.

For a physical star of centre d, the direction-i leaf forces H by the same argument: its alternative star centre has i-th bit d_i and is neither c nor d.

The forced H and H' vertices are A-isolated and have disjoint B-codes. They have neither an edge nor a common neighbour, contradicting diameter two.

Thus exactly two distinct star centres are impossible.

## Zero or one centre

A nonempty single-centre support is impossible by the previously proved antipodal-pair theorem: all halfcube-star edges are eliminated; same-centre star edges would need the missing opposite star code as a third target; the star then has no A-neighbour to bridge its undominated cube antipode.

Therefore nonempty support has at least three centres.

## Scope and significance

The former extra-multiplicity/parity escape from the minimal two-opposite-star face is closed completely. The live star branch must now introduce at least a third distinct centre, or leave the antipodal-transversal hypothesis. This strengthens a finite-population bound to an arbitrary-multiplicity structural obstruction, but does not settle the full Q3 branch or the eventual conjecture.
