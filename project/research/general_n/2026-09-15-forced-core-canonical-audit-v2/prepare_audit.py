#!/usr/bin/env python3
from __future__ import annotations
import csv, json, sys
from pathlib import Path

EXPECTED_TARGETS=306
EXPECTED_CANDIDATES=170
EXPECTED_RESCANNED_SURVIVORS=136
EXPECTED_ROUTE_SURVIVORS=782
EXPECTED_N35_CANDIDATES=0
FINAL_DIGEST='sha256:60409b6049e9436aeaaaf898509f7022abb3b3ade030359174379ba22e238705'

def parse_state_lines(path: Path):
    lines=[x.strip() for x in path.read_text().splitlines() if x.strip()]
    n=int(lines[0]); body=lines[1:]
    if len(body)!=n: raise SystemExit(f'target input count mismatch {len(body)} != {n}')
    return {(int(x.split()[0]),int(x.split()[1])):x for x in body}

def ints(s): return [] if not s else [int(x) for x in s.split(',')]

def main():
    if len(sys.argv)!=4: raise SystemExit('usage: prepare_audit.py PLAN_DIR DISCOVERY_DIR OUTDIR')
    plan=Path(sys.argv[1]); disc=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
    states=parse_state_lines(plan/'TARGET_INPUT.txt')
    if len(states)!=EXPECTED_TARGETS: raise SystemExit('expected 306 target states')
    with (disc/'RESULTS.tsv').open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    if len(rows)!=EXPECTED_TARGETS: raise SystemExit('discovery results count mismatch')
    bykey={(int(r['layer']),int(r['state_id'])):r for r in rows}
    if set(bykey)!=set(states): raise SystemExit('discovery/plan key mismatch')
    cand=[r for r in rows if r['status']=='FORCED_CORE_EXCLUDED']
    surv=[r for r in rows if r['status']=='SURVIVES_FORCED_CORE']
    if len(cand)!=EXPECTED_CANDIDATES or len(surv)!=EXPECTED_RESCANNED_SURVIVORS: raise SystemExit('170/136 split mismatch')
    if sum(int(r['layer'])==1 for r in cand)!=EXPECTED_N35_CANDIDATES: raise SystemExit('unexpected N35 candidate')
    ckeys=[(int(r['layer']),int(r['state_id'])) for r in cand]
    (out/'CANDIDATE_INPUT.txt').write_text(str(len(ckeys))+'\n'+'\n'.join(states[k] for k in ckeys)+'\n')
    with (out/'PRIMARY_CANDIDATE_RESULTS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t'); w.writeheader(); w.writerows(cand)
    rec=[str(len(surv))]
    for r in surv:
        k=(int(r['layer']),int(r['state_id'])); q=ints(r['witness_q']); rho=ints(r['witness_rho'])
        if not q or not rho or len(q)!=len(rho): raise SystemExit(f'missing witness {k}')
        rec.append(states[k]+' '+str(len(q))+' '+' '.join(map(str,q))+' '+str(len(rho))+' '+' '.join(map(str,rho)))
    (out/'SURVIVOR_WITNESSES.txt').write_text('\n'.join(rec)+'\n')
    with (out/'PRIMARY_SURVIVOR_RESULTS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t'); w.writeheader(); w.writerows(surv)
    summary={
      'schema':'canonical-forced-core-independent-audit-v2-plan',
      'target_count':len(states),'candidate_count':len(cand),'rescanned_survivor_count':len(surv),
      'route_survivor_count':EXPECTED_ROUTE_SURVIVORS,'n35_candidate_count':0,
      'candidate_keys':[list(k) for k in ckeys], 'discovery_artifact_digest':FINAL_DIGEST,
      'promotion_status':'AUDIT_PLAN_ONLY_NOT_PROMOTED'
    }
    (out/'PLAN.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'candidates':len(cand),'survivors':len(surv)}))
if __name__=='__main__': main()
