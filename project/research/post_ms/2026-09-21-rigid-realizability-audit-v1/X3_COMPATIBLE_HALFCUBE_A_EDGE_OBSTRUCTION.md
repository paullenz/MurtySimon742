# Compatible Q3 halfcube palettes cannot carry A-A edges in a D2C graph

Date: 2026-09-21

## Theorem

Let `G` have a root `v` with `B=N(v)` inducing `Q3`, and let `A=V(G)\(B∪{v})`. Suppose every `x∈A` has a B-neighbourhood `H_x` equal to one of the eight odd affine halfcubes of `Q3`, and suppose the palette is **compatible**: no two A-vertices use opposite sides of the same linear form. Equivalently, every pair `H_x,H_y` intersects.

If `G` has diameter two, then every A-A edge is redundant for diameter two. Consequently a diameter-2-critical `G` has

`e(G[A])=0`.

Thus no internal A-density can rescue the linear-defect X3 blow-up while the graph stays inside one compatible odd-halfcube palette.

## Proof

Fix an A-edge `xy` and delete it. We show every pair of vertices remains at distance at most two.

Only a pair involving `x` or `y` could have used the deleted edge in a path of length at most two. By symmetry it is enough to check pairs `(x,z)`.

1. `z=y`: compatibility gives `H_x∩H_y != empty`, so `x` and `y` retain a two-path through B.

2. `z∈B` and a lost two-path was `x-y-z`: then `z∈H_y`. If `z∈H_x`, the pair is still adjacent. If `z∉H_x`, every odd affine halfcube dominates Q3: a coordinate halfcube gives exactly one cube neighbour of `z` in `H_x`, while a parity halfcube gives all three cube neighbours in `H_x`. Hence some `b∈H_x` is adjacent to `z`, giving the surviving path `x-b-z`.

3. `z∈A` and a lost two-path was `x-y-z`: compatibility gives `H_x∩H_z != empty`, so `x` and `z` retain a two-path through B.

4. `z=v`: the deleted A-A edge is irrelevant to every root-A two-path, which uses a B-neighbour of `x`.

Pairs not involving `x` or `y` cannot use `xy` in a path of length at most two. Therefore `G-xy` still has diameter at most two, contradicting edge-criticality. So no A-A edge exists.

## Structural consequence

Combined with `X3_Q3_ROOT_INDEPENDENT_A_CLASSIFICATION.md`, this isolates the only way a Q3-root branch could ever acquire the quadratic A-density needed for near-extremality: it must **leave the compatible halfcube palette**. In particular it must introduce at least one of:

- opposite orientations of the same halfcube direction, whose B-neighbourhoods are disjoint and therefore require A-mediated distance-two repair; or
- B-neighbourhoods outside the odd-halfcube class, which likewise means the independent-A classification hypotheses have broken.

So the residual-defect escape is not “add A-A edges to the X3 blow-up”. Internal density requires a qualitative change in the rooted code geometry first.

## Scope

This is a raw graph-level observation. It uses neither Hall selection nor the conditional rigid one-code interface.
