# Exact triangle taxonomy in the four-centre parity/star block

21 September 2026. Raw-criticality consequence at Q3 parity-plane scope.

Write `R=P0`, `T=P1`, and let `S` be the physical star set. Call a missing `R--T` pair **occupied** when it receives the parity-substitution charge of a same-parity edge; the remaining missing pairs are **unoccupied**. Put `U=M-I`, the number of unoccupied pairs.

## Classification

Up to exchanging the two parity sides where the bridge rules permit it, every triangle in `G[R union T union S]` has one of the following vertex-part patterns:

    RRR, TTT, RRT, RTT,
    RRS, TTS, RTS, RSS.

The patterns `SSS` and `TSS` are impossible.

- `SSS` is excluded by the parity-plane star-forest theorem.
- In a putative `TSS` triangle, the `S--S` edge joins different star centres. For either star endpoint, both the other star and its adjacent `T=P1` vertex contain that endpoint's odd antipode. Hence neither endpoint has bridge degree one. But every `S--S` edge requires an endpoint with exactly one antipode bridge, contradiction.

Thus a triangle with two star vertices, if it exists, has pattern `RSS`.

## Exact missing-pair tolls

The existing substitution and parity--star injections give the following local tolls; all listed missing pairs are distinct because occupied and unoccupied buckets are disjoint and both charge maps are injective.

| triangle type | forced occupied pairs | forced unoccupied pairs |
|---|---:|---:|
| `RRR` or `TTT` | 3 | 0 |
| `RRT` or `RTT` | 1 | 0 |
| `RRS` | 1 | 2 |
| `TTS` | 1 | 2 |
| `RTS` | 0 | at least 2 |
| `RSS` | 0 | 2 |

For `RRS`, its same-`R` edge occupies one missing pair and its two `R--S` arms charge two unoccupied pairs. The same reasoning for `TTS` needs one extra observation: the star has two `T` antipode bridges, so neither `T--S` edge can be first-kind (unique-bridge) critical; both are second-kind edges and charge distinct unoccupied pairs. In `RSS`, both `R--S` arms charge unoccupied pairs.

The apparently cheaper `RTS` case also forces two unoccupied pairs. Let its vertices be `r,t,x`. The edge `rx` charges a missing pair `rt'` and therefore forces the additional edge `xt'`. Since `rt` is present, `t'!=t`. Thus `x` has at least two `T` antipode bridges, so `tx` cannot be first-kind. It is second-kind and charges another missing pair `r't`; this pair differs from `rt'`. Hence the triangle expands to two crossed missing pairs around `x`.

## Consequence

Combined with `FOUR_CENTRE_TRIANGLE_FREE_BLOCK_CLOSURE.md`, every surviving counterexample lies in one of two sharply separated regimes:

1. a parity-only triangle, which spends at least one unit of `I` (three for a one-side triangle); or
2. a star-containing triangle, which spends at least two units of `U`.

The next local target is the expanded `RTS` bow-tie: a present `R--T` edge beside two crossed unoccupied missing pairs and four star arms. It is the only star-triangle pattern whose two-unit toll is not already visible from two same-side star arms.

## Trust boundary

This is a local classification and charge statement, not yet a density closure. It uses only the proved star-forest necessity, parity substitution injection, and the first-/second-kind classification of `T--S` edges. It does not use selected/Hall source-tuple premises.
