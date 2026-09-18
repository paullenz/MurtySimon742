# Complementary-pair Hall-cut theorem

Date: 2026-09-18

Status: structural strengthening of the pair residual-demand theorem.

The single-pair inequality is not the natural endpoint. If several complementary code pairs are grouped together, **all non-direct A-edges internal to their union must still source a criticality certificate from one of those same pairs**. This gives a Hall-type cut condition for every collection of complementary pairs and, unlike a sum of singleton inequalities, also captures A-edges running between different pairs inside the collection.

## 1. A collection of complementary pairs

Let `X` be any collection of unordered complementary tight-code pairs. Put

> `A_X=union_{P in X} A_P`,
>
> `a_X=|A_X|`,                                            `(X0)`
>
> `L_X=sum_{P in X} L_P`,
>
> `S_X=sum_{P in X} S_P`,
>
> `Z_X=sum_{P in X} Z_P`,
>
> `R_X=sum_{P in X} R_P`.                                `(X1)`

Here

- `Z_P=a_Pu-e(A_P,U)` is the A--U nonedge deficit;
- `R_P=sum_{z in A_P} r_z d_A(z)` is the local rooted-slot Hamming resource.

Recall

> `T=a-p=p+u-lambda-1`,
>
> `L=lambda+1`.                                           `(X2)`

Let `D_X` and `N_X` be respectively the direct and non-direct A-edges with both endpoints in `A_X`.

## 2. Subset crowding

### Lemma 2.1 — exact cross-deficit crowding on `A_X`

> `2e(G[A_X])>=a_X(a_X-T)-L_X+Z_X`.                     `(XC)`

#### Proof

For `z in A_X`,

`d_A(z)=p+u-epsilon_z-d_U(z)`.

There are at most `a-a_X` A-vertices outside `A_X`, hence

`d_{A_X}(z)>=d_A(z)-(a-a_X)`.

Summing gives

`2e(G[A_X])`
` >=a_X(p+u)-L_X-e(A_X,U)-a_X(a-a_X)`.

Since `Z_X=a_Xu-e(A_X,U)` and `p-a=lambda+1-p-u`, this simplifies to `(XC)`. `square`

This is stronger than summing the singleton-pair crowding inequalities because it also counts edges between different complementary pairs in `X`.

## 3. Local residual slots remove the direct part on the same cut

A direct A-edge joins complementary tight codes. Therefore if one endpoint lies in `A_X`, its other endpoint belongs to the **same** complementary pair and also lies in `A_X`. Thus every direct edge incident with `A_X` is internal to `A_X`.

The local witness-slot theorem gives

`p d_D(z)<=r_z d_A(z)`

for every `z in A`. Summing over `A_X` yields

> `2pD_X<=R_X`.                                          `(XD)`

Subtracting the direct part from `(XC)` gives:

### Theorem 3.1 — subset non-direct demand

> `2N_X`
> ` >=[a_X(a_X-T)-L_X+Z_X-R_X/p]_+`.                    `(XND)`

## 4. Hall anti-export property

Choose one criticality certificate for every non-direct A-edge.

If both endpoints of such an edge lie in `A_X`, then whichever endpoint is chosen as source has its complementary code pair in `X`. Hence the certificate is charged either to

- matched-B traffic `P_P`, or
- A/U UCN traffic `C_P`

for some `P in X`.

Therefore

> `N_X<=sum_{P in X}(P_P+C_P)`.                          `(XLOC)`

This is precisely a Hall cut: internal demand of `X` cannot be exported to source capacity outside `X`.

## 5. Capacity side

For each pair `P`, the preserved local capacities give

> `C_P<=R_code(S_P)S_P/L`,                               `(XAU)`
>
> `P_P<=g_P R_code(S_P)/2+h_P`.                          `(XMB)`

Thus

> `2(P_P+C_P)`
> ` <=R_code(S_P)[g_P+2S_P/L]+2h_P`.                    `(XCAP)`

## 6. Main theorem

Combining `(XND)`, `(XLOC)` and `(XCAP)` gives:

### Theorem 6.1 — complementary-pair Hall-cut feasibility

For **every** collection `X` of complementary tight-code pairs,

> `[a_X(a_X-T)-L_X+Z_X-R_X/p]_+`
> ` <=sum_{P in X}`
> `   { R_code(S_P)[g_P+2S_P/L]+2h_P }`.                `(HALL-P)`

The singleton choice `X={P}` recovers the strengthened pair residual-feasibility theorem. The choice of all pairs gives a global consequence. Intermediate `X` is the new information: it captures non-direct A-edges crossing between several low-capacity pairs, which no sum of singleton inequalities can see.

## 7. Resource budgets

The Hall cuts are coupled by disjoint global budgets:

> `sum_P a_P=a`,                                         `(B1)`
>
> `sum_P L_P=L_A`,                                       `(B2)`
>
> `sum_P S_P=S`,                                         `(B3)`
>
> `sum_P Z_P=u(p-lambda)+2q+E_U`,                        `(B4)`
>
> `sum_P R_P<=rK_A`,                                     `(B5)`
>
> `sum_P g_P=p`,                                         `(B6)`
>
> `L sum_P h_P<=R_A(L_A)L_A`.                            `(B7)`

The exact residual split remains

> `f=(p-lambda)(p+u)+q+E_U-delta`.                        `(RSF)`

Thus the live problem can now be phrased as a **cut-feasibility problem on complementary code pairs**: distribute A-population, unmatched cross-deficit, slack, unused-slot Hamming resource, matched fibres, and two-sided matched traffic so that every Hall cut `(HALL-P)` is satisfied while `delta<D_M`.

## 8. Why this is materially stronger

The failed scalar synthesis allowed capacity in a slack-rich pair to pay demand generated anywhere. The singleton pair theorem stopped that for edges whose endpoints lie in one pair, but still missed non-direct edges joining two different pairs.

`(HALL-P)` removes that escape. If a family `X` carries a large A-population or large A--U cross deficit, its induced A-subgraph is crowded. Direct traffic on that induced subgraph is limited by the same vertices' local unused-slot budgets. Every remaining internal edge must consume non-direct capacity **inside the same family `X`**.

This is the exact Hall-style localization that the previous checkpoint identified as missing.

## 9. Next mathematical target

The next step should not be another local capacity inequality. It should be a **cut selection / majorization lemma** proving that, under the global budgets and the above-`M(n)` residual bound, some collection `X` necessarily violates `(HALL-P)`.

Natural candidate selections are threshold sets ordered by one of:

- `a_P/T` (population crowding);
- `Z_P/a_P` (A--U deficit density);
- capacity density `R_code(S_P)[g_P+2S_P/L]+2h_P` per A-vertex.

A successful threshold lemma would convert the current local resource system into a compact structural exclusion without reverting to the information-destroying global scalar envelope.

The `X_3` hostile control remains untouched: `A` is independent, so every induced non-direct demand `N_X` is zero.