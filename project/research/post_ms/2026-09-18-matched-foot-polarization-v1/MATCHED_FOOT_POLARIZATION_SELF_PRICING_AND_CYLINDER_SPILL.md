# Matched-foot polarization, self-pricing, and aggregate cylinder spill

**Status:** internal structural theorem package, 18 September 2026.

This note continues `MATCHED_FOOT_COLLISION_CAPACITY.md` after the repaired beta-cylinder localisation.  The purpose is to make the exceptional matched-B escape **scorecard-aware** rather than merely cap it by `sigma_0 a`.

The main conclusions are:

1. a large matched-foot population forces a large gamma-collision class, and therefore quadratically prices itself into `L_A`;
2. using both endpoints of one tight fibre as matched feet is directly expensive in `L_A`;
3. after grouping gamma codes into complementary pairs, the total matched-foot traffic is controlled by the **complement-majority mass** of the A-code distribution plus a two-sided-traffic slack term; and
4. every family of low-deficit beta cylinders therefore has an exact lower bound on the amount of criticality that must spill into A/U witness channels.

These are finite hand inequalities.  They do not close the near-full branch and they do not touch the published order-12, size-32 `X_3` graph, which has `u=0`.

---

## 1. Setup and preserved input

Use the live notation from `CURRENT_STATE.md`.

For a matched endpoint `w=q_i^s`, let `gamma(w)` be its row-complement source code and let `t_w` be the number of incoming repeated-cylinder certifications using `w` as the matched-B critical foot.

Write

`g_c=|{w:gamma(w)=c}|`,

`mu_gamma=max_c g_c`,

`M_P=sum_w t_w`.

The previous matched-foot theorem gives

> `t_w<=n_{gamma(w)}`,                                    `(P1)`

where `n_c` is the number of A-vertices of code `c`, and every gamma-collision class is a switchable zero-signed matched subcore.  Hence

> `M_P<=mu_gamma a<=sigma_0 a`.                           `(P2)`

It also gives the weighted form

> `sum_i(t_i^0 epsilon_i^1+t_i^1 epsilon_i^0)`
>
> `<=mu_gamma L_A<=sigma_0 L_A`,                          `(P3)`

with

> `epsilon_i^0+epsilon_i^1=lambda+1`.                     `(P4)`

Finally, opposite endpoints have complementary gamma codes:

> `gamma(q_i^1)=bar gamma(q_i^0)`.                        `(P5)`

The preserved zero-signed-subcore theorem says that any switchable zero-signed subcore of order `s>=3` forces

> `L_A>=s(s-1)`.                                          `(ZS)`

---

## 2. Matched-foot escape prices itself quadratically

The old capacity `(P2)` can be inverted before replacing `mu_gamma` by the coarser parameter `sigma_0`.

### Theorem 2.1 (matched-foot self-pricing)

Put

> `m=ceil(M_P/a)`.

If `m>=3`, then

> `L_A>=m(m-1)`.                                          `(MSP1)`

Equivalently, for every value of `L_A`, define

> `R_A(L_A)=max(2,floor((1+sqrt(1+4L_A))/2))`.

Then

> `mu_gamma<=R_A(L_A)`,                                   `(MSP2)`

and therefore

> `M_P<=a R_A(L_A)`.                                      `(MSP3)`

### Proof

From `(P2)`,

`M_P<=mu_gamma a`,

so

`mu_gamma>=ceil(M_P/a)=m`.

If `m>=3`, the largest gamma-collision class contains a switchable zero-signed subcore on at least `m` fibres.  `(ZS)` gives

`L_A>=mu_gamma(mu_gamma-1)>=m(m-1)`.

Conversely, if `mu_gamma<=2`, then `mu_gamma<=R_A(L_A)` by definition.  If `mu_gamma>=3`, `(ZS)` gives

`mu_gamma(mu_gamma-1)<=L_A`,

which is exactly

`mu_gamma<=floor((1+sqrt(1+4L_A))/2)`.

Substitution into `(P2)` gives `(MSP3)`.

### Corollary 2.2 (quadratic matched escape costs quadratic scorecard)

Whenever `M_P>2a`,

> `L_A >= ceil(M_P/a)(ceil(M_P/a)-1)`.                    `(MSP4)`

In particular, if `a=O(p)` and `M_P=Omega(p^2)`, then necessarily

> `L_A=Omega(p^2)`.

Conversely, if `a=O(p)` and `L_A=o(p^2)`, then

> `M_P=o(p^2)`.                                           `(MSP5)`

Thus the earlier `O(p^{3/2})` bound in the `L_A=O(p)` regime is one instance of a broader principle: **subquadratic A-slack forbids a quadratic matched-B escape**.

