# Residual-one k=2 half-ray: residual-column deficit barrier

Date: 2026-09-20

Status: **same-session conditional theorem**, downstream of the corrected B-layer H--U orientation-capacity theorem. This note does not use the invalidated U-source/private-foot chain. It starts from the corrected capacity decomposition and keeps the residual-column location of every shared resource explicit.

## 1. Setup and audit reconciliation

Work on the corrected intermediate half-ray

- `p=2t`, `c=y=t`,
- `u=t+1`, `h=|H|=p-1=2t-1`,
- `k=2`, `J2=empty`,
- residual coordinate `j`, residual opposite endpoint `q_j`,
- two selected witnesses `W_s subseteq U_bar(d)` with `d_H=0`.

The corrected H--U theorem partitions a chosen certificate for every H--U edge into

- `R_q`: reverse private matched certificates, capacity `2M_H`;
- `R_j`: reverse residual-`q_j` certificates, capacity `h`;
- `S`: triangle-free / reverse-U / U-sourced A_X / U-sourced Y mechanisms, capacity `u-2`.

Put

`a=2M_H-R_q`, `b=h-R_j`, `c0=(u-2)-S`,

and

`Delta=a+b+c0`.

Then

> **`L_H=(3t-1)+Delta`**                                 `(D0)`

and exactly

> **`e(H,U)=2M_H+h+u-2-Delta`.**                         `(D1)`

This is the corrected capacity-deficit decomposition; the previous private-foot coordinate-slice claims remain superseded.

## 2. Shared resources all lie in the residual-bar column

Let

`P=U_j^-={w in U:c(w)_j=bar(d)_j}`,

and put `g=|U\P|`.

Every physical U-resource counted by `S` is either

- a `bar d` H-degree-one vertex, or
- a vertex of an endpoint-indexed class `U_{bar d xor e_i}` with `i` private.

Every such code still has residual bit `bar(d)_j`. The two selected witnesses also lie in `P`, and the `S`-capacity proof uses distinct physical resources outside `W_s`. Therefore

`S <= |P|-2 = u-g-2`.

Since `S=u-2-c0`,

> **`g<=c0`.**                                           `(D2)`

Thus the shared-capacity deficit has a literal meaning: it upper-bounds the number of U-vertices outside the residual-bar column.

## 3. Residual-slot saturation bounds H--U degree

For each H-source counted by `R_j`, the singleton equation with `q_j` says that the H-row has exactly one neighbour in all of `P`:

`|N_U(h_i) cap P|=1`.

There are `h-b` such rows. Each has at most `g` further U-neighbours outside `P`, hence degree at most `g+1`. The remaining `b` rows have degree at most `u`. Consequently

> **`e(H,U) <= (h-b)(g+1)+bu`.**                         `(D3)`

Using `g<=c0` and `(D1)` gives the exact necessary inequality

> **`2M_H+u-2-Delta <= h c0 + b(u-c0-1)`.**              `(D4)`

This inequality is independent of how the private-hole, residual-slot and shared mechanisms are distributed internally.

On the half-ray `u-1=t<=h`, the right side is at most `h(b+c0)<=h Delta`. Therefore

> **`Delta(h+1) >= 2M_H+u-2`.**                          `(D5)`

Since `h+1=2t` and `u-2=t-1`,

> **`Delta >= ceil((2M_H+t-1)/(2t))`.**                  `(D6)`

In particular exact equality in the predecessor H-slack theorem (`Delta=0`) is impossible for every `t>=2`.

## 4. A second exact constraint: shared edges on residual-saturated rows

Fix one chosen certificate mechanism per H--U edge as in the decomposition. On a row counted by `R_j`, the unique H--U edge whose head lies in `P` is already assigned to the residual-`q_j` mechanism. Therefore any *different* edge assigned to `S` on that row must have its U-head outside `P`.

Hence a residual-saturated row supports at most `g` S-assigned edges, while an unsaturated row supports at most `u`. Thus

> **`S <= (h-b)g+bu`.**                                  `(D7)`

Using `S=u-2-c0` and `g<=c0`,

> **`u-2-c0 <= (h-b)c0+bu`.**                            `(D8)`

This rules out a pure private-capacity deficit: if `b=c0=0` and `u>2`, no positive `S=u-2` can be placed.

## 5. Complete hostile classification of Delta=1

Assume `t>=4` and `Delta=1`.

Because `a,b,c0` are nonnegative integers, there are only three nominal cases.

### 5.1 `a=1`, `b=c0=0` is impossible

By `(D8)`, `S=u-2>0` but the right side is zero. So this case is impossible.

### 5.2 `b=1`, `a=c0=0`

