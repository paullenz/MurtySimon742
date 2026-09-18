# Same-code crowding, complementary-pair localization, and a distribution-free cylinder cap

**Status:** internal structural theorem package, 18 September 2026.

This note continues `AU_WITNESS_OVERLAP_CAPACITY_AND_COMPLETE_CYLINDER_FEASIBILITY.md`.  At the preceding checkpoint the repaired cylinder route had reduced a quadratic A/U witness population to one remaining structural escape: a macroscopic Boolean code class in `A` or `A union U`.

The point here is that this escape is not free.  Same-code edge criticality extends from `A` to the whole coded layer `A union U`; elementary degree crowding then forces a large code class either to create many same-code edges or to pay slack; and the complementary-witness capacity of those edges forces either a large complementary code class or further scorecard payment.  This gives an explicit finite cap on the aligned code concentration and hence a **distribution-free** upper bound on the entire A/U cylinder channel.

The published order-12, size-32 `X_3` graph has `u=0` and is untouched.  No all-order or eventual second-extremal theorem is claimed.

---

## 1. Setup

Use the live near-full notation.  There are `p>=1` tight antipode pairs, unmatched set `U`, and `A=V\N[v]`.  Every vertex of `A union U` has a Boolean code in `{0,1}^p`.

For a code `c`, put

`A_c={x in A:c(x)=c}`, `n_c=|A_c|`,

`U_c={y in U:c(y)=c}`, `t_c=|U_c|`,

`V_c=A_c union U_c`, `N_c=n_c+t_c`.

Write

`L_c=sum_{x in A_c} epsilon_x`,

`E_c=sum_{y in U_c} epsilon_y`,

`S_c=L_c+E_c`.

Thus `sum_c S_c=E_U+L_A`.

Two global abbreviations will be useful:

> `T=a-p=p+u-lambda-1`,                                  `(LC0)`
>
> `V_0=a+u=2p+2u-lambda-1`.                              `(LC0b)`

For an unordered complementary pair `P={c,bar c}`, write

`S_P=S_c+S_bar c`,

`L_P=max(N_c,N_bar c)`.

---

## 2. Same-code critical edges throughout `A union U`

The existing same-code localization was stated for edges inside `A`.  The same argument works for every edge in the coded layer, with a useful extra restriction for `U--U` edges.

### Lemma 2.1 (full coded-layer same-code localization)

Let `xy` be an edge with `x,y in V_c` and `p>=1`.  Then one may orient the criticality certificate so that one endpoint is a source `z in {x,y}` and there is a vertex `w` satisfying

> `N(z) cap N(w)={the other endpoint}`.                  `(SC0)`

Moreover:

1. `w in A union U`;
2. `c(w)=bar c`;
3. if the source `z` lies in `U`, then in fact `w in A`.

#### Proof

The endpoints have the same Boolean code, so they share a matched endpoint and the edge lies in a triangle.  Deleting `xy` therefore leaves `x,y` at distance two.  Since the graph is diameter-2-critical, some other pair loses every path of length at most two; the usual triangle-edge criticality argument gives `(SC0)` with one endpoint of `xy` as source.

The witness cannot be the root `v`.  If the source is in `U`, it is adjacent to `v`, whereas a unique-common-neighbour certificate requires the source and witness to be nonadjacent.  If the source is in `A`, then its `p` matched neighbours all lie in `N(v)`; if the head lies in `A`, it is not adjacent to `v`, and if the head lies in `U`, those matched neighbours give additional common neighbours besides the head.

The witness cannot be a matched endpoint either: two equal-code vertices have identical adjacency to every matched endpoint, while `(SC0)` requires the witness to be adjacent to the head and nonadjacent to the source.

Thus `w in A union U`.  If `w` agreed with the source in any tight coordinate, the selected matched endpoint in that fibre would be a second common neighbour in `(SC0)`.  Hence `c(w)=bar c`.

Finally, if both the source and `w` lay in `U`, the root would be a second common neighbour.  Therefore a `U` source has its witness in `A`.

---

### Theorem 2.2 (same-code edge capacity)

Let

`e_c=e(G[V_c])`,

`e_A(c)=e(G[A_c])`,

