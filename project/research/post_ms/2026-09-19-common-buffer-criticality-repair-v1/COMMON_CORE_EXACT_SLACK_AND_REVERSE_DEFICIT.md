# Common-core exact slack and reverse-deficit stability

Date: 2026-09-19

Status: structural strengthening of the repaired unloaded common-buffer `z=1` branch. This note supersedes the **numerical core floor only** (`E_core>=k(p+k-2)`) by an exact identity. The older floor remains true but is not sharp in the unloaded common-buffer geometry. No eventual theorem is claimed.

## 1. Reassessment

The previous repair corrected the buffer--X criticality orientation and then kept the predecessor common-core floor

`E_core>=k(p+k-2)`.

A direct degree recount of a common-core witness shows that this floor left one full unit per core witness unused. This is not a change of hypotheses: throughout the unloaded common-buffer model

- `W_0` has k vertices;
- every `w in W_0` is used as a crossing witness by every source in Y;
- `X--Y` is complete;
- `e(G[U_-])=0`, where `U_-=W_0 dotcup {b}`;
- `U_o=U\U_-`, `u_o=u-k-1`.

The correction is therefore upstream of the scalar score arithmetic and must be inserted before more local-pair optimization.

## 2. Structural unit I: the core head map is injective

Fix `w in W_0` and a source `s in Y`. Since w is a selected crossing witness, for its selected crossing head `h_s(w) in X` one has

`N(s) cap N(w)={h_s(w)}`.

Every vertex of X is adjacent to s. Hence w can have **at most one** X-neighbour. It has at least the selected head, so

> `d_X(w)=1`.                                              `(2.1)`

The unique X-neighbour is independent of s; denote it by `h(w)`.

For a fixed source s, the k selected U-witnesses in W0 certify k distinct crossing edges, so their heads are distinct. Therefore

> `h:W_0 -> X` is injective.                               `(2.2)`

Write

`H_0=h(W_0)`, so `|H_0|=k`.

Also every core witness is nonadjacent to every source using it, hence

> `d_Y(w)=0`.                                              `(2.3)`

These are graph facts, not selected-incidence multiplicity claims.

## 3. Structural unit II: exact common-core slack identity

For `w in W_0`, put

`h_w := u_o-d_{U_o}(w)`,

the number of missing `w--U_o` edges.

A U-vertex satisfies

`d_{A union U}(w)=p+u-1-epsilon_w`.

By `(2.1)`, `(2.3)`, and `e(G[U_-])=0`,

`d_{A union U}(w)=1+d_{U_o}(w)`.

Therefore

> `epsilon_w=p+k-1+h_w`.                                  `(3.1)`

Summing over the k core vertices gives the exact identity

> `E_core=k(p+k-1)+H_core`,                               `(3.2)`

where

`H_core := e_bar(W_0,U_o)=sum_w h_w`.

Consequences:

> `E_core>=k(p+k-1)`,                                     `(3.3)`

with equality iff

> `W_0--U_o` is complete.                                 `(3.4)`

Thus the predecessor `k(p+k-2)` floor was safe but one unit per core vertex too weak in the unloaded model.

The same identity holds for every r in the unloaded common-buffer source-edge theorem; it is not restricted to `r=0`.

## 4. Structural unit III: zero-buffer reverse-head deficit

Now specialize to the repaired `r=0`, zero-buffer-slack branch:

`g=p`, `k=x-p>0`, `epsilon_b=0`.

Every `b--x` edge lies in a triangle. The corrected reverse orientation B uses a matched endpoint of gamma code `bar d`. There are p such endpoints, and each can have at most one singleton X-head. Let

`R_B subseteq X`

be the set of X-heads admitting such a reverse certificate, and put

> `r_B=|R_B|<=p`,
>
> `d:=p-r_B>=0`.                                          `(4.1)`

Every x outside `R_B` must use corrected Orientation A. Since `g=p`, no matched Orientation-A foot has an X-code, so every such edge requires an outside witness in `U_o`. Therefore

> `ell>=x-r_B=k+d`.                                       `(4.2)`

This sharpens the previous `ell>=k` statement by recording unused reverse matched capacity.

## 5. Structural unit IV: core heads force core--outside holes

Take `x=h(w) in H_0` which is not in `R_B`. Its buffer edge must use an outside witness z with

`N(x) cap N(z)={b}`.

But w is adjacent to x. Therefore w cannot be adjacent to z, or w would be a second common neighbour. Thus every core head outside `R_B` creates a physical missing edge in `W_0--U_o`.

The pairs are distinct because the core head map h is injective. Hence

> `H_core>=|H_0\R_B|`
> ` >= [k-r_B]_+`
> ` = [k-p+d]_+`.                                        `(5.1)`

Combining with `(3.2)`,

> `E_core`
> ` >= k(p+k-1)+[k-p+d]_+`.                              `(5.2)`

In particular, even with all p reverse slots used (`d=0`),

> `E_core>=k(p+k-1)+(k-p)_+`.                            `(5.3)`

So if `k>p`, literal core completeness to `U_o` is impossible in the zero-buffer branch.

## 6. Structural unit V: reverse deficit also raises outside-witness demand

Use the aligned-code cap from the repaired note. Put

`R_A=floor(R_code(C0)/2)`

for an above-threshold candidate. A fixed outside witness serves only one X-code class, so at most `R_A` X-sources can reuse it. From `(4.2)`, the number m of distinct outside witnesses satisfies

