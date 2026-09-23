# Pair eligibility Hall filter

23 September 2026. Status: **PROVED INTERNAL NECESSARY CONDITION; ACTUAL-GRAPH FILTER**.

For a maximum-degree root `v`, let `C_i` be the set of `G[B]`-edges having an endpoint-label certificate selectable for label `i`. Then `s_i=|C_i|`. Define

`tau_i=floor(h_i/2)+1`.

A label can be positive-demand only if at least `tau_i` distinct `B`-edges are assigned to it.

Therefore two labels `i,k` can simultaneously have positive demand only if

`|C_i|>=tau_i`, `|C_k|>=tau_k`, and

`|C_i union C_k|>=tau_i+tau_k`. `(PAIR-ELIG)`

The last inequality is the two-label Hall condition: each `G[B]`-edge supplies at most one certificate choice. This is strictly stronger than checking `2s_i>h_i` separately.

## Third-batch ELIG--ELIG collision

The only collision in the disjoint seeds 200--299 batch whose two endpoints pass the scalar eligibility test occurs at `n=20`, seed 228, root 13, `Delta=11`. It joins labels 2 and 4 using supplements 14 and 18 at sources 0 and 19.

Both labels have `h=8,s=5`, hence `tau=5`. Their certificate-edge sets each have size five but overlap on edge `{7,11}`, so their union has size nine, below the required ten. `PAIR-ELIG` rules out simultaneous positive demand.

Direct enumeration with the four collision certificates forced found 18 legal completions: 13 have `S=0`, five have `S=2`, and none makes both collided labels positive. The exact maximum is `S=2`, whereas the scalar graph envelope is `E=4`.

## Consequence

Replace per-label `ELIG` by Hall eligibility whenever collision endpoints matter. The next search target is an `E>=15` live-strip root containing a collision whose label pair passes `PAIR-ELIG`. Nonappearance remains finite evidence, not a theorem.
