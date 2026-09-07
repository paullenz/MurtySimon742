# Order-28 reviewer release v1

7 September 2026. **Candidate proof; independent mathematical review and external computational reproduction OPEN.** This edition consolidates the direct LocalIncidence-v7 / direct197-v8 route. It is not an independently accepted theorem or a solution of the general conjecture.

## Papers

Read the [mathematical manuscript (PDF)](N28_Reviewer_Manuscript_v1.pdf), then the [computational verification and reviewer guide (PDF)](N28_Verification_Companion_v1.pdf). Their editable sources are [manuscript LaTeX](N28_Reviewer_Manuscript_v1.tex) and [companion LaTeX](N28_Verification_Companion_v1.tex). The [review report template](REVIEW_REPORT_TEMPLATE.md) separates mathematical assessment from computational reproduction. No invitation has been sent by this release.

The proposed conclusion is at most **196 edges**, with equality exactly for **K(14,14)**. The manuscript covers the 196-edge equality calculation and the freshly generated 197-edge calculation separately, as well as all other maximum-degree cases and the external Fan bound. The alternative degree-load-v7 weak-core reduction is not a dependency. Infinite excluded profile families and the full general conjecture are not claimed resolved.

## Default hardened checking entry point

Place the six original ZIPs named in [ARCHIVES.json](ARCHIVES.json) in one directory. From this release, run:

```sh
python3 -I -B review_check.py --archives-dir /absolute/path/to/original-zips --output /absolute/path/to/new-n28-review --jobs 3
```

**Full arithmetic checking is the default.** It requires Python 3.10+, g++ with C++17 and Boost headers, no optimisation solver and no network. Keep assertions enabled; do not use `-O`. The output directory must be new and outside this release.

For integrity only, explicitly add `--verify-only`. That mode reports `arithmetic_replayed: false` and must not be cited as a proof replay.

The driver verifies the original archive sizes, SHA-256 hashes, CRCs, safe paths, exact manifest coverage and all 400 payloads. It then makes a separate v8 working copy and **automatically installs the guarded helper** after checking both source hashes in [OVERLAY.json](OVERLAY.json). Original archives, manifests, source and historical timings stay unchanged. The complete [patch](check_rows_input_guard.patch) is auditable; it changes input/output validation, not the enumeration or rejection arithmetic. The new guard implements the recorded RT-01 fix and is not claimed byte-identical to the earlier audit patch.

The six component routes, all-degree calculation and helper regression are run; all five handoffs are checked byte-for-byte. A successful report records both final survivor counts as zero. It does not certify the universal structural lemmas. See [CHANGELOG.md](CHANGELOG.md) for scope and provenance.

## Original evidence locations

In a complete repository checkout, recover v3 using `project/research/general_n/2026-09-07-demand-support-v3/restore_checkpoint.py` and v4 using the corresponding `2026-09-07-label-tail-v4/restore_checkpoint.py`. Their guides specify `--zip-output` and pinned recovery environments. Recovery must fail rather than replace an original whose exact hash differs.

The original v5, v6, LocalIncidence-v7 and v8 ZIPs are already in their dated `project/research/general_n/` directories. The [committed audit](../../project/reviews/n28/2026-09-07-redteam-v1/README.md) supplies its own recovery and replay instructions. The reviewer bundle supplied with this release in the research chat includes copies of all six exact original ZIPs for offline checking; those copies do not replace or edit the repository originals.

## Validation performed for this release

The **new default driver was actually executed in full**. All eight jobs passed; all five handoffs match, both scopes end with zero survivors, and all six ZIPs and 400 original extracted payloads remain unchanged. All **13 malformed helper inputs** are rejected before output creation; the full valid 8,216,928-row scope reproduces the original report, survivor bytes and per-demand band bytes.

Read [the complete fresh release report](validation/REVIEW_CHECK_REPORT.json), [the helper tests](validation/helper_regressions/HELPER_TEST_REPORT.json) and [the fresh direct197 checker report](validation/v8_check/EXACT_CHECK_REPORT.json). These are this release's execution records, distinct from the historical internal audit. Preliminary wrapper-path mistakes were corrected before the successful run and are disclosed in the provenance.

The build script compiles both papers three times and records source/output hashes and page counts in `PAPER_BUILD_REPORT.json`. That is document build evidence, not computational proof verification. The repository workflow is narrowly scoped to this release's publication capsule. Local rendering checks are recorded separately; a different TeX distribution can yield different PDF bytes while preserving identical source.

## Review status and attribution

Paul Lenz directed the project. ChatGPT/Geeps developed the mathematics, software, manuscript and internal checks. The [review register](REVIEW_REGISTER.json) starts OPEN. An additional arithmetic kernel in the historical audit reuses preserved model constructors, so it is not a third independent graph-to-model derivation. Actual critical-graph regression samples contain no positive-surplus graph. Independent mathematical review and external reproduction remain essential next review steps.

Frozen n25/n27 editions, all original n28 archives and the governed theorem ledger are untouched. This is a versioned editorial and engineering release, not a silent promotion of mathematical status.
