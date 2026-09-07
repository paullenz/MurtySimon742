# Degree-load v7: readable order-28 candidate record

7 September 2026. **Complete candidate n=28 proof route; internal arithmetic reproduced; independent mathematical review OPEN.**

Read [N28_CANDIDATE.md](N28_CANDIDATE.md), [PROOF.md](PROOF.md), [CORE_SCOPE_AUDIT.md](CORE_SCOPE_AUDIT.md), and [RESULTS.json](RESULTS.json). These four files are byte-identical to the corresponding files in the complete v7 checkpoint. The final 388 rows are excluded in two exact stages, 173 plus 215. A new weak-core density reduction extends the degree-15 exclusion from 196 edges to all larger edge counts. No earlier frozen proof or theorem ledger is changed.

## Important distribution boundary

**This repository directory contains readable documents and reports, not the full new binary evidence.** The complete audit archive was supplied separately in the research chat and has not been uploaded here. The original v6 archive is also included there, not silently assumed to exist in this repository. Existing v5 and earlier repository checkpoints remain available unchanged.

The complete archive is:

```text
MurtySimon_N28_Complete_Candidate_Audit_v7.zip
21,975,757 bytes
SHA-256 7e8440aee4d4e566b94937f6d2b927b216c1064eb2a4d40d4153c80e399c8005
```

It includes the original v3/v4/v5/v6 ZIPs, the complete v7 checkpoint, readable proof mirrors, checksums and `replay_chain.py`. All 285 nested payload files plus their five original manifests were integrity-checked. Every original upstream archive is unchanged. The v7-only ZIP is 1,114,523 bytes, SHA-256 `ba2fe44a116b754be75b40ee2302feeef5ca0b11d35bcab740d60e4e3bd408d8`.

## Complete-bundle replay

After obtaining and extracting the complete audit ZIP, from its directory run:

```sh
python3 -I -S -B replay_chain.py --verify-only
python3 -I -S -B replay_chain.py --check --output /absolute/path/to/new-n28-check
```

Integrity-only mode is not arithmetic replay. Full checking runs v3's n28/Delta16 scope, the complete v4 arithmetic, full v5/v6 separately implemented checker routes and the full v7 checker/model tests. Python plus a C++17 compiler and Boost headers are needed for the upstream route; v7 checking alone uses only the Python standard library. No optimisation solver is required for verification. The new combined wrapper was tested in integrity mode; every component entry point was separately run in this research session, including a fresh-copy v7 replay. The bundle states this distinction explicitly.

The [exact v7 report](evidence/EXACT_CHECK_REPORT.json) and [fresh-copy report](evidence/V7_FRESH_CHECK_REPORT.json) are copied here. They do not replace the coefficients and original input files in the audit archive. A subsequent binary-archive attachment must be verified and recorded before complete repository evidence publication is claimed.

Both implementations and the internal scope audit are by the same assistant. Independent expert review, independent researcher reproduction and formal verification remain OPEN. A new general-order density-reduction tool and this one completed candidate order do not establish the full conjecture or improve the existing uniform maximum-degree coefficient.
