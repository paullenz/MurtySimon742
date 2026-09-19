# Exact outside-unmatched balance in the forced-omitted-nonedge full-support branch

Date: 2026-09-19

Status: internal hand corollary of `OMITTED_PAIR_NONEDGE_FORCING.md` and the preserved rooted identities. This remains conditional on the rigid one-code full-support hypotheses and is not an eventual theorem.

## 1. Purpose

After raw criticality forces `nu=y`, the remaining correction variables in the minimal `z=1`, `h=0` full-support branch are not independent. The previous ledger still treated

`H_X,H_Y,M,q,Q_rest,E_o`

as partly separate. The foundational tight-pair identity

`Q=p(p+u-1)+q`

shows that `q` is exactly the number of edges in the unmatched B-layer U. Combining that with `e(U_-)=0` collapses the outside layer to a vertexwise degree identity.

The result is a more compact structural normal form suitable for external review.

## 2. Setup

Retain:

- `U_-=U_{bar d}`, `|U_-|=k+1`;
- `U_o=U\U_-`, `u_o=|U_o|=u-k-1`;
- `H_X` and `H_Y` = A--`U_o` nonedges from X and Y;
- `H=H_X+H_Y`;
- `M=(k+1)u_o-e(U_-,U_o)`;
- `Q_o=e(G[U_o])`;
- `E_o=sum_{z in U_o} epsilon_z`;
- `B=(k+1)(p+k-1)`.

The forced omitted-nonedge theorem gives

`nu=y`,

and therefore

`E_-=B+M`.

## 3. Structural unit I — q is exact unmatched internal edge count

The preserved rooted-triangle decomposition is

> `Q=p(p+u-1)+q`.                                         `(3.1)`

On the other hand the tight-fibre baseline gives

> `Q=p(p-1)+pu+e(G[U])`.                                  `(3.2)`

The first two terms on the right of `(3.2)` equal `p(p+u-1)`. Hence

### Lemma 3.1

> `q=e(G[U])`.                                             `(3.3)`

Since source visibility proves `e(G[U_-])=0`,

> `q=e(U_-,U_o)+Q_o`
> ` =(k+1)u_o-M+Q_o`.                                     `(3.4)`

Thus q is no longer a free residual variable in this branch.

## 4. Structural unit II — exact local outside-U balance

Fix `z in U_o`. Define

- `h_z=a-d_A(z)`, the number of A-nonneighbours of z;
- `m_z=(k+1)-d_{U_-}(z)`, the number of missing edges from z to `U_-`;
- `d_o(z)=d_{G[U_o]}(z)`.

Every unmatched B-vertex has exactly p neighbours in the matched tight-fibre layer. Therefore its maximum-degree slack is

`epsilon_z`
` =b-[1+p+d_A(z)+d_{U_-}(z)+d_o(z)]`,

where the 1 is the root neighbour and `b=2p+u`.

Substituting `a=2p+u-lambda-1` and `|U_-|=k+1` gives the exact vertexwise identity

> `h_z+m_z`
> ` = (p+k+1-lambda)+d_o(z)+epsilon_z`.                   `(4.1)`

Put

> `C_out:=p+k+1-lambda`.                                  `(4.2)`

Then every outside unmatched vertex must pay its baseline `C_out`, plus one further A/U_- defect for each internal `U_o` neighbour, plus its own degree slack.

This is a physical incidence identity, not a Hall or selected-witness count.

## 5. Structural unit III — exact summed correction identity

Summing `(4.1)` over `U_o` gives

`sum h_z=H`,

`sum m_z=M`,

`sum d_o(z)=2Q_o`,

and `sum epsilon_z=E_o`. Therefore

### Theorem 5.1 — outside-U correction balance

> `H+M=u_o C_out+2Q_o+E_o`.                               `(5.1)`

Equivalently,

> `E_o=H+M-2Q_o-u_o(p+k+1-lambda)`.                       `(5.2)`

Since `E_o>=0`,

> `H+M>=u_o(p+k+1-lambda)+2Q_o`                           `(5.3)`

whenever the right side is positive; `(5.1)` remains exact without a sign assumption on `C_out`.

