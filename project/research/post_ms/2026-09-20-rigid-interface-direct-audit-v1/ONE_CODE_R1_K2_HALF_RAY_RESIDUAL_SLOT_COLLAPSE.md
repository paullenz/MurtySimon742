# Residual-one k=2 half-ray: endpoint collapse and residual-slot deficit theorem

Date: 2026-09-20

Status: **same-session conditional structural theorem, pending the dedicated hostile replay recorded in the session handoff.** It is downstream only of the corrected B-layer H--U capacity theorem, the raw residual-bar private-spoke classification, and the exact H--H private-foot/U-witness dichotomy. It does **not** use the superseded H--U private-foot coordinate-slice argument. The unresolved rigid complete-Hall-cut interface and mandatory X_3 negative control remain unchanged.

## 1. Setup

Work on the corrected intermediate half-ray

`p=2t, c=y=t, u=t+1, h=|H|=2t-1`,

with `k=2`, `J2=empty`, residual coordinate `j`, and residual-bar column

`P=U_j^-`.

Choose one H--U certificate mechanism per H--U edge as in the corrected capacity decomposition. Write

- `R_q` for reverse private-coordinate matched certificates;
- `R_j` for reverse residual-q_j certificates;
- `S` for the shared U-resource block;
- `a=2M_H-R_q`;
- `b=h-R_j`;
- `c0=(u-2)-S`;
- `Delta=a+b+c0`.

Then

`L_H=3t-1+Delta`.

Let `N=R_j=h-b` be the number of residual-q_j-saturated H-sources. Every such source `h_i` has a unique P-neighbour `z_i`.

## 2. Endpoint-indexed U vertices are H-anticomplete

For `z in P`, let

`D(z)={i private : z p_i in E}`,

where `p_i` is the private matched endpoint selected by d.

The raw private-spoke classification already proved:

> if `d_H(z)>0`, then `D(z)` is either empty or has size exactly two.

Indeed, if `i in D(z)`, raw criticality of the B-edge `z p_i` forces a private-head witness `h_l`, `l!=i`; fibre comparison gives `D(z)={i,l}`, and the symmetric spoke forces z to miss both `h_i,h_l`.

But every endpoint-indexed code

`U_{bar d xor e_i}`

lies in P and has `D={i}`. Therefore

> **every endpoint-indexed U vertex is H-anticomplete.**      `(EC-1)`

This removes two corrected H--U shared roles immediately: an endpoint-indexed vertex cannot be a triangle-free H--U endpoint and cannot be a U-sourced A_X H--U endpoint.

## 3. There are no U-certified H--H edges

The exact H--H dichotomy says that a U-witness for an H--H edge sourced at `h_i` must lie in the endpoint-indexed class

`U_{bar d xor e_i}`

and must be adjacent to the singleton H-head. By `(EC-1)` this is impossible.

Hence:

> **every H--H edge is certified by one of its two private matched feet.** `(EC-2)`

This is an H--H statement. It is not the superseded H--U private-foot claim.

## 4. Residual-q_j-saturated H-sources form an independent set

Take two residual-saturated rows `h_i,h_l` and suppose `h_i h_l` is an edge.

By `(EC-2)`, one valid orientation must use a private foot. Suppose the source is `h_i` and the witness is `q_l`. Since `z_i` is adjacent to `h_i`, singleton criticality requires `z_i q_l` to be absent. Thus `l in D(z_i)`.

Write `D(z_i)={l,r}`. The raw private-spoke proof applied to the edge `z_i p_r` uses `h_l` as its A-witness and requires

`N(z_i) cap N(h_l)={p_r}`.

But `h_i` is adjacent to z_i, and the assumed H-edge makes `h_i` adjacent to `h_l`. Thus `h_i` is an illicit second common neighbour. Contradiction.

The reverse private-foot orientation is symmetric. Therefore

> **the N residual-q_j-saturated H-rows are pairwise nonadjacent.** `(EC-3)`

## 5. Reverse-private capacity of one saturated row

Fix a saturated source `h_i` with carrier `z_i`.

If a missing H-coordinate `l` is not in `D(z_i)`, then `z_i` sees `q_l`. Consequently any singleton equation for the physical pair `(h_i,q_l)` has z_i in its common-neighbour set. The only possible U-head would therefore be z_i itself. But the edge `h_i z_i` is already the unique edge assigned to the residual-q_j mechanism. The one-edge/one-chosen-mechanism partition means it cannot also contribute to `R_q`.

Thus reverse-private assignments from `h_i` can use only missing coordinates in `D(z_i)`. Hence

> `r_i^q <= |D(z_i)| <= 2`.                               `(EC-4)`

If `D(z_i)=empty`, then `r_i^q=0`.

Since `a_i=m_i-r_i^q`, the independent saturated set already gives

`a_i >= (N-1)-|D(z_i)|`.

## 6. Physical D=2 carriers and the quadratic deficit bill

Let R be the number of saturated rows whose carrier has `|D|=2`.

From `(EC-3)` and `(EC-4)`,

> `a >= N(N-1)-2R`.                                      `(EC-5)`

A physical D=2 carrier cannot be a shared H--U resource:

