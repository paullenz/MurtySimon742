# Q3 halfcube palette: every A-edge is paid for by an opposite-side A-pair

Date: 2026-09-21

## Setup

Let `G` be diameter-2-critical with root `v`, `B=N(v)` inducing `Q3`, and `A=V(G)\(B∪{v})`. In this note do **not** assume A is independent. Assume instead that every `x∈A` has a B-neighbourhood `H_x=N_B(x)` equal to one of the eight odd affine halfcubes of `Q3`.

For each odd linear direction `l∈{100,010,001,111}`, let `a_{l,0},a_{l,1}` be the numbers of A-vertices on the two affine sides. Define the number of opposite-side physical A-pairs

`P_opp = sum_l a_{l,0} a_{l,1}`.

Let `f=e(G[A])`.

## Raw A-edge witness lemma

Every critical A-edge can be charged to an opposite-side A-pair. More precisely, for an A-edge `xy`, at least one of the following holds.

1. **Endpoint certificate.** `H_x` and `H_y` are opposite sides of the same direction, and after deleting `xy` the endpoints themselves have no surviving two-path.

2. **Two-edge path certificate.** There is `z∈A` such that `H_z` is the opposite side of `H_x`, `xz` is a nonedge, and `y` is the unique common A-neighbour of `x,z`; deleting `xy` destroys the unique two-path `x-y-z` (or the symmetric statement with x and y exchanged).

### Proof

Delete `xy`. Any pair whose distance can increase must involve x or y; take it to be `(x,z)`.

- If `z=v`, root-to-A distance two survives through any B-neighbour of x.
- If `z∈B`, then either xz is an edge or, since every odd affine halfcube dominates Q3, there is `b∈H_x` adjacent to z. Thus `(x,z)` has a surviving path of length at most two not using `xy`.
- Hence `z∈A`. If z=y, deletion can make the endpoints exceed distance two only if `H_x∩H_y=empty`, which for odd affine halfcubes means they are opposite sides of the same direction.
- If `z!=y`, a lost length-two path using `xy` has form `x-y-z`. Any B-vertex in `H_x∩H_z` would give a surviving two-path, so the two halfcubes must be disjoint, hence opposite. Moreover y must have been their unique common A-neighbour.

This proves the lemma.

## Physical capacity theorem

A fixed unordered opposite-side pair `{u,z}` can certify at most two A-edges:

- if `uz` is an edge, the pair remains distance one unless that very edge is deleted, so it can certify at most `uz` itself;
- if `uz` is a nonedge, it can be broken by a single-edge deletion only when it has a unique common A-neighbour y, in which case only the two edges `uy` and `yz` can be certified by that pair.

Therefore any choice of one criticality certificate per A-edge gives the exact physical-resource bound

`f <= 2 P_opp = 2 sum_l a_{l,0}a_{l,1}`.      (OPP)

This is a graph-level witness-capacity inequality; no selected-system injection premise is being imported.

## Consequences

### Compatible palette recovers A-independence

If at most one side of every direction occurs, then `P_opp=0`, so `(OPP)` gives `f=0`. This recovers `X3_COMPATIBLE_HALFCUBE_A_EDGE_OBSTRUCTION.md` from a sharper witness-capacity viewpoint.

### Near-extremality forces a macroscopic opposite-side population

Every halfcube A-vertex has exactly four B-neighbours, so

`m = 8 + 12 + 4a + f = 20+4a+f`,

where `a=|A|` and `n=9+a`. Also

`M(n)=floor(a^2/4)+4a+17`.

Thus if

`m >= M(n)-C`,

then necessarily

`f >= floor(a^2/4)-3-C`.

Combining with `(OPP)`,

`P_opp >= (floor(a^2/4)-3-C)/2 = a^2/8-O(C+1)`.

Since there are only four directions, some direction l satisfies

`a_{l,0}a_{l,1} >= a^2/32-O(C+1)`.

In particular, for fixed C and sufficiently large a, **both opposite orientations of one halfcube direction occur linearly many times**. A simple finite consequence is

`min(a_{l,0},a_{l,1}) >= P_l/a`,

so along a fixed-defect near-extremal sequence one obtains

`min(a_{l,0},a_{l,1}) >= a/32-o(a)`

for at least one l.

Hence the only way the Q3 halfcube-palette branch can move from the sparse X3 blow-up toward quadratic edge density is through a macroscopic opposite-orientation regime. The next structural target is therefore not another compatible-palette inequality but the geometry of many opposite-side pairs and their unique A-middle vertices.

## Scope and caution

This note assumes every A-to-B neighbourhood is already one of the eight odd affine halfcubes. With A-A edges present, that property is not yet proved from raw D2C criticality. The result should therefore be used as a clean conditional branch theorem / diagnostic, not as a classification of all Q3-root D2C graphs.
