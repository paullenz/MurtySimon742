# V6 / V7 archive review and scope reconciliation

7 September 2026. Candidate mathematics; independent mathematical review OPEN.

## Distinct checkpoints sharing the name v7

The uploaded-in-chat originals are `MurtySimon_GeneralN_SharedAdjacency_v6.zip` and `MurtySimon_GeneralN_LocalIncidence_v7.zip`. They must not be confused with the separate `2026-09-07-degree-load-v7` workstream, whose complete audit bundle has a different filename, size and checksum.

The shared-adjacency v6 archive contains 88 payloads plus its manifest. It records 6,530 exclusions of v5's 6,918 rows, leaving 388 rows in 167 demand patterns, all at (n,Delta,m)=(28,15,196). Local-incidence v7 contains 87 payloads plus its manifest and excludes those 388 rows in a 22/19/347 partition. Its own proof and handoff explicitly leave 197 edges open. Neither archive asserts the separate weak-core reduction.

The degree-load v7 readable proof already in the repository instead records a 173/215 partition of the same final 388-row frontier and supplies a candidate weak-core density reduction. It therefore claims a complete order-28 candidate route. These are alternative arguments, not additional disjoint exclusions. Its `CORE_SCOPE_AUDIT.md` is a central separate proof obligation; the two v7 archives are not interchangeable evidence for its models.

## Checks completed at intake

The original local V6 and LocalIncidence V7 archives pass CRC testing, safe-path inspection and exact manifest coverage. Every payload length and SHA-256 matches: 88 in v6 and 87 in v7. This is integrity checking, not a new assertion of mathematical certification. A fresh-copy arithmetic review of local-incidence v7 is recorded separately when finished.

| Archive | Bytes | SHA-256 | Git blob computed from original bytes |
|---|---:|---|---|
| MurtySimon_GeneralN_SharedAdjacency_v6.zip | 17940219 | d00a9627e9ed4d8a6f22ae1f2b194791412ee2d16d502b1968be16e02aa30496 | 40d3067484d2b1efc61e12781f9b545f1a96f166 |
| MurtySimon_GeneralN_LocalIncidence_v7.zip | 15943487 | 0637c6b91d7e0c311025bf68dc7a373f57f6230e271588bd6693d8ffc17eb6cf | 8aaf3028d9af6d4d854d5a25b3728763a49fe3e6 |

## Repository availability at intake

Paul reported uploading V6 and V7. At the read-back baseline `239eee18aa05a21e2265b8fcd34bd6553a38ef6a`, the root tree, recursive project inventory and branch listing do not expose these archives. An attempted tree entry using the byte-verified v6 Git object returned HTTP 422: `tree.sha 40d3067484d2b1efc61e12781f9b545f1a96f166 is not a valid blob`. No branch was changed by that failed tree creation. Therefore this intake record does NOT claim that either archive has been moved or attached to main. It does not infer a loss of permission or diagnose the user's upload interface.

When the repository exposes the files, verify their original hashes and attach the unchanged blobs to `2026-09-07-shared-adjacency-v6/` and `2026-09-07-local-incidence-v7/` respectively. Do not replace the separate degree-load-v7 directory or claim its larger audit bundle is present merely because these two archives are attached.

## Direct 197-edge continuation

The direct target is (a,b,t)=(12,15,2). It requires newly generated demand/residual/slack domains or a proved transfer theorem. Do not reuse the t=1 survivor list as the t=2 domain without proof. The separate weak-core candidate is preserved unchanged; a direct t=2 check is useful corroboration with a different density-scope dependency.

This record and any README update are documentation-only. Frozen n25/n27 proofs, prior evidence and the governed theorem ledger are untouched. Publication status, arithmetic reproduction, graph-theoretic necessity and independent expert review remain separate questions.
