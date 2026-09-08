# n=29 restarted red team — fully fresh Delta=16 finite check

8 September 2026. Additive assurance record for the n=29 candidate. The original candidate proof and its production evidence are not modified by this check.

**Verdict: PASS. No blocking mathematical or computational defect was found.** The complete finite Delta=16 calculation at `m=211` and `m=210` has now been reproduced by a second source tree written during the restarted red-team audit. The clean replay uses no inherited Murty-Simon verifier/model module and no inherited prepared input at runtime. This is still same-assistant work, so it is **not independent researcher reproduction**, peer review, or formal verification.

## 1. Why this check was built

The original n=29 Delta=16 proof reused the hash-pinned n=28 direct197 machinery. That production route had clean runners, separate checkers and exact Farkas verification, but common code ancestry remained the largest computational trust boundary after the first-principles mathematical red team.

The replacement finite implementation is preserved at:

`project/research/n29/2026-09-08-independent-d16-v1/`

Its five load-bearing sources are:

- `fresh_prepare.py` — demand enumeration and early exact pruning;
- `fresh_rows.cpp` — independent residual-row enumeration and source-capacity scan;
- `fresh_joint.py` — pure-Python joint propagation/Hall/row-feasibility engine;
- `fresh_endpoint.py` — strongest endpoint LP and exact integer Farkas checker;
- `run_independent.py` — full orchestration and evidence packaging.

None imports a production Murty-Simon model or checker.

## 2. Fully fresh early finite domains

For `a=12`, `b=16`, the fresh preparation code enumerates the complete charging domains directly from

`sum s_i(13-2s_i)/(12-s_i) >= 16+2t`

with exact rational arithmetic.

At `m=211` (`t=3`):

- complete demand tuples: **4,867**;
- source-count rejections: **3,488**;
- support rejections: **261**;
- exact dual rejections: **779**;
- retained demand intervals: **339**.

At `m=210` (`t=2`):

- complete demand tuples: **9,251**;
- source-count rejections: **6,990**;
- support rejections: **116**;
- exact dual rejections: **1,244**;
- retained demand intervals: **901**.

During development, the fresh retained-demand files matched the production retained-demand files byte-for-byte.

The fresh C++ row scanner then enumerates the entire sorted residual domain independently:

- `m=211`: **1,848,957** raw residual profiles -> **206** row survivors;
- `m=210`: **5,765,218** raw residual profiles -> **2,087** row survivors.

The fresh survivor and per-demand band files matched the two older production scanners byte-for-byte in development. `run_independent.py` also independently recounts the raw profile totals via an integer-partition dynamic program.

The fresh scanner reports zero uses of the hard `r>60-t` rejection on these retained bands. Thus the undocumented numerical guard involved in `RT-N29-001` is inactive for this finite input. The separate mathematical bridge establishing `d_F<=10` remains load-bearing in the joint model and has already been rederived as valid.

## 3. Fresh projected and joint stages

The projected filter is independently recomputed:

- `m=211`: 206 -> **118** projected rows;
- `m=210`: 2,087 -> **1,225** projected rows.

The pure-Python joint engine then gives exactly the same complete partition as the production route.

### `m=211`

| disposition | count |
|---|---:|
| survivor | 36 |
| source matching | 38 |
| source Hall | 2 |
| joint total source | 42 |

### `m=210`

| disposition | count |
|---|---:|
| survivor | 593 |
| source matching | 311 |
| source Hall | 29 |
| label domain | 6 |
| total source | 58 |
| joint total source | 222 |
| pair Hall | 6 |

The development comparison matched the production joint states row-by-row, not merely the aggregate counts.

## 4. One fresh endpoint model closes every joint survivor

Unlike the production route, the new implementation does not use successive shared/typed/endpoint LP stages. Every joint survivor is sent directly to one independently coded strongest endpoint relaxation.

SciPy/HiGHS is permitted to propose a dual ray, but a row is excluded only after the fresh verifier constructs integer multipliers and checks exactly that all inequality multipliers are nonnegative, every combined primal coefficient is nonnegative, and the exact combined right-hand side is strictly negative.

The result is:

- `m=211`: **36/36** joint survivors have exact Farkas contradictions;
- `m=210`: **593/593** joint survivors have exact Farkas contradictions;
- total preserved exact certificates: **629**;
- unresolved rows: **0**.

The exact RHS range is `-997..-50` at 211 and `-999..-10` at 210. The least-negative accepted contradiction is therefore still the strict exact inequality `-10<0`.

The two deepest old endpoint rows again produce exact RHS contradictions `-830` and `-355` under the new model.

## 5. Clean-runner reproduction

Canonical clean run:

- workflow: `.github/workflows/n29-independent-d16.yml`;
- run ID: **34244187889**;
- input/source head: `ac7ed309740e8d56ac84a7dd9816729464091139`;
- runner: Ubuntu 24.04;
- conclusion: **success**;
- evidence commit: `536b6a2c365d387d6b9c5729c4cd402ffb613c7d`.

Every workflow stage succeeded: fresh demand generation, fresh residual-row scan, fresh joint/endpoint verification, evidence upload and evidence commit.

The resulting manifest is

`project/research/n29/2026-09-08-independent-d16-v1/MANIFEST.json`.

## 6. Evidence preservation and read-back

The complete generated states and certificate bundles are stored with Git LFS because the repository tracks `*.gz` through LFS. The Git-tree files are therefore LFS pointer records; they are not mistaken here for the payload themselves.

The LFS pointers record:

- states payload: SHA-256 `15ed09b9ccbce4fae5b98a87bebc41aed8fe924c3bf7787abba43ea5bf4402ab`, **12,284 bytes**;
- certificate payload: SHA-256 `5e9c35e8d6d688d37c3ac47a353d8df6aff3e35f25d62b1f5c602cbf105c48cd`, **174,857 bytes**.

Those values exactly match the manifest.

The successful workflow also uploaded artifact `10063767946`, `n29-independent-d16-v1`, with size **184,981 bytes** and SHA-256 `fb93fa713e35dd3b2ef72ec40acb3a1dbe3b672e482ea496c1ee0481779cfed7`.

That artifact was downloaded again during this red-team session. Its ZIP hash matched the GitHub artifact digest. The actual gzip payloads passed `gzip -t`; their compressed SHA-256 values matched the manifest and LFS OIDs; and their decompressed JSON hashes also matched the manifest:

- states JSON: `34d163d48c5178acb9896c69d9e665c48d32de1ba4e029da8adc069a6c82e98b`;
- certificates JSON: `1a6cf1f2a7813b83cf1a414eff4ef6558fb5a79cdffc53028281db30a9f9a9d0`.

The machine-readable read-back receipt is `INDEPENDENT_D16_READBACK_RECEIPT.json`.

## 7. Effect on the restarted red-team findings

### RT-N29-001 — proof traceability

Still a genuine documentation defect in the original candidate edition, not a mathematical defect. The bridge for `dmax=10` / `r<=60-t` has been rederived and remains valid. The fully fresh row replay additionally shows that the `r>60-t` scanner guard itself removes zero retained rows.

### RT-N29-002 — production certificate retention

Still a genuine historical preservation defect in the original production run: its 629 exact certificate objects were verified at runtime but not retained individually.

The new independent run **materially mitigates** this risk by preserving a fresh exact certificate for every one of the 629 late-stage cases. It does not pretend to recover the historically discarded production certificate objects.

## 8. Current assurance judgement

The principal *computational common-code* trust boundary for Delta=16 has now been removed: two separate implementations reach the same zero-survivor conclusion, and the second implementation reconstructs the complete finite calculation from the charging domain onward without inherited code or prepared input.

What remains materially open is now much more mathematical than computational:

1. specialist reconstruction of the graph-to-model necessity arguments;
2. reproduction by a genuinely separate researcher or independently authored program;
3. formalisation of the structural lemmas and, optionally, the finite exact checker.

Accordingly the correct status remains:

**N=29: COMPLETE CANDIDATE, with substantially strengthened independent-code computational assurance; independent mathematical review and independent researcher reproduction OPEN.**

No governed theorem-ledger promotion is made by this red-team check.
