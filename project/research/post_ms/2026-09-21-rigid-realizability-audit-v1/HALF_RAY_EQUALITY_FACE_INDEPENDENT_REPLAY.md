# Independent replay of the corrected half-ray equality face

Date: 2026-09-21

Status: independent hostile reconstruction at the **conditional one-code rigid / residual-one half-ray scope**. This note does not establish reachability of that interface from an arbitrary D2C graph. It deliberately avoids the superseded H--U private-foot coordinate-slice argument.

## Setup

Use the corrected half-ray notation

- `p=2t`, `c=y=t`, `h=2t-1`, `u=t+1`, `k=2`, `J_2=empty`;
- `R_q,R_j,S` are respectively reverse-private, reverse-residual, and shared H--U mechanisms;
- `a=2M_H-R_q`, `b=h-R_j`, `c0=(u-2)-S`;
- `Delta=a+b+c0`, so `L_H=3t-1+Delta`;
- `N=R_j=h-b` is the number of residual-`q_j`-saturated H-rows;
- each saturated row has its unique residual-bar carrier `z_i`;
- `D(z_i)` is the private-coordinate support of that carrier.

The corrected residual-slot collapse gives

`a+c0 >= binom(N,2)`

and therefore

`Delta >= h-N+binom(N,2)`.

At the equality face `Delta=h`, only `N=0,1,2,3` are possible and

`a+c0=N`.

The purpose of this note is to reconstruct **all four** faces from the physical row/resource geometry, because the 21 September daily audit correctly required this before `Delta>=h+1` or the later superconstant package may be promoted.

## N=0

Then `a=c0=0`, `R_j=0`, `R_q=2M_H`, and `S=t-1`.

Every used shared physical resource is either B1 or endpoint-indexed. Endpoint-indexed resources are H-anticomplete, so

`e(H,U)<=t-1`.

But the exact mechanism partition gives

`e(H,U)=R_q+R_j+S=2M_H+t-1`.

Hence `M_H=0`. Every one of the `t-1` shared resources must therefore be B1.

Two H-rows touched by B1 vertices cannot be adjacent: the two B1 vertices destroy the two private-foot certificate orientations of that H-edge. Since `M_H=0`, H is complete, so all B1 vertices must attach to one H-row. On that row the exact local identity with `m_i=0` gives `d_U(h_i)<=3`. Therefore `t-1<=3`.

Thus `N=0` is impossible for `t>=5`.

## N=3

Here `a+c0=3`. The coarse inequalities alone do **not** force `(a,c0)=(0,3)`; in particular `(2,1)` survives the scalar EC-5/EC-6 bounds. This is the gap that had to be repaired.

A saturated carrier with `D=0` contributes at least two units to `a`, because its saturated source is H-nonadjacent to the other two saturated rows. A saturated `D=2` carrier occupies a nonshared physical slot.

### `(a,c0)=(2,1)`

Exactly one saturated row can have a `D=0` carrier, and it exhausts `a`. The other two saturated rows therefore have zero local `a` contribution and their carriers must have `D=2` containing both other saturated indices. Those two `D=2` carriers are physically distinct: each misses the other saturated row. But `c0=1` leaves room for only one nonshared physical slot. Contradiction.

The allocations `(1,2)` and `(3,0)` fail by the same `D=0` / `D=2` resource accounting.

### `(a,c0)=(0,3)`

All three saturated rows have distinct `D=2` carriers. They exhaust the three nonshared slots and force `g=0`.

Each such carrier has H-degree exactly one. It cannot touch an unsaturated H-neighbour of its saturated source, because that would spoil both private-foot orientations of the corresponding H-edge; and every H-nonneighbour index belongs to its two-element D-set and is missed by the carrier.

Now a B1 vertex on an unsaturated row would block the remaining private-foot orientation of the edge from that row to a saturated row. Hence no B1 shared resource exists. The other possible shared resources are endpoint-indexed and H-anticomplete. Thus no shared H--U edge exists, contradicting

`S=t-4>0`

for `t>=5`.

So `N=3` is impossible for `t>=5`.

## N=2

Now `a+c0=2`.

### `(a,c0)=(0,2)`

Both saturated carriers must be distinct `D=2` carriers. They force `g=0` and exhaust the two nonshared slots. As above, each has H-degree one.

A B1 edge on a row adjacent to a saturated source destroys the only remaining private-foot orientation of that H-edge. A row nonadjacent to both saturated sources has missing H-degree at least two; with `a=0` it cannot support a B1 edge while also supplying the required reverse-private slots. Hence no B1/shared edge remains, contradicting `S=t-3`.

### `(a,c0)=(1,1)`

One saturated carrier is `D=0` and accounts for the unique unit of `a`; the other is `D=2`. The latter consumes the unique nonshared slot and again forces `g=0`. The `D=0` carrier is a bar-`d`, H-degree-one vertex whose only H--U edge is already used by the residual `R_j` mechanism, so the same physical vertex cannot also supply its B1 shared mechanism. Thus there is a second unusable shared resource although `c0=1`. Contradiction.

### `(a,c0)=(2,0)`

Both saturated carriers are `D=0`. Their unique H--U edges are already assigned to `R_j`, making both physical vertices unusable as shared B1 resources. But `c0=0` requires complete shared-resource saturation. Contradiction.

Therefore `N=2` is impossible.

## N=1

Here `a+c0=1`.

### `(a,c0)=(1,0)`

There is no nonshared slot, so the saturated carrier cannot be `D=2`; it is `D=0`. Its only H--U edge is the residual `R_j` edge and therefore cannot simultaneously be its B1 shared edge. This contradicts `c0=0` full shared-resource saturation.

### `(a,c0)=(0,1)`

The saturated carrier, whether `D=0` or `D=2`, consumes the unique nonshared allowance and forces `g=0`. Every other nonselected U-vertex must therefore be a used shared resource.

Endpoint-indexed resources are H-anticomplete. A reverse-U shared edge needs an H-positive U-head. Hence all `S=t-2` used shared resources must be B1.

A B1-touched row must be nonadjacent to the saturated source; otherwise the residual carrier and the B1 vertex spoil opposite private-foot orientations of that H-edge. Since `a=0`, the saturated source has at most two H-holes, so at most two rows are eligible. On either eligible row `a_i=0` and `m_i>=1`; two B1 neighbours would block every reverse-private slot although the row needs `r_i^q=m_i`. Hence each eligible row supports at most one B1 vertex.

Thus `S<=2`, contradicting `S=t-2` for `t>=5`.

So `N=1` is impossible for `t>=5`.

## Reconstructed conclusion

All four equality faces are impossible for `t>=5`. Therefore, **conditional on the corrected half-ray interface and the residual-slot-collapse lemmas**, the strict statement is independently recovered:

`Delta >= h+1 = 2t`,

hence

`L_H >= 5t-1`.

This closes the equality-face audit gate identified on 21 September. It does **not** close the more important upstream question of whether an actual D2C graph can realize the rigid complete-Hall-cut interface at all; that is treated separately in the boundary-code-edge realizability note from this session.