- endpoint-indexed shared resources have |D|=1 and are H-free by `(EC-1)`;
- H-positive shared bar-d resources have H-degree exactly one and `D=empty`.

The shared capacity leaves exactly `c0-g` unused physical slots in `P\W_s`, where `g=|U\P|`. Therefore the number of physical D=2 carriers is at most `c0-g<=c0`.

If one such carrier serves a cluster of c saturated rows, those c rows are all H-neighbours of the carrier while its two D-coordinates lie outside the cluster. Every ordered H-hole inside that cluster is therefore unavailable to `R_q`, contributing at least

`c(c-1)`

to a. Summing over D=2 carrier clusters shows

`R <= c0+a/2`.                                            `(EC-6)`

Combining `(EC-5)` and `(EC-6)` gives

`a >= N(N-1)-2c0-a`,

hence the compact exact theorem

> **`a+c0 >= binom(N,2)`.**                               `(EC-7)`

Because `b=h-N`,

> **`Delta >= h-N+binom(N,2)`.**                          `(EC-8)`

The right side is minimized at N=1 or N=2 and equals `h-1=2t-2`. Thus `(EC-8)` alone gives `Delta>=2t-2`.

## 7. The N=2 equality face cannot occur

Suppose `Delta=2t-2` and N=2. Then `a+c0=1`.

If `(a,c0)=(1,0)`, there is no physical D=2 carrier slot. Both saturated rows have D=0 carriers, so their mutual H-hole contributes one unit to a from each source. Thus `a>=2`, contradiction.

If `(a,c0)=(0,1)`, each source needs its mutual H-hole assigned through a D=2 carrier containing the other row in D. One physical carrier cannot serve both rows, because its D-set is disjoint from its H-neighbour cluster. Two D=2 physical carriers are required but only one non-shared slot exists. Contradiction.

Hence equality can only have N=1.

## 8. The N=1 equality face also collapses

Assume `Delta=2t-2`, N=1. Then necessarily

`a=c0=0`, `b=h-1`, `g=0`.

Let `h_*` be the unique residual-q_j-saturated row. Since `P=U`, it has exactly one U-neighbour z. Exact row accounting gives `m_*=0`, so `h_*` is H-universal.

Because `c0=0`, the shared U reservoir is physically saturated:

`S=u-2=t-1`.

By `(EC-1)`, the only H-positive shared resources are `bar d` vertices of H-degree exactly one (`B1`). Therefore z is such a B1 vertex.

For every `i!=*`, the H-edge `h_i h_*` cannot use the private-foot orientation sourced at `h_*` through `q_i`: z has code `bar d`, so z sees every q_i and is an extra common neighbour. By `(EC-2)`, the edge is forced into the reverse orientation sourced at `h_i` through `q_*`:

`N(h_i) cap N(q_*)={h_*}`.                                `(EC-9)`

Any B1 vertex adjacent to `h_i` would also see q_* and violate `(EC-9)`. Thus no B1 vertex can be adjacent to any unsaturated H-row. Since `h_*` has only the single U-neighbour z, there is exactly one B1 shared resource.

Physical saturation of the shared reservoir now forces every other shared resource to be an endpoint-indexed reverse-U witness. These vertices are H-free by `(EC-1)`. A reverse-U H--U edge needs an H-positive U-head. The only H-positive U vertex is z, but z is adjacent only to h_* and that unique edge is already assigned to the residual-q_j mechanism. Hence there is no reverse-U edge at all.

So `S<=1`, contradicting `S=t-1` for `t>=3`.

Therefore:

> **THEOREM. On the corrected half-ray, for every `t>=3`,**
>
> **`Delta >= h = 2t-1`.**                                `(EC-10)`

Equivalently,

> **`L_H >= 5t-2`.**                                      `(EC-11)`

## 9. Stability above the new barrier

Write

`Delta=h+s`, `s>=0`.

Since `N=h-b`, the exact deficit identity gives

`a+c0=s+N`.

Combining with `(EC-7)`,

`s+N >= binom(N,2)`,

or

`N^2-3N-2s<=0`.

Thus

> **`N <= floor((3+sqrt(9+8s))/2)`.**                     `(EC-12)`

So a configuration within s units of the new H-slack barrier has only `O(sqrt(s)+1)` residual-q_j-saturated H-sources. In particular at exact equality `Delta=h`, at most three H-sources can use the residual q_j slot.

This is the new literal frontier: near-minimal corrected H-slack forces almost complete loss of the residual-q_j certificate layer, rather than the near-saturation geometry investigated earlier in the session.

## 10. Next attack

First hostile-replay `(EC-1)--(EC-12)` independently, especially the use of the one-chosen-mechanism partition in `(EC-4)` and the physical unused-slot count in `(EC-6)`. If that passes, stop iterating the obsolete small-Delta carrier argument. The next raw-criticality target is the tiny residual-saturated core under `Delta=h+s`: at equality it has N<=3, while the shared reservoir still contains `t-O(1)` physical roles. Classify the N=0,1,2,3 equality geometries and force the large shared H--U load through the remaining unsaturated H rows and the few non-shared U-heads.

No graph-level realizability claim is made. Bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; X_3 remains mandatory.