---

## 3. Two-sided traffic in one fibre is expensive

The paired weighted inequality `(P3)` contains a useful term that was not previously extracted.

### Lemma 3.1 (paired cross-slack inequality)

For every tight fibre `i`,

> `t_i^0 epsilon_i^1+t_i^1 epsilon_i^0`
>
> `>=(lambda+1) min(t_i^0,t_i^1)`.                        `(PT1)`

### Proof

Assume without loss that `t_i^0>=t_i^1`.  Then

`t_i^0 epsilon_i^1+t_i^1 epsilon_i^0`

`=t_i^1(epsilon_i^0+epsilon_i^1)+(t_i^0-t_i^1)epsilon_i^1`

`>=t_i^1(lambda+1)`.

The other ordering is symmetric.

Summing and using `(P3)` gives:

### Theorem 3.2 (matched-foot traffic polarization)

> `(lambda+1) sum_i min(t_i^0,t_i^1)<=mu_gamma L_A`.      `(PT2)`

For `lambda>=0`, if

`D_t=sum_i |t_i^0-t_i^1|`,

then, since

`M_P-D_t=2 sum_i min(t_i^0,t_i^1)`,

> `M_P-D_t <= 2 mu_gamma L_A/(lambda+1)`.                 `(PT3)`

Hence low A-slack forces almost all matched-foot traffic to be **fibrewise one-sided**.  The matched-B escape cannot be simultaneously large and balanced between the two endpoints of many tight fibres.

---

## 4. Complement-pair capacity

The fibrewise polarization has a global code-theoretic consequence because opposite matched endpoints have complementary gamma codes.

Partition the Boolean code space into unordered complementary pairs

`Pi={c,bar c}`.

For such a pair define

`I_Pi={i:{gamma(q_i^0),gamma(q_i^1)}=Pi}`,

`g_Pi=|I_Pi|`,

and let `M_Pi` be the total matched-foot traffic on endpoints of fibres in `I_Pi`.

By `(P5)`, every tight fibre belongs to exactly one such `Pi`.  Moreover each fibre in `I_Pi` contributes one endpoint with gamma code `c` and one with gamma code `bar c`.  Hence both gamma-collision classes have size `g_Pi`, so

> `g_Pi<=mu_gamma`.                                       `(CP1)`

Put

> `a_pm=sum_{Pi={c,bar c}} max(n_c,n_bar c)`
>
> `=(a+Delta_A)/2`,                                       `(CP2)`

where

> `Delta_A=sum_{Pi={c,bar c}} |n_c-n_bar c|`.             `(CP3)`

Thus `a/2<=a_pm<=a`; it measures the complement-majority mass of the A-code distribution.

### Lemma 4.1 (one complementary gamma pair)

For every complementary pair `Pi`,

> `M_Pi`
>
> `<=g_Pi max(n_c,n_bar c)`
>
> `  +sum_{i in I_Pi} min(t_i^0,t_i^1)`.                 `(CP4)`

### Proof

In each fibre `i in I_Pi`, one endpoint has gamma code `c`, the other has gamma code `bar c`.  By `(P1)` their loads are at most `n_c` and `n_bar c`, respectively.  Therefore

`t_i^0+t_i^1`

`=max(t_i^0,t_i^1)+min(t_i^0,t_i^1)`

`<=max(n_c,n_bar c)+min(t_i^0,t_i^1)`.

Sum over `I_Pi`.

Summing `(CP4)`, using `(CP1)` and `(PT2)`, gives the main result.

### Theorem 4.2 (complement-majority matched-foot capacity)

For `lambda>=0`,

> `M_P<=mu_gamma[a_pm+L_A/(lambda+1)]`.                   `(CP5)`

Together with the old `M_P<=mu_gamma a`,

> `M_P<=mu_gamma min(a,a_pm+L_A/(lambda+1))`.             `(CP6)`

Using `(MSP2)` eliminates the switching parameter completely:

> `M_P`
>
> `<=R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1))`.      `(CP7)`

This is a finite scorecard-aware capacity theorem for the complete matched-B cylinder escape.

### Corollary 4.3 (near-maximal matched escape forces complement polarization)

Rearranging `(CP5)` gives

> `Delta_A`
>
> `>= 2M_P/mu_gamma-a-2L_A/(lambda+1)`,                   `(CP8)`

whenever the right side is positive.

Thus a matched-foot population close to the old `mu_gamma a` cap is possible only if the A-layer itself is strongly one-sided across complementary Boolean code pairs, unless `L_A` is already large.

Equivalently, the traffic excess over pure complement-majority capacity is directly priced:

