# Audit correction: assignment labels are not independent regime evidence

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal audit: ChatGPT/Geeps.

## Status

This note corrects an over-interpretation of the exploratory script

`adjacent_t123_regime_key_redteam.py`.

The correction does **not** affect the exact fixed-potential template covers or their exact lower bounds. It affects only claims that attempted to infer structural regime laws by reclassifying the *chosen assignment labels*.

## What went wrong

The exploratory cross-`t` script used label functions that were not independent targets:

- at `t=2`, `label_t2` is defined directly from `D1 = #{i:s_i=1}`;
- at `t=3`, `label_t3` is defined directly from the previously discovered count-tree rule, including the split `rho1 <= 8` (equivalently `z2 >= 8` for `b=16`).

Therefore observations such as

- “`D1` alone classifies the t=2 labels,”
- “the half-source threshold `z2=8=b/2` is the unique successful threshold for the t=3 labels,” and
- the resulting scan of many linear encodings of those labels

are statements about how well one can re-encode a rule that was already used to create the labels. They are **not independent evidence** that those statistics determine the intrinsic exact-certificate geometry.

The script remains useful as a deterministic replay/compression of the chosen assignment rules, but it must not be cited as a discovery or validation of those rules.

## What remains valid

The following earlier exact statements are unaffected:

1. The n=29,t=3 fixed potential
   `F = 6 B(3,0)+4 B(3,5)+3 B(3,9)` has an exact rational four-template cover of all 94 regenerated profiles. The checker recomputes every template gap with `fractions.Fraction` and uses no LP/MIP solver for acceptance.
2. Profiles `0,1,38,30` are pairwise incompatible under one nonnegative scalar template at common gap `>=0`, by exact rational Farkas certificates. Hence at least four templates are necessary within that fixed-potential architecture.
3. Together, those two facts establish exact template count 4 within that fixed-potential model.
4. The old count tree is still a valid *sufficient assignment rule*: assigning profiles according to its tests gives a positive exact gap for every profile. What is withdrawn is the inference that its branching statistics are thereby intrinsic or minimal.

## Correct replacement test

The right independent target is the complete **validity mask**

`M(P) = {T : exact_gap_T(P) > 0}`

of every profile under all templates in the preserved exact cover.

A feature set is structurally informative only if it predicts or compresses these independently recomputed masks (or another independently defined object), rather than labels generated from the same feature set.

The replacement checker is

`n29_t3_template_mask_structure_exact.py`.

It imports the preserved exact four-template checker, recomputes all four exact rational gaps on every regenerated profile, constructs the 4-bit validity mask, and only then tests candidate feature compressions. The associated GitHub Actions replay is included in

`.github/workflows/general-rx-hall-adjacent-regime-key-redteam.yml`.

## Research consequence

Until the non-circular mask scan says otherwise, treat the following as **retracted as structural evidence**:

- special significance of coefficient `2` in `J=2 z2-D1`;
- special significance of the threshold `z2=b/2`;
- the claimed 2/3/4 assignment-regime classifiers as evidence for an all-order `t+1` regime lemma.

The exact minimum template counts `2,3,4` in the three finite fixed-potential laboratories remain separately established; what is under audit is the proposed low-dimensional explanation of those counts.

This is an internal same-assistant audit correction, not external review.