`e_U(c)=e(G[U_c])`.

Choosing one orientation and witness for every same-code edge gives

> `e_c <= N_c N_bar c`,                                  `(SC1)`
>
> `e_A(c) <= n_c N_bar c`,                               `(SC1A)`
>
> `e_U(c) <= t_c n_bar c`.                               `(SC1U)`

For `lambda>=0`, the unique-common-neighbour slack identity also gives

> `(lambda+1)e_c`
>
> `<=N_bar c S_c+N_c S_bar c`,                           `(SC2)`
>
> `(lambda+1)e_A(c)`
>
> `<=N_bar c L_c+n_c S_bar c`,                           `(SC2A)`
>
> `(lambda+1)e_U(c)`
>
> `<=n_bar c E_c+t_c L_bar c`.                           `(SC2U)`

#### Proof

For `(SC1)`, map a certified edge to its ordered `(source,witness)` pair.  By Lemma 2.1 this lies in `V_c x V_bar c`.  A fixed ordered pair can occur only once, because its common neighbourhood is the singleton containing the head of the certified edge.  This proves injectivity.  The A-only and U-only versions use the corresponding source sets; for a U source, Lemma 2.1 restricts the witness to `A_bar c`.

For the weighted inequalities, every certificate satisfies

`epsilon_source+epsilon_witness>=lambda+1`.

A fixed source is paired with at most all allowable complementary witnesses, while a fixed witness is paired with at most all allowable sources.  Summing gives `(SC2)--(SC2U)`.

### Corollary 2.3 (same-code clique payment on the whole coded layer)

For `lambda>=0`, if `K subseteq V_c` is a clique of order `r>=2`, then

> `E_U+L_A >= ceil(r(lambda+1)/2)`.                       `(SCC+)`

This extends the preserved A-only same-code clique theorem to cliques containing unmatched vertices.

#### Proof

Orient the edges of `K` by chosen criticality certificates.  The orientation is a tournament.  Every witness has code `bar c`, hence lies outside `K`.  As in the preserved A-only proof, one witness cannot certify edges with two different heads, so it occurs on at most `r-1` oriented edges; each clique vertex is a source on at most `r-1` edges.  Summing the `binom(r,2)` slack inequalities and dividing by `r-1` gives `(SCC+)`.

---

## 3. Degree crowding inside one Boolean code

The same-code edge upper bounds become useful because high total degree leaves limited room outside a large code class.

### Lemma 3.1 (exact crowding lower bounds)

For every code `c`,

> `2e_A(c) >= n_c(n_c-T)-L_c`,                           `(CR-A)`
>
> `2e_U(c) >= t_c(t_c-T-1)-E_c`,                         `(CR-U)`
>
> `2e_c >= N_c(N_c-T)-t_c-S_c`.                          `(CR-V)`

#### Proof

An A-vertex `x` has

`d_{A union U}(x)=p+u-epsilon_x`.

There are `a+u-n_c` possible neighbours outside `A_c` but still in `A union U`, hence

`d_{A_c}(x)>=n_c-T-epsilon_x`.

Sum over `A_c`.

For `y in U`, the root and its `p` matched neighbours already account for `p+1` neighbours, so

`d_{A union U}(y)=p+u-1-epsilon_y`.

The same outside-capacity count gives

`d_{U_c}(y)>=t_c-T-1-epsilon_y`.

Summing proves `(CR-U)`.  Summing the corresponding bounds inside the whole `V_c` gives `(CR-V)`; A vertices contribute `N_c-T-epsilon_x`, while U vertices lose one further unit.

---

### Theorem 3.2 (one-sided complement-forcing slack)

Combining Lemma 3.1 with `(SC1)--(SC1U)` gives

> `L_c >= [n_c(n_c-T-2N_bar c)]_+`,                      `(CF-A)`
>
> `E_c >= [t_c(t_c-T-1-2n_bar c)]_+`,                    `(CF-U)`
>
> `S_c >= [N_c(N_c-T-2N_bar c)-t_c]_+`.                  `(CF-V)`

Thus a macroscopic code class can remain cheap only if its complementary class is itself sufficiently large.  The U-only statement is stronger: a large same-code U-class specifically requires A-mass in the complementary code, because U-source witnesses cannot lie in U.

