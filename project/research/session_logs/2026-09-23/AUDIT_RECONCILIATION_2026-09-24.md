# 23 September launch and utilisation reconciliation

Audit date: 24 September 2026. Audited predecessor: `083dc162be599fe102274c4ce23f4f99ba5c7476`.

This reconciliation treats each Europe/London `HH:00:38` trigger as one session. It does not infer time from commits, unit counts or prose. The 05:00 trigger had no canonical record and now has an audit-created record containing only `UNVERIFIED` fields. Six records with real research retain incomplete stop/preservation fields and are therefore unverified for whole-session accounting. Historical fragments and incorrect intermediate claims remain preserved.

The canonical interval union was recalculated from explicit `start` plus `stop`/`end` boundaries, accepting the legacy duration-key variants only for this audit. The resulting lower bound is 432m09.31s across scheduled research records. Fully finalized records contribute 402m25s over 622m01s of evidenced available windows, or 64.70%. This percentage is not whole-day utilisation.

The 13:00 record preserves an invalid intermediate cap `x_i<=n-Delta-1`. The same session's current note, `EXACT_D2C18_AND_SUPPLEMENT_CAP.md`, explicitly withdraws it: assigned witnesses lie on `B=N(v)`, so only `x_i<=Delta` follows. No later result may cite the invalid cap.

See `project/research/general_n/2026-09-24-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md` for the complete per-trigger table and classifications.
