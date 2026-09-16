# Murty–Simon / Erdős #742 — live current state

> Read this first. The d=2 singleton exception is hand-closed and internally checked. Intrinsic defects zero and one are now excluded for every exact block with d>=2. Proof and summary are published; separate source/raw GitHub transfer remains pending.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_D2_SINGLETON_CLOSURE_VERIFIED_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Theorem-first priority. Verification and compact publication of the preserved d=2 closure, not a survivor scan.

**INSPECTED PREDECESSOR:** `56812deda04c3eb5e4c7a25b3e13ec483ed11c16`, tree `4cd73d84a9da82f5ccf5530a7d0ba6c5fbee6a6b`, freshly re-read before final publication. The full direct closure was preserved there before verification; the normal form remains at `81067c78adc18c1bb4c3792c289d168af20f0540`; prior d>=3 results remain at `cf718afcba303618f2231b95d452b9af5671c8d8`.

**LAST VERIFIED RESULT:** internal hand proof. Criticality of ts forces the singleton neighbourhood N(k)={s} union Y and residual label k at every off-pool vertex. Every common label q then has R_q=delta_q=2 and N(q)={t,s} union X union Y union O. At least two common labels are full false twins. The singleton has a proper subset of their neighbourhood. An elementary diameter-two graph lemma makes every C-X edge separately redundant, contradicting all-edge criticality. The successful twins are the COMMON LABELS, not the X sources of the abandoned fibre shortcut.

**UNIFIED CONSEQUENCE:** L+beta+2mu>=2 for every actual exact block |T|=|H|=d>=2, without a positive-surplus, fixed-order or pool-size hypothesis. Hence W>=d+(d-1)m+2. The d>=3 quadratic clique increment still requires complete F[T]. For d=2 the generic cutoffs 6 and 8 already followed by rounding older bounds because W is even; this closes the structural exception and strengthens the joint W,m bound, not those rounded scalar cutoffs. Larger defects and configurations without an exact block remain open.

**CHECKS:** Python bitset and C++ explicit-path implementations agree on all 6204 graph records and 18485 eligible redundant deletions. Generic lemma: 33867 labelled graphs through n=6 inspected, with 1710 premise-satisfying graphs and 4080 target edges. Local completions: 4400 records, 2132 diameter-two graphs and 11021 eligible deletions. Full NONCRITICAL representative controls: 90 graphs, 1053 valid representatives, 42 controls with a nonempty selected Y-set, and 3384 redundant C-X edges. Each control still has a critical ts edge losing exactly one pair. Four negative controls have destructive designated deletions; one has diameter three. Fresh generation and stored replay succeeded with byte-identical graph/input/decision/summary outputs. Both implementations are by the same assistant; external review and novelty assessment OPEN.

**PROOF LIMIT:** local and representative controls are not critical-graph witnesses or conjecture counterexamples. The final twin-containment lemma does not need X-Y selected-set equality in its deletion step; that stronger true normal-form consequence and the longer direct proof remain preserved. No canonical graph census or old-pipeline replay is claimed.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. The prior 203-key candidate union, 41 strict/equality certificates, 170-candidate audit and state3349 retain their earlier boundaries. No workflow launch, q-enumeration or promotion.

**PRESERVATION:** exact proof, compact check summary and publication-status record are in `project/research/general_n/2026-09-16-d2-singleton-closure-v1/`. The complete 19-file delivered package `MurtySimon742_D2_Singleton_Closure_2026-09-16_v2.zip`, SHA256 `9c5ac15c427c3d70f9109fd7dddb5382a15f5a1f546c985b922616cc80ecbfc1`, preserves original sources, raw compressed graphs/input/decisions, checksums, audit notes and the predecessor ZIP unchanged. All manifested members verified locally. Input SHA256 `620a4f0806056fb1a4d13689a8f2233dfbf35bc8d4ac3998db89fca19888b547`; decision SHA256 `5744e8e2f91385abc7d477e89d7cf18ddee2b6cc225188c81e2b9d8d6461f470`.

**TRANSFER CORRECTION:** two attempted source-archive transfers failed exact byte-identity checks because assistant-transcribed base64 payloads differed from the correct local bytes. The corrupted objects were never published on main. Final publication deliberately excludes them and any unusable unpacker link. No generic GitHub service or permission diagnosis is inferred. Separate source and raw-stream GitHub transfer remains PENDING; full tested bytes are in the delivered ZIP. The earlier proposed handoff claiming source installation is archived as unpublished and superseded.

**UNPRESERVED WORK:** no completed mathematical finding remains only in session memory after remote confirmation. Verification source and full raw evidence are preserved in the delivered package, but are NOT separately installed in GitHub; this transfer and older attachment transfers remain pending.

**DEFERRED ADMIN:** source/raw and older evidence transfers; root README/reviewer integration; unrelated CI/status work; independent review, literature novelty assessment and promotion.

**NEXT ACTION:** one bounded generalization of critical-edge covering to incomplete F[T], with one missing tight edge as the first stress test. Identify the additional private witnesses permitted by missing tight edges and seek a parameterized charge, rather than transplanting the clique theorem or launching a survivor scan. Preserve the first theorem, obstruction or failed overextension. No missing-edge branch is claimed closed here.

**PROCESS RULE:** one bounded unit then preservation and one remote confirmation; no background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Evidence

- [d=2 closure and twin-containment lemma](project/research/general_n/2026-09-16-d2-singleton-closure-v1/D2_SINGLETON_CLOSURE.md).
- [Exact compact check summary](project/research/general_n/2026-09-16-d2-singleton-closure-v1/PUBLICATION_SUMMARY.json).
- [Publication scope, hashes and pending evidence transfer](project/research/general_n/2026-09-16-d2-singleton-closure-v1/PUBLICATION_STATUS.md).

The milestone remains a comparatively short structural treatment with explicit coverage and external-review boundaries. Finite checks support that treatment rather than replacing it.
