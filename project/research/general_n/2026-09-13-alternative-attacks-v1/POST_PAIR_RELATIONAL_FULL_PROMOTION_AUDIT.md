# Full post-pair relational promotion audit

14 September 2026. **Reviewed ledger promotion after complete independent-implementation audit; external mathematical review and third-party reproduction remain OPEN. This is not an unrestricted Murty-Simon proof.**

## Frozen evidence

- Discovery/recovery run: `34844403328`; complete 3,607-state result SHA-256 `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`.
- Independent audit run: `34854911792`; 256 shards plus successful aggregate requiring complete two-implementation agreement.
- Discovery candidate-key TSV and final audited-key TSV are byte-identical: SHA-256 `67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2`.
- Audit candidate-input SHA-256: `fbcbef0d532a52f4d4897fc4c63ec3ebbe534ac2ba01335dccd4cb1057147f83`.
- Unresolved states: **0** in discovery and **0** in the independent audit.

## Reviewed ledger reconciliation

The audited family contains **2,655** closures: **2,580 N34** and **75 N35**. The reviewed pre-promotion ledgers contained **977 N34** and **0 N35** closures, with zero overlap with the audited family. Promotion therefore gives:

```text
N34 whole-state ledger: 3,557
N35 whole-state ledger: 75
whole-state closures:   3,632
canonical exclusions:   4,626
canonical survivors:      952
  N34 survivors:           949
  N35 survivors:             3
```

The finite accounting universe is unchanged: 4,626 + 952 = 5,578. The promotion changes the canonical finite frontier, not the status of the unrestricted conjecture or the external-review dependency of the graph-to-selected/residual bridge.
