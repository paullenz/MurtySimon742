#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
if len(sys.argv)!=4:
    raise SystemExit('usage: compare_independent.py PRIMARY_RESULTS.tsv INDEPENDENT.tsv OUTDIR')
primary, independent, outdir=map(Path,sys.argv[1:]); outdir.mkdir(parents=True,exist_ok=True)
fields=['layer','state_id','profiles_tested','paircap_fail','paircap_pass','incidence_fail','incidence_pass','pairhall_fail','pairhall_pass','targethall_fail','targethall_pass','cost_fail','cost_pass','core_fail','core_capacity_fail','core_high_fail','status']
def load(p):
    with p.open(newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
P=[r for r in load(primary) if r['status']=='FORCED_CORE_EXCLUDED']
I=load(independent)
assert len(P)==170, len(P); assert len(I)==170, len(I)
pd={(r['layer'],r['state_id']):r for r in P}; idd={(r['layer'],r['state_id']):r for r in I}
assert set(pd)==set(idd), (sorted(set(pd)-set(idd)),sorted(set(idd)-set(pd)))
mismatches=[]
for k in sorted(pd,key=lambda x:(int(x[0]),int(x[1]))):
    for f in fields:
        if pd[k][f] != idd[k][f]: mismatches.append({'layer':k[0],'state_id':k[1],'field':f,'primary':pd[k][f],'independent':idd[k][f]})
with (outdir/'MISMATCHES.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['layer','state_id','field','primary','independent'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(mismatches)
matched=170-len({(x['layer'],x['state_id']) for x in mismatches})
summary={'schema':'forced-core-independent-full-audit-v1','candidate_states':170,'matched_states':matched,'mismatch_cells':len(mismatches),'exact_match':not mismatches,'fields_compared':fields}
(outdir/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
if mismatches:
    print(json.dumps(summary,indent=2)); raise SystemExit(1)
with (outdir/'INDEPENDENT_CLOSURE_MATCHES.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader()
    for k in sorted(idd,key=lambda x:(int(x[0]),int(x[1]))): w.writerow({f:idd[k][f] for f in fields})
print(json.dumps(summary,indent=2))
