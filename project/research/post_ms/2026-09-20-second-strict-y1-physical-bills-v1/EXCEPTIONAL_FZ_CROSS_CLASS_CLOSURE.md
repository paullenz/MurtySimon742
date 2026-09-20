# Exceptional Fz — cross-class U_o edges are impossible

Date: 2026-09-20

Status: **same-session internal structural strengthening**. This supersedes the permissive `alpha*beta` internal-U_o edge allowance in Section 4 of `SECOND_STRICT_Y1_PHYSICAL_BILLS.md`. The earlier two-class bookkeeping remains historically useful for identifying the issue, but cross-class edges are now ruled out structurally.

Assume the large-head exceptional-Fz geometry from `SECOND_STRICT_Y1_HOSTILE_EXTENSION.md`:

- `Y={y}`;
- `S_0={j}` and the radius-one code is `C`;
- there is one higher-radius head `h` with code `H`, `S_H={j} union T`, `T nonempty`;
- `z_0` has code `D=bar C`, is adjacent exactly to `y` and `h` in A, and is anticomplete to U;
- every ordinary outside vertex is itself a Type-R buffer certificate;
- ordinary outside vertices therefore have one of exactly two codes:
  - `D=bar C`, when they certify a C-head;
  - `E=bar H`, when they certify h.

Both physical classes are nonempty.

## Theorem — no D--E outside edge

Let `w_D` be an ordinary D-coded outside vertex and `w_E` an ordinary E-coded outside vertex. Then

> `w_D w_E notin E`.

### Proof

Assume `w_Dw_E in E`. Since both endpoints lie in U, the root is a common neighbour, so in the raw singleton certificate for this U-U edge the witness cannot lie in U. It must lie in A.

### Orientation `w_D -> w_E`

A witness `a in A` must be nonadjacent to `w_D`, adjacent to `w_E`, and satisfy

`N(w_D) cap N(a)={w_E}`.

Any agreement between `c(a)` and `c(w_D)=D` would create a common tight matched endpoint distinct from `w_E`. Therefore necessarily

`c(a)=bar D=C`.

The only C-coded A-vertices are `a_0` and the radius-one C-heads.

- `a_0` is adjacent to every ordinary Type-R outside witness, in particular to `w_D`, so it cannot be the required non-neighbour witness.
- Every C-coded buffer head `x` is adjacent to `b`; `w_D` is also adjacent to `b`. Thus `b` is an extra common neighbour of `w_D` and x, so no such x can be a singleton witness.

Hence this orientation is impossible.

### Orientation `w_E -> w_D`

Now a witness `a in A` must have code

`c(a)=bar E=H`

for the same tight-coordinate reason. By the y=1 classification there is exactly one H-coded A-vertex, namely h.

But every E-coded ordinary outside vertex certifies the buffer edge `bh`, so

`N(w_E) cap N(h)={b}`.

If h were the witness for the assumed edge `w_Ew_D`, it would have to be adjacent to `w_D`; then `w_D` would be a second common neighbour of `w_E` and h in addition to b, contradicting this already-fixed singleton relation.

Thus the reverse orientation is impossible as well. Contradiction. `square`

## Corollary — the whole exceptional-Fz outside layer is independent

Within each of the D and E classes, same-code U-U edges were already excluded by the audited same-code theorem. The theorem above eliminates all cross-class edges. The hostile extension also gives `z_0--U_o^*=emptyset`.

Therefore

> **`G[U_o]=emptyset` in exceptional Fz.**                `(FZ1-UO0)`

This removes the only reason to retain `alpha,beta` in the rooted U-edge ceiling.

Consequently

> `q <= (k+1)(omega-1)`,                                  `(FZ1-Q+)`

because z_0 has no U-neighbours at all and every U_o^* edge is absent.

Every ordinary outside vertex has A-degree at most `x-1` and all `omega-1` other U_o vertices are U-nonneighbours. Hence

> `E(U_o^*) >= (omega-1)[p-x+omega]_+`.                  `(FZ1-UOPAY+)`

Together with the previous exact physical isolation

`epsilon_{z_0}>=p+k+omega-2`

and rooted-slot floor

`r>=x+2`,

the exceptional-Fz scalar tail is now no more permissive on internal U_o edges than the other y=1 cases.

## Diagnostic impact

Replaying the same abstract box used by `check_y1_physical_bills.py`

- `2<=p<=20`;
- `5<=x<=30`;
- `3<=omega<=24`;
- `1<=g<x`;

with `(FZ1-Q+)` and `(FZ1-UOPAY+)` reduces exceptional-Fz necessary-condition survivors from the superseded **12,109** two-class-cross-edge rows to **2,276** rows.

This remains an abstract parameter diagnostic, not a graph count and not a proof of closure. Its value is structural: the previous dominant freedom `alpha beta` was not real.

## Next target

The remaining exceptional-Fz rows no longer have an outside cross-class adjacency mechanism. The next proof step should combine

- `G[X]=emptyset`;
- `G[U_o]=emptyset`;
- `N_U(z_0)=emptyset`;
- `epsilon_{z_0}>=p+k+omega-2`;
- `r>=x+2`;

with the exact common-core head image and pair-local score ledger. In particular, determine whether the surviving abstract rows force very small `k` or a fixed asymptotic relation among `p,x,omega`; characterize that relation analytically rather than enlarging the finite box.