# Missing-pair cancellation: exact residual condition

21 September 2026. Rigorous reduction plus finite-model audit; the final structural inequality remains open.

Let `R=P0`, `T=P1`, and let `S` be the four-centre star population. Retain `M=rq-e(R,T)` and `I=e(R)+e(T)`. For a star vertex `x`, its bridge degree is its number of `T` neighbours plus its number of different-centre star neighbours.

Create one **hard obligation** for every `R--S` edge and for every `T--S` edge whose star endpoint has bridge degree at least two. Join an obligation to an unoccupied missing `R--T` pair when that pair is a valid raw criticality certificate for the obligation: its unique common A-neighbour is the incident star. Raw edge criticality makes every hard obligation incident with at least one such pair. Let `nu` be the maximum matching size in this obligation--pair graph and put

    h = (# hard obligations)-nu.

Let `L` be the number of low-bridge `T--S` edges plus `e(S)`. The star-forest theorem injects all these bucket edges into distinct physical star vertices, so `L<=s`.

## Cancellation criterion

If

    h <= s-L,

then

    e(R union T union S) <= rq+s.

Indeed, match `nu` hard edges to distinct unoccupied missing pairs. The remaining `h` hard edges cost at most the `h` unused star tokens. The low-bridge and star edges use the `L` occupied tokens. Hence all parity-star and star edges number at most `(M-I)+s`; after adding parity edges `rq-M+I`, the total is at most `rq+s`.

This is sharper than the previous unconditional `rq+M+s-I` ledger. Its only missing theorem is the displayed deficiency inequality. It does not assume that all hard obligations inject into missing pairs; that tempting stronger statement is false even in equality fixtures.

## Hostile replay on exact optima

For all seven exact MaxSAT optima in `PARITY_STAR_MAXSAT_GRID.json`, the checker obtains:

- six cases: `h=1`, `L=7`, `s-L=1`;
- the `(r,q)=(3,3)` case: `h=0`, `L=8`, `s-L=0`.

Thus every optimum satisfies the cancellation criterion exactly and hence explains `e(A)=rq+14` after the six coordinate edges. In particular, the repeated `h=1` cases refute the simpler proposed proof that hard obligations always have a saturating matching. The next theorem target is now precise: prove `h+L<=s` from raw star-centre criticality, or find an actual graph violating it.
