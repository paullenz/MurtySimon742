# Reproduce the conditioned row-108 closure

From repository root, using Python 3 standard library only and without `-O`:

```sh
python3 project/research/general_n/2026-09-14-conditioned-source-sharing-v1/run_replay.py
```

The replay verifies the canonical row input and the frozen shared-slack parent, runs the complete exact source-price/common-pressure verifier, and checks the complete canonical parsed-output digest and frozen headline counts.

Direct verifier invocation is:

```sh
python3 project/research/general_n/2026-09-14-conditioned-source-sharing-v1/verify_row108.py \
  --remainder project/research/general_n/2026-09-14-block-pressure-v1/REMAINDER_12.json \
  --shared-result project/research/general_n/2026-09-14-joint-blocks-v1/SHARED_SLACK_FULL.json
```

Expected canonical parsed-JSON SHA-256: `5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629`.

The calculation is a selected-incidence necessary-condition exclusion for one synthetic profile, not a graph-realization test or a whole-state promotion.
