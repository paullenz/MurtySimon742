# Parity-plane support: exact minimum order and a dense extension

Date: 21 September 2026. Status: internally proved at stated scope; external review and novelty assessment open.

## Theorem

In the Q3-antipodal-transversal setting, suppose the star centres are exactly one parity class of the cube. Then at least five distinct coordinate codes and the parity code containing the centres occur. Consequently n>=19. This is sharp: there is an explicit 19-vertex, 66-edge D2C graph of this type.

Moreover, for every n>=19 there is a triangle-containing D2C graph with exactly that four-centre support and

    m = 26+4(n-9)+floor((n-18)^2/4),
    M(n)-m = floor((9n-139)/2).

This lowers the minimum construction order and improves the earlier six-coordinate family asymptotically, but is not an optimal-density theorem over the support class. The six-coordinate family is denser at n=20,21,22,23; they tie at n=24,25; this five-coordinate family is denser for every n>=26. The exact edge difference is ceil((n-25)/2).

## 1. A missing coordinate code forces a physical matching

Normalize the centres to the four even cube vertices T={0,3,5,6}. Suppose coordinate code D=C_i^epsilon is absent. Exactly two even centres c,d lie on the opposite side c_i=d_i=1-epsilon, and d=bar c xor e_i.

For any star vertex x of centre c, its direction-i leaf s=c xor e_i has no halfcube certificate because D is absent. It must use an adjacent star y of centre d=bar s. The critical pair is (s,y), where s=bar d is y's unique undominated cube vertex. Therefore x must be the **unique A-neighbour of y whose code contains bar d**.

The same absent coordinate code applies to y's direction-i leaf. It needs some star z of centre c for which y is the unique antipode bridge. But every S_c code contains bar d, and y already has the unique such neighbour x. Hence z=x. Thus y is also the unique antipode bridge of x.

Since every physical vertex in either class needs such a partner, these two star classes are matched bijectively, and each matched vertex has no other antipode bridge. In particular their multiplicities are equal.

This is a physical matching assertion, not merely a centre-level adjacency assertion.

## 2. At most one coordinate code can be absent

The six coordinate codes correspond to the six unordered pairs of the four even centres: absence of C_i^epsilon forces the matching between the two centres on the opposite side.

If two absent codes correspond to pairs sharing a centre, every physical vertex of that centre would have to have its unique antipode bridge in two different star classes. Contradiction.

If the pairs are disjoint, they are the two edges of one coordinate-direction perfect matching of the parity tetrahedron. The two missing codes are then C_i^0 and C_i^1 for the same i. But cube-edge criticality requires at least one coordinate code in every direction. Contradiction.

Therefore at least five of the six coordinate codes occur.

For each star's centre spoke the opposite star centre is odd and absent. The halfcube alternative forces P0 to occur. Four star centres + five coordinate codes + one parity vertex give |A|>=10, hence n>=19.

## 3. Sharp construction

Take exactly one vertex of each of

    C00, C01, C10, C11, C20,
    S0, S3, S5, S6,

and r>=1 vertices of P0 and q>=0 vertices of P1. Designate one P0 vertex h. The code C21 is absent.

Inside A put:

- the two star edges S0--S3 and S5--S6;
- edges from h to C00,C01,C10,C11;
- all P0--P1 edges.

The C20 vertex is A-isolated. Add the root/Q3 skeleton and each coded four-element A-B neighbourhood as usual.

With r=1,q=0 this has a=10, n=19 and m=66.

## 4. Complete criticality check

The proof follows the fully detailed six-coordinate construction, with the following explicit changes; all other edge/pair types use exactly the witnesses listed there.

### Diameter

The only opposite-coordinate pairs present are in directions 0 and 1; they share h. C20 has no complementary-code vertex, so its A-isolation causes no missing diameter-two pair. Each star reaches its undominated antipode through its matched partner of a different even centre. P0--P1 pairs are adjacent. All remaining A pairs have intersecting B-codes.

### Cube edges

For directions 0 and 1, use the coordinate side containing the even endpoint; its sole A-neighbour h avoids the odd outside target. For direction 2, the C20 vertex is A-isolated and supplies a clean entry across every direction-2 cube edge.

### A-B edges

All C20 spokes use their usual clean coordinate certificate, since it has no A-neighbours. Connected coordinate vertices, P0/P1 vertices and root edges retain the witnesses from the six-coordinate construction.

For star S0's leaf at 4, use the adjacent S3 vertex: 4 is the latter's undominated antipode and S0 is its only A-neighbour. For S3's leaf at 7, use S0 in the same way. These are the only spokes whose coordinate witness C21 is missing.

The S5 and S6 direction-2 spokes use the present C20 vertex. All remaining star spokes use the present coordinate or P0 witnesses. Their A-neighbour sets have no common vertices, as before.

### A edges

Each star edge has degree-one endpoints and a unique antipode bridge. Each coordinate--h edge is certified by the opposite coordinate vertex, with h its unique common neighbour. P0--P1 edges are direct-critical. Thus every edge is covered.

## 5. Density

Here a=9+r+q and e(A)=6+rq, so

    m = 26+4a+rq.

At fixed a>=10, balance r,q to maximize rq=floor((a-9)^2/4). Therefore

    M(n)-m = floor(a^2/4)-floor((a-9)^2/4)-9
           = floor(9a/2)-29
           = floor((9n-139)/2).

For n>=19 this deficit is positive and linear. This is a quadratic-density infinite family, not a counterexample to the eventual target.

## Failed inference preserved

The necessary relation 'coordinate vertices can only have even-parity A-neighbours' does **not** force all six coordinate codes to occur. A coordinate vertex can be A-isolated when its complement is absent and still certify all cube edges in its direction. The five-coordinate construction is a counterexample to that tempting inference. The matching argument, rather than a clean-entry shortcut, is what correctly gives the sharp lower bound of five coordinate codes.

## Trust boundary

The n>=19 lower bound is for the parity-plane star-support class only. It is not a minimum-order claim for all star-containing graphs, other four-centre planes, or larger star supports. The family attains the bound and the support minimum; no global extremal-density optimality is claimed.
