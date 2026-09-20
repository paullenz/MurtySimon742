# Rigid Hall cuts — global gamma-budget witness theorem

Date: 2026-09-20

Status: **same-session structural strengthening** conditional on the exact rigid Hall event `M_X=E_X=0`, with `x=|A_X|>=3`. It is independent of realizability of that event and therefore does not remove the zero-positive-fixture caveat.

This note strengthens the earlier rigid witness-deficit theorem by retaining the *source-code-specific* matched-foot budget instead of replacing it immediately by the coarse global bound `mu_X<=p`.

## 1. Setup

Assume a rigid complete Hall cut

`A=A_X dotcup Y`, `x=|A_X|>=3`, `y=|Y|`,

with every crossing edge selected with source in Y. The direct audit in `RIGID_SINGLETON_HEAD_DIRECT_AUDIT.md` independently proves that every source `s in Y` needs `x` distinct physical singleton-head witnesses and that every such witness lies in a tight matched endpoint or in U.

For a tight matched endpoint w, let `gamma(w)` be its source code. A matched witness used by a source s satisfies

`gamma(w)=c(s)`.

For an unordered complementary code pair `P={d,bar d}`, let `g_P` be the number of tight fibres whose two gamma codes form P. Then:

1. for a source of code d, there are exactly `g_P` matched endpoints with gamma code d;
2. every tight fibre has one complementary gamma pair, so

> `sum_P g_P=p`.                                          `(GB-0)`

Let D be the set of distinct source codes represented in Y, let `h=|D|`, and write `y_d=|Y_d|` for `d in D`. For each d let `P(d)={d,bar d}` and put

> `k_d:=[x-g_{P(d)}]_+`.                                  `(GB-1)`

## 2. Code-specific U-witness population

Fix one source s of code d. It needs x distinct singleton-head witnesses. At most `g_{P(d)}` of them can be matched endpoints, because those are all the matched endpoints with gamma d. Therefore at least `k_d` are U-witnesses.

Every such U-witness must have code `bar d`, by the raw tight-coordinate argument in the direct audit. Hence

> `|U_bar d|>=k_d`                                        `(GB-2)`

for every represented source code d.

Distinct source codes have distinct complementary U-code classes. Consequently the witness populations are physically disjoint and

> **`u>=K:=sum_{d in D} k_d`.**                           `(GB-3)`

This is stronger than applying only the uniform coarse matched-singleton bound when the represented source codes have small pair-local gamma budgets.

## 3. Global gamma budget

A complementary source-code pair P can contribute at most two represented codes to D. Therefore

`sum_{d in D} g_{P(d)}`
` =sum_P r_P g_P`,

where `r_P in {0,1,2}` is the number of the two codes in P represented in Y. Using `(GB-0)`,

> `sum_{d in D} g_{P(d)} <= 2p`.                          `(GB-4)`

Since `sum [z_i]_+ >= [sum z_i]_+`, `(GB-1)`--`(GB-4)` give

> `K >= [h x-2p]_+`.                                      `(GB-5)`

Together with `u>=K`, this yields the compact diversity obstruction

> **`h x <= u+2p`.**                                      `(GB-6)`

This is unconditional within the rigid event, including the regime `x<=p` where the older bound `h(x-p)_+<=u` is silent.

If Y represents at most one code from each complementary pair, then `r_P<=1`, so `(GB-4)` improves to `sum_d g_{P(d)}<=p` and

> **`h x <= u+p`.**                                       `(GB-7)`

For h=1, the exact statement `u>=x-g_P` should of course be retained rather than the relaxed `(GB-6)`.

## 4. Refined physical A--U deficit

For each d choose the union `W_d subseteq U_bar d` of U-witnesses used by all sources of code d. Put `m_d=|W_d|`; then `m_d>=k_d`.

Every used U-witness has exactly one A_X-neighbour. Because the W_d are disjoint across d,

> `Z_X >= (x-1)K`.                                        `(GB-ZX)`

Each source of code d uses at least `k_d` distinct U-witnesses and is nonadjacent to each of them. Hence

> `Z_Y >= sum_d y_d k_d`.                                 `(GB-ZY)`

Therefore

> **`Z>= (x-1)K+sum_d y_d k_d`.**                         `(GB-Z)`

The earlier uniform-k theorem is recovered by replacing every `k_d` by a common lower bound; `(GB-Z)` preserves strictly more local information.

## 5. Refined U-slack price

Put

`g0=x-T0=p-y`.

For `w in W_d`, let `t_w` be the number of d-coded sources that use w. The raw singleton-head degree count gives

`epsilon_w >= [g0+t_w-1]_+`,

with

`sum_{w in W_d} t_w >= y_d k_d`.

If `g0>=1`, then

`sum_{w in W_d} epsilon_w`
` >= (g0-1)m_d+sum_w t_w`
` >= k_d(g0-1+y_d)`.

Summing over source codes gives the refined floor

> **`E_U >= sum_d k_d(y_d+g0-1)`** for `g0>=1`.            `(GB-EU+)`

If `g0<=1`, set `c=1-g0`. Convex truncation within each complementary U-code class gives

`E(U_bar d) >= [y_d k_d-c |U_bar d|]_+`.

Summing and using `sum_d |U_bar d|<=u` gives the safe aggregate form

> **`E_U >= [sum_d y_d k_d-(1-g0)u]_+`.**                 `(GB-EU-)`

These estimates retain source multiplicity and pair-local gamma scarcity simultaneously.

## 6. Why this matters for the zero-fixture question

The bounded graph regression has not realized a rigid complete Hall cut with x>=3. The direct audit shows that this is not because the elementary singleton-head implication was misstated. The present theorem adds a more global necessary geometry:

- every represented outside source code consumes a distinct complementary U-code population;
- the total matched-foot relief available to *all* represented source codes is at most `2p`;
- consequently `h x<=u+2p`;
- and the same code-specific populations create located A--U nonedges and U-slack through `(GB-Z)` and `(GB-EU+)`/`(GB-EU-)`.

The next useful reachability attack is to combine these exact code-specific bills with the rooted identity

`Z=u(p-lambda)+2q+E_U`

and with the pair-local Hall/score constraints before aggregating to a total score. If that conjunction excludes all parameter regimes that can reach a rigid cut, the empirical zero-fixture phenomenon would become a theorem rather than a coverage gap.