# General-N continuation v3: demand stability and threshold support

**Candidate mathematics; exact arithmetic REPRODUCED; independent review OPEN.**

Start with `PROOF.md`, then `REVIEW_AND_HANDOFF.md`. This checkpoint adds an exact demand-defect identity, an all-order threshold-support charging inequality, short structural exclusions of maximum degree 16 at n=28 and degree 19 at n=33, and a complete internally reproduced projected-domain exclusion of degree 17 at n=30.

It does **not** complete any new order. Remaining dense non-bipartite degrees are 15 at n=28, 16 at n=30 and 18 at n=33. The earlier candidate global coefficient `(10-sqrt(2))/14` is unchanged. The n=25/n=27 frozen candidates and theorem ledger are unchanged.

## Evidence and replay

Python 3.10+ and its standard library suffice. No external solver is needed. From the extracted package:

```sh
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --replay --output /absolute/path/to/new-v3-replay
```

The first command checks preserved-file hashes. The second re-executes both implementations for all six scopes, compares domains and stored results (ignoring only run time), checks the small-graph regressions and exact hand tables, and writes fresh outputs to a new directory. Run without `-O`. The default invocation is verification only.

`projected_scan.py` is the discovery implementation. `check_projected.py` independently generates the necessary numerical domains and uses a weaker supplier-count argument; it imports no discovery code. Both were authored by the same assistant. They reject all **2,070,205** states in the six recorded scopes, with **zero** survivors. These are numerical profiles, not graphs.

The detailed JSON files preserve exact band counts, domain fingerprints, dispositions and diagnostic survivors. Graph tests preserve the actual adjacency bitmasks of all 608 critical graphs found in the exhaustive labelled n=3..6 test. No positive-surplus actual graph was found.

The repository distribution additionally contains a lossless `PACKAGE.part*.b64` transport and `unpack.py`; the transport includes all package source and evidence files. Decode into a new directory with `python3 unpack.py /absolute/path/to/new-directory`, then use the commands above. The readable proof and review documents are also exposed directly in the repository. Transport checksum information is in the repository preservation record.

## Attribution and limits

Paul Lenz directed this research. ChatGPT/Geeps developed the new derivations and checks on 7 September 2026. Independent mathematical review, independent researcher reproduction and formal verification remain OPEN. No novelty or priority claim is made. Original unavailable chat transcripts were not reconstructed as historical evidence.
