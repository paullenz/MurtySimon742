# No-singleton-star theorem in the Q3 antipodal-transversal branch

Date: 2026-09-21

## Theorem

Let `G` be diameter-2-critical, let `v` be a root with `B=N(v)` inducing `Q3`, and assume every `x∈A=V(G)\(B∪{v})` has `N_B(x)` equal to an antipodal transversal of Q3.

If one star code `S_c=N_Q[c]` occurs, then **at least one additional star-code A-vertex occurs**. Equivalently, there is no D2C graph in this branch with exactly one physical star vertex.

This statement is independent of `|A|`.

## Proof

Let x be the unique star vertex, with

`H_x=S_c=N_Q[c]`.

The B-vertex `bar c` is the unique vertex of Q3 not dominated by `S_c`: it is not in `S_c` and has no cube neighbour in `S_c`.

Since G has diameter two, x and `bar c` must therefore have an A-mediated two-path

`x-y-bar c`

for some A-neighbour y of x whose code `H_y` contains `bar c`.

Because x is assumed to be the only star vertex, y is an odd affine halfcube. There are only four such halfcubes containing `bar c`:

1. the parity halfcube `P_bar` opposite the parity side through c;
2. for each coordinate i, the coordinate halfcube `C_i={u:u_i=1-c_i}` opposite c in that coordinate.

We show that none can be adjacent to the unique star x while keeping all A-B edges critical.

### Case 1: y has opposite parity code `P_bar`

The star `S_c` meets `P_bar` in exactly the three leaves

`s_i=c⊕e_i`, `i=1,2,3`.

Fix one such leaf s. Consider the physical edge `ys`.

For a parity halfcube source, the standard criticality mechanism is direct: after deleting `ys`, the pair `(y,s)` must have no common neighbour. But x is adjacent to y and x is also adjacent to s, so the path

`y-x-s`

survives. Thus the standard parity certificate fails.

By the complete local transversal certificate table, the only two possible replacement mechanisms use a star code:

- a nonadjacent star `S_s`, giving a singleton-intersection `(y,z)` certificate; or
- an adjacent star `S_{bar s}`, giving an `(s,z)` B-end certificate.

The unique available star is `S_c`. For a leaf s of `S_c`, neither `S_s` nor `S_{bar s}` equals `S_c`. Hence neither replacement exists.

Therefore `ys` is noncritical, contradiction.

### Case 2: y has coordinate code `C_i={u:u_i=1-c_i}`

This halfcube meets `S_c` in the single leaf

`s=c⊕e_i`.

For the physical edge `ys`, the standard coordinate certificate is the outside cube vertex c: s is the unique `C_i`-neighbour of c. But because x is adjacent to y and c lies in `S_c`, the path

`y-x-c`

survives after deleting `ys`. So the standard certificate fails.

Again the local certificate table lists the only replacements:

- a nonadjacent star `S_c` (the unique transversal meeting `C_i` exactly in `{s}`); or
- an adjacent star `S_{bar s}`.

The only star present is x itself, of type `S_c`, but x is adjacent to y, so it cannot be the nonadjacent singleton-intersection certificate. The distinct star `S_{bar s}` does not exist.

Thus `ys` is noncritical, contradiction.

Both possible halfcube bridge types fail. Hence the required diameter-two bridge from x to `bar c` cannot exist when x is the only star vertex.

Therefore every star occurrence forces at least a second physical star vertex. QED.

## Consequences

1. The star branch has a genuine **propagation property** rather than merely a four-witness population tax.
2. The `|A|<=6` exclusion in `Q3_ANTIPODAL_TRANSVERSAL_STAR_FAN.md` can be viewed as the first finite corollary of this stronger mechanism plus the four-spoke fan and mandatory coordinate directions.
3. Any asymptotic star-supported escape must contain a nontrivial star subsystem. A lone star perturbation of the dense parity-bridge family is impossible at every order.
4. The next natural object is the graph on physical star vertices, labelled by their Q3 centres. A star-star edge can bridge both undominated antipodes only when the two centres are at Hamming distance two or three (`d∈N_Q[bar c]`), exactly the same relation that appears in the star-spoke alternatives. This gives a finite eight-centre propagation system to analyse next.
