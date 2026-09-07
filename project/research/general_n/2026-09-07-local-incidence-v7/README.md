# Local incidence v7: complete original archive

7 September 2026. Candidate mathematics; creation-session exact arithmetic REPRODUCED; independent mathematical review OPEN.

The [complete original ZIP](MurtySimon_GeneralN_LocalIncidence_v7.zip) contains 87 payload files plus MANIFEST.json: proof, source programs, separate checkers, exact certificates, input data, tests and historical reports. It is the unchanged Git blob uploaded by Paul in commit `9698513eb20817ebfa9556e79b11d5f538280065`.

Bytes: 15,943,487. SHA-256: `0637c6b91d7e0c311025bf68dc7a373f57f6230e271588bd6693d8ffc17eb6cf`. Git blob: `8aaf3028d9af6d4d854d5a25b3728763a49fe3e6`.

Publication intake checked archive CRCs, safe paths, exact manifest coverage and all payload lengths and hashes. These checks preserve the original evidence; they do not by themselves replay the mathematics.

Extract into a fresh directory. Inside `MurtySimon_GeneralN_LocalIncidence_v7`, read PROOF.md, REVIEW_AND_HANDOFF.md and README.md. Run `python3 -I -B replay.py --verify-only` for integrity, or `python3 -I -B replay.py --check --output /absolute/path/to/new-v7-replay` for the complete separate checking route. Checking uses Python's standard library, no optimisation solver. Keep assertions enabled; do not use `-O`.

This route excludes all 388 final v6 rows at n=28, Delta=15, m=196, in a 22/19/347 partition. Its original proof explicitly leaves 197 edges open. [Direct197 v8](../2026-09-07-direct-197-v8/README.md) supplies that later density scope through a fresh t=2 calculation.

This is NOT the separate [degree-load-v7](../2026-09-07-degree-load-v7/README.md) workstream, which uses a different 173/215 partition and a weak-core reduction. The two proof routes and evidence archives must not be conflated or counted twice.

The earlier intake record's missing-archive status is superseded by this publication. All historical files inside the ZIP are unchanged. Independent mathematical review remains OPEN; publication does not promote the theorem ledger.
