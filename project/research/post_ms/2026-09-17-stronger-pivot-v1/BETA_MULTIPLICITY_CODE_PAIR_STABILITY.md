# Beta multiplicity and complementary-code-pair stability

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural theorems; external mathematical and novelty review remain open. This note continues the near-full tight-antipode programme. It does not assume the false all-order 2019 Dailly--Foucaud--Hansberg strengthening. The published order-12/32 `X_3` graph remains a mandatory negative control in the already-closed full-tight `u=0` branch.

The purpose here is to make the unmatched-row Hall system genuinely multiplicative. The previous row-cover results used only whether an A-code exists. For a whole U-code class, however, the same row obligation repeats once for every vertex of the class. D2C criticality makes the beta witnesses injective at each matched target, so A-code **multiplicity** must pay for those repetitions.

Throughout use the near-full notation from `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`:

- `P_i={u_i,w_i}`, `1<=i<=p`, are the tight antipode pairs;
- `P=union_i P_i` and `U=B\P`, `|U|=u`;
- `A=V(G)\N[v]`, `|A|=a`;
- every vertex of `A union U` has a partial Boolean code in `{0,1}^p`;
- `n_d=|{x in A:c(x)=d}|`;
- `mu_alpha=max_d |alpha^{-1}(d)|`, the switching true-twin invariant.

For a U-code `c`, write

`t_c=|{y in U:c(y)=c}|`.

For every coordinate `i`, all vertices of that class choose the same matched endpoint; call it `q_i(c) in P_i`. Put

`a_i(c)=alpha(q_i(c))`,

`b_i(c)=beta_i(c)=bar c Delta {i}`.

Thus the `t_c` physical edges `y q_i(c)` all have the same two possible witness codes `{a_i(c),b_i(c)}`.

---

## 1. Beta-target injectivity

The old per-source Hall rule says that among obligations oriented from a fixed matched source `q`, at most `n_{alpha(q)}` can use the alpha code. There is a dual injectivity on the beta side which is stronger than mere support.

Take a P--U edge `yq` and suppose its selected criticality witness is beta-oriented from the unmatched endpoint. In G-language the witness `x in A` satisfies

- `x~y`;
- `x not~q`;
- `N(x) cap N(q)={y}`.

Now fix the matched target `q`. If the same `x` beta-certified two distinct edges `yq` and `zq`, then both `y` and `z` would lie in `N(x) cap N(q)`, contradicting the displayed uniqueness condition.

Therefore:

> **BETA-TARGET INJECTIVITY.** For a fixed matched endpoint `q`, distinct beta-oriented P--U obligations incident with `q` use distinct A-witness vertices.

For one U-code class and one coordinate this gives a multiplicity inequality. Let `h_i(c)` be the number of the `t_c` obligations oriented to the alpha code. Then

`h_i(c)<=n_{a_i(c)}`

by the old per-source rule, while beta-target injectivity gives

`t_c-h_i(c)<=n_{b_i(c)}`.

Hence

> **MULTIPLICITY ROW-EDGE INEQUALITY**
>
> `t_c <= n_{a_i(c)}+n_{b_i(c)}` for every occupied code `c` and every `i`.       (1.1)

This is strictly stronger than the statement that the realised A-code set covers the row edge.

### Matching consequence inside one row

Let `nu_c` be the matching number of the row-singleton graph `Psi(K_c)`. Sum (1.1) over a matching of `nu_c` pairwise code-disjoint row edges. Every A-code multiplicity is then counted at most once, so

> `nu_c t_c <= a`.                                            (1.2)

Thus

> `t_c <= floor(a/nu_c)`.                                     (1.3)

For every graph, the endpoints of a maximal matching form a vertex cover, so `tau(Psi(K_c))<=2nu_c`. Therefore

> `t_c <= floor( a / ceil(tau(Psi(K_c))/2) )`.                 (1.4)

Combining with the preserved high-complexity row bound

`tau(Psi(K_c)) >= ceil(p/(R_*+1))`

shows that, in an above-threshold candidate,

> `t_c <= floor( a / ceil( ceil(p/(R_*+1))/2 ) )`.             (1.5)

For fixed `lambda` and `u=O(p)`, one has `R_*=O(sqrt(p))`, so every individual U-code class has size `O(sqrt(p))`.

This is a multiplicity theorem, not a support count.

---

## 2. Complementary-pair multiplicity cap

The row systems for complementary U-codes have an exact symmetry.

If `bar c` is the complement of `c`, then

- `K_bar c=K_c`, because complementing all selected fibre endpoints preserves each 2-lift matching relation;
- `q_i(bar c)` is the tight mate of `q_i(c)`;
- `alpha(q_i(bar c))=bar(alpha(q_i(c)))`;
- the beta pools `B(c)={bar c Delta {i}:i in [p]}` and `B(bar c)` are disjoint for `p>=3`.

