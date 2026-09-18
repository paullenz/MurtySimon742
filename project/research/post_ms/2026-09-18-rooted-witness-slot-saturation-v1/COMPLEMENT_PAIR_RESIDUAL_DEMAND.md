# Complementary-pair residual demand

Date: 2026-09-18

Status: live structural theorem; this is the first source-to-pair composition of the rooted witness-slot budget with the preserved matched-B/A-U capacities.

## 1. Why this is the right composition

The preceding global scalar synthesis failed because forced A-edge demand could be paid, algebraically, by slack in unrelated Boolean-code pairs. The local witness-slot theorem supplies exactly the missing information for the direct channel: a direct edge incident with `z` consumes the local unused-slot budget `r_z` at that same A-coordinate.

The next step is therefore to look at **all A-edges whose two endpoints lie in one unordered complementary tight-code pair**. Such an edge cannot export its non-direct criticality certificate to another source pair: whichever endpoint is chosen as source still belongs to the same complementary pair.

This yields a genuinely local residual-demand inequality.

## 2. Notation

Let

> `P={c,bar c}`

be an unordered complementary tight-code pair. Put

> `A_P=A_c union A_bar c`,
>
> `a_P=|A_P|=n_c+n_bar c`,                               `(P0)`
>
> `L_P=L_c+L_bar c`,
>
> `S_P=S_c+S_bar c`.                                     `(P1)`

Recall

> `T=a-p=p+u-lambda-1`,
>
> `L=lambda+1`.                                           `(P2)`

For each `z in A`, let `r_z` be the number of unused rooted B-edge witness slots with A-coordinate `z`. Define the **pair residual-Hamming resource**

> `R_P=sum_{z in A_P} r_z d_A(z)`.                       `(P3)`

The pairs partition A, so

> `sum_P R_P=sum_{z in A} r_z d_A(z)<=r K_A`,            `(P4)`

where `K_A=min(p+u,a-1)`.

Let

- `D_P` be the direct A-edges with both endpoints in `A_P`;
- `N_P` be the non-direct A-edges with both endpoints in `A_P`.

Then

> `e(G[A_P])=D_P+N_P`.                                   `(P5)`

## 3. Pair crowding forces internal A-edges

### Lemma 3.1 — complementary-pair A-crowding

> `2e(G[A_P])>=a_P(a_P-T)-L_P`.                          `(PC)`

#### Proof

For `z in A_P`, the degree of `z` inside the full coded layer is

`d_{A union U}(z)=p+u-epsilon_z`.

There are exactly `(a+u)-a_P` coded-layer vertices outside `A_P`, so

`d_{A_P}(z)`
` >= p+u-epsilon_z-[(a+u)-a_P]`
` = a_P-(a-p)-epsilon_z`
` = a_P-T-epsilon_z`.

Sum over `z in A_P`. `square`

The right side is useful precisely when the complementary pair contains more than the natural outside-capacity threshold `T`.

## 4. Local residual slots remove the affordable direct share

The local witness-slot Hamming theorem gives, for every `z in A`,

> `p d_D(z)<=r_z d_A(z)`.                                `(LH-D)`

Every direct A-edge joins complementary tight codes, so every direct edge incident with a vertex of `A_P` has its other endpoint in the same `A_P`. Summing `(LH-D)` over `z in A_P` therefore gives

> `2pD_P<=R_P`.                                          `(PD)`

Subtracting the direct share from `(PC)` yields the local non-direct demand.

### Theorem 4.1 — pair residual-demand floor

> `2N_P`
> ` >= [a_P(a_P-T)-L_P-R_P/p]_+`.                        `(PRD)`

Equivalently,

> `N_P`
> ` >= (1/2)[a_P(a_P-T)-L_P-R_P/p]_+`.                   `(PRD')`

This is the key new lower bound: a crowded complementary A-pair must create internal A-edges; the part that can be direct is limited by **unused rooted slots belonging to vertices of that same pair**; the remainder is forced into the non-direct witness channels.

## 5. Internal non-direct edges cannot export their source pair

Choose one criticality certificate for every non-direct A-edge, as in the preserved complete-channel theorem.

If an internal edge of `A_P` is oriented from either endpoint, its source code is either `c` or `bar c`. Therefore:

