#!/usr/bin/env python3
"""Summarize all-excess orientation/variable-incidence scan output."""
from pathlib import Path
import argparse
import csv
import hashlib
import json


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("--output",default="ORIENTATION_ALL_EXCESS_SUMMARY.json"); a=ap.parse_args()
    p=Path(a.input)
    with p.open() as f: rows=list(csv.DictReader(f,delimiter="\t"))
    exc=[r for r in rows if r["status"]=="ALL_EXCESS_EXCLUDED"]
    surv=[r for r in rows if r["status"]=="SURVIVES_RELAXATION"]
    stages={k:sum(int(r[k]) for r in rows) for k in ["incidence_fail","cap_fail","prefix_fail","pair_fail","target_fail"]}
    hard=sorted(rows,key=lambda r:(float(r["seconds"]),int(r["profiles_tested"])),reverse=True)[:20]
    report={
      "schema":"orientation-all-excess-scan-summary-v1",
      "input_tsv_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
      "states":len(rows),"all_excess_excluded":len(exc),"survives_relaxation":len(surv),
      "all_excess_excluded_state_ids":[int(r["state_id"]) for r in exc],
      "surviving_state_ids":[int(r["state_id"]) for r in surv],
      "stage_failure_profile_counts":stages,
      "profiles_tested":sum(int(r["profiles_tested"]) for r in rows),
      "total_reported_seconds":sum(float(r["seconds"]) for r in rows),
      "witness_excess_histogram":{},
      "hardest_states":[{"state_id":int(r["state_id"]),"status":r["status"],"profiles_tested":int(r["profiles_tested"]),"seconds":float(r["seconds"]),"witness_Q":int(r["witness_Q"]),"S":int(r["S"])} for r in hard],
      "proof_scope":"ALL_EXCESS_EXCLUDED means every symmetry-reduced q profile with Q>=S and within the universal source/incoming bounds failed either the exact variable-x selected-incidence circulation or a universal orientation necessary condition. Under the canonical bridge this excludes the whole scalar state, not merely E=0.",
      "survival_scope":"SURVIVES_RELAXATION means one q profile and some variable selected-label degree allocation survive these necessary conditions. It does not assert graph feasibility.",
      "external_review":"OPEN"
    }
    hist={}
    for r in surv:
        e=int(r["witness_Q"])-int(r["S"]); hist[str(e)]=hist.get(str(e),0)+1
    report["witness_excess_histogram"]={k:hist[k] for k in sorted(hist,key=lambda x:int(x))}
    Path(a.output).write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
