# Maximal m=2 complementary F/R normal form: physical reservoir pricing

Date: 2026-09-20

Status: internal structural continuation of `MAXIMAL_SELECTION_MATCHING_AND_M1_CLOSURE.md`. Assumptions are the audited first-strict unique-hole setup, maximal raw eligibility matching number `m=2`, `p>=3`, `x>=4`, and therefore the complementary F/R normal form proved in the companion note.

## 1. The `omega>2` geometry is a literal two-star code swap

Let `omega=|U_o|>2`. The two X'-code classes are F and R, with

- `S_0={s}`;
- `I_F=S_0`;
- `I_R=I_0=[p]\S_0`;
- the F and R codes complementary.

Because the R component has matching number one and Type-R fixed-foot uniqueness, it has one physical outside witness `z_R`. Since `omega>2`, the F component has at least two physical complementary-code witnesses; a matching-one component with multiple right vertices has exactly one left vertex. Hence the F class consists of one head, call it `f`, while the R class consists of the remaining `x-2` heads.

Write

`Z_F=U_o\{z_R}`, `L=|Z_F|=omega-1`.

The codes swap:

- `a_0` and every R-head have the radius-one R-code `C_R`;
- `f` has `C_F=bar C_R`;
- `z_R` has code `C_F`;
- every vertex of `Z_F` has code `C_R`.

Raw eligibility gives:

- `z_R` is nonadjacent to every R-head and adjacent to `a_0`;
- every `z in Z_F` is nonadjacent to `f` and to `a_0`;
- every outside vertex is anticomplete to `Y`.

No selected-incidence multiplicity is being substituted for a physical statement here.

## 2. The F-star reservoir is independent in U

### Theorem 2.1

> `G[Z_F]` is edgeless.                                  `(ZF-INDEP)`

### Proof

Suppose `zz'` is an edge with `z,z' in Z_F`. Both are U-vertices of the same code `C_R`. By the independently re-derived full same-code raw-criticality theorem, a U-source on this edge must use an A-witness of complementary code `C_F`.

In the present normal form the only A-vertex of code `C_F` is the unique F-head `f`: `a_0` and the R-heads have code `C_R`, while `Y` has code `d` (and `p>=3` keeps these codes distinct).

But every F-star witness is eligible for the buffer edge `bf`, so in particular `fz` and `fz'` are both nonedges. Thus `f` cannot be adjacent to the head of either orientation of `zz'`, contradicting the required singleton certificate.

Hence no such edge exists. `square`

This is a physical U-U obstruction, not a selected-witness count.

## 3. Quadratic outside-reservoir slack bill

Each `z in Z_F` has the following located nonneighbours in `A union U`:

- all `y` vertices of `Y`;
- the F-head `f`;
- `a_0`;
- the other `L-1` vertices of `Z_F` by `(ZF-INDEP)`.

These are `y+L+1=y+omega` distinct physical nonneighbours. For a U-vertex the rooted slack identity is

`epsilon_z=p+u-1-d_{A union U}(z)`.

Equivalently, if `H_z` is its number of nonneighbours in `A union U`, then

`epsilon_z=H_z+p-(x+y)`.

Therefore

> `epsilon_z >= [p-x+omega]_+` for every `z in Z_F`,

and hence

> `E_{Z_F} >= (omega-1)[p-x+omega]_+`.                 `(ZF-SCORE)`

Together with the reverse-fan exact Y-price

`L_Y=y(p-g+1+omega)`,

we get the unconditional total-score necessary condition

> `y(p-g+1+omega)+(omega-1)[p-x+omega]_+ <= C0`,        `(OMEGA-SCORE)`

before charging the common core, buffer, R-witness, X-side or any other positive slack. Thus the physical F-star reservoir is quadratically self-pricing once `omega>x-p`.

Pair-locally, the Y term remains in the audited `{d,bar d}` pair and must be inserted into the exact `S_P/Ccap_P` ledger; the `Z_F` term is an outside-pair bill and must not be substituted into `S_P`.

## 4. Direct rooted-triangle surcharge

The independent set `Z_F` contributes

`binom(omega-1,2)`

forced missing U-U pairs. These pairs are disjoint from the already-known missing pairs inside the independent common-core/buffer set `U_-=W_0 dotcup {b}`. Consequently the rooted U-edge count satisfies the safe physical ceiling

> `q <= binom(u,2)-binom(k+1,2)-binom(omega-1,2)`,       `(Q-ZF)`

before subtracting any additional core-separation or certificate-forced U-holes already present in the stronger local ledgers.

Thus every extra F-star leaf is priced twice: in slack by `(ZF-SCORE)` and in rooted triangle capacity by `(Q-ZF)`.

## 5. The bulk R-code graph is a star forest controlled by f

Let `R_X` be the `x-2` R-heads. Every vertex of `R_X` has code `C_R`, and every pair is nonadjacent to `a_0` by Type R.

Consider a same-code edge inside `G[R_X]`. The complementary-code vertices in `A union U` relevant to the same-code theorem are the F-head `f` and the R-witness `z_R` (plus no Y/a0/R vertices of that code). The witness `z_R` is nonadjacent to every R-head because it certifies all of their buffer edges, so it cannot be adjacent to the head of a same-code R-edge. Therefore every R-R edge must use `f` as its raw complementary-code witness.

Let

`R_1=N(f) cap R_X`, `R_0=R_X\R_1`.

For an R-R edge certified by `f`, the source must lie in `R_0` and the head in `R_1`. Moreover a fixed source `r in R_0` has one graph-fixed common-neighbour set with `f`; it can therefore have at most one R-neighbour in `R_1`.

Hence

> `G[R_X]` is a star forest with centres in `R_1` and leaves in `R_0`,

and in particular

> `e(R_X) <= |R_0|=(x-2)-|R_1|`.                       `(R-STAR)`

Equivalently

> `d_{R_X}(f)+e(R_X) <= x-2`.                           `(F-R-TRADE)`

This converts the same-code witness theorem into a physical internal-X density tradeoff.

## 6. Consequence for the whole X-side

There are no `a_0--R_X` edges by Type R. Therefore the only possible internal X-edges are

- possibly `a_0f`;
- edges from `f` to `R_X`;
- the star-forest edges inside `R_X`.

Using `(F-R-TRADE)`,

> `e(X) <= 1+(x-2)=x-1`.                                `(X-M2-FR)`

The value is attained only if the entire allowance is spent through the F-controlled star geometry; increasing `f`'s R-degree reduces the permitted R-R edge count one-for-one.

This is suitable for direct substitution into the exact Hall-density identity and the rooted unused-slot ledger.

## 7. Next attack

The most valuable next step is to combine the three now-independent physical bills in the `omega>2` normal form:

1. exact pair-local source bill `L_Y=y(p-g+1+omega)`;
2. outside-pair quadratic reservoir bill `(ZF-SCORE)`;
3. rooted triangle loss `(Q-ZF)`;
4. internal-X ceiling `(X-M2-FR)`.

Do this without replacing `S_P` by total `C0`: first solve the exact pair-local `Ccap_P/(ONE-P)/(CROWD)` requirement for the `{d,bar d}` pair, then spend the remaining total slack on `Z_F`, and finally feed `(Q-ZF)` and `(X-M2-FR)` into `r-e(F)=delta`. The `omega=2` branch should be treated separately because `(ZF-INDEP)` has no quadratic content there.