> `m>=ceil((k+d)/R_A)`.                                  `(6.1)`

Each is anticomplete to Y, so

> `H_Y>=y m`.                                              `(6.2)`

The exact r=0 source slack therefore gives

> `L_Y>=y(1+m)`.                                          `(6.3)`

The reverse deficit d is thus monotone-costly in three separate physical ledgers:

1. it raises outside source incidence `ell` by d;
2. it can force extra `W_0--U_o` holes through `(5.1)`;
3. it weakly raises the distinct outside-witness count m and therefore Y-holes.

## 7. Structural unit VI: sharpened zero-buffer score floor

Let

`m_d=ceil((k+d)/R_A)`.

Ignoring only the nonnegative outside-witness slack itself, `(5.2)` and `(6.3)` give

> `S`
> ` >= k(p+k-1)+[k-p+d]_+`
> `    +max{phi(p), y(1+m_d)}`.                           `(7.1)`

The right side is nondecreasing in d. Therefore the cheapest reverse geometry occurs at

> `d=0`, i.e. `r_B=p`.                                    `(7.2)`

So every near-minimal zero-buffer survivor is driven toward **saturation of all p reverse gamma-`bar d` matched endpoints by distinct X-heads**.

At d=0 the safe floor is

> `S`
> ` >= k(p+k-1)+(k-p)_+`
> `    +max{phi(p), y(1+ceil(k/R_A))}`.                   `(7.3)`

This replaces the older zero-buffer scalar floor in subsequent work.

## 8. Structural unit VII: sharpened rooted residual floor

The physical A--U hole argument from the repair note becomes, using `(4.2)`,

`Z>=k(a-1)+y+ym+ell`.

Hence

> `Z>=ka+y(1+m)+d`.                                       `(8.1)`

At the cheapest witness count `m_d`, put

`D_d=ka+y(1+m_d)+d-u(p-lambda)`.

With

`E0_d=k(p+k-1)+[k-p+d]_+`,

the exact integer residual minimization gives

> `q+E_U`
> ` >= E0_d+ceil([D_d-E0_d]_+/2)`.                       `(8.2)`

Again the d=0 geometry is the cheapest scalar possibility. Any unused reverse matched slot directly worsens the residual ledger.

## 9. Structural unit VIII: equality partition at d=0

There is a second graph-fixed head partition already present in the crossing layer.

For each of the p gamma-d matched endpoints used by every Y-source, completeness of `X--Y` forces that matched endpoint to have a unique X-neighbour. The p selected matched witnesses for a fixed source certify p distinct crossing heads. Together with the k injective core heads, they cover all x=p+k vertices of X.

Thus X has a graph-fixed disjoint partition

> `X=H_M dotcup H_0`,
>
> `|H_M|=p`, `|H_0|=k`,                                  `(9.1)`

where `H_M` is the matched-crossing head set and `H_0` the core-head set.

If d=0 and `H_core=0`, then every core head must lie in `R_B`, by `(5.1)`. Consequently `k<=p`, and the k outside-certified heads `X\R_B` lie entirely in `H_M`.

So exact cheapest geometry forces:

1. all p reverse gamma-`bar d` endpoints to have distinct singleton X-heads;
2. all k core heads to be among those reverse heads;
3. all k compulsory outside-certified buffer edges to lie in the matched-crossing head set `H_M`;
4. `W_0--U_o` complete.

For `k>p`, item 2 is impossible; the precise replacement is the mandatory core-hole bill `(k-p)_+`.

This head-partition geometry is the next object for direct D2C criticality analysis.

## 10. Diagnostic impact

The companion checker repeats the same coarse parameter box as the preceding common-buffer diagnostics.

Using only the exact `+1` per core witness in `(3.3)` throughout the unloaded common-buffer branch reduces abstract common-buffer survivor states from

> `64,892` to `64,159`,

excluding 733 states.

Combining that exact core floor with the already-repaired zero-buffer outside-witness Y-hole floor and the new reverse-head surcharge `(5.3)` gives

> `64,079`

abstract common-buffer survivor states, 813 fewer than the predecessor `64,892` and 788 fewer than the immediately preceding repaired common-buffer diagnostic (`64,867`).

The full-support comparator remains contained in this sharpened common-buffer survivor set on the same coarse existential parameter grid, so the z=1 support union is also `64,079` there.

Within the zero-buffer g=p branch alone, 17,174 predecessor abstract branches passed the old floor. The exact core floor plus repaired outside-witness geometry rejects 594; adding the core-head surcharge raises that to 644, leaving 16,530. These are parameter-branch counts, not graph counts.

## 11. Trust boundary and next move

- `(3.1)--(3.2)` are exact degree identities from the already-proved singleton-head property and `e(G[U_-])=0`.
- The injectivity of h is selected-edge bookkeeping for a fixed source plus graph-fixed singleton neighbourhood; no cross-source witness injectivity is assumed.
- `(5.1)` counts literal missing `W_0--U_o` edges and does not identify witness incidences with physical obligations.
- The reverse-deficit parameter d uses only the p physical gamma-`bar d` endpoints and their graph-fixed singleton heads.
- Diagnostics are arithmetic support only.

Next: attack the cheapest d=0 head-partition geometry directly. In particular test whether a reverse gamma-`bar d` head in `H_0` and an outside-certified head in `H_M` can coexist with `W_0--U_o` completeness and the tight-pair adjacency pattern. Keep exact local `Ccap_P`, directed A/U capacity and the residual floor active; do not jump to z=2.