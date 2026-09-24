# Substantive source and mathematical-evidence review — 24 September 2026

**Verdict:** PR #2 is not acceptable as submitted. Its claimed hardening is absent and its new tests fail. Supported repairs are supplied separately against current main. Fresh finite replays retain the conditional n16/Delta9 and n19/Delta10 exclusions. The n18/Delta10 full-row certification is **suspended pending a complete status-safe replay**; its local exclusions are retained with corrected dependencies. No general theorem or equality claim is promoted.

This is a user-requested manual substantive review, not another scheduled research session and not external mathematical acceptance. The research cadence remains **PAUSED**. The starting main was `2ff383498ee08f607aa958181f6dbc4e36d136a1`; the read-only source export was `90b5fd21a90f88aec1ba6445a5ab385559eea999` (Actions run `36011981168`, artifact `10812503619`). The first confirmed-finding checkpoint is `c674d51517ab7691e546cd0852893c997ea4ee7f`. All four files at PR #2 head `bdd46c59365757d373bd359867d9fe47cde0d70f` were reviewed. Complete available histories of the two incomplete artifact paths were inspected.

## 1. Replay integrity and PR #2 — changes required

The PR's `universal_core_checked.py` is byte-identical to the original preserved `universal_core_impl.py`, Git blob `8b9124fc5bc384c4388a0f2d92c1f9be80425ff2`. It does not implement the record-count, digest or pending-file safeguards asserted in the PR body. The new status-mode tests import an absent `work_mode` helper and raise ImportError. Its obsolete CURRENT_STATE must not replace the current pause/review handoff. The draft is not blindly merged.

**Executed positive control:** fresh original generation and C++ replay pass all 11,357 records and reproduce both published hashes:

- Input: `ab9ed63d9caa99b5fbd237fc6b238f77b69a8dc893ff17a764f96ff5cc9ab4bb`.
- Decisions: `c4859538b56444860b26fdc46e40f68bf21b4c65b68dce2e394b531c621ba82a`.

**Executed negative controls:** replacing BOTH input and expected-decision files by empty streams or matching one-record prefixes still made the original checker exit zero and report `PASS_LOCAL_AND_INCIDENCE_CHECKS` with `replay_agreement_records=11357`. Actual C++ output had zero or one records. Byte agreement between two incomplete streams is not proof of complete replay. This failure does not invalidate the separately regenerated complete replay.

**Repair:** a separate `universal_core_integrity.py` wraps the untouched original Python and C++ implementations. It pins reviewed source hashes, input/decision hashes and counts, and the graph-sidecar hash/count. It validates before and after replay; works in a staging directory; excludes concurrent writers; suppresses premature legacy success; handles gzip-only fresh packages; and rejects optimized Python because the inherited checker uses assertions. Validated data is published with the summary last. This is not represented as an atomic multi-file database transaction: every invocation rechecks all bytes.

The portable integrity suite passes 11 complete/hostile scenarios, including complete replay, empty/matching-prefix corruption, changed input/decisions/summary/sidecar/source, gzip-only replay, `-O`, and an occupied lock. A complete stream still passes. [Executed suite](portable_integrity_tests.json), [test source](test_integrity_repairs.py), [original positive output](universal-original.log), [empty false success](empty.log), [matching-prefix false success](truncated_matching.log).

## 2. Status guard — repaired and tested

The old mode regular expression accepted valid prefixes of invalid values such as `MATH2` and `MATH_EXTRA`. The new helper validates the full token, preserves supported plain/bold/backtick formats, and rejects malformed quotes and duplicate fields. A fresh run of the existing legacy regression also exposed that removing the old policy was not rejected; the guard now rejects that removal while retaining the intended V2 migration route. All 11 legacy checks and the mode-format/negative subtests pass. [Executed results](final_status_tests.json).

## 3. Solver handling — a real certification hazard, not a proven historical false exclusion

Four source files (six solver-return sites) treated any returned objective as `minimum_deficit`, irrespective of optimization status. A controlled time-limit result with incumbent 17 and lower bound 16 was exported as minimum 17; a row driver could therefore exclude a case with allowance 16 despite no proved minimum. A result without an incumbent could disappear without an unresolved count. [Reproduced control](nonoptimal_solver_control.json).

