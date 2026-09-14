# Reproduce row471 `e_L=42,43` closures

From repository root, using Python 3 standard library only and without `-O`:

```sh
python3 project/research/general_n/2026-09-15-row471-e42-e43-common-pressure-v1/run_replay.py
```

The replay runs the exact verifier against the preserved `REMAINDER_12.json`, requires complete parsed-object equality with `RESULT.json`, checks canonical parsed-JSON SHA-256 `b2f2b8f1f714eb11225c07d9a9595154a7c53523b5d8da74be8a2028c170cc15`, reconfirms `e_L=41` as an independent regression, and verifies the new `214<222` and `215<222` contradictions for `42,43`.

Scope: the conditioned selected-incidence/common-pressure relaxation only. `e_L=47` remains open; row471 as a whole is not excluded.