- an A/U unique-common-neighbour witness has the complementary source code and remains in pair `P`;
- a matched-B witness has gamma code equal to the source code and likewise belongs to the gamma pair `P`.

Let

- `C_P` be A/U certificate traffic sourced from pair `P`;
- `P_P` be matched-B certificate traffic sourced from pair `P`.

Then every internal non-direct edge in `A_P` consumes one of these two local capacities, so

> `N_P<=C_P+P_P`.                                        `(LOC)`

This is the exact anti-export property missing from the preceding scalar synthesis.

## 6. Pair-local capacity

The preserved aligned A/U capacity gives

> `L C_P<=max(w_c,w_bar c)S_P`
> `          <=R_code(S_P)S_P`.                          `(AU-P)`

For matched-B traffic, let `g_P` be the number of tight fibres whose two gamma codes are the pair `P`, and put

> `h_P=sum_{i in I_P} min(t_i^0,t_i^1)`.                 `(H0)`

The preserved complementary-pair matched-foot theorem gives

> `P_P<=g_P max(n_c,n_bar c)+h_P`.                       `(MB-P0)`

Aligned-code self-pricing implies

> `max(n_c,n_bar c)<=R_code(S_P)/2`,                     `(MB-P1)`

hence

> `P_P<=g_P R_code(S_P)/2+h_P`.                          `(MB-P)`

The resources satisfy

> `sum_P g_P=p`,                                          `(G)`

and fibre polarization gives the global auxiliary budget

> `L sum_P h_P<=R_A(L_A)L_A`.                            `(H)`

## 7. Main local feasibility theorem

Combining `(PRD')`, `(LOC)`, `(AU-P)` and `(MB-P)` gives:

### Theorem 7.1 — complementary-pair residual feasibility

For every unordered complementary pair `P`,

> `(1/2)[a_P(a_P-T)-L_P-R_P/p]_+`
> ` <= g_P R_code(S_P)/2`
> `    +h_P`
> `    +R_code(S_P)S_P/L`.                               `(CPRF)`

Equivalently,

> `[a_P(a_P-T)-L_P-R_P/p]_+`
> ` <= R_code(S_P)[g_P+2S_P/L]+2h_P`.                    `(CPRF2)`

This is the first theorem in the live branch that simultaneously keeps:

1. **pair population** `a_P`;
2. **pair A-slack** `L_P`;
3. **pair total slack** `S_P`;
4. **pair-local unused rooted-slot resource** `R_P`;
5. **pair matched-fibre multiplicity** `g_P`;
6. **pair two-sided matched-foot traffic** `h_P`.

None of the forced internal non-direct demand can be paid by slack in an unrelated complementary pair.

## 8. Aggregate resource system

The local inequalities `(CPRF)` come with disjoint global budgets:

> `sum_P a_P=a`,                                         `(B1)`
>
> `sum_P L_P=L_A`,                                       `(B2)`
>
> `sum_P S_P=S`,                                         `(B3)`
>
> `sum_P R_P<=rK_A`,                                     `(B4)`
>
> `sum_P g_P=p`,                                         `(B5)`
>
> `sum_P h_P<=R_A(L_A)L_A/L`.                            `(B6)`

Thus the current residual problem has been reduced to a finite **pair-resource allocation problem** rather than a single global scalar inequality.

The positive-part term is important: if a pair is not crowded beyond `T`, no internal-edge demand is asserted. But any pair with `a_P>T` must pay its quadratic crowding either through local A-slack, local unused-slot/Hamming resource, or the non-direct matched/A-U capacities of that same pair.

## 9. Strategic consequence

This theorem answers the precise obstruction recorded at the previous checkpoint. The forced A-edge mass is still global, but whenever it creates a crowded complementary pair, that pair's internal non-direct demand is no longer exportable.

The next move should be to combine `(CPRF)` with a lower bound forcing **some** `a_P` above `T` (or forcing a large sum of the positive crowding terms) from the exact rooted-transfer demand and the source/Hall population data. A convexity/majorization argument over the `a_P` is the natural candidate. Unlike the failed scalar envelope, such an argument would retain the local resources all the way to the contradiction.

The `X_3` negative control remains untouched: its A-layer is independent, so `N_P=0` for every pair and `(CPRF)` is vacuous.