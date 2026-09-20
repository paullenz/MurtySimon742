# Residual-one k=2 half-ray: reverse-capacity/private-foot overlap — SUPERSEDED

Date: 2026-09-20

Status: **SUPERSEDED / DO NOT USE DOWNSTREAM.**

This same-session note correctly developed parts of the reverse H--U capacity bookkeeping, but it retained the predecessor's invalid premise that a U-sourced H--U singleton certificate could use a matched endpoint `q_i` as witness.

That premise fails because both the U-source and every matched endpoint lie in the rooted B-layer and therefore share the root. The private-foot equations and coordinate-slice exclusions in the original version are invalid.

The valid reverse-capacity material was independently re-derived after discovering the error and incorporated into:

`ONE_CODE_R1_K2_HALF_RAY_HU_B_LAYER_CORRECTION_AND_SLACK_THEOREM.md`.

The replacement theorem gives the exact half-ray bound `L_H >= 3t-1` without using any B--B singleton pair. The failed derivation remains available in git history for audit purposes.