The principal conceptual point is that the outside A-holes H, missing `U_- -- U_o` edges M, internal outside edges `Q_o`, and outside slack `E_o` are one ledger, not four independent resources.

## 6. Structural unit IV — exact q+E_U and 2q+E_U forms

Using

`E_U=E_-+E_o=B+M+E_o`

and `(3.4)`,

### Corollary 6.1

> `q+E_U`
> ` =B+(k+1)u_o+Q_o+E_o`.                                `(6.1)`

The missing-edge variable M cancels exactly.

Likewise

> `2q+E_U`
> ` =B+2(k+1)u_o-M+2Q_o+E_o`.                            `(6.2)`

Substituting `(5.2)` into `(6.2)` yields

> `2q+E_U`
> ` =B+2(k+1)u_o-u_o C_out+H`.

The right side simplifies to the already-preserved forced-nu residual identity

> `2q+E_U=D0+H`,                                          `(6.3)`

so the new local balance independently reconciles the rooted residual bookkeeping. This is a useful consistency check: the global residual equation and the direct outside-U degree sum are the same physical conservation law in different coordinates.

## 7. Structural unit V — score floor with the outside slack restored

The previous score bound used only `E_U>=E_-=B+M`. We now retain the exact outside contribution.

The forced omitted-nonedge theorem gives

> `L_Y=y(p-g+1)+H_Y`.                                     `(7.1)`

The independent gamma-collision floor gives `L_A>=phi(g)`. Hence

### Theorem 7.1 — outside-aware full-support score floor

> `S=L_A+E_U`
> ` >=B+M+E_o`
> `   +max{phi(g), y(p-g+1)+H_Y}`.                        `(7.2)`

Using `(5.1)` one may equivalently write

> `S`
> ` >=B+H+2M-2Q_o-u_o C_out`
> `   +max{phi(g), y(p-g+1)+H_Y}`.                        `(7.3)`

The first form `(7.2)` is normally safer because every displayed term outside the max is manifestly nonnegative except none; the second form is useful for exact optimization over the physical correction ledger.

Since `g<=p`, equation `(7.1)` also gives the simple universal surcharge

> `L_Y>=y`.                                                `(7.4)`

Thus each outside source pays at least one unit of A-slack in addition to the exact U_- floor B.

## 8. Structural unit VI — corrected rooted triangle/slack invariant

From `(3.2)` and `E_-=B+M`,

`Q+E_-`
` =p(p+u-1)+[(k+1)u_o-M+Q_o]+B+M`.

Hence

> `Q+E_-`
> ` =p(p+u-1)+B+(k+1)u_o+Q_o`.                           `(8.1)`

This is the same invariant obtained in the predecessor note after explicitly removing the forced tight-fibre baseline from `Q_rest`, now written directly in the canonical q-coordinate.

## 9. Equality geometry

The exact local identity `(4.1)` makes equality cases concrete.

If an outside vertex has zero slack, then

> `h_z+m_z=C_out+d_o(z)`.                                 `(9.1)`

If it is also isolated inside `U_o`, it must have exactly `C_out` combined missing incidences into `A union U_-`.

If `C_out>0`, no outside vertex can be simultaneously complete to A, complete to `U_-`, and zero-slack. If `C_out` is large, the outside layer necessarily carries a correspondingly large physical hole/missing-edge budget before any internal `U_o` edges are allowed.

If `C_out<=0`, this particular baseline does not by itself force defects; the exact identity should then be retained rather than relaxed.

## 10. Negative control and trust boundary

`X_3` has `u=0`; the present `U_o` balance is inactive on its canonical root.

No source-tuple premise is used here. The proof uses only the tight-fibre edge baseline, the already-established full-support sterility `e(U_-)=0`, the forced omitted-nonedge theorem, and direct degree sums. The graph-level regression coverage caveat for the rigid `x>=3` conjunction remains unchanged.

## 11. Forward use

The next full-support calculation should no longer optimize independently over `q,M,H,Q_rest,E_o`. Use instead the exact coordinates

`H_X,H_Y,M,Q_o,E_o`

subject to `(5.1)`, with q reconstructed by `(3.4)`. In particular, the exact pair bill and `(CROWD)` should be intersected with `(7.2)` rather than the older `B+M+max(...)` floor that discarded `E_o`.
