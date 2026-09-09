# Hostile assembly audit — Fan-free fixed-order frontier

9 September 2026. **PASS internally; independent external review remains OPEN.**

This audit was written after an external-AI critique challenged two selection/residual semantics and the reliance on Fan's 1987 upper bound. The two semantic objections were resolved by explicit definitions; the project then went further and removed Fan as a logical dependency from its current fixed-order candidate proofs at n=25,27,28,29,30.

The audit checks the replacement as an assembled dependency chain rather than merely trusting green workflows. It verifies complete edge-range coverage of the new upper-band computations, zero final survivors in every required exact checkpoint, exact-certificate acceptance flags, the absence of the old logical Fan phrases from v2 proof surfaces, and SHA-256 integrity of every frozen historical source named by the v2 history files.

Result: **PASS** on all machine-checkable assembly checks. See `FAN_FREE_AUDIT_REPORT.json`.

The result is deliberately not described as external verification. The universal graph-to-residual lemmas and the short hand monotonicity arguments remain the main mathematical trust boundary. Historical v1 proof surfaces and Fan citations are retained rather than overwritten.
