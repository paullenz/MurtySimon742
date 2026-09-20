# Residual-one k=2 exception-conservation coefficient refinement

Date: 2026-09-20

Status: **same-session hostile replay and sharpening** of `ONE_CODE_R1_K2_EXCEPTION_ORIENTATION_CONSERVATION.md`. Conditional on the same rigid residual-one interface. No finite scan is used.

## 1. Replay of the load-bearing chain

The following steps were rechecked directly after preservation of the first version.

1. `OC-UU` is an exact degree-sum consequence: for a U--U singleton pair, the neighbourhood union inside `A union U` omits both endpoints and the intersection has size one.
2. `OC-INERT` is correctly scoped. The predecessor heavy-endpoint theorem applies to **any** K-free escape adjacent to `z_h`, not only to a W-heavy vertex. The forced equation `N(t) cap N(h)={z_h}` makes t Y-anticomplete and anticomplete to every K-heavy escape. Hence a K-free vertex touching W_s can serve neither orientation of a K-heavy internal edge nor either orientation of a K-heavy--Y edge.
3. For the fully-free class F0, internal-edge U--U certificates and K-heavy--Y U--U certificates really do share the same graph-fixed ordered `(w,t)` pair. One pair cannot have two distinct singleton heads, so the incidence sets are disjoint.
4. In the opposite Y-edge orientation, a fixed ordered `(y,t)` pair has one graph-fixed singleton head, so `J_X<=yq` is the correct physical pair count.
5. The predecessor edge-capacity inequality uses the number I of exceptional oriented internal-edge certificates. After `OC-INERT`, every such U-exception lies in F0, so no omitted K-free/W-touching class enlarges I.

No scope or orientation defect was found in this replay. The claims remain same-day candidate mathematics pending the next independent daily audit.

## 2. Keep the actual F0 size instead of replacing it by p

Let

- `r=|R|` be the K-heavy population;
- `f=|F0|` be the fully K/W_s-free exceptional population;
- `E_R=sum_R epsilon_w`;
- `E_F=sum_F0 epsilon_t`.

On the exact low-k ray the singleton degree-sum price is p. Summing over the shared internal/Y U--U certificate incidences gives the sharper form

> **`p(I+J_U) <= f E_R+r E_F`.**                         `(CR-IJ)`

Put

`W=(f E_R+r E_F)/p`.

Then

`I+J_U<=W`.                                               `(CR-W)`

As before, the exceptional Y-edge need gives

`eta<=r+J_U+yq<=r+W-I+yq`.                               `(CR-ETA)`

The exact internal-edge capacity inequality is

`E_R+3A+2I>=r^2-eta`.

Therefore

`r^2`
` <= E_R+3A+2I+eta`
` <= E_R+3A+r+W+I+yq`
` <= E_R+3A+r+2W+yq`.

Hence the coefficient-sensitive conservation law is

> **`(1+2f/p)E_R + (2r/p)E_F + 3A + yq >= r(r-1)`.**     `(CR-MAIN)`

This strictly strengthens the coarsened

`3E_R+2E_F+3A+yq>=r(r-1)`

whenever `f<p` or `r<p`, which is always on the ray because the whole escape reservoir has size `p-1`.

A simple uniform corollary using `r,f<=p-1` is

> **`(3-2/p)E_R+(2-2/p)E_F+3A+yq>=r(r-1)`.**            `(CR-UNIF)`

The main value of `(CR-MAIN)` is strategic rather than cosmetic: in the weighted partition optimization, a small F0 class makes K-heavy U-slack markedly more expensive, while a large F0 class simultaneously triggers the F0/D sector-deficit theorem. This is exactly the coupling lost by the five-class max relaxation.

## 3. Next use

The next weighted optimization should retain `(r,f)` and `(CR-MAIN)` rather than only `D_phys>=r(r-1)/3`. The competing mechanism is now explicit:

- small f -> `(CR-MAIN)` forces a large K-heavy slack/hole bill;
- large f -> the W_s-free sector identity forces `Omega(fp)` located H/Y/U holes.

This two-variable coupling is the most promising route to improve the coarse asymptotic coefficient `tau=(13-sqrt(69))/50` without another raw-criticality theorem.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics.