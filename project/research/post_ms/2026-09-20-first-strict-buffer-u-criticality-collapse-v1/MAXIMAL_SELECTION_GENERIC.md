# Generic maximal-witness normalization in the first-strict branch

Date: 2026-09-20

Status: internal conditional representative-selection lemma. This strengthens the all-F-specific observation in `MAXIMAL_OUTSIDE_WITNESS_SELECTION.md` and uses only the generic reverse-fan theorem.

## Theorem

In the first-strict unloaded unique-hole branch, choose one valid outside-U certificate for each buffer edge `bx`, `x in X'=X\{a_0}`, so as to maximize the number m of distinct physical outside witnesses used. Then

> `m=1  =>  |U_o|=1`.                                   `(MAX-GEN)`

### Proof

For every physical `w in U_o`, `BUFFER_UO_REVERSE_FAN.md` gives at least one `x_w in X'` with

`wx_w notin E`, `bw in E`, `N(w) cap N(x_w)={b}`.

Thus w is a valid outside-U certificate for the buffer edge `b x_w`.

Suppose a maximal representative system has `m=1`, with sole selected witness z, but `|U_o|>=2`. Because every one of the `|X'|=x-1>=2` buffer edges has a selected outside witness and m=1, z certifies every `b x`, `x in X'`.

Choose `w!=z` in U_o. Use w instead of z for `b x_w`. Choose any other head `x'!=x_w` and retain z for `b x'`. This is a valid representative system using two distinct physical outside witnesses, contradicting maximality.

Therefore `|U_o|=1`. `square`

## Consequences

Since `|U_o|=u-k-1=T+1`, maximal selection gives

> `m=1  =>  T=0, u=k+2`.

This conclusion is **independent of the F/R polarization** and therefore sits upstream of the later one-witness split. It uses no raw-witness uniqueness; on the contrary it exploits the audited freedom of selected representatives.

A graph with `|U_o|>=2` may still have a non-maximal chosen system with m=1, so earlier m=1 algebra remains formally correct for that choice. For graph-level case partitioning, however, such a graph belongs to the `m>=2` branch once representatives are chosen maximally.

The next adversarial audit should verify that every downstream selected-system theorem used after this normalization is invariant under changing valid representatives. The P2 premise is already explicitly a selected-representative statement, so no contradiction with the audited source-tuple semantics is apparent.
