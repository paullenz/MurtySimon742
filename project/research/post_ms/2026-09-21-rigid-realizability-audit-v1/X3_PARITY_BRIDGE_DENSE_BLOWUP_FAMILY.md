# Dense parity-bridge blow-ups of the X3/Q3 root

Date: 2026-09-21

## Construction

Let `B=F_2^3` induce `Q3`, with root `v` adjacent to all of B.

For each coordinate `j=1,2,3`, choose one side `H_j={s:s_j=epsilon_j}` and add `c_j>=1` A-vertices with B-neighbourhood exactly `H_j`.

For parity, allow **both** sides

`P_0={s:s_1 xor s_2 xor s_3=0}` and `P_1={s:s_1 xor s_2 xor s_3=1}`,

with multiplicities `p,q>=0`. Join every parity-type A-vertex on side 0 to every parity-type A-vertex on side 1, i.e. put a complete bipartite `K_{p,q}` between the two parity classes. There are no other A-A edges.

Write `c=c_1+c_2+c_3>=3` and `a=c+p+q`.

## Theorem

Every graph in this construction is diameter-2-critical.

### Diameter two

- B-B pairs use the root.
- root-A pairs use any B-neighbour.
- A-B nonedges are repaired inside Q3: a coordinate halfcube gives the unique cross-coordinate cube neighbour; an opposite-parity B-vertex has all three cube neighbours in the required parity halfcube.
- A-A vertices with intersecting halfcube types share B-neighbours. Distinct non-opposite affine halfcubes intersect in two B-vertices, and equal types intersect in four.
- The only disjoint halfcube pair is the two parity sides used simultaneously; those A-vertices are adjacent by the inserted `K_{p,q}`.

Hence the graph has diameter two.

### Every edge is critical

1. **Root-B edge `vs`.** The antipode `bar s` has no cube common neighbour with s. Every coordinate or parity halfcube used here is defined by an odd-weight linear form, hence contains exactly one of `s,bar s`. Thus no A-vertex is adjacent to both, and v is the unique common neighbour of the antipodal B-pair. Deleting `vs` breaks that two-path.

2. **Cube edge `st` in coordinate direction j.** Choose any coordinate-j A-vertex x on the side containing s. It has no A-neighbours. The outside endpoint t has exactly one cube neighbour in `H_j`, namely s. Thus s is the unique common neighbour of x,t; deleting `st` makes their distance exceed two.

3. **Coordinate A-B edge `xs`.** Across the coordinate cut, the unique outside cube neighbour t of s has s as its unique neighbour in `H_j`. Since x has no A-neighbours, deleting `xs` makes `d(x,t)>2`.

4. **Parity A-B edge `xs`.** A parity halfcube is independent in Q3. Any A-neighbour y of x lies in the opposite parity A-class, whose B-neighbourhood is the opposite parity halfcube and therefore does not contain s. Thus after deleting `xs`, x and s have no common neighbour at all; the edge is direct-critical.

5. **Parity A-A edge `xy`.** The endpoints lie on opposite parity sides, so their B-neighbourhoods are disjoint. The A-graph between the two parity classes is complete bipartite and triangle-free, so x and y have no common A-neighbour. The root is adjacent to neither. Hence deleting `xy` leaves the endpoints with no common neighbour; the edge is direct-critical.

Therefore every edge is critical.

## Exact parameters

The graph has

`n=9+a`,

`m=8+12+4a+pq = 20+4a+pq = 4n-16+pq`.

At the Q3 root,

- `b=8`;
- the four antipodal B-pairs remain tight, so `p_root=4` and `u_root=0` in the rooted tight-pair notation;
- `Q=e(B)=12`;
- `f=e(A)=pq`;
- `delta=b(n-b)-m = 4a-12-pq`.

Therefore the exact rooted identity `delta=r-f` gives

`r=4a-12=4(a-3)`,

**independent of the parity split and of the quadratic internal density `pq`.** This makes the family a particularly clean hostile control for any future use of `(r,f,delta,Q)`: increasing the complete bipartite parity core changes f and delta but leaves the physical residual count r fixed and linear.

For a fixed a, this construction is densest when the mandatory coordinate population is minimal (`c=3`) and the remaining `a-3` vertices are split as evenly as possible between the two parity sides. Then

`m_dense(a)=20+4a+floor((a-3)^2/4)`.

Since

`M(n)=floor(a^2/4)+4a+17`,

the exact gap is

`M(n)-m_dense(a)=floor(a^2/4)-floor((a-3)^2/4)-3`.

Equivalently,

- if `a` is even: `M-m = 3a/2 - 5`;
- if `a` is odd: `M-m = (3a-11)/2`.

Thus the family passes through X3 at `a=3,n=12` (gap `-1`), gives `M-1` at n=13, `M-2` at n=14, and thereafter lies below M by an explicitly linear amount asymptotic to `3a/2`.

## Structural significance

This is a genuine graph-level escape from the independent-A X3 blow-up, and it explains the first opposite-orientation fixtures found by exhaustive halfcube-palette search at `a=5`: three coordinate witnesses plus one vertex on each parity side, joined by the single parity A-edge.

More importantly, it shows that opposite-side geometry can support **quadratic A-density** while preserving D2C: if p and q are balanced, `pq=Theta(a^2)`. The unavoidable price is that at least three coordinate A-vertices must remain outside that dense parity split to certify the three cube directions. Those three mandatory witness populations create the linear extremal deficit above.

So the correct graph-level question is sharper than “can multiple/opposite code classes occur?” They can, abundantly. The eventual near-M problem should ask whether one can reduce the mandatory coordinate-witness tax, or whether raw criticality forces a linear defect whenever a fixed Q3 root is used to support a dense opposite-parity A-core.

This family is triangle-containing for every size because every cube edge together with the root forms a triangle. It is therefore an infinite explicit hostile/control family on the **triangle-containing** side of the eventual second-extremal problem, not a triangle-free artefact.

## Diagnostic search provenance

An exhaustive bitset replay over all odd-halfcube palettes with `a<=5` and all A-edge subsets found the first opposite-orientation D2C fixtures exactly at `a=5`: one orientation of each coordinate type, both parity orientations, and precisely the edge joining the two parity vertices (eight labelled orientation choices). This diagnostic suggested the theorem above; the edge-by-edge proof, not the finite scan, establishes the family.