All affected entry points now fail closed on time limits, missing or malformed witnesses and other unresolved statuses. Status-zero integral witnesses are rounded only within a tight tolerance and checked against every original bound, constraint and objective using integer arithmetic. All six optimizations request zero relative MIP gap. The rewritten active row driver preserves every case, counts UNKNOWNs explicitly, and returns failure if any remain. The portable suite exercises seven solver controls across each of four modules, plus an injected unknown that must produce one unresolved record and exit 2.

These changes check status and primal arithmetic. **They do not turn a floating-point solver's optimality or infeasibility declaration into a rational dual certificate.** A rejected injected result proves a code defect, not that a specific earlier computation actually made a false exclusion. A fresh run with a two-second limit also does not diagnose a historical ten-second run.

## 4. Fresh complete finite-row replays

| Row | Fresh coverage | Initially unresolved | Bounded rechecks | Final supported position |
|---|---:|---:|---|---|
| n=16, Delta=9 | All 7,008 stable indices | 2 at a two-second per-case limit | Indices 2,200 and 6,289 both optimal with minimum deficit 26 under 30-second limits | 7,008 accounted for; zero remaining unknowns or abstract survivors; conditional internal exclusion retained |
| n=19, Delta=10 | All 1,752 stable indices | 0 | None | Zero unknowns or abstract survivors; conditional internal exclusion retained |
| n=18, Delta=10 | Scalar enumeration of all 54,820; targeted optimal replays only | Full new MILP coverage not performed | Local proofs and identities reviewed | Full-row certification suspended, not disproved |

The initial n16 run properly ended incomplete; it has not been relabelled a clean initial run. Its two original UNKNOWN records and separate rechecks remain saved. Final n16 accounting is 6,917 optimal cases and 91 infeasible statuses; n19 accounting is 1,533 optimal cases and 219 infeasible statuses. The closest n16 deficit is 19 against allowance 14; the closest n19 deficit is 14 against allowance 8.

[Full accounting](FINITE_ROW_REPLAY_SUMMARY.json), [n16 case decisions](n16d9_decisions.json), [n19 case decisions](n19d10_decisions.json), and lossless full original per-case records in `n16d9_safe.jsonl.xz` / `n19d10_safe.jsonl.xz` **inside the delivered review archive**. The repository contains all per-case decisions and the raw-record hashes, rather than the two larger raw-primal files. Each compressed file's uncompressed hash is recorded in the summary. These results still rely on the stated finite normal form, graph-to-profile bridge, star bounds and numerical solver; they are not fresh proofs of those universal premises or of equality.

## 5. n18 identity and proof corrections

A new scalar enumeration reproduces exactly 54,820 candidates and resolves the old identity discrepancy without modifying old output:

- `(5,5,5)/(5,5,5)` is stable index **14,444**, not 20,851.
- Index **20,851** is `d=(5,4,2,1,1,1,1)`, `x=(6,5,3,5,2,1,1)`, `h=(7,6,4,9,3,1,1)`, agreeing with the retained JSON. Its fresh exact-star v4 minimum is 33; the older JSON minimum 30 belongs to a different model.
- Index **50,740** is `d=x=h=(8,8)`.
- Index **2**, `d=(8,7), x=(8,8)`, is another v4 abstract survivor with its own singleton-source exclusion. The historical statement that the only v4 survivors were 20,851 and 50,740 cannot certify coverage.

The n18 local star-five exclusion survives independent star arithmetic. The 50,740 proof contained a genuine bad inequality: it substituted another centre's maximum as a lower bound. Its conclusion can be repaired using BOTH star inequalities. With centre deficits p,q and noncentre deficit R,

`p+q+R<=16`, `8p+R>=59`, `8q+R>=59`, `0<=p,q<=8`

imply `7p-q>=43`, `7q-p>=43`, hence `p+q>=15`. If p<=7 then `7p-q<=8p-15<=41`, contradiction; symmetrically q=8. Thus p=q=8,R=0. The rest of the forced skeleton/root-edge deletion argument was reviewed at its explicit premises. The original invalid paragraph is replaced by a dated correction, not silently endorsed. The inherited x=8 lower bound of 35 and universal graph bridge remain separate review dependencies.

