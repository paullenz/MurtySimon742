# Two-X-hole branch — certificate-incidence and paired-hole strengthening

Date: 2026-09-20

Status: **same-session internal structural strengthening** of `SECOND_STRICT_TWO_X_HOLE_NORMAL_FORM.md`, conditional on the audited rigid one-code interface. No finite scan is used as proof. The zero-positive-rigid-cut caveat remains binding.

## 1. Setup

Work in the exact second-strict two-X-hole branch with `y>=2`, `x>=4`.

The predecessor proves

- `(h_X,h_o)=(2,0)`;
- the two buffer holes are `a_0,a_1`;
- `R=X\{a_0,a_1}`, `|R|=x-2`;
- every buffer edge `bx`, `x in R`, has an outside certificate `z in U_o` with
  `xz notin E`, `N(x) cap N(z)={b}`, `c(z)=bar c(x)`;
- every physical `z in U_o` is itself such a certificate for at least one head in R;
- complete-cut criticality saturates the common core: `g=0`, `k=x`, and the graph-fixed common-core head map
  `c_: X -> W_0`
  is a bijection, with `c_x x in E` and `c_x` adjacent to no other X-vertex.

Write `omega=|U_o|`.

The predecessor only used one chosen head for each outside vertex and obtained `H_core>=omega`. The full certificate incidence relation gives more.

## 2. Certificate incidence graph

Define a bipartite graph

> `J subseteq R x U_o`

by putting `xz in J` whenever z is used as a valid outside certificate for the buffer edge `bx`, i.e.

`xz notin E(G)`, `N(x) cap N(z)={b}`, `c(z)=bar c(x)`.

We may choose J so that every head has at least one certificate and every physical outside vertex retains at least one certificate supplied by `(2X-EVERY-UO-CERT)`.

Therefore

> `d_J(x)>=1` for every `x in R`,
>
> `d_J(z)>=1` for every `z in U_o`.                       `(J-NOISO)`

Put

> `L=|E(J)|`.

Then immediately

> **`L>=max(x-2,omega)`.**                                `(J-LOAD)`

This load is physical certificate traffic, not selected-source multiplicity in an abstract relaxation.

## 3. Every certificate incidence forces a distinct core--outside hole

Fix `xz in E(J)`. The core vertex `c_x` is adjacent to x. If `c_xz` were also an edge, then

`c_x in N(x) cap N(z)`

in addition to the required singleton head b, contradicting

`N(x) cap N(z)={b}`.

Hence

> `c_x z notin E(G)` for every `xz in E(J)`.              `(J-COREHOLE)`

The map

> `(x,z) -> (c_x,z)`

is injective because the core-head map `x -> c_x` is a bijection. Therefore

> **`H_core=e_bar(W_0,U_o)>=L>=max(x-2,omega)`.**         `(J-HCORE)`

The predecessor bound `H_core>=omega` is the special consequence obtained by forgetting the head side of J. `(J-HCORE)` is strictly stronger whenever `x-2>omega` and gains further strength if the actual certificate relation needs more than the minimum edge cover.

Using the exact common-core identity gives

> **`E_core>=x(p+x-1)+L`.**                              `(J-ECORE)`

## 4. Per-witness double self-pricing

For `z in U_o`, put

> `r_z=d_J(z)>=1`.

The r_z certified heads are distinct X-nonneighbours of z. By `(J-COREHOLE)`, z also misses the r_z distinct corresponding core vertices.

Every outside vertex is Y-anticomplete in this branch. To maximize `d(z)` subject only to these forced holes, allow z every other possible neighbour:

- the root;
- exactly one endpoint in each of the p tight matched fibres;
- all X except its r_z certified heads;
- all U-vertices except the r_z forced core holes.

Since the maximum-degree root has degree `2p+u`, this yields

`d(z)<=1+p+(x-r_z)+(u-1-r_z)`

and therefore

> **`epsilon_z>=p-x+2r_z`.**                             `(J-ZPAY0)`

Slack is nonnegative, so the useful form is

> **`epsilon_z>=[p-x+2r_z]_+`.**                         `(J-ZPAY)`

Summing over U_o,

> `E(U_o)>=sum_z [p-x+2r_z]_+`
>
> `       >=[omega(p-x)+2L]_+`.                          `(J-UOPAY)`

The second line uses `sum [q_z]_+ >= [sum q_z]_+` and `sum r_z=L`.

This is a genuine paired-hole effect: each certificate head costs z once in A and once again at the head's graph-fixed common-core vertex.

## 5. Strengthened rooted U-edge ceiling

`U_-=W_0 dotcup {b}` is independent and has size x+1. The only possible U-edges are therefore

- inside U_o;
- across `U_- -- U_o`.

There are exactly L distinct forced cross nonedges from `(J-COREHOLE)`. Hence

> `q<=binom(omega,2)+(x+1)omega-L`.                      `(J-Q)`

Equivalently,

> `q<=binom(u,2)-binom(x+1,2)-L`.

Again the predecessor's `-omega` correction is recovered by replacing L by its weaker lower bound omega.

## 6. Code-class decomposition of the incidence graph

Certificate localization gives

> `c(z)=bar c(x)`

for every incidence `xz in J`.

Thus J decomposes into disjoint complementary-code blocks. Let C run over the represented head codes in R and put

- `n_C=|R cap A_C|`;
- `m_C=|U_o cap B_{bar C}|`;
- `L_C=|E(J) cap (A_C x B_{bar C})|`.

Because every head and every outside vertex is incident,

> `n_C,m_C>=1`,
>
> `L_C>=max(n_C,m_C)`,
>
> `sum_C n_C=x-2`,
>
> `sum_C m_C=omega`,
>
> `L=sum_C L_C`.                                         `(J-CLASS)`

Consequently

> `L>=sum_C max(n_C,m_C)`
>
> ` =(x-2+omega+sum_C |n_C-m_C|)/2`.                    `(J-IMBAL)`

This exposes a new **class-imbalance surcharge**. Reusing witnesses heavily in a large head class or carrying many physical witnesses for a small head class cannot be hidden by the global `max(x-2,omega)` relaxation; it creates extra located core--outside holes and outside slack through L.

This is the right interface to the exact aligned-code / pair-local capacity machinery, because `n_C` and `m_C` are code-class populations rather than anonymous scalar traffic.

## 7. Pair-local consequence

In the core-saturated branch `g_P=0` for the outside pair `P={d,bar d}`. The physical score sitting in P already contains

- the common-core bill `x(p+x-1)+L`;
- buffer slack `p+2`;
- the Y-side d-code slack.

Thus any future use of `Ccap_P/(ONE-P)/(CROWD)` should carry L **inside the local P score**, not only in a global total-score floor. The class decomposition `(J-CLASS)/(J-IMBAL)` supplies the matching outside-class populations needed to prevent unrelated slack from paying this bill.

No pair-capacity claim is promoted here; this section records the exact resource placement for the next attack.

## 8. Diagnostic status and next move

A coarse score/rooted replay using only `(J-HCORE)`, `(J-UOPAY)` and `(J-Q)` still has unbounded abstract survivor families. That is expected: the two-foot support geometry and class allocation have not yet been used.

The next high-value theorem should therefore stay structural:

1. combine the two-foot routing normal form with `(J-CLASS)` to classify the possible represented head codes C relative to the two hole codes;
2. use same-code criticality to bound `n_C,m_C,L_C` for each allowed foot pattern;
3. only then apply exact pair-local capacity with the local L surcharge.

Do not replace L by `max(x-2,omega)` before that geometry is extracted.