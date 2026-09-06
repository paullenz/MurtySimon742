# N=25 reviewer edition 1

**A complete candidate proof for review. Independent mathematical review is OPEN.**

Read `N25_Reviewer_Manuscript_v1.pdf`, then `REVIEW_GUIDE.md`. The proposed theorem is e(G)≤156 for every 25-vertex diameter-2-critical graph, with equality exactly for K₁₂,₁₃. This edition makes no announcement that the result is settled and does not promote the project theorem ledger.

The manuscript has editable `.tex` and `.md` sources. `EDITORIAL_PROVENANCE.json` identifies the frozen proof and explains the limited presentation changes. The original mathematical evidence ZIP is unchanged, with SHA256:

```text
0588c85900762184040dfb313c89d36349f2a8183db5cbc91a1ee50915cb4e95
```

## Verify and replay

```sh
python3 -I -B review_package.py --verify-only
python3 -I -B review_package.py --replay --output /absolute/path/to/new-n25-replay
```

The complete replay includes the separately nested original Δ14/157-edge argument and all four new scopes. A rerun by this assistant in the same environment is an internal check; a fresh reproduction by an external researcher remains to be obtained.

## Review materials

- `LITERATURE_AND_ATTRIBUTION.md`: precise published inputs, targeted literature-check results, limits and AI contribution disclosure.
- `REVIEW_GUIDE.md`: mathematical obligations and computational scope.
- `REVIEW_REPORT_TEMPLATE.md`: a form for the reviewer's actual findings.
- `REVIEW_REQUEST_DRAFT.md`: an unsent request and two possible initial contacts based on relevant publications.
- `REVIEW_REGISTER.json`: the actual external-review state; no invitation or external verdict has been recorded.
- `RELEASE_UPLOAD_GUIDE.md`: prepared instructions for a GitHub Release page and one-file distribution.
- `MANIFEST.json`: every payload's exact byte size and SHA256.

## If downloading from the repository

The distribution ZIP is stored in two byte-contiguous parts because of the assistant connection's request-size limit. Download both `N25_Reviewer_Package_v1_2026-09-06.zip.part1` and `.part2`, concatenate them in that order, and check the joined ZIP against `ARCHIVE_RECEIPT.json`. Both parts are required.

```sh
cat N25_Reviewer_Package_v1_2026-09-06.zip.part1 N25_Reviewer_Package_v1_2026-09-06.zip.part2 > N25_Reviewer_Package_v1_2026-09-06.zip
```

Extract the resulting ZIP and run the commands from its `N25_Reviewer_Package_v1` directory. The single ZIP supplied directly to Paul contains the same bytes and needs no assembly. GitHub itself can accept this archive as one file.

## Rebuild the PDF

The supplied standalone TeX requires a working XeLaTeX installation with Latin Modern fonts and the standard packages named in its preamble. Run XeLaTeX twice on `N25_Reviewer_Manuscript_v1.tex`. Rebuilding the editable Markdown additionally uses Pandoc with the `tex_math_single_backslash` extension. The manuscript builder source is included for provenance.
