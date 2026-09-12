# N35 complete candidate: reviewer v1

12 September 2026. **Candidate e(G)<=306, equality exactly K(17,18).**
External specialist review, novelty assessment and external reproduction OPEN.

Start with the [complete candidate proof](../../project/research/n35/2026-09-12-candidate-v1/PROOF.md),
[focused internal audit](../../project/research/n35/2026-09-12-candidate-v1/AUDIT.md)
and [research/replay index](../../project/research/n35/2026-09-12-candidate-v1/README.md).

The balanced-degree theorem handles Delta=18, the a=14 high-b theorem handles
Delta=20, and the 7/12 theorem handles Delta>=21. At Delta=19, the fifteen-label
tail bound leaves only the 307- and 306-edge layers.

| Layer | Demand profiles | States | Hand/accounting | Exact envelopes | Unresolved |
|---|---:|---:|---:|---:|---:|
| 307 edges | 13 | 19 | 9 | 10 | 0 |
| 306 edges | 144 | 466 | 219 | 247 | 0 |
| **Total** | — | **485** | **228** | **257** | **0** |

The standard-library replay checks **92,701 local integer inequalities**, all
three zero-demand states and exact disjoint coverage. The residual frontier
is reconstructed recursively and compared state-for-state with the earlier
breadth expansion. The complete a=15 demand enumeration remains a shared,
hash-pinned proof-critical dependency. No numerical status is a proof event.

```sh
python project/research/n35/2026-09-12-candidate-v1/verify.py
python project/research/n35/2026-09-12-candidate-v1/audit_frontier.py
python releases/n35-reviewer-v1/check_manifest.py
```

[MANIFEST.json](MANIFEST.json) pins artifacts and the unchanged transitive
dependency baseline. [VALIDATION.json](VALIDATION.json) records the clean
replay, hashes and navigation checks. Discovery scripts, original certificate
streams, failed proposals and provenance are preserved alongside exact replay.

This pass also publishes the [N34 reviewer-v2 simplification](../n34-reviewer-v2/README.md).
Its p<=4 hand theorem is not silently applied to N35, where the generic
rho=2 source bound is p<=5. The two current proof packages keep that distinction
explicit.

Paul Lenz directed the work. ChatGPT/Geeps developed the candidate mathematics,
software and same-assistant internal audit. The fixed-order candidate frontier
now reaches n=35; no complete candidate above n=35, unrestricted all-order
solution, external acceptance or novelty determination is claimed.
