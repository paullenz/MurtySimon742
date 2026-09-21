# An explicit infinite A-layer blow-up family through X3

Date: 2026-09-21

## Construction

Let `B={0,1}^3` induce the 3-cube `Q3`, and add a root `r` adjacent to every vertex of B.  For `j=1,2,3`, choose a side `epsilon_j in {0,1}` of the j-th coordinate cut and put

`H_j={s in B : s_j=epsilon_j}`.

Choose multiplicities `m_j>=1`.  For each j add `m_j` independent A-vertices whose neighbourhood in B is exactly `H_j`.

Optionally choose one parity side

`H_4={s in B : s_1 xor s_2 xor s_3 = epsilon_4}`

and add `m_4>=0` independent A-vertices with that B-neighbourhood.  There are no A-A edges and no root-A edges.

Write `a=m_1+m_2+m_3+m_4`.

## Theorem — every such graph is diameter-2-critical

### Diameter two

- Any two B-vertices have the root as a common neighbour.
- The root is at distance two from every A-vertex through any B-neighbour.
- If `x in A` has neighbourhood H and `s in B\H`, then:
  - for a coordinate halfcube H, s has exactly one cube neighbour in H;
  - for a parity halfcube H, all three cube neighbours of s lie in H.
  Hence every A-B nonedge has distance two.
- Any two A-vertices of the same chosen type share all four B-neighbours.  Any two A-vertices of distinct chosen types have B-neighbourhoods that are two affine halfcubes with a 2-point intersection.  Thus every A-A pair has distance two.

Using only one orientation of each of the four cut types is essential: opposite sides of one cut are disjoint and would give A-vertices with no common neighbour.

### Every edge is critical

There are three edge types.

1. **Root-cube edge `rs`.** Let `bar(s)` be the antipode of s.  The pair `s,bar(s)` has the root as its unique common neighbour: Q3 antipodes have no cube common neighbour, and every A-neighbourhood chooses exactly one point from each antipodal pair.  Deleting `rs` therefore makes `d(s,bar(s))>2`.

2. **Cube edge `st`.** Suppose it flips coordinate j.  Exactly one endpoint, say s, lies in the chosen coordinate halfcube `H_j`.  Any A-vertex of coordinate type j is adjacent to s and not t.  Moreover t has exactly one cube neighbour in `H_j`, namely s.  Since A is independent, s is the unique common neighbour of t and that type-j A-vertex.  Deleting `st` makes their distance exceed two.  The requirement `m_j>=1` for j=1,2,3 is exactly what certifies all three directions of cube edges.

3. **A-B edge `xs`, with `s in N(x)=H`.**
   - If H is a coordinate halfcube, let t be the unique cube neighbour of s across that coordinate cut.  Then t lies outside H and s is the unique cube neighbour of t in H.  Since x has no neighbours outside B, `N(x) cap N(t)={s}`.  Deleting `xs` makes `d(x,t)>2`.
   - If H is a parity halfcube, H is an independent set of Q3.  Therefore x and s have no common neighbour at all after deleting `xs`; the edge itself is direct-critical.

Thus every edge is diameter-2-critical. ∎

## Exact parameters

The graph has

`n = 9+a`,

`m = 8 + 12 + 4a = 20+4a = 4n-16`.

At the cube root:

- `b=8`;
- the four antipodal cube pairs are tight, so `p=4,u=0`;
- `Q=e(B)=12`;
- `f=e(A)=0`;
- `delta=b(n-b)-m = 4a-12 = 4(n-12)`;
- therefore the exact rooted identity gives `r=delta=4(a-3)`;
- `q=Q-p(p+u-1)=12-4*3=0`;
- `lambda=2p+u-a-1=7-a=16-n`.

For `a=3,m_4=0,m_1=m_2=m_3=1`, this is exactly the published 12-vertex X3 graph: `n=12,m=32`, while `M(12)=31`.

For `a=4`, the family gives the five one-vertex D2C extensions isolated in `X3_ONE_VERTEX_MULTICLASS_EXTENSIONS.md` (up to the choices of existing/optional orientations and duplicate type).  From `n=13` onward the family is already below `M(n)` and then falls linearly while `M(n)` is quadratic.

## Structural significance

This family resolves an important ambiguity exposed by the graph-level regression.

- Multiple A code-pair classes are not merely possible: they persist in an explicit infinite D2C family.
- The price is visible exactly in the rooted residual ledger: every A-vertex beyond X3 adds four edges but increases `delta=r-f` by **four**, while `f` remains zero and `Q` remains fixed at 12.
- Hence the correct eventual-extremal obstruction is not “multiple classes cannot occur.”  It must show that a near-extremal graph cannot afford the **inter-class missing-edge / residual-defect bill**, unless substantial A-A density is introduced; and then that density must itself pay through criticality.

This gives a concrete bridge between the mandatory X3 negative control and the eventual problem: X3 is the zero-residual endpoint of a linear-defect blow-up ray rather than an isolated anomaly.

## Independent computational support

Before writing the proof, direct D2C checks were run on:

- all 128 one-vertex rooted X3 extensions;
- all ordered 2- and 3-vertex additions from the five observed admissible code orientations;
- 600 random valid-orientation blow-ups with 1 through 20 added vertices.

Every tested multiplicity pattern obeying the construction above was D2C.  The proof above, not those finite checks, is the basis for the theorem.
