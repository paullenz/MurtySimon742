# Reproduce the fresh forced-core/high-squeeze closure

From repository root, with Python 3 standard library only and without `-O`:

```sh
python3 project/research/general_n/2026-09-15-fresh-forced-core-high-squeeze-v1/run_replay.py
```

The replay reads `2026-09-14-joint-blocks-v1/FRESH_RECHECK_FULL.json`, checks seed `74220260919` and embedded source SHA-256 `f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e`, reconstructs all seven fresh survivors, and requires exact parsed-object equality with `RESULT.json`.

Expected canonical parsed-result SHA-256:

```text
7357a5139417a1b48f94d8ddbb6122c57363ce70ab0c4586673a290a25c51464
```

Expected result: six profiles fail total forced-core receiver capacity and row490 fails the exact `43<45` high-demand squeeze, taking the fresh synthetic namespace to `715/715` rejected. The original synthetic namespace remains `713/713`; the canonical finite frontier remains unchanged. This is not an unrestricted proof.
