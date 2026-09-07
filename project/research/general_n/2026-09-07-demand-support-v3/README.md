# Demand-support v3: preserved original checkpoint

7 September 2026. Repository publication of the checkpoint prepared in the chat that continued the Murty-Simon generalised attack.

**Candidate mathematical arguments; arithmetic REPRODUCED; independent mathematical review OPEN.** Publication does not certify the graph-theoretic lemmas, resolve a complete new order, or promote the theorem ledger.

## Contents and scope

The original checkpoint proposes degree-case exclusions (n, Delta) = (28,16), (30,17), and (33,19), at and above the respective equality edge counts. It also preserves incomplete n=28/Delta15 and n=29/Delta16 exploration. These are the claims and limitations of that checkpoint, not a reconciliation or promotion of later work in other directories.

Read the unchanged [original proof](PROOF.md). The complete original package is preserved through the lossless capsule and recovery program here: 41 manifested payload files plus their original MANIFEST.json. This includes source code, all numerical certificates and rows, test inputs, reports, provenance, and unfinished explorations.

The storage representation removes redundant numerical fields and row tables and encodes the seeded abstract-test inputs by their deterministic original recipe. All other values, including the actual discovered dual weights and historical timings, are stored. Recovery invokes no solver and needs no network. It is not an instruction to rediscover missing certificates. Recovery was executed locally: every file hash and the complete original ZIP hash matched exactly, and the recovered arithmetic evidence passed the separate checker.

## Recover and replay

Use trusted project code and a fresh output directory. The byte-exact recovery was tested with CPython 3.13.5 and zlib 1.3.1; a differing serializer, PRNG implementation or compressor must fail the hashes rather than silently alter evidence. SciPy is not required for recovery or verification.

```sh
python3 -I -B restore_checkpoint.py --output /absolute/path/to/new-v3-copy --zip-output /absolute/path/to/MurtySimon_GeneralN_DemandSupport_v3.zip
cd /absolute/path/to/new-v3-copy
python3 -I -B verify_manifest.py
python3 -I -B check.py
python3 -I -B test_hand_endgame.py
```

The CAPSULE.part*.b64 files are parts of an encoded lossless capsule, not individually ZIP files. Use the recovery program rather than unzipping them directly. CAPSULE_MANIFEST.json verifies the storage parts; the original MANIFEST.json verifies the recovered payload.

Original ZIP: 1,258,114 bytes.

SHA-256: `4d5e06a85f2e9112776205a632436a8e9224bc9f14055ceabf5a67dd83d89fd1`.

## Correction to the original publication-status wording

The original README and provenance are preserved unchanged. They correctly record that this checkpoint was not uploaded during its creation turn. Their explanation that write actions were unavailable was incorrect: write tools had not been discovered properly. This publication supersedes that historical upload status; there was no demonstrated loss of the user's GitHub permission.

This is an additive checkpoint. The existing demand-stability-v3 and pair-budgets-v2 workstreams, frozen n=25/n=27 editions, earlier general-order checkpoints, and governed theorem ledger are not changed by this publication. No independent review or novelty determination is claimed.
