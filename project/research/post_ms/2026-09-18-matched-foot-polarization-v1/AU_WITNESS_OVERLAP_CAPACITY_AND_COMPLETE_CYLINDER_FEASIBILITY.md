# A/U witness overlap capacity and complete cylinder feasibility

**Status:** internal structural theorem package, 18 September 2026.

This note continues `MATCHED_FOOT_POLARIZATION_SELF_PRICING_AND_CYLINDER_SPILL.md`.  That file shows that a large family of low-deficit beta cylinders must either spend substantial `L_A` on matched-B feet or spill a quantified number of criticality certificates into witnesses in `A union U`.

The remaining issue was global overlap: the same A/U witness can be reused across different centres, so a per-cylinder distinct-witness count cannot simply be summed.

The key observation below closes that bookkeeping gap.  Every A/U cylinder certificate is determined by an **ordered complementary-code source/witness pair**, and a fixed pair can occur at most once because its common neighbourhood is a singleton.  This gives both a pure complement-product capacity and a scorecard-weighted capacity.  Combining them with the matched-foot theorem yields one exact inequality covering **all three critical-witness channels**.

The result is a reduction theorem, not an eventual second-extremal proof.  The published order-12, size-32 `X_3` graph has `u=0` and is untouched.

---

## 1. Setup

For a Boolean code `c`, write

`A_c={x in A:c(x)=c}`, `n_c=|A_c|`,

`U_c={y in U:c(y)=c}`, `t_c=|U_c|`,

`N_c=n_c+t_c`.

Define codewise slack masses

`L_c=sum_{x in A_c} epsilon_x`,

`E_c=sum_{y in U_c} epsilon_y`,

`S_c=L_c+E_c`.

Thus

`sum_c L_c=L_A`,

`sum_c E_c=E_U`,

`sum_c S_c=E_U+L_A`.

Let `C` be any chosen collection of A/U critical-witness certifications coming from repeated beta-cylinder edges.  Each certification has:

- a **source** `z in A`;
- a **witness** `w in A union U`;
- a unique common neighbour `h`, with

> `N(z) cap N(w)={h}`;                                    `(AU1)`

- and, by the repaired localisation theorem,

> `c(w)=bar c(z)`.                                        `(AU2)`

For an outgoing cylinder edge, the source is the centre.  For an incoming A/U cylinder edge, the source is the repeated-class vertex.  In both cases the source lies in `A`.

Let `C_c` be the number of chosen certifications whose source has code `c`, and

`M_AU=sum_c C_c`.

---

## 2. Fixed source/witness pairs cannot be reused

### Lemma 2.1 (pair uniqueness)

A fixed ordered pair `(z,w)` with `z in A`, `w in A union U` can occur in at most one A/U cylinder certification.

### Proof

If `(z,w)` is used, `(AU1)` says that `N(z) cap N(w)` is the singleton `{h}`.  The head `h` is therefore uniquely determined by the pair.  The certified critical edge is the source-head edge `zh`.  A second certification using the same source/witness pair would require a second head in the same singleton common neighbourhood.

This argument is global: it does not depend on the centre or repeated cylinder class from which the certificate arose.

---

## 3. Pure complementary-code product capacity

Pair uniqueness immediately gives a first aggregate bound.

### Theorem 3.1 (complement-product A/U capacity)

For every code `c`,

> `C_c<=n_c N_{bar c}`.                                   `(AUC1)`

Consequently

> `M_AU<=sum_c n_c N_{bar c}`.                            `(AUC2)`

### Proof

A source of code `c` has exactly `N_{bar c}` possible A/U witnesses of the required complementary code.  There are `n_c` possible A-sources.  By Lemma 2.1 each ordered source/witness pair can be used at most once.

This is a genuine global overlap theorem: arbitrary reuse of one witness across centres is already included in the product count.

---

## 4. Scorecard-weighted A/U capacity

