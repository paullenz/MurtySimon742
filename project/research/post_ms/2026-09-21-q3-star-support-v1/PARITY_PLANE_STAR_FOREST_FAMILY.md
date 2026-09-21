# A realizable four-centre star family with quadratic density

Date: 21 September 2026. Status: internally proved by explicit edge-deletion witnesses; external review and novelty assessment open.

## Construction

Fix Q3 on B={0,...,7}, with root v adjacent to all eight B vertices. Partition A into:

1. Coordinate vertices C: a positive arbitrary number in each of the six coordinate codes C_i^epsilon. Let t=|C|>=6.
2. Star vertices S: codes drawn from the four even centres {0,3,5,6}, with each centre occurring at least once. Let s=|S|>=4. On S choose a forest F whose every component is a nontrivial star, with every edge joining different codes. Thus every edge has a degree-one endpoint, no vertex is isolated, and e(F)=s-k where k is the component count.
3. r>=1 even-parity vertices U of code P0; designate one h in U.
4. q>=0 odd-parity vertices W of code P1.

Join every A vertex to its four coded B vertices. Inside A, put exactly:

- the edges of F;
- every C--h edge;
- every U--W edge.

There are no other A edges. The star forest does not need to be properly coloured beyond its edges joining distinct codes; repeated colours among leaves/components are allowed, and all four even-centre colours must occur globally.

## Theorem

Every graph in this construction is diameter-two-critical. Its star support is exactly the parity affine plane, showing that the four-centre lower bound is sharp.

Write a=t+s+r+q, n=a+9. Then

    m = 20+4a+t+(s-k)+rq.

The proof below covers every pair type for diameter and every edge type for criticality.

## Diameter two

- Every B pair has common neighbour v. Every v--A pair has the four B entries.
- Coordinate and parity codes dominate Q3. A star S_c dominates every cube vertex except bar c. A forest neighbour has a different even centre d, hence dist(c,d)=2 and its code S_d contains bar c. Thus it supplies the missing length-two path.
- Two A vertices with intersecting B-codes share a B neighbour. The only disjoint code pairs are complementary types. Opposite coordinate vertices share h. P0--P1 vertices are adjacent. No opposite-star codes occur because complementation changes parity.

Thus all pairs are at distance at most two, and v is nonadjacent to A, so diameter is exactly two.

## Criticality: root and cube edges

For v--b, the pair b,bar b has exactly one common neighbour v: antipodes have no common cube neighbour, and a transversal contains only one of them. Deleting v--b destroys their only two-path.

For a cube edge st, orient it so s is even and t is odd. The coordinate vertex x on the side containing s in that edge direction has s as its unique coded cube neighbour of t. Its only A-neighbour h has even code and does not contain t. Therefore deleting st makes x,t farther than two.

## Criticality: coordinate-to-B edges

Let x have coordinate code H=C_i^epsilon, let b in H, and put u=b xor e_i.

- If u is odd, x,u have exactly the one two-path x--b--u: h's even code omits u. Deleting xb destroys it.
- If u is even, a star vertex z of code S_u exists. H intersect S_u={b}; xz is a nonedge; x has only h as an A-neighbour while z has only star neighbours. Thus x,z have exactly common neighbour b. Deleting xb destroys their only two-path.

## Criticality: parity-to-B edges

For any odd-parity vertex w and b in P1, deleting wb leaves no common neighbour: B parity is independent and all A-neighbours of w have even code. This is a direct endpoint certificate.

The same direct certificate works for u in U other than h, since its A-neighbours have odd code. For h--b with b even, choose a star vertex z of code S_b. Its code meets P0 only at b. There is no h--z edge and no common A-neighbour: h's neighbours have coordinate or odd-parity codes, while z's neighbours are stars. Hence b is their unique common neighbour, certifying h--b.

## Criticality: star-to-B edges

For star x of code S_c, use P0 for its centre spoke and C_i^(1-c_i) for its direction-i leaf spoke. Every such halfcube exists and meets S_c in exactly the corresponding spoke vertex. It is nonadjacent to x, and their A-neighbour sets are disjoint: x only has star neighbours, while halfcube vertices have coordinate/parity neighbours. The spoke is therefore their unique common neighbour, giving a deletion witness for every star-to-B edge.

## Criticality: A edges

- For x--h with x coordinate-coded, choose any physical z in the opposite coordinate class. x,z are nonadjacent, have disjoint B-codes and have exactly common neighbour h. Thus x--h is critical.
- A U--W edge has disjoint B endpoint codes and no common A-neighbour (U neighbours are W and possibly C; W neighbours are U). It is direct-critical.
- Every forest edge has a degree-one star endpoint x of centre c. Its neighbour has a different even centre, so contains bar c. Since x's only A-neighbour is that forest neighbour, and S_c does not dominate bar c, deleting the forest edge makes x,bar c farther than two.

All edge types are covered, proving the theorem.

## Dense specialization and exact deficit

Take exactly one vertex in each coordinate code (t=6) and four star vertices, one of each even centre, forming K_(1,3) (s=4,k=1). Vary r>=1 and q>=0. Then a=r+q+10 and

    m = 29+4a+rq.

For fixed a>=11, balance r,q so rq=floor((a-10)^2/4). Since 10 is even,

    M(n)-m = floor(a^2/4)-floor((a-10)^2/4)-12
           = 5a-37
           = 5n-82.

Therefore for every n>=20 this yields a triangle-containing D2C graph with exactly four star centres and

    m = M(n)-(5n-82) = floor((n-19)^2/4)+4n-7.

It has quadratic leading density but stays below M by a positive linear margin. The smallest specialization has n=20, m=73 and M(20)=91.

## Interpretation

This is an actual infinite graph family, not an abstract parameter survivor. It blocks any attempted proof that all star codes are impossible and makes the four-centre support lower bound sharp. It provides a new explicit positive regression family for the Q3-star interface. It is not an eventual counterexample, not evidence that the remaining affine-plane orbits exist, and not a claimed optimum over four-centre graphs.
