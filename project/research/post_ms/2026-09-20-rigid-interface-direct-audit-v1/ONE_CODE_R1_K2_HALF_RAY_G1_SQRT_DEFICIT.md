# Residual-one k=2 half-ray: square-root deficit when g=1

Date: 2026-09-20

Status: **same-session conditional scaling theorem**, downstream of the replayed Delta-three barrier and the H-positive P-carrier private-spoke classification. No finite scan is used.

## 1. Setup

Use the corrected half-ray

`p=2t, c=y=t, u=t+1, h=2t-1`,

with deficit variables

`Delta=d=a+b+c0`,

and residual-bar column `P=U_j^-`. Assume

> **`g=|U\P|=1`.**

Then `c0>=1` and `|P\W_s|=t-2`.

The general small-deficit theorem gives at least

`T>=t-1-d-2b`

shared reverse-U edges on residual-saturated H-rows.

Because there is only one outside U-head, each saturated row supports at most one such shared edge; hence these T edges have T distinct H-source rows and T distinct endpoint-indexed reverse witnesses.

## 2. Many source rows have missing H-degree zero

For a saturated shared-source row `h_i`, residual-slot saturation already uses one U-neighbour and its shared edge uses the unique outside head. Therefore `d_U(h_i)<=2` is tight at the row-capacity level.

The local partition is

`d_U(h_i)=r_i^q+1+s_i`,

with `s_i=1`, while `a_i=m_i-r_i^q`. Thus `r_i^q=0` and

> **`m_i=a_i`.**                                        `(G1-1)`

Since `sum_i a_i=a`, at most a of the T source rows have positive `a_i`. Let `R0` be the number with `a_i=0`; then each such row has `m_i=0`, so the R0 rows form a clique in H, and

`R0>=T-a`

`>=t-1-d-2b-a`

`=t-1-2a-3b-c0`.

Using `a+b+c0=d` and `c0>=1`,

> **`R0>=t+1-3d`.**                                     `(G1-2)`

## 3. Their reverse witnesses cannot supply the residual P-neighbour slots

Each of the R0 rows has a distinct endpoint-indexed reverse-U witness. The singleton equation gives

`d_H(w)<=m_i=0`,

so all R0 witnesses are H-anticomplete. The two selected witnesses `W_s` are also H-anticomplete.

Every R0 source row is residual-saturated and therefore needs exactly one P-neighbour. None of the R0 reverse witnesses and neither selected witness can provide it.

Since `|P\W_s|=t-2`, after removing the R0 H-anticomplete reverse witnesses there are at most

> **`N_car<=t-2-R0<=3d-3`**                              `(G1-3)`

P-vertices available to act as carriers for these R0 unique P-neighbour slots.

## 4. One carrier can touch only O(sqrt(t)) clique rows

The replayed private-spoke theorem applies to every H-positive carrier `z in P`: its private d-support is either empty or exactly two coordinates, and in the two-coordinate case z misses the corresponding two H-vertices.

Therefore, for every missing-degree-zero H-row actually touched by z, z sees that row's private foot. For any two touched R0 rows, z spoils both private-foot orientations of their H--H edge. The preserved H--H certificate split forces that edge to be U-certified.

The total number of U-certified H--H edges is at most `u=t+1`. Thus, if a carrier touches r of the R0 clique rows,

`binom(r,2)<=u`.

Set

`R(t)=floor((1+sqrt(8t+9))/2)`.

Then every carrier touches at most `R(t)` rows.

Covering all R0 rows with at most `N_car` carriers gives

> **`R0<=(3d-3)R(t)`.**                                  `(G1-4)`

Combining with `(G1-2)`:

> **`t+1-3d <= (3d-3)R(t)`.**                            `(G1-5)`

Equivalently,

> **`d >= ceil((t+1+3R(t))/(3(R(t)+1)))`.**              `(G1-6)`

In particular

> **`Delta=Omega(sqrt(t))` whenever `g=1`.**             `(G1-7)`

Asymptotically `R(t)~sqrt(2t)`, so the explicit lower bound is

`Delta >= (1/(3sqrt(2))+o(1)) sqrt(t)`.

## 5. Significance

This is the first scaling, rather than constant, lower bound on the corrected H--U capacity deficit along the intermediate half-ray. It shows that the one-residual-plus-head geometry cannot remain within O(1) of simultaneous capacity saturation.

The argument uses only located physical constraints:

1. one outside U-head;
2. exact row capacity;
3. distinct reverse witnesses;
4. H-anticompleteness of witnesses sourced from H-complete rows;
5. raw private-spoke carrier classification;
6. the global U-certified H--H capacity.

No score-ceiling comparison and no finite enumeration substitutes for the proof.

## 6. Next target

Generalize from `g=1` to `1<g<=Delta`. A saturated shared-source row then satisfies

`m_i<=a_i+g-s_i`,

so most source rows have missing H-degree `O(g)`, not zero. The needed extension is a carrier theorem for a set of H-rows with bounded missing degree: a carrier touching r such rows should force all but `O(rg)` pairs to be U-certified. If this yields

`r=O(sqrt(u+rg))`,

the same covering argument should produce a square-root or stronger lower bound for arbitrary small Delta.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.