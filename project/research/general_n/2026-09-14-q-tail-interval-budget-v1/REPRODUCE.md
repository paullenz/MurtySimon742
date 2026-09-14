# Reproduction and evidence provenance

## Small independent audit

From this directory, with Python 3.10 or newer and no optimization flags:

```sh
python3 verify_interval_budget.py --obstruction FIXED_WEIGHT_OBSTRUCTION.json --output actual.json
python3 -m json.tool --sort-keys actual.json actual.canonical.json
python3 -m json.tool --sort-keys INTERVAL_INDEPENDENT_VERIFICATION.json expected.canonical.json
diff -u expected.canonical.json actual.canonical.json
```

Only the standard library is required. Do not use `python -O`: these research verifiers deliberately use assertions. CI runs this exact certificate audit; the much larger replay below is a separate local evidence claim until independently rerun.

## Frozen inputs

The full replay uses two original GitHub Actions artifacts. Download with an authorized GitHub CLI connection, or use the copies in the accompanying evidence bundle. Artifact retention is finite; a missing or expired artifact is an evidence-availability failure, not mathematical disagreement. The delivered evidence bundle preserves copies of both ZIPs and their extracted source inputs.

```sh
gh api repos/paullenz/MurtySimon742/actions/artifacts/10356424619/zip > pilot.zip
gh api repos/paullenz/MurtySimon742/actions/artifacts/10351372086/zip > diagnostic.zip
printf '%s\n' \
 'b91c48268fb6b2b3c6545b28ced230d4ab8ad71b371b49205af1b6166c2a63f4  pilot.zip' \
 'd856c6987acedfc824a85ddd2826ca05d35a4a724b5417c866a235deba17fe4e  diagnostic.zip' | sha256sum -c -
unzip -o pilot.zip
unzip -o diagnostic.zip
```

Extract into a COPY of this package directory if avoiding generated files in the working tree is important. The nested `project/...` paths inside the original artifact are intentional. All replay scripts resolve these paths relative to their own directory. The source hash is checked again by the instrumentation script before any generated code is written.

## Full original pilot plus interval probes

Needs a C++17 compiler and NumPy in the Python environment. Generation and original stopping rules are unchanged; the added code records every profile reaching the target-flow stage.

```sh
python3 instrument_interval_replay.py
g++ -O3 -std=c++17 scan_interval_probe.cpp -o scan_interval_probe
./scan_interval_probe \
 project/research/general_n/2026-09-13-alternative-attacks-v1/Q_STRATIFIED_RECEIVER_REACH_PILOT_INPUT.txt \
 INTERVAL_REPLAY.tsv INTERVAL_PROFILES.tsv 2> INTERVAL_REPLAY.log
python3 audit_interval_replay.py
python3 audit_812.py
```

The independently implemented NumPy audit checks every exported profile and requires all original logical pilot totals to match. Only runtime seconds are excluded from comparison. It writes full diagnostic examples, all target-Hall passes, and state/Esel budget correlations. The 812 audit writes all 6,667 threshold budget rows with q/rho histograms. The full-profile TSV must have SHA256 `4b183b899127f4f9e05faed0cb23a11c6962c854f077d0e3ad209d09b386fb67`.

`explore_thresholds.py` preserves the earlier weaker dead-target and count-only trials. `find_weight_obstruction.py` is an OPTIONAL discovery script requiring SciPy and NumPy. It now writes `FIXED_WEIGHT_OBSTRUCTION_DISCOVERED.json`, leaving the frozen certificate unchanged. Different optimizer versions may discover another valid certificate; the mathematical certificate check uses exact integers and does not require SciPy.

## Synthetic bridge-relaxation tests

```sh
g++ -O3 -std=c++17 search_synthetic_interval.cpp -o search_synthetic_interval
./search_synthetic_interval 100000 > SYNTHETIC_INTERVAL_SEARCH.json
python3 audit_synthetic_interval.py
```

The included frozen generator's main function is renamed and never called; some compilers warn about its missing explicit return after renaming. The new synthetic main is separate. The search seed is 74220260914. The BFS-flow audit is separately implemented from the original Dinic/min-cost routines. It verifies all 713 surviving pair-flow instances and retains selected-incidence/target-flow certificates for examples.

The synthetic domain does NOT impose F-graph realization, residual column realization, or all selected quasi-edge forcing. Its 239 Hall-feasible profiles are counterexamples to forcing Hall deficiency from the ENUMERATED relaxation alone, not counterexamples to Murty-Simon or to the full canonical bridge.

## Current evidence locations and scope

`REPLAY_SUMMARY.json` freezes the principal counts and source hashes in Git. The standalone verifier, obstruction arrays, instrumentation, discovery scripts and independent audits are committed here. The accompanying `MurtySimon742_Interval_Budget_Evidence.zip` preserves the detailed locally executed outputs, original source inputs and compressed 205,931-profile TSV. Its large raw rows have not been silently described as uploaded into the Git repository.

The pilot remains a 15-state experiment. No finite-frontier count changes, no universal q-tail theorem and no external mathematical approval follow from these tests.
