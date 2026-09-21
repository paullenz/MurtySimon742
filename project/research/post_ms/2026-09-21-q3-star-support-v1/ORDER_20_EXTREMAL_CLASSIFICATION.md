# Exact order-20 extremal classification in the four-star branch

21 September 2026. Internally proved at Q3-antipodal-transversal scope; external review open.

## Theorem

Let G be diameter-two-critical with root neighbourhood Q3, antipodal-transversal outside codes and exactly four distinct star centres. If n=20, then

    m<=73.

Equality holds exactly when, up to cube isometry, A consists of one vertex in each of the six coordinate codes, one P0 vertex and one vertex in each even-centred star code; the P0 vertex is adjacent to all six coordinate vertices and the four stars induce K_1,3. Thus the order-20 equality graph is unique up to cube symmetry.

## Common structural inputs

The four centres form the even parity plane. At least five coordinate types, P0 and all four stars occur. With |A|=11, the code multiset is obtained from the ten-vertex order-19 minimum by one addition: the missing sixth coordinate, a duplicate present code, P1, or a fifth physical star.

The raw type classification gives coordinate--A edges only to P0. A coordinate--P0 edge needs the complementary coordinate as its third-A certificate unless P1 supplies a parity-side certificate; but coordinate--P1 edges are forbidden. Consequently an unpaired coordinate (whose complement type is absent) has no A-edge, and a present complementary pair can use a P0 vertex only as their unique common neighbour.

P0--star edges are impossible when P1 is absent. When a sole P0 and a P1 are present, a P0--star edge is still impossible: the star's centre spoke requires a nonadjacent P0 singleton witness, and no second P0 exists. Same-parity edges need the absent complementary parity target in the cases below.

By `PARITY_PLANE_STAR_FOREST_NECESSITY.md`, the star-induced graph is a star forest.

## Cases for the eleventh A vertex

### Sixth coordinate

There are six possible coordinate--P0 edges and at most three star edges. Hence e(A)<=9. Equality forces all six hub edges and a connected four-vertex star forest, necessarily K_1,3. The construction package proves this graph is D2C, so m=20+4(11)+9=73.

### Duplicate coordinate

Only two complementary coordinate pairs are present. With one P0, the duplicated pair contributes at most three hub edges and the other pair at most two; an unpaired type contributes none. Together with at most three star edges, e(A)<=8.

### Second P0

For each of the two present complementary coordinate pairs, at most one P0 can be their common hub: if both were, neither would be a unique common neighbour for the relevant A-edge certificate. Thus coordinate--parity edges contribute at most four. There is no P0--P0 edge because P1 is absent. With at most three star edges, e(A)<=7.

### One P1

The two complementary coordinate pairs contribute at most four coordinate--P0 edges. If P0--P1 is present, no P1--star edge can occur because it would give the centre-spoke P0 target a common A-neighbour; the remaining star forest has at most three edges, for total at most eight. If P0--P1 is absent, include the sole P1 with the star vertices in the antipode-bridge graph. Every edge has a star endpoint of bridge degree one, so this five-vertex graph is a star forest with at most four edges. Again e(A)<=8.

### Fifth physical star

The two coordinate pairs give at most four hub edges, and the five star vertices induce a star forest with at most four edges. Thus e(A)<=8.

These cases exhaust the code multisets and prove the bound and equality statement.

## Exact computational audit

`maxsat_fixed_codes.py` independently encodes all A-edges and maximizes their number subject to diameter two and edge criticality. `ORDER_20_MAXSAT_RESULTS.json` checks every possible eleventh code relative to a fixed missing coordinate. It returns maximum nine only for the sixth-coordinate case and reconstructs the equality graph. The proof above does not depend on the optimization run.