[Exact identities](n18_identities.json), [targeted optimal replays](repaired_profile_replay.json), [corrected proof](../../../research/general_n/2026-09-23-independent-742-r12-count-audit/STABLE_50740_GRAPH_EXCLUSION.md).

## 6. R9 and R11 — fresh evidence, not fabricated recovery

The available history of the R9 audit path begins with a 26-byte timestamp-only file. The R11 support-six output begins with five progress lines, not a complete result. No complete older version of either exact path was found. [Path-history evidence](HISTORY_REVIEW.json).

A fresh execution of the preserved R9 C++ enumerator reproduces 1,044 unit orbits, 79,264 rooted/coloured orbits and the exact saved set of 69 strict masks. A separately written Burnside/group-action audit reproduces both orbit counts, verifies all 69 masks are pairwise inequivalent and checks the stated necessary inequalities. It replaces the unusable R9 stub as an explicitly dated **fresh reconstruction**. Its digest uses a declared ascending-decimal-line encoding; the old note's digest had no declared serialization and is not silently substituted.

The fresh R11 support-six enumeration completes all seven partitions, with strict counts `18,72,15,39,13,27,5` (189 total). Only the sixth partition has source-feasible cores, four in total. The four returned witnesses also pass separately implemented integer checks. The original progress-only artifact remains explicitly incomplete. [New complete result](R11_SUPPORT6_REPLAY.json). This does not by itself replay every downstream R11 supplement exclusion.

## 7. Independent checks of the recent graph-interface arguments

The new edge-first weighted-cover implementation checks all labelled graphs at orders 3,4,5 and every Graph Atlas representative at 6,7. It reproduces exact star minima `4,8,14,21,30`, using a different search organization from the original certificate-type enumeration.

Independent integer checks reproduce the n19/Delta11 contradiction bounds **31,29,28**, each exceeding allowance 27. All **3,072 relevant index-2 core/outer skeletons**, reduced only by the stated omitted-outer-endpoint symmetry, are covered. Exactly the two symmetric hard configurations of the proof remain in its final subcase. This supports the reviewed local case split; it is not an enumeration of all 19-vertex graphs. The index-1 derivation and index-2 root-criticality argument were read against their source/one-use/star assumptions, with no new contradiction found at that conditional scope. The full n19/Delta11 row remains open.

[Independent finite checker](check_finite_evidence.py), [exact output](finite_math_review.json).

## 8. Scope, remaining obligations and reproducibility

This review does **not** establish a general independent Murty–Simon proof, full equality, external acceptance, or a full audit of every fixed-order package. The inherited threshold `250/429`, demand bound `S<=14` at internal computer-assisted scope and equality only through `S<=8` are not newly certified by this review. The R12 all-32 LP replay and the entire universal graph-to-profile chain were not rederived here. A complete status-safe n18 replay, exact solver certificates where required, and independent specialist review remain genuine obligations.

No historical research time, timestamp, scheduled-slot count or focused-session credit was added. Existing failures and immutable source versions remain in Git history. There is no automatic continuation; only this requested review was performed.

Reproduction commands from repository root (see [environment](ENVIRONMENT.json)):

```sh
python3 scripts/test_status_sync.py
python3 scripts/test_status_modes.py
python3 project/reviews/substantive/2026-09-24/test_integrity_repairs.py
python3 project/reviews/substantive/2026-09-24/check_finite_evidence.py
python3 project/research/general_n/2026-09-22-r9-quotient-v1/audit_r9_support8_orbits.py
python3 scripts/check_repository_text_integrity.py
python3 tools/check_readme_review_materials.py
```

The row driver is `project/research/general_n/2026-09-23-independent-742-r12-count-audit/screen_exact_star_row.py`; use `n Delta --records-jsonl OUTPUT --case-time-limit SECONDS`. An UNKNOWN is a failed completeness gate, never an exclusion. Original uncompressed streams, logs, tests and proposed source are also retained in the delivered review archive. The final publication check distinguishes executed test results from a proposed checklist.
