# The RTS triangle expands to a locally saturated two-pair bow-tie

21 September 2026. Raw local obstruction in the four-centre parity-plane branch.

Let `r in R=P0`, `t in T=P1`, and `x in S` span an `RTS` triangle. Criticality of `rx` gives a vertex `t' in T`, distinct from `t`, such that

    rt' is missing,  xt' is present,
    N_A(r) intersect N_A(t')={x}.             (1)

Now `x` has the two antipode bridges `t,t'`, so `tx` is not first-kind. Its second-kind certificate gives `r' in R`, distinct from `r`, with

    r't is missing,  r'x is present,
    N_A(r') intersect N_A(t)={x}.             (2)

Thus every RTS triangle contains the four-arm bow-tie on `r,r',t,t',x`, with present edge `rt` and crossed missing pairs `rt'`, `r't`.

This expansion is locally saturated: (1) simultaneously certifies both arms `rx` and `xt'`, while (2) simultaneously certifies `tx` and `r'x`. Hence raw edge criticality of the four arms does **not** force a third missing pair or another physical vertex. The two unoccupied pairs pay for exactly four parity--star incidences, attaining the capacity-two accounting in `PARITY_STAR_MISSING_PAIR_LEDGER.md`.

This blocks the tempting next inference that an RTS triangle automatically replicates beyond its two-pair toll. Any stronger loss must instead use one of:

1. criticality of the present edge `rt` in the surrounding Q3 skeleton;
2. the status of the fourth cross pair `r't'`;
3. star centre-spoke obligations outside these four arms; or
4. competition with coordinate--P0 certificates.

No claim is made that the five-vertex bow-tie alone extends to a D2C graph. The statement is only that the local arm certificates close exactly and therefore cannot support an unconditional third-pair argument.
