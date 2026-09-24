# 02:00 recovery — r=12 support-ten timeout reconciliation

Scope: independent mathematical review inside the recovered 02:00 trigger. This does **not** retro-credit work from the prior 01:00 session and does not upgrade abstract profile/source feasibility to graph realizability.

## Durable-state reconciliation

The launch-time `CURRENT_STATE.md` correctly retained the audited position: 6,386 strict r=12 support-ten kernels, 32 exact source-feasible rows, 19 HiGHS helper-LP exclusions, and 13 timeout/UNKNOWN rows; therefore `S<=14` remained frozen.

A durable artifact already present on `main`, `HELPER_LP_ALL32_COMPLETE.md`, was committed at `b52a4475cd7281429b2622785983158cf2fcc89d` after the prior session's last credited boundary. It reports a later trust-constr pass that resolves the timeout set. That later artifact was not eligible for retroactive time credit, but it is legitimate evidence to inspect afresh in this session.

The exact timeout set in `HELPER_LP_ALL32_PASS1.md` is

`{362, 363, 437, 438, 451, 455, 1494, 3755, 3758, 4663, 4664, 4665, 4682}`.

Direct row-by-row comparison against `HELPER_LP_ALL32_COMPLETE.md` shows the same 13 indices, each marked `pass ipm`, `status 2`, with reported objective strictly greater than 1. The later `HELPER_LP_IPM_PASS2.md` accounts for the last eight of these indices: 451, 455, 1494, 3755, 3758, 4664, 4665, 4682.

## What this unit establishes

1. The launch-time 13-row UNKNOWN set and the durable COMPLETE artifact refer to exactly the same rows; there is no row-identity mismatch.
2. The later artifact claims zero remaining UNKNOWN rows, rather than silently dropping timeout cases.
3. Its provenance is after the prior session's credited boundary, so the mathematical claim must be revalidated now rather than inherited as credited work.

## What it does not establish

This reconciliation does **not** independently certify the 13 trust-constr optima or their constraint encoding. Consequently `S<=14` remains frozen at this checkpoint. The next bounded task is to reconstruct/check the helper LP constraints for these 13 rows with an independent solver/encoding or exact lower-bound certificate.

Observed research interval for this unit: 02:08:30--02:11:48 Europe/London = 3m18s. Administration and publication time excluded.
