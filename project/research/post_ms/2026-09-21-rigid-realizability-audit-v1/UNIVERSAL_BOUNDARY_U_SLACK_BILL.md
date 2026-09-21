# Universal boundary coordinates force an unmatched-witness slack bill

Date: 2026-09-21

Status: raw-to-ledger consequence of the boundary-code-edge trichotomy in the rigid complete one-code branch. It is upstream of the later half-ray H--U analysis and does not use the superseded private-foot route.

## 1. Setup

Assume the rigid complete cut `X--Y` with one outside code

`Y=A_d`, `|Y|=y`, `|X|=x`.

Use

`C=C(d,X)={i: every x in X has c(x)_i=d_i}`

for the universal-agreement coordinates.

For `i in C`, reverse boundary certificates are impossible: the forced reverse code `gamma(q_i^{d_i})` has bit `1-d_i` at coordinate i, while every X-code has bit `d_i`.

Let

`L_C={i in C: there exists j in C with N_{R_d}(j)={i}}`

be the universal heads that have even a possible matched-forward leaf witness.

Put

`C_U=C\L_C`, `r_U=|C_U|`.

For every `i in C_U` and every `y0 in Y`, the edge `y0 q_i^{d_i}` must therefore use the **U-forward** arm of the boundary trichotomy.

## 2. Slack of one unmatched boundary witness

Fix `i in C_U`. Let `W_i` be the union of unmatched witnesses actually used by the `y` boundary edges at coordinate i. Every `w in W_i` has

- `c(w)=bar d xor e_i`;
- `N_X(w)=empty`.

Let `t_w` be the number of outside sources `y0 in Y` for which `w` is used at coordinate i. Then `w` is nonadjacent to those `t_w` sources as well.

The exact U-degree identity is

`d_{A union U}(w)=p+u-1-epsilon_w`.

On the other hand, because w has no X-neighbour, at most `y-t_w` neighbours in Y, and at most `u-1` neighbours in U,

`d_{A union U}(w) <= y-t_w+u-1`.

Hence

`epsilon_w >= p-y+t_w`.                                  `(2.1)`

This is one unit stronger than the familiar complete-cut singleton-head witness inequality, because the present boundary witness has **zero** X-neighbours rather than one.

Summing over `W_i` and using

`sum_{w in W_i} t_w >= y`

gives

`sum_{w in W_i} epsilon_w >= (p-y)|W_i|+y`.               `(2.2)`

The code classes `bar d xor e_i` are distinct for distinct coordinates i, so the sets `W_i` are disjoint.

## 3. Universal-coordinate U-slack theorem

### Theorem 3.1

If `p>=y`, every universal coordinate without matched-leaf support costs at least p units of U-slack:

`sum_{w in W_i} epsilon_w >= p`.

Consequently

`E_U >= p r_U`.                                           `(3.1)`

More precisely, without assuming `p>=y`,

`E_U >= sum_{i in C_U} [y+(p-y)|W_i|]`,                  `(3.2)`

with `|W_i|>=1` and pairwise-disjoint witness sets.

### Proof

When `p>=y`, the right side of `(2.2)` is minimized at `|W_i|=1`, giving p. Distinct coordinates use disjoint U-code classes, so the costs add. `square`

### Corollary 3.2 — score-limited universal exposure

For an above-threshold candidate with the preserved total U-slack ceiling

`E_U<=C0`,

one necessarily has

`r_U <= floor(C0/p)`                                      `(3.3)`

whenever `p>=y`.

This is stronger than the mere population statement `r_U<=u`: even one available unmatched witness does not make an uncovered universal coordinate free.

## 4. Half-ray specialization

On the corrected diagnostic half-ray

`p=2t`, `y=t`,

so every universal coordinate not supplied by a matched leaf costs at least

`2t`

units of U-slack. Thus

`E_U >= 2t r_U`.                                          `(4.1)`

Any survivor with a linear number of such coordinates therefore pays a quadratic score before the later H--U residual-slot machinery is used.

The cheap alternative is now explicit: most universal coordinates must be organised into the degree-one matched-leaf geometry of `R_d`. That geometry is itself rigid (and becomes a perfect matching when `u=0`), giving a concrete next raw-criticality target rather than another free scalar parameter.

## 5. Audit boundary

This theorem concerns the **realizability** of the rigid complete cut. It does not prove that such a cut occurs in an actual D2C graph. The current bounded graph-level corpus still contains zero positive rigid complete pair-family cuts with `x>=3`; this remains the dominant upstream caveat.