Every certificate also obeys the unique-common-neighbour slack inequality

> `epsilon_z+epsilon_w>=lambda+1`.                        `(AU3)`

The same pair uniqueness controls the multiplicities with which source and witness slack can be charged.

### Theorem 4.1 (codewise weighted overlap capacity)

For every code `c`,

> `(lambda+1) C_c`
>
> `<=N_{bar c} L_c+n_c S_{bar c}`.                        `(AUC3)`

### Proof

Sum `(AU3)` over all `C_c` certifications with source code `c`.

A fixed source `z in A_c` can be paired with at most all `N_{bar c}` complementary-code witnesses, so its slack occurs at most `N_{bar c}` times.  Hence the total source-slack contribution is at most

`N_{bar c} L_c`.

A fixed witness `w` of code `bar c` can be paired with at most the `n_c` A-sources of code `c`, so its slack occurs at most `n_c` times.  Summing over all A/U witnesses of code `bar c` gives at most

`n_c S_{bar c}`.

This proves `(AUC3)`.

### Corollary 4.2 (exact global scorecard capacity)

For `lambda>=0`,

> `M_AU`
>
> `<=sum_c min(`
>
> `     n_c N_{bar c},`
>
> `     [N_{bar c} L_c+n_c S_{bar c}]/(lambda+1))`.      `(AUC4)`

The first term is pair capacity; the second is scorecard capacity.  Keeping the minimum code by code is stronger than taking either global bound separately.

---

## 5. Coarse but useful overlap parameter form

Define

`mu_A=max_c n_c`,

`mu_V=max_c N_c=max_c(n_c+t_c)`.

Summing `(AUC3)` and using the two maxima gives

> `(lambda+1)M_AU`
>
> `<=mu_V L_A+mu_A(E_U+L_A)`
>
> `<= (mu_V+mu_A)(E_U+L_A)`.                              `(AUC5)`

Therefore an above-`M(n)` candidate satisfies, for `lambda>=0`,

> `M_AU<=((mu_V+mu_A) C_0)/(lambda+1)`.                  `(AUC6)`

This identifies the only way that a large A/U witness population can remain cheap: the graph must contain a **macroscopic Boolean code class** in `A` or `A union U`.

Notice that no clique assumption is used.  Large code multiplicity itself is not declared impossible; `(AUC6)` isolates it as the next structural obstruction.

---

## 6. Complete aggregate cylinder feasibility inequality

Return to any family `X` of beta-loaded centres and choose one repeated cylinder class `R_x` per centre as in the repaired cylinder theorem.

Put

`R_X=sum_{x in X}|R_x|`.

Every chosen criticality certificate lies in exactly one of two aggregate channels:

1. an A/U witness, counted by `M_AU(X)`;
2. an incoming matched-B foot, counted by `M_P(X)`.

Thus

> `R_X=M_AU(X)+M_P(X)`.                                   `(CF1)`

The matched-foot theorem from the preceding note gives, for `lambda>=0`,

> `M_P(X)<=M_P`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`,       `(CF2)`

where

`R_A(L_A)=max(2,floor((1+sqrt(1+4L_A))/2))`

and

`Delta_A=sum_{ {c,bar c} } |n_c-n_bar c|`.

The A/U channel obeys `(AUC4)`.  Therefore:

### Theorem 6.1 (complete witness-channel cylinder capacity)

For `lambda>=0`, every family `X` satisfies

> `R_X`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`
>
> `  +sum_c min(`
>
> `      n_c N_{bar c},`
>
> `      [N_{bar c}L_c+n_c S_{bar c}]/(lambda+1))`.      `(CFC)`

Since the cylinder theorem gives

> `|R_x|>=ceil((p-epsilon_x)_+/2^{k_x})`,

we obtain the exact low-deficit feasibility inequality

