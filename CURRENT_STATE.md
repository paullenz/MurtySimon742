# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff is preserved byte-for-byte at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_UNVERIFIED` / `BLOCKED_INPUT_TRANSPORT`. Preserves the first one-spare hand argument and the explicitly requested input-download diagnosis. No new whole-state exclusions or promotions.

**WORK MODE:** `ADMIN`, explicitly requested by the user's interruption: “Can you fix the input download limits?” No further mathematical unit was started after that interruption. The preceding hand argument is preserved below rather than left only in chat.

**INSPECTED PREDECESSOR:** `96732d048070c1b78a12d524b433d138b6d989fa` on `main`; rechecked immediately before this write. Its V3 policy remains in force.

**LAST VERIFIED RESULT:** unchanged: the prior equality package records 25 internally verified whole-state certificates and 4,588/4,588 Python/C++ decision agreement, with 41 distinct active certificates across the strict-block and equality families, all `NOT_PROMOTED`. Those are prior recorded results, NOT a fresh replay in this session. The one-spare argument below is `WIP_UNVERIFIED`; external review of the canonical bridge and new argument remains OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The completed 170-candidate forced-core independent audit remains `AUDIT_COMPLETE_NOT_PROMOTED`. No new candidate count has been computed. State 3349 q-enumeration remains unresolved.

**ACTIVE / PENDING:** the proposed one-spare result is exact high-source selection and a two-occurrence residual-union bound, proved conditionally below for d>=2. It has not been independently audited or applied to the catalogue. The requested baseline replay has NOT run: a direct download of the 1,341-byte replay script failed before any response body because the execution environment could not resolve `raw.githubusercontent.com`. This is a reproduced DNS/transport failure, not evidence of a file-size rejection. GitHub connector text/metadata reads work. The separate download tool required a web-viewed URL; that web fetch returned `DisabledError`, so that route was also unavailable.

**UNPRESERVED WORK:** `None` after publication of this checkpoint: the complete candidate argument, seven-file transfer manifest, downloader source, test outcomes and actual failure are recorded below. No missing proof inputs have been reconstructed from guesses or truncated text.

**DEFERRED ADMIN:** automatic workflow-completion reporting remains `NOT_IMPLEMENTED`; no workflows were launched, cancelled or polled during this unit. The transport helper is preserved inline here as WIP; extraction to a normal script/package is non-blocking and should not trigger a maintenance spiral. Session DNS/web-download availability is not fixed by this commit.

**NEXT ACTION:** do not repeat the failed DNS route in this unchanged session. When a working file-transfer path or exact local inputs exist, use the seven-file hash-checked helper below, then run the original equality replay once. If it passes, audit the one-spare argument below and only then implement its scalar test. Until then, the replay is `NOT_RUN`, the new lemma is `WIP_UNVERIFIED`, and no exclusion count changes.

**PROCESS RULE NOW IN FORCE:** `RESEARCH_EXECUTION_POLICY_V3`. Exact-input reads, one bounded unit, immediate preservation, one publication verification. This checkpoint does not authorize further work after a user pause/stop instruction.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Read `AGENTS.md`; inspect only commits/evidence required by this handoff and the active work mode.
3. If durable sources agree, execute `NEXT ACTION` directly; do not reconstruct the project from chat history.
4. In `MATH` mode, do one bounded research unit and checkpoint it before beginning the next.

## Checkpoint invariant

A timeout may lose at most the single small in-memory research unit currently being attempted. Results, failures, counterexamples, changed attacks, and completed bounded computations are checkpoint events.

## Protected MATH-mode summary

- no unrelated README/reviewer-document maintenance;
- no broad repo archaeology or CI inventory;
- no repeated workflow polling;
- no piggybacked housekeeping/process fixes;
- maximum one sensible fallback after a preservation write failure;
- after two consecutive connector/write failures, checkpoint `BLOCKED_TOOLING` if possible and stop retrying;
- `UNPRESERVED WORK: None` before starting the next substantive unit;
- put non-blocking process work in `DEFERRED ADMIN:` instead of doing it immediately.

## Preserved one-spare receiver argument — WIP_UNVERIFIED

This is a candidate hand proof, not a new computational certificate or an independently accepted theorem. It depends on the canonical graph-to-selected/residual bridge, whose external review remains open. Sources at the inspected predecessor:

- `project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`, Sections 3, 5 and 6;
- `project/research/general_n/2026-09-15-tight-label-block-v1/README.md`;
- `project/research/general_n/2026-09-15-tight-label-equality-v1/README.md`.

### Hypotheses and notation

Fix d>=2. Put T={i:s_i=d}, H={u:rho_u>=d}, M={v:rho_v=d-1}, and L={v:rho_v<d-1}. Assume |T|=|H|=d and |M|=d+1. At every B-vertex u, N_u is the disjoint union of selected labels S_u and residual labels R_u, with |R_u|=rho_u. A label i has at least s_i distinct selected sources, and selection at u implies s_i<=rho_u. Each selected obligation (u,i)->v has i absent from N_v. Distinct selected labels at one source have distinct destinations. Opposite orientations of one unordered B-pair cannot both be selected.

Use two containments inherited from this representative construction. For (u,i)->v, S_u minus {i} is contained in N_v, and S_v is contained in N_u. For the second containment, any j in S_v has a selected destination z different from u because the unordered pair {u,v} is already represented in the orientation u->v. The selected quasi-edge (v,j) must therefore dominate u. Since uv is missing, ju is present. This proves j in N_u.

### 1. Tight destinations and saturated receivers

Every i in T must be selected at all d vertices of H, because these are its only eligible sources. Thus T is contained in S_u for every u in H.

A T-obligation from u cannot terminate in H, whose vertices already contain its label. Outside H no vertex can select a T-label. A receiver must nevertheless contain the other d-1 T-labels in its residual set. Its residual degree is less than d, hence is exactly d-1: the receiver lies in M. If it receives label i in T, its residual set is exactly T minus {i}.

Let D_u be the receivers of the d T-obligations from u. Then D_u is a d-element subset of the (d+1)-element set M. Write o(u) for its unique omitted receiver.

### 2. Candidate rigidity: no additional high-source selections

Suppose j in S_u minus T for some u in H. For every v in D_u, the T-obligation from u forces j in N_v. The residual set of v is contained in T, so j must in fact lie in S_v.

For any other w in H, |D_u intersect D_w|>=2d-(d+1)=d-1>=1. Choose v in this intersection. Since w sends a T-obligation to v, reverse containment gives S_v contained in N_w. Therefore j lies in N_w. It also lies in N_u by its original selection, so j belongs to N_w for every w in H.

The selected obligation (u,j) cannot have a destination in H, because its destination must omit j. It cannot have a destination outside H either: that destination would need to contain all d labels of T; none can be selected there, while fewer than d residual slots are available. This contradicts the existence of a destination for every selected label.

Consequently, under these hypotheses,

    S_u = T and q_u = d for every u in H.                 (OS1)

The proof uses a common receiver, not identical omitted receivers. Thus it covers both equal and different omission patterns. The case d=1 is deliberately outside this recorded statement; the displayed common-receiver estimate does not prove that case.

### 3. Candidate two-occurrence residual-union bound

For i outside T define

    e_L(i) = |{w in L:rho_w>=s_i}|,
    K_2 = {i outside T:s_i>e_L(i)+1}.

By OS1 there are no selected occurrences of i in H. At most e_L(i) selected occurrences can occur in L, by eligibility and distinct sources. Each i in K_2 therefore has selected occurrences at at least two distinct receivers in M.

Any u in H omits only o(u). At least one of those two receivers belongs to D_u, so reverse containment puts i in N_u. OS1 says S_u=T, and i is outside T, hence i is in R_u. Therefore

    K_2 is contained in R_u for every u in H,
    |K_2| <= min_{u in H} rho_u.                         (OS2)

This is an s/rho-only necessary condition under the stated hypotheses. A strict violation would be a candidate whole-state obstruction independent of q. No catalogue application, exclusion count, independent checker, or new replay success is claimed here. Labels forced to only one receiver are not covered by K_2; simply reusing the equality-case K would be unjustified.

