# Archive storage correction — 24 September 2026

The first housekeeping application, run 35982433341 / job 107577260761 at commit 66dd36aa87c95c8751ac1a305a1883798d3986b5, stopped before staging or publication. Its exact changed-path guard detected nine unexpected archive changes. Checkout had warned that these files should have been LFS pointers but were not: broad `*.zip` and `*.gz` LFS rules conflicted with the actual ordinary Git blobs.

The correction adds exact-path `-filter -diff -merge -text` exceptions for those nine files. The general LFS rules and existing N30 reviewer exception remain unchanged. No archive content is edited, regenerated, migrated or deleted. The old attributes file is preserved as `archive/maintenance/2026-09-24/.gitattributes.original.txt`, Git blob 0f0ceed0a74e17283a827ad49fc110421e0c3fca.

The follow-up housekeeping run must start from a clean checkout and check the stored archive bytes against these SHA-256 values from the read-only inventory at 21202de191c1560c0046fe665758112aacb0a916. The exact changed-path guard is not weakened.

| Archive path | SHA-256 |
|---|---|
| `MurtySimon_GeneralN_ColumnPropagation_v5.zip` | `79bdbdf02b23b9eef38e964b54eb300921b24d539014f07b476655d1575e63b6` |
| `project/research/general_n/2026-09-07-column-propagation-v5/MurtySimon_GeneralN_ColumnPropagation_v5.zip` | `79bdbdf02b23b9eef38e964b54eb300921b24d539014f07b476655d1575e63b6` |
| `project/research/general_n/2026-09-07-direct-197-v8/MurtySimon_N28_197_Direct_v8.zip` | `b753076ffc755066a0c57756be91cc5b265c163d869244d3aa65e3943799347b` |
| `project/research/general_n/2026-09-07-local-incidence-v7/MurtySimon_GeneralN_LocalIncidence_v7.zip` | `0637c6b91d7e0c311025bf68dc7a373f57f6230e271588bd6693d8ffc17eb6cf` |
| `project/research/general_n/2026-09-07-shared-adjacency-v6/MurtySimon_GeneralN_SharedAdjacency_v6.zip` | `d00a9627e9ed4d8a6f22ae1f2b194791412ee2d16d502b1968be16e02aa30496` |
| `project/research/general_n/2026-09-22-independent-742-r12-quotient/r12_support10_case1_masks.txt.gz` | `44ce0db04777f751278864138ae5b0d8213205cb26c19c70df1916ae982b070b` |
| `project/research/general_n/2026-09-22-independent-742-r12-quotient/r12_support9_masks.txt.gz` | `55a47fedf4b2735bac3bdde418f1b0b58b53a355af2b3300b7b1cc28c3805c29` |
| `project/reviews/delta14/2026-09-06-document-review-v1/N25_Delta14_Document_Review_Evidence_2026-09-06.zip` | `91b95fa86e03713779e9a9e6c9f20514c04668e7cc8c2083a025662aef9c0b36` |
| `project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Evidence_2026-09-06_v1.zip` | `6e0b92a9edddbc75cf1b35094de20c8371cf5e5a4f5cc06fbb7830273aa725f1` |

This is a storage-integrity repair, not a mathematical replay or an assertion that all historical binary contents have been re-audited.