> `sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`
>
> `  +sum_c min(`
>
> `      n_c N_{bar c},`
>
> `      [N_{bar c}L_c+n_c S_{bar c}]/(lambda+1))`.      `(LDCF)`

This is the first aggregate cylinder inequality in the project in which **every critical-witness type is priced globally** after the repeated-code scope correction.

No witness channel has been silently dropped:

- matched-B feet are controlled by gamma collisions, self-pricing and complement polarization;
- outgoing A/U witnesses are included as complementary source/witness pairs;
- incoming A/U witnesses are included by the same pair rule, with arbitrary cross-centre witness reuse already allowed.

---

## 7. Coarse scorecard form and the new survivor obstruction

Replacing the codewise A/U term by `(AUC6)` gives the shorter necessary condition

> `sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`
>
> `  +((mu_V+mu_A)(E_U+L_A))/(lambda+1)`.                `(LDCF2)`

Above threshold one may replace `E_U+L_A` by `C_0`.

### Corollary 7.1 (linear-imbalance quadratic-cylinder trichotomy)

Consider a regime with

`a=O(p)`, `lambda+1=Theta(p)`, `C_0=O(p^2)`.

If a family of low-deficit centres has repeated-cylinder mass

`R_X=Omega(p^2)`,

then at least one of the following holds:

1. `L_A=Omega(p^2)`;
2. `mu_A=Omega(p)`;
3. `mu_V=Omega(p)`.

### Proof

If `L_A=o(p^2)`, matched-foot self-pricing gives `M_P=o(p^2)`.  If also `mu_A+mu_V=o(p)`, `(AUC6)` gives

`M_AU=o(p^2)`

because `C_0/(lambda+1)=O(p)`.  Then `(CF1)` gives `R_X=o(p^2)`, contradiction.

Thus a quadratic low-deficit cylinder population in the genuine linear-`lambda` regime can survive only by spending quadratic A-slack or by creating a **linear-sized Boolean code class**.

This is a sharper target than the previous generic request for an A/U overlap theorem.

---

## 8. Strategic consequence

The aggregate witness-overlap problem is now algebraically closed.  The local cylinder route has been reduced to one identifiable structural survivor:

> **macroscopic Boolean code concentration** in `A` or `A union U`.

The next compact theorem should therefore attack a code class of order `Omega(p)` directly.  Two existing facts look relevant:

1. same-code edges already have complementary unique-common-neighbour witnesses and same-code cliques pay `ceil(r(lambda+1)/2)` into the scorecard;
2. a large code class whose induced graph is sparse leaves many nonedges sharing all `p` matched neighbours, so D2C criticality of its incident edges and the surrounding cylinder structure may constrain how it can connect to complementary code classes.

The high-value next step is not another generic overlap count.  It is a **large-code-class structure theorem**: show that a linear A-code class either creates enough same-code edges/clique structure to spend the scorecard, or is sufficiently sparse/independent that the beta/source-tuple requirements cannot route through it at quadratic scale.

In parallel, the continuum `(CEIPM)` remains the independent global route for the linear-`lambda` parameter region.

---

## 9. Trust boundary

- Lemma 2.1 uses only the fact that a critical source/witness pair has singleton common neighbourhood.
- `(AUC1)--(AUC4)` are exact finite counts and the exact unique-common-neighbour slack inequality.
- The witness source always lies in `A` for both outgoing and incoming repeated-cylinder orientations; this is essential in the factor `n_c`.
- `(CFC)/(LDCF)` combine only already proved matched-foot capacity with the new A/U capacity; no repeated cylinder class is identified with its centre code.
- Corollary 7.1 is an asymptotic consequence of the finite inequalities and explicitly assumes the genuine linear-imbalance scale.
- The new reduction does not itself bound `mu_A` or `mu_V`; macroscopic code concentration is the surviving obstruction, not a closed case.
- No eventual or all-order second-extremal theorem is claimed.
- `X_3` has `u=0` and is untouched.
