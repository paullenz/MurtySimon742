# Complete local A–B certificate table for Q3 antipodal-transversal codes

Date: 2026-09-21

## Scope

Let `G` be diameter-2-critical, let `v` be a root with `B=N(v)=Q3`, and assume every `x∈A=V(G)\(B∪{v})` has `H_x=N_B(x)` equal to one of the 16 antipodal transversals of Q3. By `Q3_ANTIPODAL_TRANSVERSAL_STAR_FAN.md`, these are exactly the eight odd affine halfcubes and the eight stars `S_c=N_Q[c]`.

This note classifies all possible local certificate *types* for an A–B edge. It is a necessary-condition table: a listed code type still has to satisfy the corresponding A-adjacency uniqueness condition to be a genuine critical pair.

## General observation

For an edge `xs`, `x∈A`, `s∈B`, any pair that can become longer after deleting `xs` must contain x or s. Thus the only possibilities are:

1. the endpoint pair `(x,s)`;
2. `(x,t)` with `t∈N_Q(s)`;
3. `(x,z)` with `z∈A`, `s∈H_z`;
4. `(s,y)` with `y∈N_A(x)`.

Pairs entirely in B retain the root as a common neighbour, and the root-A pair has other B intermediates because every code has size four.

The 16-code universe makes the singleton-intersection and closed-neighbourhood-avoidance possibilities unique, yielding the table below.

## 1. Coordinate halfcube source

Let

`H_x=C_i^epsilon={u:u_i=epsilon}`,

and let `s∈H_x`. Put `t=s⊕e_i`, the unique cube neighbour of s outside H.

The edge `xs` can be critical only through one of the following three mechanisms.

### C1. Standard outside-end certificate

The pair `(x,t)` becomes long. In B, s is the unique H-neighbour of t. Therefore this works exactly when no A-neighbour of x has a B-code containing t.

This is the mechanism used in the star-free odd-halfcube classification.

### C2. Star singleton-intersection certificate

The unique antipodal transversal K satisfying

`K∩H_x={s}`

is the star

`K=S_t=N_Q[t]`.

Thus `(x,z)` can replace the standard certificate only when a star-code vertex `z` of type `S_t` exists, `xz` is a nonedge, and x,z have no common A-neighbour.

### C3. Adjacent antipodal-star B-end certificate

For `(s,y)` to become long, `H_y` must avoid `N_Q[s]`. The unique transversal doing so is

`H_y=S_{bar s}`.

Thus the third possibility is an A-neighbour y of x of star type `S_{bar s}`, with no surviving alternative s–y two-path.

No other transversal code can certify `xs`.

## 2. Parity halfcube source

Let H_x=P be one parity class and s∈P. Since P is independent in Q3, `(x,s)` has no B common neighbour after deleting `xs`.

The edge can be critical only through one of three mechanisms.

### P1. Standard direct endpoint certificate

`(x,s)` itself becomes long. This requires that no A-neighbour of x have a B-code containing s.

This gives the star-free rule that parity vertices may have A-neighbours only on the opposite parity side.

### P2. Star singleton-intersection certificate

The unique transversal meeting P exactly in `{s}` is the star centred at s:

`S_s=N_Q[s]`.

Thus `(x,z)` can replace the direct certificate only through a nonadjacent star-code vertex z of type `S_s`, with no common A-neighbour of x,z.

### P3. Adjacent antipodal-star B-end certificate

As before, an `(s,y)` certificate requires `H_y∩N_Q[s]=∅`, hence uniquely

`H_y=S_{bar s}`.

Thus y must be an A-neighbour of x of star type `S_{bar s}` with the required uniqueness.

No other transversal code can certify `xs`.

## 3. Star source

Let `H_x=S_c=N_Q[c]` and `s∈S_c`. The star-fan theorem gives exactly two mechanisms.

### S1. Unique halfcube singleton-intersection certificate

The unique transversal `D_s` with

`D_s∩S_c={s}`

is an odd halfcube: parity through c when `s=c`, and the opposite coordinate halfcube in direction i when `s=c⊕e_i`. A nonadjacent vertex z of type `D_s` may certify `(x,z)`.

### S2. Adjacent antipodal-star B-end certificate

The only code avoiding `N_Q[s]` is `S_{bar s}`. Thus an adjacent star of that type may certify `(s,y)`.

There is no B-only/direct star certificate.

## 4. Star-supported deviation principle

The table gives a useful exact interpretation of every departure from the already-classified odd-halfcube palette.

### Coordinate deviation

Let x have coordinate code H and let y be an A-neighbour with code K. For each outside vertex

`t∈K∩H^c`,

write `s=t⊕e_i∈H`. The neighbour y destroys the standard C1 certificate for the physical edge `xs`, because `x-y-t` survives deletion of `xs`.

Therefore each such s must switch to C2 or C3. The required star code types are distinct as s varies. Hence a noncanonical coordinate adjacency is supported by at least

`|K∩H^c|`

distinct star certificate types/vertices across the affected physical edges.

In particular:

- K=H costs 0 at this stage;
- a nonopposite odd halfcube K costs 2;
- the opposite coordinate halfcube costs 4;
- a star K costs 1,2, or 3 according to its intersection size with H.

### Parity deviation

Let x have parity code P and y an A-neighbour with code K. For every

`s∈P∩K`,

the neighbour y destroys the direct P1 certificate for `xs`, since `x-y-s` survives. Each affected s must therefore switch to P2 or P3, again using a distinct star type for each s.

Thus a noncanonical parity adjacency is supported by at least

`|P∩K|`

distinct star certificate types/vertices across the affected physical edges.

For odd-halfcube K this cost is 0 only for the opposite parity side; it is 2 for a coordinate halfcube and 4 for the same parity side. For a star K the intersection size is 1 or 3 according to the centre parity.

## 5. Recovery of the star-free theorem

If no star codes occur, mechanisms C2/C3/P2/P3/S1/S2 disappear. Then:

- every coordinate vertex must use C1 on all four A-B edges, forcing every A-neighbour to have the same coordinate halfcube;
- every parity vertex must use P1 on all four edges, forcing every A-neighbour to lie on the opposite parity side.

The previous complete odd-halfcube palette classification follows immediately. Thus the star-free theorem is not a separate phenomenon: it is the zero-star face of this complete local transition table.

## 6. Strategic consequence

Any Q3-root antipodal-transversal construction that improves on the dense parity-bridge family must pay for every forbidden halfcube-halfcube adjacency by invoking star-specific criticality certificates. The only remaining asymptotic escape is therefore quantitatively star-supported.

The next step is to turn this local support requirement into an edge-deficit inequality: charge noncanonical A-edges and star antipode bridges against the finite set of star spokes, while preserving the exact `m=20+4a+e(A)` identity. A successful charge would give a graph-level linear gap from M throughout the full antipodal-transversal universe.
