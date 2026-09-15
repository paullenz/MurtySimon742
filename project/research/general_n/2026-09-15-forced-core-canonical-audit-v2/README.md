# Canonical forced-core independent audit v2

Date: 15 September 2026.

This package extends the independent audit of the completed 306-state forced-core discovery. It has two logically separate purposes:

1. independently re-enumerate **all 170 candidate whole-state exclusions** with the type-multiplicity scanner from `forced-core-canonical-audit-v1`, comparing complete profile counts and every acceptance/rejection stage count against the authoritative discovery rows;
2. independently replay the **136 rescanned survivor witnesses** through the same independently structured acceptance semantics, without relying on the primary discovery search order.

Nothing in this package promotes a closure by itself. The canonical ledger remains **4,626 exclusions / 952 survivors / 3,632 whole-state closures** until the audit is complete and a separate reviewed promotion gate is applied.

## Local checkpoint before remote full audit

The first audit package already had 24 field-for-field independent exclusion matches. Five additional candidate states were re-enumerated locally with the exact repository `scan_forced_core_types.cpp` blob (`1328bbe6fdbac77e599fe504de9efd9b3c057183`) and matched the authoritative discovery field-for-field:

```text
9858, 10296, 10507, 10858, 10898
```

Thus **29/170** candidate exclusions have direct independent exact matches before launching the full remote matrix.

The direct survivor replay harness initially exposed one semantic pitfall: the scanner uses `envelope=-1` as a sentinel meaning that no envelope cap is active, not as a literal upper bound. After reproducing that canonical semantics exactly, **136/136 survivor witnesses pass**, and the replay reproduces every witness `E`, target-flow cost and envelope field exactly. The temporary sentinel mismatch is retained in this narrative rather than hidden.

## Remote gate

The accompanying workflow downloads the pinned discovery artifacts, reconstructs the exact 306-state plan, isolates the 170 candidates, and launches **one independent state per job**. This intentionally mirrors the safe sharding of the discovery run because the heaviest states exceed one billion type profiles.

The aggregate succeeds only if:

- all 170 expected candidate keys occur exactly once;
- the independent scanner returns `FORCED_CORE_EXCLUDED` on every candidate;
- the primary and independent rows agree exactly on `S`, `Emax`, complete profile count, every old acceptance/rejection stage count, all forced-core rejection counts, and status;
- all 136 survivor keys occur exactly once in the replay;
- every survivor witness passes and reproduces the authoritative witness `E`, target-flow cost and envelope.

A successful aggregate records `promotion_status=AUDIT_COMPLETE_NOT_PROMOTED`. Promotion remains a separate reviewed step.

See `RECEIVER_PRICE_LEMMA.md` for the parallel analytic compression work.
