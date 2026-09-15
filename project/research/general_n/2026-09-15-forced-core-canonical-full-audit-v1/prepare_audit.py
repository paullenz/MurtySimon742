#!/usr/bin/env python3
import csv, hashlib, json, sys
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit("usage: prepare_audit.py SOURCE_FINAL_DIR SOURCE_PLAN_DIR OUT_DIR")

final_dir=Path(sys.argv[1]); plan_dir=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
here=Path(__file__).resolve().parent
old=here.parent/"2026-09-15-forced-core-canonical-audit-v1"

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def keyfile(path):
    with path.open(newline="") as f:
        return [(int(r["layer"]),int(r["state_id"])) for r in csv.DictReader(f,delimiter="\t")]

summary=json.loads((final_dir/"SUMMARY.json").read_text())
if summary.get("source_results_sha256")!="2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970":
    raise SystemExit("unexpected promoted-relational source hash")
if summary.get("new_candidate_whole_state_exclusions")!=170 or summary.get("rescanned_survivors")!=136 or summary.get("rescanned_targets")!=306:
    raise SystemExit("unexpected final summary counts")

with (final_dir/"RESULTS.tsv").open(newline="") as f:
    results=list(csv.DictReader(f,delimiter="\t"))
rmap={(int(r["layer"]),int(r["state_id"])):r for r in results}
if len(rmap)!=306:
    raise SystemExit("RESULTS.tsv does not have 306 unique keys")
cand=sorted(k for k,r in rmap.items() if r["status"]=="FORCED_CORE_EXCLUDED")
surv=sorted(k for k,r in rmap.items() if r["status"]=="SURVIVES_FORCED_CORE")
if len(cand)!=170 or len(surv)!=136 or any(k[0]!=0 for k in cand):
    raise SystemExit("unexpected candidate/survivor partition")

committed_cand=sorted(keyfile(here/"CANDIDATE_KEYS.tsv"))
committed_surv=sorted(keyfile(here/"RESCAN_SURVIVOR_KEYS.tsv"))
if cand!=committed_cand or surv!=committed_surv:
    raise SystemExit("committed classification does not match authoritative final artifact")

with (old/"CERTIFIED_RESCUES.tsv").open(newline="") as f:
    old_rescues={(int(r["layer"]),int(r["state_id"])) for r in csv.DictReader(f,delimiter="\t")}
expected_extra={(0,x) for x in [2454,3145,4453,4618,5163,5672,5972,7664,7851,7927,9014,9849]}
if len(old_rescues)!=124 or not old_rescues <= set(surv) or set(surv)-old_rescues!=expected_extra:
    raise SystemExit("124+12 rescue reconciliation failed")

with (old/"INDEPENDENT_CLOSURE_MATCHES.tsv").open(newline="") as f:
    old_matches=list(csv.DictReader(f,delimiter="\t"))
old_keys={(int(r["layer"]),int(r["state_id"])) for r in old_matches}
if len(old_keys)!=24 or not old_keys <= set(cand):
    raise SystemExit("initial 24 independent matches are not a subset of final 170")

primary_fields=[
    "profiles_tested","paircap_fail","paircap_pass","incidence_fail","incidence_pass",
    "pairhall_fail","pairhall_pass","targethall_fail","targethall_pass","cost_fail","cost_pass",
    "core_fail","core_capacity_fail","core_high_fail","status"
]
for r in old_matches:
    k=(int(r["layer"]),int(r["state_id"]))
    if any(r[f]!=rmap[k][f] for f in primary_fields):
        raise SystemExit(f"initial independent row no longer matches final primary counts at {k}")

lines=(plan_dir/"TARGET_INPUT.txt").read_text().splitlines()
if not lines or int(lines[0])!=306:
    raise SystemExit("unexpected TARGET_INPUT count")
target={}
for line in lines[1:]:
    p=line.split()
    target[(int(p[0]),int(p[1]))]=line
if set(target)!=set(rmap):
    raise SystemExit("target-input keys do not match final result keys")

(out/"AUDIT_INPUT.txt").write_text("170\n"+"\n".join(target[k] for k in cand)+"\n")
det_cols=[
    "layer","state_id","S","Emax","profiles_tested","paircap_fail","paircap_pass",
    "incidence_fail","incidence_pass","pairhall_fail","pairhall_pass",
    "targethall_fail","targethall_pass","cost_fail","cost_pass",
    "core_fail","core_capacity_fail","core_high_fail","status"
]
with (out/"PRIMARY_CANDIDATE_COUNTS.tsv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=det_cols,delimiter="\t",lineterminator="\n"); w.writeheader()
    for k in cand: w.writerow({c:rmap[k][c] for c in det_cols})

extra_cols=["layer","state_id","S","Emax","profiles_tested","status","witness_E","witness_cost","witness_envelope","witness_rho","witness_q"]
with (out/"FULL_ENUMERATION_ONLY_RESCUES.tsv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=extra_cols,delimiter="\t",lineterminator="\n"); w.writeheader()
    for k in sorted(expected_extra): w.writerow({c:rmap[k][c] for c in extra_cols})

receipt={
    "schema":"forced-core-canonical-reconciliation-v1",
    "source_discovery_run":34950746007,
    "source_results_sha256":summary["source_results_sha256"],
    "source_summary_sha256":sha256(final_dir/"SUMMARY.json"),
    "source_results_tsv_sha256":sha256(final_dir/"RESULTS.tsv"),
    "source_candidate_keys_sha256":sha256(final_dir/"CANDIDATE_KEYS.tsv"),
    "source_plan_json_sha256":sha256(plan_dir/"PLAN.json"),
    "source_target_input_sha256":sha256(plan_dir/"TARGET_INPUT.txt"),
    "candidate_count":len(cand),
    "survivor_count":len(surv),
    "candidate_n34_count":sum(k[0]==0 for k in cand),
    "candidate_n35_count":sum(k[0]==1 for k in cand),
    "old_rescue_count":len(old_rescues),
    "full_enumeration_only_rescues":sorted(k[1] for k in set(surv)-old_rescues),
    "old_independent_match_count":len(old_keys),
    "pass":True,
}
(out/"RECONCILIATION.json").write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
print(json.dumps(receipt,sort_keys=True))