This is the promised dense/sparse dichotomy in a finite form.  If the complementary capacity is small, crowding forces more same-code edges than criticality can certify without paying slack; if the complement is large, the survivor is localized to a complementary pair rather than an isolated large class.

---

## 4. Complementary-pair scorecard payment

The weighted edge capacities turn the same crowding into direct pairwise scorecard inequalities.

### Theorem 4.1 (pair payment from one side)

Let `P={c,bar c}` and `L_P=max(N_c,N_bar c)`.  For `lambda>=0`,

> `S_P >=`
>
> ` (lambda+1)[N_c(N_c-T)-t_c]_+`
>
> ` /(2L_P+lambda+1)`.                                   `(CPP-V)`

Likewise

> `S_P >=`
>
> ` (lambda+1)[n_c(n_c-T)]_+`
>
> ` /(2L_P+lambda+1)`,                                   `(CPP-A)`
>
> `S_P >=`
>
> ` (lambda+1)[t_c(t_c-T-1)]_+`
>
> ` /(2L_P+lambda+1)`.                                   `(CPP-U)`

The integer scorecard may of course be replaced by the ceiling of these real lower bounds.

#### Proof

For `(CPP-V)`, put `D=N_c(N_c-T)-t_c`.  By `(CR-V)`,

`2e_c>=D-S_c`.

By `(SC2)`,

`(lambda+1)e_c<=N_bar c S_c+N_c S_bar c<=L_P S_P`.

Therefore

`(lambda+1)(D-S_c)<=2L_P S_P`.

Since `S_c<=S_P`, rearrangement gives `(CPP-V)`.  The A and U forms are identical, using `(CR-A)/(SC2A)` and `(CR-U)/(SC2U)` respectively.

### Theorem 4.2 (symmetric complementary-pair payment)

Put `N=N_c`, `M=N_bar c`.  Then

> `S_P >=`
>
> `(lambda+1)[`
>
> ` N(N-T)+M(M-T)-(t_c+t_bar c)`
>
> `]_+ /(4L_P+lambda+1)`.                                `(CPP-P)`

#### Proof

Add the two crowding inequalities `(CR-V)` for `c` and `bar c`.  The two weighted edge upper bounds have the same right-side expression after swapping the codes.  Hence

`(lambda+1)(e_c+e_bar c)<=2L_P S_P`.

The summed crowding lower bound is

`2(e_c+e_bar c)>=D_c+D_bar c-S_P`.

Rearrange.

---

## 5. The A/U witness channel localizes to one complementary pair

Return to the selected A/U cylinder certifications from `(AUC1)--(AUC4)`.  For an unordered pair `P={c,bar c}`, put

`C_P=C_c+C_bar c`,

`A_P=n_c+n_bar c`,

`V_P=N_c+N_bar c`.

Let

`M_AU=sum_P C_P`

and `V_0=a+u=sum_P V_P`.

### Theorem 5.1 (pair-traffic concentration)

For every complementary pair,

> `C_P<=A_P V_P`.                                        `(PT1)`

Consequently,

> `max_P C_P >= M_AU^2/(a V_0)`.                         `(PT2)`

For a maximizing pair, at least one directed product satisfies

> `max(n_cN_bar c,n_bar c N_c)`
>
> `>= M_AU^2/(2aV_0)`.                                   `(PT3)`

Thus quadratic A/U cylinder traffic in a linear-size coded layer forces **one actual complementary code pair** to carry quadratic traffic; in that pair an A-source class and the complementary A/U witness class are both linear.

#### Proof

`(AUC1)` gives

`C_P<=n_cN_bar c+n_bar cN_c<=A_PV_P`.

Therefore

`sum_P sqrt(C_P)<=sum_P sqrt(A_PV_P)<=sqrt(aV_0)`

by Cauchy.  If `C_max=max C_P`, then

`M_AU=sum_P C_P<=sqrt(C_max)sum_P sqrt(C_P)<=sqrt(C_max aV_0)`,

which proves `(PT2)`.  The two directed products sum to at least `C_P`, proving `(PT3)`.

---

### Theorem 5.2 (aligned-code weighted capacity)

