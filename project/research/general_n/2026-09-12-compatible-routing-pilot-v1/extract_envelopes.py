#!/usr/bin/env python3
"""Remove LP normalization and variable-bound rows from successful witnesses."""
from collections import Counter
from pathlib import Path
import json
from model import build
from evidence_io import read_records
HERE=Path(__file__).resolve().parent

def extract(rec,attempt):
    model=build(rec,attempt['h'],attempt['j'],attempt['mode']);cert=attempt['certificate']
    coefficients=[0]*len(model['names']);constant=0;weights=[]
    for kind in ('ub','eq'):
        for index,w in cert[kind]:
            row=model[kind][index]
            if row['name'][0] in ('source_count','high_sender_count','count_cap'):continue
            weights.append([kind,row['name'],w]);constant+=w*row['rhs']
            for col,c in row['coefficients'].items():coefficients[col]-=w*c
    best={}
    h,j=attempt['h'],attempt['j']
    for opt,cost in zip(model['names'],coefficients):
        key=(opt[0],int(opt[3]>h));best[key]=max(best.get(key,cost),cost)
    low=[];differences=[]
    for rv,n in sorted(Counter(rec['rho']).items()):
        if (rv,0) not in best:continue
        low.extend([best[rv,0]]*n)
        if (rv,1) in best:differences.extend([best[rv,1]-best[rv,0]]*n)
    assert len(differences)>=j
    maximum=sum(low)+sum(sorted(differences,reverse=True)[:j]);gap=-constant-maximum
    assert gap>0,(rec['layer'],rec['state_id'],h,j,attempt['mode'],gap)
    return dict(h=h,j=j,mode=attempt['mode'],weights=weights,constant=constant,
        local_class_maxima=[[rv,e,v] for (rv,e),v in sorted(best.items())],maximum_with_j_high=maximum,gap=gap)

def main():
    recs={(r['layer'],r['state_id']):r for r in json.loads((HERE/'pilot_inputs.json').read_text())['sample']}
    results=read_records('pilot_results.jsonl')
    out=[]
    for result in results:
        rec=recs[result['layer'],result['state_id']]
        for ai,attempt in enumerate(result['attempts']):
            if not attempt['certificate']:continue
            env=extract(rec,attempt);env.update(layer=rec['layer'],state_id=rec['state_id'],attempt_index=ai);out.append(env)
    (HERE/'envelopes.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(dict(exact_envelopes=len(out),all_positive_gaps=True,minimum_gap=min(r['gap'] for r in out),
                         no_LP_normalization_or_variable_bound_rows=True)))

if __name__=='__main__':main()