### Review still required

Check the inherited reverse containment and the graph-to-selected bridge; independently review OS1 and OS2; retain the d>=2 scope; reproduce the old equality baseline before a new scan. This checkpoint stops at the first substantive candidate argument instead of extending it to further spare receivers or claiming new certificates.

## Input transport diagnosis and bounded repair attempt

A 1,341-byte pinned file failed under curl with exit 6: `Could not resolve host: raw.githubusercontent.com`. The Python downloader below independently failed with `Temporary failure in name resolution`, stopped on the first DNS error, wrote an `INCOMPLETE` transfer report, and did not run the replay. The separate file downloader could not proceed through its web-view requirement because the web fetch returned `DisabledError`. These observations do not establish a GitHub file-size limit and do not justify more repeated download attempts in the unchanged session.

The exact minimal replay is seven files, **693,544 bytes total**, not a whole repository checkout. GitHub connector directory reads supplied the following immutable Git blob hashes and byte sizes at commit `96732d048070c1b78a12d524b433d138b6d989fa`:

| Package | File | Bytes | Git blob SHA-1 |
|---|---|---:|---|
| equality-v1 | run_replay.py | 1341 | b4afc6994894466e0771fde6870a06e25f0949e7 |
| equality-v1 | scan_equality.py | 2533 | 172014696bcb8854f74fa012a2f6ab346f8b9c17 |
| equality-v1 | verify_equality.cpp | 1302 | 1a46b8d0d2ba849504dc5c655ddf99db0333a047 |
| equality-v1 | RESULTS.json | 153447 | 42559db1cf186d940fea43e498e78048475525eb |
| equality-v1 | INDEPENDENT_RESULTS.tsv | 83701 | 3bd852fcd9b4b86a0975e43db7588564d932d2d2 |
| block-v1 | INDEPENDENT_INPUT.txt | 423339 | e0aa50b79df3825bc92f7eb1b1a75908e3e546a0 |
| block-v1 | RESULTS.json.gz.b64 | 27881 | b780462063f929e0361d4cccb94efeaf7fd8bb5b |

Here equality-v1 and block-v1 abbreviate the exact dated paths in the source below. The local helper's tests passed for a valid synthetic byte string, rejection of truncated and same-length-corrupted strings, and atomic file installation. These are helper unit tests, NOT mathematical replay tests. The live download attempt exited 1, with zero verified replay files and `replay: NOT_RUN`.

### Preserved downloader source: fetch_equality_replay.py

This is a prepared, locally unit-tested transfer helper, not a claim that this session's network has been repaired. Extract the following code verbatim to a script when a usable transfer path exists. It also accepts an exact prepopulated directory via `--verify-only`. No proof input is altered and no missing row is invented.

```python
#!/usr/bin/env python3
"""Fetch seven immutable replay files with exact size and Git-blob validation.

No GitHub credentials are read. Public files only. Existing valid files are
reused. A DNS failure stops immediately; other transport failures get one
raw-content API fallback. Partial files are never installed. The verifier is
not run unless --replay is explicitly provided and all input checks pass.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

REPO = 'paullenz/MurtySimon742'
COMMIT = '96732d048070c1b78a12d524b433d138b6d989fa'
ROOT = 'project/research/general_n/'
EQUALITY = ROOT + '2026-09-15-tight-label-equality-v1/'
BLOCK = ROOT + '2026-09-15-tight-label-block-v1/'
FILES = (
    (EQUALITY + 'run_replay.py', 1341, 'b4afc6994894466e0771fde6870a06e25f0949e7'),
    (EQUALITY + 'scan_equality.py', 2533, '172014696bcb8854f74fa012a2f6ab346f8b9c17'),
    (EQUALITY + 'verify_equality.cpp', 1302, '1a46b8d0d2ba849504dc5c655ddf99db0333a047'),
    (EQUALITY + 'RESULTS.json', 153447, '42559db1cf186d940fea43e498e78048475525eb'),
    (EQUALITY + 'INDEPENDENT_RESULTS.tsv', 83701, '3bd852fcd9b4b86a0975e43db7588564d932d2d2'),
    (BLOCK + 'INDEPENDENT_INPUT.txt', 423339, 'e0aa50b79df3825bc92f7eb1b1a75908e3e546a0'),
    (BLOCK + 'RESULTS.json.gz.b64', 27881, 'b780462063f929e0361d4cccb94efeaf7fd8bb5b'),
)

def validate(data: bytes, size: int, expected: str) -> None:
    if len(data) != size:
        raise ValueError(f'Length mismatch: expected {size}, received {len(data)}')
    actual = hashlib.sha1(b'blob ' + str(size).encode('ascii') + b'\0' + data).hexdigest()
    if actual != expected:
        raise ValueError(f'Git blob mismatch: expected {expected}, received {actual}')

def atomic_write(destination: Path, data: bytes) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as f:
            name = f.name
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(name, destination)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)

def download(path: str, size: int, expected: str) -> bytes:
    urls = (
        f'https://raw.githubusercontent.com/{REPO}/{COMMIT}/{path}',
        f'https://api.github.com/repos/{REPO}/contents/{path}?ref={COMMIT}',
    )
    failures = []
    for url in urls:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'MurtySimon742-bounded-input-fetch/1',
            'Accept': 'application/vnd.github.raw+json',
        })
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                data = response.read(size + 1)
            validate(data, size, expected)
            return data
        except urllib.error.URLError as exc:
            failures.append(f'{url}: {exc}')
            if isinstance(exc.reason, socket.gaierror):
                raise RuntimeError('DNS unavailable; stopped without retrying. ' + failures[-1]) from exc
        except (OSError, ValueError) as exc:
            failures.append(f'{url}: {exc}')
    raise RuntimeError('Both bounded download routes failed:\n' + '\n'.join(failures))

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path, help='New directory for this pinned seven-file replay')
    parser.add_argument('--verify-only', action='store_true', help='Check existing files without using the network')
    parser.add_argument('--replay', action='store_true', help='Run the original verifier after all file checks pass')
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    report = {'commit': COMMIT, 'status': 'INCOMPLETE', 'files': [], 'replay': 'NOT_RUN'}
    try:
        for path, size, expected in FILES:
            target = args.destination / path
            if target.exists():
                data = target.read_bytes()
                validate(data, size, expected)
                source = 'existing_verified_file'
            elif args.verify_only:
                raise FileNotFoundError(f'Missing input: {path}')
            else:
                data = download(path, size, expected)
                atomic_write(target, data)
                source = 'download'
            report['files'].append({'path': path, 'bytes': size, 'git_blob': expected,
                                    'sha256': hashlib.sha256(data).hexdigest(), 'source': source})
            print(f'VERIFIED {path}', flush=True)
        report['status'] = 'ALL_SEVEN_FILES_VERIFIED'
        if args.replay:
            run = subprocess.run([sys.executable, str(args.destination / EQUALITY / 'run_replay.py')],
                                 capture_output=True, text=True, timeout=45)
            report['replay_stdout'] = run.stdout
            report['replay_stderr'] = run.stderr
            report['replay_returncode'] = run.returncode
            report['replay'] = 'PASS' if run.returncode == 0 else 'FAIL'
            print(run.stdout, end='')
            if run.returncode:
                print(run.stderr, file=sys.stderr)
                raise RuntimeError(f'Replay failed with exit code {run.returncode}')
    except (OSError, RuntimeError, ValueError, subprocess.TimeoutExpired) as exc:
        report['error'] = str(exc)
        print(f'BLOCKED: {exc}', file=sys.stderr)
        return_code = 1
    else:
        return_code = 0
    atomic_write(args.destination / 'TRANSFER_REPORT.json',
                 (json.dumps(report, indent=2, sort_keys=True) + '\n').encode())
    return return_code

if __name__ == '__main__':
    raise SystemExit(main())
```

Example in an environment with working public GitHub downloads:

```sh
python3 fetch_equality_replay.py equality-replay --replay
```

The command was NOT successfully completed in this session. A session-local copy of the helper was tested only as described above. No fresh Python/C++ mathematical agreement, third-party verification, or input-transport restoration is asserted.