> `L_A >= ((lambda+1)/mu_gamma)[M_P-mu_gamma a_pm]_+`.    `(CP9)`

This is the precise tradeoff: **dispersion over both endpoints pays A-slack; avoiding that payment forces complement polarization in A**.

---

## 5. Exact aggregate spill from low-deficit cylinders

Let `X` be any family of beta-loaded centres.  For each `x in X`, choose one repeated A-code class `R_x subseteq N_A(x)` supplied by the repaired cylinder theorem, and choose one criticality certificate for every edge `xz`, `z in R_x`.

Write

`R_X=sum_{x in X}|R_x|`.

Decompose each chosen certificate into:

- an outgoing A/U witness;
- an incoming A/U witness; or
- an incoming matched-B foot.

Let `M_AU(X)` be the total number of chosen certifications in the first two channels, counted with multiplicity over centres, and `M_P(X)` the matched-B part.  Then exactly

> `R_X=M_AU(X)+M_P(X)`,                                   `(CS1)`

and trivially

> `M_P(X)<=M_P`.                                          `(CS2)`

The repaired cylinder multiplicity theorem gives

> `|R_x|>=ceil((p-epsilon_x)_+/2^{k_x})`,                 `(CS3)`

where `k_x=p-ell_x`.

Combining `(CS1)--(CS3)` with `(CP7)` gives:

### Theorem 5.1 (scorecard-aware aggregate cylinder spill)

For `lambda>=0`, every family `X` satisfies

> `M_AU(X)`
>
> `>= [ sum_{x in X} ceil((p-epsilon_x)_+/2^{k_x})`
>
> `     -R_A(L_A) min(a,(a+Delta_A)/2+L_A/(lambda+1)) ]_+`. `(CS4)`

This is the desired exact bridge from the finite source-deficit staircase to the A/U criticality channels.  It is valid for arbitrary repeated cylinder code; no assumption `c(R_x)=c(x)` is used.

### Corollary 5.2 (quadratic-cylinder dichotomy)

Suppose `a=O(p)` and a family of low-deficit centres has

> `R_X=Omega(p^2)`.

Then either

> `M_AU(X)=Omega(p^2)`,

or

> `L_A=Omega(p^2)`.                                       `(CS5)`

### Proof

If `M_AU(X)` is not quadratic, `(CS1)` forces `M_P=Omega(p^2)`.  Corollary 2.2 then gives `L_A=Omega(p^2)`.

Thus a quadratic repeated-cylinder population can no longer disappear into the matched-B exception without itself exhausting a quadratic amount of the A-side scorecard.

---

## 6. Why this is the useful next reduction

Before this note, the corrected cylinder programme had one unresolved aggregate escape: many low-deficit centres might send their repeated-class critical edges to matched-B feet, avoiding the A/U witness machinery.

That escape now has three nested controls:

1. **self-pricing:** `M_P` forces `L_A` quadratically through the largest gamma-collision class;
2. **fibre polarization:** two-sided matched-foot traffic pays `(lambda+1)` per paired unit into the weighted A-slack budget;
3. **complement capacity:** polarized traffic can remain cheap only by concentrating on the majority A-code in each complementary pair.

Consequently `(CS4)` is the correct next interface with the source-tuple staircase.  The remaining local task is no longer to control matched-B feet.  It is to price the forced `M_AU(X)` channel, using the already preserved facts:

- outgoing A/U witnesses are distinct inside one repeated class;
- incoming A/U reuse creates same-code source blocks;
- same-code cliques pay directly into `E_U+L_A`;
- common-foot concentration obeys the quadratic hole/clique bound.

A successful A/U overlap theorem would therefore combine with `(CS4)` without any remaining unpriced critical-witness type.

---

## 7. Trust boundary

- `(MSP1)--(MSP4)` use only the existing matched-foot source-capacity theorem and the hand-proved zero-signed-subcore payment.  The special `max(2,...)` in `R_A` is necessary because the zero-signed payment was proved for subcores of order at least three.
- `(PT1)--(PT3)` are exact algebra from the paired endpoint-slack identity and the existing weighted matched-foot theorem.
- `(CP1)--(CP9)` use only the exact opposite-endpoint complement identity for `gamma`, source uniqueness `t_w<=n_gamma(w)`, and `(PT2)`.
- `(CS4)` is an exact counting consequence of the repaired cylinder decomposition and does not identify the repeated class code with the centre code.
- The asymptotic statements in Corollaries 2.2 and 5.2 are consequences of the finite inequalities, not scan-derived claims.
- The accompanying checker audits the new finite algebra only; it is not part of the proof.
- No global eventual second-extremal theorem is claimed.
- The published `X_3` negative control has `u=0` and is untouched.
