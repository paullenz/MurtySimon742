# Rejected archival-transfer attempts

14 September 2026. This is a data-transfer correction, not a mathematical counterexample.

The first long compressed-source transfer, commit 69e4debfad9acb16ab39e03eceb98bdd17e1a133, contained an incomplete/corrupted payload. It was rejected and removed from the working tree at 0d5dd7f6b7aa988b72fc25eaf069d8ae549d78b9. A subsequent chunk attempt included a correct first chunk and an incorrect second chunk; the incomplete set is also removed. Neither encoded attempt is accepted as evidence or preservation-complete. Their history remains visible.

The replacement stores readable source files. Every source blob was compared with the original portable-bundle Git blob before inclusion. Historical JSON outputs are normalized for whitespace/key order only, retaining their parsed values. Original raw-file hashes and executable reconstruction are separate records where applicable. The conditioned-excess proof, verified source and frozen mathematical result were unaffected by the archive-transfer errors.

Never accept a partial archive, alter a hash to make a failed transfer pass, or infer preservation from a successful write alone. The scientific content and its transfer integrity have separate checks.
