# N35 complete candidate research package

12 September 2026. **Candidate e(G)<=306, equality exactly K(17,18).**
External specialist review, novelty assessment and external reproduction OPEN.

Read the [complete proof](PROOF.md), [focused internal audit](AUDIT.md), and
[reviewer-v1 package](../../../../releases/n35-reviewer-v1/README.md).

The sole new Delta=19 branch has 19 states at 307 edges and 466 at 306 edges.
All 485 are excluded: 228 by hand/accounting and 257 by exact potential
envelopes. The standard-library replay checks 92,701 local integer
inequalities, complete disjoint coverage and all three zero-demand states.

```sh
python project/research/n35/2026-09-12-candidate-v1/verify.py
python project/research/n35/2026-09-12-candidate-v1/audit_frontier.py
```

Inputs are the hash-pinned complete a=15 demand CSV and the plain UTF-8
`t3.jsonl` and `t2.jsonl` certificate streams. Each stream retains every state,
its accepted hand reason or exact certificate, and failed numerical proposals.
`verification.json` and `frontier_audit.json` record the exact checks.
The certificate streams are small enough to keep directly, without encoding.

Optional coefficient rediscovery requires NumPy/SciPy:

```sh
python project/research/n35/2026-09-12-candidate-v1/sweep.py
```

The sweep resumes from saved states. To rediscover from scratch, use a separate
checkout and remove its two streams first; do not overwrite the historical
discovery logs and certificate evidence in the canonical checkout. No numerical
library is required for proof replay. The complete demand enumeration can be
reproduced with the preserved N34 C++17 enumerator, writing its output to a
temporary CSV and comparing bytes with the pinned original.

This is a new 12 September reconstruction and extension, based on repository
baseline ef030cc4e3d1ecc1355c94b5b1fac6befe6ebb78. It preserves prior N34
models and outputs. Paul Lenz directed the work; ChatGPT/Geeps developed the
candidate mathematics, implementation and same-assistant internal audit.
