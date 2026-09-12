# N34 complete candidate: reviewer v1

12 September 2026. **Candidate e(G)<=289, with equality exactly K(17,17).**
External specialist review, novelty assessment and independent external
reproduction remain OPEN.

Start with the [complete proof and equality ledger](../../project/research/n34/2026-09-12-equality-v1/README.md),
the [new universal source-capped threshold lemma](../../project/research/general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md),
the [heavy-degree model proof](../../project/research/n34/2026-09-12-equality-v1/HEAVY_SPLIT.md)
and the [focused internal audit](../../project/research/n34/2026-09-12-equality-v1/AUDIT.md).

The previously open equality branch is completely covered: 13,546 states,
6,708 hand/accounting exclusions, 6,837 exact envelope certificates and one
exact heavy-split Farkas certificate. The replay checks 3,018,781 envelope
inequalities and all 12,570 columns of the final certificate. The earlier
bound package remains the upper-bound dependency.

Full N34 certificate replay from the repository root, using only Python's
standard library:

```sh
python project/research/n34/2026-09-12-frontier-v1/verify_upper_layers.py
python project/research/n34/2026-09-12-m290-v1/verify.py
python project/research/n34/2026-09-12-equality-v1/verify.py
python releases/n34-reviewer-v1/check_manifest.py
```

[MANIFEST.json](MANIFEST.json) pins the new artifacts, direct replay inputs,
and the unchanged dependency baseline. The equality streams include their
complete original bytes through lossless gzip/base64 storage, with original
and encoded hashes checked during replay. SciPy is needed only for optional
coefficient rediscovery.

The [bound-only reviewer package](../n34-bound-reviewer-v1/README.md) and
[joint-clipping/upper-layer checkpoint](../general-joint-clipping-reviewer-v1/README.md)
remain preserved as history and dependencies. Their original manifests refer
to their stated publication snapshots; current navigation files have new hashes.

Paul Lenz directed the research. ChatGPT/Geeps developed and internally checked
the candidate mathematics and implementations. The complete fixed-order
candidate frontier now reaches n=34; no unrestricted all-order proof is claimed.
