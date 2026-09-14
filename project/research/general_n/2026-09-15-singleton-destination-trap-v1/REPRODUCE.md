# Reproduce the singleton-destination / cardinality arc-slot exclusions

From repository root, with Python 3 standard library only and without `-O`:

```sh
python3 project/research/general_n/2026-09-15-singleton-destination-trap-v1/run_replay.py
```

The replay reads the preserved original relaxed-profile corpus, verifies its source digest, runs the exact singleton-source matching and the stronger all-source cardinality-compatible unordered-pair max flow on rows160,338,347,471,586, and requires complete parsed-object equality with `RESULT.json`.

Expected canonical parsed-result SHA-256:

```text
9a89c420f82a0bd89eb8e99a34dd3109ace9c1829879e62e819d452f408313f7
```

Expected newly excluded original synthetic rows: `347,471,586`.
Expected retained rows under this route: `160,338`.

Scope: necessary selected-label/destination cardinality coupling and simple-orientation constraints in the original synthetic namespace only. This is not a canonical whole-state promotion or an unrestricted proof.