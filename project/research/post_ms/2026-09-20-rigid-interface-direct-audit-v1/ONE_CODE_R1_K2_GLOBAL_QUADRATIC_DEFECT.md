# Residual-one k=2 global quadratic physical defect

Date: 2026-09-20

Status: **same-session candidate synthesis theorem**, conditional on the preceding k=2 residual-one packages. It does not close the ray by itself; it proves that the former linear-cost scaling picture is physically impossible. No finite scan is used.

## 1. Common physical defect functional

On the preserved low-k ray

`c=p=lambda`, `y=p-1`, `u=x=p+1`, `k=2`,

write

`E=U\W_s`, so `|E|=p-1`.

Define the nonnegative physical defect functional

> `D_phys = E_U + Z_X + Z_Y + M_U`,                       `(GD-D)`

where

- `E_U=sum_{z in U} epsilon_z` is total U-slack;
- `Z_X` is the number of missing X--U pairs;
- `Z_Y` is the number of missing Y--U pairs;
- `M_U=binom(u,2)-e(U)` is the number of missing U--U pairs.

The point is not that these four terms are interchangeable in the final proof. They are kept separate in the exact rooted ledger. `D_phys` is used here only as a safe common container in which every physical bill from the preceding structural analysis lives.

## 2. One remaining cheap-looking class also has a linear-per-vertex hole bill

The previous endpoint partition explicitly priced K-heavy, W-heavy, mixed, and K-free/W-free vertices. There is one additional one-sided type that must not be omitted:

> a vertex t with `N(t) cap W_s=empty` and exactly one K-neighbour.

More generally let t be W_s-free and put

`d_K(t)=|N(t) cap K|<=1`.

Its neighbours in `A union U` can occur only in

`N_K(t) union H union Y union (E\{t})`.

The last three sectors have total size `3p-4`, while

`d_{A union U}(t)=2p-epsilon_t`.

Therefore, if

`alpha_t=|H\N(t)|`, `beta_t=|Y\N(t)|`, `gamma_t=|(E\{t})\N(t)|`,

then

> **`alpha_t+beta_t+gamma_t=p-4+epsilon_t+d_K(t)`.**      `(GD-DEF)`

Since `epsilon_t>=2`, every W_s-free non-K-heavy escape has at least `p-2` missing incidences across H, Y and E.

As in the F0 sector note, summing and converting U--U incidences to distinct pairs loses at most a factor two. Thus if D is any set of d W_s-free non-K-heavy escapes,

> **`Z_H(D)+Z_Y(D)+M_U(D) >= d(p-2)/2`.**                `(GD-DSECT)`

Here `M_U(D)` counts distinct missing U--U pairs incident with D and another vertex of E. All three terms lie inside `D_phys`.

## 3. Five-way partition of the escape reservoir

Every escape vertex lies in one of the following five classes.

1. **R: K-heavy** — complete to K and anticomplete to W_s.
2. **D: W_s-free but not K-heavy** — zero or one K-neighbour.
3. **F1: K-free with exactly one W_s-neighbour.**
4. **S: W-heavy** — complete to W_s and anticomplete to K.
5. **M: mixed** — has at least one K-neighbour and at least one W_s-neighbour.

These classes cover E and are disjoint. Write their sizes as `r,d,f1,s,m`, so

`r+d+f1+s+m=p-1`.                                        `(GD-PART)`

The predecessor and same-session theorems give the following safe bills.

### R: K-heavy

Exception-orientation conservation gives

> `D_phys >= r(r-1)/3`.                                  `(GD-R)`

This already allows arbitrary K-free exceptional witnesses; it is not a heavy-only statement.

### D: W_s-free, not K-heavy

By `(GD-DSECT)`,

> `D_phys >= d(p-2)/2`.                                  `(GD-DCLASS)`

### F1: one selected-witness neighbour, no K-neighbour

The forced heavy-endpoint orientation makes every such vertex Y-anticomplete, so

> `D_phys >= f1*y=f1(p-1)`.                              `(GD-F1)`

(There is also a missing block to the K-heavy class, but it is not needed here.)

### S: W-heavy

Every W-heavy escape is Y-anticomplete, hence

> `D_phys >= s*y=s(p-1)`.                                `(GD-S)`

The stronger W-heavy internal-edge slack theorem is again not needed for this coarse synthesis.

### M: mixed

The k=2 mixing theorem gives `epsilon_w>=p+1` for every mixed escape, so

> `D_phys >= m(p+1)`.                                    `(GD-M)`

## 4. Quadratic defect is unavoidable

Let

`q=floor((p-1)/5)`.

By `(GD-PART)`, one of the five classes has size at least q.

If that class is R, `(GD-R)` gives

`D_phys>=q(q-1)/3`.

For every other class, its displayed lower bound is at least `q(q-1)/3` for the relevant range `p>=4` (indeed those bounds are linear in p per vertex and much larger asymptotically).

Therefore:

> **Global low-k quadratic-defect theorem.**
>
> **`D_phys >= q(q-1)/3`, where `q=floor((p-1)/5)`.**    `(GD-MAIN)`

In particular

> **`D_phys = Omega(p^2)`.**                              `(GD-ASYM)`

This is the main conceptual change. The exact parameter ray survived all earlier aggregate scalar gates because those gates permitted only linear physical cost in the escape reservoir. After the heavy-reservoir exception audit and the sector-deficit decomposition, **no realization of the ray can remain linear-cost**. Every possible escape partition forces a quadratic amount of actual U-slack or located X--U / Y--U / U--U defect.

## 5. Why this is not yet a closure

`D_phys` is a deliberately coarse container. The final rooted identities weight its components differently:

- `Z_X` feeds the X-side exact degree identity and `L_X`;
- `Z_Y` feeds the Y-side/rooted residual balance;
- `M_U` lowers `q=e(U)` directly;
- `E_U` is literal degree slack.

Thus `(GD-MAIN)` cannot simply be compared to the old scalar ceiling `C0` without re-deriving the exact coefficients and avoiding overlap with predecessor Hamming / selected-witness bills.

The next highest-value step is therefore precise: substitute the five-class partition into the exact rooted residual identity, keep `E_U,Z_X,Z_Y,M_U` separate, and minimize the resulting weighted quadratic form. If that minimum exceeds the available residual budget for large p, the low-k ray becomes finite-order. If it does not, the minimizing class mixture identifies the next literal geometry for raw criticality.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; this is conditional downstream mathematics pending independent hostile replay.