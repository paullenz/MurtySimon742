# Residual-one k=2 half-ray: H--U orientation filter — SUPERSEDED

Date: 2026-09-20

Status: **SUPERSEDED / DO NOT USE DOWNSTREAM.**

The original version of this note allowed a U-sourced H--U singleton certificate to use a matched endpoint, in particular the private foot `q_i`, and derived `HU-PRIVATE`, `HU-QI`, and `HU-IHOLE` from that possibility.

That is invalid. Every U-vertex and every matched endpoint lies in the rooted B-layer `B=N(v)`. Therefore a U-source t and a matched witness q share the root v, so `N(t) cap N(q)` can never be the singleton `{h_i}` with an A-head. The error was found by hostile replay and is preserved rather than silently erased.

The corrected replacement theorem is:

`ONE_CODE_R1_K2_HALF_RAY_HU_B_LAYER_CORRECTION_AND_SLACK_THEOREM.md`.

Its valid conclusions include:

- every U-sourced H--U witness lies in A, never in the matched/U B-layer;
- U-sourced edges are confined to H-positive `bar d` vertices or endpoint-indexed classes `U_{bar d xor e_l}`;
- reverse matched certificates are charged to directed H-holes or the residual hub;
- the exact half-ray satisfies the replacement bound `L_H >= 3t-1`.

The original failed derivation remains recoverable in git history for audit purposes. The upstream rigid-interface realizability caveat and mandatory `X_3` negative control remain unchanged.