Here `S=u-2=t-1` and `(D2)` gives `g=0`, so every U-vertex lies in `P`. The `h-1` residual-saturated H-rows therefore have U-degree exactly one. All additional H--U edges must lie on the unique unsaturated row.

Since `a=0`, every directed H-hole must be represented by an `R_q` edge. If `M_H>0`, each H-hole has two directions, one from each endpoint; at most one endpoint can be the unique unsaturated row, so one of those directed `R_q` edges would have to live on a residual-saturated degree-one row already occupied by its `R_j` edge. Because the edge partition assigns only one mechanism per edge, this is impossible. Hence

> **`M_H=0`; H is complete.**                            `(D9)`

The unique unsaturated row must then carry all `S=t-1` H--U edges. But exact local degree bookkeeping on the half-ray is

`d_U(h_i)=m_i+3-epsilon_i`.

For this row `m_i=0` and `epsilon_i>=0`, so `d_U(h_i)<=3`. Therefore `t-1<=3`; in particular

> **this case is impossible for `t>=5`.**                 `(D10)`

### 5.3 `c0=1`, `a=b=0`

Now all H-rows are residual-saturated and `(D2)` gives `g<=1`. Since `S=u-3=t-2>0`, `(D7)` forces `g=1`. Write

`U\P={t_*}`.

Every S-assigned edge on a saturated row must therefore have head `t_*`. Each row has at most one such edge, so the `S=t-2` source rows are distinct.

Moreover the only S mechanism whose edge-head can lie outside `P` is the **reverse-U** mechanism: triangle-free endpoints and U-sourced A_X/Y sources themselves belong to the residual-bar resource classes. Hence all `t-2` S edges are reverse-U-certified edges

`h_i t_*`

with pairwise distinct endpoint-indexed witnesses

`w_i in U_{bar d xor e_i}`.

The sources `i` are distinct, so the witness codes are distinct. The count is exact:

- two selected witnesses `W_s`;
- `t-2` endpoint-indexed witnesses `w_i`;
- the single residual-plus vertex `t_*`.

These exhaust all `u=t+1` U-vertices.

As `a=0`, any H-hole would create an additional `R_q` edge. But every saturated H-row already has exactly one P-neighbour and at most the single outside neighbour `t_*`; the `S` source rows use both slots and the others use only their `R_j` slot. More directly, `(D3)` is tight with total row capacity `h+S`, while `(D1)` would add `2M_H` further edges. Hence

> **`M_H=0`; H is complete.**                            `(D11)`

Now inspect a reverse-U certificate

`N(h_i) cap N(w_i)={t_*}`.

The source and witness are nonadjacent. Since H is complete, every `h_l` with `l!=i` is adjacent to `h_i`; singleton criticality therefore forces `w_i` to miss every such `h_l`, and it also misses `h_i`. Thus

> **every endpoint-indexed witness `w_i` is H-anticomplete.** `(D12)`

The two selected witnesses `W_s` are H-anticomplete by construction. Hence every vertex of `P` is H-anticomplete. But residual-slot saturation requires every H-row to have exactly one neighbour in `P`. Contradiction.

Therefore this case is impossible for every `t>=4`.

## 6. Deficit-two barrier

Combining the three cases:

> **For every corrected half-ray parameter `t>=5`,**
>
> **`Delta>=2`, hence `L_H>=3t+1`.**                     `(D13)`

This is only a constant improvement over the linear H-slack floor and does not close the half-ray. Its value is structural: it proves that the three H--U capacity blocks cannot even come within one unit of simultaneous saturation asymptotically.

More importantly, the proof identifies the two cheapest one-defect hostile geometries and destroys both. The surviving `Delta>=2` configurations must contain at least two units among:

- unused private-hole certificate capacity;
- missing residual-`q_j` source slots;
- missing shared U-resource capacity.

The same argument also gives the quantitative lower bound `(D6)`: if H has `Omega(p^2)` missing edges, then `Delta=Omega(p)` automatically.

## 7. Next target

The next useful question is not another scalar score comparison. It is whether the above residual-column argument can be iterated for `Delta=d=o(p)`.

For small `d`, `(D2)` leaves only `d` residual-plus U-vertices, while all but `d` H-rows have exactly one residual-bar U-neighbour. Equation `(D7)` then forces the `Theta(p)` shared H--U load through a small set of residual-plus heads or a small set of residual-unsaturated H-rows. Each reverse-U edge in the former concentration consumes a distinct endpoint-indexed witness and a physical U--U edge. This creates a concrete concentration problem in which the global U-sparsity and repaired ordered-pair injection can be brought back in safely.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory. This note is conditional downstream mathematics.