Sum (1.1) over all coordinates for both sides of one complement pair `gamma={c,bar c}`. Across the two sides, the alpha endpoints run through both physical endpoints of every tight fibre. Hence the total alpha multiplicity appearing in the sum is at most

`W_alpha=sum_{q in P} n_{alpha(q)} <= mu_alpha a`.

The `2p` beta codes in `B(c) union B(bar c)` are all distinct, so their total A-multiplicity is at most `a`.

Consequently, with

`T_gamma=t_c+t_bar c`,

we obtain

> **COMPLEMENTARY-PAIR MASS CAP**
>
> `p T_gamma <= (mu_alpha+1)a`.                         (2.1)

Equivalently,

> `T_gamma <= floor((mu_alpha+1)a/p)`.                  (2.2)

In the above-threshold high-complexity regime, the preserved alpha-cap theorem gives `mu_alpha<=R_*`, so

> `T_gamma <= floor((R_*+1)a/p)=O(sqrt(p))`             (2.3)

whenever `u=O(p)` and `lambda` is fixed.

Thus even a complementary pair of U-code classes cannot absorb a linear fraction of U.

---

## 3. Global beta-pool proliferation

The complementary-pair cap is local. There is also a global consequence of the beta demand.

Let `H` be the set of occupied complementary code pairs and put `h=|H|`. For `gamma={c,bar c}` define its beta union

`S_gamma=B(c) union B(bar c)`.

By beta-target injectivity, the number of beta-oriented obligations sourced from `gamma` is at most

`N_gamma=sum_{d in S_gamma} n_d`.                       (3.1)

Globally, the preserved alpha-spill theorem gives

`B_beta >= pu-W_alpha >= pu-mu_alpha a`.                (3.2)

Now use an exact hypercube incidence fact. For any A-code `d`,

`d in B(c)` iff `c` is a Hamming neighbour of `bar d`.

There are exactly `p` such `c`, and for `p>=3` no complementary pair contains two of them. Therefore **every Boolean code belongs to exactly p complementary-pair beta unions `S_gamma`** over the full cube. In particular, over only the `h` occupied pairs it belongs to at most `min(h,p)` such unions.

Hence

`sum_{gamma in H} N_gamma <= min(h,p)a`.                (3.3)

Combining (3.1)--(3.3) yields

> **BETA-POOL PROLIFERATION THEOREM**
>
> `min(h,p)a >= pu-mu_alpha a`.                         (3.4)

In particular

> `h >= max(0, ceil(pu/a-mu_alpha))`.                   (3.5)

For an above-threshold candidate, `mu_alpha<=R_*`, so

> `h >= max(0, ceil(pu/a-R_*))`.                        (3.6)

If `u=cp+O(1)` with fixed `c>0` and fixed `lambda`, then

`a=(2+c)p+O(1)`

and `R_*=O(sqrt(p))`. Therefore

> `h >= (c/(2+c))p-O(sqrt(p))`.                         (3.7)

So a linear unmatched layer cannot be hidden in a bounded or square-root number of Boolean code types. It forces **linearly many complementary code-pair types**.

This is the first aggregate Hall consequence in the high-complexity regime that scales linearly with `p`.

---

## 4. The Boolean fan theorem also prices matched antipode hubs

`BOOLEAN_ANTIPODE_FAN_PAYMENT.md` was stated for unmatched hubs. Its proof in fact has a wider partial-Boolean form.

Let `z in B` be any antipode hub and let `Y subseteq U` be a set of unmatched antipode partners of `z` which all have the same partial Boolean code. Put `d=|Y|`.

Any two members of `Y` share a matched neighbour in a tight fibre. Therefore, for an edge `yy'` inside `G[Y]`, the criticality witness for `yy'` cannot be another member of `Y`; exactly the same injective external-hole charge used in the original BAF proof applies. Nonedges in `Y` again consume two hole incidences.

Thus:

> **PARTIAL-BOOLEAN FAN PAYMENT**
>
> `sum_{y in Y} eta(yz) >= binom(d,2)+bar e(G[Y])`.     (4.1)

This includes the old U--U fan theorem, but it also applies when `z` is a matched endpoint. In the latter case every unmatched antipode partner automatically has the single special code `alpha(z)`, so the hypothesis is automatic.

A finite graph-atlas replay of the genuinely new matched-hub case is recorded by the companion checker. It is only regression evidence; (4.1) follows by the hand injection above.

---

## 5. One-sided U-code classes pay matched-hub curvature

Consider a complementary code pair `gamma={c,bar c}` with

`t_c=t>0`, `t_bar c=0`.

A U--U antipode of a vertex of code `c` would have code `bar c`, which is absent. Hence every vertex in the class must use a matched antipode.

Let

`R_c={q in P:alpha(q)=c}`,

`r_c=|R_c|`.

If `r_c=0`, such a one-sided class is impossible. Otherwise assign each `y` of code `c` to one matched antipode `q in R_c`; let `d_q` be the number assigned to `q`. Then

`sum_q d_q=t`.

