# N30 reviewer package v3

**Current reviewer-facing edition - 11 September 2026. Complete candidate; independent specialist review OPEN.**

Claim: `e(G)<=225`, with equality exactly `K(15,15)`, for finite simple diameter-two edge-critical graphs on thirty vertices.

- [N30_Reviewer_Manuscript_v3.pdf](N30_Reviewer_Manuscript_v3.pdf): the complete proof, including the bridge and all proof-critical finite tables.
- [N30_Verification_Companion_v3.pdf](N30_Verification_Companion_v3.pdf): dependencies, corrections, audit evidence and reproduction instructions.
- [N30_Reviewer_Package_v3.zip](N30_Reviewer_Package_v3.zip): both PDFs, editable Markdown, build source, exact input files and a portable mathematical replay.

The new edition includes the hand higher-degree closure, direct Delta=15 equality proof, hand 100-profile classification, eight 226-edge source inequalities and all 211 225-edge envelope rows. The historical large searches, grouped LPs and Farkas certificates are no longer premises. **Explicit finite arithmetic tables remain part of the proof.**

The [canonical source](../../project/reviews/n30/2026-09-11-reviewer-v3/PROOF.md), [editorial review](../../project/reviews/n30/2026-09-11-reviewer-v3/EDITORIAL_REVIEW.md), [source map](../../project/reviews/n30/2026-09-11-reviewer-v3/SOURCE_MAP.json) and [review report template](../../project/reviews/n30/2026-09-11-reviewer-v3/REVIEW_REPORT_TEMPLATE.md) are preserved. [MANIFEST.json](MANIFEST.json) pins the released files; [BUNDLE_CONTENTS.json](BUNDLE_CONTENTS.json) pins the files inside the ZIP.

After extracting the ZIP, change into `N30_Reviewer_Package_v3` and run:

```bash
python3 -I -B project/reviews/n30/2026-09-11-reviewer-v3/replay_bundle.py
```

The [historical N30 reviewer-v2 package](../n30-reviewer-v2/README.md) remains preserved byte-for-byte. This edition updates the reading surface, not the governed theorem ledger. Internal checks remain REPRODUCED, not external acceptance.
