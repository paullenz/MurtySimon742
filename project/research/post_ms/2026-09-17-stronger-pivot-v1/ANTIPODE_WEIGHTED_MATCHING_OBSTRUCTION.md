# Obstruction to an ABE-only weighted antipode-matching argument

18 September 2026. Research directed by Paul Lenz; analysis by ChatGPT/Geeps.

**Status: methodological obstruction, not a graph construction and not a theorem about D2C realisability.** The purpose of this note is to prevent the next attack from over-reading `ANTIPODE_BRANCHING_ERROR_PAYMENT.md`.

The antipode branching-error theorem gives, at every antipode-graph vertex `w`,

`3 sum_{e incident w} eta(e) >= d_J(w)(d_J(w)-1)`.       `(ABE)`

It is tempting to try to feed this directly into `(AMC)` by proving that a matching captures a large fraction of the total antipode error or of the vertices covered by errorful antipodes. The local inequality alone is not strong enough for such a conclusion at the scale one would want.

## Abstract star obstruction

Consider the abstract weighted graph

`J=K_{1,4}`

and assign

`eta(e)=1`

to all four edges.

At the centre,

`3 sum eta = 3*4 = 12 = 4*3 = d(d-1)`,

so `(ABE)` is attained exactly. At every leaf the right-hand side is zero. Thus this weighted graph satisfies all of the local ABE inequalities.

But every matching has only one edge. Hence

- the total antipode error is `4`;
- the maximum matching captures eta-weight only `1`;
- five vertices are incident with errorful edges, but a maximum matching covers only two of them.

Therefore **ABE by itself cannot justify a strong near-perfect weighted matching extraction**. Any argument that tries to convert the quadratic local error curvature directly into `(AMC)` must use additional D2C structure beyond the inequalities already recorded.

In particular, the useful extra information now available is precisely the near-full partial-Boolean system:

- unmatched vertices carry Boolean transversals;
- their antipodes are complementary/special-code constrained;
- their P--U selected obligations form the row-singleton systems `Psi(K_y)`;
- selected obligations have per-source Hall capacities.

These should be combined with ABE rather than discarded in favour of a purely abstract weighted-graph lemma.

## Regression comment

A direct scan of all D2C graph-atlas classes through order seven and every root found **no realised antipode centre of degree four whose four incident antipode errors are all one**. Thus `K_{1,4}` above is currently only a numerical obstruction to an ABE-only deduction, not a known D2C counterexample to a stronger theorem.

That distinction is important: additional D2C/Boolean constraints may well exclude the abstract star pattern in the eventual near-full regime.

## Strategic consequence

The preferred next line is now the augmented-Hall route. For each unmatched `y`, first price the local row-singleton cover `Psi(K_y)`.

- Generic `tau(Psi(K_y))>=2` should create repeated A-code/capacity pressure when many unmatched vertices are present.
- The only `tau=1` local patterns are `K_p` and `K_{p-1} dotcup K_1` by `UNMATCHED_ROW_SINGLETON_COVER.md`; these force, respectively, a large B-clique or a complementary U--U antipode.

Only after exploiting that extra structure should ABE/AMC be used to charge the remaining errorful antipode graph.
