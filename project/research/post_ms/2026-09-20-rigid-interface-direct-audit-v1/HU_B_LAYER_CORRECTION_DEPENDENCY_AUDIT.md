# Dependency audit for the H--U B-layer correction

Date: 2026-09-20

Status: **same-session adversarial dependency trace**.

## 1. Invalidated statement

The invalid premise was very specific:

> a U-sourced triangular H--U edge could use a matched endpoint `q_i` as the external singleton witness.

This fails because both the U-source and every matched endpoint belong to `B=N(v)` and therefore share the root v.

The affected claims were the private-foot chain `HU-PRIVATE`, `HU-QI`, `HU-IHOLE` in `ONE_CODE_R1_K2_HALF_RAY_HU_ORIENTATION_FILTER.md`, together with the same-session attempted extension `ONE_CODE_R1_K2_HALF_RAY_HU_REVERSE_CAPACITY_AND_PRIVATE_FOOT_OVERLAP.md`.

Both files are now explicit SUPERSEDED tombstones. Their failed derivations remain in git history.

## 2. Commit blast radius before this correction

The invalid private-foot strengthening was introduced by commit

`e6ca8c76f7e711404d04302fc983ac8a1142dee9` — `Force private-foot witnesses in matched H-U arm`.

The next pre-session commit

`be5a0a102a5bf03519874a2034fe39d98212eeb7`

changed only `CURRENT_STATE.md`; a direct commit comparison shows no downstream theorem file was added between the invalid strengthening and the present repair.

Thus no later preserved mathematical theorem in the pre-session repository depends on `HU-QI/HU-IHOLE`. The stale handoff did, and must be replaced.

## 3. Nearby private-spoke theorems are not invalidated

Two earlier families use matched endpoints in a different logical role and survive this correction.

### D1 / W_s-free private-spoke theorems

`ONE_CODE_R1_K2_D1_NONHUB_PRIVATE_SPOKE.md` and `ONE_CODE_R1_K2_WS_FREE_PRIVATE_SPOKE.md` apply criticality to an **edge inside B**, such as `t q_i`. Their singleton witness is forced into A (`h_i` or another matched head), exactly as rooted B-edge criticality requires. They do not use a B witness against a B source. The shared-root obstruction is therefore already respected.

### H--H private-foot certificates

`ONE_CODE_R1_K2_Y_INDEPENDENCE_AND_HH_CERTIFICATE_SPLIT.md` uses equations such as

`N(h_l) cap N(q_i)={h_i}`.

Here the source `h_l` lies in A while `q_i` lies in B; they do **not** both share the root. The B-layer correction does not invalidate this mechanism.

### Residual-hub criticality

`ONE_CODE_R1_RESIDUAL_HUB_CRITICALITY.md` applies criticality to B-layer edges but uses A witnesses in the singleton orientations. Again it respects the rooted layer separation.

## 4. Repaired live chain

The invalid branch is replaced by

`ONE_CODE_R1_K2_HALF_RAY_HU_B_LAYER_CORRECTION_AND_SLACK_THEOREM.md`

and its generalization

`ONE_CODE_R1_K2_GENERAL_HU_ORIENTATION_CAPACITY.md`.

The repaired theorem no longer uses any U-source / matched-witness singleton pair. It instead classifies U-sourced witnesses inside A and reverse witnesses from an H-source, producing the exact general bound

`L_H >= h(u-y+1)-u+2`.

## 5. Audit conclusion

The conceptual error was real and load-bearing for the immediately preceding live frontier, but the preserved blast radius is narrow. It does **not** propagate backward into the D1 private-spoke, W_s-free private-spoke, H--H private-foot, or residual-hub theorem packages.

The correct next frontier is the equality/saturation geometry of the repaired H--U capacity theorem, not the discarded coordinate-slice H--U mechanism.