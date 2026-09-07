# N=27 candidate evidence, edition 1

7 September 2026. Complete candidate argument; external mathematical review and external computational reproduction remain OPEN.

The proposed statement is e(G) <= 182 for every simple diameter-two edge-critical graph on 27 vertices, with equality exactly K13,14. The [proof and browsable source files](../../project/reviews/n27/2026-09-07-candidate-v1/README.md) describe the argument and its audit limits.

## Obtain the complete archive

Download or clone this repository with all files in this directory. Run:

```sh
python3 assemble_archive.py
```

This verifies each byte part, reconstructs `N27_Candidate_Evidence_2026-09-07_v1.zip`, and verifies the complete archive. The parts are pieces of one archive and cannot be extracted individually.

- Complete ZIP: 71,778,093 bytes.
- SHA-256: `8381ed450859b9efa54fa6ec3c76bda786ec3fc31ec52732637c5346224caf3c`.
- Entries: 116; all ledgers, original outputs, source code, certificates, checks, clean replay logs and instructions are included.

Extract the complete ZIP. Inside `N27_Candidate_2026-09-07_v1`, run:

```sh
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --replay --output /absolute/path/to/new-n27-replay
```

The first command verifies frozen files and final certificates. The second rebuilds and repeats the entire arithmetic in a new directory. Python 3.10+, a C++17 compiler (`g++`), zlib and OpenSSL libcrypto development headers/libraries are required. Executables are rebuilt from the preserved source.

A complete clean replay passed internally before this archive was frozen. Its data match the original outputs, including all 80,978,546 canonical residual columns representing 1,451,011,425 labelled columns. No final numerical cases remain. These are same-assistant checks and do not replace external mathematical assessment.

The frozen n=25 packages and governed theorem ledger are preserved unchanged.
