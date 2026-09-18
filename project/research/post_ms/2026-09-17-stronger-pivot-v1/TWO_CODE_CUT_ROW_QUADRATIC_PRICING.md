# Complete-bipartite two-code rows also force quadratic A-slack

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural corollary; not externally reviewed.** This note pushes the one-code global-collapse argument through the first of the three exact `tau<=2` row kernels.

## 1. Sign graph of a fixed unmatched row

Fix `y in U` and label each tight fibre so that `y` selects `q_i`. Let

`L_y=bar K_y`.

For each fibre pair `i,j`, the edge `ij` belongs to `L_y` exactly when the selected-selected edge `q_iq_j` is **absent**, equivalently when the matched 2-lift uses the crossed rather than parallel matching relative to these labels.

Thus `L_y` is literally the sign graph of the matched 2-lift in the coordinate system centred at `y`.

Switching the labels in a coordinate set `S subseteq [p]` toggles precisely the cut `delta(S)` of this sign graph.

## 2. Complete-bipartite complement is a pure cut

The exact two-code row classification says that one possible `tau(Psi(K_y))<=2` family is

`L_y=K_{R,[p]\R}`

for some `R subseteq [p]`, including the empty degeneration.

But

`K_{R,[p]\R}=delta(R)`.

Switch every fibre indexed by `R`. This toggles exactly the whole sign graph and leaves no crossed fibre pair.

Therefore:

> **CUT-ROW GLOBAL COLLAPSE THEOREM.** If an unmatched row has complete-bipartite complement
>
> `L_y=bar K_y`,
>
> then the full matched 2-lift is switching-equivalent to
>
> `K_p dotcup K_p`.                                             `(CB1)`

This strictly extends the one-code theorem: `L_y=empty` and a spanning star are boundary cases, but every complete bipartite `K_{r,p-r}` is covered.

## 3. Quadratic A-side pricing

Once `(CB1)` holds, the matched orientation graph is the two-clique singleton/co-singleton graph and the edge-by-edge private-foot theorem applies exactly as in `MATCHED_PRIVATE_FOOT_SLACK_AND_COMPLETE_ROW_QUADRATIC_EXCLUSION.md`.

Hence:

> **COMPLETE-BIPARTITE ROW QUADRATIC SLACK.** If some unmatched row satisfies
>
> `bar K_y` complete bipartite,
>
> then
>
> `L_A>=p(p-1)`.                                                `(CB2)`

The same exact second-extremal exclusion region follows. With

`c_lambda=ceil(lambda(lambda+2)/2)`,

if

> `(lambda+2)u <= p^2-(lambda+4)p+c_lambda+3`,                  `(CB3)`

then `m<=M(n)`.

Thus, inside `(CB3)`, an above-threshold configuration cannot use **any** row from the complete-bipartite-complement branch of the exact `tau<=2` classification.

## 4. What remains of tau<=2

The exact two-code classification had three complement families:

1. complete bipartite;
2. star plus isolated vertices;
3. two-centre leaf graph, with optional centre edge.

Family 1 is now quadratically priced by `(CB2)`.

For family 2, if the star has `r` leaves and `s=p-1-r` isolates, switching the centre converts the sign graph to the complementary star with `s` leaves. Hence its best immediate signing normal form is a star with

`min(r,s)`

crossed fibre pairs. This may grow with `p`, so fixed-defect closure cannot simply be invoked.

Family 3 similarly has a bounded kernel but need not be a cut. It remains the genuinely new two-code frontier.

The next useful target is therefore no longer all `tau<=2` rows. It is specifically the **star-plus-isolates and two-centre sign kernels**, with the aim of extracting either a large matched clique whose critical edges can be A-slack-priced, or a complementary U-antipode/fan payment.

The order-12/size-32 hostile control is full-tight (`u=0`) and is unaffected.
