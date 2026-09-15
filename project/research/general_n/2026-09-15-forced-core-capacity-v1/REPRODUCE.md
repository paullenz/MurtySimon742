# Reproduce the forced-core receiver-capacity exclusions

From repository root, with Python 3 standard library only and without `-O`:

```sh
python3 project/research/general_n/2026-09-15-forced-core-capacity-v1/run_replay.py
```

The replay reads `2026-09-14-block-pressure-v1/REMAINDER_12.json`, verifies its preserved source digest, reconstructs the forced low-label cores for original rows160 and338, enumerates every relaxed receiver-capacity partition, runs the tiny structural challenge, and requires byte-independent parsed-object equality with `RESULT.json`.

Expected canonical parsed-result SHA-256:

```text
8784209ee05bb1ec6cd6da559e8845dbfeee3e041a96dcce9f41360c6d12920e
```

Expected result: rows160 and338 excluded, taking the original synthetic sample to `713/713` rejected. The canonical finite frontier remains unchanged. This is not an unrestricted proof.
