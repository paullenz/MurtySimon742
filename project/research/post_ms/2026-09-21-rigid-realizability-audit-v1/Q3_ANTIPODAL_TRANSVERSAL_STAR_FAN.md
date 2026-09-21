# Q3 antipodal transversals and the star-code certificate fan

Date: 2026-09-21

## Scope

Let `G` be diameter-2-critical. Fix a root `v` with `B=N(v)` inducing `Q3`, and put `A=V(G)\(B∪{v})`. In this note assume only that every `x∈A` has a four-element B-neighbourhood `H_x=N_B(x)` meeting every antipodal pair of Q3 in exactly one vertex. No rigid-cut, Hall, source-tuple, or selected-system hypothesis is used.

The purpose is to identify the first graph-level branch outside the odd affine halfcube palette.

## 1. The 16 antipodal transversals split 8+8

Q3 has four antipodal pairs. Hence there are exactly `2^4=16` four-sets meeting each antipodal pair exactly once.

Exactly eight are the odd affine halfcubes

`{z : l(z)=epsilon}`

for `l∈{100,010,001,111}` and `epsilon∈F_2`.

The other eight are precisely the closed cube neighbourhoods

`S_c=N_Q[c]={c,c⊕e_1,c⊕e_2,c⊕e_3}`,

one for each `c∈F_2^3`.

Proof: translate so that a chosen transversal contains `000`. The remaining choices select one vertex from each of `(001,110)`, `(010,101)`, `(100,011)`. The four affine choices through `000` are the three coordinate faces and the even-parity halfcube; the other four are the stars centred at `000,001,010,100`. Complementing gives the remaining eight. Equivalently, direct enumeration gives the same disjoint 8+8 partition.

Thus the complete odd-halfcube classification leaves only one type of antipodal-transversal code to understand: a star `S_c`.

## 2. General edge-criticality observation

If an edge `xs` with `x∈A`, `s∈B` is deleted, any newly long pair must contain `x` or `s`: every length-at-most-two path using `xs` is of the form `x-s-z` or `s-x-z`.

Let `x` have star code `H_x=S_c=N_Q[c]`. Every edge `xs`, `s∈S_c`, has an internal B two-path after deletion:

- for `s=c`, the three leaves of `S_c` are common B-neighbours of x and c;
- for a leaf `s=c⊕e_i`, the centre c is a common B-neighbour of x and s.

So no star A-B edge is direct-critical at its own endpoints.

For a newly long pair `(x,z)` with `z∈A` adjacent to s, a necessary condition is

`H_x ∩ H_z = {s}`;

otherwise another common B-neighbour survives.

For a newly long pair `(s,y)` with `y∈A` adjacent to x, a necessary condition is

`H_y ∩ N_Q[s] = ∅`;

otherwise either `sy` itself or a B-mediated two-path survives.

The B-vertex and root alternatives cannot be critical pairs here: at the centre all cube neighbours already lie in `S_c`; at a leaf each outside cube neighbour has a second neighbour in `S_c`; and x has three other B-neighbours for the root pair.

These observations give an exact code-level dichotomy for every star A-B edge.

## 3. Exact four-spoke star certificate fan

For each `s∈S_c`, define `D_s` to be the unique antipodal transversal with

`D_s ∩ S_c = {s}`.

Then `D_s` is always an odd affine halfcube:

- for the centre `s=c`, `D_c` is the parity halfcube containing c;
- for the leaf `s=c⊕e_i`, `D_s` is the coordinate halfcube on the side opposite c in coordinate i.

Also the unique antipodal transversal disjoint from `N_Q[s]` is

`Q3 \ N_Q[s] = N_Q[bar s]=S_{bar s}`.

Therefore criticality of the physical edge `xs` forces at least one of the following two mechanisms:

### Halfcube-side certificate

There is a vertex `z∈A` with code `H_z=D_s` such that deletion of `xs` can make `(x,z)` long. In particular xz must be a nonedge and no other common A-neighbour may survive.

### Star-neighbour certificate

There is a vertex `y∈A` adjacent to x with code

`H_y=S_{bar s}=N_Q[bar s]`,

so deletion of `xs` can make `(s,y)` long. Again the full D2C certificate additionally requires no surviving A-mediated two-path.

The two code types are unique. Thus a star vertex carries four distinct physical certificate spokes:

- centre c: parity halfcube through c **or** adjacent opposite-centre star `S_{bar c}`;
- leaf `c⊕e_i`: opposite-coordinate halfcube in direction i **or** adjacent star `S_{bar(c⊕e_i)}`.

No one typed vertex can discharge two different spokes.

### Immediate population consequence

Every star-code A-vertex forces at least four other A-vertices in distinct code types. Hence under the antipodal-transversal hypothesis,

`|A| >= 5`

whenever any star code occurs.

This is only the first tax. A star code is not a dominating set of Q3: its unique undominated B-vertex is `bar c`. Diameter two therefore additionally forces x to have an A-neighbour whose B-code contains `bar c`. How this bridge interacts with the four criticality spokes is the next load-bearing problem.

## 4. Cube-edge control remains coordinate-halfcube only

A star transversal cannot by itself provide the unique B-entry certificate for a cube edge. For a star `S_c`, an outside vertex at distance two from c has two neighbours in `S_c`, while the antipode `bar c` has none. A parity halfcube gives three entries at every outside vertex. Only a coordinate halfcube has an outside vertex with a unique neighbour across a cube edge.

Consequently, in any D2C graph satisfying the antipodal-transversal hypothesis, cube-edge criticality still forces at least one coordinate-halfcube A-vertex in each of the three coordinate directions. This is independent of the star fan above.

## 5. Diagnostic finite check

As a diagnostic only, an exhaustive bitset replay over all multisets of at most five antipodal-transversal codes, all A-edge subsets, and the fixed Q3-root skeleton found no star-containing D2C fixture. The unrestricted `a=5` scan first exceeded the local 60-second execution budget; after pruning by the necessary three-coordinate-direction condition it completed exhaustively. This finite check is not used as proof of nonexistence.

The structural reason for the empty small range is now visible: a star already demands four distinct certificate spokes, while its undominated antipode imposes an additional A-bridge constraint that can interfere with those certificates.

## 6. Consequence for the live programme

The independently replayed odd-halfcube theorem closes one half of the 16 antipodal-transversal codes. The star-fan theorem isolates the only remaining half and converts it from an unstructured search into a finite local certificate problem.

The next high-value step is to determine whether the antipode bridge can coexist with all four spoke certificates without forcing either:

1. another star and recursive certificate propagation;
2. both orientations of a coordinate direction, with a cube-edge criticality collision; or
3. an unavoidable extra population/edge tax large enough to give a linear deficit from `M(n)`.

Any of those outcomes would extend the graph-level Q3 classification strictly beyond the odd-halfcube palette.
