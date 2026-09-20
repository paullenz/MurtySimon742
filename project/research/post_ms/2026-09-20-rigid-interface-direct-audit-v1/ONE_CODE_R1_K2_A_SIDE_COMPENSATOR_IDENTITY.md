# Residual-one k=2 A-side compensator identity

Date: 2026-09-20

Status: **same-session exact rooted bookkeeping**, on the exact low-k ray and downstream of the global H/Y polarization. No finite scan is used.

The new weighted source-collapse bound leaves the unused `2L_A` term as the principal gap. This note identifies exactly how `L_A` can remain small despite the compulsory A--U hole block: the H and/or Y layers must become internally dense.

## 1. Exact H-side identity

On the exact ray

`u=p+1`, `x=p+1`, `y=p-1`,

and the root degree is

`b=2p+u=3p+1`.

Take `h in H`. Its fixed neighbours include

- exactly p matched endpoints from its code;
- every Y-vertex, giving p-1 neighbours;
- no K-vertex, by the preserved K--H anticompleteness.

Write `d_U(h)` for its U-degree and `d_H(h)` for its internal H-degree. Then

`d(h)=2p-1+d_U(h)+d_H(h)`.

Since `d(h)=b-epsilon_h`,

`epsilon_h=p+2-d_U(h)-d_H(h)`.

Let `z_U(h)=u-d_U(h)=p+1-d_U(h)`. Then

> **`epsilon_h=z_U(h)+1-d_H(h)`.**                       `(AC-H)`

Summing over H gives

> **`L_H=Z_{H,U}+|H|-2e(H)`.**                           `(AC-HSUM)`

## 2. Exact Y-side identity

Take `y0 in Y`. Its fixed neighbours include

- p matched endpoints;
- all x=p+1 vertices of X.

Write `d_U(y0)` and `d_Y(y0)` for its U-degree and internal Y-degree. Then

`d(y0)=2p+1+d_U(y0)+d_Y(y0)`,

so

`epsilon_y=p-d_U(y0)-d_Y(y0)`.

With `z_U(y0)=p+1-d_U(y0)`,

> **`epsilon_y=z_U(y0)-1-d_Y(y0)`.**                     `(AC-Y)`

Summing gives

> **`L_Y=Z_{Y,U}-|Y|-2e(Y)`.**                           `(AC-YSUM)`

Because `|H|=|Y|=p-1`, the constants cancel:

> **`L_H+L_Y=Z_{H,U}+Z_{Y,U}-2e(H)-2e(Y)`.**            `(AC-MAIN)`

## 3. Insert the global escape polarization

The global H/Y theorem gives

`Z_{H,E}+Z_{Y,E}>=(p-1)(p-2)`.

The two selected witnesses W_s can change the total H/Y--U hole count by only O(p). Therefore

`Z_{H,U}+Z_{Y,U} >= (1-o(1))p^2`.

Substitute into `(AC-MAIN)`:

> **`L_H+L_Y >= p^2-2[e(H)+e(Y)]-o(p^2)`.**             `(AC-COMP)`

Hence any sequence with `L_A=o(p^2)` must satisfy

> **`e(H)+e(Y) >= (1/2-o(1))p^2`.**                     `(AC-DENSE)`

So the A-side slack gap has a precise structural meaning: low A-slack forces a half-quadratic internal-edge compensator in H and Y.

## 4. Y-compensation itself needs `bar d` witnesses

All Y-vertices have the same code d. By the raw same-code theorem, every Y--Y edge uses a complementary witness of code `bar d`. Since `A_{bar d}=empty`, the witness lies in U_{bar d}.

A B_0 witness is impossible because B_0 is Y-anticomplete. Up to the two selected W_s vertices, usable Y--Y witnesses therefore lie in

`B_+=U_{bar d}\B_0`,

the H-positive `bar d` class.

Ordered `(source,witness)` injection yields

> **`e(Y) <= |Y||B_+|+O(p)`.**                           `(AC-YCAP)`

Thus a dense Y-compensator requires a linear H-positive `bar d` witness class. Those vertices have zero U--U source capacity and, by global polarization, at most one Y-neighbour.

This exposes a three-way tension:

- B_0 supplies the only linear U-edge source capacity but is H/Y-anticomplete;
- B_+ can witness Y--Y compensation but cannot source U--U edges and is Y-sparse;
- if neither bar-d class is large enough, `(AC-DENSE)` forces the compensation almost entirely into H.

## 5. Live endpoint

The next literal geometry is therefore not an undifferentiated low-A-slack graph. A near-minimizer must choose between

1. **Y-compensated:** linear B_+ and dense Y;
2. **H-compensated:** H close to the density needed to supply roughly half of p^2 internal A-edges;
3. a mixture of the two, while still satisfying the source-collapse optimum in B_0.

The H-compensated arm is especially concrete. H--H edges can use private matched endpoints as witnesses, so it cannot be discarded by same-code capacity. The next raw-criticality audit should keep those private witness identities explicitly and ask whether a dense H graph is compatible with the U support patterns required by the B_0/B_+ source split.

## 6. Trust boundary

No closure is claimed. The identity is exact inside the conditional residual-one `J2=empty` branch. The upstream rigid-cut realizability gap and mandatory `X_3` negative control remain unchanged.