Define

> `w_c=N_c+n_c=2n_c+t_c`,
>
> `mu_* = max_c w_c`.

Then the old coarse factor `mu_V+mu_A` can be replaced by the aligned maximum:

> `(lambda+1)M_AU <= mu_*(E_U+L_A)`.                     `(AUC5+)`

More locally,

> `(lambda+1)C_P`
>
> `<=max(w_c,w_bar c) S_P`.                              `(PT4)`

Hence the heavy pair from Theorem 5.1 pays

> `S_P >= (lambda+1)C_P/max(w_c,w_bar c)`.               `(PT5)`

and, since `max(w_c,w_bar c)<=2V_0`,

> `E_U+L_A`
>
> `>= (lambda+1)M_AU^2/(2aV_0^2)`.                       `(PT6)`

Equivalently,

> `M_AU <= V_0 sqrt(2a(E_U+L_A)/(lambda+1))`.             `(PT7)`

#### Proof

Sum `(AUC3)` over all codes:

`(lambda+1)M_AU`

`<=sum_c [N_bar c L_c+n_cS_bar c]`.

Reindex the second term and use `L_c<=S_c`:

`<=sum_c (N_bar c+n_bar c)S_c`

`<=mu_* sum_c S_c`.

This is `(AUC5+)`.

For one complementary pair, the same calculation without taking the global maximum gives

`(lambda+1)C_P`

`<=w_bar c S_c+w_c S_bar c`

`<=max(w_c,w_bar c)S_P`.

Combine with `(PT2)` and `max(w_c,w_bar c)<=2V_0` to obtain `(PT6)--(PT7)`.

---

## 6. Macroscopic aligned code concentration self-prices

The parameter `mu_*` is no longer an unbounded structural escape.  The one-sided complement-forcing theorem and the finite total coded population give a direct scorecard cap.

### Theorem 6.1 (global aligned-code self-pricing)

For every code `c`, put `w_c=2n_c+t_c`.  Define

> `D_0=T+2V_0+1=5p+5u-3lambda-2`.                        `(AC0)`

Then

> `S_c >=`
>
> `[ (w_c/2)(3w_c/2-D_0) ]_+`.                           `(AC1)`

#### Proof

Let `N=N_c`, `M=N_bar c`, and `w=w_c=N+n_c`.  From `(CF-V)`,

`S_c >= [N(N-T-2M)-t_c]_+`.

Since `t_c<=N`,

`N(N-T-2M)-t_c>=N(N-T-2M-1)`.

Also `N>=w/2`, while the complementary class is part of the remaining coded population, so

`M<=V_0-N<=V_0-w/2`.

Therefore

`N-T-2M-1>=3N-D_0`.

Whenever the right side of `(AC1)` is positive, `N(3N-D_0)` is increasing for `N>=w/2`, so it is at least

`(w/2)(3w/2-D_0)`.

If that expression is nonpositive, `(AC1)` is trivial.

### Corollary 6.2 (finite code-concentration cap above threshold)

Assume `m>M(n)`, so `E_U+L_A<=C_0`, with `C_0>=0`.  Define

> `R_code=`
>
> `floor((D_0+sqrt(D_0^2+12C_0))/3)`.                    `(AC2)`

Then

> `mu_*<=R_code`.                                         `(AC3)`

#### Proof

Each `S_c<=C_0`.  The positive root of

`(w/2)(3w/2-D_0)=C_0`

is exactly the real quantity inside the floor in `(AC2)`.  If `D_0>=0`, that root is at least the zero-payment threshold `2D_0/3`; if `D_0<0`, the quadratic payment is positive for every `w>0`.  Thus `(AC1)` implies `(AC3)` in both cases.

This closes the previous checkpoint's generic “macroscopic code class” escape at the level of finite parameters: a large class may still occur, but its maximum size is now explicitly controlled by the second-extremal scorecard.

---

## 7. Distribution-free A/U and complete cylinder caps

Combining `(AUC5+)` with Corollary 6.2 removes every code-distribution parameter from the A/U overlap bound.

### Corollary 7.1 (distribution-free A/U witness capacity)

For `lambda>=0` and an above-`M(n)` candidate,

