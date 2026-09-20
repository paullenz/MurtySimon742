# Residual-one k=2: exact H--U capacity-deficit decomposition

Date: 2026-09-20

Status: **same-session conditional corollary** of the corrected general H--U orientation-capacity theorem. It records the equality geometry explicitly, because future work should attack saturation rather than repeatedly relax the same inequality.

## 1. Choose one valid certificate mechanism per H--U edge

Work in residual dimension one, `k=2`, `J2=empty`, `p>=4`, `y>0`.

For every H--U edge choose exactly one of the valid mechanisms from the corrected classification. Let

- `R_q` = number assigned to reverse private-coordinate matched witnesses `q_l`, `l!=i`;
- `R_j` = number assigned to the residual matched witness `q_j`;
- `S` = number assigned to the shared U reservoir, namely triangle-free edges, reverse-U certificates, U-sourced A_X certificates, or U-sourced Y certificates.

Then this is a partition of the H--U edge set:

> `e(H,U)=R_q+R_j+S`.                                    `(CD-0)`

The proven capacities are

> `R_q<=2M_H`, `R_j<=h`, `S<=u-2`.                       `(CD-CAP)`

Define the nonnegative unused-capacity variables

`a=2M_H-R_q`, `b=h-R_j`, `c=(u-2)-S`.

## 2. Exact identity

The exact H-degree identity is

`e(H,U)=2M_H+h(u-y+2)-L_H`.

Subtracting this from the total capacity `2M_H+h+u-2` gives

> **`L_H-[h(u-y+1)-u+2]=a+b+c`.**                        `(CD-ID)`

Thus the general H-slack theorem is not merely an inequality: its entire gap is exactly the sum of three physically interpretable unused-capacity deficits.

## 3. Near-equality consequences

Put

`Delta_H=L_H-[h(u-y+1)-u+2]>=0`.

Then `(CD-ID)` gives simultaneously

> `R_q >= 2M_H-Delta_H`,
>
> `R_j >= h-Delta_H`,
>
> `S >= u-2-Delta_H`.                                    `(CD-SAT)`

Hence if `Delta_H=o(p)` along an unbounded bounded-ratio sequence, all three resources are asymptotically saturated:

1. almost every directed H-hole carries a reverse private-coordinate certificate;
2. almost every H-source uses its residual `q_j` certificate slot;
3. almost every U-vertex outside the two selected witnesses is consumed by exactly one of the shared endpoint-indexed / H-degree-one roles.

This is far more rigid than the scalar statement `L_H>=...`.

## 4. Residual-column consequence

Whenever source `h_i` uses its `q_j` reverse slot, there is a unique U-head `t_i` with

`N(h_i) cap N(q_j)={t_i}`.

Every U-vertex whose residual bit equals `bar d_j` is adjacent to q_j. Therefore

> **`|N_U(h_i) cap U_j^-|=1`**                            `(CD-JCOL)`

for every q_j-saturated H-source, where

`U_j^-={w in U:c(w)_j=bar d_j}`.

Consequently, if `B` is the set of H-sources without a q_j certificate,

> `e(H\B,U_j^-) = |H\B|`, and `|B|<=Delta_H`.            `(CD-JCOL2)`

Thus near-minimal H-slack forces a near-regular residual-column pattern: almost every H-row contains exactly one neighbour from the entire residual-bar U sector.

All `bar d` vertices and all endpoint-indexed classes `U_{bar d xor e_l}` lie inside `U_j^-`. In particular the same U population that carries the shared exceptional roles is visible in this residual-column constraint.

## 5. Directed private-column consequence

If a reverse private-coordinate certificate from source h_i uses q_l, `l!=i`, then

`N(h_i) cap N(q_l)={t}`.

Every U-vertex with bit `bar d_l` sees q_l. Hence the corresponding H-row contains exactly one U-neighbour in that private bar-column:

> **`|N_U(h_i) cap U_l^-|=1`.**                           `(CD-PCOL)`

Near saturation `R_q>=2M_H-Delta_H` therefore says that all but at most `Delta_H` directed H-holes impose an exact one-neighbour column equation.

The next attack should treat `(CD-JCOL)` and `(CD-PCOL)` as a binary incidence matrix problem constrained by the exact row degrees

`d_U(h_i)=u-y+2+m_i-epsilon_i`.

## 6. Why this is the right next level

The corrected half-ray is not closed by the linear H-slack floor itself. Any improvement must show that the three capacity blocks cannot be simultaneously saturated. `(CD-ID)` identifies exactly what such a proof must break.

A promising route is to prove that the same U-code distribution cannot provide

- one residual-bar neighbour in almost every H-row,
- one private-bar neighbour for almost every directed missing H-pair,
- and the endpoint-indexed/H-degree-one shared roles,

while also satisfying the H-row degree identities and the already-established U/Y defect constraints.

No claim of graph-level rigid-interface reachability is made; the `X_3` negative control remains mandatory.