For a matched antipode `yq`, the preserved identity gives

`eta(yq)=epsilon_y-epsilon_{q'}`,

where `q'` is the tight mate of `q`. Applying (4.1) to the assigned partner set of each hub gives

`sum_{y assigned to q} epsilon_y`

` >= binom(d_q,2)+bar e(G[Y_q])+d_q epsilon_{q'}`

` >= binom(d_q,2)`.                                    (5.1)

Also every such matched antipode is errorful, so `epsilon_y>=1` for every vertex in the one-sided class. Therefore, if

`E_c=sum_{y:c(y)=c} epsilon_y`,

then

> `E_c >= max( t, sum_{q in R_c} binom(d_q,2) )`.       (5.2)

Convexity gives a parameter-only form. If `t=r_c k+s` with `0<=s<r_c`, then the minimum possible quadratic term is

`Phi(t,r_c)=r_c binom(k,2)+s k`.                        (5.3)

Hence

> `E_c >= max(t,Phi(t,r_c))`.                          (5.4)

Since `r_c<=mu_alpha`, a convenient coarse consequence is

> `E_c >= max( t, ceil((t^2/mu_alpha-t)/2) )`           (5.5)

when `mu_alpha>0`.

Thus one-sided code concentration is doubly expensive: it has no zero-slack vertices at all, and concentration beyond the available alpha hubs incurs quadratic branching slack.

---

## 6. Generic complementary pairs pay imbalance slack at lambda=-1

There is a complementary statement for a code pair with **no matched antipode eligibility**.

For a complement pair `gamma={c,bar c}`, let

`r_gamma=|alpha^{-1}(c)|=|alpha^{-1}(bar c)|`.

(The equality follows because tight mates map alpha codes to complements.) Suppose `r_gamma=0`. Then every unmatched vertex in either side has no matched antipode candidate. By the no-private-foot theorem it must therefore have a U--U antipode in the opposite code class. In particular, if one side is occupied, so is the other.

Now specialise to the hardest degree layer `lambda=-1`. Write

`t=t_c`, `s=t_bar c`,

`E_c=sum_{y:c(y)=c} epsilon_y`,

`E_bar=sum_{z:c(z)=bar c} epsilon_z`.

A zero-slack vertex in the c-side must be assigned to a positive-slack antipode hub in the bar-c side: two zero-slack U vertices would have `eta=0` by the antipode slack identity and hence would form a tight pair, contrary to their membership in U.

If a bar-c hub has slack `e`, then the Boolean fan bound gives capacity at most `2e+1` for assigned zero-slack c-partners. Summing over positive hubs and using

`# positive bar-c vertices <= E_bar`

gives

`# zero c-vertices <= 3E_bar`.

The positive c-vertices themselves number at most `E_c`. Hence

> `t <= E_c+3E_bar`.                                    (6.1)

Symmetrically,

> `s <= 3E_c+E_bar`.                                    (6.2)

Adding and weakening each separately yields the clean pairwise lower bound

> **GENERIC-PAIR IMBALANCE PAYMENT, lambda=-1**
>
> `E_c+E_bar >= ceil( max( (t+s)/4, t/3, s/3 ) )`.      (6.3)

The first term recovers the old `1/4` fan floor on a balanced complementary pair. The `t/3` or `s/3` term is strictly stronger when one side is sufficiently imbalanced.

Thus low slack in the hardest layer forces generic complementary code pairs to be approximately balanced; heavily one-sided behaviour is available only through the exceptional alpha-image pairs, where Section 5 prices matched-hub branching instead.

---

## 7. Strategic consequence

The high-complexity unmatched regime is now constrained simultaneously in four directions.

1. **No heavy exact code class:** row matching plus multiplicity gives `t_c=O(sqrt(p))` when `u=O(p)`.
2. **No heavy complementary pair:** `(2.3)` gives `t_c+t_bar c=O(sqrt(p))`.
3. **Linear U forces linear code-pair diversity:** `(3.7)` gives `h=Omega(p)` when `u=Theta(p)`.
4. **Antipode escape is priced:** one-sided alpha-image classes pay matched-hub curvature, while non-alpha complementary pairs must occur on both sides and pay the imbalance bound `(6.3)` at `lambda=-1`.

This changes the remaining obstruction. A putative large counterexample can no longer concentrate its unmatched layer in a few reusable Boolean rows. In the linear-unmatched regime it must distribute U across linearly many complementary Hamming types while keeping each type small, and it must simultaneously arrange enough alpha eligibility or sufficiently balanced U--U antipode pairs to avoid the new slack charges.

The next high-value target is to combine this **linear code-pair proliferation** with D2C edge-criticality among the corresponding U vertices. Many distinct U-code types have large common matched neighbourhoods unless their Hamming distances are large; pricing U--U edges/nonedges across a linear family should be capable of producing the missing linear contribution to `E_U+L_A` in the exact `(GS-A)` budget.

No eventual second-extremal theorem is claimed here.