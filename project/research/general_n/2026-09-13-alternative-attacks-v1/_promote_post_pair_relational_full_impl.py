#!/usr/bin/env python3
"""Promote the fully audited post-pair relational closure family.

This script is intentionally narrow and hash-gated. It may run only from the
one-shot GitHub Actions promotion workflow after the discovery and independent
audit artifacts have been downloaded from their pinned run IDs.

It does not rerun or alter audit 34854911792. It performs the separate reviewed
ledger step required by the repository's standing promotion gate.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import csv
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N34_LEDGER = HERE / "WHOLE_STATE_LEDGER.tsv"
N35_LEDGER = HERE / "WHOLE_STATE_LEDGER_N35.tsv"
FRONTIER = HERE / "POST_PAIR_RELATIONAL_FULL_FRONTIER.md"
EVIDENCE = ROOT / "RESEARCH_EVIDENCE_INDEX.md"
README = ROOT / "README.md"
CURRENT = ROOT / "CURRENT_STATE.md"

SOURCE_RUN = 34844403328
AUDIT_RUN = 34854911792
SOURCE_RESULTS_SHA256 = "2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970"
KEYS_SHA256 = "67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2"
AUDIT_CANDIDATE_INPUT_SHA256 = "fbcbef0d532a52f4d4897fc4c63ec3ebbe534ac2ba01335dccd4cb1057147f83"
BASE_N34_BLOB = "7b5c50eeed94b198dde4584ec6efeb2b4992fcc4"
BASE_N35_BLOB = "411fff42fd3d0839c1642a541ec7605d7ab146e2"
BASE_N34_COUNT = 977
BASE_N35_COUNT = 0
CANDIDATE_N34 = 2580
CANDIDATE_N35 = 75
CANDIDATE_TOTAL = 2655
FINAL_N34 = 3557
FINAL_N35 = 75
FINAL_CLOSURES = 3632
FINAL_EXCLUSIONS = 4626
FINAL_SURVIVORS = 952
FINAL_N34_SURVIVORS = 949
FINAL_N35_SURVIVORS = 3
METHOD = "post-pair relational full independent-audit closure"
RECORD = "POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.md"


def die(msg: str) -> None:
    raise SystemExit(msg)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def one(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        die(f"expected exactly one {name} under {root}, found {len(hits)}")
    return hits[0]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def key_pairs(path: Path) -> list[tuple[int, int]]:
    rows = read_tsv(path)
    if rows and list(rows[0].keys()) != ["layer", "state_id"]:
        die(f"unexpected candidate key columns in {path}")
    pairs = [(int(r["layer"]), int(r["state_id"])) for r in rows]
    if len(pairs) != len(set(pairs)):
        die(f"duplicate candidate key in {path}")
    return pairs


def ledger_rows(path: Path) -> list[dict[str, str]]:
    rows = read_tsv(path)
    for r in rows:
        if set(r) != {"state", "method", "record"}:
            die(f"unexpected ledger columns in {path}: {r.keys()}")
    ids = [int(r["state"]) for r in rows]
    if len(ids) != len(set(ids)):
        die(f"duplicate state in {path}")
    return rows


def git_blob(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path.relative_to(ROOT))],
        cwd=ROOT,
        text=True,
    ).strip()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        die(f"{label}: expected one replacement target, found {count}: {old[:120]!r}")
    return text.replace(old, new, 1)


def append_ledger(path: Path, ids: list[int]) -> None:
    raw = path.read_text()
    if not raw.endswith("\n"):
        die(f"{path.name} must end with newline")
    addition = "".join(f"{state}\t{METHOD}\t{RECORD}\n" for state in sorted(ids))
    path.write_text(raw + addition)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--discovery", type=Path, required=True)
    ap.add_argument("--audit", type=Path, required=True)
    args = ap.parse_args()

    source_results = one(args.discovery, "POST_PAIR_RELATIONAL_FULL_FINAL_RESULTS.tsv")
    source_summary = one(args.discovery, "POST_PAIR_RELATIONAL_FULL_FINAL_SUMMARY.json")
    source_keys = one(args.discovery, "POST_PAIR_RELATIONAL_FULL_FINAL_CANDIDATES.tsv")
    source_unresolved = one(args.discovery, "POST_PAIR_RELATIONAL_FULL_FINAL_UNRESOLVED.json")
    audit_summary = one(args.audit, "FULL_RELATIONAL_FINAL_AUDIT_SUMMARY.json")
    audit_keys = one(args.audit, "FULL_RELATIONAL_FINAL_AUDITED_KEYS.tsv")

    if sha256(source_results) != SOURCE_RESULTS_SHA256:
        die("source discovery results hash mismatch")
    if sha256(source_keys) != KEYS_SHA256 or sha256(audit_keys) != KEYS_SHA256:
        die("candidate/audited key hash mismatch")
    if source_keys.read_bytes() != audit_keys.read_bytes():
        die("discovery candidate keys and independently audited keys are not byte-identical")
    if json.loads(source_unresolved.read_text()) != {}:
        die("source discovery unresolved file is nonempty")

    ss = json.loads(source_summary.read_text())
    expected_source = {
        "schema": "post-pair-relational-full-discovery-final-v1",
        "retry_workflow_run_id": SOURCE_RUN,
        "results_sha256": SOURCE_RESULTS_SHA256,
        "candidates_sha256": KEYS_SHA256,
        "expected_frontier": 3607,
        "states_completed": 3607,
        "relational_excluded_candidates": CANDIDATE_TOTAL,
        "relational_excluded_n34": CANDIDATE_N34,
        "relational_excluded_n35": CANDIDATE_N35,
        "survives_relational": FINAL_SURVIVORS,
        "survives_n34": FINAL_N34_SURVIVORS,
        "survives_n35": FINAL_N35_SURVIVORS,
        "unresolved_count": 0,
        "unattempted_count": 0,
        "discovery_complete": True,
    }
    for k, v in expected_source.items():
        if ss.get(k) != v:
            die(f"source summary mismatch {k}: {ss.get(k)!r} != {v!r}")

    aa = json.loads(audit_summary.read_text())
    expected_audit = {
        "schema": "post-pair-relational-full-independent-audit-v1",
        "source_recovery_run_id": SOURCE_RUN,
        "source_results_sha256": SOURCE_RESULTS_SHA256,
        "candidate_input_sha256": AUDIT_CANDIDATE_INPUT_SHA256,
        "candidate_count": CANDIDATE_TOTAL,
        "candidate_n34": CANDIDATE_N34,
        "candidate_n35": CANDIDATE_N35,
        "states_audited": CANDIDATE_TOTAL,
        "unresolved_count": 0,
        "result": "PASS",
        "promotion_status": "AUDIT_COMPLETE_NOT_YET_LEDGER_PROMOTED",
    }
    for k, v in expected_audit.items():
        if aa.get(k) != v:
            die(f"audit summary mismatch {k}: {aa.get(k)!r} != {v!r}")

    pairs = key_pairs(source_keys)
    if len(pairs) != CANDIDATE_TOTAL:
        die(f"candidate key count {len(pairs)} != {CANDIDATE_TOTAL}")
    n34_ids = [state for layer, state in pairs if layer == 0]
    n35_ids = [state for layer, state in pairs if layer == 1]
    if len(n34_ids) != CANDIDATE_N34 or len(n35_ids) != CANDIDATE_N35:
        die("candidate layer counts mismatch")
    if any(layer not in (0, 1) for layer, _ in pairs):
        die("unexpected layer in candidate keys")

    results = read_tsv(source_results)
    if len(results) != 3607:
        die(f"source result row count {len(results)} != 3607")
    excluded = {
        (int(r["layer"]), int(r["state_id"]))
        for r in results if r["status"] == "RELATIONAL_EXCLUDED"
    }
    survivors = [r for r in results if r["status"] == "SURVIVES_RELATIONAL"]
    other = [r for r in results if r["status"] not in {"RELATIONAL_EXCLUDED", "SURVIVES_RELATIONAL"}]
    if other:
        die(f"unexpected discovery statuses: {sorted({r['status'] for r in other})}")
    if excluded != set(pairs):
        die("discovery excluded-key set differs from audited candidate keys")
    if len(survivors) != FINAL_SURVIVORS:
        die("discovery survivor count mismatch")
    if sum(int(r["layer"]) == 0 for r in survivors) != FINAL_N34_SURVIVORS:
        die("N34 survivor count mismatch")
    if sum(int(r["layer"]) == 1 for r in survivors) != FINAL_N35_SURVIVORS:
        die("N35 survivor count mismatch")

    if git_blob(N34_LEDGER) != BASE_N34_BLOB:
        die(f"N34 ledger changed since reviewed base: {git_blob(N34_LEDGER)}")
    if git_blob(N35_LEDGER) != BASE_N35_BLOB:
        die(f"N35 ledger changed since reviewed base: {git_blob(N35_LEDGER)}")
    old34 = ledger_rows(N34_LEDGER)
    old35 = ledger_rows(N35_LEDGER)
    if len(old34) != BASE_N34_COUNT or len(old35) != BASE_N35_COUNT:
        die(f"unexpected base ledger sizes: N34={len(old34)} N35={len(old35)}")
    old34ids = {int(r["state"]) for r in old34}
    old35ids = {int(r["state"]) for r in old35}
    if old34ids.intersection(n34_ids):
        die("audited N34 promotion keys overlap existing N34 ledger")
    if old35ids.intersection(n35_ids):
        die("audited N35 promotion keys overlap existing N35 ledger")

    audit_record = {
        "schema": "post-pair-relational-full-promotion-audit-v1",
        "promotion_status": "PROMOTED",
        "external_review": "OPEN",
        "source_discovery_run_id": SOURCE_RUN,
        "independent_audit_run_id": AUDIT_RUN,
        "source_results_sha256": SOURCE_RESULTS_SHA256,
        "audited_keys_sha256": KEYS_SHA256,
        "audit_candidate_input_sha256": AUDIT_CANDIDATE_INPUT_SHA256,
        "source_frontier": 3607,
        "audited_candidates": CANDIDATE_TOTAL,
        "audited_n34": CANDIDATE_N34,
        "audited_n35": CANDIDATE_N35,
        "unresolved": 0,
        "base_ledger_n34": BASE_N34_COUNT,
        "base_ledger_n35": BASE_N35_COUNT,
        "promoted_ledger_n34": FINAL_N34,
        "promoted_ledger_n35": FINAL_N35,
        "whole_state_closures": FINAL_CLOSURES,
        "canonical_exclusions": FINAL_EXCLUSIONS,
        "canonical_survivors": FINAL_SURVIVORS,
        "survivors_n34": FINAL_N34_SURVIVORS,
        "survivors_n35": FINAL_N35_SURVIVORS,
        "note": (
            "Separate reviewed ledger step after complete two-implementation audit. "
            "This finite promotion remains conditional on the canonical bridge and "
            "does not prove the unrestricted Murty-Simon conjecture."
        ),
    }
    audit_json = HERE / "POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.json"
    audit_json.write_text(json.dumps(audit_record, indent=2, sort_keys=True) + "\n")
    audit_md = HERE / RECORD
    audit_md.write_text(
        "# Full post-pair relational promotion audit\n\n"
        "14 September 2026. **Reviewed ledger promotion after complete independent-implementation audit; "
        "external mathematical review and third-party reproduction remain OPEN. This is not an unrestricted "
        "Murty-Simon proof.**\n\n"
        "## Frozen evidence\n\n"
        f"- Discovery/recovery run: `{SOURCE_RUN}`; complete 3,607-state result SHA-256 "
        f"`{SOURCE_RESULTS_SHA256}`.\n"
        f"- Independent audit run: `{AUDIT_RUN}`; 256 shards plus successful aggregate requiring complete "
        "two-implementation agreement.\n"
        f"- Discovery candidate-key TSV and final audited-key TSV are byte-identical: SHA-256 `{KEYS_SHA256}`.\n"
        f"- Audit candidate-input SHA-256: `{AUDIT_CANDIDATE_INPUT_SHA256}`.\n"
        "- Unresolved states: **0** in discovery and **0** in the independent audit.\n\n"
        "## Reviewed ledger reconciliation\n\n"
        f"The audited family contains **{CANDIDATE_TOTAL:,}** closures: **{CANDIDATE_N34:,} N34** and "
        f"**{CANDIDATE_N35} N35**. The reviewed pre-promotion ledgers contained "
        f"**{BASE_N34_COUNT} N34** and **{BASE_N35_COUNT} N35** closures, with zero overlap with the "
        "audited family. Promotion therefore gives:\n\n"
        "```text\n"
        f"N34 whole-state ledger: {FINAL_N34:,}\n"
        f"N35 whole-state ledger: {FINAL_N35:,}\n"
        f"whole-state closures:   {FINAL_CLOSURES:,}\n"
        f"canonical exclusions:   {FINAL_EXCLUSIONS:,}\n"
        f"canonical survivors:      {FINAL_SURVIVORS:,}\n"
        f"  N34 survivors:           {FINAL_N34_SURVIVORS:,}\n"
        f"  N35 survivors:             {FINAL_N35_SURVIVORS}\n"
        "```\n\n"
        "The finite accounting universe is unchanged: 4,626 + 952 = 5,578. The promotion changes the "
        "canonical finite frontier, not the status of the unrestricted conjecture or the external-review "
        "dependency of the graph-to-selected/residual bridge.\n"
    )

    append_ledger(N34_LEDGER, n34_ids)
    append_ledger(N35_LEDGER, n35_ids)
    new34 = ledger_rows(N34_LEDGER)
    new35 = ledger_rows(N35_LEDGER)
    if len(new34) != FINAL_N34 or len(new35) != FINAL_N35:
        die(f"post-promotion ledger sizes wrong: {len(new34)}, {len(new35)}")
    if len({int(r["state"]) for r in new34}) != FINAL_N34:
        die("duplicate N34 state after promotion")
    if len({int(r["state"]) for r in new35}) != FINAL_N35:
        die("duplicate N35 state after promotion")
    if any(r["method"] != METHOD or r["record"] != RECORD for r in new34[-CANDIDATE_N34:]):
        die("N34 appended provenance mismatch")
    if any(r["method"] != METHOD or r["record"] != RECORD for r in new35[-CANDIDATE_N35:]):
        die("N35 appended provenance mismatch")

    audit_record["promoted_n34_ledger_sha256"] = sha256(N34_LEDGER)
    audit_record["promoted_n35_ledger_sha256"] = sha256(N35_LEDGER)
    audit_json.write_text(json.dumps(audit_record, indent=2, sort_keys=True) + "\n")

    ftext = FRONTIER.read_text()
    if "## Promotion receipt — 14 September 2026" in ftext:
        die("promotion receipt already present")
    FRONTIER.write_text(
        ftext
        + "\n## Promotion receipt — 14 September 2026\n\n"
        + f"The separate promotion gate is now complete. Discovery run `{SOURCE_RUN}` covered all 3,607 "
          f"then-current survivors with zero unresolved states and identified {CANDIDATE_TOTAL:,} candidate "
          "closures. Independent audit run "
        + f"`{AUDIT_RUN}` audited exactly the same byte-identical key set with two implementations and a "
          "successful aggregate requiring complete agreement. The reviewed ledger step found no overlap with "
          f"the existing ledgers and promoted {CANDIDATE_N34:,} N34 plus {CANDIDATE_N35} N35 closures. "
          f"The canonical finite frontier is therefore **{FINAL_EXCLUSIONS:,} exclusions / "
          f"{FINAL_SURVIVORS:,} survivors / {FINAL_CLOSURES:,} whole-state closures**, with "
          f"{FINAL_N34_SURVIVORS} N34 and {FINAL_N35_SURVIVORS} N35 survivors. "
          f"See [`{RECORD}`]({RECORD}) and "
          "[`POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.json`](POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.json). "
          "**The unrestricted conjecture is not claimed proved; external review remains open.**\n"
    )

    text = README.read_text()
    text = replace_once(
        text,
        "| Canonical finite frontier | **1,971 exclusions / 3,607 survivors; 977 quantified whole-state closures** — unchanged |",
        "| Canonical finite frontier | **4,626 exclusions / 952 survivors; 3,632 quantified whole-state closures** after reviewed promotion of the fully audited relational family |",
        "README canonical frontier",
    )
    text = replace_once(
        text,
        "| Relational candidates | **2,655 recovered candidates remain UNPROMOTED** pending completed independent audit and separate reviewed ledger promotion; audit run **34854911792 SUCCESS**, promotion workflow pending |",
        "| Relational audit/promotion | **2,655/2,655 audited keys promoted** after run **34854911792 SUCCESS** and reviewed ledger reconciliation: 2,580 N34 + 75 N35 closures; 949 N34 + 3 N35 survivors remain |",
        "README relational row",
    )
    text = replace_once(
        text,
        "**Checkpoint — 14 September 2026, `relational-ledger-validation-v1`.** Inspected predecessor `13d62aeb7abb1c84acb483610c0667c905709025`. The full 2,655-key audit is now confirmed complete and green, with byte-identical discovery/audit key ledgers and zero unresolved states. This commit installs the hash-gated separate ledger-promotion step and fixes target reconstruction to subtract both N34 and N35 ledgers. **Mathematical status unchanged in this preparatory commit; canonical counts remain 1,971 / 3,607 / 977 until the promotion workflow itself succeeds.**",
        "**Checkpoint — 14 September 2026, `relational-ledger-promotion-v1`.** The separate reviewed ledger step has completed after discovery run **34844403328** and independent audit run **34854911792**. Exact source/result/key hashes, complete dual agreement, zero unresolved states, base-ledger non-overlap and final ledger counts were checked before publication. **Canonical finite frontier promoted to 4,626 exclusions / 952 survivors / 3,632 whole-state closures.** Fixed-order candidates, general7/12 candidate, row108/row471 sample results and their verification status are otherwise unchanged. External mathematical review remains OPEN.",
        "README checkpoint",
    )
    text = replace_once(
        text,
        "The2,655 recovered relational candidates have completed the full two-implementation audit (run34854911792 SUCCESS, zero unresolved, successful aggregate) but still require the separate reviewed ledger step before promotion. This commit installs that hash-gated promotion step; no candidate is promoted by this preparatory commit.",
        "The 2,655 recovered relational candidates completed full discovery and two-implementation audit, then the separate reviewed ledger step. All 2,655 are now ledger-promoted with pinned hashes and zero unresolved states. This finite closure family remains conditional on the canonical bridge and does not replace external specialist review.",
        "README audit gate",
    )
    text = text.replace("<!-- RELATIONAL-FULL-PROMOTION:PENDING -->", "<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->")
    README.write_text(text)

    text = CURRENT.read_text()
    text = replace_once(
        text,
        "**14 September 2026 — checkpoint `relational-ledger-validation-v1`.** Inspected predecessor: `13d62aeb7abb1c84acb483610c0667c905709025`. The 2,655-key relational audit is confirmed complete: exact discovery/audit key sets are byte-identical, all 256 audit shards plus aggregate succeeded, both implementations agree, and unresolved count is zero. This commit installs the hash-gated separate reviewed-ledger promotion step and updates target reconstruction to respect both N34 and N35 ledgers. **Mathematical status unchanged in this preparatory commit; canonical counts remain unchanged until that promotion workflow succeeds.**",
        "**14 September 2026 — checkpoint `relational-ledger-promotion-v1`.** The separate reviewed-ledger gate has completed after full discovery run `34844403328` and independent audit run `34854911792`. The candidate key files are byte-identical; all 2,655 keys have dual agreement; unresolved count is zero; the reviewed base ledgers were non-overlapping; and the promoted ledgers reconcile exactly. **Canonical finite frontier is now 4,626 exclusions / 952 survivors / 3,632 whole-state closures.** Fixed-order/general candidate and boundary-profile mathematical status is otherwise unchanged; external review remains OPEN.",
        "CURRENT checkpoint",
    )
    text = replace_once(
        text,
        "whole-state closures:               977\ncanonical exclusions:             1,971\ncanonical survivors:              3,607\nrecovered relational candidates:  2,655 — AUDIT COMPLETE / LEDGER REVIEW PENDING",
        "whole-state closures:             3,632\ncanonical exclusions:             4,626\ncanonical survivors:                952\n  N34-derived survivors:             949\n  N35-derived survivors:               3\nrecovered relational candidates:  2,655 — AUDITED AND PROMOTED",
        "CURRENT canonical block",
    )
    pending_section = (
        "## Relational validation lane — audit complete, promotion pending\n\n"
        "Run `34854911792` completed successfully after auditing all 2,655 recovered keys "
        "with two independent implementations over 256 shards and a successful aggregate requiring complete "
        "agreement. The discovery and audit key TSVs are byte-identical (SHA256 `67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2`), and both "
        "report zero unresolved states. The separate reviewed-ledger step is installed by this checkpoint but "
        "has not yet run; therefore no canonical count changes are claimed here.\n\n"
    )
    promoted_section = (
        "## Relational validation lane — promoted\n\n"
        "Discovery/recovery run `34844403328` and independent audit run `34854911792` cover the exact same "
        "2,655-key set (SHA256 `67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2`), with zero unresolved states and successful "
        "two-implementation aggregate agreement. The separate reviewed ledger step confirmed zero overlap with "
        "the pre-existing ledgers and promoted 2,580 N34 plus 75 N35 closures. "
        "The remaining relational frontier is 952 states: 949 N34 and 3 N35. "
        "See the promotion audit in the alternative-attacks package. This remains "
        "finite evidence conditional on the canonical bridge, not an unrestricted proof.\n\n"
    )
    text = replace_once(text, pending_section, promoted_section, "CURRENT validation section")
    text = replace_once(
        text,
        "The2,655 recovered relational candidates have now cleared complete coverage, both implementations agreeing, zero unresolved cases and a successful aggregate in run34854911792. The final separate reviewed-ledger step is installed by this checkpoint and remains the only promotion gate. Sample exclusions do not change that gate. Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge.",
        "The 2,655 recovered relational candidates have now cleared complete coverage, dual agreement, zero unresolved cases, successful aggregate and the separate reviewed-ledger step. Their ledger promotion changes only the canonical finite frontier. Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge.",
        "CURRENT audit gate",
    )
    text = text.replace("<!-- RELATIONAL-FULL-PROMOTION:PENDING -->", "<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->")
    CURRENT.write_text(text)

    text = EVIDENCE.read_text()
    text = replace_once(
        text,
        "This index distinguishes derivation, finite verification, preservation and external acceptance. It does not promote the 2,655 recovered relational candidates. The canonical frontier remains 1,971 exclusions / 3,607 survivors / 977 whole-state closures. Fixed-order reviewer packages retain their separate status in [the reviewer index](releases/REVIEW_READY_INDEX.md).",
        "This index distinguishes derivation, finite verification, preservation and external acceptance. The fully audited 2,655-key relational family has now passed the separate reviewed-ledger step and is promoted. The canonical finite frontier is 4,626 exclusions / 952 survivors / 3,632 whole-state closures. Fixed-order reviewer packages retain their separate status in [the reviewer index](releases/REVIEW_READY_INDEX.md).",
        "evidence intro",
    )
    start = text.index("## Relational audit: separate scope")
    end = text.index("## Review obligations", start)
    relational = (
        "## Relational audit and reviewed promotion\n\n"
        "Discovery/recovery run `34844403328` completed all 3,607 then-current canonical survivors and "
        "identified 2,655 relational candidate closures (2,580 N34, 75 N35) with zero unresolved states. "
        "Complete result SHA256: `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`; "
        "candidate-key SHA256: `67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2`.\n\n"
        "Independent audit run `34854911792` completed all 256 shards plus the aggregate. Its final aggregate "
        "required complete agreement between two independently compiled implementations. The final audited-key "
        "TSV is byte-identical to the discovery candidate-key TSV, and the audit reports zero unresolved cases. "
        "The separate reviewed-ledger step then confirmed non-overlap with the existing 977/0 N34/N35 ledgers "
        "and promoted all 2,655 keys. Canonical accounting is now 4,626 exclusions / 952 survivors / 3,632 "
        "whole-state closures, leaving 949 N34 and 3 N35 survivors.\n\n"
        "See [`POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.md) and the "
        "[machine-readable promotion audit](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_FULL_PROMOTION_AUDIT.json). This is a finite promotion conditional on the "
        "canonical bridge; external mathematical review and independent third-party reproduction remain OPEN.\n\n"
    )
    text = text[:start] + relational + text[end:]
    EVIDENCE.write_text(text)

    if FINAL_EXCLUSIONS + FINAL_SURVIVORS != 5578:
        die("final catalogue accounting arithmetic mismatch")

    print(json.dumps({
        "result": "PROMOTION_READY_TO_COMMIT",
        "promoted": CANDIDATE_TOTAL,
        "n34": CANDIDATE_N34,
        "n35": CANDIDATE_N35,
        "whole_state_closures": FINAL_CLOSURES,
        "canonical_exclusions": FINAL_EXCLUSIONS,
        "canonical_survivors": FINAL_SURVIVORS,
        "n34_survivors": FINAL_N34_SURVIVORS,
        "n35_survivors": FINAL_N35_SURVIVORS,
        "n34_ledger_sha256": sha256(N34_LEDGER),
        "n35_ledger_sha256": sha256(N35_LEDGER),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
