# N=27 red-team audit, 8 September 2026

Start with [REPORT.md](REPORT.md). **No blocking mathematical defect found; original n=27 candidate retained, independent specialist review OPEN.** This is an audit of the frozen n=27 route, not a substitution of the later 293/500 result. No frozen proof or theorem-ledger entry is modified.

The audit replays the entire original computation, rederives all 35,435 terminal source-cap vectors using augmenting-path matching, and deliberately corrupts certificates. It found a permissive raw C++ digit parser; a strict JSON guard now rejects malformed inputs before the original checker runs. Original archive hashes protect the published frozen inputs. The first added comparison failed on one compression-dependent input hash; the corrected comparison verifies both raw links and equal decompressed content before normalizing that single field. All limitations and the first failure are preserved, not silently upgraded.

## Replay with the original archive

Assemble and extract the exact archive from `releases/n27-candidate-v1` using its instructions. Let ORIGINAL be the extracted `N27_Candidate_2026-09-07_v1` directory, AUDIT this directory, and FRESH a new output directory.

```sh
python3 -I -B "$AUDIT/check_raw_inputs.py" "$ORIGINAL" --output strict-inputs.json
python3 -I -B "$ORIGINAL/replay.py" --replay --output "$FRESH"
python3 -I -B "$AUDIT/compare_replay.py" "$ORIGINAL" "$FRESH" --output comparison.json
python3 -I -B "$AUDIT/audit_n27.py" "$ORIGINAL" --output terminal-caps.json
python3 -I -B "$AUDIT/mutation_tests.py" "$ORIGINAL" --output new-mutation-results
```

Python 3.10+, C++17 `g++`, zlib and OpenSSL libcrypto development files are needed. Output files/directories must not already exist. The audit programs never modify the original evidence. `audit_n27.py` explicitly reports missing manifest payloads when used on a partial source transfer; it is not the full archive verifier. Use the full workflow above for complete coverage. Mutation tests intentionally reproduce the raw-parser weakness and require the strict guard to reject it; their completed-with-finding status is expected, not a claim that the frozen raw parser rejected every malformed input.

The automated full sequence is `.github/workflows/n27-redteam.yml`. [evidence/REMOTE_REPLAY.json](evidence/REMOTE_REPLAY.json) identifies the exact archive, source commit, two run outcomes and payload hashes. The directory preserves complete comparison records, the final cap audit, strict-input coverage and the mutation results. First-run diagnostics are in `history/`. [MANIFEST.json](MANIFEST.json) records payload bytes/hashes; the separate publication receipt identifies the verified repository changes.

The mathematical result remains a candidate: at most 182 edges on 27 vertices, equality exactly K(13,14). All enumeration and additional code are by the same assistant, not independent specialist authorship, a full Lean formalisation, or a journal-level acceptance.
