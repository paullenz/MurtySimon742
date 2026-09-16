# Recovery of the completed 124-record scalar screen

16 September 2026. INTERNAL_CONDITIONAL_CERTIFICATES_NOT_PROMOTED. This bounded recovery precedes a new full-frontier application. Inspected main e6b10d064243e252caaa71e031630bffd0c7e400, tree 61a9ed951e6d2e9a99e2bb2f0b114ea09e19688d. The pending attachment has exactly this base. No ledger or mathematical dependency is changed.

## Preserved mathematical argument

Use the FULL canonical selected/residual construction. For d>=2, let T be the entire level {i:s_i=d} and H={u:rho_u>=d}. Suppose |T|=|H|=d. Eligibility and demand force each t in T selected at all H and nowhere else. For K=N_F(T) minus T, the previously proved endpoint cap gives s_k<=d-2 for every k in K.

Fix a high source and its d distinct destinations for T. Each destination is low because the sent label is already present at every high vertex. Each contains all other d-1 tight labels by forward containment, residually because tight labels are never selected at low vertices. Thus for every t, R_t>=d-1, giving deg_F(t)=d+R_t>=2d-1. Every F-neighbour of t is in T minus {t} or K, so deg_F(t)<=d-1+|K|. Consequently |K|>=d, and at least d labels must satisfy s_i<=d-2. This argument is independent of q, positive surplus and extra selections, but conditional on the full canonical bridge and endpoint-cap theorem.

The screen rejects a fixed s,rho profile when an exact block exists and l=#{i:s_i<=d-2}<d. The certificate is 2d-1<=deg_F(t)<=d-1+l. Altering the saved q does not repair the profile.

## All certificates and non-rejections

The completed input has 124 records (123 n34-m289, one n35-m306), all equality-layer records. Twenty records have an applicable exact block; seventeen fail and 107 records are not rejected. All 337 level decisions, including inapplicable levels and non-rejections, are preserved losslessly in DECISIONS.tsv.gz.b64. Decode with Python base64.b64decode then gzip.decompress. Decompressed SHA256 is ac56ba8f648a558884fb675e570016e867125114946b23d77d97097d6165f302. The original exact inputs already exist in the predecessor's saturated-receiver-barrier package.

Certificates, all n34-m289:

| IDs | d | low labels l | degree contradiction |
|---|---:|---:|---|
| 978,979 | 4 | 3 | 7<=degree<=6 |
| 5802,5834 | 5 | 4 | 9<=degree<=8 |
| 5915,5926,5932,5973,5993 | 5 | 3 | 9<=degree<=7 |
| 6095,6102,6103,6133,6135,6139 | 5 | 2 | 9<=degree<=6 |
| 6261,6273 | 5 | 1 | 9<=degree<=5 |

The three applicable non-rejections 5666,5694,5710 meet l=d and already belong to the earlier strict family. State232 and n35-m306 state18 have no applicable block. State3349 is not excluded here. No sample fraction is extrapolated.

## Reconciliation

The named prior families contain 170 forced-core, 16 strict and 25 equality keys. Their union has 192 keys. None of the 17 new-screen keys overlaps the 170 or strict lists; six overlap equality: 5802,5834,5915,5932,5973,5993. Eleven are outside the 192 union: 978,979,5926,6095,6102,6103,6133,6135,6139,6261,6273. Of those,978 and979 were already found in the preceding three-record diagnostic. Thus nine were additional in the pending full124 unit, and the compared candidate union is 203, NOT_PROMOTED. This is not a repo-wide novelty search.

## Recovery verification and exact attachment boundary

Original attachment: MurtySimon742_Rescue_Scalar_Screen_2026-09-16.zip, SHA256 72aa0471f32f6241513a6b31b4ecf7f30536897984544f7872d27857c0d784b9. All eleven entries in its source manifest and its exact predecessor handoff were hash-checked locally. The original check_scan.py and C++ companion were freshly run during this recovery. They reproduced all337 decisions; regenerated RESULTS.json, CHECK_RESULTS.json, DECISIONS.tsv and RECONCILIATION.json are byte-identical to their originals. The optional original-overlap whole-file comparison was not run; its earlier key-extraction boundary remains unchanged.

Exact input Git blobs: REPLAY_INPUT.txt 10b302fb8a8dd4d1b7d040dac3bc4e4a0f008dd5; RESCUE_PROFILES.json 3d683af1884e9b9e6974b69553a5d1246f25f259. Existing repository path prefix: project/research/general_n/2026-09-15-saturated-receiver-barrier-v1/.

Original output SHA256: RESULTS.json 80f3cc0569eb317f57ceb1f93af4f5e77fec422c7d2ec4354a25bf86d734a714; CHECK_RESULTS.json 5e27277ba9982a85bd11fde5389ac0cd027b08fe4e08de0a67c71e3551a26515; RECONCILIATION.json 0e4e0b1642f321b9536e46000081b52cb06adb92ee63294002a7de63e8eda73c. Programs: check_scan.py 0ea84ac624276855955b2c617a9004ba9782ba294f71fcac731abfa462daa839; verify_screen.cpp aee16c326d6bde84a5f1edf066cd6615e40c52b8a3752b1df4fc9ae9c6d405b2.

This recovery publishes the complete mathematical reasoning, certificate list, reconciliation and all level decisions, not a literal upload of every original ZIP byte. Original programs, normalized key extraction and other exact evidence remain in the identified attachment. Both checkers were by the same assistant. No external review, original-graph enumeration, old-pipeline replay, new q enumeration or remote CI success is claimed.

Canonical ledger unchanged:4626 exclusions/952 survivors/3632 whole-state closures. Audit/promotion gates unchanged. Next: apply the SAME condition to the authoritative952 keys with pinned scalar input, and reconcile against the203-key union. Do not fabricate adjacency information or infer closure from a missing input.