> `M_AU <= R_code C_0/(lambda+1)`.                        `(DAU1)`

The independent pair-concentration estimate `(PT7)` gives

> `M_AU <= V_0 sqrt(2aC_0/(lambda+1))`.                   `(DAU2)`

Hence

> `M_AU <= min(`
>
> ` R_code C_0/(lambda+1),`
>
> ` V_0 sqrt(2aC_0/(lambda+1))`
>
> `)`.                                                    `(DAU3)`

This is stronger conceptually than the previous `mu_A/mu_V` trichotomy: there is no longer an unspecified large-code parameter on the right.

### Corollary 7.2 (distribution-free complete cylinder feasibility)

Let `X` be any family of beta-loaded A-centres and choose one repeated class `R_x` for each centre as in the repaired cylinder theorem.  Then

> `sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `<= a R_A(C_0)`
>
> ` + min(`
>
> `     R_code C_0/(lambda+1),`
>
> `     V_0 sqrt(2aC_0/(lambda+1))`
>
> `   )`,                                                `(DCF)`

where

`R_A(C_0)=max(2,floor((1+sqrt(1+4C_0))/2))`.

#### Proof

The matched-B channel satisfies

`M_P<=aR_A(L_A)<=aR_A(C_0)`.

The A/U channel satisfies `(DAU3)`.  Every repeated-cylinder edge certificate lies in exactly one of these two channels, and the cylinder theorem supplies the left-side lower bound.

`(DCF)` is deliberately coarser than the codewise `(LDCF)`, but it is the first **fully parameter-only** complete-cylinder inequality after the repeated-code scope repair.

---

## 8. Strategic consequence

The preceding checkpoint ended with a structural trichotomy: a quadratic repeated-cylinder population had to pay quadratic `L_A` or create a macroscopic A/AU Boolean code class.  The new results sharpen that in three ways.

1. A same-code class in `A union U` now has an exact edge-critical capacity, with an even stronger U-only complement requirement.
2. Degree crowding converts large code multiplicity into either scorecard payment or a genuinely large **complementary pair**, and the pair itself has a weighted scorecard inequality.
3. The aligned concentration `mu_*` is explicitly bounded by `R_code`, so the complete A/U cylinder channel has the distribution-free cap `(DAU3)`, and the whole cylinder route has `(DCF)`.

The next coherent target is therefore no longer a generic dense/sparse large-code-class theorem.  It is to combine the **parameter-only cylinder upper bound `(DCF)`** with a lower bound on repeated-cylinder mass obtained from the source-tuple / beta-deficit distribution.  The continuum source-profile route already controls how much beta mass can sit at each deficit; the missing bridge is to turn enough of that low-deficit population into the left side of `(DCF)` without losing the exponential `2^{k_x}` factor.

In parallel, `(CPP-P)` and `(PT4)` identify the equality/stability structure if `(DCF)` is close to sharp: cylinder traffic must concentrate in a small number of complementary code pairs whose class sizes, internal same-code edges, and scorecard slacks simultaneously approach their crowding capacities.  That is a much narrower object for a direct structural attack.

The independent `Q=0` / false-twin-core branch remains separate.  Nothing here suppresses the published `X_3` negative control, which has `u=0`.

---

## 9. Trust boundary

- Lemma 2.1 is a hand D2C triangle-edge criticality argument plus the partial-Boolean transversal structure.
- `(SC1)--(SC2U)` are hand injections and slack multiplicity counts.
- `(CR-A)--(CR-V)` are exact degree-capacity counts.
- `(CF-A)--(CPP-P)` are algebraic consequences of those two theorem families.
- `(PT1)--(PT7)` are exact complementary-pair double counts and Cauchy.
- `(AC1)--(AC3)` eliminate complement mass only through the finite total coded population and the above-threshold scorecard.
- The algebraic consequences have an independent finite checker; that checker is audit support only and does not verify the D2C witness-localization proof itself.
- All positive `(lambda+1)` capacity conclusions are promoted here for `lambda>=0`.
- No arbitrary repeated cylinder class is identified with its centre code.
- No all-order or eventual second-extremal theorem is claimed.
- `X_3` has `u=0` and remains a mandatory hostile control.
